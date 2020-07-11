
from codegen.ue4_stub import *

from Script.UMG import RemoveChildAt
from Game.FactoryGame.Interface.UI.InGame.Chat.Widget_ChatWindow import ExecuteUbergraph_Widget_ChatWindow
from Script.UMG import SetKeyboardFocus
from Game.FactoryGame.Interface.UI.InGame.Chat.Widget_ChatWindow import ExecuteUbergraph_Widget_ChatWindow.K2Node_Event_InFocusEvent
from Script.FactoryGame import Default__FGChatManager
from Script.FactoryGame import GetReceivedChatMessages
from Script.Engine import SetObjectPropertyByName
from Game.FactoryGame.Interface.UI.InGame.Chat.Widget_ChatWindow import ExecuteUbergraph_Widget_ChatWindow.K2Node_Event_MouseEvent1
from Script.FactoryGame import FGChatManager
from Script.UMG import GetChildrenCount
from Script.UMG import AddChildToVerticalBox
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Script.UMG import ESlateVisibility
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import EqualEqual_IntInt
from Script.FactoryGame import FGInteractWidget
from Script.Engine import BooleanOR
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.Interface.UI.InGame.Chat.Widget_ChatWindow import ExecuteUbergraph_Widget_ChatWindow.K2Node_Event_MouseEvent
from Script.FactoryGame import GetMessageVisibleDuration
from Game.FactoryGame.Interface.UI.InGame.Chat.Widget_ChatMessageRow import Widget_ChatMessageRow
from Script.UMG import ScrollToEnd
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import VerticalBoxSlot
from Script.UMG import Create
from Script.Engine import GetGameState
from Game.FactoryGame.Interface.UI.InGame.BP_GameUI import BP_GameUI
from Script.FactoryGame import ChatMessageStruct
from Script.FactoryGame import GetMaxNumMessagesInHistory
from Script.Engine import Min
from Game.FactoryGame.Interface.UI.InGame.Chat.Widget_ChatWindow import ExecuteUbergraph_Widget_ChatWindow.K2Node_Event_MyGeometry
from Script.Engine import Array_Clear

