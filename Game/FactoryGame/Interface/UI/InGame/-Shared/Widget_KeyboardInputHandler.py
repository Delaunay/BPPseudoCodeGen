
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_KeyboardInputHandler import ExecuteUbergraph_Widget_KeyboardInputHandler.K2Node_CustomEvent_CommitMethod
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_KeyboardInputHandler import ExecuteUbergraph_Widget_KeyboardInputHandler.K2Node_CustomEvent_Text
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.UMG import SetUserFocus
from Script.UMG import GetChildAt
from Script.UMG import Handled
from Script.UMG import Unhandled
from Script.UMG import Widget
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_KeyboardInputHandler import ExecuteUbergraph_Widget_KeyboardInputHandler
from Script.UMG import HasUserFocusedDescendants
from Script.Engine import PrintString
from Script.UMG import EditableText
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Not_PreBool
from Script.UMG import EventReply
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class Widget_KeyboardInputHandler(UserWidget):
    bIsFocusable = True
    
    def OnKeyUp(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_1: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_2: bool = self.mContent.HasUserFocusedDescendants(ReturnValue)
        Variable: bool = ReturnValue_2
        
        switch = {
            False: ReturnValue_0,
            True: ReturnValue_1
        }
        ReturnValue_3: EventReply = switch.get(Variable, None)
    

    def OnTextCommited(self, text: Const[Ref[FText]], CommitMethod: uint8):
        ExecuteUbergraph_Widget_KeyboardInputHandler.K2Node_CustomEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_KeyboardInputHandler.K2Node_CustomEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_KeyboardInputHandler(26)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_KeyboardInputHandler(452)
    

    def ExecuteUbergraph_Widget_KeyboardInputHandler(self):
        # Label 10
        self.bIsFocusable = True
        # End
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: bool = self.HasUserFocusedDescendants(ReturnValue)
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        if not ReturnValue_1:
            goto('L457')
        Default__KismetSystemLibrary.PrintString(self, "Hello there", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        self.SetUserFocus(ReturnValue1)
        # End
        # Label 257
        ReturnValue_2: Ptr[Widget] = self.mContent.GetChildAt(0)
        Text: Ptr[EditableText] = Cast[EditableText](ReturnValue_2)
        bSuccess: bool = Text
        if not bSuccess:
            goto('L457')
        OutputDelegate.BindUFunction(self, OnTextCommited)
        Text.OnTextCommitted.AddUnique(OutputDelegate)
        goto('L10')
        goto('L257')
    
