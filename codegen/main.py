import json
from dataclasses import dataclass, field
from typing import List


@dataclass
class Value:
    AssetPath: str = ''

    @staticmethod
    def from_dict(kwargs):
        if not isinstance(kwargs, dict):
            return kwargs

        asset = kwargs.pop('$AssetPath')
        self = Value(**kwargs)
        self.AssetPath = asset
        return self

    def generate(self):
        return 'Asset'


@dataclass
class Field:
    Name: str = ''
    Value: Value = None
    PinType: 'Type' = None
    PropertyFlags: int = 0

    @staticmethod
    def from_dict(kwargs):
        if not isinstance(kwargs, dict):
            return kwargs

        self = Field(**kwargs)
        self.PinType = Type.from_dict(self.PinType)
        self.Value = Value.from_dict(self.Value)
        return self

    def generate(self):
        val = ''
        if self.Value:
            val = f' = {self.Value.generate()}'

        vtype = ''
        if self.PinType:
            vtype = f': {self.PinType.type}'

        return f'{self.Name}{vtype}{val}'


@dataclass
class Argument:
    Name: str = ''
    PinType: 'Type' = None

    @staticmethod
    def from_dict(kwargs):
        if not isinstance(kwargs, dict):
            return kwargs

        self =  Argument(**kwargs)
        self.PinType = Type.from_dict(self.PinType)
        return self

    def generate(self):
        return f'{self.Name}: {self.PinType.type}'


@dataclass
class Type:
    PinCategory: str = ''
    PinSubCategory: str = ''
    PinSubCategoryObject: str = ''
    ContainerType: int = 0
    IsWeakPointer: bool = False
    PinValueType: 'Type' = None
    TerminalCategory: str = ''
    TerminalSubCategoryObject: str = ''
    IsConst: bool = False
    IsReference: bool = False

    @staticmethod
    def from_dict(kwargs):
        if not isinstance(kwargs, dict):
            return kwargs

        self = Type(**kwargs)
        self.PinValueType = Type.from_dict(self.PinValueType)
        return self

    @property
    def type(self):
        base = Type.get_type(self.PinCategory, Type.object_from_path(self.PinSubCategoryObject), Type.IsWeakPointer)

        if self.ContainerType == 1:
            base = f'TArray<{base}>'

        elif self.ContainerType == 2:
            base = f'TSet<{base}>'

        elif self.ContainerType == 3:
            value_object = self.PinValueType
            value_type = Type.get_type(
                value_object.TerminalCategory,
                Type.object_from_path(value_object.TerminalSubCategoryObject),
                value_object.IsWeakPointer)

            if value_object.IsConst:
                value_type = f'{value_type} const'

            base = f'TMap<{base}, {value_type}>'

        if self.IsReference:
            base = f'{base}&'

        if self.IsConst:
            base = f'{base} const'

        return base

    @staticmethod
    def get_type(cat: str, subcatobj, is_weak):
        cat = cat.lower()
        if cat == 'interface':
            return f'TScriptInterface<{subcatobj}>'

        if cat == 'class':
            return f'TSubclassOf<{subcatobj}>'

        if cat == 'softclass':
            return f'TSoftClassPtr<{subcatobj}>'

        if cat == 'softobject':
            return f'TSoftObjectPtr<{subcatobj}>'

        if cat == 'object':
            if is_weak:
                return f'TWeakObjectPtr<{subcatobj}>'
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
            string='Fstring',
            text='FText',
            delegate='FScriptDelegate',
            mcdelegate='FMulticastScriptDelegate'
        )

        return mapping.get(cat, f'$BAD_TYPE({cat})')

    @staticmethod
    def object_from_path(path: str):
        if not path:
            return ''

        if path.endswith('_C'):
            path = path[:-2]

        idx = path.find(':')
        if idx == -1:
            idx = path.find('.')

        return path[idx + 1:]


