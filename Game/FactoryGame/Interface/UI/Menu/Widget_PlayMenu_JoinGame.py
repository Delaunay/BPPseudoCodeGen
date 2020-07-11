
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Script.OnlineSubsystemUtils import BlueprintSessionResult
from Script.Engine import SetObjectPropertyByName
from Script.FactoryGame import Sort
from Script.Engine import UniqueNetIdRepl
from Script.UMG import AddChildToVerticalBox
from Script.FactoryGame import FGLocalPlayer
from Script.FactoryGame import JoinSessionByID
from Script.CoreUObject import Timespan
from Script.Engine import MakeTimespan
from Game.FactoryGame.Interface.UI.Menu.Widget_PlayMenu_JoinGame import ExecuteUbergraph_Widget_PlayMenu_JoinGame.K2Node_CustomEvent_updatedFriends
from Script.FactoryGame import GetSessionVisibility
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import CopyTextFromClipboard
from Game.FactoryGame.Interface.UI.Menu.Widget_PlayMenu_JoinGame import ExecuteUbergraph_Widget_PlayMenu_JoinGame.K2Node_CustomEvent_Session
from Script.Engine import PlayerController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import Map_Clear
from Script.UMG import PlayAnimation
from Script.FactoryGame import ESessionVisibility
from Script.Engine import FormatArgumentData
from Game.FactoryGame.Interface.UI.Menu.Widget_PlayMenu_JoinGame import ExecuteUbergraph_Widget_PlayMenu_JoinGame.K2Node_CustomEvent_ClickedButton
from Script.UMG import SetText
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import BP_MenuBase
from Script.FactoryGame import GetFriendList
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import OnMenuEnter
from Script.Engine import IsValid
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Conv_IntToText
from Game.FactoryGame.-Shared.Blueprint.BP_OnlineHelpers import Default__BP_OnlineHelpers
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import OnMenuExit
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Interface.UI.Menu.Widget_PlayMenu_JoinGame import ExecuteUbergraph_Widget_PlayMenu_JoinGame.K2Node_Event_noAnimation
from Game.FactoryGame.Interface.UI.Menu.Widget_PlayMenu_JoinGame import ExecuteUbergraph_Widget_PlayMenu_JoinGame.K2Node_Event_prevMenu1
from Script.Engine import BreakTimespan
from Script.FactoryGame import JoinSession
from Script.Engine import Format
from Script.FactoryGame import FGOnlineFriend
from Script.UMG import GetText
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.Menu.Widget_Multiplayer_ListButton import Widget_Multiplayer_ListButton
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.Engine import NotEqual_ByteByte
from Script.FactoryGame import GetSessionSettings
from Script.Engine import Map_Find
from Script.Engine import Map_Add
from Script.FactoryGame import GetFriendUniqueNetId
from Game.FactoryGame.Interface.UI.Menu.Widget_PlayMenu_JoinGame import ExecuteUbergraph_Widget_PlayMenu_JoinGame.K2Node_CustomEvent_updatedId
from Script.UMG import VerticalBoxSlot
from Script.FactoryGame import GetFriendFromNetId
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Script.FactoryGame import Default__FGSessionLibrary
from Script.FactoryGame import IsSessionValid
from Script.FactoryGame import Default__FGFriendsLibrary
from Game.FactoryGame.Interface.UI.Menu.Widget_PlayMenu_JoinGame import ExecuteUbergraph_Widget_PlayMenu_JoinGame
from Game.FactoryGame.Interface.UI.Menu.Widget_PlayMenu_JoinGame import ExecuteUbergraph_Widget_PlayMenu_JoinGame.K2Node_Event_prevMenu
from Script.UMG import SetRenderOpacity
from Script.Engine import Default__BlueprintMapLibrary
from Script.FactoryGame import FGOnlineSessionSettings
from Script.Engine import LocalPlayer

