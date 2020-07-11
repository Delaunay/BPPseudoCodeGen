
from codegen.ue4_stub import *

from Game.FactoryGame.World.Environment.Rock.GasPillar.Mesh.BP_GasPillar import BP_GasPillar

class BP_GasPillar_03(BP_GasPillar):
    mMesh = Namespace(Mobility=0, ObjectClass='/Script/Engine.StaticMeshComponent', ObjectFlags=2883617, ObjectName='Mesh', StaticMesh={'$AssetPath': '/Game/FactoryGame/World/Environment/Rock/GasPillar/Mesh/GasPillar_03.GasPillar_03'})
    mOverlapCollision = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', AttachParent={'$ObjectClass': '/Script/Engine.StaticMeshComponent', '$ObjectFlags': 2883617, '$ObjectName': 'Mesh', 'StaticMesh': {'$AssetPath': '/Game/FactoryGame/World/Environment/Rock/GasPillar/Mesh/GasPillar_03.GasPillar_03'}, 'Mobility': 0}, Mobility=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='OverlapBox', SphereRadius=2000)
    mDotComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SphereComponent', '$ObjectFlags': 2883617, '$ObjectName': 'OverlapBox', 'SphereRadius': 2000, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'AttachParent': {'$ObjectClass': '/Script/Engine.StaticMeshComponent', '$ObjectFlags': 2883617, '$ObjectName': 'Mesh', 'StaticMesh': {'$AssetPath': '/Game/FactoryGame/World/Environment/Rock/GasPillar/Mesh/GasPillar_03.GasPillar_03'}, 'Mobility': 0}, 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGDotComponent', ObjectFlags=2883617, ObjectName='DotComponent', mDotClass='/Game/FactoryGame/World/Hazard/GasCloud/BP_DoTGasCloud.BP_DoTGasCloud_C')
    mSignificanceRange = 15000
    bReplicates = True
    RemoteRole = 1
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.StaticMeshComponent', ObjectFlags=2883617, ObjectName='Mesh', StaticMesh={'$AssetPath': '/Game/FactoryGame/World/Environment/Rock/GasPillar/Mesh/GasPillar_03.GasPillar_03'})
    
