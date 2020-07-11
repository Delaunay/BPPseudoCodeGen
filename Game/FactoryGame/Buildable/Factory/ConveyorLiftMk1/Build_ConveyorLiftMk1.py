
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import FGBuildableConveyorLift
from Game.FactoryGame.Buildable.Factory.ConveyorBeltMk1.Audio.Play_F_Construction_ConveyorBelt import Play_F_Construction_ConveyorBelt
from Game.FactoryGame.Buildable.Factory.ConveyorLiftMk1.Build_ConveyorLiftMk1 import ExecuteUbergraph_Build_ConveyorLiftMk1

class Build_ConveyorLiftMk1(FGBuildableConveyorLift):
    mMeshHeight = 200
    mBottomMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk1/Mesh/ConveyorLift_Bottom_static_LOD0.ConveyorLift_Bottom_static_LOD0')
    mMidMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk1/Mesh/ConveyorLiftMid_Mk1_static_LOD0.ConveyorLiftMid_Mk1_static_LOD0')
    mTopMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk1/Mesh/ConveyorLift_Top_static_LOD0.ConveyorLift_Top_static_LOD0')
    mBellowMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk1/Mesh/ConveyorLift_Connector.ConveyorLift_Connector')
    mShelfMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk1/Mesh/ConveyorLift_Lift_01.ConveyorLift_Lift_01')
    mSpeed = 120
    mConnection0 = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGFactoryConnectionComponent', ObjectFlags=2883617, ObjectName='ConveyorAny0', bNetAddressable=True, mConnectorClearance=200, mDirection='EFactoryConnectionDirection::FCD_ANY', mForwardPeekAndGrabToBuildable=True)
    mConnection1 = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGFactoryConnectionComponent', ObjectFlags=2883617, ObjectName='ConveyorAny1', RelativeLocation={'X': 100, 'Y': 0, 'Z': 0}, bNetAddressable=True, mConnectorClearance=200, mDirection='EFactoryConnectionDirection::FCD_ANY', mForwardPeekAndGrabToBuildable=True)
    mHologramClass = NewObject[FGConveyorLiftHologram]()
    mDisplayName = NSLOCTEXT("", "5C5A467946AE13761CD97AB4188241D3", "Conveyor Lift Mk.1")
    mDescription = NSLOCTEXT("", "B55C6E1642062D242A3BB695B625186D", "Transports up to 60 resources per minute. Used to move resources between floors.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def PlayConstructSound(self):
        self.ExecuteUbergraph_Build_ConveyorLiftMk1(10)
    

    def ExecuteUbergraph_Build_ConveyorLiftMk1(self):
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_F_Construction_ConveyorBelt, self, True)
    
