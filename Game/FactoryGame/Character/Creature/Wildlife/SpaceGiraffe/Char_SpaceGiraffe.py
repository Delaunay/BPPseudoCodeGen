
from codegen.ue4_stub import *

from Script.Engine import FinishSpawningActor
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import GetTransform
from Script.CoreUObject import Rotator
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_instigatedBy
from Script.FactoryGame import SetPersistent
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_NewController
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_damageType
from Script.FactoryGame import StartRotationMovement
from Script.Engine import IsValid
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_byCharacter3
from Script.Engine import NotEqual_FloatFloat
from Script.Engine import FlushNetDormancy
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_targetRotation
from Script.Engine import ReceiveUnpossessed
from Script.AkAudio import PostAkEventAttached
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Audio.Play_E_SpaceGiraffe_VO_Death import Play_E_SpaceGiraffe_VO_Death
from Script.FactoryGame import FGUseState_Valid
from Script.FactoryGame import ReceiveDied
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_state
from Script.FactoryGame import FGPlayerController
from Script.Engine import Controller
from Script.Engine import SetObjectPropertyByName
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Audio.Stop_E_SpaceGiraffe_VO import Stop_E_SpaceGiraffe_VO
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_state2
from Script.FactoryGame import FGCreature
from Script.Engine import VSize2D
from Script.Engine import HUD
from Script.Engine import SelectFloat
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_ComponentBoundEvent_bFromSweep
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_damageCauser
from Script.Engine import GetHUD
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_player
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_EndPlayReason
from Game.FactoryGame.Character.Creature.BP_CreatureSeat import BP_CreatureSeat
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_state3
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_OldController
from Script.Engine import MakeTransform
from Script.FactoryGame import SetShowCrossHair
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_damagedActor
from Script.AkAudio import AkComponent
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_InputAxisEvent_AxisValue1
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_ComponentBoundEvent_OverlappedComponent
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_CustomEvent_controller
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_state1
from Script.AkAudio import PostAkEvent
from Script.Engine import ReceivePossessed
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Controller_SpaceGiraffe import Controller_SpaceGiraffe
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_byCharacter1
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Audio.Play_SpaceGiraffe_Bounce import Play_SpaceGiraffe_Bounce
from Script.FactoryGame import AddGainSignificanceObjectToSignificanceManager
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_damageAmount
from Script.Engine import BreakTransform
from Script.Engine import HasAuthority
from Script.Engine import GetController
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_DeltaSeconds
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_InputAxisEvent_AxisValue
from Script.Engine import CurveFloat
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_ComponentBoundEvent_SweepResult
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe
from Script.Engine import MakeRotator
from Script.CoreUObject import Vector2D
from Script.Engine import GetForwardVector
from Script.FactoryGame import RemoveGainSignificanceObjectFromSignificanceManager
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_byCharacter2
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_ComponentBoundEvent_OtherActor
from Script.Engine import SetComponentTickInterval
from Script.Engine import ReceiveBeginPlay
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_ComponentBoundEvent_OtherBodyIndex
from Script.Engine import GetAnimInstance
from Script.Engine import ReceiveTick
from Script.Engine import BeginDeferredActorSpawnFromClass
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_ComponentBoundEvent_OtherComp
from Script.FactoryGame import NotifyOnTakeDamage
from Script.CoreUObject import Vector
from Script.FactoryGame import FGHUD
from Script.Engine import Actor
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_player1
from Script.Engine import AnimInstance
from Script.FactoryGame import UpdateUseState
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Anim_SpaceGiraffe import Anim_SpaceGiraffe
from Script.CoreUObject import Transform
from Script.Engine import GetFloatValue
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_byCharacter