@dataclass
class Instruction:
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

    # Text
    SrcStr: str = None
    StringTable: str = None
    KeyStr: str = None
    OffsetToNextCase: int = None

    @staticmethod
    def from_dict(kwargs):
        if not isinstance(kwargs, dict):
            return kwargs

        self = Instruction(**kwargs)
        self.EvaluateProp = Instruction.from_dict(self.EvaluateProp)
        self.EvaluateExp = Instruction.from_dict(self.EvaluateExp)
        self.Code = Instruction.from_dict(self.Code)

        if isinstance(self.Value, dict):
            self.Value = Instruction.from_dict(self.Value)

        if self.Condition:
            self.Condition = Instruction.from_dict(self.Condition)

        if self.Params:
            self.Params = [Instruction.from_dict(param) for param in self.Params]

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

        if self.VarType:
            self.VarType = Type.from_dict(self.VarType)

        return self

    def unsupported(self, *args, **kwargs):
        return f'$UNSUPPORTED({self.Instruction})'

    def generate(self, state, obj, IsAssignmentLeftSide: bool = False):
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
            'EX_CallMath': self.function_call,
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
        return handler(state, obj, IsAssignmentLeftSide)

    def jump(self, state, obj, *args):
        offset = self.Offset
        return f'goto L{offset}'

    def jump_if_not(self, state, obj, *args):
        offset = self.Offset
        condition = self.Condition.generate(state, state.Object)

        if condition.starswith('!'):
            condition = condition[1:]
        condition = f'!{condition}'

        code = f"""if {condition}:
        |    goto L{offset}""".replace('        |', '')
        return code

    def computed_jump(self, state, obj, *args):
        target = self.Offset.generate(state, state.Object)
        return f'goto ComputedJump({target})'

    def pop_exec(self, state, obj, *args):
        return 'goto ExecutionFlowPop()'

    def push_exec(self, state, obj, *args):
        offset = self.Offset
        return f'ExecutionFlow.Push(L{offset})'

    def pop_exec_if_not(self, state, obj, *args):
        condition = self.Condition.generate(state, state.Object)

        if condition.starswith('!'):
            condition = condition[1:]
        condition = f'!{condition}'

        code = f"""if {condition}:
        |    goto ExecutionFlow.Pop()""".replace('        |', '')
        return code


    Variable: Instruction = None
    Delegate: Instruction = None

    def add_multicast(self, state, obj, *args):
        variable = self.Variable.generate(state, state.Object)
        bound = self.Delegate.generate(state, state.Object)
        return f'{variable}.AddUnique({bound})'

    def remove_multicast(self, state, obj, *args):
        variable = self.Variable.generate(state, state.Object)
        bound = self.Delegate.generate(state, state.Object)
        return f'{variable}.Remove({bound})'

    def clear_multicast(self, state, obj, *args):
        variable = self.Variable.generate(state, state.Object)
        return f'{variable}.Clear()'

    def bind_delegate(self, state, obj, *args):
        variable = self.Variable.generate(state, state.Object)
        name = self.FunctionName
        bound = self.Object.generate(state, state.Object)
        return f'{variable}->BindUFunction({bound}, {name})'

    FunctionName: str = None

    def instance_delegate(self, state, obj, *args):
        name = self.FunctionName
        return f'{state.LastExpression}->BindUFunction({state.Object}, {name})'

    Input: Instruction = None
    Cases: List['Instruction'] = None
    Default: Instruction = None
    Match: Instruction = None
    Result: Instruction = None

    def switch(self, state, obj, *args):
        target = self.Input.generate(state, state.Object)
        default = self.Default.generate(state, state.Object)

        lines = []
        for case in self.Cases:
            match_val = case.Match.generate(state, state.Object)
            match_result = case.Result.generate(state, state.Object)
            lines.append(f'case {match_val}: return {match_result}')

        idt = '        '
        cases = f'\n    {idt}'.join(lines)
        code = f"""swith {target} {{
        |    {cases}
        |    default: return {default}
        |}}""".replace('        |', idt)
        return code

    def end_inline(self, *args):
        return '# End'

    Key: Instruction = None
    KeyType: str = None
    # Value: Instruction = None
    ValueType: str = None

    def _map_literal(self, state):
        values = []
        for arg in self.Values:
            key_val = arg.Key.generate(state, state.object)
            val_val = arg.Value.generate(state, state.object)
            values.append(f'{key_val}: {val_val}')

        values = ', '.join(values)
        return f'{{{values}}}'

    def map_const(self, state, obj, *args):
        map_type = f'Map<{self.KeyType}, {self.ValueTYpe}>'
        literal = self._array_literal(state)
        return f'{map_type}(${literal})'

    def set_map(self, state, obj, *args):
        map_inst = self.Set.generate(state, state.object, True)
        literal = self._map_literal(state)
        # ?
        return f'{map_inst} = {literal}'

    def set_const(self, state, obj, *args):
        set_type = self.Type
        literal = self._array_literal(state)
        return f'Set<{set_type}>(${literal})'

    def set_set(self, state, obj, *args):
        set_inst = self.Set.generate(state, state.object, True)
        literal = self._array_literal(state)
        # ?
        return f'{set_inst} = {literal}'

    Array: Instruction = None

    def _array_literal(self, state):
        values = []
        for arg in self.Values:
            arg_val = arg.generate(state, state.object)
            values.append(arg_val)

        values = ', '.join(values)
        return f'[{values}]'

    def set_array(self, state, obj, *args):
        array_inst = self.Array.generate(state, state.Object, True)
        literal = self._array_literal(state)
        # ?
        return f'{array_inst} = {literal}'

    def array_const(self, state, obj, *args):
        array_type = self.Type
        literal = self._array_literal(state)
        return f'Array<{array_type}>(${literal})'

    def array_get_by_ref(self, state, obj, *args):
        var = self.Variable.generate(state,  state.Object)
        index = self.Index.generate(state, state.Object)
        return f'{var}[{index}]'

    Struct: str = None
    Values: List['Instruction'] = field(default_factory=list)
    StructPropName: str = None

    def struct_const(self, state, obj, *args):
        name = self.Struct
        args = []
        for arg in self.Value:
            # FIXME
            if isinstance(arg, dict):
                arg = Instruction.from_dict(arg)

            val = arg.generate(state, state.Object)
            args.append(f'{arg.StructPropName} = {val}')

        args = ', '.join(args)
        return f'{name}({args})'

    def softobject_const(self, state, obj, *args):
        value = self.Value.generate(state, state.Object)
        return f'SoftObjectPath({value})'

    def cross_interface_cast(self, state, obj, *args):
        value = self.Value.generate(state, state.Object)
        return f'InterfaceCast<{self.Type}>({value})'

    def interface_object_cast(self, state, obj, *args):
        value = self.Value.generate(state, state.Object)
        return f'Cast<{self.Type}>({value})'

    Cast: int = 0

    def primitive_cast(self, state, obj, *args):
        cast_val = self.Value.generate(state, state.Object)
        cast_kind = self.Cast

        if cast_kind == 70:
            # Instruction = EX_ObjToInterfaceCast
            return f'QueryInterface<{self.Type}>({cast_val})'

        return cast_val

    def object_interface_cast(self, state, obj, *args):
        cast_val = self.Value.generate(state, state.Object)
        return f'QueryInterface<{self.Type}>({cast_val})'

    def dynamic_cast(self, state, obj, *args):
        cast_class = self.Type
        cast_expr = self.Code.generate(state, obj, *args)
        return f'Cast<{cast_class}>({cast_expr})'

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

    def transform_const(self, state, obj, *args):
        rotator = f'Rotator({self.RotX}, {self.RotY}, {self.RotZ}, {self.RotW})'
        translate = f'Vector({self.TransX}, {self.TransY}, {self.TransZ})'
        scale = f'Vector({self.ScaleX}, {self.ScaleY}, {self.ScaleZ})'
        return f'Transform({rotator}, {translate}, {scale})'

    def none(self, *args):
        return "None"

    def text_const(self, *args):
        type = self.Type
        if type == 0:
            return ''

        if type in (1, 2, 3):
            return f'"{self.SrcStr}"'

        return f'STRING_TABLE_ENTRY("{self.StringTable}", "{self.KeyStr}"'

    def int_one(self, *args):
        return "1"

    def int_zero(self, *args):
        return "0"

    def true(self, *args):
        return "True"

    def false(self, *args):
        return "False"

    # Rotation
    Pitch: float = 0
    Yam: float = 0
    Roll: float = 0

    def rotation_const(self, state, obj, *args):
        return f'Rotator::FromPitchYawRoll({self.Pitch}, {self.Yaw}, {self.Roll})'

    # Vector
    X: float = 0
    Y: float = 0
    Z: float = 0

    def vector_const(self, state, obj, *args):
        return f'Vector({self.X}, {self.Y}, {self.Z})'

    def object_const(self, state, obj, *args):
        name = Type.object_from_path(self.Value)
        if name.startswith('Default__'):
            name = name[10:]
        return name

    def get_self(self, state, obj, *args):
        return obj

    def meta_cast(self, state, obj, *args):
        class_inst = self.Castee.generate(state, obj, *args)
        meta_class = self.MetaClass
        return f'ClassCast<{meta_class}>({class_inst})'

    def class_context(self, state, obj, IsAssignmentLeftSide):
        ctx_inst = self.Context.generate(state, obj)
        accessor = f'{ctx_inst}->ClassDefaultObject'
        return self.Code.generate(state, accessor)

    Interface: Instruction = None

    def interface_context(self, state, obj, *args):
        interface = self.Interface.generate(state, obj)
        return f'GetInterfaceUObject({interface})'

    def nothing(self, *args):
        return ''

    def cassert(self, state, obj, IsAssignmentLeftSide):
        inst = self.Condition.generate(state, state.Object)
        return f'assert({inst})'

    def value(self, *args):
        return str(self.Value)

    def value_str(self, *args):
        return f'"{self.Value}"'


    def _gen_call_args(self, state):
        lines = []
        for arg in self.Params:
            arg_res = ''
            if arg.FunctionParamOut:
                arg_res += '[ref] '

            arg_res += arg.generate(state, state.Object)
            lines.append(arg_res)
        args = ', '.join(lines)
        return args

    def multicast_call(self, state, obj, *args):
        obj = self.Variable.generate(state, obj, *args)
        args = self._gen_call_args(state)
        return f'{obj}->ProcessMulticastDelegate({args})'
        
    def function_call(self, state, obj, IsAssignmentLeftSide):
        funName = Type.object_from_path(self.Function)
        args = self._gen_call_args(state)
        return f'{obj}->{funName}({args})'

    def context(self, state, obj, IsAssignmentLeftSide):
        ctx_inst = self.Context.generate(state, state.Object)
        return self.Code.generate(state, ctx_inst)


    def let_value(self, state, obj, *args):
        value = self.Value.generate(state, state.Object)
        prop = self.Dest
        return f'PERSISTENT_FRAME({prop} = {value})'

    def let(self, state, obj, IsAssignmentLeftSide):
        prop = self.EvaluateProp
        prop_inst = prop.generate(state, state.Object, True)
        value_inst = self.EvaluateExp.generate(state, state.Object)
        return f'{prop_inst} = {value_inst}'

    def retinst(self, **kwargs):
        return 'return'

    def getattr(self, state, obj, IsAssignmentLeftSide):
        return f'{obj}->{self.VarName}'


    def getmember(self, state, obj, *args):
        value = self.Code.generate(state, state.Object)
        prop_name = self.Context
        return f'{value}.{prop_name}'

    def new_variable(self, state, obj, IsAssignmentLeftSide):
        name = state.get_rename(self.VarName, self.VarName)

        # if (ShouldRenameLocalVariable(VariableName)) {
        #    new_name = GenerateLocalVariableName(Instruction.VarType, FunctionState.UsedVariableNames);
        #    state['RenamedLocalVariables'][name] = new_name;
        #}

        if IsAssignmentLeftSide and not state.local_var_exist(name):
            state.LocalVariables[name] = True
            return f'{self.VarType.type} {name}'

        return name


