
from codegen.ue4_stub import *

from Script.FactoryGame import GetFloatCurveValue
from Script.Engine import VSizeSquared
from Script.FactoryGame import GetItemMesh
from Script.Engine import SpawnEmitterAtLocation
from Script.CoreUObject import Rotator
from Script.Engine import VSize
from Script.Engine import SetWorldScale3D
from Script.Engine import K2_SetWorldLocation
from Script.Engine import FindLookAtRotation
from Game.FactoryGame.Buildable.Factory.-Shared.BP_CostEffectActor import ExecuteUbergraph_BP_CostEffectActor
from Script.Engine import K2_SetActorLocation
from Script.Engine import Multiply_RotatorFloat
from Script.Engine import FMax
from Script.Engine import Default__GameplayStatics
from Script.Engine import BreakRotator
from Script.Engine import VInterpTo_Constant
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.Engine import K2_SetActorRotation
from Script.Engine import K2_GetComponentLocation
from Script.Engine import ComposeRotators
from Script.Engine import RuntimeFloatCurve
from Script.FactoryGame import Default__FGSkySphere
from Script.Engine import RandomRotator
from Script.Engine import MakeRotator
from Script.Engine import ParticleSystemComponent
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Script.Engine import K2_SetRelativeLocation
from Script.FactoryGame import Default__FGItemDescriptor
from Script.FactoryGame import FGItemDescriptor
from Game.FactoryGame.VFX.Misc.BuildEffect.P_PartHitSparks_01 import P_PartHitSparks_01
from Script.Engine import K2_SetRelativeRotation
from Game.FactoryGame.Buildable.Factory.-Shared.BP_CostEffectActor import ExecuteUbergraph_BP_CostEffectActor.K2Node_Event_DeltaSeconds
from Script.Engine import StaticMesh

