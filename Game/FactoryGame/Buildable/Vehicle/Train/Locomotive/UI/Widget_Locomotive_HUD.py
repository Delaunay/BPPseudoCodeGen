
from codegen.ue4_stub import *

from Script.Engine import Delay
from Script.Engine import FClamp
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import Pawn
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Locomotive_HUD import ExecuteUbergraph_Widget_Locomotive_HUD.K2Node_Event_MyGeometry
from Script.FactoryGame import GetTargetConsumption
from Script.FactoryGame import FGPowerInfoComponent
from Script.FactoryGame import HasPower
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Locomotive_HUD import ExecuteUbergraph_Widget_Locomotive_HUD
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import IsDocked
from Script.UMG import PlayAnimation
from Script.Engine import Conv_FloatToText
from Script.FactoryGame import GetDynamicBrake
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Locomotive_HUD import ExecuteUbergraph_Widget_Locomotive_HUD.K2Node_Event_InDeltaTime
from Script.FactoryGame import CmS2KmH
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import BooleanOR
from Script.FactoryGame import GetTrain
from Script.UMG import Construct
from Script.UMG import SetRenderAngle
from Script.Engine import PrintString
from Script.UMG import WidgetAnimation
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.FactoryGame import GetAirBrake
from Script.UMG import UserWidget
from Script.UMG import GetOwningPlayerPawn
from Script.UMG import UMGSequencePlayer
from Script.Engine import Abs
from Script.FactoryGame import FGTrain
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.BP_Locomotive import BP_Locomotive
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.FactoryGame import GetForwardSpeed
from Script.FactoryGame import GetPowerInfo
from Script.CoreUObject import LinearColor

