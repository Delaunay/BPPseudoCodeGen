
from codegen.ue4_stub import *

from Script.FactoryGame import IsReadyToUpgrade
from Script.UMG import OverlaySlot
from Script.FactoryGame import Default__FGGamePhaseManager
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Script.Engine import FormatArgumentData
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Widget_SpaceElevatorPayOffSlot import Widget_SpaceElevatorPayOffSlot
from Script.UMG import StopAnimation
from Script.Engine import GetValidValue
from Script.FactoryGame import IsFullyUpgraded
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import Init
from Script.Engine import SetIntPropertyByName
from Script.FactoryGame import GetGamePhaseForTechTier
from Script.Engine import NotEqual_ObjectObject
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Destruct
from Script.UMG import Create
from Script.Engine import GetGameState
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Audio.Play_SpaceElevator_Compress import Play_SpaceElevator_Compress
from Script.CoreUObject import LinearColor
from Script.Engine import EqualEqual_ByteByte
from Script.FactoryGame import EGamePhase
from Script.Engine import SetObjectPropertyByName
from Script.FactoryGame import FGBuildable
from Script.UMG import GetChildrenCount
from Script.Engine import Add_ByteByte
from Script.UMG import GridSlot
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Script.FactoryGame import GetBaseCostForGamePhase
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Widget_SpaceElevator import ExecuteUbergraph_Widget_SpaceElevator.K2Node_Event_MyGeometry
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Widget_SpaceElevator import ExecuteUbergraph_Widget_SpaceElevator.K2Node_CustomEvent_NewGamePhase
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Widget_SpaceElevator import ExecuteUbergraph_Widget_SpaceElevator.K2Node_Event_InDeltaTime
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Audio.Stop_SpaceElevator_Chime import Stop_SpaceElevator_Chime
from Script.UMG import AddChildToHorizontalBox
from Script.FactoryGame import GetGamePhaseName
from Script.AkAudio import AkComponent
from Script.FactoryGame import FGBuildableSpaceElevator
from Script.Engine import PrintString
from Script.Engine import SetTextPropertyByName
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Widget_SpaceElevator import ExecuteUbergraph_Widget_SpaceElevator
from Script.FactoryGame import FGGamePhaseManager
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Audio.Play_SpaceElevator_Chime import Play_SpaceElevator_Chime
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.UMG import PlayAnimation
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Audio.Stop_SpaceElevator_Lever_Pull import Stop_SpaceElevator_Lever_Pull
from Script.Engine import Default__GameplayStatics
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Smoke import Widget_Smoke
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.Engine import RandomIntegerInRange
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Audio.Stop_SpaceElevator_Compress import Stop_SpaceElevator_Compress
from Script.UMG import BindToAnimationFinished
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Audio.Play_SpaceElevator_Lever_Clonk_02 import Play_SpaceElevator_Lever_Clonk_02
from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.UMG import AddChildToGrid
from Script.UMG import HorizontalBoxSlot
from Script.Engine import Default__KismetNodeHelperLibrary
from Script.Engine import Not_PreBool
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Widget_SpaceElevator import ExecuteUbergraph_Widget_SpaceElevator.K2Node_CustomEvent_SelectionIndex
from Script.UMG import SetColumn
from Script.UMG import GetRenderOpacity
from Script.UMG import UnbindAllFromAnimationFinished
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Audio.Play_SpaceElevator_Lever_Clonk import Play_SpaceElevator_Lever_Clonk
from Script.UMG import Widget
from Script.FactoryGame import GetGamePhase
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Widget_SpaceElevator_TierInfo import Widget_SpaceElevator_TierInfo
from Script.Engine import Conv_ByteToText
from Script.UMG import UMGSequencePlayer
from Script.UMG import IsAnimationPlaying
from Script.UMG import SetRenderOpacity
from Game.FactoryGame.Buildable.Factory.SpaceElevator.Audio.Play_SpaceElevator_Conveyor import Play_SpaceElevator_Conveyor
from Script.UMG import AddChildToOverlay

