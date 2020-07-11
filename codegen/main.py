import json
from dataclasses import dataclass, field, asdict
from typing import List
from argparse import Namespace

missing = dict()
missing_sorted = dict()
value_examples = []


class Node:
    def iterate(self, fun, *args, **kwargs):
        fun(self, *args, **kwargs)

        for name, attr in asdict(self).items():
            if isinstance(attr, list) and len(attr) > 0 and hasattr(attr[0], 'iterate'):
                for item in attr:
                    item.iterate(fun, *args, **kwargs)

            elif hasattr(attr, 'iterate'):
                attr.iterate(fun, *args, **kwargs)

def safe_ctor(ctor, kwargs):
    exception = True

    if not isinstance(kwargs, dict):
        return kwargs

    while exception:
        try:
            self = ctor(**kwargs)
            exception = False

        except TypeError as error:
            exception = error
            msg: str = error.args[0]

            start = msg.find("'")
            end = msg.rfind("'")

            name = msg[start + 1:end]
            val = kwargs.pop(name)

            ctor_name = ctor.__name__
            if (ctor_name, name) not in missing:
                # print(f'{ctor_name}_{name}: {type(val).__name__} = None')
                missing[(ctor_name, name)] = val

                if ctor_name not in missing_sorted:
                    missing_sorted[ctor_name] = []

                missing_sorted[ctor_name].append((name, val))

    return self

@dataclass
class Value(Node):
    val: Namespace = None

    @staticmethod
    def from_dict(kwargs):
        if not isinstance(kwargs, dict):
            return kwargs

        new_kwargs = dict()
        for k, v in kwargs.items():
            if k[0] == '$':
                new_kwargs[k[1:]] = v
            else:
                new_kwargs[k] = v

        # Value can hold anything we cannot
        # create a struct for it
        # safe_ctor(Value, new_kwargs)
        self = Value()
        self.val = Namespace(**new_kwargs)
        value_examples.append(self)
        return self

    def to_json(self):
        value = dict(Expression='Value')
        value.update(**vars(self.val))
        return value

    def generate(self):
        rep = repr(self.val)
        return rep


@dataclass
class Field(Node):
    Name: str = ''
    Value: Value = None
    PinType: 'Type' = None
    PropertyFlags: int = 0

    @staticmethod
    def from_dict(kwargs):
        if not isinstance(kwargs, dict):
            return kwargs

        self = safe_ctor(Field, kwargs)
        self.PinType = Type.from_dict(self.PinType)
        self.Value = Value.from_dict(self.Value)
        return self

    def generate(self, state=None):
        val = ''

        if isinstance(self.Value, Value):
            val = f' = {self.Value.generate()}'

        elif self.Value is not None and isinstance(self.Value, str) and '/' in self.Value:
            val = f' = NewObject[{Type.object_from_path(self.Value)}]()'

        elif self.Value is not None:
            val = f' = {self.Value}'

        vtype = ''
        if self.PinType:
            cpp_type = self.PinType.type(state)
            if cpp_type[-1] == '*':
                cpp_type = f'Ptr[{cpp_type[:-1]}]'

            vtype = f': {cpp_type}'

        correct_name = self.Name.replace(' ', '_')
        return f'{correct_name}{vtype}{val}'


@dataclass
class Argument(Node):
    Name: str = ''
    PinType: 'Type' = None

    @staticmethod
    def from_dict(kwargs):
        if not isinstance(kwargs, dict):
            return kwargs

        self =  safe_ctor(Argument, kwargs)
        self.PinType = Type.from_dict(self.PinType)
        return self

    def generate(self, state=None):
        return f'{self.Name}: {self.PinType.type(state)}'


