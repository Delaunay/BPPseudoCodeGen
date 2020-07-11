
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Game.FactoryGame.Interface.UI.Menu.Widget_AreaSelection_Button import Widget_AreaSelection_Button
from Script.AkAudio import PostAkEvent
from Script.UMG import CanvasPanelSlot
from Script.UMG import SetAlignment
from Script.Engine import NotEqual_BoolBool
from Script.FactoryGame import CreateSessionAndTravelToMap
from Script.FactoryGame import FGSaveSystem
from Script.FactoryGame import Default__FGMusicManager
from Script.UMG import SetAutoSize
from Game.FactoryGame.Interface.UI.Menu.Widget_PlayMenu_Alpha import ExecuteUbergraph_Widget_PlayMenu_Alpha.K2Node_ComponentBoundEvent_Text
from Script.Engine import Not_PreBool
from Script.FactoryGame import SetSkipOnboarding
from Game.FactoryGame.Interface.UI.Menu.Widget_PlayMenu_Alpha import ExecuteUbergraph_Widget_PlayMenu_Alpha.K2Node_Event_IsDesignTime
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.Engine import SetStructurePropertyByName
from Script.UMG import GetChildAt
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import PlayAnimation
from Script.FactoryGame import ESessionVisibility
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.Menu.Widget_PlayMenu_Alpha import ExecuteUbergraph_Widget_PlayMenu_Alpha.K2Node_Event_prevMenu
from Script.FactoryGame import IsSessionNameUsed
from Script.Engine import GetGameInstance
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import BP_MenuBase
from Script.Engine import Len
from Script.UMG import StopAnimation
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import OnMenuEnter
from Script.FactoryGame import Default__FGSaveSystem
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import SetAnchors
from Game.FactoryGame.-Shared.Blueprint.BP_OnlineHelpers import Default__BP_OnlineHelpers
from Script.Engine import SetFloatPropertyByName
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import IsValidSaveName
from Script.Engine import Default__GameplayStatics
from Script.Engine import NotEqual_StrStr
from Script.UMG import Widget
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import Construct
from Game.FactoryGame.Interface.UI.Audio.MainMenu.Play_UI_MainMenu_LaunchGame import Play_UI_MainMenu_LaunchGame
from Script.Engine import Concat_StrStr
from Game.FactoryGame.Interface.UI.Menu.BP_MenuBase import OnEscape
from Script.UMG import GetText
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import WidgetAnimation
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.FactoryGame import FGGameInstance
from Game.FactoryGame.Interface.UI.Menu.Widget_PlayMenu_Alpha import ExecuteUbergraph_Widget_PlayMenu_Alpha
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Script.CoreUObject import Vector2D
from Game.FactoryGame.Interface.UI.Menu.Widget_PlayMenu_Alpha import ExecuteUbergraph_Widget_PlayMenu_Alpha.K2Node_CustomEvent_mStartingLocs
from Script.UMG import SetPosition
from Script.AkAudio import AkComponent
from Game.FactoryGame.Interface.UI.Menu.StartingLocationsDataStruct import StartingLocationsDataStruct
from Script.Engine import GameInstance
from Script.FactoryGame import FGMusicManager
from Script.UMG import AddChildToCanvas
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor
from Game.FactoryGame.Interface.UI.Menu.Widget_PlayMenu_Alpha import ExecuteUbergraph_Widget_PlayMenu_Alpha.K2Node_ComponentBoundEvent_SelectedOption

