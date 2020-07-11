
from codegen.ue4_stub import *

from Script.UMG import SetUserFocus
from Script.FactoryGame import StartRespawn
from Script.FactoryGame import TravelToMainMenu
from Script.AkAudio import PostAkEvent
from Script.OnlineSubsystemUtils import BlueprintSessionResult
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import Destruct
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import GetFGGameUserSettings
from Script.FactoryGame import GetMySession
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.CoreUObject import Timespan
from Script.Engine import MakeTimespan
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.Widget_Options import Widget_Options
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetIsIntroSequenceDone
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.UMG import SetInputMode_UIOnlyEx
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Script.Engine import FormatArgumentData
from Script.FactoryGame import FGTutorialIntroManager
from Script.UMG import ESlateVisibility
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import BP_MenuBase
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_Back import Play_UI_MainMenu_Back
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.FactoryGame import FGGameUserSettings
from Script.FactoryGame import EndSkipIntroSequence
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.FactoryGame import Default__FGGameUserSettings
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import NATTypeToText
from Script.FactoryGame import GetCanSkipTutorial
from Script.FactoryGame import FGGameState
from Script.FactoryGame import Default__FGNetworkLibrary
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.BP_PauseWidget import ExecuteUbergraph_BP_PauseWidget.K2Node_CustomEvent_Confirm
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_Forward import Play_UI_MainMenu_Forward
from Script.Engine import LocalPlayer
from Script.Engine import BreakTimespan
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import Construct
from Script.Engine import Format
from Script.FactoryGame import NeedRespawn
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import OnEscape
from Script.UMG import WidgetAnimation
from Script.UMG import GetActiveWidgetIndex
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.FactoryGame import ApplyRestartRequiredChanges
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.BP_PauseWidget import ExecuteUbergraph_BP_PauseWidget
from Script.Engine import LaunchURL
from Script.FactoryGame import Suicide
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.Widget_GiveFeedback import Widget_GiveFeedback
from Script.FactoryGame import Default__FGSessionLibrary
from Script.Engine import GetGameState
from Script.UMG import Create
from Script.Engine import IsServer
from Script.FactoryGame import AddPopupWithCloseDelegate
from Script.FactoryGame import GetSessionName
from Script.AkAudio import AkComponent
from Script.FactoryGame import Default__FGTutorialIntroManager
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.BP_PauseWidget import ExecuteUbergraph_BP_PauseWidget.K2Node_CustomEvent_Confirm1
from Script.FactoryGame import FGOnlineSessionSettings
from Script.FactoryGame import GetTotalPlayDuration
from Script.Engine import QuitGame
from Script.FactoryGame import ResumeGame
from Script.FactoryGame import GetSessionSettings

