
from codegen.ue4_stub import *

from Script.OnlineSubsystemUtils import BlueprintSessionResult
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import SetObjectPropertyByName
from Script.FactoryGame import GetMySession
from Script.FactoryGame import FGPlayerState
from Script.UMG import AddChildToVerticalBox
from Script.UMG import GetChildrenCount
from Script.FactoryGame import CopyTextToClipboard
from Script.UMG import GetActiveWidget
from Script.FactoryGame import GetSessionVisibility
from Script.UMG import SetToolTipText
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageSession import ExecuteUbergraph_Widget_ManageSession.K2Node_Event_PlayBackgroundAnim
from Script.FactoryGame import Default__FGInviteLibrary
from Script.Engine import PlayerController
from Script.UMG import GetChildAt
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageSession import ExecuteUbergraph_Widget_ManageSession.K2Node_ComponentBoundEvent_SelectedOption
from Script.Engine import Map_Clear
from Script.Engine import GameStateBase
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import ESessionVisibility
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageSession import ExecuteUbergraph_Widget_ManageSession.K2Node_ComponentBoundEvent_newWidget
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import BP_MenuBase
from Script.Engine import TimerHandle
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import OnMenuEnter
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageSession import ExecuteUbergraph_Widget_ManageSession
from Script.Engine import IsValid
from Script.FactoryGame import PendingInvite
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.-Shared.Blueprint.BP_OnlineHelpers import Default__BP_OnlineHelpers
from Script.Engine import PlayerState
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import JoinInvite
from Script.Engine import NotEqual_StrStr
from Script.UMG import Widget
from Script.FactoryGame import FGPlayerControllerBase
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageSession import ExecuteUbergraph_Widget_ManageSession.K2Node_CustomEvent_ClickedButton
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ListButton import Widget_ListButton
from Script.Engine import EqualEqual_ObjectObject
from Script.UMG import PanelWidget
from Script.FactoryGame import FGOnlineFriend
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import MakeLiteralText
from Game.FactoryGame.Interface.UI.Menu.Widget_Multiplayer_ListButton import Widget_Multiplayer_ListButton
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageSession import ExecuteUbergraph_Widget_ManageSession.K2Node_CustomEvent_button
from Script.UMG import GetText
from Script.FactoryGame import GetSessionID
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.Engine import Map_Add
from Script.Engine import Map_Find
from Script.Engine import NotEqual_ObjectObject
from Script.FactoryGame import FGAdminInterface
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageSession import ExecuteUbergraph_Widget_ManageSession.K2Node_Event_prevMenu
from Script.UMG import VerticalBoxSlot
from Script.FactoryGame import Default__FGSessionLibrary
from Script.UMG import Create
from Script.Engine import GetGameState
from Script.Engine import TrimTrailing
from Game.FactoryGame.Interface.UI.Menu.Widget_ManageSession import ExecuteUbergraph_Widget_ManageSession.K2Node_ComponentBoundEvent_oldWidget
from Script.Engine import Default__BlueprintMapLibrary
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.UMG import SetSelectedOption
from Script.FactoryGame import GetAdminInterface
from Script.Engine import LocalPlayer