class Char_SpaceGiraffe(FGCreature):
    mDoPanic: bool
    mRotationRateCurve: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Wildlife/SpaceGiraffe/Curve_TurnrateSpaceGiraffe.Curve_TurnrateSpaceGiraffe')
    mIsMoving: bool
    mRotationWhileStill: float = 1
    mRotationWhileMoving: float = 0.20000000298023224
    mIsSprinting: bool
    mDefaultCameraRotation: Rotator
    mSeat: Ptr[BP_CreatureSeat]
    mNavigationGenerationRadius = 7000
    mNavigationRemovalRadius = 8000
    mIsEnabled = 2
    mItemToDrop = NewObject[BP_HogParts]()
    mActualAIControllerClass = NewObject[Controller_SpaceGiraffe]()
    mCanSpawnDuringDay = True
    mCanSpawnDuringNight = True
    mRotationSpeedMultiplier = 0.30000001192092896
    mEyeLocationComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 140, 'CapsuleRadius': 85, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='EyeLocationComponent')
    mSpawnWeight = 1
    mNeedsSpawner = True
    mSpawnDistance = 25000
    mFeetNames = ['fronttoe_l', 'fronttoe_r', 'backtoe_l', 'backtoe_r']
    mFootstepEffect = [{'Surface': 0, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 1, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 2, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 3, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 4, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 5, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 6, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}]
    mFootstepAudioEvents = [{'$AssetPath': '/Game/FactoryGame/Character/Creature/Wildlife/SpaceGiraffe/Audio/Play_E_SpaceGiraffe_FootStepSwitch_Front.Play_E_SpaceGiraffe_FootStepSwitch_Front'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Wildlife/SpaceGiraffe/Audio/Play_E_SpaceGiraffe_FootStepSwitch_Front.Play_E_SpaceGiraffe_FootStepSwitch_Front'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Wildlife/SpaceGiraffe/Audio/Play_E_SpaceGiraffe_FootStepSwitch_Back.Play_E_SpaceGiraffe_FootStepSwitch_Back'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Wildlife/SpaceGiraffe/Audio/Play_E_SpaceGiraffe_FootStepSwitch_Back.Play_E_SpaceGiraffe_FootStepSwitch_Back'}]
    mMaxFootstepParticleSpawnDistance = 2500
    mMaxFootstepDecalSpawnDistance = 1250
    mFootstepDecalSize = [{'X': -20, 'Y': -20, 'Z': -20}, {'X': 20, 'Y': 20, 'Z': 20}]
    mFootstepDecalLifetime = 10
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True, mCurrentHealth=200, mMaxHealth=200, mOnAdjustDamage=[0], mReplicateDamageEvents=True, mReplicateDeathEvents=True)
    mFallDamageCurve = Namespace(AssetPath='/Game/FactoryGame/Character/Player/FallDamageCurve.FallDamageCurve')
    mFallDamageDamageType = NewObject[DamageType_FallDamage]()
    mMaxDeathStayTime = 60
    mDeathRemoveCheckTime = 5
    mEnemyTargetDesirability = 1
    mDeathSound = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Wildlife/SpaceGiraffe/Audio/Play_E_SpaceGiraffe_VO_Death.Play_E_SpaceGiraffe_VO_Death')
    mMinVehiclePushVelocityForRagdoll = 400
    mTimeToGetUpFromRagdoll = 3
    mMaxDistanceMovedToGetUp = 9
    mRagdollMeshLocBoneName = Pelvis
    mRagdollMeshPhysicsBoneName = Pelvis
    mSyncBodyMaxDistance = 6
    mWeakspotMultiplier = 2
    mNormalDamageMultiplier = 1
    Mesh = Namespace(AnimClass='/Game/FactoryGame/Character/Creature/Wildlife/SpaceGiraffe/Anim_SpaceGiraffe.Anim_SpaceGiraffe_C', AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 140, 'CapsuleRadius': 85, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, BodyInstance={'ObjectType': 5, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Ragdoll', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Pawn', 'Response': 0}, {'Channel': 'WeaponInstantHit', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CachedMaxDrawDistance=25000, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='CharacterMesh0', RelativeLocation={'X': 0, 'Y': 0, 'Z': -142}, RelativeRotation={'Pitch': 0, 'Yaw': -90, 'Roll': 0}, SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Character/Creature/Wildlife/SpaceGiraffe/Mesh/SpaceGiraffe.SpaceGiraffe'}, VisibilityBasedAnimTickOption='EVisibilityBasedAnimTickOption::AlwaysTickPose', bReceivesDecals=False)
    CharacterMovement = Namespace(MaxAcceleration=3072, MaxStepHeight=100, NavAgentProps={'AgentRadius': 300, 'AgentHeight': 600, 'AgentStepHeight': 200, 'NavWalkingSearchHeightScale': 0.5, 'PreferredNavData': {'AssetPathName': 'None', 'SubPathString': ''}, 'bCanCrouch': False, 'bCanJump': True, 'bCanWalk': True, 'bCanSwim': True, 'bCanFly': False}, ObjectClass='/Script/Engine.CharacterMovementComponent', ObjectFlags=2883617, ObjectName='CharMoveComp', WalkableFloorAngle=50, WalkableFloorZ=0.6427876353263855, bUseAccelerationForPaths=True, bUseControllerDesiredRotation=True)
    CapsuleComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=140, CapsuleRadius=85, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    AutoPossessAI = EAutoPossessAI::PlacedInWorldOrSpawned
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=140, CapsuleRadius=85, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    
    def GetLookAtDecription(self):
        ReturnValue = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': 'Looking at a giraffe'}"
    

    def IsUseable(self):
        ReturnValue = False
    

    def UpdateUseState(self):
        
        useState = None
        Default__FGBlueprintFunctionLibrary.UpdateUseState(FGUseState_Valid, Ref[useState])
    

    def OnRep_mDoPanic(self):
        ReturnValue: Ptr[SkeletalMeshComponent] = self.GetMesh3P()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L275')
        ReturnValue = self.GetMesh3P()
        ReturnValue_1: Ptr[AnimInstance] = ReturnValue.GetAnimInstance()
        Giraffe: Ptr[Anim_SpaceGiraffe] = Cast[Anim_SpaceGiraffe](ReturnValue_1)
        bSuccess: bool = Giraffe
        if not bSuccess:
            goto('L275')
        Giraffe.mIsPanic = self.mDoPanic
    

    def OnUseStop(self):
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_byCharacter3 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_state3 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceGiraffe(575)
    

    def RegisterInteractingPlayer(self):
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_player1 = Player #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceGiraffe(580)
    

    def StartIsLookedAt(self):
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_byCharacter2 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_state2 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceGiraffe(585)
    

    def StopIsLookedAt(self):
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_byCharacter1 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_state1 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceGiraffe(590)
    

    def UnregisterInteractingPlayer(self):
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_player = Player #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceGiraffe(595)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Char_SpaceGiraffe(600)
    

    def ReceiveTick(self):
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceGiraffe(654)
    

    def NotifyOnTakeDamage(self):
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_damagedActor = DamagedActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_damageAmount = damageAmount #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_damageType = DamageType #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_instigatedBy = InstigatedBy #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_damageCauser = DamageCauser #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceGiraffe(984)
    

    def StartRotationMovement(self):
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_targetRotation = TargetRotation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceGiraffe(1179)
    

    def InpAxisEvt_MoveForward_K2Node_InputAxisEvent_0(self, AxisValue: float):
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_InputAxisEvent_AxisValue1 = AxisValue #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceGiraffe(1393)
    

    def InpAxisEvt_MoveRight_K2Node_InputAxisEvent_9(self, AxisValue: float):
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_InputAxisEvent_AxisValue = AxisValue #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceGiraffe(1595)
    

    def ReceivePossessed(self):
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_NewController = NewController #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceGiraffe(1775)
    

    def ClientSetupHUD(self, Controller: Ptr[FGPlayerController]):
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_CustomEvent_controller = Controller #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceGiraffe(1912)
    

    def ReceiveUnpossessed(self):
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_OldController = OldController #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceGiraffe(2071)
    

    def OnUse(self):
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_byCharacter = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceGiraffe(2106)
    

    def BndEvt__Capsule_K2Node_ComponentBoundEvent_0_ComponentBeginOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32, bFromSweep: bool, SweepResult: Const[Ref[HitResult]]):
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_ComponentBoundEvent_OverlappedComponent = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_ComponentBoundEvent_OtherActor = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_ComponentBoundEvent_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_ComponentBoundEvent_OtherBodyIndex = OtherBodyIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_ComponentBoundEvent_bFromSweep = bFromSweep #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_ComponentBoundEvent_SweepResult = SweepResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceGiraffe(2111)
    

    def ReceiveDied(self):
        self.ExecuteUbergraph_Char_SpaceGiraffe(2441)
    

    def ReceiveEndPlay(self):
        ExecuteUbergraph_Char_SpaceGiraffe.K2Node_Event_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceGiraffe(2604)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Char_SpaceGiraffe(2643)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Char_SpaceGiraffe(2722)
    

    def ExecuteUbergraph_Char_SpaceGiraffe(self):
        # Label 10
        self.FlushNetDormancy()
        self.mSeat = ReturnValue
        ReturnValue: bool = self.mSeat.DriverEnter(byCharacter)
        # End
        # Label 99
        ReturnValue_0: bool = self.HasAuthority()
        if not ReturnValue_0:
            goto('L2796')
        ReturnValue_1: Transform = self.GetTransform()
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_1], Ref[Location], Ref[Rotation], Ref[Scale])
        ReturnValue_2: Transform = MakeTransform(Location, Rotation, Scale)
        
        ReturnValue_3: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_CreatureSeat, 0, self, Ref[ReturnValue_2])
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_3, "mMountedCreature", self)
        ReturnValue_1 = self.GetTransform()
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_1], Ref[Location], Ref[Rotation], Ref[Scale])
        ReturnValue_2 = MakeTransform(Location, Rotation, Scale)
        
        ReturnValue = Default__GameplayStatics.FinishSpawningActor(ReturnValue_3, Ref[ReturnValue_2])
        goto('L10')
        # End
        # End
        # End
        # End
        # End
        self.ReceiveBeginPlay()
        Default__FGBlueprintFunctionLibrary.AddGainSignificanceObjectToSignificanceManager(self, self, 15000)
        # End
        self.ReceiveTick(DeltaSeconds)
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(self.CharacterMovement.Velocity)
        ReturnValue_4: Vector2D = Vector2D(X, Y)
        ReturnValue_5: float = VSize2D(ReturnValue_4)
        ReturnValue_6: float = self.mRotationRateCurve.GetFloatValue(ReturnValue_5)
        ReturnValue_7: Rotator = MakeRotator(0, 0, ReturnValue_6)
        self.CharacterMovement.RotationRate = ReturnValue_7
        # End
        self.NotifyOnTakeDamage(damagedActor, damageAmount, damageType, instigatedBy, damageCauser)
        ReturnValue_8: Ptr[Controller] = self.GetController()
        Giraffe: Ptr[Controller_SpaceGiraffe] = Cast[Controller_SpaceGiraffe](ReturnValue_8)
        bSuccess: bool = Giraffe
        if not bSuccess:
            goto('L2796')
        Giraffe.StartPanic()
        # End
        self.StartRotationMovement(targetRotation)
        ReturnValue_9: Ptr[SkeletalMeshComponent] = self.GetMesh3P()
        ReturnValue_10: Ptr[AnimInstance] = ReturnValue_9.GetAnimInstance()
        Giraffe_0: Ptr[Anim_SpaceGiraffe] = Cast[Anim_SpaceGiraffe](ReturnValue_10)
        bSuccess3: bool = Giraffe_0
        if not bSuccess3:
            goto('L2796')
        Giraffe_0.StartRotation(targetRotation)
        # End
        ReturnValue_11: bool = NotEqual_FloatFloat(AxisValue1, 0)
        self.mIsMoving = ReturnValue_11
        
        OutLocation = None
        OutRotation = None
        self.GetActorEyesViewPoint(Ref[OutLocation], Ref[OutRotation])
        ReturnValue_12: Vector = GetForwardVector(OutRotation)
        ReturnValue_13: Vector = ReturnValue_12 * AxisValue1
        self.AddMovementInput(ReturnValue_13, 1, False)
        # End
        ReturnValue_14: float = SelectFloat(self.mRotationWhileMoving, self.mRotationWhileStill, self.mIsMoving)
        ReturnValue1: float = SelectFloat(0.10000000149011612, ReturnValue_14, self.mIsSprinting)
        ReturnValue_15: float = AxisValue * ReturnValue1
        self.AddControllerYawInput(ReturnValue_15)
        # End
        self.ReceivePossessed(NewController)
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](NewController)
        bSuccess1: bool = Controller
        if not bSuccess1:
            goto('L2796')
        self.ClientSetupHUD(Controller)
        self.SetPersistent(True)
        # End
        ReturnValue_16: Ptr[HUD] = controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_16)
        bSuccess2: bool = AsFGHUD
        if not bSuccess2:
            goto('L2796')
        AsFGHUD.SetShowCrossHair(False)
        # End
        self.ReceiveUnpossessed(OldController)
        self.SetPersistent(False)
        # End
        goto('L99')
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](OtherActor)
        bSuccess4: bool = Player
        if not bSuccess4:
            goto('L2796')
        ReturnValue_17: Vector = Player.GetVelocity()
        ReturnValue1_0: Vector = ReturnValue_17 * -1.5
        ReturnValue_18: Vector = ReturnValue1_0 + Vector(0, 0, 1000)
        Player.LaunchCharacter(ReturnValue_18, False, False)
        ReturnValue_19: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_SpaceGiraffe_Bounce, self, True)
        # End
        self.ReceiveDied()
        ReturnValue1_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_E_SpaceGiraffe_VO, self.Mesh, "chest", True)
        ReturnValue_20: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_E_SpaceGiraffe_VO_Death, self.Mesh, "chest", True)
        # End
        Default__FGBlueprintFunctionLibrary.RemoveGainSignificanceObjectFromSignificanceManager(self, self)
        # End
        self.Mesh.SetComponentTickInterval(0)
        self.CharacterMovement.SetComponentTickInterval(0)
        # End
        self.Mesh.SetComponentTickInterval(0)
        self.CharacterMovement.SetComponentTickInterval(0.10000000149011612)
    
