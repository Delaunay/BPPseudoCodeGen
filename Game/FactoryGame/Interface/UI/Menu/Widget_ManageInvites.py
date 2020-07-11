
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Menu.Widget_ManageInvites import ExecuteUbergraph_Widget_ManageInvites.K2Node_CustomEvent_receivedInvite
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageInvites import ExecuteUbergraph_Widget_ManageInvites.K2Node_CustomEvent_ClickedButton
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import Destruct
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageInvites import ExecuteUbergraph_Widget_ManageInvites.K2Node_Event_prevMenu
from Script.Engine import SetObjectPropertyByName
from Script.FactoryGame import GetPendingInvites
from Script.FactoryGame import Sort
from Script.FactoryGame import SendInviteToFriend
from Script.Engine import UniqueNetIdRepl
from Script.UMG import AddChildToVerticalBox
from Script.FactoryGame import FGLocalPlayer
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageInvites import ExecuteUbergraph_Widget_ManageInvites.K2Node_CustomEvent_updatedId1
from Script.FactoryGame import Default__FGInviteLibrary
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import Map_Clear
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import BP_MenuBase
from Script.Engine import TimerHandle
from Script.FactoryGame import GetFriendList
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import OnMenuEnter
from Script.FactoryGame import PendingInvite
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageInvites import ExecuteUbergraph_Widget_ManageInvites.K2Node_CustomEvent_button
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import OnMenuExit
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageInvites import ExecuteUbergraph_Widget_ManageInvites
from Script.FactoryGame import JoinInvite
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import Construct
from Script.UMG import PanelWidget
from Script.Engine import EqualEqual_ObjectObject
from Script.FactoryGame import FGOnlineFriend
from Game.FactoryGame.Interface.UI.Menu.Widget_Multiplayer_ListButton import Widget_Multiplayer_ListButton
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageInvites import ExecuteUbergraph_Widget_ManageInvites.K2Node_CustomEvent_updatedFriends
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageInvites import ExecuteUbergraph_Widget_ManageInvites.K2Node_Event_noAnimation
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.Engine import Map_Add
from Script.Engine import Map_Find
from Script.Engine import NotEqual_ObjectObject
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageInvites import ExecuteUbergraph_Widget_ManageInvites.K2Node_ComponentBoundEvent_newWidget
from Script.FactoryGame import GetFriendUniqueNetId
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import VerticalBoxSlot
from Script.FactoryGame import GetFriendFromNetId
from Script.UMG import Create
from Script.FactoryGame import Default__FGFriendsLibrary
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageInvites import ExecuteUbergraph_Widget_ManageInvites.K2Node_ComponentBoundEvent_oldWidget
from Script.FactoryGame import AddPopupWithCloseDelegate
from Script.Engine import Default__BlueprintMapLibrary
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageInvites import ExecuteUbergraph_Widget_ManageInvites.K2Node_CustomEvent_updatedId
from Script.FactoryGame import GetInviteFromSender
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageInvites import ExecuteUbergraph_Widget_ManageInvites.K2Node_Event_prevMenu1
from Script.Engine import LocalPlayer