class BP_PauseWidget(BP_MenuBase):
    PauseFade: Ptr[WidgetAnimation]
    OnSaveClicked: FMulticastScriptDelegate
    OnLoadClicked: FMulticastScriptDelegate
    OnOptionsClicked: FMulticastScriptDelegate
    mFeedbackWidget: Ptr[Widget_GiveFeedback]
    OnManagePlayersClicked: FMulticastScriptDelegate
    OnBackClicked: FMulticastScriptDelegate
    mHandleEscape = True
    bIsFocusable = True
    
    def CanDoServerAdministration(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: bool = self.IsIntroSequenceDone()
        
        valid = None
        Default__HUDHelpers.HasValidAdminInterface(ReturnValue, self, Ref[valid])
        ReturnValue_1: bool = ReturnValue_0 and valid
        canAdminister = ReturnValue_1
    

    def IsIntroSequenceDone(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGTutorialIntroManager] = Default__FGTutorialIntroManager.Get(ReturnValue)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L281')
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0 = Default__FGTutorialIntroManager.Get(ReturnValue)
        ReturnValue_2: bool = ReturnValue_0.GetIsIntroSequenceDone()
        ReturnValue_3: bool = ReturnValue_2
        goto('L292')
        # Label 281
        ReturnValue_3 = False
    

    def UpdateMenuItemVisibility(self):
        ExecutionFlow.Push("L951")
        ExecutionFlow.Push("L651")
        ReturnValue: bool = Default__KismetSystemLibrary.IsServer(self)
        if not ReturnValue:
            goto('L912')
        Variable4: uint8 = 0
        Variable5: uint8 = 1
        ReturnValue_0: bool = self.IsIntroSequenceDone()
        Variable2: bool = ReturnValue_0
        
        switch = {
            False: Variable5,
            True: Variable4
        }
        self.mRespawn.SetVisibility(switch.get(Variable2, None))
        
        switch_0 = {
            False: Variable5,
            True: Variable4
        }
        self.mInvites.SetVisibility(switch_0.get(Variable2, None))
        
        switch_1 = {
            False: Variable5,
            True: Variable4
        }
        self.mManageSesseion.SetVisibility(switch_1.get(Variable2, None))
        Variable2_0: uint8 = 0
        Variable3: uint8 = 2
        ReturnValue_1: Ptr[FGTutorialIntroManager] = Default__FGTutorialIntroManager.Get(self)
        ReturnValue_2: bool = ReturnValue_1.GetCanSkipTutorial()
        Variable1: bool = ReturnValue_2
        
        switch_2 = {
            False: Variable3,
            True: Variable2_0
        }
        self.mSkipIntro.SetVisibility(switch_2.get(Variable1, None))
        goto(ExecutionFlow.Pop())
        # Label 651
        Variable: uint8 = 0
        Variable1_0: uint8 = 1
        
        canAdminister = None
        self.CanDoServerAdministration(Ref[canAdminister])
        Variable_0: bool = canAdminister
        
        switch_3 = {
            False: Variable1_0,
            True: Variable
        }
        self.mSaveGame.SetVisibility(switch_3.get(Variable_0, None))
        
        switch_4 = {
            False: Variable1_0,
            True: Variable
        }
        self.mLoadGame.SetVisibility(switch_4.get(Variable_0, None))
        goto(ExecutionFlow.Pop())
        # Label 912
        self.mSkipIntro.SetVisibility(1)
        goto(ExecutionFlow.Pop())
    

    def UpdateHostNATText(self):
        ReturnValue: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        ReturnValue_0: BlueprintSessionResult = Default__FGSessionLibrary.GetMySession(ReturnValue)
        
        ReturnValue_1: FGOnlineSessionSettings = Default__FGSessionLibrary.GetSessionSettings(Ref[ReturnValue_0])
        ReturnValue_2: FText = Default__FGNetworkLibrary.NATTypeToText(ReturnValue_1.natType)
        FormatArgumentData.ArgumentName = "NATType"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_2
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 475, 'Value': 'Host NAT: {NATType}'}", Array)
        self.HostNAT.SetText(ReturnValue_3)
    

    def GetPlayDurationText(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue)
        bSuccess: bool = State
        if not bSuccess:
            goto('L1062')
        ReturnValue_0: int32 = State.GetTotalPlayDuration()
        ReturnValue_1: Timespan = MakeTimespan(0, 0, 0, ReturnValue_0, 0)
        
        Days = None
        Hours = None
        Minutes = None
        Seconds = None
        Milliseconds = None
        BreakTimespan(ReturnValue_1, Ref[Days], Ref[Hours], Ref[Minutes], Ref[Seconds], Ref[Milliseconds])
        FormatArgumentData.ArgumentName = "hours"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = Hours
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "sec"
        FormatArgumentData1.ArgumentValueType = 0
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = Seconds
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        FormatArgumentData2.ArgumentName = "min"
        FormatArgumentData2.ArgumentValueType = 0
        FormatArgumentData2.ArgumentValue = 
        FormatArgumentData2.ArgumentValueInt = Minutes
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData, FormatArgumentData2, FormatArgumentData1]
        ReturnValue_2: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 945, 'Value': 'Play Duration: {hours}h {min}m {sec}s'}", Array)
        ReturnValue_3: FText = ReturnValue_2
        goto('L1082')
        # Label 1062
        ReturnValue_3 = 
    

    def GetSessionNameText(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue)
        bSuccess: bool = State
        if not bSuccess:
            goto('L258')
        ReturnValue_0: FString = State.GetSessionName()
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_0)
        ReturnValue_2: FText = ReturnValue_1
    

    def DoResume(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        gameUI = None
        Default__HUDHelpers.GetFGGameUI(ReturnValue, self, Ref[gameUI])
        gameUI.ResumeGame()
    

    def OnEscape(self):
        self.ExecuteUbergraph_BP_PauseWidget(3587)
    

    def BndEvt__bResume_K2Node_ComponentBoundEvent_152_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BP_PauseWidget(1944)
    

    def BndEvt__bLoadGame_K2Node_ComponentBoundEvent_166_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BP_PauseWidget(174)
    

    def BndEvt__bRespawn_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BP_PauseWidget(279)
    

    def BndEvt__bSaveGame_K2Node_ComponentBoundEvent_3_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BP_PauseWidget(518)
    

    def Construct(self):
        self.ExecuteUbergraph_BP_PauseWidget(623)
    

    def BndEvt__bFeedback_K2Node_ComponentBoundEvent_53_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BP_PauseWidget(1469)
    

    def Event ExitToMainMenu(self, confirm: bool):
        ExecuteUbergraph_BP_PauseWidget.K2Node_CustomEvent_Confirm1 = confirm #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PauseWidget(2366)
    

    def Event ExitToDesktop(self, confirm: bool):
        ExecuteUbergraph_BP_PauseWidget.K2Node_CustomEvent_Confirm = confirm #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_PauseWidget(2715)
    

    def BndEvt__bExitMainMenu_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BP_PauseWidget(2824)
    

    def BndEvt__bExitDesktop_K2Node_ComponentBoundEvent_2_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BP_PauseWidget(2829)
    

    def BndEvt__mOptions_K2Node_ComponentBoundEvent_4_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BP_PauseWidget(2834)
    

    def BndEvt__bSkipIntro_K2Node_ComponentBoundEvent_5_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BP_PauseWidget(3257)
    

    def Destruct(self):
        self.ExecuteUbergraph_BP_PauseWidget(3365)
    

    def ExecuteUbergraph_BP_PauseWidget(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Default__KismetSystemLibrary.LaunchURL("https://questions.satisfactorygame.com/")
        ReturnValue7: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Forward, ReturnValue7, True)
        goto(ExecutionFlow.Pop())
        self.mFocusWidget = self.mLoadGame
        ReturnValue6: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Forward, ReturnValue6, True)
        goto(ExecutionFlow.Pop())
        ReturnValue14: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue14)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue: bool = Controller.NeedRespawn()
        if not ReturnValue:
            goto('L481')
        Controller.StartRespawn()
        # Label 466
        self.DoResume()
        goto(ExecutionFlow.Pop())
        # Label 481
        Controller.Suicide()
        goto('L466')
        self.mFocusWidget = self.mSaveGame
        ReturnValue3_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Forward, ReturnValue3_0, True)
        goto(ExecutionFlow.Pop())
        self.Construct()
        self.mFocusWidget = self.mResume
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__WidgetBlueprintLibrary.SetInputMode_UIOnlyEx(ReturnValue2, None, 0)
        ReturnValue2 = self.GetOwningPlayer()
        ReturnValue2.bShowMouseCursor = True
        ReturnValue15: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mFocusWidget.SetUserFocus(ReturnValue15)
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.PauseFade, 0, 1, 0, 1)
        self.UpdateHostNATText()
        self.UpdateMenuItemVisibility()
        ReturnValue1: Ptr[FGTutorialIntroManager] = Default__FGTutorialIntroManager.Get(self)
        OutputDelegate2.BindUFunction(self, UpdateMenuItemVisibility)
        ReturnValue1.mOnIntroSequenceStateUpdated.AddUnique(OutputDelegate2)
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 1069
        Array: List[Ptr[BP_MenuBase]] = [self.Widget_LoadSession, self.Widget_ManageInvites, self.Widget_ManageSession, self.Widget_SaveList]
        
        ReturnValue_2: int32 = len(Array)
        ReturnValue_3: bool = Variable <= ReturnValue_2
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L1395")
        Array = [self.Widget_LoadSession, self.Widget_ManageInvites, self.Widget_ManageSession, self.Widget_SaveList]
        
        Item = None
        Item = Array[Variable_0]
        Item.mOwningMenu = self
        goto(ExecutionFlow.Pop())
        # Label 1395
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L1069')
        goto('L15')
        # Label 1474
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__KismetSystemLibrary.QuitGame(self, ReturnValue_5, 0, False)
        ReturnValue9: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue6_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Back, ReturnValue9, True)
        goto(ExecutionFlow.Pop())
        # Label 1629
        self.OnEscape()
        ReturnValue_6: int32 = self.mSwitcher.GetActiveWidgetIndex()
        ReturnValue_7: bool = ReturnValue_6 != 0
        if not ReturnValue_7:
            goto('L1929')
        self.mSwitcher.SetActiveWidgetIndex(0)
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mFocusWidget.SetUserFocus(ReturnValue1_0)
        ReturnValue4_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Back, ReturnValue4_0, True)
        goto(ExecutionFlow.Pop())
        # Label 1929
        self.DoResume()
        goto(ExecutionFlow.Pop())
        self.DoResume()
        ReturnValue8: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Forward, ReturnValue8, True)
        goto(ExecutionFlow.Pop())
        # Label 2044
        ReturnValue5_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue2_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Back, ReturnValue5_0, True)
        goto(ExecutionFlow.Pop())
        # Label 2130
        OutputDelegate.BindUFunction(self, Event ExitToDesktop)
        ReturnValue10: Ptr[PlayerController] = self.GetOwningPlayer()
        
        OutputDelegate = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue10, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2219, 'Value': 'Exit to Desktop'}", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2274, 'Value': 'Are you sure you want to exit the game?'}", 1, None, None, Ref[OutputDelegate])
        goto(ExecutionFlow.Pop())
        if not Confirm1:
            goto('L2450')
        ReturnValue12: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__FGBlueprintFunctionLibrary.TravelToMainMenu(ReturnValue12)
        goto('L2044')
        # Label 2450
        self.RestoreFocusOnPopupClosed(False)
        goto(ExecutionFlow.Pop())
        # Label 2466
        OutputDelegate1.BindUFunction(self, Event ExitToMainMenu)
        ReturnValue11: Ptr[PlayerController] = self.GetOwningPlayer()
        
        OutputDelegate1 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue11, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2555, 'Value': 'Exit to Main Menu'}", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2612, 'Value': 'Are you sure you want to go back to the Main Menu?'}", 1, None, None, Ref[OutputDelegate1])
        goto(ExecutionFlow.Pop())
        if not Confirm:
            goto('L2808')
        ReturnValue_8: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        ReturnValue_8.ApplyRestartRequiredChanges()
        goto('L1474')
        # Label 2808
        self.RestoreFocusOnPopupClosed(False)
        goto(ExecutionFlow.Pop())
        goto('L2466')
        goto('L2130')
        ReturnValue_9: bool = Default__KismetSystemLibrary.IsValid(self.mOptions.mMenuSwitcherContainer_DEPRECATED)
        if not ReturnValue_9:
            goto('L2941')
        self.mFocusWidget = self.mOptions
        goto(ExecutionFlow.Pop())
        # Label 2941
        ReturnValue13: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_10: Ptr[Widget_Options] = Default__WidgetBlueprintLibrary.Create(self, Widget_Options, ReturnValue13)
        ReturnValue_11: Ptr[PanelSlot] = self.mSwitcher.AddChild(ReturnValue_10)
        self.mOptions.mSwitcherWidget = self.mSwitcher
        self.mOptions.mTargetWidget = ReturnValue_10
        self.mSwitcher.SetActiveWidget(ReturnValue_10)
        ReturnValue_10.mOwningMenu = self
        self.mFocusWidget = self.mOptions
        goto(ExecutionFlow.Pop())
        ReturnValue16: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_12: Ptr[FGTutorialIntroManager] = Default__FGTutorialIntroManager.Get(ReturnValue16)
        ReturnValue_12.EndSkipIntroSequence()
        goto(ExecutionFlow.Pop())
        self.Destruct()
        ReturnValue2_1: Ptr[FGTutorialIntroManager] = Default__FGTutorialIntroManager.Get(self)
        ReturnValue1_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue2_1)
        if not ReturnValue1_2:
           goto(ExecutionFlow.Pop())
        ReturnValue2_1 = Default__FGTutorialIntroManager.Get(self)
        OutputDelegate2.BindUFunction(self, UpdateMenuItemVisibility)
        ReturnValue2_1.mOnIntroSequenceStateUpdated.Remove(OutputDelegate2)
        goto(ExecutionFlow.Pop())
        goto('L1629')
    

    def OnBackClicked__DelegateSignature(self):
        pass
    

    def OnManagePlayersClicked__DelegateSignature(self):
        pass
    

    def OnOptionsClicked__DelegateSignature(self):
        pass
    

    def OnLoadClicked__DelegateSignature(self):
        pass
    

    def OnSaveClicked__DelegateSignature(self):
        pass
    
