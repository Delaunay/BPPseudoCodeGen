
from codegen.ue4_stub import *

from Script.Engine import GetTangentAtDistanceAlongSpline
from Script.Engine import FinishSpawningActor
from Script.Engine import AddSplinePointAtIndex
from Game.FactoryGame.Buildable.Factory.-Shared.BP_BuildEffect_TrainTrackSegment import BP_BuildEffect_TrainTrackSegment
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
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import ETimelineDirection
from Script.Engine import ReceiveTick
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import FGBuildableRailroadTrack
from Script.Engine import MaterialInstance
from Script.Engine import GetRotationAtDistanceAlongSpline
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.Engine import FCeil
from Script.Engine import Default__GameplayStatics
from Script.AkAudio import PostAssociatedAkEvent
from Script.Engine import SplineComponent
from Script.CoreUObject import Vector
from Script.Engine import Percent_IntInt
from Script.Engine import K2_GetComponentLocation
from Script.Engine import GetSplineLength
from Script.Engine import MakeTransform
from Script.Engine import ParticleSystemComponent
from Script.Engine import Actor
from Game.FactoryGame.Buildable.Factory.-Shared.BP_BuildEffect_TrainTrack import ExecuteUbergraph_BP_BuildEffect_TrainTrack.K2Node_Event_DeltaSeconds
from Script.Engine import GetOwner
from Script.FactoryGame import GetSplineComponent
from Game.FactoryGame.Buildable.Factory.-Shared.BP_BuildEffect_TrainTrack import ExecuteUbergraph_BP_BuildEffect_TrainTrack
from Script.Engine import SetTangentAtSplinePoint
from Script.Engine import SetLocationAtSplinePoint
from Script.CoreUObject import Transform
from Script.Engine import StaticMesh

