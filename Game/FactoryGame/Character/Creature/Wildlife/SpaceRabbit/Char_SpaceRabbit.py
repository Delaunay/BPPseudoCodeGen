
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damageCauser
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import Default__FGLootSettings
from Script.CoreUObject import Rotator
from Script.FactoryGame import SetPersistent
from Script.FactoryGame import GetLootSettingsDefaultObject
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damage1
from Script.Engine import TimerHandle
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.BP_SpaceRabbitSettings import BP_SpaceRabbitSettings
from Script.Engine import IsValid
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_instigatedBy
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_byCharacter1
from Script.Engine import FlushNetDormancy
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damageType2
from Script.FactoryGame import IsEmpty
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_player1
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_DeltaSeconds
from Script.FactoryGame import FGUseState_Valid
from Script.FactoryGame import ReceiveDied
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import Conv_RotatorToVector
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_byCharacter2
from Script.CoreUObject import LinearColor
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_state2
from Script.FactoryGame import FGPlayerController
from Script.Engine import Controller
from Script.FactoryGame import FGCreature
from Script.Engine import HUD
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_itemDescriptor
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_instigatedBy1
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Audio.Play_E_SpaceBunny_VO_Hurt import Play_E_SpaceBunny_VO_Hurt
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damagedActor
from Script.Engine import GetHUD
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damageCauser2
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_state
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_byCharacter3
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_HitLocation
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damagedActor1
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import FGCreatureController
from Script.FactoryGame import NotifyOnTakeRadialDamage
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_player
from Script.Engine import GetDistanceTo
from Script.AIModule import SetValueAsObject
from Script.AkAudio import AkComponent
from Script.Engine import PrintString
from Script.AIModule import GetValueAsBool
from Script.AkAudio import PostAkEvent
from Script.AIModule import BlackboardComponent
from Script.Engine import Delay
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Audio.Play_E_SpaceBunny_Idle_Alt_02_Graze import Play_E_SpaceBunny_Idle_Alt_02_Graze
from Script.Engine import LatentActionInfo
from Script.Engine import HasAuthority
from Script.Engine import GetController
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_byCharacter
from Script.AIModule import Default__AIBlueprintHelperLibrary
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damagedActor2
from Script.AIModule import GetBlackboard
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_state3
from Script.Engine import EqualEqual_ObjectObject
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_amount
from Script.Engine import K2_GetActorRotation
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damage
from Script.AIModule import GetAIController
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damageCauser1
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_boneName
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damageAmount
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Controller_SpaceRabbit import Controller_SpaceRabbit
from Script.Engine import RandomFloatInRange
from Script.FactoryGame import InventoryStack
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Audio.Play_E_SpaceBunny_VO_Friendly import Play_E_SpaceBunny_VO_Friendly
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damageType
from Script.AIModule import AIController
from Script.FactoryGame import NotifyOnTakePointDamage
from Script.Engine import ReceiveBeginPlay
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_instigatedBy2
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damageType1
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_shotFromDirection
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Widget_SpaceRabbit import Widget_SpaceRabbit
from Script.CoreUObject import Vector
from Script.FactoryGame import FGHUD
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_state1
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_hitComponent
from Script.Engine import Actor
from Script.FactoryGame import UpdateUseState

