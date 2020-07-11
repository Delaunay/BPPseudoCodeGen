
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import FinishSpawningActor
from Script.Engine import Delay
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterProjectileVolley import BP_SpitterProjectileVolley
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Script.Engine import SpawnEmitterAtLocation
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterProjectile import ExecuteUbergraph_BP_SpitterProjectile.K2Node_ComponentBoundEvent_bReset
from Script.Engine import GetTransform
from Script.Engine import VSize
from Script.AkAudio import PostAkEventAtLocation
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterProjectile import ExecuteUbergraph_BP_SpitterProjectile.K2Node_ComponentBoundEvent_Component
from Script.Engine import BreakTransform
from Game.FactoryGame.VFX.Character.Creature.Spitter.P_SpitImpact_01 import P_SpitImpact_01
from Script.Engine import ReceiveBeginPlay
from Script.Engine import LatentActionInfo
from Script.Engine import SphereComponent
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterProjectile import ExecuteUbergraph_BP_SpitterProjectile
from Script.Engine import GetPlayerPawn
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import HasAuthority
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Stop_E_Spitter_Projectile_Loop import Stop_E_Spitter_Projectile_Loop
from Script.Engine import ReceiveTick
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Play_E_Spitter_Projectile_Land import Play_E_Spitter_Projectile_Land
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterProjectile import ExecuteUbergraph_BP_SpitterProjectile.K2Node_Event_DeltaSeconds
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.Engine import DegreesToRadians
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Play_E_Spitter_Projectile_Loop import Play_E_Spitter_Projectile_Loop
from Script.Engine import EqualEqual_IntInt
from Script.Engine import CurveFloat
from Script.Engine import Default__GameplayStatics
from Script.Engine import FlushNetDormancy
from Script.FactoryGame import GetCollisionSphere
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.Engine import Normal
from Script.FactoryGame import GetProjectileTargetLocation
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import MakeTransform
from Script.FactoryGame import SetInitialVelocity
from Script.Engine import Actor
from Script.Engine import ParticleSystemComponent
from Script.Engine import K2_GetActorLocation
from Script.Engine import Multiply_VectorVector
from Script.Engine import GetOwner
from Script.AkAudio import AkComponent
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.FactoryGame import IsAliveAndWell
from Script.Engine import GetFloatValue
from Script.FactoryGame import FGProjectile
from Script.CoreUObject import Transform
from Script.Engine import RandomUnitVectorInConeInRadians