class Widget_ManageSession(BP_MenuBase):
    UpdateManageListTimer: TimerHandle
    mButtonToFriend: Dict[Ptr[Widget_Multiplayer_ListButton], FGOnlineFriend]
    mButtonToIngamePlayer: Dict[Ptr[Widget_Multiplayer_ListButton], PlayerState*]
    mButtonToInvite: Dict[Ptr[Widget_Multiplayer_ListButton], PendingInvite]
    
    def UpdateSessionID(self):
        ReturnValue: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        ReturnValue_0: FString = Default__FGSessionLibrary.GetSessionID(ReturnValue)
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_0)
        self.mSessionIDText.SetText(ReturnValue_1)
    

    def ClearIngamePlayerList(self):
        self.ManagePlayers.ClearChildren()
        
        Default__BlueprintMapLibrary.Map_Clear(Ref[self.mButtonToIngamePlayer])
    

    def IsHost(self, State: Ptr[PlayerState]):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: bool = EqualEqual_ObjectObject(State, ReturnValue.PlayerState)
        isOurself = ReturnValue_0
    

    def DisableSessionType(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        valid = None
        Default__HUDHelpers.HasValidAdminInterface(ReturnValue, self, Ref[valid])
        self.Widget_Options_DropdownBox.mDropdownBox.SetIsEnabled(valid)
        ReturnValue = self.GetOwningPlayer()
        
        valid = None
        Default__HUDHelpers.HasValidAdminInterface(ReturnValue, self, Ref[valid])
        if not valid:
            goto('L337')
        ReturnValue_0: FText = Default__KismetSystemLibrary.MakeLiteralText()
        
        # Label 291
        self.Widget_Options_DropdownBox.SetToolTipText(Ref[ReturnValue_0])
        # End
        # Label 337
        ReturnValue1: FText = Default__KismetSystemLibrary.MakeLiteralText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 388, 'Value': 'Only server admin can change this setting'}")
        
        self.Widget_Options_DropdownBox.SetToolTipText(Ref[ReturnValue1])
    

    def DisableClientOptions(self):
        self.DisableSessionType()
    

    def UpdateCurrentSessionType(self):
        Variable: FString = "Friends Only"
        Variable1: FString = "Private"
        ReturnValue: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        ReturnValue_0: BlueprintSessionResult = Default__FGSessionLibrary.GetMySession(ReturnValue)
        
        ReturnValue_1: uint8 = Default__FGSessionLibrary.GetSessionVisibility(Ref[ReturnValue_0])
        Variable_0: uint8 = ReturnValue_1
        
        switch = {
            0: Variable1,
            1: Variable
        }
        self.Widget_Options_DropdownBox.mDropdownBox.SetSelectedOption(switch.get(Variable_0, None))
    

    def PopulateManagePlayerList(self):
        ExecutionFlow.Push("L1002")
        self.ClearIngamePlayerList()
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 65
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        
        ReturnValue.PlayerArray = None
        ReturnValue_0: int32 = len(ReturnValue.PlayerArray)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L928")
        ReturnValue = Default__GameplayStatics.GetGameState(self)
        
        ReturnValue.PlayerArray = None
        Item = None
        Item = ReturnValue.PlayerArray[Variable_0]
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](Item)
        bSuccess: bool = State
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: Ptr[Widget_Multiplayer_ListButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_Multiplayer_ListButton, None)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "mParentWidget", self.ManagePlayers)
        ReturnValue_2.SetupForManagePlayers(State)
        OutputDelegate.BindUFunction(self, OnKick)
        ReturnValue_2.OnActionButtonClicked.AddUnique(OutputDelegate)
        ReturnValue_3: Ptr[VerticalBoxSlot] = self.ManagePlayers.AddChildToVerticalBox(ReturnValue_2)
        ReturnValue = Default__GameplayStatics.GetGameState(self)
        
        ReturnValue.PlayerArray = None
        Item = None
        Item = ReturnValue.PlayerArray[Variable_0]
        
        Item = None
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mButtonToIngamePlayer], Ref[ReturnValue_2], Ref[Item])
        goto(ExecutionFlow.Pop())
        # Label 928
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L65')
    

    def ClearLeftSelection(self):
        ExecutionFlow.Push("L365")
        Variable: int32 = 0
        # Label 28
        ReturnValue: int32 = self.OptionsList.GetChildrenCount()
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L291")
        ReturnValue_1: Ptr[Widget] = self.OptionsList.GetChildAt(Variable)
        Button: Ptr[Widget_ListButton] = Cast[Widget_ListButton](ReturnValue_1)
        bSuccess: bool = Button
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Button.mIsSelected = False
        goto(ExecutionFlow.Pop())
        # Label 291
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L28')
    

    def OnEscape(self):
        self.ExecuteUbergraph_Widget_ManageSession(1663)
    

    def OnKick(self, ClickedButton: Ptr[Widget_Multiplayer_ListButton]):
        ExecuteUbergraph_Widget_ManageSession.K2Node_CustomEvent_ClickedButton = ClickedButton #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManageSession(962)
    

    def BndEvt__Widget_Options_DropdownBox_K2Node_ComponentBoundEvent_0_onSelectionChanged__DelegateSignature(self, SelectedOption: FString):
        ExecuteUbergraph_Widget_ManageSession.K2Node_ComponentBoundEvent_SelectedOption = SelectedOption #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManageSession(43)
    

    def OnJoinInvite(self, Button: Ptr[Widget_Multiplayer_ListButton]):
        ExecuteUbergraph_Widget_ManageSession.K2Node_CustomEvent_button = Button #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManageSession(726)
    

    def SpawnAnim(self):
        ExecuteUbergraph_Widget_ManageSession.K2Node_Event_PlayBackgroundAnim = PlayBackgroundAnim #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManageSession(957)
    

    def OnMenuEnter(self):
        ExecuteUbergraph_Widget_ManageSession.K2Node_Event_prevMenu = prevMenu #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManageSession(1416)
    

    def BndEvt__mSwitcher_K2Node_ComponentBoundEvent_1_OnActiveWidgetSet__DelegateSignature(self, oldWidget: Ptr[Widget], newWidget: Ptr[Widget]):
        ExecuteUbergraph_Widget_ManageSession.K2Node_ComponentBoundEvent_oldWidget = oldWidget #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ManageSession.K2Node_ComponentBoundEvent_newWidget = newWidget #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ManageSession(1440)
    

    def BndEvt__mCopyToClipboard_K2Node_ComponentBoundEvent_2_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ManageSession(1704)
    

    def ExecuteUbergraph_Widget_ManageSession(self):
        # Label 10
        self.UpdateSessionID()
        self.DisableClientOptions()
        # End
        ReturnValue: FString = Default__KismetStringLibrary.TrimTrailing(SelectedOption)
        ReturnValue_0: bool = Default__KismetStringLibrary.NotEqual_StrStr(ReturnValue, "")
        if not ReturnValue_0:
            goto('L1795')
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        Base: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue1)
        bSuccess1: bool = Base
        if not bSuccess1:
            goto('L1795')
        ReturnValue_1: Ptr[FGAdminInterface] = Base.GetAdminInterface()
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_1)
        # Label 365
        if not ReturnValue_2:
            goto('L1795')
        
        enum = None
        Default__BP_OnlineHelpers.SessionVisibilityStringToEnum(SelectedOption, self, Ref[enum])
        ReturnValue_1 = Base.GetAdminInterface()
        ReturnValue_1.SetSessionVisibility(enum)
        # End
        
        # Label 526
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.UpdateManageListTimer])
        # End
        # Label 573
        self.UpdateCurrentSessionType()
        goto('L10')
        # Label 592
        self.PopulateManagePlayerList()
        OutputDelegate.BindUFunction(self, PopulateManagePlayerList)
        ReturnValue_3: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 10, True)
        self.UpdateManageListTimer = ReturnValue_3
        goto('L573')
        
        button = None
        Value = None
        ReturnValue_4: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mButtonToInvite], Ref[button], Ref[Value])
        if not ReturnValue_4:
            goto('L1795')
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        
        button = None
        Value = None
        ReturnValue_4 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mButtonToInvite], Ref[button], Ref[Value])
        
        Value = None
        Default__FGInviteLibrary.JoinInvite(ReturnValue_5, Ref[Value])
        # End
        # End
        
        ClickedButton = None
        Value1 = None
        ReturnValue1_0: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mButtonToIngamePlayer], Ref[ClickedButton], Ref[Value1])
        if not ReturnValue1_0:
            goto('L1795')
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        Base1: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue2)
        bSuccess2: bool = Base1
        if not bSuccess2:
            goto('L1795')
        ReturnValue1_1: Ptr[FGAdminInterface] = Base1.GetAdminInterface()
        ReturnValue1_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_1)
        if not ReturnValue1_2:
            goto('L1795')
        
        ClickedButton = None
        Value1 = None
        ReturnValue1_0 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mButtonToIngamePlayer], Ref[ClickedButton], Ref[Value1])
        ReturnValue1_1 = Base1.GetAdminInterface()
        ReturnValue1_1.KickPlayer(Value1)
        # End
        self.OnMenuEnter(prevMenu)
        goto('L592')
        ReturnValue_6: bool = NotEqual_ObjectObject(oldWidget, newWidget)
        if not ReturnValue_6:
            goto('L1795')
        ReturnValue_7: Ptr[Widget] = self.mSwitcher.GetActiveWidget()
        Widget: Ptr[PanelWidget] = Cast[PanelWidget](ReturnValue_7)
        bSuccess: bool = Widget
        if not bSuccess:
            goto('L1795')
        self.mSettings.PlayListSpawnAnim(Widget)
        # End
        self.mOwningMenu.OnEscape()
        goto('L526')
        ReturnValue_8: FText = self.mSessionIDText.GetText()
        Default__FGBlueprintFunctionLibrary.CopyTextToClipboard(ReturnValue_8)
    
