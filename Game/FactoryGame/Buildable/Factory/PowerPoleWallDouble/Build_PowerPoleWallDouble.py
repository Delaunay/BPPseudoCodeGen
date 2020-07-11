
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.PowerPoleWallDouble.Build_PowerPoleWallDouble import ExecuteUbergraph_Build_PowerPoleWallDouble
from Script.FactoryGame import FGBuildable
from Script.FactoryGame import AddHiddenConnection

class Build_PowerPoleWallDouble(FGBuildable):
    mHologramClass = NewObject[FGWallAttachmentHologram]()
    mDisplayName = NSLOCTEXT("", "3CBDE809445D273AADB1188105F8A8FF", "Double Wall Outlet Mk.1")
    mDescription = NSLOCTEXT("", "A27D86D648474EA536D633936F7F0DD9", "Power Pole that attaches to a wall. Has one connector on each side of the wall.\r\n\r\nCan handle up to 4 Power Line connections.\r\n\r\nConnect Power Poles, Power Generators and factory buildings together with Power Lines to create a power grid. The power grid supplies the connected buildings with power.")
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
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Build_PowerPoleWallDouble(10)
    

    def ExecuteUbergraph_Build_PowerPoleWallDouble(self):
        self.PowerConnection1.AddHiddenConnection(self.PowerConnection2)
    