class BP_CostEffectActor(Actor):
    mTargetLocation: Vector
    mTargetExtent: float
    mItemDescriptor: TSubclassOf[FGItemDescriptor]
    mRotationRate: Rotator
    OnReachedTarget: FMulticastScriptDelegate
    mTravelLength: float
    mArcOffset: Vector = Namespace(X=0, Y=0, Z=500)
    mArcCurveX: RuntimeFloatCurve = Namespace(EditorCurveData={'Keys': [], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/-Shared/Curve_CostEffectArcX.Curve_CostEffectArcX'})
    mArcCurveY: RuntimeFloatCurve = Namespace(EditorCurveData={'Keys': [], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/-Shared/Curve_CostEffectArcZ.Curve_CostEffectArcZ'})
    mArcCurve_SAFE: RuntimeFloatCurve = Namespace(EditorCurveData={'Keys': [], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/-Shared/Curve_CostEffectArcZ.Curve_CostEffectArcZ'})
    mTrailVfx: Ptr[ParticleSystemComponent]
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_CostEffectActor(2666)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_CostEffectActor.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_CostEffectActor(2163)
    

    def ExecuteUbergraph_BP_CostEffectActor(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        # Label 30
        self.mTrailVfx.Deactivate()
        goto('L15')
        # Label 71
        self.OnReachedTarget.ProcessMulticastDelegate()
        ExecutionFlow.Push("L110")
        if not Variable:
            goto('L281')
        goto(ExecutionFlow.Pop())
        # Label 110
        if not Variable:
            goto('L125')
        goto(ExecutionFlow.Pop())
        # Label 125
        Variable: bool = True
        ReturnValue: Vector = self.ItemMesh.K2_GetComponentLocation()
        ReturnValue_0: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_PartHitSparks_01, ReturnValue, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        goto('L30')
        # Label 281
        Variable = True
        if not False:
           goto(ExecutionFlow.Pop())
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 306
        ReturnValue_1: Vector = self.K2_GetActorLocation()
        ReturnValue_2: Vector = Subtract_VectorVector(ReturnValue_1, self.mTargetLocation)
        ReturnValue_3: float = VSize(ReturnValue_2)
        self.mTravelLength = ReturnValue_3
        ReturnValue_1 = self.K2_GetActorLocation()
        
        ReturnValue_4: Rotator = FindLookAtRotation(Ref[ReturnValue_1], Ref[self.mTargetLocation])
        ReturnValue_5: Rotator = RandomRotator(True)
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_5, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_6: float = Roll * 0.5
        ReturnValue_7: float = ReturnValue_6 - 90
        ReturnValue_8: Rotator = MakeRotator(ReturnValue_7, 0, 0)
        ReturnValue_9: Rotator = ComposeRotators(ReturnValue_4, ReturnValue_8)
        ReturnValue_10: bool = self.K2_SetActorRotation(ReturnValue_9, False)
        ReturnValue1: Vector = self.ItemMesh.K2_GetComponentLocation()
        ReturnValue1_0: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_PartHitSparks_01, ReturnValue1, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), False, 0)
        self.mTrailVfx = ReturnValue1_0
        goto(ExecutionFlow.Pop())
        # Label 960
        ReturnValue_11: float = FMax(self.mTargetExtent, 250)
        ReturnValue1_1: Vector = self.K2_GetActorLocation()
        ReturnValue1_2: Vector = Subtract_VectorVector(self.mTargetLocation, ReturnValue1_1)
        ReturnValue_12: float = VSizeSquared(ReturnValue1_2)
        ReturnValue_13: bool = ReturnValue_12 <= ReturnValue_11
        if not ReturnValue_13:
           goto(ExecutionFlow.Pop())
        goto('L71')
        # Label 1166
        ReturnValue1_3: Rotator = RandomRotator(True)
        self.mRotationRate = ReturnValue1_3
        goto('L306')
        # Label 1227
        ReturnValue2: Vector = self.K2_GetActorLocation()
        ReturnValue2_0: Vector = Subtract_VectorVector(ReturnValue2, self.mTargetLocation)
        ReturnValue1_4: float = VSize(ReturnValue2_0)
        ReturnValue_14: float = ReturnValue1_4 / self.mTravelLength
        
        ReturnValue_15: float = Default__FGSkySphere.GetFloatCurveValue(ReturnValue_14, Ref[self.mArcCurveY])
        ReturnValue1_5: Vector = self.mArcOffset * ReturnValue_15
        
        SweepHitResult = None
        self.ItemMesh.K2_SetRelativeLocation(ReturnValue1_5, False, False, Ref[SweepHitResult])
        ReturnValue_16: Rotator = Multiply_RotatorFloat(self.mRotationRate, DeltaSeconds)
        ReturnValue1_6: Rotator = ComposeRotators(self.ItemMesh.RelativeRotation, ReturnValue_16)
        
        SweepHitResult = None
        self.ItemMesh.K2_SetRelativeRotation(ReturnValue1_6, False, False, Ref[SweepHitResult])
        ReturnValue2 = self.K2_GetActorLocation()
        ReturnValue2_0 = Subtract_VectorVector(ReturnValue2, self.mTargetLocation)
        ReturnValue1_4 = VSize(ReturnValue2_0)
        ReturnValue_14 = ReturnValue1_4 / self.mTravelLength
        ReturnValue1_7: float = 1 - ReturnValue_14
        ReturnValue_17: Vector = Vector(0.800000011920929, 0.800000011920929, 0.800000011920929) * ReturnValue1_7
        ReturnValue_18: Vector = Vector(0.20000000298023224, 0.20000000298023224, 0.20000000298023224) + ReturnValue_17
        self.ItemMesh.SetWorldScale3D(ReturnValue_18)
        ReturnValue2_1: Vector = self.ItemMesh.K2_GetComponentLocation()
        
        SweepHitResult = None
        self.mTrailVfx.K2_SetWorldLocation(ReturnValue2_1, False, False, Ref[SweepHitResult])
        goto('L960')
        ReturnValue2 = self.K2_GetActorLocation()
        ReturnValue2_0 = Subtract_VectorVector(ReturnValue2, self.mTargetLocation)
        ReturnValue1_4 = VSize(ReturnValue2_0)
        ReturnValue_14 = ReturnValue1_4 / self.mTravelLength
        ReturnValue1_7 = 1 - ReturnValue_14
        ReturnValue1_8: float = 8000 * ReturnValue1_7
        ReturnValue1_9: float = FMax(ReturnValue1_8, 1000)
        ReturnValue_19: Vector = VInterpTo_Constant(ReturnValue2, self.mTargetLocation, DeltaSeconds, ReturnValue1_9)
        
        SweepHitResult = None
        ReturnValue_20: bool = self.K2_SetActorLocation(ReturnValue_19, False, False, Ref[SweepHitResult])
        goto('L1227')
        # Label 2555
        ReturnValue_21: Ptr[StaticMesh] = Default__FGItemDescriptor.GetItemMesh(self.mItemDescriptor)
        ReturnValue_22: bool = self.ItemMesh.SetStaticMesh(ReturnValue_21)
        goto('L1166')
        goto('L2555')
    

    def OnReachedTarget__DelegateSignature(self):
        pass
    