class Widget_ManageInvites(BP_MenuBase):
    UpdateManageListTimer: TimerHandle
    mButtonToFriend: Dict[Ptr[Widget_Multiplayer_ListButton], FGOnlineFriend]
    mButtonToInvite: Dict[Ptr[Widget_Multiplayer_ListButton], PendingInvite]
    mFriendToButton: Dict[UniqueNetIdRepl, Widget_Multiplayer_ListButton*]
    mInviteToButton: Dict[PendingInvite, Widget_Multiplayer_ListButton*]
    UsesSubmenuBackground = True
    
    def AddInviteToInviteList(self, invite: Ref[PendingInvite]):
        
        Value = None
        ReturnValue: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mInviteToButton], Ref[invite], Ref[Value])
        if not ReturnValue:
            goto('L88')
        # End
        # Label 88
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[Widget_Multiplayer_ListButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_Multiplayer_ListButton, ReturnValue_0)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_1, "mParentWidget", self.ManageInvites)
        
        self.SetupButtonForJoinInvite(Ref[ReturnValue_1], Ref[invite])
        self.ManageInvites.Sort()
    

    def UpdateFriendInviteButton(self, netId: Ref[UniqueNetIdRepl]):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        ReturnValue_0: PendingInvite = Default__FGInviteLibrary.GetInviteFromSender(ReturnValue, Ref[netId])
        
        Value = None
        ReturnValue_1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mInviteToButton], Ref[ReturnValue_0], Ref[Value])
        if not ReturnValue_1:
            goto('L413')
        ReturnValue = self.GetOwningPlayer()
        
        ReturnValue_0 = Default__FGInviteLibrary.GetInviteFromSender(ReturnValue, Ref[netId])
        
        Value = None
        ReturnValue_1 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mInviteToButton], Ref[ReturnValue_0], Ref[Value])
        
        Value.SetupForJoinInvite(Ref[ReturnValue_0])
        self.ManageInvites.Sort()
    

    def SetupButtonForJoinInvite(self, Button: Const[Ref[Ptr[Widget_Multiplayer_ListButton]]], invite: Ref[PendingInvite]):
        
        Button.SetupForJoinInvite(Ref[invite])
        
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mButtonToInvite], Ref[Button], Ref[invite])
        
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mInviteToButton], Ref[invite], Ref[Button])
        OutputDelegate.BindUFunction(self, OnJoinInvite)
        Button.OnActionButtonClicked.AddUnique(OutputDelegate)
        ReturnValue: Ptr[VerticalBoxSlot] = self.ManageInvites.AddChildToVerticalBox(Button)
    

    def SetupButtonForSendInvite(self, Button: Ptr[Widget_Multiplayer_ListButton], onlineFriend: Const[Ref[FGOnlineFriend]]):
        
        Button.SetupForSendInvite(Ref[onlineFriend])
        
        ReturnValue: UniqueNetIdRepl = Default__FGFriendsLibrary.GetFriendUniqueNetId(Ref[onlineFriend])
        
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mFriendToButton], Ref[ReturnValue], Ref[Button])
        
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mButtonToFriend], Ref[Button], Ref[onlineFriend])
        OutputDelegate.BindUFunction(self, OnInvite)
        Button.OnActionButtonClicked.AddUnique(OutputDelegate)
        ReturnValue_0: Ptr[VerticalBoxSlot] = self.InvitePlayers.AddChildToVerticalBox(Button)
    

    def UpdateOrAddFriendsToInvite(self, UpdatedFriends: Ref[List[FGOnlineFriend]]):
        ExecutionFlow.Push("L975")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(UpdatedFriends)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L628')
        Variable_0 = Variable
        ExecutionFlow.Push("L661")
        
        Item = None
        Item = UpdatedFriends[Variable_0]
        
        Item = None
        ReturnValue_1: UniqueNetIdRepl = Default__FGFriendsLibrary.GetFriendUniqueNetId(Ref[Item])
        
        Value = None
        ReturnValue_2: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mFriendToButton], Ref[ReturnValue_1], Ref[Value])
        if not ReturnValue_2:
            goto('L735')
        
        Item = None
        Item = UpdatedFriends[Variable_0]
        
        Item = None
        ReturnValue_1 = Default__FGFriendsLibrary.GetFriendUniqueNetId(Ref[Item])
        
        Value = None
        ReturnValue_2 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mFriendToButton], Ref[ReturnValue_1], Ref[Value])
        
        Item = None
        Value.SetupForSendInvite(Ref[Item])
        goto(ExecutionFlow.Pop())
        # Label 628
        self.InvitePlayers.Sort()
        goto(ExecutionFlow.Pop())
        # Label 661
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L51')
        # Label 735
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: Ptr[Widget_Multiplayer_ListButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_Multiplayer_ListButton, ReturnValue_4)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_5, "mParentWidget", self.InvitePlayers)
        
        Item = None
        Item = UpdatedFriends[Variable_0]
        
        Item = None
        self.SetupButtonForSendInvite(ReturnValue_5, Ref[Item])
        goto(ExecutionFlow.Pop())
    

    def UpdateInviteFriendButton(self, friendId: UniqueNetIdRepl):
        
        Value = None
        ReturnValue: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mFriendToButton], Ref[friendId], Ref[Value])
        if not ReturnValue:
            goto('L321')
        ReturnValue_0: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        
        ReturnValue_1: FGOnlineFriend = Default__FGFriendsLibrary.GetFriendFromNetId(ReturnValue_0, Ref[friendId])
        
        Value = None
        ReturnValue = Default__BlueprintMapLibrary.Map_Find(Ref[self.mFriendToButton], Ref[friendId], Ref[Value])
        
        Value.SetupForSendInvite(Ref[ReturnValue_1])
        self.InvitePlayers.Sort()
    

    def PopulateInviteList(self):
        ExecutionFlow.Push("L640")
        self.ClearInviteList()
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        invites: List[PendingInvite] = []
        
        Default__FGInviteLibrary.GetPendingInvites(ReturnValue1, Ref[invites])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 150
        ReturnValue: int32 = len(invites)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L533')
        Variable_0 = Variable
        ExecutionFlow.Push("L566")
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Widget_Multiplayer_ListButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_Multiplayer_ListButton, ReturnValue_1)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mParentWidget", self.InvitePlayers)
        
        Item = None
        Item = invites[Variable_0]
        
        Item = None
        self.SetupButtonForJoinInvite(Ref[ReturnValue_2], Ref[Item])
        goto(ExecutionFlow.Pop())
        # Label 533
        self.ManageInvites.Sort()
        goto(ExecutionFlow.Pop())
        # Label 566
        ReturnValue_3: int32 = Variable + 1
        Variable = ReturnValue_3
        goto('L150')
    

    def ClearInviteList(self):
        self.ManageInvites.ClearChildren()
        
        Default__BlueprintMapLibrary.Map_Clear(Ref[self.mButtonToInvite])
        
        Default__BlueprintMapLibrary.Map_Clear(Ref[self.mInviteToButton])
    

    def ClearInvitePlayerList(self):
        self.InvitePlayers.ClearChildren()
        
        Default__BlueprintMapLibrary.Map_Clear(Ref[self.mButtonToFriend])
        
        Default__BlueprintMapLibrary.Map_Clear(Ref[self.mFriendToButton])
    

    def PopulateFriendsToInvite(self):
        ExecutionFlow.Push("L733")
        self.ClearInvitePlayerList()
        ReturnValue: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue)
        bSuccess: bool = Player
        friends: List[FGOnlineFriend] = []
        
        ReturnValue_0: bool = Player.GetFriendList(Ref[friends])
        FriendsList = friends
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 243
        ReturnValue_1: int32 = len(FriendsList)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
            goto('L626')
        Variable_0 = Variable
        ExecutionFlow.Push("L659")
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_4: Ptr[Widget_Multiplayer_ListButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_Multiplayer_ListButton, ReturnValue_3)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_4, "mParentWidget", self.InvitePlayers)
        
        Item = None
        Item = FriendsList[Variable_0]
        
        Item = None
        self.SetupButtonForSendInvite(ReturnValue_4, Ref[Item])
        goto(ExecutionFlow.Pop())
        # Label 626
        self.InvitePlayers.Sort()
        goto(ExecutionFlow.Pop())
        # Label 659
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L243')
    

    def OnEscape(self):
        self.ExecuteUbergraph_Widget_ManageInvites(784)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ManageInvites(15)
    

    def OnJoinInvite(self, Button: Ptr[Widget_Multiplayer_ListButton]):
        ExecuteUbergraph_Widget_ManageInvites.K2Node_CustomEvent_button = Button #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManageInvites(300)
    

    def AddInvitePlayersDelegates(self):
        self.ExecuteUbergraph_Widget_ManageInvites(523)
    

    def FriendListUpdated_InvitePlayerss(self, UpdatedFriends: UpdatedFriends):
        ExecuteUbergraph_Widget_ManageInvites.K2Node_CustomEvent_updatedFriends = UpdatedFriends #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManageInvites(751)
    

    def PresenceUpdated_InvitePlayers(self, updatedId: Const[Ref[UniqueNetIdRepl]]):
        ExecuteUbergraph_Widget_ManageInvites.K2Node_CustomEvent_updatedId1 = updatedId #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManageInvites(789)
    

    def RemoveInvitePlayersDelegates(self):
        self.ExecuteUbergraph_Widget_ManageInvites(1041)
    

    def AddManageInvitesDelegates(self):
        self.ExecuteUbergraph_Widget_ManageInvites(1046)
    

    def FriendsPresenceUpdate_ManageInvites(self, updatedId: Const[Ref[UniqueNetIdRepl]]):
        ExecuteUbergraph_Widget_ManageInvites.K2Node_CustomEvent_updatedId = updatedId #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManageInvites(1274)
    

    def RemoveManageInvitesDelegates(self):
        self.ExecuteUbergraph_Widget_ManageInvites(1526)
    

    def InviteReceived_ManageInvites(self, receivedInvite: Const[Ref[PendingInvite]]):
        ExecuteUbergraph_Widget_ManageInvites.K2Node_CustomEvent_receivedInvite = receivedInvite #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManageInvites(1531)
    

    def OnMenuExit(self):
        ExecuteUbergraph_Widget_ManageInvites.K2Node_Event_prevMenu1 = prevMenu #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ManageInvites.K2Node_Event_noAnimation = noAnimation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManageInvites(1792)
    

    def BndEvt__mSwitcher_K2Node_ComponentBoundEvent_0_OnActiveWidgetSet__DelegateSignature(self, oldWidget: Ptr[Widget], newWidget: Ptr[Widget]):
        ExecuteUbergraph_Widget_ManageInvites.K2Node_ComponentBoundEvent_oldWidget = oldWidget #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ManageInvites.K2Node_ComponentBoundEvent_newWidget = newWidget #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManageInvites(2089)
    

    def OnMenuEnter(self):
        ExecuteUbergraph_Widget_ManageInvites.K2Node_Event_prevMenu = prevMenu #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManageInvites(2142)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_ManageInvites(2240)
    

    def OnInvite(self, ClickedButton: Ptr[Widget_Multiplayer_ListButton]):
        ExecuteUbergraph_Widget_ManageInvites.K2Node_CustomEvent_ClickedButton = ClickedButton #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManageInvites(2279)
    

    def ExecuteUbergraph_Widget_ManageInvites(self):
        goto(ComputedJump("EntryPoint"))
        self.Construct()
        
        IsInMainMenu = None
        Default__HUDHelpers.IsInMainMenu(self, self, Ref[IsInMainMenu])
        Variable: uint8 = 0
        Variable1: uint8 = 1
        Variable_0: bool = IsInMainMenu
        
        switch = {
            False: Variable,
            True: Variable1
        }
        self.mInvitePlayers.SetVisibility(switch.get(Variable_0, None))
        goto(ExecutionFlow.Pop())
        # Label 221
        self.mOwningMenu.OnEscape()
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.UpdateManageListTimer])
        goto(ExecutionFlow.Pop())
        
        button = None
        Value = None
        ReturnValue: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mButtonToInvite], Ref[button], Ref[Value])
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        
        button = None
        Value = None
        ReturnValue = Default__BlueprintMapLibrary.Map_Find(Ref[self.mButtonToInvite], Ref[button], Ref[Value])
        
        Value = None
        Default__FGInviteLibrary.JoinInvite(ReturnValue_0, Ref[Value])
        goto(ExecutionFlow.Pop())
        ReturnValue1: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue1)
        bSuccess: bool = Player
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        OutputDelegate4.BindUFunction(self, FriendListUpdated_InvitePlayerss)
        Player.mOnFriendsListUpdated.AddUnique(OutputDelegate4)
        OutputDelegate3.BindUFunction(self, PresenceUpdated_InvitePlayers)
        Player.mOnFriendsPresenceUpdated.AddUnique(OutputDelegate3)
        goto(ExecutionFlow.Pop())
        
        updatedFriends.Friends = None
        self.UpdateOrAddFriendsToInvite(Ref[updatedFriends.Friends])
        goto(ExecutionFlow.Pop())
        goto('L221')
        self.UpdateInviteFriendButton(updatedId1)
        goto(ExecutionFlow.Pop())
        # Label 813
        ReturnValue2: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player1: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue2)
        bSuccess1: bool = Player1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        OutputDelegate4.BindUFunction(self, FriendListUpdated_InvitePlayerss)
        Player1.mOnFriendsListUpdated.Remove(OutputDelegate4)
        OutputDelegate3.BindUFunction(self, PresenceUpdated_InvitePlayers)
        Player1.mOnFriendsPresenceUpdated.Remove(OutputDelegate3)
        goto(ExecutionFlow.Pop())
        goto('L813')
        ReturnValue3: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player2: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue3)
        bSuccess2: bool = Player2
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        OutputDelegate1.BindUFunction(self, InviteReceived_ManageInvites)
        Player2.mOnInviteReceived.AddUnique(OutputDelegate1)
        OutputDelegate2.BindUFunction(self, FriendsPresenceUpdate_ManageInvites)
        Player2.mOnFriendsPresenceUpdated.AddUnique(OutputDelegate2)
        goto(ExecutionFlow.Pop())
        
        updatedId = None
        self.UpdateFriendInviteButton(Ref[updatedId])
        goto(ExecutionFlow.Pop())
        # Label 1298
        ReturnValue4: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player3: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue4)
        bSuccess3: bool = Player3
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        OutputDelegate1.BindUFunction(self, InviteReceived_ManageInvites)
        Player3.mOnInviteReceived.Remove(OutputDelegate1)
        OutputDelegate2.BindUFunction(self, FriendsPresenceUpdate_ManageInvites)
        Player3.mOnFriendsPresenceUpdated.Remove(OutputDelegate2)
        goto(ExecutionFlow.Pop())
        goto('L1298')
        
        receivedInvite = None
        self.AddInviteToInviteList(Ref[receivedInvite])
        goto(ExecutionFlow.Pop())
        # Label 1555
        OutputDelegate.BindUFunction(self.mOwningMenu, RestoreFocusOnPopupClosed)
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        
        OutputDelegate = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue1_0, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1652, 'Value': 'Invites'}", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1699, 'Value': 'Invite sent'}", 0, None, None, Ref[OutputDelegate])
        goto(ExecutionFlow.Pop())
        # Label 1763
        self.RemoveInvitePlayersDelegates()
        self.RemoveManageInvitesDelegates()
        goto(ExecutionFlow.Pop())
        self.OnMenuExit(prevMenu1, noAnimation)
        goto('L1763')
        # Label 1825
        ExecutionFlow.Push("L1951")
        Widget: Ptr[PanelWidget] = Cast[PanelWidget](newWidget)
        bSuccess4: bool = Widget
        if not bSuccess4:
           goto(ExecutionFlow.Pop())
        self.mSettings.PlayListSpawnAnim(Widget)
        goto(ExecutionFlow.Pop())
        # Label 1951
        ReturnValue_1: bool = EqualEqual_ObjectObject(newWidget, self.InvitePlayers)
        if not ReturnValue_1:
            goto('L2046')
        self.RemoveManageInvitesDelegates()
        self.AddInvitePlayersDelegates()
        self.PopulateFriendsToInvite()
        goto(ExecutionFlow.Pop())
        # Label 2046
        self.RemoveInvitePlayersDelegates()
        self.AddManageInvitesDelegates()
        self.PopulateInviteList()
        goto(ExecutionFlow.Pop())
        ReturnValue_2: bool = NotEqual_ObjectObject(oldWidget, newWidget)
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        goto('L1825')
        self.OnMenuEnter(prevMenu)
        self.mSwitcher.SetActiveWidgetIndex(0)
        self.mNavigation.PlayListSpawnAnim(None)
        goto(ExecutionFlow.Pop())
        self.Destruct()
        self.RemoveInvitePlayersDelegates()
        self.RemoveManageInvitesDelegates()
        goto(ExecutionFlow.Pop())
        
        ClickedButton = None
        Value1 = None
        ReturnValue1_1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mButtonToFriend], Ref[ClickedButton], Ref[Value1])
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        ReturnValue_3: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        
        ClickedButton = None
        Value1 = None
        ReturnValue1_1 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mButtonToFriend], Ref[ClickedButton], Ref[Value1])
        
        Value1 = None
        Default__FGInviteLibrary.SendInviteToFriend(ReturnValue_3, Ref[Value1])
        goto('L1555')
    
