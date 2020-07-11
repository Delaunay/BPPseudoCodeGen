
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_Event_EndPlayReason
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_Event_bSelfMoved
from Script.Engine import SpawnEmitterAtLocation
from Script.AkAudio import PostAkEventAtLocation
from Script.CoreUObject import Rotator
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_CustomEvent_damageType
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab
from Script.Engine import GetPhysicsLinearVelocity
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_Event_Other
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_ComponentBoundEvent_bFromSweep
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_ComponentBoundEvent_SweepResult
from Game.FactoryGame.Character.Creature.Enemy.Crab.Particle.BabyCrabTakeDmg_01 import BabyCrabTakeDmg_01
from Script.Engine import Normal
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_Event_HitLocation
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_Event_OtherComp
from Script.Engine import NegateVector
from Script.FactoryGame import FGCreatureSpawner
from Script.Engine import Cross_VectorVector
from Script.FactoryGame import ReceiveDied
from Script.Engine import Conv_RotatorToVector
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import GetActorForwardVector
from Game.FactoryGame.Character.Creature.Enemy.CrabHatcher.Audio.Play_E_Hatchery_Baby import Play_E_Hatchery_Baby
from Script.Engine import FClamp
from Script.Engine import Controller
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_Event_Hit
from Script.Engine import VSize
from Script.Engine import FMin
from Script.FactoryGame import GetCurrentAggroTarget
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_ComponentBoundEvent_OverlappedComponent
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_CustomEvent_Damage
from Script.FactoryGame import GetSpawner
from Script.Engine import K2_GetComponentLocation
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_Event_MyComp
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_ComponentBoundEvent_OtherBodyIndex
from Script.AkAudio import AkComponent
from Game.FactoryGame.Character.Creature.Enemy.Crab.Particle.ProjectileExplosion_01 import ProjectileExplosion_01
from Script.Engine import SkeletalMeshComponent
from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_ComponentBoundEvent_OtherActor
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_Event_HitNormal
from Script.Engine import LatentActionInfo
from Script.Engine import FindLookAtRotation
from Script.Engine import HasAuthority
from Script.Engine import GetController
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_Event_NormalImpulse
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_ComponentBoundEvent_OtherComp
from Game.FactoryGame.Character.Creature.Enemy.Hog.DamageType_HogHit import DamageType_HogHit
from Script.Engine import CurveFloat
from Script.Engine import Dot_VectorVector
from Script.Engine import Default__GameplayStatics
from Script.Engine import K2_SetActorRotation
from Script.Engine import Subtract_VectorVector
from Script.Engine import K2_GetActorRotation
from Script.Engine import ApplyDamage
from Script.Engine import RandomIntegerInRange
from Script.Engine import Multiply_VectorVector
from Game.FactoryGame.Character.Creature.Enemy.CrabHatcher.Audio.Play_E_Hatchery_Baby_Suicide import Play_E_Hatchery_Baby_Suicide
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_Event_DeltaSeconds
from Script.Engine import Divide_VectorFloat
from Script.FactoryGame import IsAliveAndWell
from Script.Engine import RandomFloatInRange
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_CustomEvent_damagedActor
from Script.Engine import ReceiveBeginPlay
from Script.Engine import Not_PreBool
from Script.Engine import ReceiveTick
from Script.Engine import GetWorldDeltaSeconds
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_CustomEvent_damageCauser
from Script.Engine import BooleanOR
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import ExecuteUbergraph_Char_BabyCrab.K2Node_CustomEvent_instigatedBy
from Script.CoreUObject import Vector
from Script.FactoryGame import FGEnemy
from Script.Engine import RInterpTo
from Script.Engine import ParticleSystemComponent
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation

