
from codegen.ue4_stub import *

from Script.Engine import FinishSpawningActor
from Script.Engine import RandomPointInBoundingBox
from Script.Engine import SetVisibility
from Game.FactoryGame.Character.Creature.Enemy.CrabHatcher.Char_CrabHatcher import ExecuteUbergraph_Char_CrabHatcher.K2Node_Event_EndPlayReason
from Script.Engine import SetObjectPropertyByName
from Script.AkAudio import PostAkEventAtLocation
from Script.Engine import SpawnEmitterAtLocation
from Script.Engine import SetComponentTickInterval
from Script.CoreUObject import Rotator
from Script.FactoryGame import AddGainSignificanceObjectToSignificanceManager
from Script.Engine import K2_SetTimer
from Game.FactoryGame.Character.Creature.Enemy.CrabHatcher.Char_CrabHatcher import ExecuteUbergraph_Char_CrabHatcher.K2Node_CustomEvent_Loaded
from Script.Engine import ReceiveBeginPlay
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Character.Creature.Enemy.CrabHatcher.Char_CrabHatcher import ExecuteUbergraph_Char_CrabHatcher.K2Node_Event_OtherActor
from Script.Engine import HasAuthority
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import SetAnimation
from Game.FactoryGame.Character.Creature.Enemy.CrabHatcher.Char_CrabHatcher import ExecuteUbergraph_Char_CrabHatcher.K2Node_CustomEvent_damagedActor
from Script.FactoryGame import FGCrabHatcher
from Script.Engine import LoadAsset
from Script.Engine import SkeletalMeshComponent
from Script.Engine import GetObjectClass
from Game.FactoryGame.Character.Creature.Enemy.CrabHatcher.Char_CrabHatcher import ExecuteUbergraph_Char_CrabHatcher.K2Node_CustomEvent_damageCauser
from Script.Engine import TimerHandle
from Script.CoreUObject import Object
from Game.FactoryGame.Character.Creature.Enemy.Crab.BabyCrab.Char_BabyCrab import Char_BabyCrab
from Script.Engine import IsValid
from Game.FactoryGame.Character.Creature.Enemy.CrabHatcher.Char_CrabHatcher import ExecuteUbergraph_Char_CrabHatcher.K2Node_CustomEvent_damageType
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.FactoryGame import GetSpawner
from Script.FactoryGame import SpawnCrabs
from Script.Engine import ClassIsChildOf
from Script.FactoryGame import SetDidSpawnCrabs
from Script.Engine import Conv_SoftObjectReferenceToObject
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.Character.Creature.Enemy.CrabHatcher.Char_CrabHatcher import ExecuteUbergraph_Char_CrabHatcher
from Script.Engine import ParticleSystem
from Script.Engine import AnimSequence
from Script.CoreUObject import Vector
from Script.Engine import K2_GetComponentLocation
from Script.FactoryGame import GetDidSpawnCrabs
from Script.Engine import K2_GetActorRotation
from Game.FactoryGame.Character.Creature.Enemy.CrabHatcher.Char_CrabHatcher import ExecuteUbergraph_Char_CrabHatcher.K2Node_CustomEvent_Damage
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import Kill
from Script.Engine import MakeTransform
from Script.Engine import ParticleSystemComponent
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Script.FactoryGame import FGCreatureSpawner
from Game.FactoryGame.Character.Creature.Enemy.CrabHatcher.Char_CrabHatcher import ExecuteUbergraph_Char_CrabHatcher.K2Node_CustomEvent_instigatedBy
from Script.FactoryGame import SetAnimationLength
from Script.FactoryGame import StartExpanding
from Script.Engine import RandomUnitVector
from Script.FactoryGame import RemoveGainSignificanceObjectFromSignificanceManager
from Game.FactoryGame.Character.Creature.Enemy.CrabHatcher.Audio.Play_E_Hatchery_Hive import Play_E_Hatchery_Hive
from Script.AkAudio import AkComponent
from Script.FactoryGame import ReceiveDied
from Script.CoreUObject import Transform
from Script.FactoryGame import AddCreature
from Script.FactoryGame import FGWheeledVehicle