@dataclass
class Type(Node):
    PinCategory: str = None
    PinSubCategory: str = None
    PinSubCategoryObject: str = None
    ContainerType: int = None
    IsWeakPointer: bool = False
    PinValueType: 'Type' = None

    IsConst: bool = False
    IsReference: bool = False

    TerminalSubCategory: str = None
    TerminalIsConst: bool = None
    TerminalIsWeakPointer: bool = None
    TerminalCategory: str = None
    TerminalSubCategoryObject: str = None

    @staticmethod
    def from_dict(kwargs):
        if not isinstance(kwargs, dict):
            return kwargs

        self = safe_ctor(Type, kwargs)
        self.PinValueType = Type.from_dict(self.PinValueType)
        return self

    def type(self, state=None):
        base = Type.get_type(self.PinCategory, Type.object_from_path(self.PinSubCategoryObject, state), Type.IsWeakPointer)

        if base[-1] == '*':
            base = f'Ptr[{base[:-1]}]'

        if self.ContainerType == 1:
            base = f'List[{base}]'

        elif self.ContainerType == 2:
            base = f'Set[{base}]'

        elif self.ContainerType == 3:
            value_object = self.PinValueType
            value_type = Type.get_type(
                value_object.TerminalCategory,
                Type.object_from_path(value_object.TerminalSubCategoryObject, state),
                value_object.IsWeakPointer)

            if value_object.IsConst:
                value_type = f'Const[{value_type}]'

            base = f'Dict[{base}, {value_type}]'

        if self.IsReference:
            base = f'Ref[{base}]'

        if self.IsConst:
            base = f'Const[{base}]'

        return base

    @staticmethod
    def get_type(cat: str, subcatobj, is_weak):
        cat = cat.lower()
        if cat == 'interface':
            return f'TScriptInterface[{subcatobj}]'

        if cat == 'class':
            return f'TSubclassOf[{subcatobj}]'

        if cat == 'softclass':
            return f'TSoftClassPtr[{subcatobj}]'

        if cat == 'softobject':
            return f'TSoftObjectPtr[{subcatobj}]'

        if cat == 'object':
            if is_weak:
                return f'TWeakObjectPtr[{subcatobj}]'
            return f'{subcatobj}*'

        if cat == 'struct':
            return subcatobj

        mapping = dict(
            float='float',
            int64='int64',
            int='int32',
            byte='uint8',
            name='FName',
            bool='bool',
            string='FString',
            text='FText',
            delegate='FScriptDelegate',
            mcdelegate='FMulticastScriptDelegate'
        )

        return mapping.get(cat, f'$BAD_TYPE({cat})')

    @staticmethod
    def object_from_path(original_path: str, state: 'FunctionGenerationState' = None):
        path = original_path
        if not path:
            return ''

        if path.endswith('_C'):
            path = path[:-2]

        idx = path.find(':')
        if idx == -1:
            idx = path.find('.')

        object = path[idx + 1:]

        if '.' in original_path and state is not None and state.BPState is not None:
            import_path = original_path.split(' ')[-1]

            path_stop = import_path.find('.')
            start = 0
            if import_path[0] == '/':
                start = 1

            file_path = import_path[start:path_stop]
            # Object was replaced with something else
            if object not in state.ReplaceCall:
                state.BPState.imports.append((file_path.replace('/', '.'), object))

        return object


