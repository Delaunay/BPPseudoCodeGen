
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.PowerPoleWall.Build_PowerPoleWall import Build_PowerPoleWall

class Build_PowerPoleWall_Mk2(Build_PowerPoleWall):
    mDisplayName = NSLOCTEXT("", "DEEEE01349157EA3E08139852D0250DB", "Wall Outlet  Mk.2")
    mDescription = NSLOCTEXT("", "96A62EB94767EE5F65E2ADA8418EC506", "Power Pole that attaches to a wall.\r\n\r\nCan handle up to 7 Power Line connections.\r\n\r\nConnect Power Poles, Power Generators and factory buildings together with Power Lines to create a power grid. The power grid supplies the connected buildings with power.")
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
    