class Char_CrabHatcher(FGCrabHatcher):
    mGrowAnimation: Ptr[AnimSequence] = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Crab/CrabEggs/Animation/shake_01.shake_01')
    mEnemiesSpawned: int32
    mEnemiesToSpawn: int32 = 3
    mCrabParticles: TSoftObjectPtr[Object] = NewObject[P_CrabEggsHatch_01]()
    mExplodingEggs_VFX: Ptr[ParticleSystemComponent]
    mThreatTimerMax = 1.2000000476837158
    mNavigationGenerationRadius = 7000
    mNavigationRemovalRadius = 8000
    mIsEnabled = 2
    mItemToDrop = NewObject[BP_CrabEggParts]()
    mShouldOptimizeMeshWhenVisible = True
    mActualAIControllerClass = NewObject[Controller_CrabHatcher]()
    mCanSpawnDuringDay = True
    mCanSpawnDuringNight = True
    mRotationSpeedMultiplier = 0.30000001192092896
    mEyeLocationComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 180, 'CapsuleRadius': 180, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}, {'Channel': 'Vehicle', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='EyeLocationComponent')
    mSpawnWeight = 0.5
    mNeedsSpawner = True
    mSpawnDistance = -1
    mMaxFootstepParticleSpawnDistance = 2500
    mMaxFootstepDecalSpawnDistance = 1250
    mFootstepDecalSize = [{'X': -20, 'Y': -20, 'Z': -20}, {'X': 20, 'Y': 20, 'Z': 20}]
    mFootstepDecalLifetime = 10
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True, mOnAdjustDamage=[0], mReplicateDamageEvents=True, mReplicateDeathEvents=True)
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
    Mesh = Namespace(AnimationData={'AnimToPlay': {'$Empty': True}, 'bSavedLooping': False, 'bSavedPlaying': False, 'SavedPosition': 0, 'SavedPlayRate': 1}, AnimationMode=1, AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 180, 'CapsuleRadius': 180, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}, {'Channel': 'Vehicle', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, BodyInstance={'ObjectType': 2, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'CharacterMesh', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Pawn', 'Response': 0}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Vehicle', 'Response': 0}, {'Channel': 'WeaponInstantHit', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='CharacterMesh0', OverrideMaterials=[{'$Empty': True}], RelativeLocation={'X': 0, 'Y': -0.0001220703125, 'Z': -223.79071044921875}, RelativeScale3D={'X': 0.5, 'Y': 0.5, 'Z': 0.5}, SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Crab/CrabEggs/Mesh/CrabEggs_skl.CrabEggs_skl'}, VisibilityBasedAnimTickOption='EVisibilityBasedAnimTickOption::AlwaysTickPose', bComponentUseFixedSkelBounds=True)
    CharacterMovement = Namespace(ObjectClass='/Script/Engine.CharacterMovementComponent', ObjectFlags=2883617, ObjectName='CharMoveComp', bAutoActivate=False, bUseControllerDesiredRotation=True)
    CapsuleComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}, {'Channel': 'Vehicle', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=180, CapsuleRadius=180, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    AutoPossessAI = EAutoPossessAI::PlacedInWorldOrSpawned
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}, {'Channel': 'Vehicle', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=180, CapsuleRadius=180, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    
    def SpawnTimer(self):
        ReturnValue: bool = self.mEnemiesSpawned <= self.mEnemiesToSpawn
        if not ReturnValue:
            goto('L1193')
        ReturnValue_0: int32 = self.mEnemiesSpawned + 1
        Variable: int32 = ReturnValue_0
        self.mEnemiesSpawned = Variable
        # Label 148
        ReturnValue_1: Rotator = self.K2_GetActorRotation()
        ReturnValue_2: Vector = self.K2_GetActorLocation()
        ReturnValue_3: Vector = Vector(300, 300, 100)
        ReturnValue_4: Vector = RandomPointInBoundingBox(ReturnValue_2, ReturnValue_3)
        ReturnValue_5: Vector = ReturnValue_4 + Vector(0, 0, 100)
        ReturnValue_6: Transform = MakeTransform(ReturnValue_5, ReturnValue_1, Vector(1, 1, 1))
        
        ReturnValue_7: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, Char_BabyCrab, 2, None, Ref[ReturnValue_6])
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_7, "Instigator", self)
        ReturnValue_1 = self.K2_GetActorRotation()
        ReturnValue_2 = self.K2_GetActorLocation()
        ReturnValue_3 = Vector(300, 300, 100)
        ReturnValue_4 = RandomPointInBoundingBox(ReturnValue_2, ReturnValue_3)
        ReturnValue_5 = ReturnValue_4 + Vector(0, 0, 100)
        ReturnValue_6 = MakeTransform(ReturnValue_5, ReturnValue_1, Vector(1, 1, 1))
        
        ReturnValue_8: Ptr[Char_BabyCrab] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_7, Ref[ReturnValue_6])
        ReturnValue_9: Ptr[FGCreatureSpawner] = self.GetSpawner()
        ReturnValue_10: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_9)
        if not ReturnValue_10:
            goto('L981')
        ReturnValue_9 = self.GetSpawner()
        ReturnValue_9.AddCreature(ReturnValue_8)
        # Label 981
        ReturnValue_11: Vector = RandomUnitVector()
        ReturnValue_12: Vector = ReturnValue_11 * 1000
        ReturnValue_8.CharacterMovement.AddImpulse(ReturnValue_12, True)
        ReturnValue_13: TimerHandle = Default__KismetSystemLibrary.K2_SetTimer(self, "SpawnTimer", 0.10000000149011612, False)
        # End
        # Label 1193
        self.mHealthComponent.Kill()
    

    def PlaySpawnEffects(self):
        self.CapsuleComponent.SetCollisionEnabled(0)
        self.StaticMesh.SetCollisionEnabled(0)
        self.Mesh.SetCollisionEnabled(0)
        self.Mesh.SetVisibility(False, True)
        # Label 148
        self.EvokeParticles()
    

    def OnLoaded_380093F94E88F37148B05C99D8047F22(self, Loaded: Ptr[Object]):
        ExecuteUbergraph_Char_CrabHatcher.K2Node_CustomEvent_Loaded = Loaded #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_CrabHatcher(1936)
    

    def Damaged(self, DamagedActor: Ptr[Actor], Damage: float, DamageType: Const[Ptr[DamageType]], InstigatedBy: Ptr[Controller], DamageCauser: Ptr[Actor]):
        ExecuteUbergraph_Char_CrabHatcher.K2Node_CustomEvent_damagedActor = DamagedActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_CrabHatcher.K2Node_CustomEvent_Damage = Damage #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_CrabHatcher.K2Node_CustomEvent_damageType = DamageType #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_CrabHatcher.K2Node_CustomEvent_instigatedBy = InstigatedBy #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_CrabHatcher.K2Node_CustomEvent_damageCauser = DamageCauser #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_CrabHatcher(939)
    

    def SpawnCrabs(self):
        self.ExecuteUbergraph_Char_CrabHatcher(954)
    

    def StartExpanding(self):
        self.ExecuteUbergraph_Char_CrabHatcher(1569)
    

    def ReceiveActorBeginOverlap(self):
        ExecuteUbergraph_Char_CrabHatcher.K2Node_Event_OtherActor = OtherActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_CrabHatcher(1599)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Char_CrabHatcher(1703)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Char_CrabHatcher(1813)
    

    def ReceiveEndPlay(self):
        ExecuteUbergraph_Char_CrabHatcher.K2Node_Event_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_CrabHatcher(1888)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Char_CrabHatcher(1893)
    

    def EvokeParticles(self):
        self.ExecuteUbergraph_Char_CrabHatcher(1898)
    

    def ReceiveDied(self):
        self.ExecuteUbergraph_Char_CrabHatcher(1960)
    

    def ExecuteUbergraph_Char_CrabHatcher(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.SetLifeSpan(1)
        goto(ExecutionFlow.Pop())
        # Label 35
        OutputDelegate.BindUFunction(self, OnLoaded_380093F94E88F37148B05C99D8047F22)
        Default__KismetSystemLibrary.LoadAsset(self, self.mCrabParticles, OutputDelegate, LatentActionInfo(Linkage = -1, UUID = 696170389, ExecutionFunction = "ExecuteUbergraph_Char_CrabHatcher", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 148
        System: Ptr[ParticleSystem] = Cast[ParticleSystem](Variable)
        bSuccess: bool = System
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue1: Vector = self.StaticMesh.K2_GetComponentLocation()
        ReturnValue: Vector = ReturnValue1 + Vector(0, 0, 200)
        ReturnValue1_0: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, System, ReturnValue, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        self.mExplodingEggs_VFX = ReturnValue1_0
        # Label 432
        self.PlaySpawnEffects()
        self.SetDidSpawnCrabs(True)
        ReturnValue_0: bool = self.HasAuthority()
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        self.SpawnTimer()
        goto(ExecutionFlow.Pop())
        # Label 502
        ReturnValue_1: float = self.mGrowAnimation.GetPlayLength()
        self.SetAnimationLength(ReturnValue_1)
        self.Mesh.SetAnimation(self.mGrowAnimation)
        OutputDelegate1.BindUFunction(self, Damaged)
        self.OnTakeAnyDamage.AddUnique(OutputDelegate1)
        goto(ExecutionFlow.Pop())
        # Label 659
        self.ReceiveBeginPlay()
        ExecutionFlow.Push("L714")
        Default__FGBlueprintFunctionLibrary.AddGainSignificanceObjectToSignificanceManager(self, self, 5000)
        goto(ExecutionFlow.Pop())
        # Label 714
        ReturnValue_2: bool = self.GetDidSpawnCrabs()
        if not ReturnValue_2:
            goto('L897')
        self.Mesh.SetVisibility(False, True)
        self.CapsuleComponent.SetCollisionEnabled(0)
        self.StaticMesh.SetCollisionEnabled(0)
        self.Mesh.SetCollisionEnabled(0)
        goto(ExecutionFlow.Pop())
        # Label 897
        self.CharacterMovement.SetUpdatedComponent(None)
        goto('L502')
        self.SpawnCrabs()
        goto(ExecutionFlow.Pop())
        self.SpawnCrabs()
        
        ReturnValue_3: Ptr[Object] = Default__KismetSystemLibrary.Conv_SoftObjectReferenceToObject(Ref[self.mCrabParticles])
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_3)
        if not ReturnValue_4:
            goto('L35')
        
        ReturnValue_3 = Default__KismetSystemLibrary.Conv_SoftObjectReferenceToObject(Ref[self.mCrabParticles])
        System1: Ptr[ParticleSystem] = Cast[ParticleSystem](ReturnValue_3)
        bSuccess1: bool = System1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue1 = self.StaticMesh.K2_GetComponentLocation()
        ReturnValue = ReturnValue1 + Vector(0, 0, 200)
        ReturnValue_5: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, System1, ReturnValue, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        self.mExplodingEggs_VFX = ReturnValue_5
        goto('L432')
        # Label 1420
        ReturnValue_6: Ptr[SkeletalMeshComponent] = self.GetMesh3P()
        ReturnValue_7: Vector = ReturnValue_6.K2_GetComponentLocation()
        ReturnValue_8: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_E_Hatchery_Hive, ReturnValue_7, Rotator::FromPitchYawRoll(0, 0, 0))
        goto(ExecutionFlow.Pop())
        self.StartExpanding()
        goto('L1420')
        # Label 1584
        self.SpawnCrabs()
        goto(ExecutionFlow.Pop())
        ReturnValue_9: TSubclassOf[Actor] = Default__GameplayStatics.GetObjectClass(OtherActor)
        ReturnValue_10: bool = ClassIsChildOf(ReturnValue_9, FGWheeledVehicle)
        if not ReturnValue_10:
           goto(ExecutionFlow.Pop())
        goto('L1584')
        self.Mesh.SetComponentTickInterval(0)
        self.CharacterMovement.SetComponentTickInterval(0)
        goto(ExecutionFlow.Pop())
        # Label 1778
        Default__FGBlueprintFunctionLibrary.RemoveGainSignificanceObjectFromSignificanceManager(self, self)
        goto(ExecutionFlow.Pop())
        self.Mesh.SetComponentTickInterval(0.10000000149011612)
        self.CharacterMovement.SetComponentTickInterval(0.4000000059604645)
        goto(ExecutionFlow.Pop())
        goto('L1778')
        goto('L659')
        self.mExplodingEggs_VFX.Activate(False)
        goto(ExecutionFlow.Pop())
        Variable: Ptr[Object] = Loaded
        goto('L148')
        self.ReceiveDied()
        goto('L15')
    
