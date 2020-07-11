
from codegen.ue4_stub import *

from Script.FactoryGame import Default__FGResearchTree
from Script.Engine import Texture
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Buildable.-Shared.WorkBench.BPW_MAM import ExecuteUbergraph_BPW_MAM.K2Node_Event_exitCode
from Script.UMG import SlotAsCanvasSlot
from Script.UMG import AddChild
from Script.CoreUObject import Timespan
from Game.FactoryGame.Buildable.Factory.TradingPost.UI.Lock_Icon import Lock_Icon
from Script.FactoryGame import GetDisplayName
from Script.FactoryGame import FGResearchMachine
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetType
from Script.Engine import Array_Find
from Script.UMG import GetChildAt
from Script.Engine import NotEqual_ClassClass
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetAllCompletedResearch
from Script.UMG import GetLocalSize
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.Engine import TimerHandle
from Script.FactoryGame import IsAnyResearchBeingConducted
from Script.Engine import Array_Append
from Script.UMG import SetPercent
from Script.Engine import IsValid
from Script.Engine import Conv_IntToText
from Script.UMG import SetColorAndOpacity
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Interface.UI.InGame.MAMTree.BPW_MAMTree_ListButtonInfo import BPW_MAMTree_ListButtonInfo
from Script.FactoryGame import GetTimeToComplete
from Script.FactoryGame import Init
from Script.SlateCore import Geometry
from Script.UMG import UserWidget
from Script.UMG import ScrollToStart
from Script.FactoryGame import Default__FGGlobalSettings
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Destruct
from Script.UMG import Create
from Script.FactoryGame import FGResearchTree
from Script.FactoryGame import AddPopupWithCloseDelegate
from Script.SlateCore import SlateBrush
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.FactoryGame import GetSchematicDisplayName
from Script.FactoryGame import GetResearchBeingConducted
from Script.CoreUObject import LinearColor
from Game.FactoryGame.Buildable.-Shared.WorkBench.BPW_MAM import ExecuteUbergraph_BPW_MAM.K2Node_Event_popupClass
from Script.Engine import EqualEqual_ClassClass
from Script.Engine import SetClassPropertyByName
from Script.FactoryGame import GetOngoingResearchTimeLeft
from Script.Engine import EqualEqual_ByteByte
from Script.Engine import FromSeconds
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Script.Engine import GetComponentByClass
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import GetInventory
from Script.FactoryGame import FGInventoryComponent
from Script.FactoryGame import GetPendingRewards
from Game.FactoryGame.Interface.UI.InGame.Widget_PopupContentImageButton import Widget_PopupContentImageButton
from Game.FactoryGame.Buildable.-Shared.WorkBench.BPW_MAM import ExecuteUbergraph_BPW_MAM.K2Node_ComponentBoundEvent_Schematic
from Game.FactoryGame.Interface.UI.InGame.Widget_PopupToggleSelect import Widget_PopupToggleSelect
from Script.Engine import NotEqual_ByteByte
from Script.UMG import Close
from Script.FactoryGame import ESchematicType
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.Engine import Subtract_Vector2DVector2D
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import ItemAmount
from Script.FactoryGame import GetHardDriveResearchSchematic
from Script.FactoryGame import FGHardDriveSettings
from Game.FactoryGame.Schematics.Research.BPD_ResearchTree_HardDrive import BPD_ResearchTree_HardDrive
from Script.Engine import MakeLiteralByte
from Script.Engine import SetTextPropertyByName
from Game.FactoryGame.Buildable.-Shared.WorkBench.BPW_MAM import ExecuteUbergraph_BPW_MAM.K2Node_CustomEvent_Index
from Game.FactoryGame.Buildable.Factory.TradingPost.UI.SchematicIcons.SchematicIcon_MAM import SchematicIcon_MAM
from Script.FactoryGame import IsResesearchTreeUnlocked
from Script.Engine import K2_SetTimerDelegate
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import PanelSlot
from Script.Engine import SetBytePropertyByName
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import ClassIsChildOf
from Script.FactoryGame import CanAffordResearch
from Script.Engine import BreakVector2D
from Script.Engine import BreakTimespan
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_ListButton import Widget_ListButton
from Script.FactoryGame import FGResearchManager
from Script.Engine import Format
from Script.Engine import EqualEqual_ObjectObject
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.Engine import AsPercent_Float
from Script.FactoryGame import FGSchematicManager
from Script.CoreUObject import Vector2D
from Script.UMG import LocalToViewport
from Script.UMG import CanvasPanelSlot
from Script.FactoryGame import GetFallbackReturnItem
from Script.FactoryGame import EResearchState
from Script.FactoryGame import GetItemIcon
from Script.FactoryGame import GetPreUnlockDisplayName
from Script.Engine import Not_PreBool
from Script.FactoryGame import Default__FGResearchManager
from Script.Engine import K2_GetPawn
from Game.FactoryGame.Buildable.-Shared.WorkBench.BPW_MAM import ExecuteUbergraph_BPW_MAM.K2Node_CustomEvent_ListButton
from Script.FactoryGame import GetHardDriveSettingsCDO
from Script.FactoryGame import GetItemName
from Script.UMG import Open
from Script.UMG import Default__SlateBlueprintLibrary
from Script.FactoryGame import GetAllResearchTrees
from Script.UMG import Widget
from Game.FactoryGame.Buildable.-Shared.WorkBench.BPW_MAM import ExecuteUbergraph_BPW_MAM
from Script.FactoryGame import FGSchematic
from Script.UMG import GetOwningPlayerPawn
from Script.Engine import Actor
from Script.FactoryGame import Default__FGSchematic
from Script.FactoryGame import Default__FGHardDriveSettings
from Script.UMG import SetPosition
from Script.Engine import IsValidClass
from Script.FactoryGame import Default__FGSchematicManager
from Script.UMG import GetCachedGeometry

