
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildablePole
from Script.AkAudio import PostAkEvent
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.Factory.ConveyorPole.Build_ConveyorPole import ExecuteUbergraph_Build_ConveyorPole
from Game.FactoryGame.Buildable.Factory.ConveyorBeltMk1.Audio.Play_F_Construction_ConveyorBelt import Play_F_Construction_ConveyorBelt

class Build_ConveyorPole(FGBuildablePole):
    mHeight = 100
    mPoleComponentProxy = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, ComponentTags=['PoleMesh'], Mobility=0, ObjectClass='/Script/FactoryGame.FGColoredInstanceMeshProxy', ObjectFlags=2883617, ObjectName='PoleComponentProxy', bGenerateOverlapEvents=False, mCanBecolored=False)
    mSnapOnly0 = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, ComponentTags=['PoleHeight'], Mobility=0, ObjectClass='/Script/FactoryGame.FGFactoryConnectionComponent', ObjectFlags=2883617, ObjectName='SnapOnly0', mConnectorClearance=0, mDirection='EFactoryConnectionDirection::FCD_SNAP_ONLY')
    mStackHeight = 200
    mHologramClass = NewObject[FGConveyorPoleHologram]()
    mDisplayName = NSLOCTEXT("", "E75693834797F592505B699477FFC63F", "Conveyor Pole")
    mDescription = NSLOCTEXT("", "2A327C484684DE06BD78FD9C1C764E8A", "Can be used as a connection for conveyor belts. The height of the pole can be adjusted.\r\nUseful to route conveyor belts in a more controlled manner and over long distances.")
    MaxRenderDistance = -1
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
    
    def PlayConstructSound(self):
        self.ExecuteUbergraph_Build_ConveyorPole(10)
    

    def ExecuteUbergraph_Build_ConveyorPole(self):
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_F_Construction_ConveyorBelt, self, True)
    
