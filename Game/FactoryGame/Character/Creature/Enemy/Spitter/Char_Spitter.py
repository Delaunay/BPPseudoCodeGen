
from codegen.ue4_stub import *

from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Char_Spitter import ExecuteUbergraph_Char_Spitter.K2Node_ComponentBoundEvent_OtherComp
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Anim_Spitter import Anim_Spitter
from Script.Engine import SetComponentTickInterval
from Script.CoreUObject import Rotator
from Script.FactoryGame import AddGainSignificanceObjectToSignificanceManager
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Char_Spitter import ExecuteUbergraph_Char_Spitter.K2Node_Event_EndPlayReason
from Script.FactoryGame import GetCurrentAggroTarget
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Char_Spitter import ExecuteUbergraph_Char_Spitter.K2Node_ComponentBoundEvent_OtherBodyIndex
from Script.Engine import GetAnimInstance
from Script.Engine import SkeletalMeshComponent
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.Engine import SelectVector
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Char_Spitter import ExecuteUbergraph_Char_Spitter.K2Node_ComponentBoundEvent_OverlappedComponent
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Char_Spitter import ExecuteUbergraph_Char_Spitter.K2Node_ComponentBoundEvent_bFromSweep
from Script.FactoryGame import OnCurrentAggroTargetReplicated
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Char_Spitter import ExecuteUbergraph_Char_Spitter.K2Node_Event_DeltaSeconds
from Script.CoreUObject import Vector
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Char_Spitter import ExecuteUbergraph_Char_Spitter
from Script.Engine import GetRightVector
from Script.FactoryGame import FGEnemy
from Script.Engine import K2_GetActorRotation
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Char_Spitter import ExecuteUbergraph_Char_Spitter.K2Node_ComponentBoundEvent_SweepResult
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Script.Engine import Multiply_VectorVector
from Script.FactoryGame import RemoveGainSignificanceObjectFromSignificanceManager
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Char_Spitter import ExecuteUbergraph_Char_Spitter.K2Node_ComponentBoundEvent_OtherActor
from Script.Engine import AnimInstance
from Script.Engine import GetDirectionUnitVector
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import RandomBool