@dataclass
class Instruction(Node):
    Params: List['Instruction'] = field(default_factory=list)
    Instruction: str = ''
    InstOffsetFromTop: int = 0
    LocalProp: str = ''
    EvaluateProp: Instruction = None
    EvaluateExp: Instruction = None
    VarName: str = ''
    VarType: Type = None
    Context: Instruction = None
    Skip: bool = False
    ValProp: str = None
    ValSize: int = 0
    Code: 'Instruction' = None
    Dest: int = 0
    Value: str = None
    Function: str = None
    FunctionParamOut: str = None
    FunctionParamName: str = None
    Condition: Instruction = None
    Castee: Instruction = None
    MetaClass: str = None

    Type: str = None
    Offset: int = None
    Size: int = None

    # Text
    SrcStr: str = None
    StringTable: str = None
    KeyStr: str = None
    OffsetToNextCase: int = None

    Namespace: Instruction = None  # {'Instruct
    TableIDStr: Instruction = None  # {'Instruct
    Index: Instruction = None  # {'Instruct
    Signature: str = None  # 'Function
    Num: int = None  # 0

    @staticmethod
    def from_dict(kwargs):
        if not isinstance(kwargs, dict):
            return kwargs

        self = safe_ctor(Instruction, kwargs)

        self.EvaluateProp = Instruction.from_dict(self.EvaluateProp)
        self.EvaluateExp = Instruction.from_dict(self.EvaluateExp)
        self.Code = Instruction.from_dict(self.Code)

        self.Namespace = Instruction.from_dict(self.Namespace)
        self.TableIDStr = Instruction.from_dict(self.TableIDStr)
        self.Index = Instruction.from_dict(self.Index)

        self.Value = Instruction.from_dict(self.Value)
        self.Key = Instruction.from_dict(self.Key)

        if self.Condition:
            self.Condition = Instruction.from_dict(self.Condition)

        if self.Params:
            self.Params = [Instruction.from_dict(param) for param in self.Params]

        if self.Values:
            self.Values = [Instruction.from_dict(val) for val in self.Values]

        self.Interface = Instruction.from_dict(self.Interface)

        self.Input = Instruction.from_dict(self.Input)
        self.Default = Instruction.from_dict(self.Default)
        self.Match = Instruction.from_dict(self.Match)
        self.Result = Instruction.from_dict(self.Result)

        self.Delegate = Instruction.from_dict(self.Delegate)
        self.Variable = Instruction.from_dict(self.Variable)
        self.Offset = Instruction.from_dict(self.Offset)

        if self.Cases:
            self.Cases = [Instruction.from_dict(param) for param in self.Cases]

        if isinstance(self.Context, dict):
            self.Context = Instruction.from_dict(self.Context)

        self.VarType = Type.from_dict(self.VarType)
        self.Set = Instruction.from_dict(self.Set)
        self.Array = Instruction.from_dict(self.Array)
        self.Map = Instruction.from_dict(self.Map)
        self.Object = Instruction.from_dict(self.Object)
        self.Castee = Instruction.from_dict(self.Castee)

        return self

    def unsupported(self, *args, **kwargs):
        return f'$UNSUPPORTED({self.Instruction})'

    def generate(self, state, obj, IsAssignmentLeftSide: bool = False, body=None):
        dispatcher = {
            'EX_Nothing': self.nothing,
            'EX_Assert': self.cassert,
            'EX_Return': self.retinst,
            'EX_EndOfScript': self.nothing,
            'End': self.end_inline,

            # Variables
            'EX_LocalVariable': self.new_variable,
            'EX_LocalOutVariable': self.new_variable,

            'EX_InstanceVariable': self.getattr,
            'EX_DefaultVariable': self.getattr,
            'EX_StructMemberContext': self.getmember,

            # Binding to var
            'EX_Let': self.let,
            'EX_LetBool': self.let,
            'EX_LetMulticastDelegate': self.let,
            'EX_LetDelegate': self.let,
            'EX_LetObj': self.let,
            'EX_LetWeakObjPtr': self.let,
            'EX_LetValueOnPersistentFrame': self.let_value,

            # Context
            'EX_Context': self.context,
            'EX_Context_FailSilent': self.context,
            'EX_ClassContext': self.class_context,
            'EX_InterfaceContext': self.interface_context,

            # Calls
            'EX_FinalFunction': self.function_call,
            'EX_LocalFinalFunction': self.function_call,
            'EX_VirtualFunction': self.function_call,
            'EX_LocalVirtualFunction': self.function_call,
            'EX_CallMath': self.builtin_function_call,
            'EX_CallMulticastDelegate': self.multicast_call,

            # Constants / Values
            'EX_Self': self.get_self,

            'EX_IntConst': self.value,
            'EX_FloatConst': self.value,
            'EX_ByteConst': self.value,
            'EX_IntConstByte': self.value,
            'EX_Int64Const': self.value,
            'EX_UInt64Const': self.value,
            'EX_SkipOffsetConst': self.value,
            'EX_StringConst': self.value_str,
            'EX_NameConst': self.value_str,
            'EX_UnicodeStringConst': self.value_str,
            'EX_TextConst': self.text_const,
            'EX_StructConst': self.struct_const,
            'EX_SoftObjectConst': self.softobject_const,

            'EX_ObjectConst': self.object_const,
            'EX_VectorConst': self.vector_const,
            'EX_RotationConst': self.rotation_const,

            'EX_IntOne': self.int_one,
            'EX_IntZero': self.int_zero,
            'EX_True': self.true,
            'EX_False': self.false,

            'EX_NoObject': self.none,
            'EX_NoInterface': self.none,

            'EX_TransformConst': self.transform_const,

            # Casting
            'EX_MetaCast': self.meta_cast,
            'EX_DynamicCast': self.dynamic_cast,
            'EX_PrimitiveCast': self.primitive_cast,
            'EX_ObjToInterfaceCast': self.object_interface_cast,
            'EX_CrossInterfaceCast': self.cross_interface_cast,
            'EX_InterfaceToObjCast': self.interface_object_cast,

            # Containers
            'EX_SetArray': self.set_array,
            'EX_ArrayConst': self.array_const,
            'EX_SetSet': self.set_set,
            'EX_SetConst': self.set_const,
            'EX_ArrayGetByRef': self.array_get_by_ref,

            'EX_SetMap': self.set_map,
            'EX_MapConst': self.map_const,

            # MultiCast
            'EX_AddMulticastDelegate': self.add_multicast,
            'EX_RemoveMulticastDelegate': self.remove_multicast,
            'EX_ClearMulticastDelegate': self.clear_multicast,
            'EX_InstanceDelegate': self.instance_delegate,
            'EX_BindDelegate': self.bind_delegate,

            # Branching
            'EX_SwitchValue': self.switch,
            'EX_Jump': self.jump,
            'EX_JumpIfNot': self.jump_if_not,
            'EX_PushExecutionFlow': self.push_exec,
            'EX_PopExecutionFlow': self.pop_exec,
            'EX_PopExecutionFlowIfNot': self.pop_exec_if_not,
            'EX_ComputedJump': self.computed_jump

        }

        handler = dispatcher.get(self.Instruction, self.unsupported)
        return handler(state, obj, IsAssignmentLeftSide, body=body)

    def jump(self, state: 'FunctionGenerationState', obj, *args, **kwargs):
        offset = self.Offset

        # print(state.LastExpression)
        # code = f"""if {state.LastExpression}:
        # |            goto('L{offset}')""".replace('        |', '')
        return f"goto('L{offset}')"

    def jump_if_not(self, state, obj, *args, **kwargs):
        offset = self.Offset
        condition = self.Condition.generate(state, state.Object, **kwargs)

        if condition.startswith('!'):
            condition = condition[1:]
        condition = f'not {condition}'

        code = f"""if {condition}:
        |            goto('L{offset}')""".replace('        |', '')
        return code

    def computed_jump(self, state, obj, *args, **kwargs):
        target = self.Offset.generate(state, state.Object, **kwargs)
        return f'goto(ComputedJump("{target}"))'

    def pop_exec(self, state, obj, *args, **kwargs):
        return 'goto(ExecutionFlow.Pop())'

    def push_exec(self, state, obj, *args, **kwargs):
        offset = self.Offset
        return f'ExecutionFlow.Push("L{offset}")'

    def pop_exec_if_not(self, state, obj, *args, **kwargs):
        condition = self.Condition.generate(state, state.Object, **kwargs)

        if condition.startswith('!'):
            condition = condition[1:]
        condition = f'not {condition}'

        code = f"""if {condition}:
        |           goto(ExecutionFlow.Pop())""".replace('        |', '')
        return code


    Variable: Instruction = None
    Delegate: Instruction = None

    def add_multicast(self, state, obj, *args, **kwargs):
        variable = self.Variable.generate(state, state.Object, **kwargs)
        bound = self.Delegate.generate(state, state.Object, **kwargs)
        return f'{variable}.AddUnique({bound})'

    def remove_multicast(self, state, obj, *args, **kwargs):
        variable = self.Variable.generate(state, state.Object, **kwargs)
        bound = self.Delegate.generate(state, state.Object, **kwargs)
        return f'{variable}.Remove({bound})'

    def clear_multicast(self, state, obj, *args, **kwargs):
        if self.Variable is not None:
            variable = self.Variable.generate(state, state.Object)
        else:
            variable = self.Delegate.generate(state, state.Object)

        return f'{variable}.Clear()'

    Object: Instruction = None

    def bind_delegate(self, state, obj, *args, **kwargs):
        variable = self.Variable.generate(state, state.Object)
        name = self.FunctionName
        bound = self.Object.generate(state, state.Object)
        return f'{variable}.BindUFunction({bound}, {name})'

    FunctionName: str = None

    def instance_delegate(self, state, obj, *args, **kwargs):
        name = self.FunctionName
        return f'{state.LastExpression}.BindUFunction({state.Object}, {name})'

    Input: Instruction = None
    Cases: List['Instruction'] = None
    Default: Instruction = None
    Match: Instruction = None
    Result: Instruction = None

    def switch(self, state: 'FunctionGenerationState', obj, *args, **kwargs):
        target = self.Input.generate(state, state.Object)
        default = self.Default.generate(state, state.Object)
        if default == 'Default':
            default = 'None'

        lines = []
        for case in self.Cases:
            match_val = case.Match.generate(state, state.Object)
            match_result = case.Result.generate(state, state.Object)
            lines.append(f'{match_val}: {match_result}')

        i = 0
        base_name = 'switch'
        switch_name = base_name
        while state.local_var_exist(switch_name):
            switch_name = f'{base_name}_{i}'
            i += 1

        state.LocalVariables[switch_name] = 1

        idt = '        '
        elems = f',\n    {idt}'.join(lines)
        dispatch = f"""{switch_name} = {{
        |    {elems}
        |}}""".replace('        |', idt)

        state.body.append('')
        state.body.append(dispatch)
        return f'{switch_name}.get({target}, {default})'

    def end_inline(self, *args, **kwargs):
        return '# End'

    Key: Instruction = None
    KeyType: str = None
    # Value: Instruction = None
    ValueType: str = None

    def _map_literal(self, state):
        values = []
        for arg in self.Values:
            key_val = arg.Key.generate(state, state.Object)
            val_val = arg.Value.generate(state, state.Object)
            values.append(f'{key_val}: {val_val}')

        values = ', '.join(values)
        return f'{{{values}}}'

    Set: Instruction = None
    Map: Instruction = None

    def map_const(self, state, obj, *args, **kwargs):
        map_type = f'Dict[{self.KeyType}, {self.ValueTYpe}]'
        literal = self._array_literal(state)
        return f'{map_type}({literal})'

    def set_map(self, state, obj, *args, **kwargs):
        map_inst = self.Map.generate(state, state.Object, True)
        literal = self._map_literal(state)
        # ?
        return f'{map_inst} = {literal}'

    def set_const(self, state, obj, *args, **kwargs):
        set_type = self.Type
        literal = self._array_literal(state)
        return f'Set[{set_type}]({literal})'

    def set_set(self, state, obj, *args, **kwargs):
        set_inst = self.Set.generate(state, state.Object, True)
        literal = self._array_literal(state)
        # ?
        return f'{set_inst} = {literal}'

    Array: Instruction = None

    def _array_literal(self, state, **kwargs):
        values = []
        for arg in self.Values:
            arg_val = arg.generate(state, state.Object)
            values.append(arg_val)

        values = ', '.join(values)
        return f'[{values}]'

    def set_array(self, state, obj, *args, **kwargs):
        array_inst = self.Array.generate(state, state.Object, True)
        literal = self._array_literal(state)
        # ?
        return f'{array_inst} = {literal}'

    def array_const(self, state, obj, *args, **kwargs):
        array_type = self.Type
        literal = self._array_literal(state)
        return f'List[{array_type}]({literal})'

    def array_get_by_ref(self, state, obj, *args, **kwargs):
        var = self.Variable.generate(state,  state.Object)
        index = self.Index.generate(state, state.Object)
        return f'{var}[{index}]'

    Struct: str = None
    Values: List['Instruction'] = field(default_factory=list)
    StructPropName: str = None

    def struct_const(self, state, obj, *args, **kwargs):
        name = Type.object_from_path(self.Struct, state)
        args = []
        for arg in self.Value:
            # FIXME
            if isinstance(arg, dict):
                arg = Instruction.from_dict(arg)

            val = arg.generate(state, state.Object)
            args.append(f'{arg.StructPropName} = {val}')

        args = ', '.join(args)
        return f'{name}({args})'

    def softobject_const(self, state, obj, *args, **kwargs):
        value = self.Value.generate(state, state.Object)
        return f'SoftObjectPath({value})'

    def cross_interface_cast(self, state, obj, *args, **kwargs):
        value = self.Value.generate(state, state.Object)
        type = Type.object_from_path(self.Type, state)
        return f'InterfaceCast[{type}]({value})'

    def interface_object_cast(self, state, obj, *args, **kwargs):
        value = self.Value.generate(state, state.Object)
        type = Type.object_from_path(self.Type, state)
        return f'Cast[{type}]({value})'

    Cast: int = 0

    def primitive_cast(self, state, obj, *args, **kwargs):
        cast_val = self.Value.generate(state, state.Object)
        cast_kind = self.Cast

        if cast_kind == 70:
            # Instruction = EX_ObjToInterfaceCast
            type = Type.object_from_path(self.Type, state)
            return f'QueryInterface[{type}]({cast_val})'

        return cast_val

    def object_interface_cast(self, state, obj, *args, **kwargs):
        cast_val = self.Value.generate(state, state.Object)
        type = Type.object_from_path(self.Type, state)
        return f'QueryInterface[{type}]({cast_val})'

    def dynamic_cast(self, state, obj, *args, **kwargs):
        cast_class =  Type.object_from_path(self.Type, state)
        cast_expr = self.Code.generate(state, obj, *args)
        return f'Cast[{cast_class}]({cast_expr})'

    # Transform
    RotX: float = 0
    RotY: float = 0
    RotZ: float = 0
    RotW: float = 0
    TransX: float = 0
    TransY: float = 0
    TransZ: float = 0
    ScaleX: float = 0
    ScaleY: float = 0
    ScaleZ: float = 0

    def transform_const(self, state, obj, *args, **kwargs):
        rotator = f'Rotator({self.RotX}, {self.RotY}, {self.RotZ}, {self.RotW})'
        translate = f'Vector({self.TransX}, {self.TransY}, {self.TransZ})'
        scale = f'Vector({self.ScaleX}, {self.ScaleY}, {self.ScaleZ})'
        return f'Transform({rotator}, {translate}, {scale})'

    def none(self, *args, **kwargs):
        return "None"

    def text_const(self, *args, **kwargs):
        type = self.Type
        if type == 0:
            return ''

        if type in (1, 2, 3):
            return f'"{self.SrcStr}"'

        return f'STRING_TABLE_ENTRY("{self.StringTable}", "{self.KeyStr}"'

    def int_one(self, *args, **kwargs):
        return "1"

    def int_zero(self, *args, **kwargs):
        return "0"

    def true(self, *args, **kwargs):
        return "True"

    def false(self, *args, **kwargs):
        return "False"

    # Rotation
    Pitch: float = 0
    Yaw: float = 0
    Roll: float = 0

    def rotation_const(self, state, obj, *args, **kwargs):
        return f'Rotator::FromPitchYawRoll({self.Pitch}, {self.Yaw}, {self.Roll})'

    # Vector
    X: float = 0
    Y: float = 0
    Z: float = 0

    def vector_const(self, state, obj, *args, **kwargs):
        return f'Vector({self.X}, {self.Y}, {self.Z})'

    def object_const(self, state, obj, *args, **kwargs):
        name = Type.object_from_path(self.Value, state)
        # if name.startswith('Default__'):
        #    name = name[9:]
        return name

    def get_self(self, state, obj, *args, **kwargs):
        return obj

    def meta_cast(self, state, obj, *args, **kwargs):
        class_inst = self.Castee.generate(state, obj, *args)
        meta_class = Type.object_from_path(self.MetaClass, state)
        return f'ClassCast[{meta_class}]({class_inst})'

    def class_context(self, state, obj, *args, **kwargs):
        ctx_inst = self.Context.generate(state, obj)
        accessor = f'{ctx_inst}.ClassDefaultObject'
        return self.Code.generate(state, accessor)

    Interface: Instruction = None

    def interface_context(self, state, obj, *args, **kwargs):
        interface = self.Interface.generate(state, obj)
        return f'GetInterfaceUObject({interface})'

    def nothing(self, *args, **kwargs):
        return ''

    def cassert(self, state, *args, **kwargs):
        inst = self.Condition.generate(state, state.Object)
        return f'assert({inst})'

    def value(self, *args, **kwargs):
        return str(self.Value)

    def value_str(self, *args, **kwargs):
        return f'"{self.Value}"'

    def _gen_call_args(self, state, **kwargs):
        lines = []
        outputs = []

        for arg in self.Params:
            arg_res =  arg.generate(state, state.Object, **kwargs)

            if arg.FunctionParamOut:
                # arg_res = f'Ref[{arg_res}]'
                outputs.append(arg_res)
            else:
                # if 'ScriptStruct' in arg_res:
                #   print(arg)
                # print(arg_res)
                lines.append(arg_res)

        return outputs, lines

    def multicast_call(self, state, obj, *args, **kwargs):
        obj = self.Variable.generate(state, obj, *args, **kwargs)
        outputs, args = self._gen_call_args(state)

        if outputs:
            out_args = [f'Ref[{o}]' for o in outputs]
            args.extend(out_args)

        args = ', '.join(args)
        return f'{obj}.ProcessMulticastDelegate({args})'

    def builtin_function_call(self, *args, **kwargs):
        return self.function_call(*args, builtin=True, **kwargs)

    def function_call(self, state: 'FunctionGenerationState', obj, *_, builtin=False, **kwargs):
        funName = Type.object_from_path(self.Function, state)

        raw_out, raw_args = self._gen_call_args(state)

        if raw_out:
            state.body.append('')
            define_outs = [f'{o} = None' for o in raw_out if not state.local_var_exist(o)]
            state.body.extend(define_outs)

        out_args = []
        if raw_out:
            out_args = [f'Ref[{o}]' for o in raw_out]

        final_args = raw_args + out_args

        replaced = state.ReplaceCall.get(funName)
        if replaced:
            try:
                return replaced(*final_args)
            except:
                print(final_args)

        if not builtin:
            args = ', '.join(final_args)
            return f'{obj}.{funName}({args})'

        args = ', '.join(final_args)
        return f'{funName}({args})'

    def context(self, state, *args, **kwargs):
        ctx_inst = self.Context.generate(state, state.Object, **kwargs)
        return self.Code.generate(state, ctx_inst)

    def let_value(self, state, *args, **kwargs):
        value = self.Value.generate(state, state.Object, **kwargs)
        prop = Type.object_from_path(self.Dest, state)

        return f'{prop} = {value} #  PERSISTENT_FRAME('

    def let(self, state, *args, **kwargs):
        prop = self.EvaluateProp
        prop_inst = prop.generate(state, state.Object, True, **kwargs)
        value_inst = self.EvaluateExp.generate(state, state.Object, **kwargs)

        # if '/' in value_inst:
        #    print(value_inst, self.EvaluateExp)
        # state.DelayedBinds[prop_inst] = value_inst
        return f'{prop_inst} = {value_inst}'

    def retinst(self, *args, **kwargs):
        return 'return'

    def getattr(self, state, obj, *args, **kwargs):
        return f'{obj}.{self.VarName.replace(" ", "_")}'

    def getmember(self, state, *args, **kwargs):
        value = self.Code.generate(state, state.Object, **kwargs)
        prop_name = self.Context
        return f'{value}.{prop_name.replace(" ", "_")}'

    def new_variable(self, state, obj, IsAssignmentLeftSide, **kwargs):
        name = state.get_rename(self.VarName, None)

        if name is None:
            # name was not renamed, rename it to a shorter name for readability
            name = self.VarName
            base_name = name.split('_')[-1]
            name = base_name
            i = 0
            while state.local_var_exist(name):
                name = f'{base_name}_{i}'
                i += 1

            state.RenamedLocalVariables[self.VarName] = name

        if IsAssignmentLeftSide and not state.local_var_exist(name):
            state.LocalVariables[name] = True
            return f'{name}: {self.VarType.type(state)}'

        #if name in state.DelayedBinds:
        #    return state.DelayedBinds[name]

        return name



