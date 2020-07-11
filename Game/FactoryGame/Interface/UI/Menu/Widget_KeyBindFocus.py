
from codegen.ue4_stub import *

from Script.Engine import Default__KismetInputLibrary
from Script.UMG import EventReply
from Script.UMG import SetKeyboardFocus
from Script.InputCore import Key
from Script.Engine import Not_PreBool
from Script.Engine import Key_IsGamepadKey
from Script.UMG import Handled
from Script.Engine import Key_IsModifierKey
from Script.Engine import FormatArgumentData
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import GetInputEventFromPointerEvent
from Script.Engine import Default__KismetTextLibrary
from Script.SlateCore import InputEvent
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.Menu.Widget_KeybindButton import Widget_KeybindButton
from Script.Engine import GetKey
from Script.Engine import PointerEvent_GetEffectingButton
from Script.Engine import EqualEqual_KeyKey
from Script.UMG import UserWidget
from Script.UMG import GetInputEventFromKeyEvent
from Game.FactoryGame.Interface.UI.Menu.Widget_KeyBindFocus import ExecuteUbergraph_Widget_KeyBindFocus
from Script.Engine import PointerEvent_GetWheelDelta

class Widget_KeyBindFocus(UserWidget):
    mKeyOwner: Ptr[Widget_KeybindButton]
    bIsFocusable = True
    
    def OnKeyUp(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        
        ReturnValue_0: bool = Default__KismetInputLibrary.Key_IsModifierKey(Ref[ReturnValue])
        if not ReturnValue_0:
            goto('L310')
        
        ReturnValue = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        
        ReturnValue_1: InputEvent = Default__WidgetBlueprintLibrary.GetInputEventFromKeyEvent(Ref[InKeyEvent])
        
        Handled = None
        self.HandleInput(ReturnValue_1, ReturnValue, Ref[Handled])
        ReturnValue_2: EventReply = Handled
    

    def HandleInput(self, InputEvent: InputEvent, keyPressed: Key):
        
        ReturnValue: bool = Default__KismetInputLibrary.Key_IsGamepadKey(Ref[keyPressed])
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        if not ReturnValue_0:
            goto('L414')
        ReturnValue_1: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(keyPressed, Key(KeyName = "Escape"))
        ReturnValue1: bool = Not_PreBool(ReturnValue_1)
        if not ReturnValue1:
            goto('L269')
        self.mKeyOwner.HandleInput(InputEvent, keyPressed)
        # Label 269
        self.mKeyOwner.mButton.SetKeyboardFocus()
        self.RemoveFromParent()
        ReturnValue_2: EventReply = Default__WidgetBlueprintLibrary.Handled()
        Handled = ReturnValue_2
    

    def OnMouseWheel(self):
        
        ReturnValue: InputEvent = Default__WidgetBlueprintLibrary.GetInputEventFromPointerEvent(Ref[MouseEvent])
        
        ReturnValue_0: float = Default__KismetInputLibrary.PointerEvent_GetWheelDelta(Ref[MouseEvent])
        ReturnValue_1: bool = ReturnValue_0 > 0
        Variable: Key = Key(KeyName = "MouseScrollUp")
        Variable_0: bool = ReturnValue_1
        Variable1: Key = Key(KeyName = "MouseScrollDown")
        
        switch = {
            False: Variable1,
            True: Variable
        }
        
        Handled = None
        self.HandleInput(ReturnValue, switch.get(Variable_0, None), Ref[Handled])
        ReturnValue_2: EventReply = Handled
    

    def GetKeyRebindText(self):
        FormatArgumentData.ArgumentName = "A"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = self.mKeyOwner.mKeyBindData.DisplayName_5_0A86F675465E0C811D17A287BB986630
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 290, 'Value': 'Press a key to rebind {A}'}", Array)
        ReturnValue_0: FText = ReturnValue
    

    def OnKeyDown(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        
        ReturnValue_0: bool = Default__KismetInputLibrary.Key_IsModifierKey(Ref[ReturnValue])
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        if not ReturnValue_1:
            goto('L339')
        
        ReturnValue = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        
        ReturnValue_2: InputEvent = Default__WidgetBlueprintLibrary.GetInputEventFromKeyEvent(Ref[InKeyEvent])
        
        Handled = None
        self.HandleInput(ReturnValue_2, ReturnValue, Ref[Handled])
        ReturnValue_3: EventReply = Handled
    

    def OnMouseButtonDown(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.PointerEvent_GetEffectingButton(Ref[MouseEvent])
        
        ReturnValue_0: InputEvent = Default__WidgetBlueprintLibrary.GetInputEventFromPointerEvent(Ref[MouseEvent])
        
        Handled = None
        self.HandleInput(ReturnValue_0, ReturnValue, Ref[Handled])
        ReturnValue_1: EventReply = Handled
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_KeyBindFocus(25)
    

    def ExecuteUbergraph_Widget_KeyBindFocus(self):
        # Label 10
        self.SetKeyboardFocus()
        # End
        goto('L10')
    
