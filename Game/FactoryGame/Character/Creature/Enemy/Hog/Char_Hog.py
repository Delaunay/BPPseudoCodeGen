
from codegen.ue4_stub import *

from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Character.Creature.Enemy.Hog.Audio.Play_E_Hog_VO_Die import Play_E_Hog_VO_Die
from Script.CoreUObject import Rotator
from Game.FactoryGame.Character.Creature.Enemy.Hog.Audio.Play_Hog_VO_Threatened import Play_Hog_VO_Threatened
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_DeltaSeconds
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_HitLocation
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_EndPlayReason
from Game.FactoryGame.Character.Creature.Enemy.Hog.Audio.Play_Hog_VO_Charge import Play_Hog_VO_Charge
from Script.Engine import Normal
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_Other
from Script.AkAudio import PostAkEventAttached
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_damagedActor1
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.FactoryGame import ReceiveDied
from Script.Engine import Conv_RotatorToVector
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_damage
from Script.Engine import Controller
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog
from Script.Engine import Pawn
from Script.Engine import VSize
from Script.FactoryGame import GetCurrentAggroTarget
from Script.Engine import SelectFloat
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_damageCauser1
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_hitComponent
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_shotFromDirection
from Script.CoreUObject import Object
from Game.FactoryGame.Character.Creature.Enemy.Hog.AI.BTT_CircleMove import BTT_CircleMove
from Script.AIModule import GetValueAsObject
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_boneName
from Script.AkAudio import Default__AkGameplayStatics
from Script.AIModule import SetValueAsObject
from Script.AkAudio import AkComponent
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_OtherComp
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_NormalImpulse
from Script.AkAudio import PostAkEvent
from Script.AIModule import BlackboardComponent
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_damageAmount
from Script.Engine import Delay
from Script.Engine import K2_SetTimerDelegate
from Script.FactoryGame import AddGainSignificanceObjectToSignificanceManager
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_bSelfMoved
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_damageType1
from Script.Engine import Conv_IntToFloat
from Script.Engine import LatentActionInfo
from Script.Engine import FindLookAtRotation
from Script.Engine import GetController
from Script.AIModule import Default__AIBlueprintHelperLibrary
from Game.FactoryGame.Character.Creature.Enemy.Hog.DamageType_HogHit import DamageType_HogHit
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_instigatedBy1
from Script.Engine import CurveFloat
from Script.Engine import Default__GameplayStatics
from Script.Engine import BreakRotator
from Script.Engine import Subtract_VectorVector
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_CustomEvent_BTTCircleMove
from Script.AIModule import GetBlackboard
from Script.Engine import K2_SetActorRotation
from Script.Engine import K2_GetActorRotation
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.Engine import MakeRotator
from Script.Engine import ApplyDamage
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_damageType
from Script.AIModule import GetAIController
from Script.Engine import GetForwardVector
from Script.FactoryGame import RemoveGainSignificanceObjectFromSignificanceManager
from Script.FactoryGame import IsAliveAndWell
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_instigatedBy
from Script.Engine import RandomFloatInRange
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_HitLocation1
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_Hit
from Script.Engine import SetComponentTickInterval
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_damageCauser
from Script.AIModule import AIController
from Script.AIModule import SetValueAsBool
from Script.Engine import Not_PreBool
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_damagedActor
from Script.Engine import ReceiveTick
from Script.Engine import K2_GetPawn
from Game.FactoryGame.Character.Creature.Enemy.Hog.Anim_Hog import Anim_Hog
from Script.Engine import GetWorldDeltaSeconds
from Script.FactoryGame import NotifyOnTakeDamage
from Script.Engine import BooleanOR
from Script.CoreUObject import Vector
from Script.FactoryGame import FGEnemy
from Script.Engine import RInterpTo
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_MyComp
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import ExecuteUbergraph_Char_Hog.K2Node_Event_HitNormal
from Script.Engine import AnimInstance
from Script.Engine import GetFloatValue

