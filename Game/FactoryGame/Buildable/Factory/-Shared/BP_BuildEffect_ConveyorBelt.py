
from codegen.ue4_stub import *

from Script.Engine import GetTangentAtDistanceAlongSpline
from Script.Engine import FinishSpawningActor
from Script.Engine import AddSplinePointAtIndex
from Script.Engine import Delay
from Script.Engine import GetRotationAtSplinePoint
from Script.Engine import PlayFromStart
from Game.FactoryGame.Buildable.Factory.-Shared.BP_BuildEffect_ConveyorBelt import ExecuteUbergraph_BP_BuildEffect_ConveyorBelt
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
from Game.FactoryGame.Buildable.Factory.-Shared.BP_BuildEffect_ConveyorBelt import ExecuteUbergraph_BP_BuildEffect_ConveyorBelt.K2Node_Event_DeltaSeconds
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import MaterialInstance
from Script.Engine import GetRotationAtDistanceAlongSpline
from Game.FactoryGame.Buildable.Factory.-Shared.BP_BuildEffect_ConveyorBeltSegment import BP_BuildEffect_ConveyorBeltSegment
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.FactoryGame import GetSplineMesh
from Script.Engine import FCeil
from Script.Engine import Default__GameplayStatics
from Script.AkAudio import PostAssociatedAkEvent
from Script.Engine import SplineComponent
from Script.CoreUObject import Vector
from Script.Engine import Percent_IntInt
from Script.Engine import K2_GetComponentLocation
from Script.Engine import GetSplineLength
from Script.FactoryGame import FGBuildableConveyorBelt
from Script.Engine import MakeTransform
from Script.Engine import ParticleSystemComponent
from Script.Engine import Actor
from Script.Engine import GetOwner
from Script.FactoryGame import GetSplineComponent
from Script.Engine import SetTangentAtSplinePoint
from Script.Engine import SetLocationAtSplinePoint
from Script.CoreUObject import Transform
from Script.Engine import StaticMesh