def add(*args, **kwargs):
    return ' + '.join(args)

def mult(*args, **kwargs):
    return ' * '.join(args)

def sub(*args, **kwargs):
    return ' - '.join(args)

def divide(x, y, **kwargs):
    return f'{x} / {y}'

def gt(x, y, **kwargs):
    return f'{x} > {y}'

def gte(x, y, **kwargs):
    return f'{x} >= {y}'

def lte(x, y, **kwargs):
    return f'{x} <= {y}'

def lt(x, y, **kwargs):
    return f'{x} < {y}'

def neq(x, y, **kwargs):
    return f'{x} != {y}'

def BreakVector(vector, x, y, z, **kwargs):
    return f'{x[4:-1]}, {y[4:-1]}, {z[4:-1]} = BreakVector({vector})'

def getitem(idx, array, item, **kwargs):
    return f'{item[4:-1]} = {array[4:-1]}[{idx}]'

def additem(array, item, **kwargs):
    return f'{array[4:-1]}.append({item[4:-1]})'

def getlastindex(array, **kwargs):
    return f'len({array[4:-1]}) - 1'

def getlen(array, **kwargs):
    return f'len({array[4:-1]})'

def removeindex(index, array, **kwargs):
    return f'{array[4:-1]}.remove({index})'


ReplaceCall = {
    'Add_FloatFloat': add,
    'Add_IntInt': add,
    'Add_VectorVector': add,
    'MakeVector2D': lambda x, y, **kwargs: f'Vector2D({x}, {y})',
    'Greater_FloatFloat': gt,
    'Greater_IntInt': gt,
    'Divide_FloatFloat': divide,
    'BooleanAND': lambda x, y, **kwargs: f'{x} and {y}',
    'MakeVector': lambda x, y, z, **kwargs: f'Vector({x}, {y}, {z})',
    'Multiply_VectorFloat': mult,
    'Multiply_FloatFloat': mult,
    'Multiply_IntInt': mult,
    'Multiply_IntFloat': mult,
    'NotEqual_IntInt': neq,
    'Subtract_IntInt': sub,
    'Subtract_FloatFloat': sub,
    'LessEqual_IntInt': lte,
    'Less_IntInt': lte,
    'Less_FloatFloat': lte,
    'LessEqual_FloatFloat': lte,
    'BreakVector': BreakVector,
    'Array_Get': getitem,
    'Array_LastIndex': getlastindex,
    'Array_Length': getlen,
    'Array_Remove': removeindex,
    'Array_Add': additem
}

