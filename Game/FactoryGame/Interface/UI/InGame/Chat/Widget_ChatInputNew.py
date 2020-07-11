
from codegen.ue4_stub import *

from Script.Engine import Default__KismetInputLibrary
from Script.Engine import Conv_TextToString
from Script.FactoryGame import FGPlayerController
from Script.Engine import EqualEqual_ByteByte
from Script.InputCore import Key
from Game.FactoryGame.Interface.UI.InGame.Chat.Widget_ChatWindow import Widget_ChatWindow
from Game.FactoryGame.Interface.UI.InGame.Chat.Widget_ChatInputNew import ExecuteUbergraph_Widget_ChatInputNew.K2Node_ComponentBoundEvent_Text
from Script.Engine import PlayerController
from Script.FactoryGame import EnterChatMessage
from Script.UMG import Handled
from Script.UMG import Unhandled
from Script.UMG import SetText
from Game.FactoryGame.Interface.UI.InGame.Chat.Widget_ChatInputNew import ExecuteUbergraph_Widget_ChatInputNew
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import FGInteractWidget
from Script.Engine import GetKey
from Script.Engine import EqualEqual_KeyKey
from Game.FactoryGame.Interface.UI.InGame.Chat.Widget_ChatInputNew import ExecuteUbergraph_Widget_ChatInputNew.K2Node_ComponentBoundEvent_CommitMethod
from Script.UMG import EventReply

class Widget_ChatInputNew(FGInteractWidget):
    mChatWindow: Ptr[Widget_ChatWindow]
    mUseKeyboard = True
    mRestoreFocusWhenLost = True
    mCallCustomTickOnConstruct = True
    
    def OnKeyUp(self):
        
        ReturnValue: Key = Default__KismetInputLibrary.GetKey(Ref[InKeyEvent])
        ReturnValue_0: bool = Default__KismetInputLibrary.EqualEqual_KeyKey(ReturnValue, Key(KeyName = "Escape"))
        if not ReturnValue_0:
            goto('L247')
        self.ExitChat()
        ReturnValue_1: EventReply = Default__WidgetBlueprintLibrary.Handled()
        ReturnValue_2: EventReply = ReturnValue_1
        goto('L324')
        # Label 247
        ReturnValue_3: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_2 = ReturnValue_3
    

    def BndEvt__mInputField_K2Node_ComponentBoundEvent_51_OnEditableTextBoxCommittedEvent__DelegateSignature(self, text: Const[Ref[FText]], CommitMethod: uint8):
        ExecuteUbergraph_Widget_ChatInputNew.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ChatInputNew.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ChatInputNew(10)
    

    def ExitChat(self):
        self.ExecuteUbergraph_Widget_ChatInputNew(352)
    

    def ExecuteUbergraph_Widget_ChatInputNew(self):
        ReturnValue: bool = EqualEqual_ByteByte(CommitMethod, 1)
        if not ReturnValue:
            goto('L357')
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_0)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L357')
        
        Text = None
        ReturnValue_1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Text])
        Controller.EnterChatMessage(ReturnValue_1)
        self.mInputField.SetText()
        self.ExitChat()
        # End
        # Label 311
        self.mChatWindow.ExitChat()
        # End
        goto('L311')
    
