
from codegen.ue4_stub import *

from Script.FactoryGame import GetLength
from Script.FactoryGame import FGBuildableWire
from Script.Engine import SetVectorParameterValueOnMaterials
from Script.Engine import SetScalarParameterValueOnMaterials
from Script.Engine import ReceiveBeginPlay
from Script.Engine import GetLocalBounds
from Game.FactoryGame.Buildable.Factory.PowerLine.Build_PowerLine import ExecuteUbergraph_Build_PowerLine

class Build_PowerLine(FGBuildableWire):
    mMaxLength = 10000
    mLengthPerCost = 2500
    mWireMesh = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, BodyInstance={'ObjectType': 0, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'WireMesh', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WorldStatic', 'Response': 0}, {'Channel': 'WorldDynamic', 'Response': 0}, {'Channel': 'Pawn', 'Response': 0}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Camera', 'Response': 0}, {'Channel': 'PhysicsBody', 'Response': 0}, {'Channel': 'Vehicle', 'Response': 0}, {'Channel': 'Destructible', 'Response': 0}, {'Channel': 'Projectile', 'Response': 0}, {'Channel': 'Resource', 'Response': 0}, {'Channel': 'BuildGun', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CachedMaxDrawDistance=25000, CanCharacterStepUpOn=0, ComponentTags=['WireMesh'], LDMaxDrawDistance=25000, Mobility=0, ObjectClass='/Script/Engine.StaticMeshComponent', ObjectFlags=2883617, ObjectName='MainMesh', StaticMesh={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/PowerLine/Mesh/PowerLine_static.PowerLine_static'}, bCanEverAffectNavigation=False, bGenerateOverlapEvents=False, bUseAsOccluder=False)
    mHologramClass = NewObject[Holo_PowerLine]()
    mDisplayName = NSLOCTEXT("", "BA845DBE4BECEE99988C898F06411E41", "Power Line")
    mDescription = NSLOCTEXT("", "CDDF35C24A1D116A8CC4D2BF3F8B5986", "Used to connect Power Poles, Power Generators and Factory buildings.")
    MaxRenderDistance = 1000
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=False, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_WireBuild.BP_MaterialEffect_WireBuild_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 650000000
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Build_PowerLine(10)
    

    def ExecuteUbergraph_Build_PowerLine(self):
        self.ReceiveBeginPlay()
        self.mWireMesh.SetVectorParameterValueOnMaterials("Disp_Direction", Vector(0, 0, -48))
        ReturnValue: float = self.GetLength()
        
        Min = None
        Max = None
        self.mWireMesh.GetLocalBounds(Ref[Min], Ref[Max])
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(Max)
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(Min)
        ReturnValue_0: float = X1 - X
        ReturnValue_1: float = ReturnValue / ReturnValue_0
        self.mWireMesh.SetScalarParameterValueOnMaterials("UV_Tile", ReturnValue_1)
    