class Widget_Locomotive_HUD(UserWidget):
    anim_DockingPulse: Ptr[WidgetAnimation]
    anim_BreakPulse: Ptr[WidgetAnimation]
    BPLocomotive: Ptr[BP_Locomotive]
    mUpdateStatsTimer: TimerHandle
    
    def CheckHasPower(self):
        ReturnValue: Ptr[FGPowerInfoComponent] = self.BPLocomotive.GetPowerInfo()
        ReturnValue_0: bool = ReturnValue.HasPower()
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        self.Widget_TrainWarning.ShouldForceWarning(ReturnValue_1, "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 159, 'Value': 'No Power'}")
    

    def SetSpeedometerPosition(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.BPLocomotive)
        if not ReturnValue:
            goto('L388')
        ReturnValue_0: float = self.BPLocomotive.mVehicleMovement.GetForwardSpeed()
        ReturnValue_1: float = Abs(ReturnValue_0)
        ReturnValue_2: float = ReturnValue_1 / 28
        ReturnValue_3: float = ReturnValue_2 * 0.6000000238418579
        ReturnValue_4: float = ReturnValue_3 - 45
        ReturnValue_5: float = FClamp(ReturnValue_4, -45, 45)
        self.PointerContainer.SetRenderAngle(ReturnValue_5)
    

    def GetPowerConsumptionText(self):
        ReturnValue: Ptr[FGPowerInfoComponent] = self.BPLocomotive.GetPowerInfo()
        ReturnValue_0: float = ReturnValue.GetTargetConsumption()
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_0, 0, False, True, 1, 324, 0, 0)
        ReturnValue_2: FText = ReturnValue_1
    

    def GetSpeedInKMHText(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.BPLocomotive)
        if not ReturnValue:
            goto('L343')
        ReturnValue_0: float = self.BPLocomotive.mVehicleMovement.GetForwardSpeed()
        ReturnValue_1: float = Default__FGBlueprintFunctionLibrary.CmS2KmH(ReturnValue_0)
        ReturnValue_2: float = Abs(ReturnValue_1)
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_FloatToText(ReturnValue_2, 0, False, True, 1, 324, 0, 0)
        ReturnValue_4: FText = ReturnValue_3
    

    def Tick(self):
        ExecuteUbergraph_Widget_Locomotive_HUD.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Locomotive_HUD.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Locomotive_HUD(983)
    

    def StartBrakeIndicatorAnim(self):
        self.ExecuteUbergraph_Widget_Locomotive_HUD(1266)
    

    def StopBrakeIndicatorAnim(self):
        self.ExecuteUbergraph_Widget_Locomotive_HUD(1305)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Locomotive_HUD(1344)
    

    def CheckIsDocked(self):
        self.ExecuteUbergraph_Widget_Locomotive_HUD(1359)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_Locomotive_HUD(1364)
    

    def UpdateStats(self):
        self.ExecuteUbergraph_Widget_Locomotive_HUD(1407)
    

    def ExecuteUbergraph_Widget_Locomotive_HUD(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.CheckHasPower()
        goto(ExecutionFlow.Pop())
        # Label 30
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Locomotive: Ptr[BP_Locomotive] = Cast[BP_Locomotive](ReturnValue)
        bSuccess: bool = Locomotive
        if not bSuccess:
            goto('L457')
        self.BPLocomotive = Locomotive
        ReturnValue_0: Ptr[FGTrain] = self.BPLocomotive.GetTrain()
        self.Widget_TrainWarning.Init(ReturnValue_0)
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.anim_DockingPulse, 0, 0, 0, 1)
        ReturnValue_1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.anim_BreakPulse, 0, 0, 0, 1)
        self.UpdateStats()
        OutputDelegate.BindUFunction(self, UpdateStats)
        ReturnValue_2: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.5, True)
        self.mUpdateStatsTimer = ReturnValue_2
        goto(ExecutionFlow.Pop())
        # Label 457
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 30, UUID = 90976893, ExecutionFunction = "ExecuteUbergraph_Widget_Locomotive_HUD", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 534
        Variable: bool = False
        self.mDockingIndicator.SetVisibility(3)
        Default__KismetSystemLibrary.PrintString(self, "Is Docked", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
        # Label 669
        Variable1: bool = False
        if not Variable2:
            goto('L695')
        goto(ExecutionFlow.Pop())
        # Label 695
        Variable2: bool = True
        self.StopBrakeIndicatorAnim()
        goto(ExecutionFlow.Pop())
        # Label 721
        if not Variable1:
            goto('L736')
        goto(ExecutionFlow.Pop())
        # Label 736
        Variable1 = True
        Variable2 = False
        self.StartBrakeIndicatorAnim()
        goto(ExecutionFlow.Pop())
        # Label 773
        if not Variable:
            goto('L788')
        goto(ExecutionFlow.Pop())
        # Label 788
        Variable = True
        self.mDockingIndicator.SetVisibility(2)
        goto(ExecutionFlow.Pop())
        # Label 838
        ReturnValue1_0: Ptr[FGTrain] = self.BPLocomotive.GetTrain()
        ReturnValue_3: bool = ReturnValue1_0.IsDocked()
        if not ReturnValue_3:
            goto('L951')
        if not Variable3:
            goto('L967')
        goto(ExecutionFlow.Pop())
        # Label 951
        Variable3: bool = False
        goto('L773')
        # Label 967
        Variable3 = True
        goto('L534')
        self.SetSpeedometerPosition()
        ReturnValue_4: float = self.BPLocomotive.mVehicleMovement.GetAirBrake()
        ReturnValue_5: float = self.BPLocomotive.mVehicleMovement.GetDynamicBrake()
        ReturnValue_6: bool = ReturnValue_4 > 0
        ReturnValue1_1: bool = ReturnValue_5 > 0
        ReturnValue_7: bool = BooleanOR(ReturnValue1_1, ReturnValue_6)
        if not ReturnValue_7:
            goto('L669')
        goto('L721')
        self.mBrakeIndicator.SetVisibility(3)
        goto(ExecutionFlow.Pop())
        self.mBrakeIndicator.SetVisibility(2)
        goto(ExecutionFlow.Pop())
        self.Construct()
        goto('L30')
        goto('L838')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mUpdateStatsTimer])
        goto(ExecutionFlow.Pop())
        self.CheckIsDocked()
        goto('L15')
    