class BPW_MAM(Widget_UseableBase):
    mAllResearchTrees: List[TSubclassOf[FGResearchTree]]
    ResearchMachineComponent: Ptr[FGResearchMachine]
    mCurrentHoveredButton: int32
    mResearchTimerUpdateTime: float = 0.10000000149011612
    mResearchTimerHandle: TimerHandle
    mResearchState: uint8
    mCurrentTree: TSubclassOf[FGResearchTree]
    mHasBeenResearchingSinceOpening: bool
    CurrentCompletedResearch: TSubclassOf[FGSchematic]
    selectedRewardIndex: int32 = -1
    mHardDriveListButton: Ptr[Widget_ListButton]
    mShouldOpenInventory = True
    mUseKeyboard = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mInputToPassThrough = ['Use']
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mUseGamepadCursor = True
    mCallCustomTickOnConstruct = True
    
    def WidgetFactory(self):
        ExecutionFlow.Push("L760")
        ReturnValue: bool = ClassIsChildOf(PopupClass, Widget_PopupToggleSelect)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue1)
        rewards: List[TSubclassOf[FGSchematic]] = []
        
        ReturnValue_0.GetPendingRewards(self.CurrentCompletedResearch, Ref[rewards])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 235
        ReturnValue_1: int32 = len(rewards)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        # Label 332
        if not ReturnValue_2:
            goto('L654')
        Variable_0 = Variable
        ExecutionFlow.Push("L686")
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_4: Ptr[Widget_PopupContentImageButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_PopupContentImageButton, ReturnValue_3)
        
        Item = None
        Item = rewards[Variable_0]
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_4, "mSchematic", Item)
        
        ReturnValue_5: int32 = LocalWidgets.append(ReturnValue_4)
        goto(ExecutionFlow.Pop())
        # Label 654
        widgets: List[Ptr[UserWidget]] = LocalWidgets
        # End
        # Label 686
        ReturnValue_6: int32 = Variable + 1
        Variable = ReturnValue_6
        goto('L235')
    

    def SchematicsPurchased(self, schematic: TSubclassOf[FGSchematic]):
        ReturnValue: uint8 = Default__FGSchematic.GetType(schematic)
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValidClass(self.mCurrentTree)
        ReturnValue_1: bool = EqualEqual_ByteByte(ReturnValue, 6)
        ReturnValue_2: bool = ReturnValue_1 and ReturnValue_0
        if not ReturnValue_2:
            goto('L238')
        self.BPW_MAMTree_Ingame.SelectResearchTree(self.mCurrentTree)
    

    def OnHarddriveButtonClicked(self, index: int32, ListButton: Ptr[Widget_ListButton]):
        
        ReturnValue: int32 = Default__KismetArrayLibrary.Array_Find(Ref[self.mAllResearchTrees], Ref[self.mCurrentTree])
        ReturnValue_0: Ptr[Widget] = self.mResearchListContainer.GetChildAt(ReturnValue)
        Button: Ptr[Widget_ListButton] = Cast[Widget_ListButton](ReturnValue_0)
        bSuccess: bool = Button
        if not bSuccess:
            goto('L231')
        Button.mIsSelected = False
        # Label 231
        self.mCurrentTree = None
        self.mTreeScrollBox.SetVisibility(1)
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue_1)
        ReturnValue_3: bool = ReturnValue_2.IsResesearchTreeUnlocked(BPD_ResearchTree_HardDrive)
        if not ReturnValue_3:
            goto('L458')
        self.BPW_MAM_HardDriveScanner.SetVisibility(0)
    

    def OnPopupClosed(self, confirm: bool):
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        RCO = None
        Default__BPHUDHelpers.GetDefaultRCO(ReturnValue, self, Ref[RCO])
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0: Ptr[Pawn] = ReturnValue.K2_GetPawn()
        ReturnValue_1: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue)
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_0)
        bSuccess: bool = Player
        RCO.ServerClaimResearchResults(ReturnValue_1, Player, self.CurrentCompletedResearch, self.selectedRewardIndex)
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValidClass(self.mCurrentTree)
        ReturnValue_3: bool = self.mHasBeenResearchingSinceOpening and ReturnValue_2
        if not ReturnValue_3:
            goto('L481')
        self.BPW_MAMTree_Ingame.SelectResearchTree(self.mCurrentTree)
    

    def HandleCompletedResearch(self, schematic: TSubclassOf[FGSchematic]):
        self.CurrentCompletedResearch = schematic
        ReturnValue: uint8 = Default__FGSchematic.GetType(self.CurrentCompletedResearch)
        CmpSuccess: bool = NotEqual_ByteByte(ReturnValue, 6)
        if not CmpSuccess:
            goto('L173')
        # Label 123
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 8)
        if not CmpSuccess:
            goto('L867')
        # End
        # Label 173
        LocalWidgetType = None
        ReturnValue_0: FText = Default__FGSchematic.GetSchematicDisplayName(schematic)
        FormatArgumentData1.ArgumentName = "Schematic"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue_0
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1]
        ReturnValue_1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 510, 'Value': 'The analysis of {Schematic} is completed! Please choose a new node in a tree to begin a new analysis.'}", Array)
        LocalTitleText = ReturnValue_1
        # Label 686
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        OutputDelegate1.BindUFunction(self, OnPopupClosed)
        
        OutputDelegate1 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue1, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 775, 'Value': 'Analysis Complete!'}", LocalTitleText, 0, LocalWidgetType, self, Ref[OutputDelegate1])
        # End
        # Label 867
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue3)
        rewards: List[TSubclassOf[FGSchematic]] = []
        
        ReturnValue_2.GetPendingRewards(schematic, Ref[rewards])
        LocalPendingRewards = rewards
        
        ReturnValue_3: int32 = len(LocalPendingRewards)
        ReturnValue_4: bool = ReturnValue_3 > 0
        if not ReturnValue_4:
            goto('L1807')
        LocalWidgetType = Widget_PopupToggleSelect
        ReturnValue2: FText = Default__FGSchematic.GetSchematicDisplayName(schematic)
        FormatArgumentData3.ArgumentName = "Schematic"
        FormatArgumentData3.ArgumentValueType = 4
        FormatArgumentData3.ArgumentValue = ReturnValue2
        FormatArgumentData3.ArgumentValueInt = 0
        FormatArgumentData3.ArgumentValueFloat = 0
        FormatArgumentData3.ArgumentValueGender = 0
        Array2: List[FormatArgumentData] = [FormatArgumentData3]
        ReturnValue2_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1482, 'Value': 'The analysis of {Schematic} is completed! Select your desired reward.'}", Array2)
        LocalTitleText = ReturnValue2_0
        OutputDelegate.BindUFunction(self, OnPopupClosed)
        ReturnValue_5: Ptr[PlayerController] = self.GetOwningPlayer()
        
        OutputDelegate = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue_5, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1715, 'Value': 'Analysis Complete!'}", LocalTitleText, 0, LocalWidgetType, self, Ref[OutputDelegate])
        # End
        # Label 1807
        LocalWidgetType = Widget_PopupToggleSelect
        ReturnValue_6: Ptr[FGHardDriveSettings] = Default__FGGlobalSettings.GetHardDriveSettingsCDO()
        ReturnValue_7: ItemAmount = ReturnValue_6.GetFallbackReturnItem()
        ReturnValue_8: FText = Default__FGItemDescriptor.GetItemName(ReturnValue_7.ItemClass)
        FormatArgumentData.ArgumentName = "Item"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_8
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue1_0: FText = Default__FGSchematic.GetSchematicDisplayName(schematic)
        FormatArgumentData2.ArgumentName = "Schematic"
        FormatArgumentData2.ArgumentValueType = 4
        FormatArgumentData2.ArgumentValue = ReturnValue1_0
        FormatArgumentData2.ArgumentValueInt = 0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData2, FormatArgumentData]
        ReturnValue1_1: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2512, 'Value': 'The analysis of {Schematic} is completed! No new research is available. Try again later after further progress. Your {Item} has been returned to you.'}", Array1)
        LocalTitleText = ReturnValue1_1
        ReturnValue2_1: Ptr[PlayerController] = self.GetOwningPlayer()
        OutputDelegate2.BindUFunction(self, OnPopupClosed)
        
        OutputDelegate2 = None
        Default__FGBlueprintFunctionLibrary.AddPopupWithCloseDelegate(ReturnValue2_1, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2825, 'Value': 'Analysis Complete!'}", LocalTitleText, 0, LocalWidgetType, self, Ref[OutputDelegate2])
    

    def OnResearchStateChanged(self, researchState: uint8):
        ExecutionFlow.Push("L888")
        self.mResearchState = researchState
        CmpSuccess: bool = NotEqual_ByteByte(self.mResearchState, 0)
        if not CmpSuccess:
            goto('L123')
        CmpSuccess = NotEqual_ByteByte(self.mResearchState, 1)
        if not CmpSuccess:
            goto('L673')
        goto(ExecutionFlow.Pop())
        # Label 123
        self.BPW_MAM_HardDriveScanner.ResetText()
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue)
        schematics: List[TSubclassOf[FGSchematic]] = []
        
        ReturnValue_0.GetAllCompletedResearch(Ref[schematics])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 332
        ReturnValue_1: int32 = len(schematics)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
            goto('L558')
        Variable_0 = Variable
        ExecutionFlow.Push("L814")
        
        Item = None
        Item = schematics[Variable_0]
        self.HandleCompletedResearch(Item)
        goto(ExecutionFlow.Pop())
        # Label 558
        self.mCurrentResearchInfo.SetVisibility(1)
        self.mInProgressBackground.SetVisibility(1)
        self.mBlueprintGrid.SetVisibility(0)
        goto(ExecutionFlow.Pop())
        # Label 673
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue1)
        ReturnValue_3: TSubclassOf[FGSchematic] = ReturnValue1_0.GetResearchBeingConducted()
        self.OnResearchStarted(ReturnValue_3)
        goto(ExecutionFlow.Pop())
        # Label 814
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L332')
    

    def ConvertFloatTimeToText(self, Seconds: float):
        ReturnValue: Timespan = FromSeconds(Seconds)
        
        Days = None
        Hours = None
        Minutes = None
        Seconds_0 = None
        Milliseconds = None
        BreakTimespan(ReturnValue, Ref[Days], Ref[Hours], Ref[Minutes], Ref[Seconds_0], Ref[Milliseconds])
        ReturnValue_0: int32 = Days * 24
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_IntToText(Seconds_0, False, True, 2, 324)
        ReturnValue_2: int32 = ReturnValue_0 + Hours
        FormatArgumentData.ArgumentName = "s"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_1
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        FormatArgumentData1.ArgumentName = "h"
        FormatArgumentData1.ArgumentValueType = 0
        FormatArgumentData1.ArgumentValue = 
        FormatArgumentData1.ArgumentValueInt = ReturnValue_2
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_IntToText(Minutes, False, True, 2, 324)
        FormatArgumentData2.ArgumentName = "m"
        FormatArgumentData2.ArgumentValueType = 4
        FormatArgumentData2.ArgumentValue = ReturnValue1
        FormatArgumentData2.ArgumentValueInt = 0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData2, FormatArgumentData]
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 981, 'Value': '{h}:{m}:{s}'}", Array)
        Result = ReturnValue_3
    

    def UpdateResearchTimer(self):
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue1)
        ReturnValue: bool = ReturnValue1_0.IsAnyResearchBeingConducted()
        if not ReturnValue:
            goto('L2199')
        ReturnValue1 = self.GetOwningPlayer()
        ReturnValue1_0 = Default__FGResearchManager.Get(ReturnValue1)
        ReturnValue1_1: TSubclassOf[FGSchematic] = ReturnValue1_0.GetResearchBeingConducted()
        ReturnValue_0: float = Default__FGSchematic.GetTimeToComplete(ReturnValue1_1)
        ReturnValue_1: float = ReturnValue1_0.GetOngoingResearchTimeLeft(ReturnValue1_1)
        ReturnValue_2: float = ReturnValue_1 / ReturnValue_0
        ReturnValue_3: float = 1 - ReturnValue_2
        self.mResearchProgressBar.mProgressBar.SetPercent(ReturnValue_3)
        ReturnValue1 = self.GetOwningPlayer()
        ReturnValue1_0 = Default__FGResearchManager.Get(ReturnValue1)
        ReturnValue1_1 = ReturnValue1_0.GetResearchBeingConducted()
        ReturnValue_1 = ReturnValue1_0.GetOngoingResearchTimeLeft(ReturnValue1_1)
        
        Result = None
        self.ConvertFloatTimeToText(ReturnValue_1, Ref[Result])
        self.mResearchTimeCurrent.SetText(Result)
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 790, 'Value': 'Scanning Hard Drive...'}"
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 870, 'Value': 'Other research is being conducted, please standby...'}"
        ReturnValue_4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_5: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue_4)
        ReturnValue_6: TSubclassOf[FGSchematic] = ReturnValue_5.GetResearchBeingConducted()
        ReturnValue1 = self.GetOwningPlayer()
        ReturnValue_7: uint8 = Default__FGSchematic.GetType(ReturnValue_6)
        ReturnValue1_0 = Default__FGResearchManager.Get(ReturnValue1)
        ReturnValue_8: bool = EqualEqual_ByteByte(ReturnValue_7, 8)
        Variable_0: bool = ReturnValue_8
        ReturnValue1_1 = ReturnValue1_0.GetResearchBeingConducted()
        FormatArgumentData.ArgumentName = "text"
        FormatArgumentData.ArgumentValueType = 4
        
        switch = {
            False: Variable1,
            True: Variable
        }
        FormatArgumentData.ArgumentValue = switch.get(Variable_0, None)
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue_0 = Default__FGSchematic.GetTimeToComplete(ReturnValue1_1)
        ReturnValue_1 = ReturnValue1_0.GetOngoingResearchTimeLeft(ReturnValue1_1)
        ReturnValue_2 = ReturnValue_1 / ReturnValue_0
        ReturnValue_3 = 1 - ReturnValue_2
        ReturnValue_9: FText = Default__KismetTextLibrary.AsPercent_Float(ReturnValue_3, 0, False, True, 1, 324, 0, 0)
        FormatArgumentData1.ArgumentName = "%"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue_9
        FormatArgumentData1.ArgumentValueInt = 0
        # Label 1954
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData, FormatArgumentData1]
        ReturnValue_10: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2095, 'Value': '{text}\r\n{%}'}", Array)
        self.BPW_MAM_HardDriveScanner.SetText(ReturnValue_10)
    

    def OnGetTreeInfoWidget(self):
        ReturnValue: bool = self.mCurrentHoveredButton != -1
        if not ReturnValue:
            goto('L312')
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[BPW_MAMTree_ListButtonInfo] = Default__WidgetBlueprintLibrary.Create(self, BPW_MAMTree_ListButtonInfo, ReturnValue_0)
        
        Item = None
        Item = self.mAllResearchTrees[self.mCurrentHoveredButton]
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_1, "mResearchTree", Item)
        ReturnValue_1.SetVisibility(0)
        ReturnValue_2: Ptr[Widget] = ReturnValue_1
    

    def OnListButtonUnhovered(self, index: int32, ListButton: Ptr[Widget_ListButton]):
        self.mListButtonInfoAnchor.Close()
        self.mCurrentHoveredButton = -1
    

    def OnListButtonHovered(self, index: int32, ListButton: Ptr[Widget_ListButton]):
        ReturnValue: Const[Geometry] = ListButton.GetCachedGeometry()
        
        ReturnValue_0: Vector2D = Default__SlateBlueprintLibrary.GetLocalSize(Ref[ReturnValue])
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_0, Ref[X], Ref[Y])
        ReturnValue_1: float = Y / 2
        
        PixelPosition = None
        ViewportPosition = None
        Default__SlateBlueprintLibrary.LocalToViewport(self, Vector2D(X = 0, Y = 0), Ref[ReturnValue], Ref[PixelPosition], Ref[ViewportPosition])
        ReturnValue_2: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self.mListButtonInfoMover)
        ReturnValue1: Const[Geometry] = self.mResearchListContainer.GetCachedGeometry()
        
        PixelPosition1 = None
        ViewportPosition1 = None
        Default__SlateBlueprintLibrary.LocalToViewport(self, Vector2D(X = 0, Y = 0), Ref[ReturnValue1], Ref[PixelPosition1], Ref[ViewportPosition1])
        ReturnValue_3: Vector2D = Subtract_Vector2DVector2D(ViewportPosition, ViewportPosition1)
        
        X1 = None
        Y1 = None
        BreakVector2D(ReturnValue_3, Ref[X1], Ref[Y1])
        ReturnValue_4: float = Y1 + ReturnValue_1
        ReturnValue_5: Vector2D = Vector2D(15, ReturnValue_4)
        ReturnValue_2.SetPosition(ReturnValue_5)
        
        ReturnValue_6: int32 = len(self.mAllResearchTrees)
        ReturnValue_7: int32 = ReturnValue_6 - 1
        ReturnValue_8: bool = EqualEqual_ObjectObject(ListButton, self.mHardDriveListButton)
        Variable: bool = ReturnValue_8
        
        switch = {
            False: index,
            True: ReturnValue_7
        }
        self.mCurrentHoveredButton = switch.get(Variable, None)
        self.mListButtonInfoAnchor.Open(False)
    

    def OnResearchStarted(self, schematic: TSubclassOf[FGSchematic]):
        self.mCurrentResearchInfo.SetVisibility(0)
        self.mInProgressBackground.SetVisibility(0)
        ReturnValue: SlateBrush = Default__FGSchematic.GetItemIcon(schematic)
        SlateBrush.ImageSize = self.mCurrentResearchIcon.Brush.ImageSize
        SlateBrush.Margin = self.mCurrentResearchIcon.Brush.Margin
        SlateBrush.TintColor = self.mCurrentResearchIcon.Brush.TintColor
        SlateBrush.ResourceObject = ReturnValue.ResourceObject
        SlateBrush.DrawAs = self.mCurrentResearchIcon.Brush.DrawAs
        SlateBrush.Tiling = self.mCurrentResearchIcon.Brush.Tiling
        SlateBrush.Mirroring = self.mCurrentResearchIcon.Brush.Mirroring
        
        SlateBrush = None
        self.mCurrentResearchIcon.SetBrush(Ref[SlateBrush])
        self.mCurrentResearchTreeText.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 656, 'Value': 'CurrentTree'}")
        ReturnValue_0: FText = Default__FGSchematic.GetSchematicDisplayName(schematic)
        # Label 765
        self.mCurrentReseeaarchNodeText.SetText(ReturnValue_0)
        self.mBlueprintGrid.SetVisibility(2)
        self.BPW_MAMTree_Ingame.ResetSelectedNode()
        self.UpdateResearchTimer()
        OutputDelegate.BindUFunction(self, UpdateResearchTimer)
        ReturnValue_1: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mResearchTimerUpdateTime, True)
        self.mResearchTimerHandle = ReturnValue_1
        ReturnValue_2: float = Default__FGSchematic.GetTimeToComplete(schematic)
        
        Result = None
        self.ConvertFloatTimeToText(ReturnValue_2, Ref[Result])
        FormatArgumentData.ArgumentName = "time"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = Result
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1370, 'Value': ' / {time}'}", Array)
        self.mResearchTimeTotal.SetText(ReturnValue_3)
        self.mHasBeenResearchingSinceOpening = True
    

    def InitResearchListButtons(self):
        ExecutionFlow.Push("L3880")
        Variable: int32 = 0
        Variable1: int32 = 0
        # Label 51
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue3_0: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue3)
        ResearchTrees: List[TSubclassOf[FGResearchTree]] = []
        
        ReturnValue3_0.GetAllResearchTrees(Ref[ResearchTrees])
        
        ReturnValue1: int32 = len(ResearchTrees)
        ReturnValue1_0: bool = Variable <= ReturnValue1
        if not ReturnValue1_0:
            goto('L765')
        Variable1 = Variable
        ExecutionFlow.Push("L2946")
        ReturnValue3 = self.GetOwningPlayer()
        ReturnValue3_0 = Default__FGResearchManager.Get(ReturnValue3)
        ResearchTrees = []
        
        ReturnValue3_0.GetAllResearchTrees(Ref[ResearchTrees])
        
        Item1 = None
        Item1 = ResearchTrees[Variable1]
        ReturnValue: bool = EqualEqual_ClassClass(Item1, BPD_ResearchTree_HardDrive)
        if not ReturnValue:
            goto('L3020')
        ReturnValue3 = self.GetOwningPlayer()
        ReturnValue3_0 = Default__FGResearchManager.Get(ReturnValue3)
        ResearchTrees = []
        
        ReturnValue3_0.GetAllResearchTrees(Ref[ResearchTrees])
        
        Item1 = None
        # Label 686
        Item1 = ResearchTrees[Variable1]
        LocalHardDriveClass = Item1
        goto(ExecutionFlow.Pop())
        
        # Label 765
        Default__KismetArrayLibrary.Array_Append(Ref[LocalAvailableTrees], Ref[LocalLockedTrees])
        self.mAllResearchTrees = LocalAvailableTrees
        
        ReturnValue_0: int32 = self.mAllResearchTrees.append(LocalHardDriveClass)
        Variable1_0: int32 = 0
        Variable_0: int32 = 0
        
        # Label 956
        ReturnValue_1: int32 = len(self.mAllResearchTrees)
        ReturnValue_2: bool = Variable1_0 <= ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable1_0
        ExecutionFlow.Push("L2872")
        
        Item = None
        Item = self.mAllResearchTrees[Variable_0]
        LocalTree = Item
        ReturnValue4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_3: Ptr[Widget_ListButton] = Default__WidgetBlueprintLibrary.Create(self, Widget_ListButton, ReturnValue4)
        Variable_1: Ptr[Texture] = SchematicIcon_MAM
        Variable1_1: Ptr[Texture] = Lock_Icon
        ReturnValue1_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_2: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue1_1)
        ReturnValue1_3: bool = ReturnValue1_2.IsResesearchTreeUnlocked(LocalTree)
        Variable_2: bool = ReturnValue1_3
        
        switch = {
            False: Variable1_1,
            True: Variable_1
        }
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_3, "mIcon", switch.get(Variable_2, None))
        ReturnValue1_1 = self.GetOwningPlayer()
        ReturnValue1_2 = Default__FGResearchManager.Get(ReturnValue1_1)
        ReturnValue1_3 = ReturnValue1_2.IsResesearchTreeUnlocked(LocalTree)
        Variable1_2: bool = ReturnValue1_3
        ReturnValue_4: FText = Default__FGResearchTree.GetDisplayName(LocalTree)
        ReturnValue_5: FText = Default__FGResearchTree.GetPreUnlockDisplayName(LocalTree)
        
        switch_0 = {
            False: ReturnValue_5,
            True: ReturnValue_4
        }
        
        switch_0.get(Variable1_2, None) = None
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_3, "mTitle", Ref[switch_0.get(Variable1_2, None)])
        ReturnValue_6: uint8 = Default__KismetSystemLibrary.MakeLiteralByte(1)
        Default__KismetSystemLibrary.SetBytePropertyByName(ReturnValue_3, "iconVisibility", ReturnValue_6)
        ReturnValue_7: bool = NotEqual_ClassClass(LocalTree, LocalHardDriveClass)
        if not ReturnValue_7:
            goto('L3856')
        # Label 2085
        ReturnValue1_4: bool = NotEqual_ClassClass(LocalTree, LocalHardDriveClass)
        Variable3: bool = ReturnValue1_4
        
        switch_1 = {
            False: self.mHardDriveSlot,
            True: self.mResearchListContainer
        }
        ReturnValue_8: Ptr[PanelSlot] = switch_1.get(Variable3, None).AddChild(ReturnValue_3)
        OutputDelegate.BindUFunction(self, OnHarddriveButtonClicked)
        OutputDelegate1.BindUFunction(self, OnResearchListButtonClicked)
        ReturnValue2: bool = NotEqual_ClassClass(LocalTree, LocalHardDriveClass)
        Variable2: bool = ReturnValue2
        
        switch_2 = {
            False: OutputDelegate,
            True: OutputDelegate1
        }
        ReturnValue_3.OnClicked.AddUnique(switch_2.get(Variable2, None))
        OutputDelegate3.BindUFunction(self, OnListButtonHovered)
        ReturnValue_3.OnHovered.AddUnique(OutputDelegate3)
        OutputDelegate2.BindUFunction(self, OnListButtonUnhovered)
        ReturnValue_3.OnUnhovered.AddUnique(OutputDelegate2)
        ReturnValue_9: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_10: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue_9)
        ReturnValue_11: bool = ReturnValue_10.IsResesearchTreeUnlocked(LocalTree)
        ReturnValue_12: bool = Not_PreBool(ReturnValue_11)
        if not ReturnValue_12:
           goto(ExecutionFlow.Pop())
        SlateColor.SpecifiedColor = LinearColor(R = 0.06770800054073334, G = 0.0669649988412857, B = 0.0669649988412857, A = 1)
        SlateColor.ColorUseRule = 0
        ReturnValue_3.mButtonText.SetColorAndOpacity(SlateColor)
        goto(ExecutionFlow.Pop())
        # Label 2872
        ReturnValue1_5: int32 = Variable1_0 + 1
        Variable1_0 = ReturnValue1_5
        goto('L956')
        # Label 2946
        ReturnValue_13: int32 = Variable + 1
        Variable = ReturnValue_13
        goto('L51')
        # Label 3020
        ReturnValue2_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue3 = self.GetOwningPlayer()
        ReturnValue2_1: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue2_0)
        ReturnValue3_0 = Default__FGResearchManager.Get(ReturnValue3)
        ResearchTrees = []
        
        ReturnValue3_0.GetAllResearchTrees(Ref[ResearchTrees])
        
        Item1 = None
        Item1 = ResearchTrees[Variable1]
        ReturnValue2_2: bool = ReturnValue2_1.IsResesearchTreeUnlocked(Item1)
        if not ReturnValue2_2:
            goto('L3601')
        ReturnValue3 = self.GetOwningPlayer()
        ReturnValue3_0 = Default__FGResearchManager.Get(ReturnValue3)
        ResearchTrees = []
        
        ReturnValue3_0.GetAllResearchTrees(Ref[ResearchTrees])
        
        Item1 = None
        Item1 = ResearchTrees[Variable1]
        
        Item1 = None
        ReturnValue2_3: int32 = LocalAvailableTrees.append(Item1)
        goto(ExecutionFlow.Pop())
        # Label 3601
        ReturnValue3 = self.GetOwningPlayer()
        ReturnValue3_0 = Default__FGResearchManager.Get(ReturnValue3)
        ResearchTrees = []
        
        ReturnValue3_0.GetAllResearchTrees(Ref[ResearchTrees])
        
        Item1 = None
        Item1 = ResearchTrees[Variable1]
        
        Item1 = None
        ReturnValue1_6: int32 = LocalLockedTrees.append(Item1)
        goto(ExecutionFlow.Pop())
        # Label 3856
        self.mHardDriveListButton = ReturnValue_3
        goto('L2085')
    

    def DropInventorySlotStack(self):
        WasStackMoved = False
    

    def Cleanup(self):
        self.Widget_Window_DarkMode.OnClose.Clear()
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mResearchTimerHandle])
        OutputDelegate.BindUFunction(self, OnResearchStateChanged)
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue1)
        ReturnValue1_0.ResearchStateChangedDelegate.Remove(OutputDelegate)
        OutputDelegate1.BindUFunction(self, SchematicsPurchased)
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue)
        ReturnValue_0.PurchasedSchematicDelegate.Remove(OutputDelegate1)
    

    def Destruct(self):
        self.ExecuteUbergraph_BPW_MAM(447)
    

    def Init(self):
        self.ExecuteUbergraph_BPW_MAM(476)
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_MAM(670)
    

    def OnResearchListButtonClicked(self, index: int32, ListButton: Ptr[Widget_ListButton]):
        ExecuteUbergraph_BPW_MAM.K2Node_CustomEvent_Index = index #  PERSISTENT_FRAME(
        ExecuteUbergraph_BPW_MAM.K2Node_CustomEvent_ListButton = ListButton #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_MAM(1190)
    

    def BndEvt__BPW_MAMTree_Ingame_K2Node_ComponentBoundEvent_1_OnResearchSelectedSchematic__DelegateSignature(self, schematic: TSubclassOf[FGSchematic]):
        ExecuteUbergraph_BPW_MAM.K2Node_ComponentBoundEvent_Schematic = schematic #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_MAM(1949)
    

    def NotifyPopupClosed(self):
        ExecuteUbergraph_BPW_MAM.K2Node_Event_popupClass = PopupClass #  PERSISTENT_FRAME(
        ExecuteUbergraph_BPW_MAM.K2Node_Event_exitCode = exitCode #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_MAM(2253)
    

    def BndEvt__BPW_MAM_HardDriveScanner_K2Node_ComponentBoundEvent_2_OnScanStarted__DelegateSignature(self):
        self.ExecuteUbergraph_BPW_MAM(2285)
    

    def ExecuteUbergraph_BPW_MAM(self):
        # Label 10
        self.selectedRewardIndex = -1
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        
        RCO = None
        Default__BPHUDHelpers.GetDefaultRCO(ReturnValue, self, Ref[RCO])
        ReturnValue = self.GetOwningPlayer()
        ReturnValue_0: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue)
        ReturnValue_1: Ptr[Pawn] = ReturnValue.K2_GetPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_1)
        bSuccess: bool = Player
        ReturnValue_2: Ptr[FGInventoryComponent] = Player.GetInventory()
        ReturnValue_3: TSubclassOf[FGSchematic] = Default__FGHardDriveSettings.GetHardDriveResearchSchematic()
        RCO.ServerInitiateResearch(ReturnValue_0, ReturnValue_2, ReturnValue_3, None)
        # End
        self.Destruct()
        self.Cleanup()
        # End
        self.Init()
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue1)
        ReturnValue_4: bool = ReturnValue1_0.IsAnyResearchBeingConducted()
        if not ReturnValue_4:
            goto('L649')
        self.OnResearchStateChanged(1)
        self.mHasBeenResearchingSinceOpening = True
        # End
        # Label 649
        self.OnResearchStateChanged(0)
        # End
        self.Construct()
        self.InitResearchListButtons()
        OutputDelegate1.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate1)
        AsActor: Ptr[Actor] = Cast[Actor](self.mInteractObject)
        bSuccess1: bool = AsActor
        if not bSuccess1:
            goto('L2290')
        ReturnValue_5: Ptr[FGResearchMachine] = AsActor.GetComponentByClass(FGResearchMachine)
        # Label 888
        self.ResearchMachineComponent = ReturnValue_5
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue2_0: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue2)
        OutputDelegate2.BindUFunction(self, OnResearchStateChanged)
        ReturnValue2_0.ResearchStateChangedDelegate.AddUnique(OutputDelegate2)
        OutputDelegate.BindUFunction(self, SchematicsPurchased)
        ReturnValue4: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue5: Ptr[FGSchematicManager] = Default__FGSchematicManager.Get(ReturnValue4)
        ReturnValue5.PurchasedSchematicDelegate.AddUnique(OutputDelegate)
        # End
        
        Item = None
        Item = self.mAllResearchTrees[Index]
        self.mCurrentTree = Item
        self.BPW_MAMTree_Ingame.SelectResearchTree(self.mCurrentTree)
        self.mTreeScrollBox.mScrollBox.ScrollToStart()
        self.mTreeScrollBox.SetVisibility(4)
        ReturnValue_6: bool = Default__KismetSystemLibrary.IsValid(self.mHardDriveListButton)
        if not ReturnValue_6:
            goto('L2290')
        self.mHardDriveListButton.mIsSelected = False
        self.BPW_MAM_HardDriveScanner.SetVisibility(1)
        # End
        # Label 1546
        self.selectedRewardIndex = -1
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        
        RCO1 = None
        Default__BPHUDHelpers.GetDefaultRCO(ReturnValue3, self, Ref[RCO1])
        ReturnValue3 = self.GetOwningPlayer()
        ReturnValue3_0: Ptr[FGResearchManager] = Default__FGResearchManager.Get(ReturnValue3)
        ReturnValue1_1: Ptr[Pawn] = ReturnValue3.K2_GetPawn()
        Player1: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue1_1)
        bSuccess2: bool = Player1
        ReturnValue1_2: Ptr[FGInventoryComponent] = Player1.GetInventory()
        RCO1.ServerInitiateResearch(ReturnValue3_0, ReturnValue1_2, Schematic, self.mCurrentTree)
        # End
        goto('L1546')
        # Label 1954
        ReturnValue_3 = Default__FGHardDriveSettings.GetHardDriveResearchSchematic()
        ReturnValue_7: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player2: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_7)
        bSuccess3: bool = Player2
        ReturnValue4_0: Ptr[FGResearchManager] = Default__FGResearchManager.Get(Player2)
        ReturnValue2_1: Ptr[FGInventoryComponent] = Player2.GetInventory()
        ReturnValue_8: bool = ReturnValue4_0.CanAffordResearch(ReturnValue2_1, ReturnValue_3)
        if not ReturnValue_8:
            goto('L2290')
        goto('L10')
        self.selectedRewardIndex = exitCode
        # End
        goto('L1954')
    