class Widget_PlayMenu_JoinGame(BP_MenuBase):
    ShowSessionInfo: Ptr[WidgetAnimation]
    FriendsList: List[FGOnlineFriend]
    mSelectedSession: BlueprintSessionResult
    mButtonToFriend: Dict[Ptr[Widget_Multiplayer_ListButton], FGOnlineFriend]
    mFriendToButton: Dict[UniqueNetIdRepl, Widget_Multiplayer_ListButton*]
    mShouldAnimateSessionInfo: bool = True
    UsesSubmenuBackground = True
    
    def SetupButtonForJoinGame(self, Button: Const[Ref[Ptr[Widget_Multiplayer_ListButton]]], friend: Ref[FGOnlineFriend]):
        
        Button.SetupForJoinGame(Ref[friend])
        
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mButtonToFriend], Ref[Button], Ref[friend])
        
        ReturnValue: UniqueNetIdRepl = Default__FGFriendsLibrary.GetFriendUniqueNetId(Ref[friend])
        
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mFriendToButton], Ref[ReturnValue], Ref[Button])
        OutputDelegate1.BindUFunction(self, SetSessionInfo)
        Button.OnSessionSelected.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, OnSessionDeselected)
        Button.OnSessionDeselected.AddUnique(OutputDelegate)
        OutputDelegate2.BindUFunction(self, OnJoinSession)
        Button.OnActionButtonClicked.AddUnique(OutputDelegate2)
        ReturnValue_0: Ptr[VerticalBoxSlot] = self.MultiplayerList.AddChildToVerticalBox(Button)
    

    def UpdateFriendsForJoinMenu(self, Friends: Ref[List[FGOnlineFriend]]):
        ExecutionFlow.Push("L885")
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(Friends)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L597')
        Variable_0 = Variable
        ExecutionFlow.Push("L630")
        
        Item = None
        Item = Friends[Variable_0]
        friend: FGOnlineFriend = Item
        
        Item = None
        Item = Friends[Variable_0]
        
        Item = None
        ReturnValue_1: UniqueNetIdRepl = Default__FGFriendsLibrary.GetFriendUniqueNetId(Ref[Item])
        
        Value = None
        ReturnValue_2: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mFriendToButton], Ref[ReturnValue_1], Ref[Value])
        widget: Ptr[Widget_Multiplayer_ListButton] = Value
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(widget)
        if not ReturnValue_3:
            goto('L704')
        
        widget.SetupForJoinGame(Ref[friend])
        goto(ExecutionFlow.Pop())
        # Label 597
        self.MultiplayerList.Sort()
        goto(ExecutionFlow.Pop())
        # Label 630
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L51')
        # Label 704
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_6: Ptr[Widget_Multiplayer_ListButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_Multiplayer_ListButton, ReturnValue_5)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_6, "mParentWidget", self.MultiplayerList)
        
        self.SetupButtonForJoinGame(Ref[ReturnValue_6], Ref[friend])
        goto(ExecutionFlow.Pop())
    

    def UpdateFriendForJoinMenu(self, netId: UniqueNetIdRepl):
        
        Value = None
        ReturnValue: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mFriendToButton], Ref[netId], Ref[Value])
        if not ReturnValue:
            goto('L540')
        ReturnValue_0: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        
        ReturnValue_1: FGOnlineFriend = Default__FGFriendsLibrary.GetFriendFromNetId(ReturnValue_0, Ref[netId])
        
        Value = None
        ReturnValue = Default__BlueprintMapLibrary.Map_Find(Ref[self.mFriendToButton], Ref[netId], Ref[Value])
        
        Value.SetupForJoinGame(Ref[ReturnValue_1])
        self.MultiplayerList.Sort()
        
        Value = None
        ReturnValue = Default__BlueprintMapLibrary.Map_Find(Ref[self.mFriendToButton], Ref[netId], Ref[Value])
        if not Value.mIsSelected:
            goto('L540')
        
        Value = None
        ReturnValue = Default__BlueprintMapLibrary.Map_Find(Ref[self.mFriendToButton], Ref[netId], Ref[Value])
        self.SetSessionInfo(Value.mSession)
    

    def ShowSessionInfoAnim(self):
        self.mJoinButtonContainer.SetRenderOpacity(0)
        self.mSessionInfoContainer.SetRenderOpacity(0)
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ShowSessionInfo, 0, 1, 0, 1)
    

    def SetSessionInfo(self, session: BlueprintSessionResult):
        self.mSelectedSession = session
        
        ReturnValue: uint8 = Default__FGSessionLibrary.GetSessionVisibility(Ref[self.mSelectedSession])
        ReturnValue_0: bool = NotEqual_ByteByte(ReturnValue, 0)
        if not ReturnValue_0:
            goto('L1779')
        
        ReturnValue_1: FGOnlineSessionSettings = Default__FGSessionLibrary.GetSessionSettings(Ref[self.mSelectedSession])
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_1.NumConnectedPlayers, False, True, 1, 324)
        FormatArgumentData3.ArgumentName = "NumOfPlayers"
        FormatArgumentData3.ArgumentValueType = 4
        FormatArgumentData3.ArgumentValue = ReturnValue_2
        FormatArgumentData3.ArgumentValueInt = 0
        FormatArgumentData3.ArgumentValueFloat = 0
        FormatArgumentData3.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData3]
        ReturnValue1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 540, 'Value': 'Number of Connected Players: {NumOfPlayers}'}", Array1)
        self.mSessionNumOfPlayers.SetText(ReturnValue1)
        
        ReturnValue_1 = Default__FGSessionLibrary.GetSessionSettings(Ref[self.mSelectedSession])
        ReturnValue_3: Timespan = MakeTimespan(0, 0, 0, ReturnValue_1.PlayDuration, 0)
        
        Days = None
        Hours = None
        Minutes = None
        Seconds = None
        Milliseconds = None
        BreakTimespan(ReturnValue_3, Ref[Days], Ref[Hours], Ref[Minutes], Ref[Seconds], Ref[Milliseconds])
        FormatArgumentData.ArgumentName = "sec"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = Seconds
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "min"
        FormatArgumentData1.ArgumentValueType = 0
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = Minutes
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        FormatArgumentData2.ArgumentName = "hours"
        FormatArgumentData2.ArgumentValueType = 0
        FormatArgumentData2.ArgumentValue = 
        FormatArgumentData2.ArgumentValueInt = Hours
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData2, FormatArgumentData1, FormatArgumentData]
        ReturnValue_4: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1517, 'Value': 'Play Duration: {hours}h {min}m {sec}s'}", Array)
        self.mSessionPlaytime.SetText(ReturnValue_4)
        
        ReturnValue_1 = Default__FGSessionLibrary.GetSessionSettings(Ref[self.mSelectedSession])
        self.mSessionName.SetTitle(ReturnValue_1.SessionName)
        self.ShowSessionInfoAnim()
        # End
        # Label 1779
        self.mJoinButtonContainer.SetRenderOpacity(0)
        self.mSessionInfoContainer.SetRenderOpacity(0)
    

    def ClearMultiplayerList(self):
        self.MultiplayerList.ClearChildren()
        
        Default__BlueprintMapLibrary.Map_Clear(Ref[self.mButtonToFriend])
        
        Default__BlueprintMapLibrary.Map_Clear(Ref[self.mFriendToButton])
    

    def PopulateMultiplayerList(self):
        ExecutionFlow.Push("L679")
        self.ClearMultiplayerList()
        ReturnValue: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue)
        bSuccess: bool = Player
        friends: List[FGOnlineFriend] = []
        
        ReturnValue_0: bool = Player.GetFriendList(Ref[friends])
        self.FriendsList = friends
        Variable: int32 = 0
        
        # Label 220
        ReturnValue_1: int32 = len(self.FriendsList) - 1
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
            goto('L527')
        ExecutionFlow.Push("L605")
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_4: Ptr[Widget_Multiplayer_ListButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_Multiplayer_ListButton, ReturnValue_3)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_4, "mParentWidget", self.MultiplayerList)
        
        self.FriendsList[Variable] = None
        self.SetupButtonForJoinGame(Ref[ReturnValue_4], Ref[self.FriendsList[Variable]])
        goto(ExecutionFlow.Pop())
        # Label 527
        self.MultiplayerList.Sort()
        self.mFriends.PlayListSpawnAnim(self.MultiplayerList)
        goto(ExecutionFlow.Pop())
        # Label 605
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L220')
    

    def OnJoinSession(self, ClickedButton: Ptr[Widget_Multiplayer_ListButton]):
        ExecuteUbergraph_Widget_PlayMenu_JoinGame.K2Node_CustomEvent_ClickedButton = ClickedButton #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayMenu_JoinGame(29)
    

    def OnNewSessionSelected(self, session: BlueprintSessionResult):
        ExecuteUbergraph_Widget_PlayMenu_JoinGame.K2Node_CustomEvent_Session = session #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayMenu_JoinGame(348)
    

    def OnJoinSessionNew(self):
        self.ExecuteUbergraph_Widget_PlayMenu_JoinGame(387)
    

    def BndEvt__Widget_FrontEnd_Button_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PlayMenu_JoinGame(531)
    

    def OnSessionDeselected(self):
        self.ExecuteUbergraph_Widget_PlayMenu_JoinGame(550)
    

    def OnMenuEnter(self):
        ExecuteUbergraph_Widget_PlayMenu_JoinGame.K2Node_Event_prevMenu1 = prevMenu #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayMenu_JoinGame(797)
    

    def UpdateMultiplayerList(self, UpdatedFriends: UpdatedFriends):
        ExecuteUbergraph_Widget_PlayMenu_JoinGame.K2Node_CustomEvent_updatedFriends = UpdatedFriends #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayMenu_JoinGame(1052)
    

    def PresenceUpdated(self, updatedId: Const[Ref[UniqueNetIdRepl]]):
        ExecuteUbergraph_Widget_PlayMenu_JoinGame.K2Node_CustomEvent_updatedId = updatedId #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayMenu_JoinGame(1089)
    

    def OnMenuExit(self):
        ExecuteUbergraph_Widget_PlayMenu_JoinGame.K2Node_Event_prevMenu = prevMenu #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_PlayMenu_JoinGame.K2Node_Event_noAnimation = noAnimation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayMenu_JoinGame(1117)
    

    def BndEvt__mCopySessionIDButton_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PlayMenu_JoinGame(1381)
    

    def BndEvt__mJoinSessionButton_K2Node_ComponentBoundEvent_2_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PlayMenu_JoinGame(1477)
    

    def ExecuteUbergraph_Widget_PlayMenu_JoinGame(self):
        # Label 10
        self.PopulateMultiplayerList()
        # End
        
        ClickedButton = None
        Value = None
        ReturnValue: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mButtonToFriend], Ref[ClickedButton], Ref[Value])
        if not ReturnValue:
            goto('L1660')
        
        ClickedButton = None
        Value = None
        ReturnValue = Default__BlueprintMapLibrary.Map_Find(Ref[self.mButtonToFriend], Ref[ClickedButton], Ref[Value])
        ReturnValue_0: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        
        session = None
        Default__BP_OnlineHelpers.GetFriendSession(Value, ReturnValue_0, self, Ref[session])
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        
        session = None
        Default__FGSessionLibrary.JoinSession(ReturnValue1, Ref[session])
        # End
        self.mShouldAnimateSessionInfo = True
        self.SetSessionInfo(Session)
        # End
        ReturnValue_1: bool = Default__FGSessionLibrary.IsSessionValid(self.mSelectedSession)
        if not ReturnValue_1:
            goto('L1660')
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        
        Default__FGSessionLibrary.JoinSession(ReturnValue2, Ref[self.mSelectedSession])
        # End
        self.OnJoinSessionNew()
        # End
        ReturnValue1_0: bool = Default__FGSessionLibrary.IsSessionValid(self.mSelectedSession)
        if not ReturnValue1_0:
            goto('L1660')
        
        ReturnValue_2: uint8 = Default__FGSessionLibrary.GetSessionVisibility(Ref[self.mSelectedSession])
        ReturnValue_3: bool = NotEqual_ByteByte(ReturnValue_2, 0)
        if not ReturnValue_3:
            goto('L1660')
        self.mSelectedSession = BlueprintSessionResult
        ReturnValue_4: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ShowSessionInfo, 0, 1, 1, 1)
        # End
        self.OnMenuEnter(prevMenu1)
        ReturnValue1_1: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue1_1)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L1660')
        OutputDelegate1.BindUFunction(self, UpdateMultiplayerList)
        Player.mOnFriendsListUpdated.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, PresenceUpdated)
        Player.mOnFriendsPresenceUpdated.AddUnique(OutputDelegate)
        goto('L10')
        
        updatedFriends.Friends = None
        self.UpdateFriendsForJoinMenu(Ref[updatedFriends.Friends])
        # End
        self.UpdateFriendForJoinMenu(updatedId)
        # End
        self.OnMenuExit(prevMenu, noAnimation)
        ReturnValue2_0: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player1: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue2_0)
        bSuccess1: bool = Player1
        if not bSuccess1:
            goto('L1660')
        OutputDelegate1.BindUFunction(self, UpdateMultiplayerList)
        Player1.mOnFriendsListUpdated.Remove(OutputDelegate1)
        OutputDelegate.BindUFunction(self, PresenceUpdated)
        Player1.mOnFriendsPresenceUpdated.Remove(OutputDelegate)
        # End
        ReturnValue_5: FText = Default__FGBlueprintFunctionLibrary.CopyTextFromClipboard()
        self.mSessionIDTextBox.SetText(ReturnValue_5)
        # End
        ReturnValue_6: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_7: FText = self.mSessionIDTextBox.GetText()
        
        ReturnValue_8: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_7])
        Default__FGSessionLibrary.JoinSessionByID(ReturnValue_6, ReturnValue_8)
    
