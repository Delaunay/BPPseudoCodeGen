
from codegen.ue4_stub import *

from Script.FactoryGame import FGProductionIndicatorInstanceComponent

class BP_ProductionIndicatorInstanced(FGProductionIndicatorInstanceComponent):
    StaticMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/-Shared/ProductionIndicator/Mesh/SM_ProductionLight_01.SM_ProductionLight_01')
    BodyInstance = Namespace(AngularDamping=0, COMNudge={'X': 0, 'Y': 0, 'Z': 0}, CollisionEnabled=3, CollisionProfileName='BlockAll', CollisionResponses={'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'VehicleWheelQuery', 'Response': 2}]}, CustomDOFPlaneNormal={'X': 0, 'Y': 0, 'Z': 0}, CustomSleepThresholdMultiplier=1, DOFMode=0, InertiaTensorScale={'X': 1, 'Y': 1, 'Z': 1}, LinearDamping=0.009999999776482582, MassInKgOverride=100, MassScale=1, MaxAngularVelocity=3600, MaxDepenetrationVelocity=0, ObjectType=0, PhysMaterialOverride={'$Empty': True}, PhysicsBlendWeight=0, PositionSolverIterationCount=8, SleepFamily='ESleepFamily::Normal', StabilizationThresholdMultiplier=1, VelocitySolverIterationCount=1, WalkableSlopeOverride={'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, bAutoWeld=True, bEnableGravity=True, bGenerateWakeEvents=False, bInterpolateWhenSubStepping=True, bLockRotation=True, bLockTranslation=True, bLockXRotation=False, bLockXTranslation=False, bLockYRotation=False, bLockYTranslation=False, bLockZRotation=False, bLockZTranslation=False, bNotifyRigidBodyCollision=False, bOverrideMass=False, bOverrideMaxAngularVelocity=False, bOverrideMaxDepenetrationVelocity=False, bOverrideWalkableSlopeOnInstance=False, bSimulatePhysics=False, bStartAwake=True, bUpdateMassWhenScaleChanges=False, bUseCCD=False)
    PrimaryComponentTick = Namespace(EndTickGroup=0, TickGroup=2, TickInterval=0, bAllowTickOnDedicatedServer=False, bCanEverTick=False, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    