class Widget_ChatWindow(FGInteractWidget):
    mChatInputVisible: bool
    mCachedChatMessages: List[ChatMessageStruct]
    IsMouseHoveringChatWindow: bool
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mDesiredHorizontalAlignment = 1
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    
    def ExitChat(self):
        self.SetInputWindowVisibility(False)
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue, self, Ref[gameUI])
        UI: Ptr[BP_GameUI] = Cast[BP_GameUI](gameUI)
        bSuccess: bool = UI
        if not bSuccess:
            goto('L223')
        UI.ResetInput()
        self.UpdateVisibility()
    

    def OnPlayerBeginTypeMessage(self):
        self.SetInputWindowVisibility(True)
        self.SetupDefaultFocus()
        self.SetInputMode()
        self.InputWindow.mInputField.SetKeyboardFocus()
        self.UpdateVisibility()
    

    def UpdateVisibility(self):
        Variable6: uint8 = 0
        Variable7: uint8 = 2
        Variable2: bool = self.mChatInputVisible
        
        switch = {
            False: Variable7,
            True: Variable6
        }
        self.InputWindow.SetVisibility(switch.get(Variable2, None))
        
        switch_0 = {
            False: Variable7,
            True: Variable6
        }
        self.mMessageContent.SetVisibility(switch_0.get(Variable2, None))
        Variable2_0: uint8 = 3
        Variable3: uint8 = 1
        Variable: bool = self.mChatInputVisible
        
        switch_1 = {
            False: Variable3,
            True: Variable2_0
        }
        self.mMessageScrollBox.SetVisibility(switch_1.get(Variable, None))
        Variable_0: uint8 = 2
        Variable1: uint8 = 3
        Variable3_0: bool = self.mChatInputVisible
        
        switch_2 = {
            False: Variable1,
            True: Variable_0
        }
        self.mFreshMessageScrollBox.SetVisibility(switch_2.get(Variable3_0, None))
        Variable4: uint8 = 4
        Variable5: uint8 = 2
        
        IsFresh = None
        self.IsLastMessageFresh(Ref[IsFresh])
        ReturnValue: bool = BooleanOR(IsFresh, self.mChatInputVisible)
        Variable1_0: bool = ReturnValue
        
        switch_3 = {
            False: Variable5,
            True: Variable4
        }
        self.SetVisibility(switch_3.get(Variable1_0, None))
    

    def OnChatMessageReceived(self):
        self.CacheChatMessages()
        self.MatchWidgetsAndMessages()
        self.UpdateVisibility()
    

    def SetInputWindowVisibility(self, visible: bool):
        self.mChatInputVisible = visible
    

    def GetInputWindowVisibility(self):
        ReturnValue = self.mChatInputVisible
    

    def CacheChatMessages(self):
        
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mCachedChatMessages])
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_0: Ptr[FGChatManager] = Default__FGChatManager.Get(ReturnValue)
        
        ReturnValue_0.GetReceivedChatMessages(Ref[self.mCachedChatMessages])
        ReturnValue_1: int32 = self.mMessageVBox.GetChildrenCount()
        ReturnValue = Default__GameplayStatics.GetGameState(self)
        ReturnValue_0 = Default__FGChatManager.Get(ReturnValue)
        ReturnValue_2: int32 = ReturnValue_0.GetMaxNumMessagesInHistory()
        ReturnValue_3: bool = EqualEqual_IntInt(ReturnValue_1, ReturnValue_2)
        if not ReturnValue_3:
            goto('L469')
        ReturnValue_4: bool = self.mMessageVBox.RemoveChildAt(0)
    

    def IsLastMessageFresh(self):
        ReturnValue: int32 = self.mFreshMessageVBox.GetChildrenCount()
        ReturnValue_0: bool = ReturnValue > 0
        IsFresh = ReturnValue_0
    

    def RemoveMessageWidget(self):
        ReturnValue: int32 = self.mMessageVBox.GetChildrenCount()
        ReturnValue_0: int32 = ReturnValue - 1
        ReturnValue_1: int32 = Min(ReturnValue_0, 0)
        ReturnValue_2: bool = self.mMessageVBox.RemoveChildAt(ReturnValue_1)
    

    def AddMessageWidget(self):
        ExecutionFlow.Push("L845")
        # Label 5
        ReturnValue: int32 = self.mMessageVBox.GetChildrenCount()
        
        Item = None
        Item = self.mCachedChatMessages[ReturnValue]
        newMessage = Item
        ExecutionFlow.Push("L401")
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[Widget_ChatMessageRow] = Default__WidgetBlueprintLibrary.Create(self, Widget_ChatMessageRow, ReturnValue1)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue1_0, "mChatWindow", self)
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue1_0, "mChatMessage", Ref[newMessage])
        ReturnValue1_1: Ptr[VerticalBoxSlot] = self.mMessageVBox.AddChildToVerticalBox(ReturnValue1_0)
        goto(ExecutionFlow.Pop())
        # Label 401
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[Widget_ChatMessageRow] = Default__WidgetBlueprintLibrary.Create(self, Widget_ChatMessageRow, ReturnValue_0)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_1, "mChatWindow", self)
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_1, "mChatMessage", Ref[newMessage])
        ReturnValue_2: Ptr[VerticalBoxSlot] = self.mFreshMessageVBox.AddChildToVerticalBox(ReturnValue_1)
        ReturnValue_3: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_4: Ptr[FGChatManager] = Default__FGChatManager.Get(ReturnValue_3)
        ReturnValue_5: float = ReturnValue_4.GetMessageVisibleDuration()
        ReturnValue_1.RemoveWidgetAfterDelay(ReturnValue_5)
        goto(ExecutionFlow.Pop())
    

    def MatchWidgetsAndMessages(self):
        ExecutionFlow.Push("L427")
        
        # Label 5
        ReturnValue: int32 = len(self.mCachedChatMessages)
        ReturnValue_0: int32 = self.mMessageVBox.GetChildrenCount()
        ReturnValue_1: bool = ReturnValue_0 != ReturnValue
        if not ReturnValue_1:
            goto('L347')
        ExecutionFlow.Push("L5")
        
        ReturnValue = len(self.mCachedChatMessages)
        ReturnValue_0 = self.mMessageVBox.GetChildrenCount()
        ReturnValue_2: bool = ReturnValue_0 <= ReturnValue
        if not ReturnValue_2:
            goto('L412')
        self.AddMessageWidget()
        goto(ExecutionFlow.Pop())
        # Label 347
        self.mMessageScrollBox.ScrollToEnd()
        self.mFreshMessageScrollBox.ScrollToEnd()
        goto(ExecutionFlow.Pop())
        # Label 412
        self.RemoveMessageWidget()
        goto(ExecutionFlow.Pop())
    

    def OnRemovedFromFocusPath(self):
        ExecuteUbergraph_Widget_ChatWindow.K2Node_Event_InFocusEvent = InFocusEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ChatWindow(48)
    

    def OnMouseEnter(self):
        ExecuteUbergraph_Widget_ChatWindow.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ChatWindow.K2Node_Event_MouseEvent1 = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ChatWindow(124)
    

    def OnMouseLeave(self):
        ExecuteUbergraph_Widget_ChatWindow.K2Node_Event_MouseEvent = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ChatWindow(140)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ChatWindow(10)
    

    def ExecuteUbergraph_Widget_ChatWindow(self):
        self.InputWindow.mChatWindow = self
        # End
        if not self.mChatInputVisible:
            goto('L151')
        ReturnValue: bool = Not_PreBool(self.IsMouseHoveringChatWindow)
        if not ReturnValue:
            goto('L151')
        self.ExitChat()
        # End
        self.IsMouseHoveringChatWindow = True
        # End
        self.IsMouseHoveringChatWindow = False
    
