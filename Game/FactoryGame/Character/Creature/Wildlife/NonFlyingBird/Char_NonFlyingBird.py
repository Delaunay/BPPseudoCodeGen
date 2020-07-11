
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Char_NonFlyingBird import ExecuteUbergraph_Char_NonFlyingBird.K2Node_Event_damagedActor
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Anim_NonFlyingBird import Anim_NonFlyingBird
from Script.Engine import Controller
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Char_NonFlyingBird import ExecuteUbergraph_Char_NonFlyingBird.K2Node_Event_Hit
from Script.Engine import SetComponentTickInterval
from Script.FactoryGame import AddGainSignificanceObjectToSignificanceManager
from Script.CoreUObject import Rotator
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Char_NonFlyingBird import ExecuteUbergraph_Char_NonFlyingBird.K2Node_Event_damageType
from Script.FactoryGame import FGCreature
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Char_NonFlyingBird import ExecuteUbergraph_Char_NonFlyingBird.K2Node_Event_damageCauser
from Script.Engine import GetAnimInstance
from Script.Engine import SelectFloat
from Script.Engine import ReceiveTick
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Audio.Stop_E_NonFlyingBird_Walk_Rustling import Stop_E_NonFlyingBird_Walk_Rustling
from Script.Engine import GetController
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Controller_NonFlyingBird import Controller_NonFlyingBird
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Char_NonFlyingBird import ExecuteUbergraph_Char_NonFlyingBird
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Char_NonFlyingBird import ExecuteUbergraph_Char_NonFlyingBird.K2Node_Event_damageAmount
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Char_NonFlyingBird import ExecuteUbergraph_Char_NonFlyingBird.K2Node_Event_DeltaSeconds
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Char_NonFlyingBird import ExecuteUbergraph_Char_NonFlyingBird.K2Node_Event_instigatedBy
from Script.FactoryGame import NotifyOnTakeDamage
from Script.Engine import OnLanded
from Script.Engine import FlushNetDormancy
from Script.CoreUObject import Vector
from Script.Engine import K2_GetActorRotation
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Char_NonFlyingBird import ExecuteUbergraph_Char_NonFlyingBird.K2Node_Event_EndPlayReason
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Audio.Stop_E_NonFlyingBird_Fly import Stop_E_NonFlyingBird_Fly
from Script.Engine import GetForwardVector
from Script.FactoryGame import RemoveGainSignificanceObjectFromSignificanceManager
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.FactoryGame import ReceiveDied
from Script.Engine import SkeletalMeshComponent

