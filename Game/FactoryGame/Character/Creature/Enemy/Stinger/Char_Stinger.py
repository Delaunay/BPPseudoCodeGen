
from codegen.ue4_stub import *

from Script.Engine import DrawDebugLine
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_SweepResult1
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_HitComponent
from Script.FactoryGame import ReceiveDied
from Script.Engine import Conv_VectorToString
from Script.Engine import MakeRotFromZX
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherBodyIndex
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_Event_EndPlayReason
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_HitComponent1
from Script.Engine import SetComponentTickInterval
from Script.CoreUObject import Rotator
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherComp2
from Script.FactoryGame import AddGainSignificanceObjectToSignificanceManager
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_bFromSweep
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_NormalImpulse1
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import ReceiveTick
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherActor2
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OverlappedComponent1
from Script.Engine import GetWorldDeltaSeconds
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OverlappedComponent
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherComp
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherComp3
from Script.Engine import CharacterMovementComponent
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Audio.Play_Stinger_Die_01 import Play_Stinger_Die_01
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Audio.Stop_Stinger_All import Stop_Stinger_All
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherBodyIndex1
from Script.Engine import K2_SetActorRotation
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_Hit1
from Script.CoreUObject import Vector
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_Event_DeltaSeconds
from Script.Engine import BreakHitResult
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import PawnMovementComponent
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_bFromSweep1
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_NormalImpulse
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_Hit
from Script.Engine import K2_GetActorRotation
from Script.Engine import RInterpTo
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.FactoryGame import FGEnemy
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherComp1
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherActor
from Script.FactoryGame import RemoveGainSignificanceObjectFromSignificanceManager
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherActor3
from Script.AkAudio import AkComponent
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherActor1
from Script.Engine import PrintString
from Script.Engine import GetActorForwardVector
from Script.CoreUObject import LinearColor
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_SweepResult