class Widget_SpaceElevator(Widget_UseableBase):
    StatusPulse: Ptr[WidgetAnimation]
    SendCrate: Ptr[WidgetAnimation]
    WindowShake: Ptr[WidgetAnimation]
    SealCrate: Ptr[WidgetAnimation]
    SendPulseAnim: Ptr[WidgetAnimation]
    SealPulseAnim: Ptr[WidgetAnimation]
    LoadPulseAnim: Ptr[WidgetAnimation]
    SendTextAnim: Ptr[WidgetAnimation]
    SealTextAnim: Ptr[WidgetAnimation]
    LoadTextAnim: Ptr[WidgetAnimation]
    mSpaceElevator: Ptr[FGBuildableSpaceElevator]
    GamePhaseManager: Ptr[FGGamePhaseManager]
    mFirstUnlockTier: int32 = -1
    mLastUnlockTier: int32 = -1
    mShouldOpenInventory = True
    mUseMouse = True
    mCaptureInput = True
    mRestoreFocusWhenLost = True
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    bHasScriptImplementedTick = True
    
    def DisplayEarlyAccessBlocker(self):
        ExecutionFlow.Push("L513")
        Variable: int32 = self.mFirstUnlockTier
        # Label 32
        ReturnValue: bool = Variable <= self.mLastUnlockTier
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L286")
        ReturnValue_0: bool = Variable <= 1
        if not ReturnValue_0:
            goto('L360')
        self.mBlocker.SetVisibility(0)
        self.mScreen.SetVisibility(1)
        self.Widget_Manufacturing_Warning.SetVisibility(0)
        self.mInteractionBlocker.SetVisibility(0)
        goto(ExecutionFlow.Pop())
        # Label 286
        ReturnValue_1: int32 = Variable + 1
        Variable = ReturnValue_1
        goto('L32')
        # Label 360
        self.mBlocker.SetVisibility(1)
        self.mScreen.SetVisibility(3)
        self.Widget_Manufacturing_Warning.SetVisibility(1)
        self.mInteractionBlocker.SetVisibility(1)
        goto(ExecutionFlow.Pop())
    

    def UpdateHeaderText(self):
        AsFGBuildable: Ptr[FGBuildable] = Cast[FGBuildable](self.mInteractObject)
        bSuccess: bool = AsFGBuildable
        if not bSuccess:
            goto('L146')
        self.Widget_Window_DarkMode.SetTitle(AsFGBuildable.mDisplayName)
    

    def SetStatusText(self, text: FText, Pulsing: bool):
        self.StatusText.SetText(text)
        if not Pulsing:
            goto('L107')
        ReturnValue: bool = self.IsAnimationPlaying(self.StatusPulse)
        if not ReturnValue:
            goto('L253')
        # End
        # Label 107
        self.StopAnimation(self.StatusPulse)
        self.StatusText.SetRenderOpacity(1)
        ReturnValue_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_SpaceElevator_Chime, ReturnValue_0, True)
        # End
        # Label 253
        ReturnValue_2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.StatusPulse, 0, 0, 0, 1)
    

    def UpdatePhaseInfo(self):
        ExecutionFlow.Push("L2304")
        self.TierInfoContainer.ClearChildren()
        Variable: int32 = self.mFirstUnlockTier
        # Label 68
        ReturnValue: bool = Variable <= self.mLastUnlockTier
        if not ReturnValue:
            goto('L954')
        ExecutionFlow.Push("L1835")
        ReturnValue_0: int32 = self.mLastUnlockTier - 1
        ReturnValue1: bool = Variable <= ReturnValue_0
        if not ReturnValue1:
            goto('L1909')
        SeperatorSymbol = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 239, 'Value': ', '}"
        # Label 243
        ReturnValue_1: Ptr[Widget_SpaceElevator_TierInfo] = Default__WidgetBlueprintLibrary.Create(self, Widget_SpaceElevator_TierInfo, None)
        FormatArgumentData.ArgumentName = "TierNum"
        FormatArgumentData.ArgumentValueType = 0
        FormatArgumentData.ArgumentValue = 
        FormatArgumentData.ArgumentValueInt = Variable
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_2: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 558, 'Value': 'Tier {TierNum}'}", Array)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_1, "mText", Ref[ReturnValue_2])
        ReturnValue_3: Ptr[HorizontalBoxSlot] = self.TierInfoContainer.AddChildToHorizontalBox(ReturnValue_1)
        ReturnValue2: bool = Variable <= self.mLastUnlockTier
        if not ReturnValue2:
            goto('L1939')
        ReturnValue2_0: Ptr[Widget_SpaceElevator_TierInfo] = Default__WidgetBlueprintLibrary.Create(self, Widget_SpaceElevator_TierInfo, None)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue2_0, "mText", Ref[SeperatorSymbol])
        ReturnValue2_1: Ptr[HorizontalBoxSlot] = self.TierInfoContainer.AddChildToHorizontalBox(ReturnValue2_0)
        goto(ExecutionFlow.Pop())
        # Label 954
        ReturnValue1_0: uint8 = self.GamePhaseManager.GetGamePhase()
        ReturnValue1_1: uint8 = Add_ByteByte(ReturnValue1_0, 1)
        ReturnValue1_2: uint8 = Default__KismetNodeHelperLibrary.GetValidValue(EGamePhase, ReturnValue1_1)
        ReturnValue_4: FText = self.GamePhaseManager.GetGamePhaseName(ReturnValue1_2)
        self.PhaseName.SetText(ReturnValue_4)
        ReturnValue_5: uint8 = self.GamePhaseManager.GetGamePhase()
        ReturnValue_6: uint8 = Add_ByteByte(ReturnValue_5, 1)
        ReturnValue_7: uint8 = Default__KismetNodeHelperLibrary.GetValidValue(EGamePhase, ReturnValue_6)
        ReturnValue_8: FText = Default__KismetTextLibrary.Conv_ByteToText(ReturnValue_7)
        # Label 1431
        FormatArgumentData1.ArgumentName = "PhaseInt"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue_8
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData1]
        ReturnValue1_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1697, 'Value': 'Space Elevator Resource Delivery  {PhaseInt}'}", Array1)
        self.SpaceElevatorTitle.SetText(ReturnValue1_3)
        goto(ExecutionFlow.Pop())
        # Label 1835
        ReturnValue_9: int32 = Variable + 1
        Variable = ReturnValue_9
        goto('L68')
        # Label 1909
        SeperatorSymbol = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1929, 'Value': ' & '}"
        goto('L243')
        # Label 1939
        ReturnValue_10: bool = Variable <= 1
        if not ReturnValue_10:
           goto(ExecutionFlow.Pop())
        self.PhaseName.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2020, 'Value': 'Content Unavailable.'}")
        self.SpaceElevatorTitle.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2116, 'Value': 'This content is unavailable in Early Access.'}")
        ReturnValue1_4: Ptr[Widget_SpaceElevator_TierInfo] = Default__WidgetBlueprintLibrary.Create(self, Widget_SpaceElevator_TierInfo, None)
        ReturnValue1_5: Ptr[HorizontalBoxSlot] = self.TierInfoContainer.AddChildToHorizontalBox(ReturnValue1_4)
        goto(ExecutionFlow.Pop())
    

    def SetUnlockTiers(self):
        ExecutionFlow.Push("L582")
        Variable: int32 = 0
        # Label 28
        ReturnValue: bool = Variable <= 10
        if not ReturnValue:
            goto('L421')
        ExecutionFlow.Push("L480")
        ReturnValue_0: uint8 = self.GamePhaseManager.GetGamePhase()
        ReturnValue_1: uint8 = self.GamePhaseManager.GetGamePhaseForTechTier(Variable)
        ReturnValue_2: uint8 = Add_ByteByte(ReturnValue_0, 1)
        ReturnValue_3: uint8 = Default__KismetNodeHelperLibrary.GetValidValue(EGamePhase, ReturnValue_2)
        ReturnValue_4: bool = EqualEqual_ByteByte(ReturnValue_3, ReturnValue_1)
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        ReturnValue_5: bool = self.mFirstUnlockTier <= 0
        if not ReturnValue_5:
            goto('L554')
        self.mFirstUnlockTier = Variable
        goto(ExecutionFlow.Pop())
        # Label 421
        FirstUnlockTier = self.mFirstUnlockTier
        LastUnlockTier = self.mLastUnlockTier
        # End
        # Label 480
        ReturnValue_6: int32 = Variable + 1
        Variable = ReturnValue_6
        goto('L28')
        # Label 554
        self.mLastUnlockTier = Variable
        goto(ExecutionFlow.Pop())
    

    def ClearInactiveLeverSelections(self, ActiveAnimation: Ptr[WidgetAnimation]):
        LocalActiveAnim = ActiveAnimation
        ReturnValue2: float = self.LoadLit.GetRenderOpacity()
        ReturnValue2_0: bool = ReturnValue2 > 0
        ReturnValue2_1: bool = NotEqual_ObjectObject(LocalActiveAnim, self.LoadTextAnim)
        ReturnValue2_2: bool = ReturnValue2_1 and ReturnValue2_0
        if not ReturnValue2_2:
            goto('L239')
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.LoadTextAnim, 0, 1, 1, 1)
        # Label 239
        ReturnValue_0: float = self.SealLit.GetRenderOpacity()
        ReturnValue_1: bool = ReturnValue_0 > 0
        ReturnValue1: bool = NotEqual_ObjectObject(LocalActiveAnim, self.SealTextAnim)
        ReturnValue_2: bool = ReturnValue1 and ReturnValue_1
        if not ReturnValue_2:
            goto('L459')
        ReturnValue2_3: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SealTextAnim, 0, 1, 1, 1)
        # Label 459
        ReturnValue_3: bool = NotEqual_ObjectObject(LocalActiveAnim, self.SendTextAnim)
        ReturnValue1_0: float = self.SendLit.GetRenderOpacity()
        ReturnValue1_1: bool = ReturnValue1_0 > 0
        ReturnValue1_2: bool = ReturnValue_3 and ReturnValue1_1
        if not ReturnValue1_2:
            goto('L679')
        ReturnValue1_3: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SendTextAnim, 0, 1, 1, 1)
    

    def DropInventorySlotStack(self):
        ExecutionFlow.Push("L809")
        Default__KismetSystemLibrary.PrintString(self, "dfasdfasdfas", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        ExecutionFlow.Push("L569")
        # Label 98
        Variable: bool = False
        Variable_0: int32 = 0
        # Label 132
        ReturnValue: bool = Not_PreBool(Variable)
        ReturnValue_0: int32 = self.PayOffContainer.GetChildrenCount()
        ReturnValue_1: int32 = ReturnValue_0 - 1
        # Label 253
        ReturnValue_2: bool = Variable_0 <= ReturnValue_1
        ReturnValue_3: bool = ReturnValue and ReturnValue_2
        if not ReturnValue_3:
            goto('L593')
        ExecutionFlow.Push("L692")
        ReturnValue_4: Ptr[Widget] = self.PayOffContainer.GetChildAt(Variable_0)
        Slot: Ptr[Widget_SpaceElevatorPayOffSlot] = Cast[Widget_SpaceElevatorPayOffSlot](ReturnValue_4)
        bSuccess: bool = Slot
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        
        Result = None
        Slot.DropOntoInventorySlot(InventorySlot, Ref[Result])
        LocalResult = Result
        if not LocalResult:
           goto(ExecutionFlow.Pop())
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 569
        WasStackMoved = LocalResult
        # End
        # Label 593
        if not LocalResult:
            goto('L631')
        WasStackMoved = LocalResult
        # End
        
        Result = None
        # Label 631
        self.DropInventoryStackOnInventoryWidget(InventorySlot, self.Widget_Inventory, Ref[Result])
        LocalResult = Result
        goto(ExecutionFlow.Pop())
        # Label 692
        ReturnValue = Not_PreBool(Variable)
        if not ReturnValue:
            goto('L593')
        ReturnValue_5: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_5
        goto('L132')
    

    def GetPayOffContainerVisibility(self):
        Variable: uint8 = 1
        Variable1: uint8 = 0
        ReturnValue: bool = self.mSpaceElevator.IsFullyUpgraded()
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_0: uint8 = switch.get(Variable_0, None)
    

    def SetupPayOffWidgets(self):
        ExecutionFlow.Push("L1270")
        self.PayOffContainer.ClearChildren()
        ReturnValue: bool = self.mSpaceElevator.IsFullyUpgraded()
        if not ReturnValue:
            goto('L98')
        goto(ExecutionFlow.Pop())
        # Label 98
        ReturnValue_0: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue_1: Ptr[FGGamePhaseManager] = Default__FGGamePhaseManager.Get(ReturnValue_0)
        ReturnValue_2: uint8 = ReturnValue_1.GetGamePhase()
        ReturnValue_3: uint8 = Add_ByteByte(ReturnValue_2, 1)
        ReturnValue_4: uint8 = Default__KismetNodeHelperLibrary.GetValidValue(EGamePhase, ReturnValue_3)
        
        ReturnValue_1.GetBaseCostForGamePhase(ReturnValue_4, Ref[PhaseCost])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 445
        ReturnValue_5: int32 = len(PhaseCost)
        ReturnValue_6: bool = Variable <= ReturnValue_5
        if not ReturnValue_6:
            goto('L1150')
        Variable_0 = Variable
        ExecutionFlow.Push("L1196")
        ReturnValue_7: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_8: Ptr[Widget_SpaceElevatorPayOffSlot] = Default__WidgetBlueprintLibrary.Create(self, Widget_SpaceElevatorPayOffSlot, ReturnValue_7)
        
        Item = None
        Item = PhaseCost[Variable_0]
        
        Item = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_8, "mItemAmount", Ref[Item])
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_8, "mItemIndex", Variable_0)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_8, "mSpaceElevator", self.mSpaceElevator)
        ReturnValue_9: Ptr[GridSlot] = self.PayOffContainer.AddChildToGrid(ReturnValue_8)
        ReturnValue_9.SetColumn(Variable_0)
        
        Item = None
        Item = PhaseCost[Variable_0]
        
        Item.ItemClass = None
        ReturnValue_10: int32 = LocalRelevantClasses.append(Item.ItemClass)
        goto(ExecutionFlow.Pop())
        
        # Label 1150
        self.Widget_Window_DarkMode.SetupRelevantInventory(Ref[LocalRelevantClasses])
        goto(ExecutionFlow.Pop())
        # Label 1196
        ReturnValue_11: int32 = Variable + 1
        Variable = ReturnValue_11
        goto('L445')
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SpaceElevator(30)
    

    def Init(self):
        self.ExecuteUbergraph_Widget_SpaceElevator(616)
    

    def PollAndSetupInventory(self):
        self.ExecuteUbergraph_Widget_SpaceElevator(822)
    

    def OnGamePhaseChanged(self, NewGamePhase: uint8):
        ExecuteUbergraph_Widget_SpaceElevator.K2Node_CustomEvent_NewGamePhase = NewGamePhase #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SpaceElevator(1190)
    

    def On Lever Select(self, SelectionIndex: int32):
        ExecuteUbergraph_Widget_SpaceElevator.K2Node_CustomEvent_SelectionIndex = SelectionIndex #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SpaceElevator(1205)
    

    def OnUpgrade(self):
        self.ExecuteUbergraph_Widget_SpaceElevator(2739)
    

    def Tick(self):
        ExecuteUbergraph_Widget_SpaceElevator.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_SpaceElevator.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SpaceElevator(3083)
    

    def ActivateSend(self):
        self.ExecuteUbergraph_Widget_SpaceElevator(3398)
    

    def SpawnSmoke(self):
        self.ExecuteUbergraph_Widget_SpaceElevator(3725)
    

    def SpawnSparksRight(self):
        self.ExecuteUbergraph_Widget_SpaceElevator(3862)
    

    def SpawnSparksLeft(self):
        self.ExecuteUbergraph_Widget_SpaceElevator(3946)
    

    def StartShake(self):
        self.ExecuteUbergraph_Widget_SpaceElevator(4030)
    

    def StopShake(self):
        self.ExecuteUbergraph_Widget_SpaceElevator(4077)
    

    def ResetLever(self):
        self.ExecuteUbergraph_Widget_SpaceElevator(4097)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_SpaceElevator(4183)
    

    def AnimNotify_Chime(self):
        self.ExecuteUbergraph_Widget_SpaceElevator(4365)
    

    def ExecuteUbergraph_Widget_SpaceElevator(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.DisplayEarlyAccessBlocker()
        goto(ExecutionFlow.Pop())
        self.Construct()
        Elevator: Ptr[FGBuildableSpaceElevator] = Cast[FGBuildableSpaceElevator](self.mInteractObject)
        bSuccess: bool = Elevator
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        self.mSpaceElevator = Elevator
        self.UpdateHeaderText()
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
        OutputDelegate3.BindUFunction(self, On Lever Select)
        self.Widget_Lever.OnNewSelection.AddUnique(OutputDelegate3)
        self.Widget_Lever.mShakeAnim = self.WindowShake
        self.Widget_Lever.mShakeAnimTarget = self
        ReturnValue1: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        ReturnValue1_0: Ptr[FGGamePhaseManager] = Default__FGGamePhaseManager.Get(ReturnValue1)
        self.GamePhaseManager = ReturnValue1_0
        
        FirstUnlockTier = None
        LastUnlockTier = None
        self.SetUnlockTiers(Ref[FirstUnlockTier], Ref[LastUnlockTier])
        self.UpdatePhaseInfo()
        self.SetStatusText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 524, 'Value': 'Load Resources'}", True)
        self.Widget_InventorySlot_DropArea.mSpaceElevator = self
        goto('L15')
        self.Init()
        self.PollAndSetupInventory()
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        OutputDelegate2.BindUFunction(self, OnGamePhaseChanged)
        ReturnValue_0: Ptr[FGGamePhaseManager] = Default__FGGamePhaseManager.Get(ReturnValue)
        ReturnValue_0.mOnGamePhaseChanged.AddUnique(OutputDelegate2)
        self.InitInventoryWidgetCallbacks(self.Widget_Inventory)
        goto(ExecutionFlow.Pop())
        self.SetupPayOffWidgets()
        goto(ExecutionFlow.Pop())
        # Label 837
        if not False:
           goto(ExecutionFlow.Pop())
        Variable: bool = True
        goto(ExecutionFlow.Pop())
        # Label 851
        Variable_0: bool = False
        self.Widget_Lever.mMaxSelectionIndex = 1
        ReturnValue5: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SealPulseAnim, 0, 0, 0, 1)
        self.Widget_Lever.SetShowButton(True)
        self.SetStatusText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1005, 'Value': 'Seal Crate'}", True)
        goto(ExecutionFlow.Pop())
        # Label 1056
        if not Variable_0:
            goto('L1071')
        goto(ExecutionFlow.Pop())
        # Label 1071
        Variable_0 = True
        ExecutionFlow.Push("L1102")
        if not Variable_1:
            goto('L1174')
        goto(ExecutionFlow.Pop())
        # Label 1102
        if not Variable:
            goto('L1117')
        goto(ExecutionFlow.Pop())
        # Label 1117
        Variable = True
        self.Widget_Lever.mMaxSelectionIndex = 0
        goto(ExecutionFlow.Pop())
        # Label 1174
        Variable_1: bool = True
        goto('L837')
        self.SetupPayOffWidgets()
        goto(ExecutionFlow.Pop())
        CmpSuccess: bool = SelectionIndex != 0
        if not CmpSuccess:
            goto('L2099')
        CmpSuccess = SelectionIndex != 1
        if not CmpSuccess:
            goto('L1431')
        CmpSuccess = SelectionIndex != 2
        if not CmpSuccess:
            goto('L2268')
        Default__KismetSystemLibrary.PrintString(self, "Errol", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
        # Label 1431
        Default__KismetSystemLibrary.PrintString(self, "Seal", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue5_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_SpaceElevator_Lever_Clonk, ReturnValue2, True)
        ReturnValue2 = self.GetOwningPlayer()
        ReturnValue4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_SpaceElevator_Compress, ReturnValue2, True)
        ReturnValue2 = self.GetOwningPlayer()
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_SpaceElevator_Lever_Pull, ReturnValue2, True)
        self.Widget_Lever.SetShowButton(False)
        self.StopAnimation(self.SealPulseAnim)
        ReturnValue1_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SealTextAnim, 0, 1, 0, 1)
        self.ClearInactiveLeverSelections(self.SealTextAnim)
        ReturnValue3: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SealCrate, 0, 1, 0, 1)
        self.Widget_Lever.mMinSelectionIndex = 1
        OutputDelegate1.BindUFunction(self, ActivateSend)
        self.BindToAnimationFinished(self.SealCrate, OutputDelegate1)
        self.SetStatusText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2048, 'Value': 'Sealing...'}", False)
        goto(ExecutionFlow.Pop())
        # Label 2099
        Default__KismetSystemLibrary.PrintString(self, "Load", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        self.StopAnimation(self.LoadPulseAnim)
        ReturnValue_2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.LoadTextAnim, 0, 1, 0, 1)
        self.ClearInactiveLeverSelections(self.LoadTextAnim)
        goto(ExecutionFlow.Pop())
        # Label 2268
        Default__KismetSystemLibrary.PrintString(self, "Send", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        self.Widget_Lever.mSliderLocked = True
        self.StopAnimation(self.SendPulseAnim)
        ReturnValue2_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SendTextAnim, 0, 1, 0, 1)
        self.ClearInactiveLeverSelections(self.SendTextAnim)
        self.OnUpgrade()
        ReturnValue3_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue3_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_SpaceElevator_Conveyor, ReturnValue3_0, True)
        ReturnValue3_0 = self.GetOwningPlayer()
        ReturnValue2_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_SpaceElevator_Lever_Clonk_02, ReturnValue3_0, True)
        ReturnValue3_0 = self.GetOwningPlayer()
        ReturnValue1_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_SpaceElevator_Lever_Pull, ReturnValue3_0, True)
        goto(ExecutionFlow.Pop())
        ReturnValue_3: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_3)
        bSuccess1: bool = Controller
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue_4: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_4.Server_SpaceElevatorUpgradePressed(self.mSpaceElevator)
        ReturnValue7: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SendCrate, 0, 1, 0, 1)
        self.Widget_Lever.SetShowButton(False)
        self.SetStatusText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 3032, 'Value': 'Sending...'}", False)
        goto(ExecutionFlow.Pop())
        ReturnValue_5: bool = self.mSpaceElevator.IsReadyToUpgrade()
        if not ReturnValue_5:
            goto('L3170')
        if not Variable1:
            goto('L3154')
        goto(ExecutionFlow.Pop())
        # Label 3154
        Variable1: bool = True
        goto('L851')
        # Label 3170
        Variable1 = False
        goto('L1056')
        # Label 3186
        self.Widget_Lever.CurrentSelectionIndex = 0
        self.Widget_Lever.mMinSelectionIndex = 0
        self.UnbindAllFromAnimationFinished(self.SendCrate)
        self.SetStatusText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 3310, 'Value': 'Load Resources'}", True)
        self.Widget_Lever.mSliderLocked = False
        goto(ExecutionFlow.Pop())
        ReturnValue_6: bool = self.mSpaceElevator.IsFullyUpgraded()
        ReturnValue_7: bool = Not_PreBool(ReturnValue_6)
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        self.Widget_Lever.mMaxSelectionIndex = 2
        ReturnValue4_0: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.SendPulseAnim, 0, 0, 0, 1)
        self.Widget_Lever.SetShowButton(True)
        self.UnbindAllFromAnimationFinished(self.SealCrate)
        self.SetStatusText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 3641, 'Value': 'Send Crate'}", True)
        self.Widget_Lever.mSliderLocked = False
        goto(ExecutionFlow.Pop())
        ReturnValue1_3: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_8: Ptr[Widget_Smoke] = Default__WidgetBlueprintLibrary.Create(self, Widget_Smoke, ReturnValue1_3)
        ReturnValue_9: Ptr[OverlaySlot] = self.CrateSmokeContainer.AddChildToOverlay(ReturnValue_8)
        goto(ExecutionFlow.Pop())
        ReturnValue_10: int32 = RandomIntegerInRange(5, 8)
        self.SparksRight.CreateSparks(ReturnValue_10)
        goto(ExecutionFlow.Pop())
        ReturnValue1_4: int32 = RandomIntegerInRange(5, 8)
        self.SparksLeft.CreateSparks(ReturnValue1_4)
        goto(ExecutionFlow.Pop())
        ReturnValue6: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.WindowShake, 0, 0, 0, 1)
        goto(ExecutionFlow.Pop())
        self.StopAnimation(self.WindowShake)
        goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.PrintString(self, "Hello", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto('L3186')
        self.Destruct()
        ReturnValue4_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue6_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_SpaceElevator_Compress, ReturnValue4_1, True)
        goto(ExecutionFlow.Pop())
        # Label 4279
        ReturnValue5_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue7_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_SpaceElevator_Chime, ReturnValue5_1, True)
        goto(ExecutionFlow.Pop())
        goto('L4279')
    
