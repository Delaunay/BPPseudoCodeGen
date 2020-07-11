
from codegen.ue4_stub import *

from Script.FactoryGame import FGLocalPlayer
from Script.FactoryGame import SaveHeader
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import FormatArgumentData
from Game.FactoryGame.Interface.UI.Menu.MainMenu.BP_MainMenuWidget import ExecuteUbergraph_BP_MainMenuWidget
from Script.UMG import ESlateVisibility
from Script.Engine import IsValid
from Script.FactoryGame import Default__FGSaveSystem
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import GetLoginState
from Script.Engine import Conv_StringToText
from Script.FactoryGame import NATTypeToText
from Game.FactoryGame.Interface.UI.Menu.MainMenu.BP_MainMenuWidget import ExecuteUbergraph_BP_MainMenuWidget.K2Node_CustomEvent_ConfirmClicked
from Script.FactoryGame import Default__FGNetworkLibrary
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import OnEscape
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import AddPopupWithCloseDelegate
from Script.Engine import GameInstance
from Script.Engine import EqualEqual_ByteByte
from Script.FactoryGame import GetFGGameUserSettings
from Script.FactoryGame import Default__FGMusicManager
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import BP_MenuBase
from Script.Engine import GetGameInstance
from Script.FactoryGame import FGGameUserSettings
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_Forward import Play_UI_MainMenu_Forward
from Script.UMG import GetActiveWidgetIndex
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import NotEqual_ByteByte
from Script.FactoryGame import GetCachedNATType
from Script.FactoryGame import EnumerateSaveGames
from Script.FactoryGame import LoadGame
from Script.FactoryGame import GetName
from Script.FactoryGame import Default__FGSaveSession
from Script.FactoryGame import GetSessionName
from Script.AkAudio import AkComponent
from Script.Engine import QuitGame
from Script.FactoryGame import GetGameVersion
from Script.FactoryGame import GetPlayDurationSeconds
from Script.FactoryGame import GetAdminInterface
from Script.UMG import SetUserFocus
from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Game.FactoryGame.Interface.UI.Menu.MainMenu.BP_MainMenuWidget import ExecuteUbergraph_BP_MainMenuWidget.K2Node_CustomEvent_Bool
from Script.FactoryGame import ELoginState
from Script.Engine import LatentActionInfo
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import OnMenuEnter
from Script.FactoryGame import GetVersionString
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_Back import Play_UI_MainMenu_Back
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import ECachedNATType
from Script.FactoryGame import SessionSaveStruct
from Script.FactoryGame import FGPlayerControllerBase
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import Construct
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.Menu.MainMenu.BP_MainMenuWidget import ExecuteUbergraph_BP_MainMenuWidget.K2Node_CustomEvent_oldState
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.Interface.UI.Menu.MainMenu.BP_MainMenuWidget import ExecuteUbergraph_BP_MainMenuWidget.K2Node_Event_prevMenu
from Script.FactoryGame import SortSessions
from Script.FactoryGame import Default__FGVersionFunctionLibrary
from Script.FactoryGame import FGMusicManager
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import Destruct
from Game.FactoryGame.Interface.UI.Menu.MainMenu.BP_MainMenuWidget import ExecuteUbergraph_BP_MainMenuWidget.K2Node_CustomEvent_newState
from Game.FactoryGame.Interface.UI.Menu.MainMenu.BP_MainMenuWidget import ExecuteUbergraph_BP_MainMenuWidget.K2Node_CustomEvent_natType
from Script.FactoryGame import GetUsername
from Script.Engine import Len
from Script.FactoryGame import ESaveState
from Script.FactoryGame import Default__FGGameUserSettings
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_LaunchGame import Play_UI_MainMenu_LaunchGame
from Script.FactoryGame import GetSaveState
from Script.FactoryGame import EGameVersion
from Script.FactoryGame import ApplyRestartRequiredChanges
from Script.FactoryGame import FGGameInstance
from Script.FactoryGame import FGAdminInterface
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import GroupSavesPerSession
from Script.Engine import LocalPlayer