@dataclass
class FunctionGenerationState:
    LocalVariables: dict = field(default_factory=dict)
    RenamedLocalVariables: dict =field(default_factory=dict)
    UsedVariableNames: dict = field(default_factory=dict)
    Object: str = 'this'
    LastExpression: str = '$INVALID_EXPRESSION$'

    def get_rename(self, name, default=None):
        return self.RenamedLocalVariables.get(name, default)

    def local_var_exist(self, name):
        return name in self.LocalVariables


@dataclass
class Function:
    Name: str = ''
    Arguments: List[Argument] = field(default_factory=list)
    Outputs: List = field(default_factory=list)
    Access: str = ''
    FunctionFlags: int = 0
    Code: List[Instruction] = field(default_factory=list)
    SuperClass: str = None
    IsOverride: bool = True

    @staticmethod
    def from_dict(kwargs):
        if not isinstance(kwargs, dict):
            return kwargs

        self = Function(**kwargs)
        self.Arguments = [Argument.from_dict(arg) for arg in self.Arguments]
        self.Code = [Instruction.from_dict(inst) for inst in self.Code if inst is not None]

        return self

    def generate(self, depth=1):
        state = FunctionGenerationState()

        lines = []
        for instruction in self.Code:
            code = instruction.generate(state, state.Object)
            state.LastExpression = code
            lines.append(code)
        body = f'\n{"    " * (depth + 1)}'.join(lines)

        lines = []
        for arg in self.Arguments:
            code = arg.generate()
            lines.append(code)
        args = ', '.join(lines)

        code = f"""
        |def {self.Name}({args}):
        |    {body}
        |""".replace('        |', '    ' * depth)

        return code


