
from codegen.ue4_stub import *

from Script.Engine import GetTangentAtDistanceAlongSpline
from Script.Engine import FinishSpawningActor
from Script.Engine import AddSplinePointAtIndex
from Script.Engine import Delay
from Script.Engine import GetRotationAtSplinePoint
from Script.Engine import PlayFromStart
from Script.Engine import K2_SetWorldLocationAndRotation
from Script.Engine import GetLocationAtDistanceAlongSpline
from Script.CoreUObject import Rotator
from Script.Engine import VSize
from Script.Engine import GetNumberOfSplinePoints
from Script.Engine import ReceiveBeginPlay
from Script.Engine import SplineMeshComponent
from Game.FactoryGame.Buildable.Factory.-Shared.BP_BuildEffect_PipelineSegment import BP_BuildEffect_PipelineSegment
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import EffectDone
from Script.Engine import ETimelineDirection
from Script.Engine import ReceiveTick
from Script.FactoryGame import GetAttachment
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import MaterialInstance
from Script.Engine import GetRotationAtDistanceAlongSpline
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.-Shared.BP_BuildEffect_Pipeline import ExecuteUbergraph_BP_BuildEffect_Pipeline.K2Node_Event_DeltaSeconds
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.FactoryGame import FGBuildablePipeBase
from Script.FactoryGame import FGBuildEffectSpline
from Script.Engine import FCeil
from Script.Engine import Default__GameplayStatics
from Script.AkAudio import PostAssociatedAkEvent
from Script.Engine import Conv_VectorToRotator
from Script.Engine import SplineComponent
from Script.CoreUObject import Vector
from Script.Engine import Percent_IntInt
from Script.Engine import K2_GetComponentLocation
from Script.Engine import GetSplineLength
from Script.FactoryGame import FGPipeBuilderTrail
from Script.Engine import K2_SetActorLocationAndRotation
from Script.Engine import MakeTransform
from Script.Engine import ParticleSystemComponent
from Script.Engine import Actor
from Game.FactoryGame.Buildable.Factory.-Shared.BP_BuildEffect_Pipeline import ExecuteUbergraph_BP_BuildEffect_Pipeline
from Script.Engine import GetOwner
from Script.FactoryGame import GetSplineComponent
from Script.Engine import SetTangentAtSplinePoint
from Script.Engine import SetLocationAtSplinePoint
from Script.CoreUObject import Transform
from Script.Engine import StaticMesh

