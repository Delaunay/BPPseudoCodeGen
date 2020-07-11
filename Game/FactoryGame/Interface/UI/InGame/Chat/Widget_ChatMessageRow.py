
from codegen.ue4_stub import *

from Script.UMG import GetParent
from Script.Engine import Delay
from Script.FactoryGame import Default__FGChatManager
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Interface.UI.InGame.Chat.Widget_ChatWindow import Widget_ChatWindow
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import SetText
from Script.FactoryGame import GetChatMessageName
from Script.UMG import SetColorAndOpacity
from Game.FactoryGame.Interface.UI.InGame.Chat.Widget_ChatMessageRow import ExecuteUbergraph_Widget_ChatMessageRow
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Game.FactoryGame.Interface.UI.InGame.Chat.Widget_ChatMessageRow import ExecuteUbergraph_Widget_ChatMessageRow.K2Node_CustomEvent_Delay
from Script.UMG import Construct
from Script.UMG import PanelWidget
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import UserWidget
from Script.SlateCore import SlateColor
from Script.FactoryGame import ChatMessageStruct
from Script.FactoryGame import GetChatMessageColor
from Script.Engine import Concat_StrStr
from Script.UMG import RemoveChild
from Script.CoreUObject import LinearColor

class Widget_ChatMessageRow(UserWidget):
    mChatWindow: Ptr[Widget_ChatWindow]
    mChatMessage: ChatMessageStruct = Namespace(MessageString='', MessageType='EFGChatMessageType::CMT_MAX', Sender={'$Empty': True}, ServerTimeStamp=0)
    
    def SetTextMessage(self):
        ReturnValue: FText = self.GetChatText()
        
        self.mChatRichText.SetText(Ref[ReturnValue])
    

    def SetPlayerNameColor(self):
        ReturnValue: SlateColor = self.GetPlayerNameColor()
        SlateColor.SpecifiedColor = ReturnValue.SpecifiedColor
        SlateColor.ColorUseRule = 0
        self.mPlayerNameText.SetColorAndOpacity(SlateColor)
    

    def SetPlayerIconColor(self):
        ReturnValue: SlateColor = self.GetPlayerNameColor()
        self.mPlayerIcon.SetColorAndOpacity(ReturnValue.SpecifiedColor)
    

    def SetPlayerName(self):
        ReturnValue: FText = self.GetPlayerName()
        self.mPlayerNameText.SetText(ReturnValue)
    

    def GetPlayerNameColor(self):
        
        ReturnValue: LinearColor = Default__FGChatManager.GetChatMessageColor(Ref[self.mChatMessage])
        SlateColor.SpecifiedColor = ReturnValue
        SlateColor.ColorUseRule = 0
        ReturnValue_0: SlateColor = SlateColor
    

    def GetPlayerName(self):
        
        ReturnValue: FString = Default__FGChatManager.GetChatMessageName(Ref[self.mChatMessage])
        ReturnValue_0: FString = Default__KismetStringLibrary.Concat_StrStr(ReturnValue, ": ")
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_0)
        ReturnValue_2: FText = ReturnValue_1
    

    def GetChatText(self):
        ReturnValue: FText = Default__KismetTextLibrary.Conv_StringToText(self.mChatMessage.MessageString)
        ReturnValue_0: FText = ReturnValue
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ChatMessageRow(172)
    

    def RemoveWidgetAfterDelay(self, Delay: float):
        ExecuteUbergraph_Widget_ChatMessageRow.K2Node_CustomEvent_Delay = Delay #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ChatMessageRow(187)
    

    def ExecuteUbergraph_Widget_ChatMessageRow(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.SetPlayerName()
        self.SetPlayerIconColor()
        self.SetPlayerNameColor()
        self.SetTextMessage()
        goto(ExecutionFlow.Pop())
        ReturnValue: Ptr[PanelWidget] = self.GetParent()
        ReturnValue_0: bool = ReturnValue.RemoveChild(self)
        self.mChatWindow.UpdateVisibility()
        goto(ExecutionFlow.Pop())
        self.Construct()
        goto('L15')
        Default__KismetSystemLibrary.Delay(self, Delay, LatentActionInfo(Linkage = 72, UUID = 1290808301, ExecutionFunction = "ExecuteUbergraph_Widget_ChatMessageRow", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
    
