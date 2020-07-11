
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.Enemy.Stinger.BigStinger.Char_EliteStinger import ExecuteUbergraph_Char_EliteStinger.K2Node_CustomEvent_damageCauser
from Game.FactoryGame.Character.Creature.Enemy.Stinger.BigStinger.Char_EliteStinger import ExecuteUbergraph_Char_EliteStinger.K2Node_CustomEvent_damagedActor
from Script.Engine import FinishSpawningActor
from Script.Engine import Delay
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Character.Creature.Enemy.Stinger.BigStinger.Char_EliteStinger import ExecuteUbergraph_Char_EliteStinger.K2Node_CustomEvent_Damage
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Creature.Enemy.Stinger.BigStinger.Char_EliteStinger import ExecuteUbergraph_Char_EliteStinger
from Script.Engine import GreaterEqual_FloatFloat
from Script.Engine import RandomFloat
from Script.Engine import BeginDeferredActorSpawnFromClass
from Game.FactoryGame.Character.Creature.Enemy.Stinger.BigStinger.Char_EliteStinger import ExecuteUbergraph_Char_EliteStinger.K2Node_CustomEvent_damageType
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import ReceiveBeginPlay
from Game.FactoryGame.Character.Creature.Enemy.Stinger.Char_Stinger import Char_Stinger
from Script.Engine import Default__GameplayStatics
from Script.Engine import K2_GetComponentToWorld
from Script.FactoryGame import GetCurrentHealth
from Script.Engine import Actor
from Game.FactoryGame.Character.Creature.Enemy.Stinger.BigStinger.Char_EliteStinger import ExecuteUbergraph_Char_EliteStinger.K2Node_CustomEvent_instigatedBy
from Script.CoreUObject import Transform
from Game.FactoryGame.Character.Creature.Enemy.Stinger.BigStinger.BP_StingerGas import BP_StingerGas