class Char_Hog(FGEnemy):
    mStuckInMovement: bool
    mDebug: bool
    mChargeDirection: Vector
    mChargeDistance: float = 4000
    mChargeTimerHandle: TimerHandle
    mIsCharging: bool
    OnChargeMovementStopped: FMulticastScriptDelegate
    mChargeDamage: int32 = 10
    mRotationRateCurveHog: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Hog/Curve_DistanceRotation.Curve_DistanceRotation')
    mIsThreatened: bool
    mChargeDamageCooldown: float
    mChargeDamageCooldownDefault: float = 2
    mDoPanicName: FName = DoPanic
    mCircling: bool
    mCircleAngle: float = 90
    mBTTCircleMove: Ptr[BTT_CircleMove]
    mDamageCauserBBKey: FName = DamageCauser
    mStaggered: bool
    mIsAlpha: bool
    mStaggerCooldown: float = 2
    mNavigationGenerationRadius = 7000
    mNavigationRemovalRadius = 8000
    mIsEnabled = 2
    mItemToDrop = NewObject[BP_HogParts]()
    mShouldOptimizeMeshWhenVisible = True
    mActualAIControllerClass = NewObject[Controller_HogCharge]()
    mCanSpawnDuringDay = True
    mCanSpawnDuringNight = True
    mRotationSpeedMultiplier = 0.30000001192092896
    mEyeLocationComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 55, 'CapsuleRadius': 55, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 135.6358184814453, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='EyeLocationComponent')
    mSpawnWeight = 1
    mNeedsSpawner = True
    mSpawnDistance = -1
    mFeetNames = ['vfxfootsocket_front_l', 'vfxfootsocket_front_r', 'vfxfootsocket_back_l', 'vfxfootsocket_back_r']
    mFootstepEffect = [{'Surface': 0, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 1, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 2, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 3, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 4, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 5, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 6, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}]
    mFootstepAudioEvents = [{'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/_Shared/Audio/Play_E_Hog_Footstep_Switch.Play_E_Hog_Footstep_Switch'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/_Shared/Audio/Play_E_Hog_Footstep_Switch.Play_E_Hog_Footstep_Switch'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/_Shared/Audio/Play_E_Hog_Footstep_Switch.Play_E_Hog_Footstep_Switch'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/_Shared/Audio/Play_E_Hog_Footstep_Switch.Play_E_Hog_Footstep_Switch'}]
    mMaxFootstepParticleSpawnDistance = 2500
    mMaxFootstepDecalSpawnDistance = 1250
    mFootstepDecalSize = [{'X': -20, 'Y': -20, 'Z': -20}, {'X': 20, 'Y': 20, 'Z': 20}]
    mFootstepDecalLifetime = 10
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True, mCurrentHealth=20, mMaxHealth=20, mOnAdjustDamage=[0], mReplicateDamageEvents=True, mReplicateDeathEvents=True)
    mFallDamageCurve = Namespace(AssetPath='/Game/FactoryGame/Character/Player/FallDamageCurve.FallDamageCurve')
    mFallDamageDamageType = NewObject[DamageType_FallDamage]()
    mMaxDeathStayTime = 60
    mDeathRemoveCheckTime = 5
    mEnemyTargetDesirability = 1
    mTakeDamageSound = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Hog/Audio/Play_E_Hog_VO_Hurt.Play_E_Hog_VO_Hurt')
    mMinVehiclePushVelocityForRagdoll = 400
    mTimeToGetUpFromRagdoll = 3
    mMaxDistanceMovedToGetUp = 9
    mRagdollMeshLocBoneName = Pelvis
    mRagdollMeshPhysicsBoneName = Pelvis
    mSyncBodyMaxDistance = 6
    mApplyDamageMomentum = True
    mWeakspotMultiplier = 1
    mWeakspotBoneNames = ['headplate_01', 'headplate_02', 'headplate_03', 'headplate_04', 'headplate_05', 'headplate_06']
    mNormalDamageMultiplier = 1
    Mesh = Namespace(AnimClass='/Game/FactoryGame/Character/Creature/Enemy/Hog/Anim_Hog.Anim_Hog_C', AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 55, 'CapsuleRadius': 55, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 135.6358184814453, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, BodyInstance={'ObjectType': 2, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'CharacterMesh', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Pawn', 'Response': 0}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Vehicle', 'Response': 0}, {'Channel': 'WeaponInstantHit', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 121.313232421875, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CachedMaxDrawDistance=15000, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='CharacterMesh0', RelativeLocation={'X': 0, 'Y': -9.999999974752427e-07, 'Z': -56.506103515625}, RelativeRotation={'Pitch': 0, 'Yaw': -90, 'Roll': 0}, RelativeScale3D={'X': 1.5, 'Y': 1.5, 'Z': 1.5}, SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Hog/Mesh/Hog.Hog'}, VisibilityBasedAnimTickOption='EVisibilityBasedAnimTickOption::AlwaysTickPose', bReceivesDecals=False)
    CharacterMovement = Namespace(BrakingFriction=1, Mass=200, MaxAcceleration=8096, MaxStepHeight=100, MaxWalkSpeed=100, NavAgentProps={'AgentRadius': 42, 'AgentHeight': 192, 'AgentStepHeight': 100, 'NavWalkingSearchHeightScale': 1, 'PreferredNavData': {'AssetPathName': 'None', 'SubPathString': ''}, 'bCanCrouch': False, 'bCanJump': True, 'bCanWalk': True, 'bCanSwim': True, 'bCanFly': False}, NavMeshProjectionInterval=0.30000001192092896, ObjectClass='/Script/Engine.CharacterMovementComponent', ObjectFlags=2883617, ObjectName='CharMoveComp', WalkableFloorAngle=50, WalkableFloorZ=0.6427876353263855, bProjectNavMeshWalking=True, bUseAccelerationForPaths=True, bUseControllerDesiredRotation=True)
    CapsuleComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 135.6358184814453, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=55, CapsuleRadius=55, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    AutoPossessAI = EAutoPossessAI::PlacedInWorldOrSpawned
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 135.6358184814453, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=55, CapsuleRadius=55, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    
    def OnRep_mIsThreatened(self):
        ReturnValue: Ptr[SkeletalMeshComponent] = self.GetMesh3P()
        ReturnValue_0: Ptr[AnimInstance] = ReturnValue.GetAnimInstance()
        Hog: Ptr[Anim_Hog] = Cast[Anim_Hog](ReturnValue_0)
        bSuccess: bool = Hog
        if not bSuccess:
            goto('L239')
        Hog.mIsThreatened = self.mIsThreatened
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_Hog_VO_Threatened, self, True)
    

    def StartChargeMovement(self):
        OutputDelegate.BindUFunction(self, UpdateChargeDirection)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.10000000149011612, True)
        self.mChargeTimerHandle = ReturnValue
        self.mIsCharging = True
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_Hog_VO_Charge, self, True)
    

    def UpdateChargeMovement(self):
        self.AddMovementInput(self.mChargeDirection, 1, False)
    

    def StopChargeMovement(self):
        self.mChargeDirection = Vector(0, 0, 0)
        self.CharacterMovement.RotationRate = Rotator::FromPitchYawRoll(0, 300, 0)
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mChargeTimerHandle])
        self.mIsCharging = False
        self.OnChargeMovementStopped.ProcessMulticastDelegate()
    

    def UpdateChargeDirection(self):
        ReturnValue: Ptr[Actor] = self.GetCurrentAggroTarget()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L835')
        ReturnValue1: Ptr[Actor] = self.GetCurrentAggroTarget()
        ReturnValue_1: Vector = ReturnValue1.K2_GetActorLocation()
        ReturnValue_2: float = self.mChargeDistance * 1.2000000476837158
        ReturnValue1_0: Vector = self.K2_GetActorLocation()
        ReturnValue_3: Vector = Subtract_VectorVector(ReturnValue_1, ReturnValue1_0)
        ReturnValue_4: float = VSize(ReturnValue_3)
        ReturnValue_5: bool = ReturnValue_4 <= ReturnValue_2
        if not ReturnValue_5:
            goto('L835')
        ReturnValue1 = self.GetCurrentAggroTarget()
        ReturnValue_1 = ReturnValue1.K2_GetActorLocation()
        ReturnValue1_0 = self.K2_GetActorLocation()
        ReturnValue_3 = Subtract_VectorVector(ReturnValue_1, ReturnValue1_0)
        ReturnValue_4 = VSize(ReturnValue_3)
        ReturnValue_6: float = self.mRotationRateCurveHog.GetFloatValue(ReturnValue_4)
        ReturnValue_7: Rotator = MakeRotator(0, 0, ReturnValue_6)
        self.CharacterMovement.RotationRate = ReturnValue_7
        ReturnValue_8: Rotator = self.K2_GetActorRotation()
        ReturnValue_9: Vector = GetForwardVector(ReturnValue_8)
        ReturnValue_10: Vector = Normal(ReturnValue_9, 9.999999747378752e-05)
        self.mChargeDirection = ReturnValue_10
        # Label 830
        # End
        # Label 835
        self.StopChargeMovement()
    

    def ReceiveHit(self):
        ExecuteUbergraph_Char_Hog.K2Node_Event_MyComp = MyComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_Other = Other #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_bSelfMoved = bSelfMoved #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_HitLocation1 = HitLocation #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_HitNormal = HitNormal #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_NormalImpulse = NormalImpulse #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_Hit = Hit #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Hog(3688)
    

    def NotifyOnTakeDamage(self):
        ExecuteUbergraph_Char_Hog.K2Node_Event_damagedActor1 = DamagedActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_damageAmount = damageAmount #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_damageType1 = DamageType #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_instigatedBy1 = InstigatedBy #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_damageCauser1 = DamageCauser #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Hog(924)
    

    def CheckTargetHeight(self):
        self.ExecuteUbergraph_Char_Hog(504)
    

    def ReceiveTick(self):
        ExecuteUbergraph_Char_Hog.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Hog(886)
    

    def circle(self):
        self.ExecuteUbergraph_Char_Hog(1928)
    

    def StartCircling(self, BTTCircleMove: Ptr[BTT_CircleMove]):
        ExecuteUbergraph_Char_Hog.K2Node_CustomEvent_BTTCircleMove = BTTCircleMove #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Hog(2971)
    

    def StopCircling(self):
        self.ExecuteUbergraph_Char_Hog(3576)
    

    def ReceiveDied(self):
        self.ExecuteUbergraph_Char_Hog(3603)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Char_Hog(3693)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Char_Hog(3733)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Char_Hog(3843)
    

    def ReceiveEndPlay(self):
        ExecuteUbergraph_Char_Hog.K2Node_Event_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Hog(3918)
    

    def NotifyOnWeakspotHit(self):
        self.ExecuteUbergraph_Char_Hog(3923)
    

    def NotifyOnTakePointDamage(self):
        ExecuteUbergraph_Char_Hog.K2Node_Event_damagedActor = DamagedActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_damage = Damage #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_instigatedBy = InstigatedBy #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_HitLocation = HitLocation #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_hitComponent = HitComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_boneName = BoneName #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_shotFromDirection = ShotFromDirection #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_damageType = DamageType #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Hog.K2Node_Event_damageCauser = DamageCauser #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Hog(3924)
    

    def ExecuteUbergraph_Char_Hog(self):
        goto(ComputedJump("EntryPoint"))
        self.CheckTargetHeight()
        goto(ExecutionFlow.Pop())
        # Label 30
        ReturnValue: bool = self.IsAliveAndWell()
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](Other)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L379')
        ReturnValue_0: Ptr[Controller] = self.GetController()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: float = Conv_IntToFloat(self.mChargeDamage)
        ReturnValue1: Ptr[Controller] = self.GetController()
        ReturnValue_3: float = Default__GameplayStatics.ApplyDamage(Player, ReturnValue_2, ReturnValue1, self, DamageType_HogHit)
        if not self.mCircling:
            goto('L477')
        goto(ExecutionFlow.Pop())
        # Label 379
        ReturnValue3: bool = Default__KismetSystemLibrary.IsValid(self.mBTTCircleMove)
        if not ReturnValue3:
           goto(ExecutionFlow.Pop())
        self.mBTTCircleMove.FinishCircleMove()
        goto(ExecutionFlow.Pop())
        # Label 477
        self.StopChargeMovement()
        goto(ExecutionFlow.Pop())
        self.mStaggered = False
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        # Label 505
        self.ChargeParticle.Deactivate()
        Variable1: bool = False
        Variable1_0: bool = True
        goto(ExecutionFlow.Pop())
        # Label 564
        self.ChargeParticle.Activate(False)
        Variable: bool = False
        Variable_0: bool = True
        goto(ExecutionFlow.Pop())
        # Label 624
        if not self.mIsCharging:
            goto('L754')
        self.UpdateChargeMovement()
        ExecutionFlow.Push("L677")
        ExecutionFlow.Push("L830")
        if not Variable1_0:
            goto('L861')
        goto(ExecutionFlow.Pop())
        # Label 677
        Default__KismetSystemLibrary.Delay(self, 1, LatentActionInfo(Linkage = 15, UUID = 816188954, ExecutionFunction = "ExecuteUbergraph_Char_Hog", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 754
        ExecutionFlow.Push("L799")
        if not Variable_0:
            goto('L774')
        goto(ExecutionFlow.Pop())
        # Label 774
        Variable_0 = True
        if not False:
           goto(ExecutionFlow.Pop())
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 799
        if not Variable:
            goto('L814')
        goto(ExecutionFlow.Pop())
        # Label 814
        Variable = True
        goto('L505')
        # Label 830
        if not Variable1:
            goto('L845')
        goto(ExecutionFlow.Pop())
        # Label 845
        Variable1 = True
        goto('L564')
        # Label 861
        Variable1_0 = True
        if not False:
           goto(ExecutionFlow.Pop())
        Variable1 = True
        goto(ExecutionFlow.Pop())
        self.ReceiveTick(DeltaSeconds)
        self.circle()
        goto('L624')
        self.NotifyOnTakeDamage(damagedActor1, damageAmount, damageType1, instigatedBy1, damageCauser1)
        ReturnValue_4: Ptr[AIController] = Default__AIBlueprintHelperLibrary.GetAIController(self)
        ReturnValue4: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_4)
        if not ReturnValue4:
           goto(ExecutionFlow.Pop())
        ReturnValue_4 = Default__AIBlueprintHelperLibrary.GetAIController(self)
        ReturnValue_5: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(ReturnValue_4)
        
        ReturnValue_6: Ptr[Object] = ReturnValue_5.GetValueAsObject(Ref[self.mDamageCauserBBKey])
        ReturnValue5: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_6)
        if not ReturnValue5:
            goto('L1737')
        # Label 1293
        ReturnValue_4 = Default__AIBlueprintHelperLibrary.GetAIController(self)
        ReturnValue_5 = Default__AIBlueprintHelperLibrary.GetBlackboard(ReturnValue_4)
        ReturnValue_7: bool = BooleanOR(self.mStaggered, self.mIsAlpha)
        ReturnValue1_0: bool = self.mIsCharging and ReturnValue_7
        ReturnValue_8: bool = Not_PreBool(ReturnValue1_0)
        
        ReturnValue_5.SetValueAsBool(ReturnValue_8, Ref[self.mDoPanicName])
        ExecutionFlow.Push("L1645")
        ReturnValue2: bool = Default__KismetSystemLibrary.IsValid(self.mBTTCircleMove)
        if not ReturnValue2:
           goto(ExecutionFlow.Pop())
        self.mBTTCircleMove.FinishCircleMove()
        goto(ExecutionFlow.Pop())
        # Label 1645
        self.mStaggered = True
        Default__KismetSystemLibrary.Delay(self, self.mStaggerCooldown, LatentActionInfo(Linkage = 492, UUID = 1727627041, ExecutionFunction = "ExecuteUbergraph_Char_Hog", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1737
        ReturnValue_9: Ptr[Pawn] = instigatedBy1.K2_GetPawn()
        ReturnValue_4 = Default__AIBlueprintHelperLibrary.GetAIController(self)
        ReturnValue_5 = Default__AIBlueprintHelperLibrary.GetBlackboard(ReturnValue_4)
        
        ReturnValue_5.SetValueAsObject(ReturnValue_9, Ref[self.mDamageCauserBBKey])
        goto('L1293')
        if not self.mCircling:
           goto(ExecutionFlow.Pop())
        ReturnValue_10: Ptr[Actor] = self.GetCurrentAggroTarget()
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_10)
        if not ReturnValue1_1:
            goto('L2934')
        ReturnValue_10 = self.GetCurrentAggroTarget()
        ReturnValue_11: Vector = self.K2_GetActorLocation()
        ReturnValue1_2: Vector = ReturnValue_10.K2_GetActorLocation()
        
        ReturnValue_12: Rotator = FindLookAtRotation(Ref[ReturnValue_11], Ref[ReturnValue1_2])
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_12, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_13: float = Yaw + self.mCircleAngle
        ReturnValue_14: Rotator = MakeRotator(Roll, Pitch, ReturnValue_13)
        ReturnValue_15: Vector = Conv_RotatorToVector(ReturnValue_14)
        self.AddMovementInput(ReturnValue_15, 1, False)
        ReturnValue_10 = self.GetCurrentAggroTarget()
        ReturnValue_11 = self.K2_GetActorLocation()
        ReturnValue1_2 = ReturnValue_10.K2_GetActorLocation()
        
        ReturnValue_12 = FindLookAtRotation(Ref[ReturnValue_11], Ref[ReturnValue1_2])
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_12, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_16: float = Default__GameplayStatics.GetWorldDeltaSeconds(self)
        ReturnValue_17: Rotator = self.K2_GetActorRotation()
        ReturnValue_13 = Yaw + self.mCircleAngle
        ReturnValue_14 = MakeRotator(Roll, Pitch, ReturnValue_13)
        ReturnValue_18: Rotator = RInterpTo(ReturnValue_17, ReturnValue_14, ReturnValue_16, 10)
        
        Roll2 = None
        Pitch2 = None
        Yaw2 = None
        BreakRotator(ReturnValue_18, Ref[Roll2], Ref[Pitch2], Ref[Yaw2])
        ReturnValue1_3: Rotator = MakeRotator(0, 0, Yaw2)
        ReturnValue_19: bool = self.K2_SetActorRotation(ReturnValue1_3, False)
        goto(ExecutionFlow.Pop())
        # Label 2934
        self.mBTTCircleMove.FinishCircleMove()
        goto(ExecutionFlow.Pop())
        self.mBTTCircleMove = BTTCircleMove
        ReturnValue_20: float = RandomFloatInRange(80, 85)
        ReturnValue1_4: float = RandomFloatInRange(-80, -85)
        ReturnValue1_5: Rotator = self.K2_GetActorRotation()
        
        Roll1 = None
        Pitch1 = None
        Yaw1 = None
        BreakRotator(ReturnValue1_5, Ref[Roll1], Ref[Pitch1], Ref[Yaw1])
        ReturnValue2_0: Vector = self.K2_GetActorLocation()
        ReturnValue1_6: Ptr[Actor] = self.GetCurrentAggroTarget()
        ReturnValue3_0: Vector = ReturnValue1_6.K2_GetActorLocation()
        
        ReturnValue1_7: Rotator = FindLookAtRotation(Ref[ReturnValue2_0], Ref[ReturnValue3_0])
        
        Roll3 = None
        Pitch3 = None
        Yaw3 = None
        BreakRotator(ReturnValue1_7, Ref[Roll3], Ref[Pitch3], Ref[Yaw3])
        ReturnValue_21: float = Yaw1 - Yaw3
        ReturnValue_22: bool = ReturnValue_21 <= 180
        ReturnValue_23: bool = ReturnValue_21 > 0
        ReturnValue_24: bool = ReturnValue_23 and ReturnValue_22
        ReturnValue_25: float = SelectFloat(ReturnValue_20, ReturnValue1_4, ReturnValue_24)
        self.mCircleAngle = ReturnValue_25
        self.mCircling = True
        goto(ExecutionFlow.Pop())
        self.mCircling = False
        goto(ExecutionFlow.Pop())
        # Label 3588
        if not self.mIsCharging:
           goto(ExecutionFlow.Pop())
        goto('L30')
        self.ReceiveDied()
        ReturnValue_26: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_E_Hog_VO_Die, self.Mesh, "jaw", True)
        goto(ExecutionFlow.Pop())
        goto('L3588')
        Default__FGBlueprintFunctionLibrary.AddGainSignificanceObjectToSignificanceManager(self, self, 10000)
        goto(ExecutionFlow.Pop())
        self.CharacterMovement.SetComponentTickInterval(0)
        self.Mesh.SetComponentTickInterval(0)
        goto(ExecutionFlow.Pop())
        # Label 3808
        Default__FGBlueprintFunctionLibrary.RemoveGainSignificanceObjectFromSignificanceManager(self, self)
        goto(ExecutionFlow.Pop())
        self.CharacterMovement.SetComponentTickInterval(0.10000000149011612)
        self.Mesh.SetComponentTickInterval(0)
        goto(ExecutionFlow.Pop())
        goto('L3808')
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
    

    def OnChargeMovementStopped__DelegateSignature(self):
        pass
    
