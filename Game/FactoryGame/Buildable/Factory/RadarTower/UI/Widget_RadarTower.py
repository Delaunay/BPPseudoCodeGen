
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.Engine import SetScalarParameterValue
from Script.Engine import FClamp
from Script.FactoryGame import FGPlayerController
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import FromSeconds
from Script.FactoryGame import FGBuildableRadarTower
from Script.UMG import OverlaySlot
from Script.UMG import GetChildrenCount
from Script.Engine import MaterialInstanceDynamic
from Script.CoreUObject import Timespan
from Script.Engine import Not_PreBool
from Script.FactoryGame import FGActorRepresentationInterface
from Script.Engine import Ease
from Script.FactoryGame import GetNumRadarExpansionSteps
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Game.FactoryGame.Buildable.Factory.RadarTower.UI.Widget_RadarTower import ExecuteUbergraph_Widget_RadarTower.K2Node_ComponentBoundEvent_CommitMethod
from Script.UMG import GetChildAt
from Script.UMG import SetHorizontalAlignment
from Script.Engine import FormatArgumentData
from Script.UMG import PlayAnimation
from Script.UMG import SetText
from Game.FactoryGame.Buildable.Factory.RadarTower.UI.Widget_RadarTower import ExecuteUbergraph_Widget_RadarTower.K2Node_ComponentBoundEvent_Text
from Script.FactoryGame import GetCurrentExpansionStep
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Construct
from Script.Engine import TimerHandle
from Script.Engine import GreaterEqual_FloatFloat
from Script.Engine import NotEqual_TextText
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import SetColorAndOpacity
from Script.Engine import Conv_IntToText
from Script.UMG import GetDynamicMaterial
from Script.FactoryGame import IsProductionPaused
from Script.Engine import SetFloatPropertyByName
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.Engine import BreakVector2D
from Script.Engine import BooleanOR
from Script.UMG import Widget
from Script.Engine import BreakTimespan
from Game.FactoryGame.Buildable.Factory.RadarTower.UI.Widget_RadarTower import ExecuteUbergraph_Widget_RadarTower
from Script.Engine import Format
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Widget_UseableBase
from Script.Engine import LinearColorLerp
from Script.UMG import WidgetAnimation
from Script.Engine import MakeLiteralText
from Script.Engine import NotEqual_ByteByte
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.Engine import EqualEqual_TextText
from Script.Engine import AsPercent_Float
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Buildable.Factory.RadarTower.UI.Widget_RadarTower_ScanLine import Widget_RadarTower_ScanLine
from Script.UMG import Create
from Game.FactoryGame.Buildable.Factory.RadarTower.UI.Widget_RadarTower import ExecuteUbergraph_Widget_RadarTower.K2Node_ComponentBoundEvent_state
from Game.FactoryGame.Interface.UI.InGame.Widget_UseableBase import Destruct
from Game.FactoryGame.Buildable.Factory.RadarTower.UI.Widget_RadarTower import ExecuteUbergraph_Widget_RadarTower.K2Node_CustomEvent_HasChanged
from Script.FactoryGame import GetTimeToNextExpansion
from Script.UMG import SetVerticalAlignment
from Script.FactoryGame import GetNormalizedProgressValueForStep
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.UMG import AddChildToOverlay
from Script.CoreUObject import LinearColor

