
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.ConveyorLiftMk1.Build_ConveyorLiftMk1 import Build_ConveyorLiftMk1

class Build_ConveyorLiftMk3(Build_ConveyorLiftMk1):
    mMeshHeight = 200
    mMidMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk3/Mesh/ConveyorLiftMid_Mk3_static_LOD0.ConveyorLiftMid_Mk3_static_LOD0')
    mSpeed = 540
    mConnection0 = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGFactoryConnectionComponent', ObjectFlags=2883617, ObjectName='ConveyorAny0', bNetAddressable=True, mConnectorClearance=200, mDirection='EFactoryConnectionDirection::FCD_ANY', mForwardPeekAndGrabToBuildable=True)
    mConnection1 = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGFactoryConnectionComponent', ObjectFlags=2883617, ObjectName='ConveyorAny1', RelativeLocation={'X': 100, 'Y': 0, 'Z': 0}, bNetAddressable=True, mConnectorClearance=200, mDirection='EFactoryConnectionDirection::FCD_ANY', mForwardPeekAndGrabToBuildable=True)
    mDisplayName = NSLOCTEXT("", "047200AB48621F1F089EA39EF655FE78", "Conveyor Lift Mk.3")
    mDescription = NSLOCTEXT("", "64110F11433E0C3C662BBB856E92769D", "Transports up to 270 resources per minute. Used to move resources between floors.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