@dataclass
class FunctionGenerationState:
    LocalVariables: dict = field(default_factory=dict)
    RenamedLocalVariables: dict =field(default_factory=dict)
    UsedVariableNames: dict = field(default_factory=dict)
    Object: str = 'self'
    LastExpression: str = '$INVALID_EXPRESSION$'
    body: List = field(default_factory=list)
    ReplaceCall: dict = field(default_factory=lambda: ReplaceCall)
    DelayedBinds = dict()
    BPState = None

    def get_rename(self, name, default=None):
        return self.RenamedLocalVariables.get(name, default)

    def local_var_exist(self, name):
        return name in self.LocalVariables or name in self.RenamedLocalVariables


@dataclass
class Function(Node):
    Name: str = None
    Arguments: List[Argument] = field(default_factory=list)
    Outputs: List = field(default_factory=list)
    Access: str = None
    FunctionFlags: int = None
    Code: List[Instruction] = field(default_factory=list)
    SuperClass: str = None
    IsOverride: bool = None
    Static: bool = None

    @staticmethod
    def from_dict(kwargs):
        if not isinstance(kwargs, dict):
            return kwargs

        self = safe_ctor(Function, kwargs)
        self.Arguments = [Argument.from_dict(arg) for arg in self.Arguments]
        self.Code = [Instruction.from_dict(inst) for inst in self.Code if inst is not None]

        return self


    def find_used_labels(self, used_labels):
        for node in self.Code:
            if hasattr(node, 'Instruction') and node.Instruction in ('EX_Jump', 'EX_JumpIfNot', 'EX_PushExecutionFlow'):
                used_labels[node.Offset] = 1

    def generate(self, fields, bp_state, used_labels, depth=1):
        state = FunctionGenerationState()
        state.BPState = bp_state

        for field in fields:
            state.LocalVariables['self.' + field.Name] = True

        lines = []
        state.body = lines
        for instruction in self.Code:
            code = instruction.generate(state, state.Object)
            state.LastExpression = code
            if instruction.InstOffsetFromTop in used_labels:
                lines.append(f'# Label {instruction.InstOffsetFromTop}')
            lines.append(code)

        body = f'\n{"    " * (depth + 1)}'.join(lines)
        state.body = []

        lines = ['self']
        for arg in self.Arguments:
            code = arg.generate()
            lines.append(code)
        args = ', '.join(lines)

        if not body:
            body = 'pass'

        code = f"""
        |def {self.Name}({args}):
        |    {body}
        |""".replace('        |', '    ' * depth)

        return code


