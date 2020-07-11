
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.ConveyorBeltMk1.Build_ConveyorBeltMk1 import ExecuteUbergraph_Build_ConveyorBeltMk1
from Script.AkAudio import PostAkEvent
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import FGBuildableConveyorBelt
from Game.FactoryGame.Buildable.Factory.ConveyorBeltMk1.Audio.Play_F_Construction_ConveyorBelt import Play_F_Construction_ConveyorBelt

class Build_ConveyorBeltMk1(FGBuildableConveyorBelt):
    mMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk1/Mesh/SM_ConveyorBelt_Mk1.SM_ConveyorBelt_Mk1')
    mMeshLength = 200
    mSplineComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/Engine.SplineComponent', ObjectFlags=2883617, ObjectName='SplineComponent')
    mInstancedSplineComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, ObjectClass='/Script/InstancedSplines.FGInstancedSplineMeshComponent', ObjectFlags=2883617, ObjectName='InstancedSplineComponent')
    mSplineAudioEvent = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk1/Audio/Play_F_ConveyorBelt_Loop.Play_F_ConveyorBelt_Loop')
    mSpeed = 120
    mConnection0 = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGFactoryConnectionComponent', ObjectFlags=2883617, ObjectName='ConveyorAny0', bNetAddressable=True, mConnectorClearance=0, mDirection='EFactoryConnectionDirection::FCD_ANY', mForwardPeekAndGrabToBuildable=True)
    mConnection1 = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGFactoryConnectionComponent', ObjectFlags=2883617, ObjectName='ConveyorAny1', RelativeLocation={'X': 100, 'Y': 0, 'Z': 0}, bNetAddressable=True, mConnectorClearance=0, mDirection='EFactoryConnectionDirection::FCD_ANY', mForwardPeekAndGrabToBuildable=True)
    mHologramClass = NewObject[Holo_ConveyorBelt]()
    mDisplayName = NSLOCTEXT("", "49ED32984B7579C073C305A7E6AEC94F", "Conveyor Belt Mk.1")
    mDescription = NSLOCTEXT("", "3D7423FC4A6F790A0392FABBC5C13EAF", "Transports up to 60 resources per minute. Used to move resources between buildings.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_ConveyorBuild.BP_MaterialEffect_ConveyorBuild_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    NetUpdateFrequency = 3
    MinNetUpdateFrequency = 1
    NetPriority = 0.800000011920929
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def PlayConstructSound(self):
        self.ExecuteUbergraph_Build_ConveyorBeltMk1(10)
    

    def ExecuteUbergraph_Build_ConveyorBeltMk1(self):
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_F_Construction_ConveyorBelt, self, True)
    