class BP_BuildEffect_Pipeline(FGBuildEffectSpline):
    MoveParticleEffect_Time_C5045958477A801600BF8BAD6657365D: float
    MoveParticleEffect__Direction_C5045958477A801600BF8BAD6657365D: uint8
    mMesh: Ptr[StaticMesh] = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/Pipeline/Mesh/Pipeline.Pipeline')
    mPipeMaterial: Ptr[MaterialInstance] = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Material/Pipeline_Materialize_Inst.Pipeline_Materialize_Inst')
    mSplinePointLocationArray: List[Vector]
    mSplinePointTangentArray: List[Vector]
    mSplineMeshLength: float = 200
    Local_CurrentSplineMesh: Ptr[SplineMeshComponent]
    mLoopIndex: int32
    Particle: Ptr[ParticleSystemComponent]
    mSplineInitialized: bool
    mWantToStartEffect: bool
    mSegmentListan: List[Ptr[BP_BuildEffect_PipelineSegment]]
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    
    def GetSplineData(self):
        ExecutionFlow.Push("L1573")
        ReturnValue: Ptr[Actor] = self.GetOwner()
        Base: Ptr[FGBuildablePipeBase] = Cast[FGBuildablePipeBase](ReturnValue)
        bSuccess: bool = Base
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        # Label 123
        ReturnValue_0: Ptr[SplineComponent] = Base.GetSplineComponent()
        ReturnValue_1: float = ReturnValue_0.GetSplineLength()
        ReturnValue_2: float = ReturnValue_1 / self.mSplineMeshLength
        ReturnValue_3: int32 = FCeil(ReturnValue_2)
        ReturnValue_4: bool = Variable <= ReturnValue_3
        if not ReturnValue_4:
            goto('L1044')
        ExecutionFlow.Push("L1056")
        localLoopIndex = Variable
        ReturnValue_0 = Base.GetSplineComponent()
        ReturnValue_1 = ReturnValue_0.GetSplineLength()
        ReturnValue_2 = ReturnValue_1 / self.mSplineMeshLength
        ReturnValue_3 = FCeil(ReturnValue_2)
        ReturnValue_5: bool = localLoopIndex != ReturnValue_3
        if not ReturnValue_5:
            goto('L1130')
        ReturnValue_0 = Base.GetSplineComponent()
        ReturnValue_6: float = localLoopIndex * self.mSplineMeshLength
        ReturnValue_7: Vector = ReturnValue_0.GetLocationAtDistanceAlongSpline(ReturnValue_6, 0)
        
        ReturnValue2: int32 = self.mSplinePointLocationArray.append(ReturnValue_7)
        ReturnValue_0 = Base.GetSplineComponent()
        ReturnValue_6 = localLoopIndex * self.mSplineMeshLength
        ReturnValue1: Vector = ReturnValue_0.GetTangentAtDistanceAlongSpline(ReturnValue_6, 1)
        
        ReturnValue1_0: int32 = self.mSplinePointTangentArray.append(ReturnValue1)
        goto(ExecutionFlow.Pop())
        # Label 1044
        self.mSplineInitialized = True
        goto(ExecutionFlow.Pop())
        # Label 1056
        ReturnValue_8: int32 = Variable + 1
        Variable = ReturnValue_8
        goto('L123')
        # Label 1130
        ReturnValue_0 = Base.GetSplineComponent()
        ReturnValue_1 = ReturnValue_0.GetSplineLength()
        ReturnValue1_1: Vector = ReturnValue_0.GetLocationAtDistanceAlongSpline(ReturnValue_1, 0)
        
        ReturnValue3: int32 = self.mSplinePointLocationArray.append(ReturnValue1_1)
        ReturnValue_0 = Base.GetSplineComponent()
        ReturnValue_1 = ReturnValue_0.GetSplineLength()
        ReturnValue_9: Vector = ReturnValue_0.GetTangentAtDistanceAlongSpline(ReturnValue_1, 1)
        
        ReturnValue_10: int32 = self.mSplinePointTangentArray.append(ReturnValue_9)
        goto(ExecutionFlow.Pop())
    

    def SpawnSplineSegment(self, LoopIndex: int32, SplineLength: int32):
        ReturnValue: Vector = self.DefaultSceneRoot.K2_GetComponentLocation()
        ReturnValue_0: Rotator = self.Spline.GetRotationAtSplinePoint(LoopIndex, 1)
        
        Item2 = None
        Item2 = self.mSplinePointLocationArray[LoopIndex]
        ReturnValue1: Vector = ReturnValue + Item2
        ReturnValue_1: Transform = MakeTransform(ReturnValue1, ReturnValue_0, Vector(1, 1, 1))
        
        ReturnValue_2: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_BuildEffect_PipelineSegment, 1, None, Ref[ReturnValue_1])
        ReturnValue = self.DefaultSceneRoot.K2_GetComponentLocation()
        ReturnValue_0 = self.Spline.GetRotationAtSplinePoint(LoopIndex, 1)
        
        Item2 = None
        Item2 = self.mSplinePointLocationArray[LoopIndex]
        ReturnValue1 = ReturnValue + Item2
        ReturnValue_1 = MakeTransform(ReturnValue1, ReturnValue_0, Vector(1, 1, 1))
        
        ReturnValue_3: Ptr[BP_BuildEffect_PipelineSegment] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_2, Ref[ReturnValue_1])
        ReturnValue_4: int32 = LoopIndex + 1
        ReturnValue_5: int32 = Percent_IntInt(ReturnValue_4, SplineLength)
        ReturnValue = self.DefaultSceneRoot.K2_GetComponentLocation()
        
        Item1 = None
        Item1 = self.mSplinePointLocationArray[ReturnValue_5]
        ReturnValue_6: Vector = ReturnValue + Item1
        
        ReturnValue_3.Spline.SetLocationAtSplinePoint(1, 1, True, Ref[ReturnValue_6])
        ReturnValue_3.mMesh = self.mMesh
        ReturnValue_3.mPipeMaterial = self.mPipeMaterial
        
        Item3 = None
        Item3 = self.mSplinePointTangentArray[LoopIndex]
        ReturnValue1_0: float = VSize(Item3)
        ReturnValue1_1: bool = ReturnValue1_0 > self.mSplineMeshLength
        ReturnValue1_2: float = self.mSplineMeshLength / ReturnValue1_0
        ReturnValue1_3: Vector = Item3 * ReturnValue1_2
        Variable1: bool = ReturnValue1_1
        
        switch = {
            False: Item3,
            True: ReturnValue1_3
        }
        ReturnValue_3.mStartTangent = switch.get(Variable1, None)
        ReturnValue_4 = LoopIndex + 1
        ReturnValue_5 = Percent_IntInt(ReturnValue_4, SplineLength)
        
        Item = None
        Item = self.mSplinePointTangentArray[ReturnValue_5]
        ReturnValue_7: float = VSize(Item)
        ReturnValue_8: bool = ReturnValue_7 > self.mSplineMeshLength
        ReturnValue_9: float = self.mSplineMeshLength / ReturnValue_7
        Variable: bool = ReturnValue_8
        ReturnValue_10: Vector = Item * ReturnValue_9
        
        switch_0 = {
            False: Item,
            True: ReturnValue_10
        }
        ReturnValue_3.mEndTangent = switch_0.get(Variable, None)
        ReturnValue_3.AddMesh()
        
        ReturnValue_11: int32 = self.mSegmentListan.append(ReturnValue_3)
    

    def InitiateSpline(self):
        ExecutionFlow.Push("L504")
        TangentCap: float = 200
        Variable: int32 = 0
        
        # Label 51
        ReturnValue: int32 = len(self.mSplinePointLocationArray)
        ReturnValue_0: int32 = ReturnValue - 1
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L430")
        
        Item1 = None
        Item1 = self.mSplinePointLocationArray[Variable]
        
        Item1 = None
        self.Spline.AddSplinePointAtIndex(Variable, 0, True, Ref[Item1])
        
        Item = None
        Item = self.mSplinePointTangentArray[Variable]
        
        Item = None
        self.Spline.SetTangentAtSplinePoint(Variable, 1, True, Ref[Item])
        goto(ExecutionFlow.Pop())
        # Label 430
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L51')
    

    def MoveParticleEffect__FinishedFunc(self):
        self.ExecuteUbergraph_BP_BuildEffect_Pipeline(2305)
    

    def MoveParticleEffect__UpdateFunc(self):
        self.ExecuteUbergraph_BP_BuildEffect_Pipeline(784)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_BuildEffect_Pipeline(1601)
    

    def BeginEffect(self):
        self.ExecuteUbergraph_BP_BuildEffect_Pipeline(1693)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_BuildEffect_Pipeline.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_BuildEffect_Pipeline(2122)
    

    def ExecuteUbergraph_BP_BuildEffect_Pipeline(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue: Ptr[Actor] = self.GetOwner()
        ReturnValue.SetActorHiddenInGame(False)
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 118
        ReturnValue_0: int32 = len(self.mSegmentListan)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L357')
        Variable_0 = Variable
        ExecutionFlow.Push("L372")
        
        Item1 = None
        Item1 = self.mSegmentListan[Variable_0]
        Item1.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        # Label 357
        self.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        # Label 372
        ReturnValue1: int32 = Variable + 1
        Variable = ReturnValue1
        goto('L118')
        # Label 446
        ReturnValue_2: Ptr[FGPipeBuilderTrail] = self.GetAttachment()
        ReturnValue_2.EffectDone()
        # Label 498
        self.MaterializeParticle.Deactivate()
        ReturnValue1_0: int32 = self.Ak_StopLoop.PostAssociatedAkEvent()
        Default__KismetSystemLibrary.Delay(self, 1, LatentActionInfo(Linkage = 15, UUID = -257081962, ExecutionFunction = "ExecuteUbergraph_BP_BuildEffect_Pipeline", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 661
        ReturnValue_2 = self.GetAttachment()
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_2)
        if not ReturnValue_3:
            goto('L498')
        goto('L446')
        # Label 751
        self.MoveParticleEffect.PlayFromStart()
        goto(ExecutionFlow.Pop())
        ReturnValue1_1: Ptr[FGPipeBuilderTrail] = self.GetAttachment()
        ReturnValue1_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_1)
        if not ReturnValue1_2:
            goto('L1268')
        
        Item = None
        Item = self.mSegmentListan[self.mLoopIndex]
        ReturnValue_4: float = self.MoveParticleEffect_Time_C5045958477A801600BF8BAD6657365D * self.mSplineMeshLength
        ReturnValue_5: Vector = Item.Spline.GetTangentAtDistanceAlongSpline(ReturnValue_4, 1)
        ReturnValue_6: Rotator = Conv_VectorToRotator(ReturnValue_5)
        ReturnValue_7: Vector = Item.Spline.GetLocationAtDistanceAlongSpline(ReturnValue_4, 1)
        ReturnValue2: Ptr[FGPipeBuilderTrail] = self.GetAttachment()
        
        SweepHitResult = None
        ReturnValue_8: bool = ReturnValue2.K2_SetActorLocationAndRotation(ReturnValue_7, ReturnValue_6, False, False, Ref[SweepHitResult])
        
        Item = None
        # Label 1268
        Item = self.mSegmentListan[self.mLoopIndex]
        ReturnValue_4 = self.MoveParticleEffect_Time_C5045958477A801600BF8BAD6657365D * self.mSplineMeshLength
        ReturnValue_9: Rotator = Item.Spline.GetRotationAtDistanceAlongSpline(ReturnValue_4, 1)
        ReturnValue_7 = Item.Spline.GetLocationAtDistanceAlongSpline(ReturnValue_4, 1)
        
        SweepHitResult = None
        self.MaterializeParticle.K2_SetWorldLocationAndRotation(ReturnValue_7, ReturnValue_9, False, False, Ref[SweepHitResult])
        goto(ExecutionFlow.Pop())
        self.ReceiveBeginPlay()
        self.GetSplineData()
        if not self.mSplineInitialized:
           goto(ExecutionFlow.Pop())
        ReturnValue1_3: Ptr[Actor] = self.GetOwner()
        ReturnValue1_3.SetActorHiddenInGame(True)
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1763")
        self.InitiateSpline()
        ReturnValue_10: int32 = self.Ak_StartLoop.PostAssociatedAkEvent()
        goto(ExecutionFlow.Pop())
        # Label 1763
        ReturnValue_11: int32 = self.Spline.GetNumberOfSplinePoints()
        ReturnValue1_4: int32 = ReturnValue_11 - 4
        ReturnValue_12: bool = self.mLoopIndex <= ReturnValue1_4
        if not ReturnValue_12:
            goto('L661')
        ReturnValue_11 = self.Spline.GetNumberOfSplinePoints()
        ReturnValue_13: int32 = ReturnValue_11 - 1
        self.SpawnSplineSegment(self.mLoopIndex, ReturnValue_13)
        goto('L751')
        # Label 2036
        if not Variable_1:
            goto('L2051')
        goto(ExecutionFlow.Pop())
        # Label 2051
        Variable_1: bool = True
        self.BeginEffect()
        goto(ExecutionFlow.Pop())
        # Label 2077
        Variable_1 = True
        goto(ExecutionFlow.Pop())
        # Label 2089
        Variable_2: bool = True
        if not False:
           goto(ExecutionFlow.Pop())
        goto('L2077')
        # Label 2107
        if not Variable_2:
            goto('L2089')
        goto(ExecutionFlow.Pop())
        self.ReceiveTick(DeltaSeconds)
        ReturnValue_14: bool = self.mSplineInitialized and self.mWantToStartEffect
        if not ReturnValue_14:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L2036")
        goto('L2107')
        # Label 2199
        self.mLoopIndex = Variable_3
        goto('L1763')
        # Label 2231
        ReturnValue_15: int32 = self.mLoopIndex + 1
        Variable_3: int32 = ReturnValue_15
        goto('L2199')
        goto('L2231')
    
