
from codegen.ue4_stub import *

from Script.Engine import ReceiveDestroyed
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.World.Environment.Rock.GasPillar.Mesh.BP_GasPillar import ExecuteUbergraph_BP_GasPillar
from Script.CoreUObject import Vector
from Script.AkAudio import PostAkEventAtLocation
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.WorldDestruction.Play_Nobelisk_WorldDestruction_Gaspillar import Play_Nobelisk_WorldDestruction_Gaspillar
from Script.FactoryGame import FGGasPillar

class BP_GasPillar(FGGasPillar):
    mMesh = Namespace(Mobility=0, ObjectClass='/Script/Engine.StaticMeshComponent', ObjectFlags=2883617, ObjectName='Mesh')
    mOverlapCollision = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', AttachParent={'$ObjectClass': '/Script/Engine.StaticMeshComponent', '$ObjectFlags': 2883617, '$ObjectName': 'Mesh', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='OverlapBox', SphereRadius=2000)
    mDotComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SphereComponent', '$ObjectFlags': 2883617, '$ObjectName': 'OverlapBox', 'SphereRadius': 2000, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'AttachParent': {'$ObjectClass': '/Script/Engine.StaticMeshComponent', '$ObjectFlags': 2883617, '$ObjectName': 'Mesh', 'Mobility': 0}, 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGDotComponent', ObjectFlags=2883617, ObjectName='DotComponent', mDotClass='/Game/FactoryGame/World/Hazard/GasCloud/BP_DoTGasCloud.BP_DoTGasCloud_C')
    mPostProcessSettings = NewObject[BP_GasPostProcess_Fields]()
    mSignificanceRange = 15000
    bReplicates = True
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.StaticMeshComponent', ObjectFlags=2883617, ObjectName='Mesh')
    
    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_BP_GasPillar(141)
    

    def ExecuteUbergraph_BP_GasPillar(self):
        # Label 10
        self.ReceiveDestroyed()
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_Nobelisk_WorldDestruction_Gaspillar, ReturnValue, Rotator::FromPitchYawRoll(0, 0, 0))
        # End
        goto('L10')
    
