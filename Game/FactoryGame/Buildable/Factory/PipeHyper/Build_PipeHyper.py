
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.PipeHyper.Build_PipeHyper import ExecuteUbergraph_Build_PipeHyper
from Script.Engine import GetDisplayName
from Script.Engine import JoinStringArray
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Factory.PipeHyper.Build_PipeHyper import ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_SweepResult
from Game.FactoryGame.Buildable.Factory.PipeHyper.Build_PipeHyper import ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_bFromSweep1
from Game.FactoryGame.Buildable.Factory.PipeHyper.Build_PipeHyper import ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_OtherBodyIndex1
from Game.FactoryGame.Buildable.Factory.PipeHyper.Build_PipeHyper import ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_OverlappedComponent1
from Game.FactoryGame.Buildable.Factory.PipeHyper.Build_PipeHyper import ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_SweepResult1
from Game.FactoryGame.Buildable.Factory.PipeHyper.Build_PipeHyper import ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_bFromSweep
from Game.FactoryGame.Buildable.Factory.PipeHyper.Build_PipeHyper import ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_OtherComp
from Script.Engine import Default__KismetStringLibrary
from Game.FactoryGame.Buildable.Factory.PipeHyper.Build_PipeHyper import ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_OverlappedComponent
from Game.FactoryGame.Buildable.Factory.PipeHyper.Build_PipeHyper import ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_OtherActor
from Game.FactoryGame.Buildable.Factory.PipeHyper.Build_PipeHyper import ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_OtherComp1
from Script.FactoryGame import FGBuildablePipeHyper
from Game.FactoryGame.Buildable.Factory.PipeHyper.Build_PipeHyper import ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_OtherBodyIndex
from Game.FactoryGame.Buildable.Factory.PipeHyper.Build_PipeHyper import ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_OtherActor1
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class Build_PipeHyper(FGBuildablePipeHyper):
    mMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/PipeHyper/Mesh/SM_HyperTube_01.SM_HyperTube_01')
    mMeshLength = 100
    mSplineComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/Engine.SplineComponent', ObjectFlags=2883617, ObjectName='SplineComponent')
    mInstancedSplineComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, ObjectClass='/Script/InstancedSplines.FGInstancedSplineMeshComponent', ObjectFlags=2883617, ObjectName='InstancedSplineComponent')
    mHologramClass = NewObject[Holo_PipeHyper]()
    mDisplayName = NSLOCTEXT("", "F47AA5734D3C62747D47C3AABDC6D92C", "Hyper Tube")
    mDescription = NSLOCTEXT("", "EF96EA4D469F98DC529DFA9277E5D476", "Tubes for transporting Ficsit employees.\r\nA Hyper Tube Entrance needs to be attached to power and enter a Hyper Tube system.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_PipelineBuild.BP_MaterialEffect_PipelineBuild_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def UserConstructionScript(self):
        self.mConnection0 = self.PipeHyperConnection0
        self.mConnection1 = self.PipeHyperConnection1
    

    def BndEvt__PipeHyperOverlap0_K2Node_ComponentBoundEvent_0_ComponentBeginOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32, bFromSweep: bool, SweepResult: Const[Ref[HitResult]]):
        ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_OverlappedComponent1 = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_OtherActor1 = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_OtherComp1 = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_OtherBodyIndex1 = OtherBodyIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_bFromSweep1 = bFromSweep #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_SweepResult1 = SweepResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_PipeHyper(250)
    

    def BndEvt__PipeHyperOverlap1_K2Node_ComponentBoundEvent_1_ComponentBeginOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32, bFromSweep: bool, SweepResult: Const[Ref[HitResult]]):
        ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_OverlappedComponent = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_OtherActor = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_OtherBodyIndex = OtherBodyIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_bFromSweep = bFromSweep #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_PipeHyper.K2Node_ComponentBoundEvent_SweepResult = SweepResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_PipeHyper(10)
    

    def ExecuteUbergraph_Build_PipeHyper(self):
        ReturnValue: FString = Default__KismetSystemLibrary.GetDisplayName(OverlappedComponent)
        Array: Const[List[FString]] = ["Overlap: ", ReturnValue]
        
        ReturnValue_0: FString = Default__KismetStringLibrary.JoinStringArray(" ", Ref[Array])
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_0, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        # End
        ReturnValue1: FString = Default__KismetSystemLibrary.GetDisplayName(OverlappedComponent1)
        Array1: Const[List[FString]] = ["Overlap: ", ReturnValue1]
        
        ReturnValue1_0: FString = Default__KismetStringLibrary.JoinStringArray(" ", Ref[Array1])
        Default__KismetSystemLibrary.PrintString(self, ReturnValue1_0, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
    