@dataclass
class Blueprint:
    Blueprint: str = ''
    ParentClass: str = ''
    BlueprintKind: str = ''
    WidgetTreeRootWidget: dict = field(default_factory=dict)
    NamedSlots: list = field(default_factory=list)
    Fields: List[Field] = field(default_factory=list)
    Functions: List[Function] = field(default_factory=list)

    @staticmethod
    def from_dict(kwargs):
        if not isinstance(kwargs, dict):
            return kwargs

        self = Blueprint(**kwargs)
        self.Fields = [Field.from_dict(field) for field in self.Fields]
        self.Functions = [Function.from_dict(fun) for fun in self.Functions]
        return self

    def generate(self, depth=0):
        lines = []
        for field in self.Fields:
            lines.append(field.generate())
        fields = '\n    '.join(lines)

        lines = []
        for fun in self.Functions:
            lines.append(fun.generate(depth=depth + 1))
        funs = '\n'.join(lines)


        name = Type.object_from_path(self.Blueprint)
        code = f"""
        |class {name}:
        |    {fields}
        |    {funs}
        |""".replace('        |', '')

        return code



def main(filename):
    with open(filename, 'rb') as file:
        decoded_pak = json.loads(file.read().decode('utf-8-sig'))

    blueprints: list = decoded_pak['Blueprints']

    blueprints = blueprints[2:]

    for kwargs in blueprints:
        bp = Blueprint.from_dict(kwargs)
        code = bp.generate()

        print(code)
        break


if __name__ == '__main__':
    import os

    folder = os.path.dirname(__file__)
    main(os.path.join(folder, '..', 'FGBlueprints.json'))