class Widget_RadarTower(Widget_UseableBase):
    ScanCircle: Ptr[WidgetAnimation]
    mRadarTower: Ptr[FGBuildableRadarTower]
    mScannedAreaMaterial: Ptr[MaterialInstanceDynamic]
    mScanTimer: TimerHandle
    mScannedAreaLerpT: float
    mLerpUpdateTime: float = 0.009999999776482582
    mLerpHandle: TimerHandle
    CachedExpansionStep: int32
    mUseMouse = True
    mRestoreFocusWhenLost = True
    mDesiredHorizontalAlignment = 2
    mDesiredVerticalAlignment = 2
    mCallCustomTickOnConstruct = True
    
    def UpdateStandByButton(self, Producing: bool):
        ReturnValue: bool = Not_PreBool(Producing)
        self.Widget_StandbyButton.SetStandbyButtonBrush(ReturnValue)
    

    def ToggleStandby(self):
        NewStandByMode = False
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L354')
        ReturnValue_0: bool = self.mRadarTower.IsProductionPaused()
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        NewStandByMode = ReturnValue_1
        ReturnValue_2: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_2.Server_SetIsProductionPausedOnFactory(self.mRadarTower, NewStandByMode)
        self.Widget_StandbyButton.SetStandbyButtonBrush(NewStandByMode)
    

    def RevealStepToNormalizedRevealPercent(self, inInt: int32):
        ReturnValue: float = self.mRadarTower.GetNormalizedProgressValueForStep(inInt)
        ReturnValue_0: float = ReturnValue
    

    def InitScanLines(self):
        ExecutionFlow.Push("L1094")
        Variable: int32 = 0
        # Label 28
        ReturnValue: int32 = self.mRadarTower.GetNumRadarExpansionSteps()
        ReturnValue_0: int32 = ReturnValue - 1
        ReturnValue1: bool = Variable <= ReturnValue_0
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1020")
        LocalIndex = Variable
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Widget_RadarTower_ScanLine] = Default__WidgetBlueprintLibrary.Create(self, Widget_RadarTower_ScanLine, ReturnValue_1)
        
        X = None
        Y = None
        BreakVector2D(self.mMovingScanLine.Brush.ImageSize, Ref[X], Ref[Y])
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue_2, "mMaxSize", X)
        ReturnValue_3: float = self.RevealStepToNormalizedRevealPercent(LocalIndex)
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue_2, "mNormalizedRadius", ReturnValue_3)
        ReturnValue_4: Ptr[OverlaySlot] = self.mScanlineContainer.AddChildToOverlay(ReturnValue_2)
        ReturnValue_4.SetHorizontalAlignment(0)
        ReturnValue_4.SetVerticalAlignment(0)
        # Label 639
        Variable_0: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        Variable1: LinearColor = LinearColor(R = 0.09530699998140335, G = 0.09530699998140335, B = 0.09530699998140335, A = 1)
        ReturnValue_5: bool = self.mRadarTower.HasPower()
        ReturnValue_6: int32 = self.mRadarTower.GetCurrentExpansionStep()
        ReturnValue_7: bool = LocalIndex <= ReturnValue_6
        ReturnValue_8: bool = ReturnValue_7 and ReturnValue_5
        Variable_1: bool = ReturnValue_8
        
        switch = {
            False: Variable1,
            True: Variable_0
        }
        ReturnValue_2.SetColorAndOpacity(switch.get(Variable_1, None))
        goto(ExecutionFlow.Pop())
        # Label 1020
        ReturnValue_9: int32 = Variable + 1
        Variable = ReturnValue_9
        goto('L28')
    

    def UpdateTitle(self, OverrideText: FText):
        Interface: TScriptInterface[FGActorRepresentationInterface] = QueryInterface[FGActorRepresentationInterface](self.mRadarTower)
        bSuccess: bool = Interface
        if not bSuccess:
            goto('L1841')
        ReturnValue: FText = GetInterfaceUObject(Interface).GetActorRepresentationText()
        # Label 134
        ReturnValue_0: FText = Default__KismetSystemLibrary.MakeLiteralText()
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 206, 'Value': 'Radar Tower'}"
        
        ReturnValue_1: bool = Default__KismetTextLibrary.NotEqual_TextText(Ref[OverrideText], Ref[ReturnValue_0])
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_StringToText("")
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_StringToText("Radar Tower")
        Variable2: bool = ReturnValue_1
        FormatArgumentData.ArgumentName = "Name"
        FormatArgumentData.ArgumentValueType = 4
        
        switch = {
            False: ReturnValue,
            True: OverrideText
        }
        FormatArgumentData.ArgumentValue = switch.get(Variable2, None)
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        
        switch_0 = {
            False: ReturnValue,
            True: OverrideText
        }
        
        switch_0.get(Variable2, None) = None
        ReturnValue_3: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[switch_0.get(Variable2, None)], Ref[ReturnValue_2])
        Array: List[FormatArgumentData] = [FormatArgumentData]
        
        switch_1 = {
            False: ReturnValue,
            True: OverrideText
        }
        
        switch_1.get(Variable2, None) = None
        ReturnValue1_0: bool = Default__KismetTextLibrary.EqualEqual_TextText(Ref[switch_1.get(Variable2, None)], Ref[ReturnValue1])
        ReturnValue_4: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 963, 'Value': 'Radar Tower: {Name}'}", Array)
        ReturnValue_5: bool = BooleanOR(ReturnValue1_0, ReturnValue_3)
        Variable_0: bool = ReturnValue_5
        
        switch_2 = {
            False: ReturnValue_4,
            True: Variable
        }
        self.Widget_Window_DarkMode.SetTitle(switch_2.get(Variable_0, None))
        ReturnValue_0 = Default__KismetSystemLibrary.MakeLiteralText()
        
        ReturnValue_1 = Default__KismetTextLibrary.NotEqual_TextText(Ref[OverrideText], Ref[ReturnValue_0])
        Variable1: FText = 
        ReturnValue_2 = Default__KismetTextLibrary.Conv_StringToText("")
        ReturnValue1 = Default__KismetTextLibrary.Conv_StringToText("Radar Tower")
        Variable2 = ReturnValue_1
        
        switch_3 = {
            False: ReturnValue,
            True: OverrideText
        }
        
        switch_3.get(Variable2, None) = None
        ReturnValue_3 = Default__KismetTextLibrary.EqualEqual_TextText(Ref[switch_3.get(Variable2, None)], Ref[ReturnValue_2])
        
        switch_4 = {
            False: ReturnValue,
            True: OverrideText
        }
        
        switch_4.get(Variable2, None) = None
        ReturnValue1_0 = Default__KismetTextLibrary.EqualEqual_TextText(Ref[switch_4.get(Variable2, None)], Ref[ReturnValue1])
        ReturnValue_5 = BooleanOR(ReturnValue1_0, ReturnValue_3)
        Variable1_0: bool = ReturnValue_5
        
        switch_5 = {
            False: ReturnValue,
            True: OverrideText
        }
        
        switch_6 = {
            False: switch_5.get(Variable2, None),
            True: Variable1
        }
        self.mTowerName.SetText(switch_6.get(Variable1_0, None))
        # End
        # Label 1841
        ReturnValue = 
        goto('L134')
    

    def SecondsToMinutesAndSecondsText(self, Input: float):
        ReturnValue: Timespan = FromSeconds(Input)
        
        Days = None
        Hours = None
        Minutes = None
        Seconds = None
        Milliseconds = None
        BreakTimespan(ReturnValue, Ref[Days], Ref[Hours], Ref[Minutes], Ref[Seconds], Ref[Milliseconds])
        ReturnValue_0: int32 = Days * 24
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_IntToText(Seconds, False, True, 2, 324)
        ReturnValue_2: int32 = ReturnValue_0 + Hours
        FormatArgumentData.ArgumentName = "Seconds"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_1
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue1: int32 = ReturnValue_2 * 60
        ReturnValue1_0: int32 = ReturnValue1 + Minutes
        ReturnValue1_1: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue1_0, False, True, 2, 324)
        FormatArgumentData1.ArgumentName = "Minutes"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue1_1
        FormatArgumentData1.ArgumentValueInt = 0
        # Label 746
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 887, 'Value': '{Minutes}:{Seconds}'}", Array)
        Output = ReturnValue_3
    

    def InitScannedPercent(self):
        Variable: float = 0
        ReturnValue1: int32 = self.mRadarTower.GetCurrentExpansionStep()
        ReturnValue1_0: float = self.RevealStepToNormalizedRevealPercent(ReturnValue1)
        ReturnValue1_1: bool = self.mRadarTower.HasPower()
        Variable2: bool = ReturnValue1_1
        
        switch = {
            False: Variable,
            True: ReturnValue1_0
        }
        self.mScannedAreaMaterial.SetScalarParameterValue("NormalizedRadius", switch.get(Variable2, None))
        Variable_0: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 297, 'Value': 'PAUSED'}"
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 361, 'Value': 'NO POWER'}"
        ReturnValue: bool = self.mRadarTower.IsProductionPaused()
        Variable_1: bool = ReturnValue
        ReturnValue_0: int32 = self.mRadarTower.GetCurrentExpansionStep()
        ReturnValue_1: float = self.RevealStepToNormalizedRevealPercent(ReturnValue_0)
        ReturnValue_2: FText = Default__KismetTextLibrary.AsPercent_Float(ReturnValue_1, 0, False, True, 1, 324, 0, 0)
        ReturnValue_3: bool = self.mRadarTower.HasPower()
        Variable1_0: bool = ReturnValue_3
        
        switch_0 = {
            False: Variable1,
            True: ReturnValue_2
        }
        
        switch_1 = {
            False: switch_0.get(Variable1_0, None),
            True: Variable_0
        }
        self.mPercentScanned.SetText(switch_1.get(Variable_1, None))
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_RadarTower(1273)
    

    def OnRadiusChanged(self):
        self.ExecuteUbergraph_Widget_RadarTower(2364)
    

    def UpdateScanTimer(self):
        self.ExecuteUbergraph_Widget_RadarTower(2392)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_RadarTower(2520)
    

    def BndEvt__mTowerName_K2Node_ComponentBoundEvent_0_OnEditableTextCommittedEvent__DelegateSignature(self, text: Const[Ref[FText]], CommitMethod: uint8):
        ExecuteUbergraph_Widget_RadarTower.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_RadarTower.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_RadarTower(2577)
    

    def LerpScannedAreaEvent(self):
        self.ExecuteUbergraph_Widget_RadarTower(3435)
    

    def BndEvt__mRadarTower_K2Node_ComponentBoundEvent_2_BuildingStateChanged__DelegateSignature(self, State: bool):
        ExecuteUbergraph_Widget_RadarTower.K2Node_ComponentBoundEvent_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_RadarTower(4707)
    

    def BndEvt__Widget_StandbyButton_K2Node_ComponentBoundEvent_3_OnStandbyClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_RadarTower(4712)
    

    def OnProductionChanged(self, HasChanged: bool):
        ExecuteUbergraph_Widget_RadarTower.K2Node_CustomEvent_HasChanged = HasChanged #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_RadarTower(4727)
    

    def ExecuteUbergraph_Widget_RadarTower(self):
        goto(ComputedJump("EntryPoint"))
        
        # Label 15
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mLerpHandle])
        goto(ExecutionFlow.Pop())
        # Label 58
        ExecutionFlow.Push("L570")
        ReturnValue1: Ptr[Widget] = self.mScanlineContainer.GetChildAt(Variable)
        Line1: Ptr[Widget_RadarTower_ScanLine] = Cast[Widget_RadarTower_ScanLine](ReturnValue1)
        bSuccess4: bool = Line1
        if not bSuccess4:
           goto(ExecutionFlow.Pop())
        Variable: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        Variable1: LinearColor = LinearColor(R = 0.09530699998140335, G = 0.09530699998140335, B = 0.09530699998140335, A = 1)
        ReturnValue1_0: int32 = self.mRadarTower.GetCurrentExpansionStep()
        ReturnValue2: bool = self.mRadarTower.HasPower()
        ReturnValue: bool = Variable <= ReturnValue1_0
        ReturnValue_0: bool = ReturnValue and ReturnValue2
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        Line1.SetColorAndOpacity(switch.get(Variable_0, None))
        goto(ExecutionFlow.Pop())
        # Label 570
        ReturnValue_1: int32 = Variable + 1
        Variable = ReturnValue_1
        # Label 639
        ReturnValue_2: int32 = self.mScanlineContainer.GetChildrenCount()
        ReturnValue_3: bool = Variable <= ReturnValue_2
        if not ReturnValue_3:
            goto('L746')
        goto('L58')
        # Label 746
        ReturnValue_4: bool = self.mRadarTower.HasPower()
        if not ReturnValue_4:
            goto('L1024')
        ReturnValue4: int32 = self.mRadarTower.GetCurrentExpansionStep()
        ReturnValue_5: bool = ReturnValue4 != self.CachedExpansionStep
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        OutputDelegate3.BindUFunction(self, LerpScannedAreaEvent)
        ReturnValue1_1: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate3, self.mLerpUpdateTime, True)
        self.mLerpHandle = ReturnValue1_1
        goto(ExecutionFlow.Pop())
        # Label 1024
        self.mTimeUntilNextScan.SetText("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1061, 'Value': 'NO POWER'}")
        goto(ExecutionFlow.Pop())
        # Label 1109
        ReturnValue1_2: bool = self.mRadarTower.HasPower()
        if not ReturnValue1_2:
            goto('L1184')
        if not Variable1_0:
            goto('L1236')
        goto(ExecutionFlow.Pop())
        # Label 1184
        Variable1_0: bool = False
        if not Variable2:
            goto('L1210')
        goto(ExecutionFlow.Pop())
        # Label 1210
        Variable2: bool = True
        self.OnRadiusChanged()
        goto(ExecutionFlow.Pop())
        # Label 1236
        Variable1_0 = True
        Variable2 = False
        self.OnRadiusChanged()
        goto(ExecutionFlow.Pop())
        self.Construct()
        Tower: Ptr[FGBuildableRadarTower] = Cast[FGBuildableRadarTower](self.mInteractObject)
        bSuccess: bool = Tower
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        self.mRadarTower = Tower
        ReturnValue3: int32 = self.mRadarTower.GetCurrentExpansionStep()
        self.CachedExpansionStep = ReturnValue3
        self.UpdateTitle()
        OutputDelegate.BindUFunction(self, OnEscapePressed)
        self.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate)
        OutputDelegate1.BindUFunction(self, OnRadiusChanged)
        self.mRadarTower.OnRadarTowerRadiusUpdated.AddUnique(OutputDelegate1)
        OutputDelegate4.BindUFunction(self, UpdateStandByButton)
        self.mRadarTower.mOnHasProductionChanged.AddUnique(OutputDelegate4)
        ReturnValue_6: Ptr[MaterialInstanceDynamic] = self.mScannedArea.GetDynamicMaterial()
        self.mScannedAreaMaterial = ReturnValue_6
        
        X = None
        Y = None
        BreakVector2D(self.mScannedArea.Brush.ImageSize, Ref[X], Ref[Y])
        self.mScannedAreaMaterial.SetScalarParameterValue("MaxSize", X)
        ReturnValue1_3: Ptr[MaterialInstanceDynamic] = self.mMovingScanLine.GetDynamicMaterial()
        
        X1 = None
        Y1 = None
        BreakVector2D(self.mMovingScanLine.Brush.ImageSize, Ref[X1], Ref[Y1])
        ReturnValue1_3.SetScalarParameterValue("MaxSize", X1)
        self.UpdateScanTimer()
        OutputDelegate2.BindUFunction(self, UpdateScanTimer)
        ReturnValue_7: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate2, 0.30000001192092896, True)
        self.mScanTimer = ReturnValue_7
        ReturnValue_8: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.ScanCircle, 0, 0, 0, 1)
        self.InitScanLines()
        self.InitScannedPercent()
        ReturnValue_9: bool = self.mRadarTower.IsProductionPaused()
        self.Widget_StandbyButton.SetStandbyButtonBrush(ReturnValue_9)
        OutputDelegate5.BindUFunction(self, OnProductionChanged)
        self.mRadarTower.mOnHasProductionChanged.AddUnique(OutputDelegate5)
        goto(ExecutionFlow.Pop())
        Variable = 0
        goto('L639')
        ReturnValue_10: float = self.mRadarTower.GetTimeToNextExpansion()
        
        Output = None
        self.SecondsToMinutesAndSecondsText(ReturnValue_10, Ref[Output])
        self.mTimeUntilNextScan.SetText(Output)
        goto(ExecutionFlow.Pop())
        self.Destruct()
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mScanTimer])
        goto('L15')
        CmpSuccess: bool = NotEqual_ByteByte(CommitMethod, 0)
        if not CmpSuccess:
            goto('L3234')
        CmpSuccess = NotEqual_ByteByte(CommitMethod, 1)
        if not CmpSuccess:
            goto('L2713')
        CmpSuccess = NotEqual_ByteByte(CommitMethod, 2)
        if not CmpSuccess:
            goto('L3234')
        goto(ExecutionFlow.Pop())
        # Label 2713
        Interface: TScriptInterface[FGActorRepresentationInterface] = QueryInterface[FGActorRepresentationInterface](self.mRadarTower)
        bSuccess1: bool = Interface
        if not bSuccess1:
            goto('L3209')
        FormatArgumentData.ArgumentName = "Name"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = Text
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_11: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 3054, 'Value': 'Radar Tower: {Name}'}", Array)
        
        ReturnValue_12: FText = GetInterfaceUObject(Interface).SetActorRepresentationText(Ref[ReturnValue_11])
        # Label 3185
        self.UpdateTitle(Text)
        goto(ExecutionFlow.Pop())
        # Label 3209
        ReturnValue_12 = 
        goto('L3185')
        # Label 3234
        Interface1: TScriptInterface[FGActorRepresentationInterface] = QueryInterface[FGActorRepresentationInterface](self.mRadarTower)
        bSuccess2: bool = Interface1
        if not bSuccess2:
            goto('L3410')
        ReturnValue_13: FText = GetInterfaceUObject(Interface1).GetActorRepresentationText()
        # Label 3368
        self.mTowerName.SetText(ReturnValue_13)
        goto(ExecutionFlow.Pop())
        # Label 3410
        ReturnValue_13 = 
        goto('L3368')
        ReturnValue_14: float = self.mScannedAreaLerpT + self.mLerpUpdateTime
        ReturnValue_15: float = FClamp(ReturnValue_14, 0, 1)
        self.mScannedAreaLerpT = ReturnValue_15
        ReturnValue2_0: int32 = self.mRadarTower.GetCurrentExpansionStep()
        ReturnValue_16: float = self.RevealStepToNormalizedRevealPercent(ReturnValue2_0)
        ReturnValue1_4: float = self.RevealStepToNormalizedRevealPercent(self.CachedExpansionStep)
        ReturnValue1_5: float = Ease(ReturnValue1_4, ReturnValue_16, self.mScannedAreaLerpT, 7, 2, 2)
        self.mScannedAreaMaterial.SetScalarParameterValue("NormalizedRadius", ReturnValue1_5)
        ReturnValue2_0 = self.mRadarTower.GetCurrentExpansionStep()
        ReturnValue_16 = self.RevealStepToNormalizedRevealPercent(ReturnValue2_0)
        ReturnValue1_4 = self.RevealStepToNormalizedRevealPercent(self.CachedExpansionStep)
        ReturnValue1_5 = Ease(ReturnValue1_4, ReturnValue_16, self.mScannedAreaLerpT, 7, 2, 2)
        ReturnValue_17: FText = Default__KismetTextLibrary.AsPercent_Float(ReturnValue1_5, 0, False, True, 1, 324, 0, 0)
        self.mPercentScanned.SetText(ReturnValue_17)
        ReturnValue_18: int32 = self.mRadarTower.GetCurrentExpansionStep()
        ReturnValue_19: Ptr[Widget] = self.mScanlineContainer.GetChildAt(ReturnValue_18)
        Line: Ptr[Widget_RadarTower_ScanLine] = Cast[Widget_RadarTower_ScanLine](ReturnValue_19)
        bSuccess3: bool = Line
        if not bSuccess3:
            goto('L4520')
        ReturnValue_20: float = Ease(0, 1, self.mScannedAreaLerpT, 5, 2, 2)
        ReturnValue_21: LinearColor = LinearColorLerp(LinearColor(R = 0.09530699998140335, G = 0.09530699998140335, B = 0.09530699998140335, A = 1), LinearColor(R = 1, G = 1, B = 1, A = 1), ReturnValue_20)
        Line.SetColorAndOpacity(ReturnValue_21)
        # Label 4520
        ReturnValue_22: bool = GreaterEqual_FloatFloat(self.mScannedAreaLerpT, 1)
        if not ReturnValue_22:
           goto(ExecutionFlow.Pop())
        ReturnValue5: int32 = self.mRadarTower.GetCurrentExpansionStep()
        self.CachedExpansionStep = ReturnValue5
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mLerpHandle])
        self.mScannedAreaLerpT = 0
        goto(ExecutionFlow.Pop())
        goto('L1109')
        self.ToggleStandby()
        goto(ExecutionFlow.Pop())
        self.InitScannedPercent()
        goto(ExecutionFlow.Pop())
    