class Char_BabyCrab(FGEnemy):
    Rotation_Curve: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Hog/Curve_DistanceAggroHog.Curve_DistanceAggroHog')
    mRotationRate: float
    mRotationScale: float = 1
    mCanMove: bool = True
    mRandomUp: float = 50
    mCanAttack: bool
    mStrategyType: int32
    mTargetMoveDir: Vector
    mTargetDistance: float
    mTargetOffsetTargetPos: Vector
    mReEvalTimer: float
    mSubtitlesVisible: bool
    mSubtitleDistance: float = 3000
    mSubtitleTimer: TimerHandle
    mNavigationGenerationRadius = 7000
    mNavigationRemovalRadius = 8000
    mIsEnabled = 2
    mShouldOptimizeMeshWhenVisible = True
    mActualAIControllerClass = NewObject[Controller_BabyCrab]()
    mCanSpawnDuringDay = True
    mCanSpawnDuringNight = True
    mRotationSpeedMultiplier = 0.30000001192092896
    mEyeLocationComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 50, 'CapsuleRadius': 50, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}, {'Channel': 'Pawn', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 135.6358184814453, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='EyeLocationComponent')
    mSpawnWeight = 0.10000000149011612
    mNeedsSpawner = True
    mSpawnDistance = -1
    mFeetNames = ['vfxfootsocket_front_l', 'vfxfootsocket_front_r', 'vfxfootsocket_back_l', 'vfxfootsocket_back_r']
    mFootstepEffect = [{'Surface': 0, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 1, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 2, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 3, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 4, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 5, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 6, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}]
    mFootstepAudioEvents = [{'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/_Shared/Audio/Play_E_Hog_Footstep_Switch.Play_E_Hog_Footstep_Switch'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/_Shared/Audio/Play_E_Hog_Footstep_Switch.Play_E_Hog_Footstep_Switch'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/_Shared/Audio/Play_E_Hog_Footstep_Switch.Play_E_Hog_Footstep_Switch'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/_Shared/Audio/Play_E_Hog_Footstep_Switch.Play_E_Hog_Footstep_Switch'}]
    mMaxFootstepParticleSpawnDistance = 2500
    mMaxFootstepDecalSpawnDistance = 1250
    mFootstepDecalSize = [{'X': -20, 'Y': -20, 'Z': -20}, {'X': 20, 'Y': 20, 'Z': 20}]
    mFootstepDecalLifetime = 10
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True, mCurrentHealth=6, mMaxHealth=6, mOnAdjustDamage=[0], mReplicateDamageEvents=True, mReplicateDeathEvents=True)
    mFallDamageDamageType = NewObject[DamageType_FallDamage]()
    mMaxDeathStayTime = 60
    mDeathRemoveCheckTime = 5
    mEnemyTargetDesirability = 1
    mTakeDamageSound = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/CrabHatcher/Audio/Play_E_Hatchery_Baby_Suicide.Play_E_Hatchery_Baby_Suicide')
    mDeathSound = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/CrabHatcher/Audio/Play_E_Hatchery_Baby_Suicide.Play_E_Hatchery_Baby_Suicide')
    mMinVehiclePushVelocityForRagdoll = 400
    mTimeToGetUpFromRagdoll = 3
    mMaxDistanceMovedToGetUp = 9
    mRagdollMeshLocBoneName = Pelvis
    mRagdollMeshPhysicsBoneName = Pelvis
    mSyncBodyMaxDistance = 6
    mApplyDamageMomentum = True
    mWeakspotMultiplier = 2
    mNormalDamageMultiplier = 1
    Mesh = Namespace(AnimationMode=1, AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 50, 'CapsuleRadius': 50, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}, {'Channel': 'Pawn', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 135.6358184814453, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, BodyInstance={'ObjectType': 2, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Pawn', 'Response': 0}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Vehicle', 'Response': 0}, {'Channel': 'WorldStatic', 'Response': 0}, {'Channel': 'WorldDynamic', 'Response': 0}, {'Channel': 'Camera', 'Response': 0}, {'Channel': 'PhysicsBody', 'Response': 0}, {'Channel': 'Destructible', 'Response': 0}, {'Channel': 'Projectile', 'Response': 0}, {'Channel': 'Resource', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 121.313232421875, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CachedMaxDrawDistance=15000, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='CharacterMesh0', RelativeRotation={'Pitch': 0, 'Yaw': -90, 'Roll': 0}, RelativeScale3D={'X': 0.5, 'Y': 0.5, 'Z': 0.5}, SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Hog/Mesh/Hog.Hog'}, VisibilityBasedAnimTickOption='EVisibilityBasedAnimTickOption::AlwaysTickPose', bHiddenInGame=True, bVisible=False)
    CharacterMovement = Namespace(BrakingDecelerationFlying=8000, BrakingFriction=1, DefaultLandMovementMode=5, MaxAcceleration=8000, MaxFlySpeed=1000, MaxStepHeight=100, MaxWalkSpeed=400, NavAgentProps={'AgentRadius': 42, 'AgentHeight': 192, 'AgentStepHeight': 100, 'NavWalkingSearchHeightScale': 1, 'PreferredNavData': {'AssetPathName': 'None', 'SubPathString': ''}, 'bCanCrouch': False, 'bCanJump': True, 'bCanWalk': True, 'bCanSwim': True, 'bCanFly': True}, NavMeshProjectionInterval=0.30000001192092896, ObjectClass='/Script/Engine.CharacterMovementComponent', ObjectFlags=2883617, ObjectName='CharMoveComp', WalkableFloorZ=0.7100000381469727, bProjectNavMeshWalking=True, bUseAccelerationForPaths=True, bUseControllerDesiredRotation=True)
    CapsuleComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}, {'Channel': 'Pawn', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 135.6358184814453, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=50, CapsuleRadius=50, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    AutoPossessAI = EAutoPossessAI::PlacedInWorldOrSpawned
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}, {'Channel': 'Pawn', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 135.6358184814453, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=50, CapsuleRadius=50, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    
    def ReceiveHit(self):
        ExecuteUbergraph_Char_BabyCrab.K2Node_Event_MyComp = MyComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_BabyCrab.K2Node_Event_Other = Other #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_BabyCrab.K2Node_Event_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_BabyCrab.K2Node_Event_bSelfMoved = bSelfMoved #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_BabyCrab.K2Node_Event_HitLocation = HitLocation #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_BabyCrab.K2Node_Event_HitNormal = HitNormal #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_BabyCrab.K2Node_Event_NormalImpulse = NormalImpulse #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_BabyCrab.K2Node_Event_Hit = Hit #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_BabyCrab(3715)
    

    def Got Damaged(self, DamagedActor: Ptr[Actor], Damage: float, DamageType: Const[Ptr[DamageType]], InstigatedBy: Ptr[Controller], DamageCauser: Ptr[Actor]):
        ExecuteUbergraph_Char_BabyCrab.K2Node_CustomEvent_damagedActor = DamagedActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_BabyCrab.K2Node_CustomEvent_Damage = Damage #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_BabyCrab.K2Node_CustomEvent_damageType = DamageType #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_BabyCrab.K2Node_CustomEvent_instigatedBy = InstigatedBy #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_BabyCrab.K2Node_CustomEvent_damageCauser = DamageCauser #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_BabyCrab(5253)
    

    def ResetMovement(self):
        self.ExecuteUbergraph_Char_BabyCrab(5534)
    

    def BndEvt__Sphere_K2Node_ComponentBoundEvent_0_ComponentBeginOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32, bFromSweep: bool, SweepResult: Const[Ref[HitResult]]):
        ExecuteUbergraph_Char_BabyCrab.K2Node_ComponentBoundEvent_OverlappedComponent = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_BabyCrab.K2Node_ComponentBoundEvent_OtherActor = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_BabyCrab.K2Node_ComponentBoundEvent_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_BabyCrab.K2Node_ComponentBoundEvent_OtherBodyIndex = OtherBodyIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_BabyCrab.K2Node_ComponentBoundEvent_bFromSweep = bFromSweep #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_BabyCrab.K2Node_ComponentBoundEvent_SweepResult = SweepResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_BabyCrab(5539)
    

    def KillOrphanCrabs(self):
        self.ExecuteUbergraph_Char_BabyCrab(6198)
    

    def Event Check Subtitle Distance(self):
        self.ExecuteUbergraph_Char_BabyCrab(6474)
    

    def ChargingMovement(self):
        self.ExecuteUbergraph_Char_BabyCrab(6475)
    

    def ReceiveTick(self):
        ExecuteUbergraph_Char_BabyCrab.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_BabyCrab(9937)
    

    def ReceiveDied(self):
        self.ExecuteUbergraph_Char_BabyCrab(9976)
    

    def ReceiveEndPlay(self):
        ExecuteUbergraph_Char_BabyCrab.K2Node_Event_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_BabyCrab(9981)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Char_BabyCrab(10024)
    

    def ExecuteUbergraph_Char_BabyCrab(self):
        goto(ComputedJump("EntryPoint"))
        self.mCanAttack = True
        self.CapsuleComponent.SetSimulatePhysics(False)
        goto(ExecutionFlow.Pop())
        self.mCanAttack = True
        self.CapsuleComponent.SetSimulatePhysics(False)
        goto(ExecutionFlow.Pop())
        ReturnValue: Vector = self.CapsuleComponent.GetPhysicsLinearVelocity("None")
        ReturnValue_0: Vector = Multiply_VectorVector(ReturnValue, Vector(1, 1, 0.10000000149011612))
        ReturnValue_1: Vector = Normal(ReturnValue_0, 9.999999747378752e-05)
        ReturnValue1: Vector = ReturnValue_1 * -600
        self.mTargetOffsetTargetPos = ReturnValue1
        self.mReEvalTimer = 2.4000000953674316
        ReturnValue11: float = RandomFloatInRange(459, 800)
        self.CharacterMovement.MaxFlySpeed = ReturnValue11
        self.mRotationRate = 30
        self.mTargetDistance = 500
        ReturnValue_2: Vector = ReturnValue * -1.3300000429153442
        ReturnValue7: float = RandomFloatInRange(-600, 600)
        ReturnValue8: float = RandomFloatInRange(-600, 600)
        ReturnValue9: float = RandomFloatInRange(100, 600)
        ReturnValue1_0: Vector = Vector(ReturnValue7, ReturnValue8, ReturnValue9)
        ReturnValue1_1: Vector = ReturnValue_2 + ReturnValue1_0
        self.CapsuleComponent.AddImpulse(ReturnValue1_1, "None", True)
        Default__KismetSystemLibrary.Delay(self, 1.7999999523162842, LatentActionInfo(Linkage = 15, UUID = 179724655, ExecutionFunction = "ExecuteUbergraph_Char_BabyCrab", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.CapsuleComponent.SetSimulatePhysics(False)
        self.mCanAttack = True
        goto(ExecutionFlow.Pop())
        self.CapsuleComponent.SetSimulatePhysics(True)
        Default__KismetSystemLibrary.Delay(self, 1, LatentActionInfo(Linkage = 886, UUID = 136485694, ExecutionFunction = "ExecuteUbergraph_Char_BabyCrab", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1049
        OutputDelegate.BindUFunction(self, Got Damaged)
        self.OnTakeAnyDamage.AddUnique(OutputDelegate)
        Default__KismetSystemLibrary.Delay(self, 0.5, LatentActionInfo(Linkage = 64, UUID = -1983139921, ExecutionFunction = "ExecuteUbergraph_Char_BabyCrab", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1168
        ReturnValue_3: bool = self.mReEvalTimer <= 0
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        self.ChargingMovement()
        goto(ExecutionFlow.Pop())
        # Label 1227
        self.mCanAttack = False
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 113, UUID = 1921766502, ExecutionFunction = "ExecuteUbergraph_Char_BabyCrab", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1315
        ReturnValue_4: bool = self.IsAliveAndWell()
        ReturnValue_5: bool = ReturnValue_4 and self.mCanAttack
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](Other)
        bSuccess: bool = Player
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue1_2: Ptr[Controller] = self.GetController()
        ReturnValue_6: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_2)
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        ReturnValue_7: Ptr[Controller] = self.GetController()
        ReturnValue_8: float = Default__GameplayStatics.ApplyDamage(Player, 5, ReturnValue_7, self, DamageType_HogHit)
        # Label 1642
        ReturnValue_9: Ptr[SkeletalMeshComponent] = self.GetMesh3P()
        ReturnValue_10: Vector = ReturnValue_9.K2_GetComponentLocation()
        ReturnValue_11: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, BabyCrabTakeDmg_01, ReturnValue_10, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        self.CapsuleComponent.SetSimulatePhysics(True)
        goto('L1227')
        # Label 1848
        self.mCanAttack = False
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 935, UUID = 1261590653, ExecutionFunction = "ExecuteUbergraph_Char_BabyCrab", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1936
        self.CapsuleComponent.SetSimulatePhysics(False)
        ReturnValue_12: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Hatchery_Baby, self, True)
        ReturnValue12: float = RandomFloatInRange(-1, 1)
        ReturnValue13: float = RandomFloatInRange(-1, 1)
        ReturnValue2: Vector = Vector(ReturnValue12, ReturnValue13, 0)
        ReturnValue1_3: Vector = Normal(ReturnValue2, 9.999999747378752e-05)
        self.mTargetMoveDir = ReturnValue1_3
        self.mTargetDistance = 500
        ExecutionFlow.Push("L2270")
        ExecutionFlow.Push("L1049")
        self.ResetMovement()
        goto(ExecutionFlow.Pop())
        # Label 2270
        self.Event Check Subtitle Distance()
        OutputDelegate2.BindUFunction(self, Event Check Subtitle Distance)
        ReturnValue1_4: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate2, 1, True)
        self.mSubtitleTimer = ReturnValue1_4
        goto(ExecutionFlow.Pop())
        # Label 2400
        if not self.mCanAttack:
            goto('L3657')
        ReturnValue1_5: Ptr[Actor] = self.GetCurrentAggroTarget()
        ReturnValue1_6: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_5)
        if not ReturnValue1_6:
           goto(ExecutionFlow.Pop())
        ReturnValue_13: Rotator = self.K2_GetActorRotation()
        ReturnValue2_0: Vector = self.Mesh.K2_GetComponentLocation()
        ReturnValue_14: float = Default__GameplayStatics.GetWorldDeltaSeconds(self)
        ReturnValue_15: Ptr[Actor] = self.GetCurrentAggroTarget()
        ReturnValue1_7: Vector = ReturnValue_15.K2_GetActorLocation()
        ReturnValue_16: Vector = ReturnValue1_7 + self.mTargetOffsetTargetPos
        
        ReturnValue_17: Rotator = FindLookAtRotation(Ref[ReturnValue2_0], Ref[ReturnValue_16])
        ReturnValue_18: float = self.mTargetDistance * self.mReEvalTimer
        ReturnValue_19: float = FClamp(ReturnValue_18, 0.029999999329447746, 1)
        ReturnValue1_8: float = ReturnValue_19 * self.mRotationRate
        ReturnValue_20: Rotator = RInterpTo(ReturnValue_13, ReturnValue_17, ReturnValue_14, ReturnValue1_8)
        ReturnValue_21: bool = self.K2_SetActorRotation(ReturnValue_20, False)
        ReturnValue_13 = self.K2_GetActorRotation()
        ReturnValue2_0 = self.Mesh.K2_GetComponentLocation()
        ReturnValue_14 = Default__GameplayStatics.GetWorldDeltaSeconds(self)
        ReturnValue_15 = self.GetCurrentAggroTarget()
        ReturnValue1_7 = ReturnValue_15.K2_GetActorLocation()
        ReturnValue_16 = ReturnValue1_7 + self.mTargetOffsetTargetPos
        
        ReturnValue_17 = FindLookAtRotation(Ref[ReturnValue2_0], Ref[ReturnValue_16])
        ReturnValue_18 = self.mTargetDistance * self.mReEvalTimer
        ReturnValue_19 = FClamp(ReturnValue_18, 0.029999999329447746, 1)
        ReturnValue1_8 = ReturnValue_19 * self.mRotationRate
        ReturnValue_20 = RInterpTo(ReturnValue_13, ReturnValue_17, ReturnValue_14, ReturnValue1_8)
        ReturnValue_22: Vector = Conv_RotatorToVector(ReturnValue_20)
        self.AddMovementInput(ReturnValue_22, 1, False)
        ReturnValue_23: float = self.mReEvalTimer - DeltaSeconds
        self.mReEvalTimer = ReturnValue_23
        goto('L1168')
        # Label 3657
        ReturnValue_24: Vector = self.GetActorForwardVector()
        self.AddMovementInput(ReturnValue_24, 1, False)
        goto(ExecutionFlow.Pop())
        goto('L1315')
        # Label 3720
        ReturnValue_25: int32 = RandomIntegerInRange(0, 2)
        self.mStrategyType = ReturnValue_25
        self.ReceiveBeginPlay()
        goto('L1936')
        # Label 3800
        ReturnValue1_9: float = RandomFloatInRange(0.4000000059604645, 9)
        Variable1: int32 = self.mStrategyType
        ReturnValue4: float = RandomFloatInRange(3, 12)
        
        switch = {
            0: ReturnValue1_9,
            1: ReturnValue4,
            2: ReturnValue4
        }
        self.mRotationRate = switch.get(Variable1, None)
        Variable: float = 1200
        ReturnValue_26: float = RandomFloatInRange(520, 1000)
        ReturnValue_27: bool = self.mTargetDistance > 900
        ReturnValue3: bool = self.mTargetDistance > 1400
        Variable2: bool = ReturnValue3
        Variable2_0: int32 = self.mStrategyType
        Variable1_0: float = 1430
        Variable10: bool = ReturnValue_27
        
        switch_0 = {
            False: ReturnValue_26,
            True: Variable
        }
        
        switch_1 = {
            False: ReturnValue_26,
            True: Variable1_0
        }
        
        switch_2 = {
            False: ReturnValue_26,
            True: Variable1_0
        }
        
        switch_3 = {
            0: switch_0.get(Variable2, None),
            1: switch_1.get(Variable10, None),
            2: switch_2.get(Variable10, None)
        }
        self.CharacterMovement.MaxFlySpeed = switch_3.get(Variable2_0, None)
        goto(ExecutionFlow.Pop())
        # Label 4469
        ReturnValue2_1: float = RandomFloatInRange(50, 364)
        ReturnValue1_10: bool = self.mTargetDistance > 300
        Variable_0: bool = ReturnValue1_10
        ReturnValue5: float = RandomFloatInRange(0, 54)
        
        switch_4 = {
            False: ReturnValue5,
            True: ReturnValue2_1
        }
        self.mRandomUp = switch_4.get(Variable_0, None)
        goto('L3800')
        # Label 4674
        ReturnValue3_0: float = RandomFloatInRange(0.05000000074505806, 0.4000000059604645)
        ReturnValue_28: bool = self.mTargetDistance <= 600
        Variable8: bool = ReturnValue_28
        ReturnValue6: float = RandomFloatInRange(1, 2)
        ReturnValue2_2: bool = self.mTargetDistance > 700
        Variable1_1: bool = ReturnValue2_2
        ReturnValue10: float = RandomFloatInRange(0.10000000149011612, 0.699999988079071)
        Variable3: int32 = self.mStrategyType
        
        switch_5 = {
            False: ReturnValue10,
            True: ReturnValue6
        }
        
        switch_6 = {
            False: ReturnValue10,
            True: ReturnValue6
        }
        
        switch_7 = {
            False: switch_6.get(Variable1_1, None),
            True: ReturnValue3_0
        }
        
        switch_8 = {
            False: ReturnValue10,
            True: ReturnValue6
        }
        
        switch_9 = {
            False: switch_8.get(Variable1_1, None),
            True: ReturnValue3_0
        }
        
        switch_10 = {
            0: switch_5.get(Variable1_1, None),
            1: switch_7.get(Variable8, None),
            2: switch_9.get(Variable8, None)
        }
        self.mReEvalTimer = switch_10.get(Variable3, None)
        self.ResetMovement()
        goto(ExecutionFlow.Pop())
        ReturnValue_29: Vector = damageCauser.K2_GetActorLocation()
        ReturnValue4_0: Vector = self.Mesh.K2_GetComponentLocation()
        ReturnValue1_11: Vector = Subtract_VectorVector(ReturnValue4_0, ReturnValue_29)
        ReturnValue2_3: Vector = Normal(ReturnValue1_11, 9.999999747378752e-05)
        ReturnValue10_0: Vector = ReturnValue2_3 * 2500
        self.CharacterMovement.AddImpulse(ReturnValue10_0, True)
        goto('L1848')
        goto('L4469')
        ReturnValue2_4: bool = self.IsAliveAndWell()
        ReturnValue2_5: bool = ReturnValue2_4 and self.mCanAttack
        if not ReturnValue2_5:
           goto(ExecutionFlow.Pop())
        Player1: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](OtherActor)
        bSuccess1: bool = Player1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue2_6: Ptr[Controller] = self.GetController()
        ReturnValue3_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue2_6)
        if not ReturnValue3_1:
           goto(ExecutionFlow.Pop())
        ReturnValue3_2: Ptr[Controller] = self.GetController()
        ReturnValue1_12: float = Default__GameplayStatics.ApplyDamage(Player1, 5, ReturnValue3_2, self, DamageType_HogHit)
        goto('L1642')
        # Label 5871
        ReturnValue1_13: Ptr[SkeletalMeshComponent] = self.GetMesh3P()
        ReturnValue3_3: Vector = ReturnValue1_13.K2_GetComponentLocation()
        ReturnValue_30: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_E_Hatchery_Baby_Suicide, ReturnValue3_3, Rotator::FromPitchYawRoll(0, 0, 0))
        ReturnValue1_13 = self.GetMesh3P()
        ReturnValue3_3 = ReturnValue1_13.K2_GetComponentLocation()
        ReturnValue1_14: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, ProjectileExplosion_01, ReturnValue3_3, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        self.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        ReturnValue_31: Ptr[FGCreatureSpawner] = self.GetSpawner()
        ReturnValue_32: bool = self.HasAuthority()
        ReturnValue2_7: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_31)
        ReturnValue_33: bool = Not_PreBool(ReturnValue2_7)
        ReturnValue1_15: bool = ReturnValue_33 and ReturnValue_32
        if not ReturnValue1_15:
           goto(ExecutionFlow.Pop())
        self.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        # Label 6381
        OutputDelegate1.BindUFunction(self, KillOrphanCrabs)
        ReturnValue_34: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate1, 30, False)
        goto('L3720')
        goto(ExecutionFlow.Pop())
        ReturnValue2_8: Ptr[Actor] = self.GetCurrentAggroTarget()
        ReturnValue4_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue2_8)
        if not ReturnValue4_1:
           goto(ExecutionFlow.Pop())
        ReturnValue1_16: Vector = self.Mesh.K2_GetComponentLocation()
        ReturnValue2_8 = self.GetCurrentAggroTarget()
        ReturnValue2_9: Vector = ReturnValue2_8.K2_GetActorLocation()
        ReturnValue_35: Vector = Subtract_VectorVector(ReturnValue2_9, ReturnValue1_16)
        ReturnValue_36: float = VSize(ReturnValue_35)
        ReturnValue3_4: bool = ReturnValue_36 <= 5000
        ReturnValue5_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue2_8)
        ReturnValue1_17: bool = self.IsAliveAndWell()
        ReturnValue3_5: bool = ReturnValue5_0 and self.mCanMove
        ReturnValue4_2: bool = ReturnValue3_5 and ReturnValue1_17
        ReturnValue5_1: bool = ReturnValue4_2 and ReturnValue3_4
        if not ReturnValue5_1:
           goto(ExecutionFlow.Pop())
        ReturnValue2_8 = self.GetCurrentAggroTarget()
        ReturnValue_37: Vector = ReturnValue2_8.GetVelocity()
        ReturnValue1_18: float = VSize(ReturnValue_37)
        ReturnValue4_3: bool = ReturnValue1_18 > 20
        if not ReturnValue4_3:
            goto('L7561')
        ReturnValue2_8 = self.GetCurrentAggroTarget()
        ReturnValue_37 = ReturnValue2_8.GetVelocity()
        ReturnValue1_18 = VSize(ReturnValue_37)
        ReturnValue1_19: Vector = Divide_VectorFloat(ReturnValue_37, ReturnValue1_18)
        self.mTargetMoveDir = ReturnValue1_19
        ReturnValue1_16 = self.Mesh.K2_GetComponentLocation()
        ReturnValue2_8 = self.GetCurrentAggroTarget()
        ReturnValue2_9 = ReturnValue2_8.K2_GetActorLocation()
        ReturnValue_35 = Subtract_VectorVector(ReturnValue2_9, ReturnValue1_16)
        ReturnValue_36 = VSize(ReturnValue_35)
        self.mTargetDistance = ReturnValue_36
        # Label 7561
        Variable_1: Vector = Vector(0, 0, 0)
        Variable1_2: Vector = Vector(0, 0, 0)
        Variable_2: int32 = self.mStrategyType
        ReturnValue1_16 = self.Mesh.K2_GetComponentLocation()
        ReturnValue_38: Vector = Cross_VectorVector(self.mTargetMoveDir, Vector(0, 0, 1))
        ReturnValue_39: Vector = NegateVector(ReturnValue_38)
        ReturnValue2_10: Vector = self.mTargetMoveDir * 150
        ReturnValue3_6: Vector = self.mTargetMoveDir * 400
        ReturnValue4_4: Vector = self.mTargetMoveDir * 150
        ReturnValue5_2: Vector = self.mTargetMoveDir * 400
        ReturnValue_40: Vector = Vector(0, 0, self.mRandomUp)
        ReturnValue2_8 = self.GetCurrentAggroTarget()
        ReturnValue2_9 = ReturnValue2_8.K2_GetActorLocation()
        ReturnValue_35 = Subtract_VectorVector(ReturnValue2_9, ReturnValue1_16)
        ReturnValue_37 = ReturnValue2_8.GetVelocity()
        ReturnValue_36 = VSize(ReturnValue_35)
        ReturnValue6_0: Vector = ReturnValue_37 * 3
        ReturnValue1_20: float = FClamp(ReturnValue_36, 450, 1700)
        ReturnValue1_21: bool = ReturnValue_36 <= 400
        ReturnValue2_11: float = ReturnValue1_20 * 0.4000000059604645
        ReturnValue2_12: bool = ReturnValue_36 <= 300
        ReturnValue7_0: Vector = self.mTargetMoveDir * ReturnValue2_11
        ReturnValue_41: float = FMin(ReturnValue_36, 800)
        ReturnValue_42: Vector = Divide_VectorFloat(ReturnValue_35, ReturnValue_36)
        ReturnValue1_18 = VSize(ReturnValue_37)
        ReturnValue_43: float = Dot_VectorVector(self.mTargetMoveDir, ReturnValue_42)
        ReturnValue4_5: bool = ReturnValue_43 <= 0
        Variable4: bool = ReturnValue4_5
        ReturnValue5_3: bool = ReturnValue_43 <= -0.7699999809265137
        ReturnValue5_4: bool = ReturnValue1_18 > 300
        ReturnValue_44: bool = BooleanOR(ReturnValue5_3, ReturnValue1_21)
        Variable3_0: bool = ReturnValue5_4
        Variable5: bool = ReturnValue_44
        ReturnValue1_22: float = Dot_VectorVector(self.mTargetMoveDir, ReturnValue_42)
        ReturnValue6_1: bool = ReturnValue1_22 <= -0.10000000149011612
        ReturnValue7_1: bool = ReturnValue1_22 <= 0.05000000074505806
        ReturnValue1_23: bool = BooleanOR(ReturnValue6_1, ReturnValue2_12)
        Variable7: bool = ReturnValue7_1
        Variable6: bool = ReturnValue1_23
        ReturnValue2_13: float = Dot_VectorVector(ReturnValue_38, ReturnValue_42)
        ReturnValue8_0: bool = ReturnValue2_13 <= 0
        Variable9: bool = ReturnValue8_0
        
        switch_11 = {
            False: ReturnValue_39,
            True: ReturnValue_38
        }
        ReturnValue8_1: Vector = switch_11.get(Variable9, None) * ReturnValue1_20
        
        switch_12 = {
            False: ReturnValue_39,
            True: ReturnValue_38
        }
        ReturnValue9_0: Vector = switch_12.get(Variable9, None) * ReturnValue_41
        ReturnValue2_14: Vector = ReturnValue8_1 + ReturnValue7_0
        ReturnValue3_7: Vector = ReturnValue9_0 + ReturnValue4_4
        ReturnValue4_6: Vector = ReturnValue2_14 + ReturnValue2_10
        ReturnValue3_8: Vector = Vector(0, 0, self.mRandomUp)
        
        switch_13 = {
            False: ReturnValue3_6,
            True: ReturnValue6_0
        }
        
        switch_14 = {
            False: ReturnValue4_6,
            True: switch_13.get(Variable3_0, None)
        }
        ReturnValue5_5: Vector = switch_14.get(Variable4, None) + ReturnValue3_8
        ReturnValue4_7: Vector = Vector(0, 0, self.mRandomUp)
        
        switch_15 = {
            False: ReturnValue3_7,
            True: ReturnValue5_2
        }
        ReturnValue6_2: Vector = switch_15.get(Variable7, None) + ReturnValue4_7
        
        switch_16 = {
            False: ReturnValue5_5,
            True: Variable_1
        }
        
        switch_17 = {
            False: ReturnValue6_2,
            True: Variable1_2
        }
        
        switch_18 = {
            0: ReturnValue_40,
            1: switch_16.get(Variable5, None),
            2: switch_17.get(Variable6, None)
        }
        self.mTargetOffsetTargetPos = switch_18.get(Variable_2, None)
        goto('L4674')
        self.ReceiveTick(DeltaSeconds)
        goto('L2400')
        # Label 9961
        self.ReceiveDied()
        goto('L5871')
        goto('L9961')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mSubtitleTimer])
        goto(ExecutionFlow.Pop())
        goto('L6381')
    
