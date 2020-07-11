
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.PowerPoleMk1.Build_PowerPoleMk1 import Build_PowerPoleMk1

class Build_PowerPoleMk2(Build_PowerPoleMk1):
    mPowerConnection = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGPowerConnectionComponent', ObjectFlags=2883617, ObjectName='PowerConnection', RelativeLocation={'X': 0, 'Y': 0, 'Z': 700}, bReplicates=True, mMaxNumConnectionLinks=7)
    mMeshComponentProxy = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGColoredInstanceMeshProxy', ObjectFlags=2883617, ObjectName='PoleMeshProxy', RelativeLocation={'X': 0, 'Y': 0, 'Z': -50}, StaticMesh={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/PowerPoleMk2/Mesh/SM_PowerPole_Mk2.SM_PowerPole_Mk2'}, bAllowCullDistanceVolume=False, bGenerateOverlapEvents=False)
    mDisplayName = NSLOCTEXT("", "8D154A7C45052D3E056D428A9025AE9C", "Power Pole Mk.2")
    mDescription = NSLOCTEXT("", "E00477464DE62C65E637EEA4A93202DB", "Can handle up to 7 Power Line connections.\r\n\r\nConnect Power Poles, Power Generators and factory buildings together with Power Lines to create a power grid. The power grid supplies the connected buildings with power.")
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
    