class BP_BuildEffect_TrainTrack(Actor):
    MoveParticleEffect_Time_82E420F745BD1A027C3D16B22990E87F: float
    MoveParticleEffect__Direction_82E420F745BD1A027C3D16B22990E87F: uint8
    mMesh: Ptr[StaticMesh] = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/Train/Track/Mesh/SM_TrainTrack_02.SM_TrainTrack_02')
    mTrainMaterial: Ptr[MaterialInstance] = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/Train/Track/Material/MI_Track_Materialize.MI_Track_Materialize')
    mSplinePointLocationArray: List[Vector]
    mSplinePointTangentArray: List[Vector]
    mSplineMeshLength: float = 1200
    Local_CurrentSplineMesh: Ptr[SplineMeshComponent]
    mLoopIndex: int32
    Particle: Ptr[ParticleSystemComponent]
    mSplineInitialized: bool
    mWantToStartEffect: bool
    mSegmentListan: List[Ptr[BP_BuildEffect_TrainTrackSegment]]
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    
    def GetSplineData(self):
        ExecutionFlow.Push("L1573")
        ReturnValue: Ptr[Actor] = self.GetOwner()
        Track: Ptr[FGBuildableRailroadTrack] = Cast[FGBuildableRailroadTrack](ReturnValue)
        bSuccess: bool = Track
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        # Label 123
        ReturnValue_0: Ptr[SplineComponent] = Track.GetSplineComponent()
        ReturnValue_1: float = ReturnValue_0.GetSplineLength()
        ReturnValue_2: float = ReturnValue_1 / self.mSplineMeshLength
        ReturnValue_3: int32 = FCeil(ReturnValue_2)
        ReturnValue_4: bool = Variable <= ReturnValue_3
        if not ReturnValue_4:
            goto('L1044')
        ExecutionFlow.Push("L1056")
        localLoopIndex = Variable
        ReturnValue_0 = Track.GetSplineComponent()
        ReturnValue_1 = ReturnValue_0.GetSplineLength()
        ReturnValue_2 = ReturnValue_1 / self.mSplineMeshLength
        ReturnValue_3 = FCeil(ReturnValue_2)
        ReturnValue_5: bool = localLoopIndex != ReturnValue_3
        if not ReturnValue_5:
            goto('L1130')
        ReturnValue_0 = Track.GetSplineComponent()
        ReturnValue_6: float = localLoopIndex * self.mSplineMeshLength
        # Label 697
        ReturnValue_7: Vector = ReturnValue_0.GetLocationAtDistanceAlongSpline(ReturnValue_6, 0)
        
        ReturnValue1: int32 = self.mSplinePointLocationArray.append(ReturnValue_7)
        ReturnValue_0 = Track.GetSplineComponent()
        ReturnValue_6 = localLoopIndex * self.mSplineMeshLength
        ReturnValue1_0: Vector = ReturnValue_0.GetTangentAtDistanceAlongSpline(ReturnValue_6, 1)
        
        ReturnValue2: int32 = self.mSplinePointTangentArray.append(ReturnValue1_0)
        goto(ExecutionFlow.Pop())
        # Label 1044
        self.mSplineInitialized = True
        goto(ExecutionFlow.Pop())
        # Label 1056
        ReturnValue_8: int32 = Variable + 1
        Variable = ReturnValue_8
        goto('L123')
        # Label 1130
        ReturnValue_0 = Track.GetSplineComponent()
        ReturnValue_1 = ReturnValue_0.GetSplineLength()
        ReturnValue1_1: Vector = ReturnValue_0.GetLocationAtDistanceAlongSpline(ReturnValue_1, 0)
        
        ReturnValue3: int32 = self.mSplinePointLocationArray.append(ReturnValue1_1)
        ReturnValue_0 = Track.GetSplineComponent()
        ReturnValue_1 = ReturnValue_0.GetSplineLength()
        ReturnValue_9: Vector = ReturnValue_0.GetTangentAtDistanceAlongSpline(ReturnValue_1, 1)
        
        ReturnValue_10: int32 = self.mSplinePointTangentArray.append(ReturnValue_9)
        goto(ExecutionFlow.Pop())
    

    def SpawnSplineSegment(self, LoopIndex: int32, SplineLength: int32):
        ReturnValue: Vector = self.DefaultSceneRoot.K2_GetComponentLocation()
        ReturnValue_0: Rotator = self.Spline.GetRotationAtSplinePoint(LoopIndex, 1)
        
        Item2 = None
        # Label 111
        Item2 = self.mSplinePointLocationArray[LoopIndex]
        ReturnValue1: Vector = ReturnValue + Item2
        ReturnValue_1: Transform = MakeTransform(ReturnValue1, ReturnValue_0, Vector(1, 1, 1))
        
        ReturnValue_2: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_BuildEffect_TrainTrackSegment, 1, None, Ref[ReturnValue_1])
        ReturnValue = self.DefaultSceneRoot.K2_GetComponentLocation()
        ReturnValue_0 = self.Spline.GetRotationAtSplinePoint(LoopIndex, 1)
        
        Item2 = None
        Item2 = self.mSplinePointLocationArray[LoopIndex]
        ReturnValue1 = ReturnValue + Item2
        ReturnValue_1 = MakeTransform(ReturnValue1, ReturnValue_0, Vector(1, 1, 1))
        
        ReturnValue_3: Ptr[BP_BuildEffect_TrainTrackSegment] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_2, Ref[ReturnValue_1])
        ReturnValue_4: int32 = LoopIndex + 1
        ReturnValue_5: int32 = Percent_IntInt(ReturnValue_4, SplineLength)
        ReturnValue = self.DefaultSceneRoot.K2_GetComponentLocation()
        
        Item1 = None
        Item1 = self.mSplinePointLocationArray[ReturnValue_5]
        ReturnValue_6: Vector = ReturnValue + Item1
        
        ReturnValue_3.Spline.SetLocationAtSplinePoint(1, 1, True, Ref[ReturnValue_6])
        ReturnValue_3.mMesh = self.mMesh
        ReturnValue_3.mTrainMaterial = self.mTrainMaterial
        
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
        self.ExecuteUbergraph_BP_BuildEffect_TrainTrack(15)
    

    def MoveParticleEffect__UpdateFunc(self):
        self.ExecuteUbergraph_BP_BuildEffect_TrainTrack(1446)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_BuildEffect_TrainTrack(1779)
    

    def BeginEffect(self):
        self.ExecuteUbergraph_BP_BuildEffect_TrainTrack(1861)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_BuildEffect_TrainTrack.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_BuildEffect_TrainTrack(1941)
    

    def ExecuteUbergraph_BP_BuildEffect_TrainTrack(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue1: int32 = self.mLoopIndex + 1
        Variable: int32 = ReturnValue1
        self.mLoopIndex = Variable
        # Label 111
        ReturnValue: int32 = self.Spline.GetNumberOfSplinePoints()
        ReturnValue1_0: int32 = ReturnValue - 4
        ReturnValue_0: bool = self.mLoopIndex <= ReturnValue1_0
        if not ReturnValue_0:
            goto('L412')
        ReturnValue = self.Spline.GetNumberOfSplinePoints()
        ReturnValue_1: int32 = ReturnValue - 1
        self.SpawnSplineSegment(self.mLoopIndex, ReturnValue_1)
        self.MoveParticleEffect.PlayFromStart()
        goto(ExecutionFlow.Pop())
        # Label 412
        Variable1: int32 = 0
        Variable_0: int32 = 0
        
        # Label 458
        ReturnValue_2: int32 = len(self.mSegmentListan)
        ReturnValue_3: bool = Variable1 <= ReturnValue_2
        if not ReturnValue_3:
            goto('L697')
        Variable_0 = Variable1
        ExecutionFlow.Push("L1217")
        
        Item = None
        Item = self.mSegmentListan[Variable_0]
        Item.PlayFinishEffect()
        goto(ExecutionFlow.Pop())
        # Label 697
        self.MaterializeParticle.Deactivate()
        ReturnValue1_1: int32 = self.Ak_StopLoop.PostAssociatedAkEvent()
        Default__KismetSystemLibrary.Delay(self, 1, LatentActionInfo(Linkage = 860, UUID = 719931592, ExecutionFunction = "ExecuteUbergraph_BP_BuildEffect_TrainTrack", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue_4: Ptr[Actor] = self.GetOwner()
        ReturnValue_4.SetActorHiddenInGame(False)
        Variable_1: int32 = 0
        Variable1_0: int32 = 0
        
        # Label 963
        ReturnValue1_2: int32 = len(self.mSegmentListan)
        ReturnValue1_3: bool = Variable_1 <= ReturnValue1_2
        if not ReturnValue1_3:
            goto('L1202')
        Variable1_0 = Variable_1
        ExecutionFlow.Push("L1291")
        
        Item1 = None
        Item1 = self.mSegmentListan[Variable1_0]
        Item1.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        # Label 1202
        self.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        # Label 1217
        ReturnValue2: int32 = Variable1 + 1
        Variable1 = ReturnValue2
        goto('L458')
        # Label 1291
        ReturnValue_5: int32 = Variable_1 + 1
        Variable_1 = ReturnValue_5
        goto('L963')
        # Label 1365
        Variable_2: bool = True
        if not False:
           goto(ExecutionFlow.Pop())
        Variable_3: bool = True
        goto(ExecutionFlow.Pop())
        # Label 1390
        if not Variable_2:
            goto('L1365')
        goto(ExecutionFlow.Pop())
        # Label 1405
        if not Variable_3:
            goto('L1420')
        goto(ExecutionFlow.Pop())
        # Label 1420
        Variable_3 = True
        self.BeginEffect()
        goto(ExecutionFlow.Pop())
        ReturnValue_6: float = self.MoveParticleEffect_Time_82E420F745BD1A027C3D16B22990E87F * self.mSplineMeshLength
        
        Item2 = None
        Item2 = self.mSegmentListan[self.mLoopIndex]
        ReturnValue_7: Rotator = Item2.Spline.GetRotationAtDistanceAlongSpline(ReturnValue_6, 1)
        ReturnValue_8: Vector = Item2.Spline.GetLocationAtDistanceAlongSpline(ReturnValue_6, 1)
        
        SweepHitResult = None
        self.MaterializeParticle.K2_SetWorldLocationAndRotation(ReturnValue_8, ReturnValue_7, False, False, Ref[SweepHitResult])
        goto(ExecutionFlow.Pop())
        self.ReceiveBeginPlay()
        ReturnValue1_4: Ptr[Actor] = self.GetOwner()
        ReturnValue1_4.SetActorHiddenInGame(True)
        self.GetSplineData()
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L111")
        self.InitiateSpline()
        ReturnValue_9: int32 = self.Ak_StartLoop.PostAssociatedAkEvent()
        goto(ExecutionFlow.Pop())
        # Label 1931
        ExecutionFlow.Push("L1405")
        goto('L1390')
        self.ReceiveTick(DeltaSeconds)
        ReturnValue_10: bool = self.mSplineInitialized and self.mWantToStartEffect
        if not ReturnValue_10:
           goto(ExecutionFlow.Pop())
        goto('L1931')
    