class Char_SpaceRabbit(FGCreature):
    mFriendBBKeyName: FName = friend
    mPetText: FText = NSLOCTEXT("", "957812C544ADB75BE1EFF1A8FE2FB3AF", "Press [ E ] to pet the Lizard Doggo")
    mPotentialThreat: Ptr[FGCharacterPlayer]
    mWalkBackTimerHandle: TimerHandle
    mIsWalkingBackwards: bool
    mWalkBackDirection: Vector
    OnWalkBackStopped: FMulticastScriptDelegate
    mWalkBackDistance: float = 1500
    mFriendActor: Ptr[Actor]
    mLootTableIndex: int32 = -1
    mLootSettings: TSubclassOf[BP_SpaceRabbitSettings] = NewObject[BP_SpaceRabbitSettings]()
    mLootTimerHandle: TimerHandle
    mLotMinTime: float = 150
    mLotMaxTime: float = 1200
    mIsAlive: bool = True
    mGotBerryBBKeyName: FName = HasGottenBerry
    mFriendText: FText = NSLOCTEXT("", "AEF2B7DB4BBEEF3494EEF3BD80F257AB", "Press [ E ] to see if Lizard Doggo has found anything.")
    mNavigationGenerationRadius = 7000
    mNavigationRemovalRadius = 8000
    mIsEnabled = 2
    mShouldOptimizeMeshWhenVisible = True
    mActualAIControllerClass = NewObject[Controller_SpaceRabbit]()
    mCanSpawnDuringDay = True
    mCanSpawnDuringNight = True
    mRotationSpeedMultiplier = 0.30000001192092896
    mEyeLocationComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 68.33037567138672, 'CapsuleRadius': 45.03343200683594, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='EyeLocationComponent')
    mSpawnWeight = 1
    mNeedsSpawner = True
    mSpawnDistance = -1
    mFeetNames = ['fronttoe_l', 'fronttoe_r', 'backtoe_l', 'backtoe_r']
    mFootstepEffect = [{'Surface': 0, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 1, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 2, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 3, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 4, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 5, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 6, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}]
    mFootstepAudioEvents = [{'$AssetPath': '/Game/FactoryGame/Character/Creature/Wildlife/SpaceRabbit/Audio/Play_E_SpaceBunny_FootStepSwitch.Play_E_SpaceBunny_FootStepSwitch'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Wildlife/SpaceRabbit/Audio/Play_E_SpaceBunny_FootStepSwitch.Play_E_SpaceBunny_FootStepSwitch'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Wildlife/SpaceRabbit/Audio/Play_E_SpaceBunny_FootStepSwitch.Play_E_SpaceBunny_FootStepSwitch'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Wildlife/SpaceRabbit/Audio/Play_E_SpaceBunny_FootStepSwitch.Play_E_SpaceBunny_FootStepSwitch'}]
    mMaxFootstepParticleSpawnDistance = 2500
    mMaxFootstepDecalSpawnDistance = 1250
    mFootstepDecalSize = [{'X': -20, 'Y': -20, 'Z': -20}, {'X': 20, 'Y': 20, 'Z': 20}]
    mFootstepDecalLifetime = 10
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True, mCurrentHealth=15, mMaxHealth=15, mOnAdjustDamage=[0], mReplicateDamageEvents=True, mReplicateDeathEvents=True)
    mFallDamageCurve = Namespace(AssetPath='/Game/FactoryGame/Character/Player/FallDamageCurve.FallDamageCurve')
    mFallDamageDamageType = NewObject[DamageType_FallDamage]()
    mMaxDeathStayTime = 60
    mDeathRemoveCheckTime = 5
    mEnemyTargetDesirability = 1
    mMinVehiclePushVelocityForRagdoll = 400
    mTimeToGetUpFromRagdoll = 3
    mMaxDistanceMovedToGetUp = 9
    mRagdollMeshLocBoneName = Pelvis
    mRagdollMeshPhysicsBoneName = Pelvis
    mSyncBodyMaxDistance = 6
    mWeakspotMultiplier = 2
    mNormalDamageMultiplier = 1
    Mesh = Namespace(AnimClass='/Game/FactoryGame/Character/Creature/Wildlife/SpaceRabbit/BP_SpaceRabbitAnim.BP_SpaceRabbitAnim_C', AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 68.33037567138672, 'CapsuleRadius': 45.03343200683594, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, BodyInstance={'ObjectType': 5, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Ragdoll', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Pawn', 'Response': 0}, {'Channel': 'WeaponInstantHit', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='CharacterMesh0', RelativeLocation={'X': 1.3351439520192798e-05, 'Y': -0.0005295610753819346, 'Z': -67.80481719970703}, RelativeRotation={'Pitch': 0, 'Yaw': -90, 'Roll': 0}, SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Character/Creature/Wildlife/SpaceRabbit/Mesh/SpaceRabbit.SpaceRabbit'}, VisibilityBasedAnimTickOption='EVisibilityBasedAnimTickOption::AlwaysTickPose', bCastCapsuleDirectShadow=True, bReceivesDecals=False)
    CharacterMovement = Namespace(NavMeshProjectionInterval=0.30000001192092896, ObjectClass='/Script/Engine.CharacterMovementComponent', ObjectFlags=2883617, ObjectName='CharMoveComp', bProjectNavMeshWalking=True, bUseAccelerationForPaths=True, bUseControllerDesiredRotation=True)
    CapsuleComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=68.33037567138672, CapsuleRadius=45.03343200683594, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    AutoPossessAI = EAutoPossessAI::PlacedInWorldOrSpawned
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=68.33037567138672, CapsuleRadius=45.03343200683594, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    
    def GetLookAtDecription(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mFriendActor)
        if not ReturnValue:
            goto('L97')
        ReturnValue_0: FText = self.mFriendText
        goto('L124')
        # Label 97
        ReturnValue_0 = self.mPetText
    

    def IsUseable(self):
        ReturnValue = True
    

    def UpdateUseState(self):
        
        useState = None
        Default__FGBlueprintFunctionLibrary.UpdateUseState(FGUseState_Valid, Ref[useState])
    

    def SetupLootTimer(self):
        OutputDelegate.BindUFunction(self, RollLoot)
        ReturnValue: float = RandomFloatInRange(self.mLotMinTime, self.mLotMaxTime)
        # Label 69
        ReturnValue_0: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, ReturnValue, False)
        self.mLootTimerHandle = ReturnValue_0
    

    def OnRep_mLootTableIndex(self):
        pass
    

    def RollLoot(self):
        ReturnValue: bool = self.mInventory.IsEmpty()
        if not ReturnValue:
            goto('L324')
        ReturnValue_0: Ptr[BP_SpaceRabbitSettings] = Default__FGLootSettings.GetLootSettingsDefaultObject(self.mLootSettings)
        
        ReturnValue_0.GetRandomLoot(Ref[self.mLootTableIndex])
        Variable: List[InventoryStack] = self.mLootSettings.ClassDefaultObject.mLootTable
        
        Item = None
        Item = Variable[self.mLootTableIndex]
        
        Item = None
        ReturnValue_1: int32 = self.mInventory.AddStack(True, Ref[Item])
        # Label 324
        OutputDelegate.BindUFunction(self, RollLoot)
        ReturnValue_2: float = RandomFloatInRange(self.mLotMinTime, self.mLotMaxTime)
        ReturnValue_3: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, ReturnValue_2, False)
        self.mLootTimerHandle = ReturnValue_3
    

    def SetNewFriend(self, newFriend: Ptr[Actor]):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L550')
        ReturnValue_0: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue_1: bool = ReturnValue_0.GetValueAsBool(Ref[self.mGotBerryBBKeyName])
        if not ReturnValue_1:
            goto('L359')
        ReturnValue1: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue1.SetValueAsObject(newFriend, Ref[self.mFriendBBKeyName])
        self.FlushNetDormancy()
        self.mFriendActor = newFriend
        self.SetPersistent(True)
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(self.mFriendActor)
        # Label 326
        if not ReturnValue_2:
            goto('L508')
        self.SetupLootTimer()
        # End
        # Label 359
        ReturnValue_3: Ptr[AIController] = Default__AIBlueprintHelperLibrary.GetAIController(self)
        Controller: Ptr[FGCreatureController] = Cast[FGCreatureController](ReturnValue_3)
        bSuccess: bool = Controller
        Controller.StartPanic()
        # End
        
        # Label 508
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mLootTimerHandle])
    

    def StopBackwardWalk(self):
        self.mWalkBackDirection = Vector(0, 0, 0)
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mWalkBackTimerHandle])
        self.FlushNetDormancy()
        self.mIsWalkingBackwards = False
        self.OnWalkBackStopped.ProcessMulticastDelegate()
    

    def UpdateWalkBackMovement(self):
        if not self.mIsWalkingBackwards:
            goto('L43')
        self.AddMovementInput(self.mWalkBackDirection, 1, False)
    

    def UpdateWalkBackDirection(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mPotentialThreat)
        if not ReturnValue:
            goto('L307')
        ReturnValue_0: float = self.mPotentialThreat.GetDistanceTo(self)
        ReturnValue_1: bool = ReturnValue_0 <= self.mWalkBackDistance
        if not ReturnValue_1:
            goto('L326')
        ReturnValue_2: Rotator = self.K2_GetActorRotation()
        ReturnValue_3: Vector = Conv_RotatorToVector(ReturnValue_2)
        ReturnValue_4: Vector = ReturnValue_3 * -1
        self.mWalkBackDirection = ReturnValue_4
        # End
        # Label 307
        self.StopBackwardWalk()
        # End
        # Label 326
        self.StopBackwardWalk()
    

    def StartWalkBack(self):
        OutputDelegate.BindUFunction(self, UpdateWalkBackDirection)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.10000000149011612, True)
        self.mWalkBackTimerHandle = ReturnValue
        self.FlushNetDormancy()
        self.mIsWalkingBackwards = True
        ReturnValue_0: Ptr[Controller] = self.GetController()
        Rabbit: Ptr[Controller_SpaceRabbit] = Cast[Controller_SpaceRabbit](ReturnValue_0)
        bSuccess: bool = Rabbit
        if not bSuccess:
            goto('L284')
        self.mWalkBackDistance = Rabbit.mPersonalDistance
    

    def OnUseStop(self):
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_byCharacter3 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_state3 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceRabbit(229)
    

    def RegisterInteractingPlayer(self):
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_player1 = Player #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceRabbit(230)
    

    def StartIsLookedAt(self):
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_byCharacter2 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_state2 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceRabbit(231)
    

    def StopIsLookedAt(self):
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_byCharacter1 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_state1 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceRabbit(232)
    

    def UnregisterInteractingPlayer(self):
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_player = Player #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceRabbit(233)
    

    def ReceiveTick(self):
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceRabbit(234)
    

    def NotifyOnTakeDamage(self):
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damagedActor2 = DamagedActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damageAmount = damageAmount #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damageType2 = DamageType #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_instigatedBy2 = InstigatedBy #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damageCauser2 = DamageCauser #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceRabbit(249)
    

    def ReceiveDied(self):
        self.ExecuteUbergraph_Char_SpaceRabbit(516)
    

    def NotifyOnTakePointDamage(self):
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damagedActor1 = DamagedActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damage1 = Damage #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_instigatedBy1 = InstigatedBy #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_HitLocation = HitLocation #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_hitComponent = HitComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_boneName = BoneName #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_shotFromDirection = ShotFromDirection #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damageType1 = DamageType #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damageCauser1 = DamageCauser #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceRabbit(591)
    

    def NotifyOnTakeRadialDamage(self):
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damagedActor = DamagedActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damage = Damage #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_instigatedBy = InstigatedBy #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damageType = DamageType #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_damageCauser = DamageCauser #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceRabbit(683)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Char_SpaceRabbit(739)
    

    def PlayConsumeItemEffect(self):
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_itemDescriptor = itemDescriptor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_amount = amount #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceRabbit(754)
    

    def OnUse(self):
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_byCharacter = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_SpaceRabbit.K2Node_Event_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_SpaceRabbit(985)
    

    def ExecuteUbergraph_Char_SpaceRabbit(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_SpaceBunny_VO_Friendly, self, True)
        goto(ExecutionFlow.Pop())
        # Label 69
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_SpaceBunny_VO_Hurt, self, True)
        goto(ExecutionFlow.Pop())
        # Label 123
        ReturnValue_0: bool = self.HasAuthority()
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(self.mFriendActor)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        self.SetupLootTimer()
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        self.UpdateWalkBackMovement()
        goto(ExecutionFlow.Pop())
        if not self.mIsAlive:
           goto(ExecutionFlow.Pop())
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_SpaceBunny_VO_Hurt, self, True)
        ReturnValue1: bool = self.HasAuthority()
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: Ptr[AIController] = Default__AIBlueprintHelperLibrary.GetAIController(self)
        Controller: Ptr[FGCreatureController] = Cast[FGCreatureController](ReturnValue_2)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Controller.StartPanic()
        self.SetNewFriend(None)
        goto('L69')
        self.ReceiveDied()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_SpaceBunny_VO_Hurt, self, True)
        self.mIsAlive = False
        goto(ExecutionFlow.Pop())
        self.NotifyOnTakePointDamage(damagedActor1, damage1, instigatedBy1, HitLocation, hitComponent, boneName, shotFromDirection, damageType1, damageCauser1)
        goto(ExecutionFlow.Pop())
        self.NotifyOnTakeRadialDamage(damagedActor, damage, instigatedBy, damageType, damageCauser)
        goto(ExecutionFlow.Pop())
        self.ReceiveBeginPlay()
        goto('L123')
        Default__KismetSystemLibrary.PrintString(self, "char_rabbit ate something", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_SpaceBunny_Idle_Alt_02_Graze, self, True)
        Default__KismetSystemLibrary.Delay(self, 1, LatentActionInfo(Linkage = 15, UUID = -604063592, ExecutionFunction = "ExecuteUbergraph_Char_SpaceRabbit", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue_3: bool = byCharacter.IsLocallyControlled()
        ReturnValue_4: bool = EqualEqual_ObjectObject(self.mFriendActor, byCharacter)
        ReturnValue_5: bool = ReturnValue_4 and ReturnValue_3
        if not ReturnValue_5:
            goto('L1455')
        ReturnValue_6: Ptr[Controller] = byCharacter.GetController()
        Controller_0: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_6)
        bSuccess1: bool = Controller_0
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue_7: Ptr[HUD] = Controller_0.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_7)
        bSuccess2: bool = AsFGHUD
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        AsFGHUD.OpenInteractUI(Widget_SpaceRabbit, self)
        ReturnValue5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_SpaceBunny_VO_Friendly, self, True)
        goto(ExecutionFlow.Pop())
        # Label 1455
        self.SetNewFriend(byCharacter)
        goto(ExecutionFlow.Pop())
    

    def OnWalkBackStopped__DelegateSignature(self):
        pass
    
