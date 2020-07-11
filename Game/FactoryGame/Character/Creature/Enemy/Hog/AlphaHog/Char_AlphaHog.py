
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.Enemy.Stinger.Particle.LeapAttackImpact import LeapAttackImpact
from Game.FactoryGame.Character.Creature.Enemy.Hog.AlphaHog.Char_AlphaHog import ExecuteUbergraph_Char_AlphaHog.K2Node_ComponentBoundEvent_OverlappedComponent
from Script.Engine import ParticleSystemComponent
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.Character.Creature.Enemy.Hog.AlphaHog.Char_AlphaHog import ExecuteUbergraph_Char_AlphaHog.K2Node_ComponentBoundEvent_OtherBodyIndex
from Script.Engine import Default__GameplayStatics
from Script.CoreUObject import Vector
from Script.Engine import Normal
from Game.FactoryGame.Character.Creature.Enemy.Hog.AlphaHog.Char_AlphaHog import ExecuteUbergraph_Char_AlphaHog.K2Node_ComponentBoundEvent_OtherComp
from Game.FactoryGame.Character.Creature.Enemy.Hog.AlphaHog.Char_AlphaHog import ExecuteUbergraph_Char_AlphaHog.K2Node_ComponentBoundEvent_bFromSweep
from Script.Engine import SpawnEmitterAtLocation
from Game.FactoryGame.Character.Creature.Enemy.Hog.AlphaHog.Char_AlphaHog import ExecuteUbergraph_Char_AlphaHog.K2Node_ComponentBoundEvent_OtherActor
from Game.FactoryGame.Character.Creature.Enemy.Hog.AlphaHog.Char_AlphaHog import ExecuteUbergraph_Char_AlphaHog.K2Node_ComponentBoundEvent_SweepResult
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import Char_Hog
from Script.Engine import Character
from Game.FactoryGame.Character.Creature.Enemy.Hog.AlphaHog.Char_AlphaHog import ExecuteUbergraph_Char_AlphaHog

class Char_AlphaHog(Char_Hog):
    ThreatenedTarget: FName = NearbyThreat
    mChargeDamage = 20
    mIsAlpha = True
    mNavigationGenerationRadius = 7000
    mNavigationRemovalRadius = 8000
    mIsEnabled = 2
    mItemToDrop = NewObject[BP_AlphaHogParts]()
    mShouldOptimizeMeshWhenVisible = True
    mActualAIControllerClass = NewObject[Controller_AlphaHog]()
    mCanSpawnDuringDay = True
    mCanSpawnDuringNight = True
    mRotationSpeedMultiplier = 0.30000001192092896
    mEyeLocationComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 125, 'CapsuleRadius': 125, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 135.6358184814453, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='EyeLocationComponent')
    mSpawnWeight = 1
    mNeedsSpawner = True
    mSpawnDistance = -1
    mMaxFootstepParticleSpawnDistance = 2500
    mMaxFootstepDecalSpawnDistance = 1250
    mFootstepDecalSize = [{'X': -20, 'Y': -20, 'Z': -20}, {'X': 20, 'Y': 20, 'Z': 20}]
    mFootstepDecalLifetime = 10
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True, mCurrentHealth=80, mMaxHealth=80, mOnAdjustDamage=[0], mReplicateDamageEvents=True, mReplicateDeathEvents=True)
    mMaxDeathStayTime = 60
    mDeathRemoveCheckTime = 5
    mEnemyTargetDesirability = 1
    mMinVehiclePushVelocityForRagdoll = 400
    mTimeToGetUpFromRagdoll = 3
    mMaxDistanceMovedToGetUp = 9
    mRagdollMeshLocBoneName = Pelvis
    mRagdollMeshPhysicsBoneName = Pelvis
    mSyncBodyMaxDistance = 6
    mNormalDamageMultiplier = 1
    Mesh = Namespace(AnimClass='/Game/FactoryGame/Character/Creature/Enemy/Hog/Anim_Hog.Anim_Hog_C', AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 125, 'CapsuleRadius': 125, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 135.6358184814453, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, BodyInstance={'ObjectType': 2, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'CharacterMesh', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Pawn', 'Response': 0}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Vehicle', 'Response': 0}, {'Channel': 'WeaponInstantHit', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 121.313232421875, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CachedMaxDrawDistance=15000, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='CharacterMesh0', RelativeLocation={'X': -57.40557861328125, 'Y': 0, 'Z': -125}, RelativeRotation={'Pitch': 0, 'Yaw': -90, 'Roll': 0}, SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Hog/Mesh/HogAlpha_skl.HogAlpha_skl'}, VisibilityBasedAnimTickOption='EVisibilityBasedAnimTickOption::AlwaysTickPose', bReceivesDecals=False)
    CharacterMovement = Namespace(BrakingFriction=1, Mass=400, MaxAcceleration=8096, MaxStepHeight=100, MaxWalkSpeed=100, NavAgentProps={'AgentRadius': 42, 'AgentHeight': 192, 'AgentStepHeight': 100, 'NavWalkingSearchHeightScale': 1, 'PreferredNavData': {'AssetPathName': 'None', 'SubPathString': ''}, 'bCanCrouch': False, 'bCanJump': True, 'bCanWalk': True, 'bCanSwim': True, 'bCanFly': False}, NavMeshProjectionInterval=0.30000001192092896, ObjectClass='/Script/Engine.CharacterMovementComponent', ObjectFlags=2883617, ObjectName='CharMoveComp', WalkableFloorAngle=50, WalkableFloorZ=0.6427876353263855, bProjectNavMeshWalking=True, bUseAccelerationForPaths=True, bUseControllerDesiredRotation=True)
    CapsuleComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 135.6358184814453, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=125, CapsuleRadius=125, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 135.6358184814453, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=125, CapsuleRadius=125, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    
    def BndEvt__Sphere_K2Node_ComponentBoundEvent_0_ComponentBeginOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32, bFromSweep: bool, SweepResult: Const[Ref[HitResult]]):
        ExecuteUbergraph_Char_AlphaHog.K2Node_ComponentBoundEvent_OverlappedComponent = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_AlphaHog.K2Node_ComponentBoundEvent_OtherActor = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_AlphaHog.K2Node_ComponentBoundEvent_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_AlphaHog.K2Node_ComponentBoundEvent_OtherBodyIndex = OtherBodyIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_AlphaHog.K2Node_ComponentBoundEvent_bFromSweep = bFromSweep #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_AlphaHog.K2Node_ComponentBoundEvent_SweepResult = SweepResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_AlphaHog(10)
    

    def ExecuteUbergraph_Char_AlphaHog(self):
        if not self.mIsCharging:
            goto('L456')
        AsCharacter: Ptr[Character] = Cast[Character](OtherActor)
        bSuccess: bool = AsCharacter
        if not bSuccess:
            goto('L456')
        ReturnValue: Vector = self.GetVelocity()
        ReturnValue_0: Vector = Normal(ReturnValue, 9.999999747378752e-05)
        ReturnValue_1: Vector = ReturnValue_0 * 1200
        ReturnValue_2: Vector = ReturnValue_1 + Vector(0, 0, 500)
        AsCharacter.LaunchCharacter(ReturnValue_2, False, False)
        ReturnValue_3: Vector = AsCharacter.K2_GetActorLocation()
        ReturnValue_4: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, LeapAttackImpact, ReturnValue_3, Rotator::FromPitchYawRoll(0, 0, 0), Vector(0.5, 0.5, 0.5), True, 0)
    
