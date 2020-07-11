
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.PowerPoleMk1.Audio.Stop_F_PowerPole_Hum import Stop_F_PowerPole_Hum
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGBuildablePowerPole
from Game.FactoryGame.Buildable.Factory.PowerPoleMk1.Build_PowerPoleMk1 import ExecuteUbergraph_Build_PowerPoleMk1.K2Node_Event_newHasPower
from Game.FactoryGame.Buildable.-Shared.Audio.Play_F_PowerPole_Placement import Play_F_PowerPole_Placement
from Game.FactoryGame.Buildable.Factory.-Shared.Widget_PoleConnections import Widget_PoleConnections
from Game.FactoryGame.Buildable.Factory.PowerPoleMk1.Build_PowerPoleMk1 import ExecuteUbergraph_Build_PowerPoleMk1
from Game.FactoryGame.Buildable.Factory.PowerPoleMk1.Audio.Play_F_PowerPole_Hum import Play_F_PowerPole_Hum
from Script.UMG import GetUserWidgetObject
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import ReceiveBeginPlay
from Script.AkAudio import PostAkEventAttached
from Script.UMG import UserWidget

class Build_PowerPoleMk1(FGBuildablePowerPole):
    mConnectionWidgetClass = NewObject[Widget_PoleConnections]()
    mPowerConnection = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGPowerConnectionComponent', ObjectFlags=2883617, ObjectName='PowerConnection', RelativeLocation={'X': 0, 'Y': 0, 'Z': 600}, bReplicates=True, mMaxNumConnectionLinks=4)
    mMeshComponentProxy = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGColoredInstanceMeshProxy', ObjectFlags=2883617, ObjectName='PoleMeshProxy', RelativeLocation={'X': 0, 'Y': 0, 'Z': -50}, StaticMesh={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/PowerPoleMk1/Mesh/SM_PowerPole_Mk1.SM_PowerPole_Mk1'}, bAllowCullDistanceVolume=False, bGenerateOverlapEvents=False)
    mHologramClass = NewObject[FGPowerPoleHologram]()
    mDisplayName = NSLOCTEXT("", "DBBE58F04420F8612C67EFBCF1071637", "Power Pole Mk.1")
    mDescription = NSLOCTEXT("", "835E88C742E5553D22FBE98E33EDA65C", "Can handle up to 4 Power Line connections.\r\n\r\nConnect Power Poles, Power Generators and factory buildings together with Power Lines to create a power grid. The power grid supplies the connected buildings with power.")
    MaxRenderDistance = -1
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_PowerPole]()
    mIsUseable = True
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def OnHasPowerChanged_1(self, newHasPower: bool):
        ExecuteUbergraph_Build_PowerPoleMk1.K2Node_Event_newHasPower = newHasPower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_PowerPoleMk1(227)
    

    def PlayConstructSound(self):
        self.ExecuteUbergraph_Build_PowerPoleMk1(383)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Build_PowerPoleMk1(388)
    

    def OnShowConnectionFeedback(self):
        self.ExecuteUbergraph_Build_PowerPoleMk1(403)
    

    def ExecuteUbergraph_Build_PowerPoleMk1(self):
        # Label 10
        ReturnValue: Ptr[UserWidget] = self.mConnectionsWidgetComponent.GetUserWidgetObject()
        Connections: Ptr[Widget_PoleConnections] = Cast[Widget_PoleConnections](ReturnValue)
        bSuccess: bool = Connections
        if not bSuccess:
            goto('L408')
        Connections.PowerPoleDataModel = self
        # End
        # Label 169
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_F_PowerPole_Placement, self, True)
        # End
        if not newHasPower:
            goto('L312')
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_PowerPole_Hum, None, "PowerPoleAudioSocket_01", True)
        # End
        # Label 312
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_PowerPole_Hum, None, "PowerPoleAudioSocket_01", True)
        # End
        goto('L169')
        self.ReceiveBeginPlay()
        # End
        goto('L10')
    