class Char_NonFlyingBird(FGCreature):
    OnLandedDelegate: FMulticastScriptDelegate
    mIsLuring: bool
    mNavigationGenerationRadius = 7000
    mNavigationRemovalRadius = 8000
    mIsEnabled = 2
    mShouldOptimizeMeshWhenVisible = True
    mActualAIControllerClass = NewObject[Controller_NonFlyingBird]()
    mCanSpawnDuringDay = True
    mCanSpawnDuringNight = True
    mRotationSpeedMultiplier = 0.30000001192092896
    mEyeLocationComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 50.2294921875, 'CapsuleRadius': 34, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='EyeLocationComponent')
    mSpawnWeight = 1
    mNeedsSpawner = True
    mSpawnDistance = -1
    mFeetNames = ['foot_lSocket', 'foot_rSocket']
    mMaxFootstepParticleSpawnDistance = 2500
    mMaxFootstepDecalSpawnDistance = 1250
    mFootstepDecalSize = [{'X': -20, 'Y': -20, 'Z': -20}, {'X': 20, 'Y': 20, 'Z': 20}]
    mFootstepDecalLifetime = 10
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True, mCurrentHealth=10, mMaxHealth=10, mOnAdjustDamage=[0], mReplicateDamageEvents=True, mReplicateDeathEvents=True)
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
    Mesh = Namespace(AnimClass='/Game/FactoryGame/Character/Creature/Wildlife/NonFlyingBird/Anim_NonFlyingBird.Anim_NonFlyingBird_C', AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 50.2294921875, 'CapsuleRadius': 34, 'bDynamicObstacle': True, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, BodyInstance={'ObjectType': 5, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Ragdoll', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Pawn', 'Response': 0}, {'Channel': 'WeaponInstantHit', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CachedMaxDrawDistance=11250, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='CharacterMesh0', RelativeLocation={'X': 0, 'Y': 0, 'Z': -50}, RelativeRotation={'Pitch': 0, 'Yaw': -90, 'Roll': 0}, SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Character/Creature/Wildlife/NonFlyingBird/Mesh/NonFlyingBird.NonFlyingBird'}, VisibilityBasedAnimTickOption='EVisibilityBasedAnimTickOption::AlwaysTickPose', bReceivesDecals=False)
    CharacterMovement = Namespace(AirControl=0.10000000149011612, GravityScale=0.10000000149011612, JumpZVelocity=600, NavMeshProjectionInterval=0.30000001192092896, ObjectClass='/Script/Engine.CharacterMovementComponent', ObjectFlags=2883617, ObjectName='CharMoveComp', RotationRate={'Pitch': 0, 'Yaw': 200, 'Roll': 0}, bProjectNavMeshWalking=True, bUseAccelerationForPaths=True, bUseControllerDesiredRotation=True)
    CapsuleComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=50.2294921875, CapsuleRadius=34, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    AutoPossessAI = EAutoPossessAI::PlacedInWorldOrSpawned
    AIControllerClass = NewObject[Controller_NonFlyingBird]()
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, CapsuleHalfHeight=50.2294921875, CapsuleRadius=34, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bDynamicObstacle=True, bShouldUpdatePhysicsVolume=True)
    
    def OnRep_mIsLuring(self):
        ReturnValue: Ptr[SkeletalMeshComponent] = self.GetMesh3P()
        ReturnValue_0: Ptr[AnimInstance] = ReturnValue.GetAnimInstance()
        Bird: Ptr[Anim_NonFlyingBird] = Cast[Anim_NonFlyingBird](ReturnValue_0)
        bSuccess: bool = Bird
        if not bSuccess:
            goto('L186')
        Bird.mIsLuring = self.mIsLuring
    

    def SetLuring(self, isLuring: bool):
        self.FlushNetDormancy()
        self.mIsLuring = isLuring
        self.OnRep_mIsLuring()
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Char_NonFlyingBird(10)
    

    def ReceiveTick(self):
        ExecuteUbergraph_Char_NonFlyingBird.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_NonFlyingBird(54)
    

    def TryToJump(self):
        self.ExecuteUbergraph_Char_NonFlyingBird(276)
    

    def OnLanded(self):
        ExecuteUbergraph_Char_NonFlyingBird.K2Node_Event_Hit = Hit #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_NonFlyingBird(652)
    

    def ReceiveDied(self):
        self.ExecuteUbergraph_Char_NonFlyingBird(696)
    

    def NotifyOnTakeDamage(self):
        ExecuteUbergraph_Char_NonFlyingBird.K2Node_Event_damagedActor = DamagedActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_NonFlyingBird.K2Node_Event_damageAmount = damageAmount #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_NonFlyingBird.K2Node_Event_damageType = DamageType #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_NonFlyingBird.K2Node_Event_instigatedBy = InstigatedBy #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_NonFlyingBird.K2Node_Event_damageCauser = DamageCauser #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_NonFlyingBird(817)
    

    def ReceiveEndPlay(self):
        ExecuteUbergraph_Char_NonFlyingBird.K2Node_Event_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_NonFlyingBird(1012)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Char_NonFlyingBird(1051)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Char_NonFlyingBird(1130)
    

    def ExecuteUbergraph_Char_NonFlyingBird(self):
        Default__FGBlueprintFunctionLibrary.AddGainSignificanceObjectToSignificanceManager(self, self, 10000)
        # End
        self.ReceiveTick(DeltaSeconds)
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(self.CharacterMovement.Velocity)
        ReturnValue: bool = Z <= 0
        ReturnValue_0: float = SelectFloat(0.05000000074505806, 0.30000001192092896, ReturnValue)
        self.CharacterMovement.GravityScale = ReturnValue_0
        # End
        ReturnValue_1: bool = self.CharacterMovement.IsMovingOnGround()
        if not ReturnValue_1:
            goto('L1204')
        ReturnValue_2: Vector = Vector(0, 0, self.CharacterMovement.JumpZVelocity)
        ReturnValue_3: Rotator = self.K2_GetActorRotation()
        ReturnValue_4: Vector = GetForwardVector(ReturnValue_3)
        ReturnValue_5: Vector = ReturnValue_4 * 400
        ReturnValue_6: Vector = ReturnValue_5 + ReturnValue_2
        self.CharacterMovement.Velocity = ReturnValue_6
        self.CharacterMovement.SetMovementMode(3, 0)
        # End
        
        Hit = None
        self.OnLanded(Ref[Hit])
        self.OnLandedDelegate.ProcessMulticastDelegate(self)
        # End
        self.ReceiveDied()
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_NonFlyingBird_Walk_Rustling, self, True)
        ReturnValue_7: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_NonFlyingBird_Fly, self, True)
        # End
        self.NotifyOnTakeDamage(damagedActor, damageAmount, damageType, instigatedBy, damageCauser)
        ReturnValue_8: Ptr[Controller] = self.GetController()
        Bird: Ptr[Controller_NonFlyingBird] = Cast[Controller_NonFlyingBird](ReturnValue_8)
        bSuccess: bool = Bird
        if not bSuccess:
            goto('L1204')
        Bird.StartPanic()
        # End
        Default__FGBlueprintFunctionLibrary.RemoveGainSignificanceObjectFromSignificanceManager(self, self)
        # End
        self.Mesh.SetComponentTickInterval(0)
        self.CharacterMovement.SetComponentTickInterval(0)
        # End
        self.Mesh.SetComponentTickInterval(0)
        self.CharacterMovement.SetComponentTickInterval(0.20000000298023224)
    

    def OnLandedDelegate__DelegateSignature(self, selfPawn: Ptr[Char_NonFlyingBird]):
        pass
    