class Char_Spitter(FGEnemy):
    mIsStrafing: bool
    OnStrafeEnded: FMulticastScriptDelegate
    mStrafeHandler: TimerHandle
    mStrafeDirection: Vector
    mDoStrafeRight: bool
    mNavigationGenerationRadius = 7000
    mNavigationRemovalRadius = 8000
    mIsEnabled = 2
    mItemToDrop = NewObject[BP_AlphaSpitterParts]()
    mShouldOptimizeMeshWhenVisible = True
    mActualAIControllerClass = NewObject[Controller_Spitter]()
    mCanSpawnDuringDay = True
    mCanSpawnDuringNight = True
    mRotationSpeedMultiplier = 0.30000001192092896
    mEyeLocationComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 55, 'CapsuleRadius': 55, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 114.63198852539062, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='EyeLocationComponent')
    mSpawnWeight = 1
    mNeedsSpawner = True
    mSpawnDistance = -1
    mFeetNames = ['frontfootend_l', 'frontfootend_r', 'backfootend_l', 'backfootend_r']
    mFootstepEffect = [{'Surface': 0, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 1, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 4, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 2, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 3, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 5, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 6, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}]
    mFootstepAudioEvents = [{'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/_Shared/Audio/Play_E_Spitter_Footstep_Switch.Play_E_Spitter_Footstep_Switch'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/_Shared/Audio/Play_E_Spitter_Footstep_Switch.Play_E_Spitter_Footstep_Switch'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/_Shared/Audio/Play_E_Spitter_Footstep_Switch.Play_E_Spitter_Footstep_Switch'}, {'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/_Shared/Audio/Play_E_Spitter_Footstep_Switch.Play_E_Spitter_Footstep_Switch'}]
    mMaxFootstepParticleSpawnDistance = 2500
    mMaxFootstepDecalSpawnDistance = 1250
    mFootstepDecalSize = [{'X': -20, 'Y': -20, 'Z': -20}, {'X': 20, 'Y': 20, 'Z': 20}]
    mFootstepDecalLifetime = 10
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True, mCurrentHealth=60, mMaxHealth=60, mOnAdjustDamage=[0], mReplicateDamageEvents=True, mReplicateDeathEvents=True)
    mFallDamageCurve = Namespace(AssetPath='/Game/FactoryGame/Character/Player/FallDamageCurve.FallDamageCurve')
    mFallDamageDamageType = NewObject[DamageType_FallDamage]()
    mMaxDeathStayTime = 60
    mDeathRemoveCheckTime = 5
    mEnemyTargetDesirability = 1
    mTakeDamageSound = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Spitter/Audio/Play_E_Spitter_VO_Hurt.Play_E_Spitter_VO_Hurt')
    mDeathSound = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Spitter/Audio/Play_E_Spitter_VO_Die.Play_E_Spitter_VO_Die')
    mMinVehiclePushVelocityForRagdoll = 400
    mTimeToGetUpFromRagdoll = 3
    mMaxDistanceMovedToGetUp = 9
    mRagdollMeshLocBoneName = Pelvis
    mRagdollMeshPhysicsBoneName = Pelvis
    mSyncBodyMaxDistance = 6
    mWeakspotMultiplier = 2
    mNormalDamageMultiplier = 1
    Mesh = Namespace(AnimClass='/Game/FactoryGame/Character/Creature/Enemy/Spitter/Anim_Spitter.Anim_Spitter_C', AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 55, 'CapsuleRadius': 55, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 114.63198852539062, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, BodyInstance={'ObjectType': 2, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'CharacterMesh', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Pawn', 'Response': 0}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Vehicle', 'Response': 0}, {'Channel': 'WeaponInstantHit', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 0, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CachedMaxDrawDistance=17000, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='CharacterMesh0', RelativeLocation={'X': 0, 'Y': 0, 'Z': -55}, RelativeRotation={'Pitch': 0, 'Yaw': -90, 'Roll': 0}, SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Character/Creature/Enemy/Spitter/Mesh/Spitter.Spitter'}, VisibilityBasedAnimTickOption='EVisibilityBasedAnimTickOption::AlwaysTickPose', bCastCapsuleDirectShadow=True, bCastCapsuleIndirectShadow=True, bReceivesDecals=False)
    CharacterMovement = Namespace(Mass=400, MaxStepHeight=100, ObjectClass='/Script/Engine.CharacterMovementComponent', ObjectFlags=2883617, ObjectName='CharMoveComp', RotationRate={'Pitch': 0, 'Yaw': 260, 'Roll': 0}, WalkableFloorAngle=50, WalkableFloorZ=0.6427876353263855, bUseAccelerationForPaths=True, bUseControllerDesiredRotation=True)
    CapsuleComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 114.63198852539062, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=55, CapsuleRadius=55, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    AutoPossessAI = EAutoPossessAI::PlacedInWorldOrSpawned
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 114.63198852539062, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=55, CapsuleRadius=55, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    
    def GetAttackLocation(self):
        ReturnValue: Ptr[SkeletalMeshComponent] = self.GetMesh3P()
        ReturnValue_0: Vector = ReturnValue.GetSocketLocation("fireSocket")
        ReturnValue_1: Vector = ReturnValue_0
    

    def UpdateStrafeDirection(self):
        ReturnValue: Ptr[Actor] = self.GetCurrentAggroTarget()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L279')
        # Label 85
        ReturnValue_1: Rotator = self.K2_GetActorRotation()
        ReturnValue_2: Vector = GetRightVector(ReturnValue_1)
        ReturnValue_3: Vector = ReturnValue_2 * -1
        ReturnValue_4: Vector = SelectVector(ReturnValue_2, ReturnValue_3, self.mDoStrafeRight)
        self.mStrafeDirection = ReturnValue_4
        # End
        # Label 279
        self.StopStrafe()
    

    def StopStrafe(self):
        self.mIsStrafing = False
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mStrafeHandler])
        self.OnStrafeEnded.ProcessMulticastDelegate()
    

    def DoStrafe(self):
        self.AddMovementInput(self.mStrafeDirection, 1, False)
    

    def StartStrafe(self):
        self.mIsStrafing = True
        OutputDelegate.BindUFunction(self, UpdateStrafeDirection)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.10000000149011612, True)
        self.mStrafeHandler = ReturnValue
        ReturnValue_0: bool = RandomBool()
        self.mDoStrafeRight = ReturnValue_0
    

    def ReceiveTick(self):
        ExecuteUbergraph_Char_Spitter.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Spitter(127)
    

    def OnCurrentAggroTargetReplicated(self):
        self.ExecuteUbergraph_Char_Spitter(530)
    

    def BndEvt__Capsule_K2Node_ComponentBoundEvent_0_ComponentBeginOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32, bFromSweep: bool, SweepResult: Const[Ref[HitResult]]):
        ExecuteUbergraph_Char_Spitter.K2Node_ComponentBoundEvent_OverlappedComponent = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Spitter.K2Node_ComponentBoundEvent_OtherActor = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Spitter.K2Node_ComponentBoundEvent_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Spitter.K2Node_ComponentBoundEvent_OtherBodyIndex = OtherBodyIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Spitter.K2Node_ComponentBoundEvent_bFromSweep = bFromSweep #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Spitter.K2Node_ComponentBoundEvent_SweepResult = SweepResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Spitter(545)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Char_Spitter(850)
    

    def ReceiveEndPlay(self):
        ExecuteUbergraph_Char_Spitter.K2Node_Event_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Spitter(894)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Char_Spitter(933)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Char_Spitter(1017)
    

    def ExecuteUbergraph_Char_Spitter(self):
        # Label 10
        self.Mesh.SetComponentTickInterval(0)
        # End
        # Label 52
        if not self.mIsStrafing:
            goto('L1022')
        self.DoStrafe()
        # End
        # Label 85
        self.Mesh.SetComponentTickInterval(0)
        # End
        goto('L52')
        # Label 132
        ReturnValue: Ptr[SkeletalMeshComponent] = self.GetMesh3P()
        ReturnValue_0: Ptr[AnimInstance] = ReturnValue.GetAnimInstance()
        Spitter: Ptr[Anim_Spitter] = Cast[Anim_Spitter](ReturnValue_0)
        bSuccess: bool = Spitter
        if not bSuccess:
            goto('L1022')
        ReturnValue_1: Ptr[Actor] = self.GetCurrentAggroTarget()
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_1)
        Spitter.mHasAggroTarget = ReturnValue_2
        # End
        # Label 394
        ReturnValue = self.GetMesh3P()
        ReturnValue_0 = ReturnValue.GetAnimInstance()
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue1:
            goto('L1022')
        goto('L132')
        self.OnCurrentAggroTargetReplicated()
        goto('L394')
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](OtherActor)
        bSuccess1: bool = Player
        if not bSuccess1:
            goto('L1022')
        ReturnValue_3: Vector = self.K2_GetActorLocation()
        ReturnValue1_0: Vector = Player.K2_GetActorLocation()
        ReturnValue_4: Vector = GetDirectionUnitVector(ReturnValue_3, ReturnValue1_0)
        ReturnValue_5: Vector = Multiply_VectorVector(ReturnValue_4, Vector(500, 500, 500))
        Player.LaunchCharacter(ReturnValue_5, True, True)
        # End
        Default__FGBlueprintFunctionLibrary.AddGainSignificanceObjectToSignificanceManager(self, self, 10000)
        # End
        Default__FGBlueprintFunctionLibrary.RemoveGainSignificanceObjectFromSignificanceManager(self, self)
        # End
        self.CharacterMovement.SetComponentTickInterval(0)
        goto('L85')
        # Label 975
        self.CharacterMovement.SetComponentTickInterval(0.10000000149011612)
        goto('L10')
        goto('L975')
    

    def OnStrafeEnded__DelegateSignature(self):
        pass
    