@dataclass
class BlueprintState:
    imports: List = field(default_factory=list)

    @property
    def BPState(self):
        return self

    @property
    def ReplaceCall(self):
        return ReplaceCall

@dataclass
class Blueprint:
    Blueprint: str = ''
    ParentClass: str = ''
    BlueprintKind: str = ''
    WidgetTreeRootWidget: dict = field(default_factory=dict)
    NamedSlots: list = field(default_factory=list)
    Fields: List[Field] = field(default_factory=list)
    Functions: List[Function] = field(default_factory=list)

    ConstructionScript: str = None

    ImplementedInterfaces: list = None  # ['/Script/FactoryGame.FGActorRepresentat
    DynamicBindings: list = None  # [{'Type': 'Component', 'Bindings': [{'Co
    TargetSkeleton: dict = None  # {'$AssetPath': '/Game/FactoryGame/Builda

    @staticmethod
    def from_dict(kwargs):
        if not isinstance(kwargs, dict):
            return kwargs

        self = safe_ctor(Blueprint, kwargs)
        self.Fields = [Field.from_dict(field) for field in self.Fields]
        self.Functions = [Function.from_dict(fun) for fun in self.Functions]
        return self

    def generate(self, depth=0):
        lines = []
        bp_state = BlueprintState()

        for field in self.Fields:
            lines.append(field.generate(bp_state))
        fields = '\n    '.join(lines)


        used_labels = dict()
        for fun in self.Functions:
            lines.append(fun.find_used_labels(used_labels))

        lines = []
        for fun in self.Functions:
            lines.append(fun.generate(self.Fields, bp_state, used_labels, depth=depth + 1))
        funs = '\n'.join(lines)


        name = Type.object_from_path(self.Blueprint)
        parent_type = Type.object_from_path(self.ParentClass, bp_state)

        imports = []
        for path, obj in set(bp_state.imports):
            imports.append(f'from {path} import {obj}')
        imports = '\n'.join(imports)

        code = f"""
        |from codegen.ue4_stub import *
        |
        |{imports}
        |
        |class {name}({parent_type}):
        |    {fields}
        |    {funs}
        |""".replace('        |', '')

        return code