class Widget_PlayMenu_Alpha(BP_MenuBase):
    ErrorPulse: Ptr[WidgetAnimation]
    StartButtonEnable: Ptr[WidgetAnimation]
    StartButtonPulseAnim: Ptr[WidgetAnimation]
    Spawn: Ptr[WidgetAnimation]
    mStartLoc: FString
    mOptionString: FString
    mSelectedVisibility: uint8
    mSelectedLocation: StartingLocationsDataStruct
    mDefaultStartingLocation: int32
    mPlayButtonError: bool
    mPlayButtonErrorString: FText
    mPlayButtonEnabled: bool
    mStartingLocations: List[StartingLocationsDataStruct] = [{'Name_15_B24B9E3F4D2123245CD4C3AC88089645': 'NSLOCTEXT("", "775E4EBE4EB4DCEE3BDF9B942311DFE7", "Grass Fields")', 'Description_16_FC7E65A7491E131F357F18A1353545CB': 'NSLOCTEXT("", "72F2580D4BDD98AC33CD119A270AD508", "A large area that is open and flat with frequent patches of biomass, making building easier but distances longer.")', 'Image_17_BEFE2AB0455E5D921A998EB9F17BDDC1': {'$AssetPath': '/Game/FactoryGame/Interface/UI/Menu/Graphics/GrassFields_Area.GrassFields_Area'}, 'StartLocString_11_9994B8C8428E92F9965D6BA3CB30CE96': '?startloc=Grass Fields'}, {'Name_15_B24B9E3F4D2123245CD4C3AC88089645': 'NSLOCTEXT("", "037CEA694E63119673BE41ABAA3F8B54", "Northern Forest")', 'Description_16_FC7E65A7491E131F357F18A1353545CB': 'NSLOCTEXT("", "F34E505D4BFFC2901460E7AB028CDB82", "A small but lush mountainous area surrounded by varied biomes, making building harder but biomass a common resource.")', 'Image_17_BEFE2AB0455E5D921A998EB9F17BDDC1': {'$AssetPath': '/Game/FactoryGame/Interface/UI/Menu/Graphics/NorthernForest_Area.NorthernForest_Area'}, 'StartLocString_11_9994B8C8428E92F9965D6BA3CB30CE96': '?startloc=Northern Forest'}, {'Name_15_B24B9E3F4D2123245CD4C3AC88089645': 'NSLOCTEXT("", "FF935BCA4A1BFB2AF86E15A0834724FF", "Dune Desert")', 'Description_16_FC7E65A7491E131F357F18A1353545CB': 'NSLOCTEXT("", "28B92614484D0F3047246596090D5AAD", "A harsh starting point with large, open spaces, vast distances, and very contained foliage locations.")', 'Image_17_BEFE2AB0455E5D921A998EB9F17BDDC1': {'$AssetPath': '/Game/FactoryGame/Interface/UI/Menu/Graphics/DuneDesert_Area.DuneDesert_Area'}, 'StartLocString_11_9994B8C8428E92F9965D6BA3CB30CE96': '?startloc=DuneDesert'}, {'Name_15_B24B9E3F4D2123245CD4C3AC88089645': 'NSLOCTEXT("", "6AEA6CEA42B555CD7009B694CF79B07F", "Rocky Desert")', 'Description_16_FC7E65A7491E131F357F18A1353545CB': 'NSLOCTEXT("", "E405348947E49C17B03C579E047B4F63", "A barren, medium-sized area bordering the sea which is mostly flat, with nicely balanced distances and building opportunities, but limited biomass.")', 'Image_17_BEFE2AB0455E5D921A998EB9F17BDDC1': {'$AssetPath': '/Game/FactoryGame/Interface/UI/Menu/Graphics/RockyDesert_Area.RockyDesert_Area'}, 'StartLocString_11_9994B8C8428E92F9965D6BA3CB30CE96': 'startloc=Rocky Desert'}]
    
    def InitStartingLocs(self):
        ExecutionFlow.Push("L1805")
        ButtonWidth = 300
        ButtonSpacing = 20
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 97
        ReturnValue1: int32 = len(self.mStartingLocations)
        ReturnValue: bool = Variable <= ReturnValue1
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L1697")
        LocalIndex = Variable_0
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[Widget_AreaSelection_Button] = Default__WidgetBlueprintLibrary.Create(self, Widget_AreaSelection_Button, ReturnValue_0)
        
        Item = None
        Item = self.mStartingLocations[Variable_0]
        
        Item = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_1, "mStartingLocs", Ref[Item])
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue_1, "mWidth", ButtonWidth)
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue_1, "mSpacing", ButtonSpacing)
        localAreaSelectionButton = ReturnValue_1
        ReturnValue_2: Ptr[CanvasPanelSlot] = self.mStartingLocationsPanel.AddChildToCanvas(localAreaSelectionButton)
        localCanvasPanelSlot = ReturnValue_2
        localCanvasPanelSlot.SetAutoSize(True)
        Anchors.Minimum = Vector2D(X = 0.5, Y = 0.5)
        Anchors.Maximum = Vector2D(X = 0.5, Y = 0.5)
        localCanvasPanelSlot.SetAnchors(Anchors)
        localCanvasPanelSlot.SetAlignment(Vector2D(X = 0.5, Y = 0.5))
        ReturnValue_3: float = ButtonSpacing * 2
        ReturnValue_4: float = ButtonWidth + ReturnValue_3
        ReturnValue1_0: float = ButtonSpacing * 2
        ReturnValue1_1: float = ButtonWidth + ReturnValue1_0
        
        ReturnValue_5: int32 = len(self.mStartingLocations)
        ReturnValue_6: float = LocalIndex * ReturnValue_4
        ReturnValue_7: int32 = ReturnValue_5 - 1
        ReturnValue1_2: float = ReturnValue_7 * ReturnValue1_1
        ReturnValue_8: float = ReturnValue1_2 / 2
        ReturnValue_9: float = ReturnValue_6 - ReturnValue_8
        ReturnValue_10: Vector2D = Vector2D(ReturnValue_9, 0)
        localCanvasPanelSlot.SetPosition(ReturnValue_10)
        OutputDelegate.BindUFunction(self, OnStartLocClicked)
        localAreaSelectionButton.OnClicked.AddUnique(OutputDelegate)
        ReturnValue_11: bool = EqualEqual_IntInt(self.mDefaultStartingLocation, LocalIndex)
        if not ReturnValue_11:
            goto('L1771')
        localAreaSelectionButton.SetSelected(True)
        
        Item = None
        Item = self.mStartingLocations[Variable_0]
        self.mSelectedLocation = Item
        goto(ExecutionFlow.Pop())
        # Label 1697
        ReturnValue_12: int32 = Variable + 1
        Variable = ReturnValue_12
        goto('L97')
        # Label 1771
        localAreaSelectionButton.mIsSelected = False
        goto(ExecutionFlow.Pop())
    

    def SetStartButtonEnable(self, Enabled: bool):
        LocalIsEnabled = Enabled
        ReturnValue: bool = NotEqual_BoolBool(LocalIsEnabled, self.mPlayButtonEnabled)
        if not ReturnValue:
            goto('L414')
        self.mPlayButtonEnabled = LocalIsEnabled
        Variable: uint8 = 0
        Variable1: uint8 = 3
        Variable_0: bool = LocalIsEnabled
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mStartGame.SetVisibility(switch.get(Variable_0, None))
        if not LocalIsEnabled:
            goto('L349')
        ReturnValue2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.StartButtonPulseAnim, 0, 0, 0, 1)
        ReturnValue_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.StartButtonEnable, 0, 1, 0, 1)
        # End
        # Label 349
        self.StopAnimation(self.StartButtonPulseAnim)
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.StartButtonEnable, 0, 1, 1, 1)
    

    def CheckSessionNameForError(self):
        ReturnValue: FText = self.mSessionNameInput.GetText()
        
        ReturnValue_0: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue])
        sessionName: FString = ReturnValue_0
        ReturnValue_1: int32 = Default__KismetStringLibrary.Len(sessionName)
        ReturnValue_2: bool = ReturnValue_1 > 2
        if not ReturnValue_2:
            goto('L574')
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[FGSaveSystem] = Default__FGSaveSystem.Get(ReturnValue1)
        ReturnValue_3: bool = ReturnValue1_0.IsValidSaveName(sessionName)
        if not ReturnValue_3:
            goto('L680')
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: Ptr[FGSaveSystem] = Default__FGSaveSystem.Get(ReturnValue_4)
        ReturnValue_6: bool = ReturnValue_5.IsSessionNameUsed(sessionName)
        ReturnValue_7: bool = Not_PreBool(ReturnValue_6)
        if not ReturnValue_7:
            goto('L793')
        self.SetPlayButtonError(False, )
        # End
        # Label 574
        self.SetPlayButtonError(True, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 590, 'Value': 'Session name needs to be at least 3 characters'}")
        # End
        # Label 680
        self.SetPlayButtonError(True, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 696, 'Value': 'Session contains illegal characters or reserved names'}")
        # End
        # Label 793
        self.SetPlayButtonError(True, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 809, 'Value': 'Session name already in use'}")
    

    def SetPlayButtonError(self, Error: bool, errorMessage: FText):
        self.mPlayButtonError = Error
        self.mPlayButtonErrorString = errorMessage
        ReturnValue: bool = Not_PreBool(self.mPlayButtonError)
        self.SetStartButtonEnable(ReturnValue)
        if not self.mPlayButtonError:
            goto('L200')
        self.mErrorLabel.SetVisibility(0)
        self.mErrorLabel.SetText(self.mPlayButtonErrorString)
        # End
        # Label 200
        self.mErrorLabel.SetVisibility(2)
    

    def OnEscape(self):
        self.ExecuteUbergraph_Widget_PlayMenu_Alpha(15)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_PlayMenu_Alpha(609)
    

    def BndEvt__Widget_Options_DropdownBox_K2Node_ComponentBoundEvent_2_onSelectionChanged__DelegateSignature(self, SelectedOption: FString):
        ExecuteUbergraph_Widget_PlayMenu_Alpha.K2Node_ComponentBoundEvent_SelectedOption = SelectedOption #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayMenu_Alpha(1256)
    

    def OnStartLocClicked(self, mStartingLocs: StartingLocationsDataStruct):
        ExecuteUbergraph_Widget_PlayMenu_Alpha.K2Node_CustomEvent_mStartingLocs = mStartingLocs #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayMenu_Alpha(1737)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_PlayMenu_Alpha.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayMenu_Alpha(1822)
    

    def BndEvt__mStartGame_K2Node_ComponentBoundEvent_4_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PlayMenu_Alpha(1837)
    

    def BndEvt__mStartGame_K2Node_ComponentBoundEvent_5_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PlayMenu_Alpha(1876)
    

    def BndEvt__EditableTextBox_0_K2Node_ComponentBoundEvent_6_OnEditableTextBoxChangedEvent__DelegateSignature(self, text: Const[Ref[FText]]):
        ExecuteUbergraph_Widget_PlayMenu_Alpha.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayMenu_Alpha(1915)
    

    def BndEvt__mStartGame_K2Node_ComponentBoundEvent_7_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PlayMenu_Alpha(1920)
    

    def OnMenuEnter(self):
        ExecuteUbergraph_Widget_PlayMenu_Alpha.K2Node_Event_prevMenu = prevMenu #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayMenu_Alpha(1925)
    

    def ExecuteUbergraph_Widget_PlayMenu_Alpha(self):
        goto(ComputedJump("EntryPoint"))
        self.OnEscape()
        self.mOwningMenu.OnEscape()
        goto(ExecutionFlow.Pop())
        # Label 62
        Variable: int32 = 0
        
        # Label 85
        ReturnValue: int32 = len(self.mStartingLocations)
        ReturnValue_0: bool = Variable_0 <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable = Variable_0
        ExecutionFlow.Push("L535")
        
        Item = None
        Item = self.mStartingLocations[Variable]
        ReturnValue1: bool = Default__KismetStringLibrary.NotEqual_StrStr(Item.StartLocString_11_9994B8C8428E92F9965D6BA3CB30CE96, self.mSelectedLocation.StartLocString_11_9994B8C8428E92F9965D6BA3CB30CE96)
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        ReturnValue_1: Ptr[Widget] = self.mStartingLocationsPanel.GetChildAt(Variable)
        Button: Ptr[Widget_AreaSelection_Button] = Cast[Widget_AreaSelection_Button](ReturnValue_1)
        bSuccess1: bool = Button
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Button.SetSelected(False)
        goto(ExecutionFlow.Pop())
        # Label 535
        ReturnValue_2: int32 = Variable_0 + 1
        Variable_0: int32 = ReturnValue_2
        goto('L85')
        self.Construct()
        self.mOnEnterAnimation = self.Spawn
        self.CheckSessionNameForError()
        ReturnValue_3: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ErrorPulse, 0, 0, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 699
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_UI_MainMenu_LaunchGame, ReturnValue_4, True)
        ReturnValue_6: Ptr[GameInstance] = Default__GameplayStatics.GetGameInstance(self)
        Instance: Ptr[FGGameInstance] = Cast[FGGameInstance](ReturnValue_6)
        bSuccess: bool = Instance
        Instance.SetSkipOnboarding(self.mSkipIntroCheckbox.mIsChecked)
        ReturnValue_7: bool = Default__KismetStringLibrary.NotEqual_StrStr(self.mSelectedLocation.StartLocString_11_9994B8C8428E92F9965D6BA3CB30CE96, "")
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        ReturnValue1_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_8: FText = self.mSessionNameInput.GetText()
        
        ReturnValue_9: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[ReturnValue_8])
        Default__FGBlueprintFunctionLibrary.CreateSessionAndTravelToMap(ReturnValue1_0, "Persistent_Level", self.mSelectedLocation.StartLocString_11_9994B8C8428E92F9965D6BA3CB30CE96, ReturnValue_9, self.mSelectedVisibility)
        goto(ExecutionFlow.Pop())
        ReturnValue_10: int32 = Default__KismetStringLibrary.Len(SelectedOption)
        ReturnValue_11: bool = ReturnValue_10 > 0
        if not ReturnValue_11:
           goto(ExecutionFlow.Pop())
        if not True:
            goto('L1448')
        
        enum = None
        Default__BP_OnlineHelpers.SessionVisibilityStringToEnum(SelectedOption, self, Ref[enum])
        self.mSelectedVisibility = enum
        goto(ExecutionFlow.Pop())
        # Label 1448
        ReturnValue_12: FString = Default__KismetStringLibrary.Concat_StrStr("Unknown session visibility: ", SelectedOption)
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_12, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
        # Label 1621
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_13: Ptr[FGMusicManager] = Default__FGMusicManager.Get(ReturnValue2)
        ReturnValue_13.Stop()
        goto('L699')
        self.mSelectedLocation = mStartingLocs
        Variable_0 = 0
        goto('L62')
        # Label 1792
        self.CheckSessionNameForError()
        goto(ExecutionFlow.Pop())
        # Label 1807
        self.CheckSessionNameForError()
        goto(ExecutionFlow.Pop())
        self.InitStartingLocs()
        goto(ExecutionFlow.Pop())
        self.mStartButtonHover.SetVisibility(0)
        goto(ExecutionFlow.Pop())
        self.mStartButtonHover.SetVisibility(2)
        goto(ExecutionFlow.Pop())
        goto('L1792')
        goto('L1621')
        self.OnMenuEnter(prevMenu)
        goto('L1807')
    