class Char_EliteStinger(Char_Stinger):
    GasOnHitChance: float = 1
    OffCooldown: bool = True
    mNavigationGenerationRadius = 7000
    mNavigationRemovalRadius = 8000
    mIsEnabled = 2
    mItemToDrop = NewObject[BP_EliteStingerParts]()
    mShouldOptimizeMeshWhenVisible = True
    mCanSpawnDuringNight = True
    mEyeLocationComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 128, 'CapsuleRadius': 128, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 114.63198852539062, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'RelativeScale3D': {'X': 1.5, 'Y': 1.5, 'Z': 1.5}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='EyeLocationComponent', RelativeLocation={'X': 80, 'Y': 0, 'Z': 0})
    mSpawnWeight = 1
    mNeedsSpawner = True
    mSpawnDistance = -1
    mMaxFootstepParticleSpawnDistance = 2500
    mMaxFootstepDecalSpawnDistance = 1250
    mFootstepDecalSize = [{'X': -20, 'Y': -20, 'Z': -20}, {'X': 20, 'Y': 20, 'Z': 20}]
    mFootstepDecalLifetime = 10
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True, mCurrentHealth=100, mMaxHealth=100, mOnAdjustDamage=[0], mReplicateDamageEvents=True, mReplicateDeathEvents=True)
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
    Mesh = Namespace(AnimClass='/Game/FactoryGame/Character/Creature/Enemy/Stinger/Anim_Stinger.Anim_Stinger_C', AnimationData={'AnimToPlay': {'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Stinger/Animation/Idle_01.Idle_01'}, 'bSavedLooping': True, 'bSavedPlaying': True, 'SavedPosition': 0, 'SavedPlayRate': 1}, AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 128, 'CapsuleRadius': 128, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 114.63198852539062, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'RelativeScale3D': {'X': 1.5, 'Y': 1.5, 'Z': 1.5}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, BodyInstance={'ObjectType': 2, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'CharacterMesh', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Pawn', 'Response': 0}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Vehicle', 'Response': 0}, {'Channel': 'WeaponInstantHit', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 0, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='CharacterMesh0', OverrideMaterials=[{'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Stinger/Material/Stinger_Green.Stinger_Green'}], RelativeLocation={'X': -154.33364868164062, 'Y': -1.3333420753479004, 'Z': -130}, RelativeRotation={'Pitch': 0, 'Yaw': -90, 'Roll': 0}, SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Stinger/Mesh/Stinger.Stinger'}, VisibilityBasedAnimTickOption='EVisibilityBasedAnimTickOption::AlwaysTickPose', bEnableUpdateRateOptimizations=False, bReceivesDecals=False)
    CharacterMovement = Namespace(BrakingDecelerationWalking=12000, BrakingFrictionFactor=8, FallingLateralFriction=6, JumpZVelocity=800, Mass=400, MaxAcceleration=12000, MaxStepHeight=400, MaxWalkSpeed=2700, ObjectClass='/Script/Engine.CharacterMovementComponent', ObjectFlags=2883617, ObjectName='CharMoveComp', RotationRate={'Pitch': 0, 'Yaw': 220, 'Roll': 0}, WalkableFloorAngle=50, WalkableFloorZ=0.6427876353263855, bUseControllerDesiredRotation=True)
    CapsuleComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 114.63198852539062, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=128, CapsuleRadius=128, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', RelativeScale3D={'X': 1.5, 'Y': 1.5, 'Z': 1.5}, bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    AIControllerClass = NewObject[Controller_StingerElite]()
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 114.63198852539062, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=128, CapsuleRadius=128, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', RelativeScale3D={'X': 1.5, 'Y': 1.5, 'Z': 1.5}, bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Char_EliteStinger(594)
    

    def SpawnGas(self):
        self.ExecuteUbergraph_Char_EliteStinger(917)
    

    def OnTakeAnyDamage_Event_0(self, DamagedActor: Ptr[Actor], Damage: float, DamageType: Const[Ptr[DamageType]], InstigatedBy: Ptr[Controller], DamageCauser: Ptr[Actor]):
        ExecuteUbergraph_Char_EliteStinger.K2Node_CustomEvent_damagedActor = DamagedActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_EliteStinger.K2Node_CustomEvent_Damage = Damage #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_EliteStinger.K2Node_CustomEvent_damageType = DamageType #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_EliteStinger.K2Node_CustomEvent_instigatedBy = InstigatedBy #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_EliteStinger.K2Node_CustomEvent_damageCauser = DamageCauser #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_EliteStinger(948)
    

    def ExecuteUbergraph_Char_EliteStinger(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue: Transform = self.Scene.K2_GetComponentToWorld()
        
        ReturnValue_0: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_StingerGas, 0, None, Ref[ReturnValue])
        ReturnValue = self.Scene.K2_GetComponentToWorld()
        
        ReturnValue_1: Ptr[BP_StingerGas] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_0, Ref[ReturnValue])
        Default__KismetSystemLibrary.Delay(self, 2, LatentActionInfo(Linkage = 316, UUID = 1091680037, ExecutionFunction = "ExecuteUbergraph_Char_EliteStinger", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.CharacterMovement.MaxWalkSpeed = 2700
        self.ParticleSystem.Deactivate()
        self.ParticleSystem1.Deactivate()
        self.ParticleSystem2.Deactivate()
        self.ParticleSystem3.Deactivate()
        Default__KismetSystemLibrary.Delay(self, 5, LatentActionInfo(Linkage = 582, UUID = -424212051, ExecutionFunction = "ExecuteUbergraph_Char_EliteStinger", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.OffCooldown = True
        goto(ExecutionFlow.Pop())
        self.ReceiveBeginPlay()
        OutputDelegate.BindUFunction(self, OnTakeAnyDamage_Event_0)
        self.OnTakeAnyDamage.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        # Label 647
        self.CharacterMovement.MaxWalkSpeed = 2700
        self.ParticleSystem1.Activate(True)
        self.ParticleSystem2.Activate(True)
        self.ParticleSystem3.Activate(True)
        self.ParticleSystem.Activate(True)
        Default__KismetSystemLibrary.Delay(self, 1, LatentActionInfo(Linkage = 15, UUID = -193545620, ExecutionFunction = "ExecuteUbergraph_Char_EliteStinger", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.OffCooldown = False
        goto('L647')
        # Label 933
        self.SpawnGas()
        goto(ExecutionFlow.Pop())
        ReturnValue_2: float = RandomFloat()
        ReturnValue_3: bool = GreaterEqual_FloatFloat(self.GasOnHitChance, ReturnValue_2)
        ReturnValue_4: bool = ReturnValue_3 and self.OffCooldown
        ReturnValue_5: float = self.mHealthComponent.GetCurrentHealth()
        ReturnValue_6: bool = ReturnValue_5 > 0
        ReturnValue1: bool = ReturnValue_4 and ReturnValue_6
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        goto('L933')
    