class BP_BuildEffect_ConveyorBelt(Actor):
    MoveParticleEffect_Time_4811E78B4C611AB8FA5FFAA13FD3D646: float
    MoveParticleEffect__Direction_4811E78B4C611AB8FA5FFAA13FD3D646: uint8
    mMesh: Ptr[StaticMesh]
    mMaterialBelt: Ptr[MaterialInstance] = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Material/ConveyorBelt_Materialize_Inst.ConveyorBelt_Materialize_Inst')
    mMaterialSides: Ptr[MaterialInstance] = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Material/ConveyorFactory_Materialize_Inst.ConveyorFactory_Materialize_Inst')
    mSplinePointLocationArray: List[Vector]
    mSplinePointTangentArray: List[Vector]
    mSplineMeshLength: float = 200
    Local_CurrentSplineMesh: Ptr[SplineMeshComponent]
    mDelayDuration: float = 0.10000000149011612
    mLoopIndex: int32
    mSegmentList: List[Ptr[BP_BuildEffect_ConveyorBeltSegment]]
    Particle: Ptr[ParticleSystemComponent]
    mSplineInitialized: bool
    mWantToStartEffect: bool
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    
    def GetSplineData(self):
        ExecutionFlow.Push("L2134")
        ReturnValue: Ptr[Actor] = self.GetOwner()
        Belt: Ptr[FGBuildableConveyorBelt] = Cast[FGBuildableConveyorBelt](ReturnValue)
        bSuccess: bool = Belt
        ReturnValue_0: Ptr[StaticMesh] = Belt.GetSplineMesh()
        self.mMesh = ReturnValue_0
        Variable: int32 = 0
        # Label 174
        ReturnValue = self.GetOwner()
        Belt = Cast[FGBuildableConveyorBelt](ReturnValue)
        bSuccess = Belt
        ReturnValue_1: Ptr[SplineComponent] = Belt.GetSplineComponent()
        ReturnValue_2: float = ReturnValue_1.GetSplineLength()
        ReturnValue_3: float = ReturnValue_2 / self.mSplineMeshLength
        ReturnValue_4: int32 = FCeil(ReturnValue_3)
        ReturnValue_5: bool = Variable <= ReturnValue_4
        if not ReturnValue_5:
            goto('L1435')
        ExecutionFlow.Push("L1447")
        localLoopIndex = Variable
        ReturnValue = self.GetOwner()
        Belt = Cast[FGBuildableConveyorBelt](ReturnValue)
        bSuccess = Belt
        ReturnValue_1 = Belt.GetSplineComponent()
        ReturnValue_2 = ReturnValue_1.GetSplineLength()
        ReturnValue_3 = ReturnValue_2 / self.mSplineMeshLength
        ReturnValue_4 = FCeil(ReturnValue_3)
        ReturnValue_6: bool = localLoopIndex != ReturnValue_4
        if not ReturnValue_6:
            goto('L1521')
        ReturnValue = self.GetOwner()
        Belt = Cast[FGBuildableConveyorBelt](ReturnValue)
        # Label 886
        bSuccess = Belt
        ReturnValue_1 = Belt.GetSplineComponent()
        ReturnValue_7: float = localLoopIndex * self.mSplineMeshLength
        ReturnValue1: Vector = ReturnValue_1.GetLocationAtDistanceAlongSpline(ReturnValue_7, 0)
        
        ReturnValue2: int32 = self.mSplinePointLocationArray.append(ReturnValue1)
        ReturnValue = self.GetOwner()
        Belt = Cast[FGBuildableConveyorBelt](ReturnValue)
        bSuccess = Belt
        ReturnValue_1 = Belt.GetSplineComponent()
        ReturnValue_7 = localLoopIndex * self.mSplineMeshLength
        ReturnValue1_0: Vector = ReturnValue_1.GetTangentAtDistanceAlongSpline(ReturnValue_7, 1)
        
        ReturnValue3: int32 = self.mSplinePointTangentArray.append(ReturnValue1_0)
        goto(ExecutionFlow.Pop())
        # Label 1435
        self.mSplineInitialized = True
        goto(ExecutionFlow.Pop())
        # Label 1447
        ReturnValue_8: int32 = Variable + 1
        Variable = ReturnValue_8
        goto('L174')
        # Label 1521
        ReturnValue = self.GetOwner()
        Belt = Cast[FGBuildableConveyorBelt](ReturnValue)
        bSuccess = Belt
        ReturnValue_1 = Belt.GetSplineComponent()
        ReturnValue_2 = ReturnValue_1.GetSplineLength()
        ReturnValue_9: Vector = ReturnValue_1.GetLocationAtDistanceAlongSpline(ReturnValue_2, 0)
        
        ReturnValue1_1: int32 = self.mSplinePointLocationArray.append(ReturnValue_9)
        ReturnValue = self.GetOwner()
        Belt = Cast[FGBuildableConveyorBelt](ReturnValue)
        bSuccess = Belt
        ReturnValue_1 = Belt.GetSplineComponent()
        ReturnValue_2 = ReturnValue_1.GetSplineLength()
        ReturnValue_10: Vector = ReturnValue_1.GetTangentAtDistanceAlongSpline(ReturnValue_2, 1)
        
        ReturnValue_11: int32 = self.mSplinePointTangentArray.append(ReturnValue_10)
        goto(ExecutionFlow.Pop())
    

    def SpawnSplineSegment(self, LoopIndex: int32, SplineLength: int32):
        ReturnValue: Vector = self.DefaultSceneRoot.K2_GetComponentLocation()
        ReturnValue_0: Rotator = self.Spline.GetRotationAtSplinePoint(LoopIndex, 1)
        
        Item2 = None
        Item2 = self.mSplinePointLocationArray[LoopIndex]
        ReturnValue1: Vector = ReturnValue + Item2
        ReturnValue_1: Transform = MakeTransform(ReturnValue1, ReturnValue_0, Vector(1, 1, 1))
        
        ReturnValue_2: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_BuildEffect_ConveyorBeltSegment, 1, None, Ref[ReturnValue_1])
        ReturnValue = self.DefaultSceneRoot.K2_GetComponentLocation()
        ReturnValue_0 = self.Spline.GetRotationAtSplinePoint(LoopIndex, 1)
        
        Item2 = None
        Item2 = self.mSplinePointLocationArray[LoopIndex]
        ReturnValue1 = ReturnValue + Item2
        ReturnValue_1 = MakeTransform(ReturnValue1, ReturnValue_0, Vector(1, 1, 1))
        
        ReturnValue_3: Ptr[BP_BuildEffect_ConveyorBeltSegment] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_2, Ref[ReturnValue_1])
        # Label 674
        ReturnValue_4: int32 = LoopIndex + 1
        ReturnValue = self.DefaultSceneRoot.K2_GetComponentLocation()
        ReturnValue_5: int32 = Percent_IntInt(ReturnValue_4, SplineLength)
        
        Item1 = None
        Item1 = self.mSplinePointLocationArray[ReturnValue_5]
        ReturnValue_6: Vector = ReturnValue + Item1
        
        ReturnValue_3.Spline.SetLocationAtSplinePoint(1, 1, True, Ref[ReturnValue_6])
        ReturnValue_3.mMesh = self.mMesh
        ReturnValue_3.mMaterialSides = self.mMaterialSides
        ReturnValue_3.mMaterialBelt = self.mMaterialBelt
        
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
        
        ReturnValue_11: int32 = self.mSegmentList.append(ReturnValue_3)
    

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
        self.ExecuteUbergraph_BP_BuildEffect_ConveyorBelt(2043)
    

    def MoveParticleEffect__UpdateFunc(self):
        self.ExecuteUbergraph_BP_BuildEffect_ConveyorBelt(2038)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_BuildEffect_ConveyorBelt(1046)
    

    def BeginEffect(self):
        self.ExecuteUbergraph_BP_BuildEffect_ConveyorBelt(1128)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_BuildEffect_ConveyorBelt.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_BuildEffect_ConveyorBelt(1633)
    

    def ExecuteUbergraph_BP_BuildEffect_ConveyorBelt(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue: Ptr[Actor] = self.GetOwner()
        ReturnValue.SetActorHiddenInGame(False)
        Variable: int32 = 0
        Variable1: int32 = 0
        
        # Label 118
        ReturnValue_0: int32 = len(self.mSegmentList)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L357')
        Variable1 = Variable
        ExecutionFlow.Push("L372")
        
        Item2 = None
        Item2 = self.mSegmentList[Variable1]
        Item2.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        # Label 357
        self.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        # Label 372
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L118')
        # Label 446
        ReturnValue_3: int32 = self.Ak_StopLoop.PostAssociatedAkEvent()
        Default__KismetSystemLibrary.Delay(self, 1, LatentActionInfo(Linkage = 15, UUID = 179108560, ExecutionFunction = "ExecuteUbergraph_BP_BuildEffect_ConveyorBelt", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 573
        ExecutionFlow.Push("L674")
        
        Item = None
        Item = self.mSegmentList[Variable_0]
        Item.PlayFinishEffect()
        goto(ExecutionFlow.Pop())
        # Label 674
        ReturnValue2: int32 = Variable1_0 + 1
        Variable1_0: int32 = ReturnValue2
        
        # Label 743
        ReturnValue1: int32 = len(self.mSegmentList)
        ReturnValue1_0: bool = Variable1_0 <= ReturnValue1
        if not ReturnValue1_0:
            goto('L886')
        Variable_0: int32 = Variable1_0
        goto('L573')
        # Label 886
        self.MaterializeParticle.Deactivate()
        goto('L446')
        # Label 927
        Variable_0 = 0
        goto('L743')
        # Label 955
        if not Variable_1:
            goto('L970')
        goto(ExecutionFlow.Pop())
        # Label 970
        Variable_1: bool = True
        self.BeginEffect()
        goto(ExecutionFlow.Pop())
        # Label 996
        Variable_2: bool = True
        if not False:
           goto(ExecutionFlow.Pop())
        Variable_1 = True
        goto(ExecutionFlow.Pop())
        # Label 1021
        if not Variable_2:
            goto('L996')
        goto(ExecutionFlow.Pop())
        # Label 1036
        ExecutionFlow.Push("L955")
        goto('L1021')
        self.ReceiveBeginPlay()
        ReturnValue1_1: Ptr[Actor] = self.GetOwner()
        ReturnValue1_1.SetActorHiddenInGame(True)
        self.GetSplineData()
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1198")
        self.InitiateSpline()
        ReturnValue1_2: int32 = self.Ak_StartLoop.PostAssociatedAkEvent()
        goto(ExecutionFlow.Pop())
        # Label 1198
        ReturnValue_4: int32 = self.Spline.GetNumberOfSplinePoints()
        ReturnValue1_3: int32 = ReturnValue_4 - 4
        ReturnValue_5: bool = self.mLoopIndex <= ReturnValue1_3
        if not ReturnValue_5:
            goto('L1499')
        ReturnValue_4 = self.Spline.GetNumberOfSplinePoints()
        ReturnValue_6: int32 = ReturnValue_4 - 1
        self.SpawnSplineSegment(self.mLoopIndex, ReturnValue_6)
        self.MoveParticleEffect.PlayFromStart()
        goto(ExecutionFlow.Pop())
        # Label 1499
        Variable1_0 = 0
        goto('L927')
        # Label 1527
        self.mLoopIndex = Variable_3
        goto('L1198')
        # Label 1559
        ReturnValue1_4: int32 = self.mLoopIndex + 1
        Variable_3: int32 = ReturnValue1_4
        goto('L1527')
        self.ReceiveTick(DeltaSeconds)
        ReturnValue_7: bool = self.mSplineInitialized and self.mWantToStartEffect
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        goto('L1036')
        
        Item1 = None
        # Label 1705
        Item1 = self.mSegmentList[self.mLoopIndex]
        ReturnValue_8: float = self.MoveParticleEffect_Time_4811E78B4C611AB8FA5FFAA13FD3D646 * self.mSplineMeshLength
        ReturnValue_9: Rotator = Item1.Spline.GetRotationAtDistanceAlongSpline(ReturnValue_8, 1)
        ReturnValue_10: Vector = Item1.Spline.GetLocationAtDistanceAlongSpline(ReturnValue_8, 1)
        
        SweepHitResult = None
        self.MaterializeParticle.K2_SetWorldLocationAndRotation(ReturnValue_10, ReturnValue_9, False, False, Ref[SweepHitResult])
        goto(ExecutionFlow.Pop())
        goto('L1705')
        goto('L1559')
    