class BP_MainMenuWidget(BP_MenuBase):
    OnPlayClicked: FMulticastScriptDelegate
    OnBrowseClicked: FMulticastScriptDelegate
    OnExitClicked: FMulticastScriptDelegate
    OnLoadClicked: FMulticastScriptDelegate
    OnOptionsClicked: FMulticastScriptDelegate
    OnModsClicked: FMulticastScriptDelegate
    OnCreditsClicked: FMulticastScriptDelegate
    mRecentSave: SaveHeader
    mHandleEscape = True
    
    def OnSavesEnumerated(self, success: bool, saves: Ref[List[SaveHeader]]):
        ExecutionFlow.Push("L638")
        ExecutionFlow.Push("L567")
        if not success:
            goto('L605')
        
        ReturnValue: int32 = len(saves)
        ReturnValue_0: bool = ReturnValue > 0
        if not ReturnValue_0:
            goto('L605')
        groupedBySession: List[SessionSaveStruct] = []
        
        Default__FGSaveSystem.GroupSavesPerSession(Ref[saves], Ref[groupedBySession])
        
        Default__FGSaveSystem.SortSessions(1, 1, Ref[groupedBySession])
        
        groupedBySession[0].SaveHeaders = None
        Item = None
        Item = groupedBySession[0].SaveHeaders[0]
        
        Item = None
        ReturnValue_1: FString = Default__FGSaveSession.GetSessionName(Ref[Item])
        ReturnValue_2: int32 = Default__KismetStringLibrary.Len(ReturnValue_1)
        ReturnValue1: bool = ReturnValue_2 > 0
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        
        groupedBySession[0].SaveHeaders = None
        Item = None
        Item = groupedBySession[0].SaveHeaders[0]
        self.mRecentSave = Item
        goto(ExecutionFlow.Pop())
        # Label 567
        self.SetContinueButtonVisibility(self.mRecentSave)
        self.GetMostRecentSaveName()
        goto(ExecutionFlow.Pop())
        # Label 605
        self.mRecentSave = SaveHeader()
        goto(ExecutionFlow.Pop())
    

    def SetContinueButtonVisibility(self, recentSave: SaveHeader):
        
        ReturnValue: int32 = Default__FGSaveSession.GetPlayDurationSeconds(Ref[recentSave])
        ReturnValue_0: bool = ReturnValue > 0
        if not ReturnValue_0:
            goto('L150')
        self.mButtonContinue.SetVisibility(0)
        # End
        # Label 150
        self.mButtonContinue.SetVisibility(1)
    

    def GetMostRecentSaveName(self):
        
        ReturnValue: FString = Default__FGSaveSession.GetName(Ref[self.mRecentSave])
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue)
        FormatArgumentData1.ArgumentName = "A"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue1
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData1]
        ReturnValue1_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 377, 'Value': 'Latest Save: {A}'}", Array1)
        self.mButtonContinue.mSaveNameTextBlock.SetText(ReturnValue1_0)
        
        ReturnValue_0: FString = Default__FGSaveSession.GetSessionName(Ref[self.mRecentSave])
        # Label 567
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_0)
        FormatArgumentData.ArgumentName = "A"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_1
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_2: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 885, 'Value': 'Session Name: {A}'}", Array)
        self.mButtonContinue.mSessionNameTextBlock.SetText(ReturnValue_2)
    

    def GetExperimentalVisibility(self):
        Variable: uint8 = 3
        Variable1: uint8 = 1
        ReturnValue: uint8 = Default__FGVersionFunctionLibrary.GetGameVersion()
        ReturnValue_0: bool = EqualEqual_ByteByte(ReturnValue, 1)
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mExperimentalBuildLabel.SetVisibility(switch.get(Variable_0, None))
    

    def UpdateUsername(self):
        ReturnValue: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue)
        bSuccess: bool = Player
        ReturnValue_0: uint8 = Player.GetLoginState()
        CmpSuccess: bool = NotEqual_ByteByte(ReturnValue_0, 0)
        if not CmpSuccess:
            goto('L324')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_0, 1)
        if not CmpSuccess:
            goto('L556')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_0, 2)
        if not CmpSuccess:
            goto('L740')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_0, 3)
        if not CmpSuccess:
            goto('L324')
        # End
        # Label 324
        Array1: List[FormatArgumentData] = [FormatArgumentData(ArgumentName = "", ArgumentValueType = 0, ArgumentValue = , ArgumentValueInt = 0, ArgumentValueFloat = 0, ArgumentValueGender = 0)]
        ReturnValue1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 418, 'Value': 'Not Logged In'}", Array1)
        loginText: FText = ReturnValue1
        # Label 506
        self.UsernameLabel.SetText(loginText)
        # End
        # Label 556
        Array: List[FormatArgumentData] = [FormatArgumentData(ArgumentName = "", ArgumentValueType = 0, ArgumentValue = , ArgumentValueInt = 0, ArgumentValueFloat = 0, ArgumentValueGender = 0)]
        ReturnValue_1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 650, 'Value': 'Logging In'}", Array)
        loginText = ReturnValue_1
        goto('L506')
        # Label 740
        Array2: List[FormatArgumentData] = [FormatArgumentData(ArgumentName = "", ArgumentValueType = 0, ArgumentValue = , ArgumentValueInt = 0, ArgumentValueFloat = 0, ArgumentValueGender = 0)]
        ReturnValue = self.GetOwningLocalPlayer()
        Player = Cast[FGLocalPlayer](ReturnValue)
        bSuccess = Player
        ReturnValue_2: FString = Player.GetUsername()
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_2)
        FormatArgumentData.ArgumentName = "username"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_3
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array3: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue2: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1247, 'Value': 'Logged in as: {username}'}", Array3)
        ReturnValue3: FText = Default__KismetTextLibrary.Format(ReturnValue2, Array2)
        loginText = ReturnValue3
        goto('L506')
    

    def UpdateVersionString(self):
        ReturnValue: Ptr[GameInstance] = Default__GameplayStatics.GetGameInstance(self)
        ReturnValue_0: uint8 = Default__FGNetworkLibrary.GetCachedNATType(ReturnValue)
        ReturnValue_1: bool = NotEqual_ByteByte(ReturnValue_0, 3)
        if not ReturnValue_1:
            goto('L1034')
        ReturnValue_2: FString = Default__FGVersionFunctionLibrary.GetVersionString()
        ReturnValue = Default__GameplayStatics.GetGameInstance(self)
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_2)
        FormatArgumentData.ArgumentName = "Version"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_3
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue1: uint8 = Default__FGNetworkLibrary.GetCachedNATType(ReturnValue)
        ReturnValue_4: FText = Default__FGNetworkLibrary.NATTypeToText(ReturnValue1)
        FormatArgumentData1.ArgumentName = "NATType"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue_4
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_5: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 885, 'Value': 'NAT: {NATType} {Version}'}", Array)
        versionString: FText = ReturnValue_5
        # Label 984
        self.VersionString.SetText(versionString)
        # End
        # Label 1034
        ReturnValue1_0: FString = Default__FGVersionFunctionLibrary.GetVersionString()
        ReturnValue1_1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue1_0)
        FormatArgumentData2.ArgumentName = "Version"
        FormatArgumentData2.ArgumentValueType = 4
        FormatArgumentData2.ArgumentValue = ReturnValue1_1
        FormatArgumentData2.ArgumentValueInt = 0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData2]
        ReturnValue1_2: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1408, 'Value': '{Version}'}", Array1)
        versionString = ReturnValue1_2
        goto('L984')
    

    def CacheMostRecentSave(self):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Base: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue)
        bSuccess: bool = Base
        if not bSuccess:
            goto('L317')
        ReturnValue_0: Ptr[FGAdminInterface] = Base.GetAdminInterface()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L317')
        OutputDelegate.BindUFunction(self, OnSavesEnumerated)
        ReturnValue_0 = Base.GetAdminInterface()
        ReturnValue_0.EnumerateSaveGames(True, OutputDelegate)
    

    def GetVersionString(self):
        ReturnValue: FString = Default__FGVersionFunctionLibrary.GetVersionString()
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue)
        ReturnValue_1: FText = ReturnValue_0
    

    def OnEscape(self):
        self.ExecuteUbergraph_BP_MainMenuWidget(537)
    

    def BndEvt__mButtonQuit_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BP_MainMenuWidget(829)
    

    def Construct(self):
        self.ExecuteUbergraph_BP_MainMenuWidget(1062)
    

    def BndEvt__mButtonContinue_K2Node_ComponentBoundEvent_0_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BP_MainMenuWidget(1745)
    

    def BndEvt__mButtonMP_K2Node_ComponentBoundEvent_3_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_BP_MainMenuWidget(3268)
    

    def OnExit(self, bool: bool):
        ExecuteUbergraph_BP_MainMenuWidget.K2Node_CustomEvent_Bool = bool #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_MainMenuWidget(3373)
    

    def NATTypeUpdated(self, natType: uint8):
        ExecuteUbergraph_BP_MainMenuWidget.K2Node_CustomEvent_natType = natType #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_MainMenuWidget(3482)
    

    def Destruct(self):
        self.ExecuteUbergraph_BP_MainMenuWidget(3497)
    

    def OnMenuEnter(self):
        ExecuteUbergraph_BP_MainMenuWidget.K2Node_Event_prevMenu = prevMenu #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_MainMenuWidget(3857)
    

    def LoginStateChanged(self, oldState: uint8, newState: uint8):
        ExecuteUbergraph_BP_MainMenuWidget.K2Node_CustomEvent_oldState = oldState #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_MainMenuWidget.K2Node_CustomEvent_newState = newState #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_MainMenuWidget(3881)
    

    def BndEvt__mButtonContinue_K2Node_ComponentBoundEvent_1_OnHovered__DelegateSignature(self):
        self.ExecuteUbergraph_BP_MainMenuWidget(3896)
    

    def BndEvt__mButtonContinue_K2Node_ComponentBoundEvent_2_OnUnhovered__DelegateSignature(self):
        self.ExecuteUbergraph_BP_MainMenuWidget(4063)
    

    def ClosedLoadPopup(self, ConfirmClicked: bool):
        ExecuteUbergraph_BP_MainMenuWidget.K2Node_CustomEvent_ConfirmClicked = ConfirmClicked #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_MainMenuWidget(4212)
    

    def ExecuteUbergraph_BP_MainMenuWidget(self):
        goto(ComputedJump("EntryPoint"))
        self.mButtonContinue.Widget_ButtonShine.PlayShineAnim()
        self.mButtonContinue.Widget_AutoScrollingContainer.StartAutoScroll()
        goto(ExecutionFlow.Pop())
        # Label 132
        Variable: int32 = 0
        # Label 155
        Array: List[Ptr[BP_MenuBase]] = [self.Widget_LoadSession, self.Widget_ManageInvites, self.Widget_Options]
        
        ReturnValue: int32 = len(Array)
        ReturnValue_0: bool = Variable_0 <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable = Variable_0
        ExecutionFlow.Push("L463")
        Array = [self.Widget_LoadSession, self.Widget_ManageInvites, self.Widget_Options]
        
        Item = None
        Item = Array[Variable]
        Item.mOwningMenu = self
        goto(ExecutionFlow.Pop())
        # Label 463
        ReturnValue_1: int32 = Variable_0 + 1
        Variable_0: int32 = ReturnValue_1
        goto('L155')
        self.OnEscape()
        ReturnValue_2: int32 = self.mSwitcher.GetActiveWidgetIndex()
        ReturnValue_3: bool = ReturnValue_2 != 0
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        self.mSwitcher.SetActiveWidget(None)
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mFocusWidget.SetUserFocus(ReturnValue1)
        ReturnValue4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Back, ReturnValue4, True)
        goto(ExecutionFlow.Pop())
        ReturnValue7: Ptr[PlayerController] = self.GetOwningPlayer()
        OutputDelegate1.BindUFunction(self, OnExit)
        
        OutputDelegate1 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue7, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 918, 'Value': 'Exiting Game'}", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 970, 'Value': 'Are you sure you want to quit the game?'}", 1, None, None, Ref[OutputDelegate1])
        goto(ExecutionFlow.Pop())
        self.Construct()
        self.mFocusWidget = self.mButtonContinue
        self.CacheMostRecentSave()
        self.UpdateVersionString()
        self.UpdateUsername()
        self.GetExperimentalVisibility()
        ReturnValue_4: Ptr[GameInstance] = Default__GameplayStatics.GetGameInstance(self)
        Instance: Ptr[FGGameInstance] = Cast[FGGameInstance](ReturnValue_4)
        bSuccess: bool = Instance
        if not bSuccess:
            goto('L1333')
        OutputDelegate3.BindUFunction(self, NATTypeUpdated)
        Instance.mOnNatTypeUpdated.AddUnique(OutputDelegate3)
        # Label 1333
        ReturnValue_5: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue_5)
        bSuccess2: bool = Player
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        OutputDelegate.BindUFunction(self, LoginStateChanged)
        Player.mOnLoginStateChanged.AddUnique(OutputDelegate)
        Variable_0 = 0
        goto('L132')
        # Label 1524
        ReturnValue_6: Ptr[PlayerController] = self.GetOwningPlayer()
        self.mFocusWidget.SetUserFocus(ReturnValue_6)
        goto(ExecutionFlow.Pop())
        # Label 1590
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__KismetSystemLibrary.QuitGame(self, ReturnValue2, 0, False)
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_7: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Back, ReturnValue3, True)
        goto(ExecutionFlow.Pop())
        ReturnValue_8: Ptr[FGMusicManager] = Default__FGMusicManager.Get(self)
        ReturnValue_8.Stop()
        ReturnValue5: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue2_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_LaunchGame, ReturnValue5, True)
        
        ReturnValue_9: uint8 = Default__FGSaveSystem.GetSaveState(Ref[self.mRecentSave])
        CmpSuccess: bool = NotEqual_ByteByte(ReturnValue_9, 0)
        if not CmpSuccess:
            goto('L2149')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_9, 1)
        if not CmpSuccess:
            goto('L2414')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_9, 2)
        if not CmpSuccess:
            goto('L2699')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_9, 3)
        if not CmpSuccess:
            goto('L2986')
        goto(ExecutionFlow.Pop())
        # Label 2149
        ReturnValue8: Ptr[PlayerController] = self.GetOwningPlayer()
        
        Variable_1 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue8, STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/SaveTable.SaveTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2280, 'Value': 'UnsupportedSaveHeader'}", STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/SaveTable.SaveTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2370, 'Value': 'UnsupportedSaveBody'}", 0, None, ReturnValue8, Ref[Variable_1])
        goto(ExecutionFlow.Pop())
        # Label 2414
        OutputDelegate4.BindUFunction(self, ClosedLoadPopup)
        ReturnValue8 = self.GetOwningPlayer()
        
        OutputDelegate4 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue8, STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/SaveTable.SaveTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2568, 'Value': 'VolatileSaveHeader'}", STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/SaveTable.SaveTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2655, 'Value': 'VolatileSaveVersion'}", 1, None, ReturnValue8, Ref[OutputDelegate4])
        goto(ExecutionFlow.Pop())
        # Label 2699
        ReturnValue8 = self.GetOwningPlayer()
        Base: Ptr[FGPlayerControllerBase] = Cast[FGPlayerControllerBase](ReturnValue8)
        bSuccess4: bool = Base
        if not bSuccess4:
           goto(ExecutionFlow.Pop())
        ReturnValue_10: Ptr[FGAdminInterface] = Base.GetAdminInterface()
        ReturnValue_11: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_10)
        if not ReturnValue_11:
           goto(ExecutionFlow.Pop())
        ReturnValue_10 = Base.GetAdminInterface()
        
        ReturnValue_10.LoadGame(False, Ref[self.mRecentSave])
        goto(ExecutionFlow.Pop())
        # Label 2986
        OutputDelegate4.BindUFunction(self, ClosedLoadPopup)
        ReturnValue8 = self.GetOwningPlayer()
        
        OutputDelegate4 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue8, STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/SaveTable.SaveTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 3140, 'Value': 'VolatileSaveHeader'}", STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/Menu/SaveTable.SaveTable", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 3227, 'Value': 'NewerSaveVersion'}", 1, None, ReturnValue8, Ref[OutputDelegate4])
        goto(ExecutionFlow.Pop())
        self.mFocusWidget = self.mButtonCredits
        ReturnValue6: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue3_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_Forward, ReturnValue6, True)
        goto(ExecutionFlow.Pop())
        if not Bool:
            goto('L3466')
        ReturnValue_12: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        ReturnValue_12.ApplyRestartRequiredChanges()
        goto('L1590')
        # Label 3466
        self.RestoreFocusOnPopupClosed(False)
        goto(ExecutionFlow.Pop())
        self.UpdateVersionString()
        goto(ExecutionFlow.Pop())
        self.Destruct()
        ReturnValue1_1: Ptr[GameInstance] = Default__GameplayStatics.GetGameInstance(self)
        Instance1: Ptr[FGGameInstance] = Cast[FGGameInstance](ReturnValue1_1)
        bSuccess1: bool = Instance1
        if not bSuccess1:
            goto('L3693')
        OutputDelegate2.BindUFunction(self, NATTypeUpdated)
        Instance1.mOnNatTypeUpdated.Remove(OutputDelegate2)
        # Label 3693
        ReturnValue1_2: Ptr[LocalPlayer] = self.GetOwningLocalPlayer()
        Player1: Ptr[FGLocalPlayer] = Cast[FGLocalPlayer](ReturnValue1_2)
        bSuccess3: bool = Player1
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        OutputDelegate5.BindUFunction(self, LoginStateChanged)
        Player1.mOnLoginStateChanged.Remove(OutputDelegate5)
        goto(ExecutionFlow.Pop())
        self.OnMenuEnter(prevMenu)
        goto('L1524')
        self.UpdateUsername()
        goto(ExecutionFlow.Pop())
        ReturnValue_13: Ptr[UMGSequencePlayer] = self.mButtonContinue.PlayAnimation(self.mButtonContinue.ani_ShowSaveName, 0, 1, 0, 1)
        Default__KismetSystemLibrary.Delay(self, 0.30000001192092896, LatentActionInfo(Linkage = 15, UUID = -727381504, ExecutionFunction = "ExecuteUbergraph_BP_MainMenuWidget", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue1_3: Ptr[UMGSequencePlayer] = self.mButtonContinue.PlayAnimation(self.mButtonContinue.ani_HideSaveName, 0, 1, 0, 1)
        self.mButtonContinue.Widget_AutoScrollingContainer.StopAutoScroll()
        goto(ExecutionFlow.Pop())
        if not ConfirmClicked:
           goto(ExecutionFlow.Pop())
        goto('L2699')
    

    def OnCreditsClicked__DelegateSignature(self):
        pass
    

    def OnModsClicked__DelegateSignature(self):
        pass
    

    def OnOptionsClicked__DelegateSignature(self):
        pass
    

    def OnLoadClicked__DelegateSignature(self):
        pass
    

    def OnExitClicked__DelegateSignature(self):
        pass
    

    def OnBrowseClicked__DelegateSignature(self):
        pass
    

    def OnPlayClicked__DelegateSignature(self):
        pass
    