class BP_SpitterProjectile(FGProjectile):
    mSpeedAdjustment: float = 2000
    mDoSplit: bool = True
    mNumberofSplitProjectiles: int32 = 4
    mSplitConeHalfAngle: float
    CurveProjectileZ: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Spitter/Curve_SpitterProjectileZ.Curve_SpitterProjectileZ')
    CurveProjectileSpeed: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Spitter/Curve_SpitterProjectileSpeed.Curve_SpitterProjectileSpeed')
    mTargetPawn: Ptr[Pawn]
    CurveProjectileAngle: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Spitter/Curve_SpitterProjectileAngle.Curve_SpitterProjectileAngle')
    DistanceToTarget: float
    CurveProjectileHeight: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Spitter/Curve_SpitterProjectileHeight.Curve_SpitterProjectileHeight')
    mAdjusted_Cone_Angle: float
    mSubtitleTimer: TimerHandle
    mProjectileData = Namespace(CanTriggerExplodeBySameClass=True, DamageType='/Game/FactoryGame/Character/Creature/Enemy/Spitter/DamageType_SpitterProjectile.DamageType_SpitterProjectile_C', DamageTypeExplode='/Script/FactoryGame.FGDamageType', ExplodeAtEndOfLife=False, ExplosionDamage=40, ExplosionRadius=250, ImpactDamage=20, ProjectileClass='/Game/FactoryGame/Character/Creature/Enemy/Spitter/BP_SpitterProjectile.BP_SpitterProjectile_C', ProjectileLifeSpan=10, ProjectileStickSpan=0, ShouldExplodeOnImpact=True)
    mCollisionComp = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 14, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Projectile', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', OnComponentHit=0, RelativeScale3D={'X': 1.2000000476837158, 'Y': 1.2000000476837158, 'Z': 1.2000000476837158}, SphereRadius=16, bCanEverAffectNavigation=False)
    mProjectileMovement = Namespace(InitialSpeed=250, MaxSpeed=4000, ObjectClass='/Script/Engine.ProjectileMovementComponent', ObjectFlags=2883617, ObjectName='ProjectileComp', Velocity={'X': 0, 'Y': 0, 'Z': 1}, bAutoActivate=False, bRotationFollowsVelocity=True)
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicateMovement = True
    bReplicates = True
    RemoteRole = 1
    InitialLifeSpan = 3
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 14, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Projectile', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', OnComponentHit=0, RelativeScale3D={'X': 1.2000000476837158, 'Y': 1.2000000476837158, 'Z': 1.2000000476837158}, SphereRadius=16, bCanEverAffectNavigation=False)
    
    def GetNewTarget(self):
        ExecutionFlow.Push("L1259")
        Variable: int32 = 0
        # Label 28
        ReturnValue: bool = Variable <= 8
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1185")
        ReturnValue_0: Ptr[Pawn] = Default__GameplayStatics.GetPlayerPawn(self, Variable)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        ReturnValue_0 = Default__GameplayStatics.GetPlayerPawn(self, Variable)
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_0)
        bSuccess: bool = Player
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_1: bool = Player.IsAliveAndWell()
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue_0 = Default__GameplayStatics.GetPlayerPawn(self, Variable)
        ReturnValue2: Vector = ReturnValue_0.K2_GetActorLocation()
        ReturnValue3: Vector = self.K2_GetActorLocation()
        ReturnValue1_0: Vector = Subtract_VectorVector(ReturnValue2, ReturnValue3)
        ReturnValue1_1: float = VSize(ReturnValue1_0)
        ReturnValue_2: bool = ReturnValue1_1 <= 9999
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(self.mTargetPawn)
        if not ReturnValue_3:
            goto('L1113')
        ReturnValue_4: Vector = self.mTargetPawn.K2_GetActorLocation()
        ReturnValue1_2: Vector = self.K2_GetActorLocation()
        ReturnValue_0 = Default__GameplayStatics.GetPlayerPawn(self, Variable)
        ReturnValue_5: Vector = Subtract_VectorVector(ReturnValue_4, ReturnValue1_2)
        ReturnValue_6: float = VSize(ReturnValue_5)
        ReturnValue2 = ReturnValue_0.K2_GetActorLocation()
        ReturnValue3 = self.K2_GetActorLocation()
        ReturnValue1_0 = Subtract_VectorVector(ReturnValue2, ReturnValue3)
        ReturnValue1_1 = VSize(ReturnValue1_0)
        ReturnValue_7: bool = ReturnValue1_1 <= ReturnValue_6
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        # Label 1113
        ReturnValue_0 = Default__GameplayStatics.GetPlayerPawn(self, Variable)
        self.mTargetPawn = ReturnValue_0
        goto(ExecutionFlow.Pop())
        # Label 1185
        ReturnValue_8: int32 = Variable + 1
        Variable = ReturnValue_8
        goto('L28')
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_SpitterProjectile(1774)
    

    def SplitProjectile(self):
        self.ExecuteUbergraph_BP_SpitterProjectile(1914)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_SpitterProjectile.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SpitterProjectile(1997)
    

    def BndEvt__mProjectileMovement_K2Node_ComponentBoundEvent_0_ActorComponentActivatedSignature__DelegateSignature(self, component: Ptr[ActorComponent], bReset: bool):
        ExecuteUbergraph_BP_SpitterProjectile.K2Node_ComponentBoundEvent_Component = component #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SpitterProjectile.K2Node_ComponentBoundEvent_bReset = bReset #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SpitterProjectile(2239)
    

    def PlayExplosionEffects(self):
        self.ExecuteUbergraph_BP_SpitterProjectile(3608)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_BP_SpitterProjectile(3866)
    

    def ExecuteUbergraph_BP_SpitterProjectile(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.FlushNetDormancy()
        self.mDoSplit = False
        Variable: int32 = 0
        # Label 59
        ReturnValue: int32 = self.mNumberofSplitProjectiles - 1
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L1418')
        ExecutionFlow.Push("L1551")
        ReturnValue_1: bool = EqualEqual_IntInt(Variable, 0)
        if not ReturnValue_1:
            goto('L1625')
        # Label 206
        ReturnValue_2: Transform = self.GetTransform()
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_2], Ref[Location], Ref[Rotation], Ref[Scale])
        ReturnValue_3: Transform = MakeTransform(Location, Rotation, Scale)
        ReturnValue_4: Ptr[Actor] = self.GetOwner()
        
        ReturnValue_5: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_SpitterProjectileVolley, 0, ReturnValue_4, Ref[ReturnValue_3])
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_5, "Instigator", self.Instigator)
        ReturnValue_2 = self.GetTransform()
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_2], Ref[Location], Ref[Rotation], Ref[Scale])
        ReturnValue_3 = MakeTransform(Location, Rotation, Scale)
        
        ReturnValue_6: Ptr[BP_SpitterProjectileVolley] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_5, Ref[ReturnValue_3])
        ReturnValue_7: Vector = self.K2_GetActorLocation()
        ReturnValue_8: float = 10 / self.mSplitConeHalfAngle
        ReturnValue_9: float = DegreesToRadians(self.mSplitConeHalfAngle)
        ReturnValue_10: Vector = Vector(1, 1, ReturnValue_8)
        ReturnValue6: Vector = self.mTargetPawn.K2_GetActorLocation()
        ReturnValue3: Vector = Subtract_VectorVector(ReturnValue6, ReturnValue_7)
        ReturnValue1: Vector = Normal(ReturnValue3, 9.999999747378752e-05)
        ReturnValue_11: Vector = RandomUnitVectorInConeInRadians(ReturnValue1, ReturnValue_9)
        ReturnValue_12: Vector = Multiply_VectorVector(ReturnValue_11, ReturnValue_10)
        ReturnValue3_0: float = self.CurveProjectileHeight.GetFloatValue(self.DistanceToTarget)
        ReturnValue3_1: Vector = Vector(0, 0, ReturnValue3_0)
        ReturnValue1_0: Vector = ReturnValue_12 + ReturnValue3_1
        ReturnValue1_1: Vector = ReturnValue1_0 * self.mSpeedAdjustment
        ReturnValue_6.mProjectileMovement.Velocity = ReturnValue1_1
        ReturnValue_6.SetInitialVelocity(ReturnValue_6.mProjectileMovement.Velocity)
        goto(ExecutionFlow.Pop())
        # Label 1418
        ReturnValue5: Vector = self.K2_GetActorLocation()
        ReturnValue_13: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_SpitImpact_01, ReturnValue5, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        self.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        # Label 1551
        ReturnValue_14: int32 = Variable + 1
        Variable = ReturnValue_14
        goto('L59')
        # Label 1625
        self.mSplitConeHalfAngle = self.mAdjusted_Cone_Angle
        goto('L206')
        
        # Label 1657
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mSubtitleTimer])
        goto(ExecutionFlow.Pop())
        # Label 1700
        self.FlushNetDormancy()
        self.mDoSplit = False
        goto(ExecutionFlow.Pop())
        self.mProjectileMovement.Activate(False)
        self.GetNewTarget()
        goto(ExecutionFlow.Pop())
        self.ReceiveBeginPlay()
        ReturnValue_15: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Spitter_Projectile_Loop, self, True)
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 1722, UUID = -1595193506, ExecutionFunction = "ExecuteUbergraph_BP_SpitterProjectile", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L15')
        # Label 1919
        self.SetLifeSpan(1)
        ReturnValue1_2: Ptr[SphereComponent] = self.GetCollisionSphere()
        ReturnValue1_2.SetCollisionEnabled(0)
        goto(ExecutionFlow.Pop())
        self.ReceiveTick(DeltaSeconds)
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(self.mProjectileMovement.Velocity)
        ReturnValue_16: bool = Z <= 0
        ReturnValue_17: bool = ReturnValue_16 and self.mDoSplit
        ReturnValue_18: bool = self.HasAuthority()
        ReturnValue1_3: bool = ReturnValue_17 and ReturnValue_18
        if not ReturnValue1_3:
           goto(ExecutionFlow.Pop())
        self.SplitProjectile()
        goto(ExecutionFlow.Pop())
        ReturnValue_19: Vector = self.GetProjectileTargetLocation()
        ReturnValue1_4: Vector = self.K2_GetActorLocation()
        ReturnValue_20: Vector = Subtract_VectorVector(ReturnValue_19, ReturnValue1_4)
        ReturnValue_21: float = VSize(ReturnValue_20)
        self.DistanceToTarget = ReturnValue_21
        ReturnValue_19 = self.GetProjectileTargetLocation()
        ReturnValue1_4 = self.K2_GetActorLocation()
        ReturnValue_20 = Subtract_VectorVector(ReturnValue_19, ReturnValue1_4)
        ReturnValue_21 = VSize(ReturnValue_20)
        ReturnValue1_5: Vector = self.GetProjectileTargetLocation()
        ReturnValue2: Vector = self.K2_GetActorLocation()
        ReturnValue1_6: Vector = Subtract_VectorVector(ReturnValue1_5, ReturnValue2)
        ReturnValue_22: Vector = Normal(ReturnValue1_6, 9.999999747378752e-05)
        ReturnValue_23: float = self.CurveProjectileZ.GetFloatValue(ReturnValue_21)
        ReturnValue2_0: Vector = Vector(0, 0, ReturnValue_23)
        ReturnValue_24: Vector = ReturnValue_22 + ReturnValue2_0
        ReturnValue1_7: float = self.CurveProjectileSpeed.GetFloatValue(ReturnValue_21)
        ReturnValue_25: Vector = ReturnValue_24 * ReturnValue1_7
        self.mProjectileMovement.Velocity = ReturnValue_25
        ReturnValue_19 = self.GetProjectileTargetLocation()
        ReturnValue1_4 = self.K2_GetActorLocation()
        ReturnValue_20 = Subtract_VectorVector(ReturnValue_19, ReturnValue1_4)
        ReturnValue_21 = VSize(ReturnValue_20)
        ReturnValue2_1: float = self.CurveProjectileAngle.GetFloatValue(ReturnValue_21)
        self.mAdjusted_Cone_Angle = ReturnValue2_1
        ReturnValue_19 = self.GetProjectileTargetLocation()
        ReturnValue1_4 = self.K2_GetActorLocation()
        ReturnValue_20 = Subtract_VectorVector(ReturnValue_19, ReturnValue1_4)
        ReturnValue_21 = VSize(ReturnValue_20)
        ReturnValue1_8: bool = ReturnValue_21 <= 1500
        if not ReturnValue1_8:
           goto(ExecutionFlow.Pop())
        goto('L1700')
        # Label 3407
        ReturnValue1_9: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_Spitter_Projectile_Loop, self, True)
        ReturnValue3_2: Vector = self.K2_GetActorLocation()
        ReturnValue_26: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_E_Spitter_Projectile_Land, ReturnValue3_2, Rotator::FromPitchYawRoll(0, 0, 0))
        goto('L1919')
        # Label 3567
        self.Projectile.Deactivate()
        goto('L3407')
        ReturnValue4: Vector = self.K2_GetActorLocation()
        ReturnValue_27: Ptr[SphereComponent] = self.GetCollisionSphere()
        ReturnValue1_10: Vector = Vector(0, 0, ReturnValue_27.SphereRadius)
        ReturnValue2_2: Vector = Subtract_VectorVector(ReturnValue4, ReturnValue1_10)
        ReturnValue1_11: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_SpitImpact_01, ReturnValue2_2, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1.25, 1.25, 1.25), True, 0)
        goto('L3567')
        goto('L1657')
    
