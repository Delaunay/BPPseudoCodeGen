
from codegen.ue4_stub import *

from Script.FactoryGame import FGConveyorPoleStackable

class Build_ConveyorPoleStackable(FGConveyorPoleStackable):
    mHeight = 100
    mPoleComponentProxy = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, ComponentTags=['PoleMesh'], Mobility=0, ObjectClass='/Script/FactoryGame.FGColoredInstanceMeshProxy', ObjectFlags=2883617, ObjectName='PoleComponentProxy', bGenerateOverlapEvents=False)
    mSnapOnly0 = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, ComponentTags=['PoleHeight'], Mobility=0, ObjectClass='/Script/FactoryGame.FGFactoryConnectionComponent', ObjectFlags=2883617, ObjectName='SnapOnly0', RelativeLocation={'X': 0, 'Y': 0, 'Z': 300}, mConnectorClearance=0, mDirection='EFactoryConnectionDirection::FCD_SNAP_ONLY')
    mUseStaticHeight = True
    mCanStack = True
    mStackHeight = 200
    mHologramClass = NewObject[FGPoleHologram]()
    mDisplayName = NSLOCTEXT("", "9AA85FB14CE8061CC16D08A0129DE294", "Stackable Conveyor Pole")
    mDescription = NSLOCTEXT("", "12B7A8464A49BFC28BB03393CE3D5F51", "Conveyor pole with fixed size that is stackable")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=False, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
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
    
