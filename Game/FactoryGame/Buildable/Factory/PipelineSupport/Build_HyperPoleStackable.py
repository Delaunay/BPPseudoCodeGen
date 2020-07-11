
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Buildable.Factory.PipelineSupport.Build_HyperPoleStackable import ExecuteUbergraph_Build_HyperPoleStackable
from Script.FactoryGame import FGBuildablePipelineSupport
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.Factory.ConveyorBeltMk1.Audio.Play_F_Construction_ConveyorBelt import Play_F_Construction_ConveyorBelt

class Build_HyperPoleStackable(FGBuildablePipelineSupport):
    mLength = 200
    mSupportComponentDefaultMesh = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, ComponentTags=['PoleMesh'], Mobility=0, ObjectClass='/Script/FactoryGame.FGColoredInstanceMeshProxy', ObjectFlags=2883617, ObjectName='SupportMeshCompProxyHolder', bGenerateOverlapEvents=False)
    mUseStaticHeight = True
    mCanStack = True
    mStackHeight = 200
    mHologramClass = NewObject[MyFGPipelineSupportHologramStack]()
    mDisplayName = INVTEXT("Stackable Hyper Tube Support")
    mDescription = NSLOCTEXT("", "7BB13CFF471D2098D117CC9B5D0BBFF8", "Support for Hyper Tubes. Can be stacked on other stackable supports.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=False, bCanEverTick=False, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=False, bCanEverTick=False, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def UserConstructionScript(self):
        self.mSnapOnly0 = self.PipelineSupportSnap
    

    def PlayConstructSound_1(self):
        self.ExecuteUbergraph_Build_HyperPoleStackable(10)
    

    def ExecuteUbergraph_Build_HyperPoleStackable(self):
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_F_Construction_ConveyorBelt, self, True)
    