class Char_Stinger(FGEnemy):
    JumpAttackDone: FMulticastScriptDelegate
    mNavigationGenerationRadius = 7000
    mNavigationRemovalRadius = 8000
    mArachnophobiaModeMaterials = [{'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Stinger/Material/CatGlitch_Inst_01.CatGlitch_Inst_01'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Stinger/Material/CatGlitch_Inst_02.CatGlitch_Inst_02'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Stinger/Material/CatGlitch_Inst_03.CatGlitch_Inst_03'}]
    mIsArachnid = True
    mIsEnabled = 2
    mItemToDrop = NewObject[BP_AlphaStingerParts]()
    mShouldOptimizeMeshWhenVisible = True
    mCanSpawnDuringNight = True
    mMoveDuringRotation = True
    mRotationSpeedMultiplier = 0.6000000238418579
    mEyeLocationComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 128, 'CapsuleRadius': 84, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 114.63198852539062, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='EyeLocationComponent', RelativeLocation={'X': 80, 'Y': 0, 'Z': 0})
    mDayTimePctCountAsNight = 0.20000000298023224
    mSpawnWeight = 1
    mNeedsSpawner = True
    mSpawnDistance = -1
    mFeetNames = ['vfxfootsocket_front_l', 'vfxfootsocket_front_r', 'vfxfootsocket_back_l', 'vfxfootsocket_back_r']
    mDefaultFootstepEffect = Namespace(GroundDecals=[], Particle={'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Stinger/Particle/FootstepSoil.FootstepSoil'})
    mFootstepEffect = [{'Surface': 4, 'Effect': {'Particle': {'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Stinger/Particle/FootstepGrass.FootstepGrass'}, 'GroundDecals': []}}]
    mFootstepAudioEvents = [{'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Stinger/Audio/Play_Stinger_FootstepTest.Play_Stinger_FootstepTest'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Stinger/Audio/Play_Stinger_FootstepTest.Play_Stinger_FootstepTest'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Stinger/Audio/Play_Stinger_FootstepTest.Play_Stinger_FootstepTest'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Stinger/Audio/Play_Stinger_FootstepTest.Play_Stinger_FootstepTest'}]
    mMaxFootstepParticleSpawnDistance = 2500
    mMaxFootstepDecalSpawnDistance = 1250
    mFootstepDecalSize = [{'X': -20, 'Y': -20, 'Z': -20}, {'X': 20, 'Y': 20, 'Z': 20}]
    mFootstepDecalLifetime = 10
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True, mCurrentHealth=50, mMaxHealth=50, mOnAdjustDamage=[0], mReplicateDamageEvents=True, mReplicateDeathEvents=True)
    mFallDamageDamageType = NewObject[DamageType_FallDamage]()
    mMaxDeathStayTime = 60
    mDeathRemoveCheckTime = 5
    mEnemyTargetDesirability = 1
    mTakeDamageSound = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Stinger/Audio/Play_Stinger_Hurt.Play_Stinger_Hurt')
    mMinVehiclePushVelocityForRagdoll = 400
    mTimeToGetUpFromRagdoll = 3
    mMaxDistanceMovedToGetUp = 9
    mRagdollMeshLocBoneName = Pelvis
    mRagdollMeshPhysicsBoneName = Pelvis
    mSyncBodyMaxDistance = 6
    mWeakspotMultiplier = 2
    mNormalDamageMultiplier = 1
    Mesh = Namespace(AnimClass='/Game/FactoryGame/Character/Creature/Enemy/Stinger/Anim_Stinger.Anim_Stinger_C', AnimationData={'AnimToPlay': {'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Stinger/Animation/Idle_01.Idle_01'}, 'bSavedLooping': True, 'bSavedPlaying': True, 'SavedPosition': 0, 'SavedPlayRate': 1}, AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 128, 'CapsuleRadius': 84, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 114.63198852539062, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, BodyInstance={'ObjectType': 2, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'CharacterMesh', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Pawn', 'Response': 0}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Vehicle', 'Response': 0}, {'Channel': 'WeaponInstantHit', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 0, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='CharacterMesh0', RelativeLocation={'X': -80, 'Y': -4.768372491525952e-06, 'Z': -140}, RelativeRotation={'Pitch': 0, 'Yaw': -90, 'Roll': 0}, SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Stinger/Mesh/Stinger.Stinger'}, VisibilityBasedAnimTickOption='EVisibilityBasedAnimTickOption::AlwaysTickPose', bEnableUpdateRateOptimizations=False, bReceivesDecals=False)
    CharacterMovement = Namespace(BrakingDecelerationWalking=6000, BrakingFrictionFactor=4, FallingLateralFriction=3, JumpZVelocity=400, Mass=200, MaxAcceleration=6000, MaxStepHeight=200, MaxWalkSpeed=1800, ObjectClass='/Script/Engine.CharacterMovementComponent', ObjectFlags=2883617, ObjectName='CharMoveComp', RotationRate={'Pitch': 0, 'Yaw': 220, 'Roll': 0}, WalkableFloorAngle=90, WalkableFloorZ=-4.371138828673793e-08, bUseControllerDesiredRotation=True)
    CapsuleComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 114.63198852539062, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=128, CapsuleRadius=84, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    AutoPossessAI = EAutoPossessAI::PlacedInWorldOrSpawned
    AIControllerClass = NewObject[Controller_Stinger]()
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 114.63198852539062, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=128, CapsuleRadius=84, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    
    def BndEvt__Mesh_K2Node_ComponentBoundEvent_1_ComponentHitSignature__DelegateSignature(self, HitComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], NormalImpulse: Vector, Hit: Const[Ref[HitResult]]):
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_HitComponent1 = HitComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherActor3 = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherComp3 = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_NormalImpulse1 = NormalImpulse #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_Hit1 = Hit #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Stinger(10)
    

    def BndEvt__CapsuleComponent_K2Node_ComponentBoundEvent_2_ComponentBeginOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32, bFromSweep: bool, SweepResult: Const[Ref[HitResult]]):
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OverlappedComponent1 = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherActor2 = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherComp2 = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherBodyIndex1 = OtherBodyIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_bFromSweep1 = bFromSweep #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_SweepResult1 = SweepResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Stinger(99)
    

    def BndEvt__CapsuleComponent_K2Node_ComponentBoundEvent_3_ComponentHitSignature__DelegateSignature(self, HitComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], NormalImpulse: Vector, Hit: Const[Ref[HitResult]]):
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_HitComponent = HitComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherActor1 = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherComp1 = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_NormalImpulse = NormalImpulse #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_Hit = Hit #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Stinger(1375)
    

    def BndEvt__Mesh_K2Node_ComponentBoundEvent_0_ComponentBeginOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32, bFromSweep: bool, SweepResult: Const[Ref[HitResult]]):
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OverlappedComponent = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherActor = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_OtherBodyIndex = OtherBodyIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_bFromSweep = bFromSweep #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Stinger.K2Node_ComponentBoundEvent_SweepResult = SweepResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Stinger(1380)
    

    def ReceiveDied(self):
        self.ExecuteUbergraph_Char_Stinger(1385)
    

    def ReceiveTick(self):
        ExecuteUbergraph_Char_Stinger.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Stinger(1506)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Char_Stinger(1989)
    

    def ReceiveEndPlay(self):
        ExecuteUbergraph_Char_Stinger.K2Node_Event_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Stinger(2033)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Char_Stinger(2072)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Char_Stinger(2114)
    

    def ExecuteUbergraph_Char_Stinger(self):
        # End
        # Label 15
        self.Mesh.SetComponentTickInterval(0)
        # End
        # Label 57
        self.Mesh.SetComponentTickInterval(0)
        # End
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](OtherActor1)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L2156')
        Default__KismetSystemLibrary.PrintString(self, "bumped into player", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        ReturnValue: Ptr[PawnMovementComponent] = Player.GetMovementComponent()
        Component: Ptr[CharacterMovementComponent] = Cast[CharacterMovementComponent](ReturnValue)
        bSuccess1: bool = Component
        if not bSuccess1:
            goto('L2156')
        
        Hit = None
        bBlockingHit = None
        bInitialOverlap = None
        Time = None
        Distance = None
        Location = None
        ImpactPoint = None
        Normal = None
        ImpactNormal = None
        PhysMat = None
        HitActor = None
        HitComponent = None
        HitBoneName = None
        HitItem = None
        FaceIndex = None
        TraceStart = None
        TraceEnd = None
        Default__GameplayStatics.BreakHitResult(Ref[Hit], Ref[bBlockingHit], Ref[bInitialOverlap], Ref[Time], Ref[Distance], Ref[Location], Ref[ImpactPoint], Ref[Normal], Ref[ImpactNormal], Ref[PhysMat], Ref[HitActor], Ref[HitComponent], Ref[HitBoneName], Ref[HitItem], Ref[FaceIndex], Ref[TraceStart], Ref[TraceEnd])
        ReturnValue_0: Vector = Normal * -1
        ReturnValue1: Vector = ReturnValue_0 * 10000
        ReturnValue_1: Vector = ReturnValue1 + Vector(0, 0, 10000)
        Component.AddImpulse(ReturnValue_1, False)
        
        Hit = None
        bBlockingHit = None
        bInitialOverlap = None
        Time = None
        Distance = None
        Location = None
        ImpactPoint = None
        Normal = None
        ImpactNormal = None
        PhysMat = None
        HitActor = None
        HitComponent = None
        HitBoneName = None
        HitItem = None
        FaceIndex = None
        TraceStart = None
        TraceEnd = None
        Default__GameplayStatics.BreakHitResult(Ref[Hit], Ref[bBlockingHit], Ref[bInitialOverlap], Ref[Time], Ref[Distance], Ref[Location], Ref[ImpactPoint], Ref[Normal], Ref[ImpactNormal], Ref[PhysMat], Ref[HitActor], Ref[HitComponent], Ref[HitBoneName], Ref[HitItem], Ref[FaceIndex], Ref[TraceStart], Ref[TraceEnd])
        ReturnValue_0 = Normal * -1
        ReturnValue1 = ReturnValue_0 * 10000
        ReturnValue_2: Vector = self.K2_GetActorLocation()
        ReturnValue1_0: Vector = self.K2_GetActorLocation()
        ReturnValue1_1: Vector = ReturnValue1_0 + ReturnValue1
        Default__KismetSystemLibrary.DrawDebugLine(self, ReturnValue_2, ReturnValue1_1, LinearColor(R = 0.27083298563957214, G = 0.018441999331116676, B = 0, A = 1), 2, 3)
        ReturnValue_3: FString = Default__KismetStringLibrary.Conv_VectorToString(NormalImpulse)
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_3, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        # End
        # End
        # End
        self.ReceiveDied()
        ReturnValue_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_Stinger_Die_01, self, True)
        ReturnValue1_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_Stinger_All, self, True)
        # End
        self.ReceiveTick(DeltaSeconds)
        ReturnValue_5: Vector = self.GetActorForwardVector()
        ReturnValue_6: Rotator = self.K2_GetActorRotation()
        
        self.CharacterMovement.CurrentFloor.HitResult = None
        bBlockingHit1 = None
        bInitialOverlap1 = None
        Time1 = None
        Distance1 = None
        Location1 = None
        ImpactPoint1 = None
        Normal1 = None
        ImpactNormal1 = None
        PhysMat1 = None
        HitActor1 = None
        HitComponent1 = None
        HitBoneName1 = None
        HitItem1 = None
        FaceIndex1 = None
        TraceStart1 = None
        TraceEnd1 = None
        Default__GameplayStatics.BreakHitResult(Ref[self.CharacterMovement.CurrentFloor.HitResult], Ref[bBlockingHit1], Ref[bInitialOverlap1], Ref[Time1], Ref[Distance1], Ref[Location1], Ref[ImpactPoint1], Ref[Normal1], Ref[ImpactNormal1], Ref[PhysMat1], Ref[HitActor1], Ref[HitComponent1], Ref[HitBoneName1], Ref[HitItem1], Ref[FaceIndex1], Ref[TraceStart1], Ref[TraceEnd1])
        ReturnValue_7: float = Default__GameplayStatics.GetWorldDeltaSeconds(self)
        
        ImpactNormal1 = None
        ReturnValue_8: Rotator = MakeRotFromZX(Ref[ImpactNormal1], Ref[ReturnValue_5])
        ReturnValue_9: Rotator = RInterpTo(ReturnValue_6, ReturnValue_8, ReturnValue_7, 10)
        ReturnValue_10: bool = self.K2_SetActorRotation(ReturnValue_9, True)
        # End
        Default__FGBlueprintFunctionLibrary.AddGainSignificanceObjectToSignificanceManager(self, self, 25000)
        # End
        Default__FGBlueprintFunctionLibrary.RemoveGainSignificanceObjectFromSignificanceManager(self, self)
        # End
        self.CharacterMovement.SetComponentTickInterval(0)
        goto('L57')
        self.CharacterMovement.SetComponentTickInterval(0.10000000149011612)
        goto('L15')
    

    def JumpAttackDone__DelegateSignature(self):
        pass
    