def main(filename, outdir):
    from subprocess import check_call

    with open(filename, 'rb') as file:
        decoded_pak = json.loads(file.read().decode('utf-8-sig'))

    blueprints: list = decoded_pak['Blueprints']

    blueprints = blueprints[2:]

    for kwargs in blueprints:
        bp = Blueprint.from_dict(kwargs)

        try:
            code = bp.generate()
        except:
            import traceback
            print(bp.Blueprint)
            print(traceback.format_exc())
            continue

        path, name = bp.Blueprint.split('.', maxsplit=1)
        if path[0] == '/':
            path = path[1:]

        # shave one folder
        folders = path.split('/')
        name = folders[-1]
        path = os.path.join(*folders[:-1])

        inpath = path
        path = os.path.join(outdir, path)
        os.makedirs(path, exist_ok=True)
        filepath = os.path.join(path, f'{name}.py')

        with open(filepath, 'wb') as bpfile:
            bpfile.write(code.encode('utf-8-sig'))

        # make sure everything is a python module
        start_path = outdir
        for p in inpath.split('/'):
            start_path = os.path.join(start_path, p)

            module_init = os.path.join(start_path, '__init__.py')
            if not os.path.exists(module_init):
                with open(module_init, 'w') as f:
                    f.write(' ')

        # try:
        #     import sys
        #     print(check_call([sys.executable, '-m', 'black', filepath], shell=True))
        # except:
        #     pass


    for k, missings in missing_sorted.items():
        print(k)
        print('=' * 80)

        for k, v in missings:
            rep = repr(v)
            if len(rep) > 40:
                rep = rep[:40]

            print(f'{k}: {type(v).__name__} = None # {rep}')

    with open('values.json', 'w') as value_file:
        json.dump([v.to_json() for v in value_examples], value_file, indent=2)


if __name__ == '__main__':
    import os
    import sys
    sys.stderr = sys.stdout

    folder = os.path.dirname(__file__)
    main(os.path.join(folder, '..', 'FGBlueprints.json'),
         os.path.join(folder, '..'))