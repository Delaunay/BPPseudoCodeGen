
from codegen.ue4_stub import *

from Script.FactoryGame import FGHealthComponent
from Script.FactoryGame import GetHealthComponent
from Game.FactoryGame.Equipment.C4Dispenser.DamageType_C4 import DamageType_C4
from Script.AkAudio import PostAkEvent
from Script.Engine import FinishSpawningActor
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterProjectileBig import ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_Event_DeltaSeconds
from Script.Engine import Delay
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Script.Engine import SpawnEmitterAtLocation
from Script.AkAudio import PostAkEventAtLocation
from Script.Engine import GetTransform
from Script.Engine import VSize
from Game.FactoryGame.VFX.Character.Creature.Spitter.P_SpitImpact_01 import P_SpitImpact_01
from Script.Engine import SphereComponent
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Stop_E_Spitter_Projectile_Loop import Stop_E_Spitter_Projectile_Loop
from Script.Engine import LatentActionInfo
from Script.Engine import ReceiveBeginPlay
from Script.Engine import GetPlayerPawn
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterProjectileBig import ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_CustomEvent_DeadActor
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import HasAuthority
from Script.FactoryGame import FGCharacterBase
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterProjectileBig import ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_ComponentBoundEvent_Component
from Script.Engine import ReceiveTick
from Script.Engine import ApplyRadialDamage
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterProjectileBig import ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_CustomEvent_damagedActor
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Play_E_Spitter_Projectile_Land import Play_E_Spitter_Projectile_Land
from Script.Engine import IsValid
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.Engine import DegreesToRadians
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Play_E_Spitter_Projectile_Loop import Play_E_Spitter_Projectile_Loop
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterProjectileSplit import BP_SpitterProjectileSplit
from Script.Engine import Default__GameplayStatics
from Script.Engine import FlushNetDormancy
from Script.FactoryGame import GetCollisionSphere
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.Engine import Normal
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterProjectileBig import ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_CustomEvent_instigatedBy
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterProjectileBig import ExecuteUbergraph_BP_SpitterProjectileBig
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterProjectileBig import ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_CustomEvent_Damage
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterProjectileBig import ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_ComponentBoundEvent_bReset
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import GetProjectileTargetLocation
from Script.FactoryGame import SetInitialVelocity
from Script.Engine import ParticleSystemComponent
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.Equipment.C4Dispenser.Particles.C4Explosion import C4Explosion
from Script.Engine import GetOwner
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterProjectileBig import ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_CustomEvent_damageType
from Script.AkAudio import AkComponent
from Script.CoreUObject import Transform
from Script.FactoryGame import FGProjectile
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterProjectileBig import ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_CustomEvent_damageCauser
from Script.Engine import RandomUnitVectorInConeInRadians

class BP_SpitterProjectileBig(FGProjectile):
    mSpeedAdjustment: float = 2000
    mDoSplit: bool = True
    mNumberofSplitProjectiles: int32 = 20
    mSplitConeHalfAngle: float = 70
    mAttackLocation: Vector
    mTargetPawn: Ptr[Pawn]
    SplitDelay: float = 0.5
    mActive: bool = True
    mProjectileData = Namespace(CanTriggerExplodeBySameClass=True, DamageType='/Game/FactoryGame/Character/Creature/Enemy/Spitter/DamageType_SpitterProjectile.DamageType_SpitterProjectile_C', DamageTypeExplode='/Script/FactoryGame.FGDamageType', ExplodeAtEndOfLife=False, ExplosionDamage=20, ExplosionRadius=400, ImpactDamage=0, ProjectileClass='/Game/FactoryGame/Character/Creature/Enemy/Spitter/BP_SpitterProjectileBig.BP_SpitterProjectileBig_C', ProjectileLifeSpan=10, ProjectileStickSpan=5, ShouldExplodeOnImpact=True)
    mCollisionComp = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 14, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'Visibility', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', OnComponentHit=0, SphereRadius=16, bCanEverAffectNavigation=False)
    mProjectileMovement = Namespace(InitialSpeed=400, MaxSpeed=4000, ObjectClass='/Script/Engine.ProjectileMovementComponent', ObjectFlags=2883617, ObjectName='ProjectileComp', ProjectileGravityScale=0, Velocity={'X': 0, 'Y': 0, 'Z': 1}, bAutoActivate=False, bRotationFollowsVelocity=True)
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicateMovement = True
    bReplicates = True
    RemoteRole = 1
    InitialLifeSpan = 3
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 14, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'Visibility', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', OnComponentHit=0, SphereRadius=16, bCanEverAffectNavigation=False)
    
    def GetNewTarget(self):
        ExecutionFlow.Push("L1080")
        Variable: int32 = 0
        # Label 28
        ReturnValue: bool = Variable <= 8
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1006")
        ReturnValue_0: Ptr[Pawn] = Default__GameplayStatics.GetPlayerPawn(self, Variable)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        ReturnValue_0 = Default__GameplayStatics.GetPlayerPawn(self, Variable)
        ReturnValue2: Vector = ReturnValue_0.K2_GetActorLocation()
        ReturnValue3: Vector = self.K2_GetActorLocation()
        ReturnValue1_0: Vector = Subtract_VectorVector(ReturnValue2, ReturnValue3)
        ReturnValue1_1: float = VSize(ReturnValue1_0)
        ReturnValue_1: bool = ReturnValue1_1 <= 9999
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(self.mTargetPawn)
        if not ReturnValue_2:
            goto('L934')
        ReturnValue_3: Vector = self.mTargetPawn.K2_GetActorLocation()
        ReturnValue1_2: Vector = self.K2_GetActorLocation()
        ReturnValue_0 = Default__GameplayStatics.GetPlayerPawn(self, Variable)
        ReturnValue_4: Vector = Subtract_VectorVector(ReturnValue_3, ReturnValue1_2)
        ReturnValue_5: float = VSize(ReturnValue_4)
        ReturnValue2 = ReturnValue_0.K2_GetActorLocation()
        ReturnValue3 = self.K2_GetActorLocation()
        ReturnValue1_0 = Subtract_VectorVector(ReturnValue2, ReturnValue3)
        ReturnValue1_1 = VSize(ReturnValue1_0)
        ReturnValue_6: bool = ReturnValue1_1 <= ReturnValue_5
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        # Label 934
        ReturnValue_0 = Default__GameplayStatics.GetPlayerPawn(self, Variable)
        self.mTargetPawn = ReturnValue_0
        goto(ExecutionFlow.Pop())
        # Label 1006
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L28')
    

    def GetNewTargetLocation(self):
        ExecutionFlow.Push("L1023")
        Variable: int32 = 0
        # Label 28
        ReturnValue: bool = Variable <= 8
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L949")
        ReturnValue_0: Ptr[Pawn] = Default__GameplayStatics.GetPlayerPawn(self, Variable)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue1: Vector = self.K2_GetActorLocation()
        ReturnValue_0 = Default__GameplayStatics.GetPlayerPawn(self, Variable)
        ReturnValue2: Vector = ReturnValue_0.K2_GetActorLocation()
        ReturnValue1_0: Vector = Subtract_VectorVector(ReturnValue2, ReturnValue1)
        ReturnValue1_1: float = VSize(ReturnValue1_0)
        ReturnValue_2: bool = ReturnValue1_1 <= 3000
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        ReturnValue_3: Vector = self.K2_GetActorLocation()
        ReturnValue1 = self.K2_GetActorLocation()
        ReturnValue_4: Vector = Subtract_VectorVector(self.mAttackLocation, ReturnValue_3)
        ReturnValue_5: float = VSize(ReturnValue_4)
        ReturnValue_0 = Default__GameplayStatics.GetPlayerPawn(self, Variable)
        ReturnValue2 = ReturnValue_0.K2_GetActorLocation()
        ReturnValue1_0 = Subtract_VectorVector(ReturnValue2, ReturnValue1)
        ReturnValue1_1 = VSize(ReturnValue1_0)
        ReturnValue_6: bool = ReturnValue1_1 <= ReturnValue_5
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        ReturnValue_0 = Default__GameplayStatics.GetPlayerPawn(self, Variable)
        ReturnValue2 = ReturnValue_0.K2_GetActorLocation()
        self.mAttackLocation = ReturnValue2
        goto(ExecutionFlow.Pop())
        # Label 949
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L28')
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_SpitterProjectileBig(2960)
    

    def SplitProjectile(self):
        self.ExecuteUbergraph_BP_SpitterProjectileBig(1946)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SpitterProjectileBig(1961)
    

    def BndEvt__mProjectileMovement_K2Node_ComponentBoundEvent_0_ActorComponentActivatedSignature__DelegateSignature(self, component: Ptr[ActorComponent], bReset: bool):
        ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_ComponentBoundEvent_Component = component #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_ComponentBoundEvent_bReset = bReset #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SpitterProjectileBig(2674)
    

    def PlayExplosionEffects(self):
        self.ExecuteUbergraph_BP_SpitterProjectileBig(2965)
    

    def OnTakeAnyDamage_Event_0(self, DamagedActor: Ptr[Actor], Damage: float, DamageType: Const[Ptr[DamageType]], InstigatedBy: Ptr[Controller], DamageCauser: Ptr[Actor]):
        ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_CustomEvent_damagedActor = DamagedActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_CustomEvent_Damage = Damage #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_CustomEvent_damageType = DamageType #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_CustomEvent_instigatedBy = InstigatedBy #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_CustomEvent_damageCauser = DamageCauser #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SpitterProjectileBig(3292)
    

    def SpitterDied(self, DeadActor: Ptr[Actor]):
        ExecuteUbergraph_BP_SpitterProjectileBig.K2Node_CustomEvent_DeadActor = DeadActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SpitterProjectileBig(3297)
    

    def DestroySelf(self):
        self.ExecuteUbergraph_BP_SpitterProjectileBig(3302)
    

    def ExecuteUbergraph_BP_SpitterProjectileBig(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.mActive = False
        # Label 26
        ReturnValue3: Vector = self.K2_GetActorLocation()
        ReturnValue: Ptr[SphereComponent] = self.GetCollisionSphere()
        ReturnValue_0: Vector = Vector(0, 0, ReturnValue.SphereRadius)
        ReturnValue1: Vector = Subtract_VectorVector(ReturnValue3, ReturnValue_0)
        ReturnValue_1: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_SpitImpact_01, ReturnValue1, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        self.Projectile.Deactivate()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_Spitter_Projectile_Loop, self, True)
        ReturnValue2: Vector = self.K2_GetActorLocation()
        ReturnValue_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_E_Spitter_Projectile_Land, ReturnValue2, Rotator::FromPitchYawRoll(0, 0, 0))
        self.SetLifeSpan(1)
        ReturnValue1_1: Ptr[SphereComponent] = self.GetCollisionSphere()
        ReturnValue1_1.SetCollisionEnabled(0)
        goto(ExecutionFlow.Pop())
        # Label 548
        self.FlushNetDormancy()
        self.mDoSplit = False
        ReturnValue_3: bool = self.mNumberofSplitProjectiles > 0
        if not ReturnValue_3:
            goto('L1822')
        ReturnValue_4: int32 = self.mNumberofSplitProjectiles - 1
        Variable: int32 = ReturnValue_4
        self.mNumberofSplitProjectiles = Variable
        ReturnValue_5: Vector = self.mTargetPawn.GetVelocity()
        ReturnValue4: Vector = self.mTargetPawn.K2_GetActorLocation()
        ReturnValue1_2: Vector = ReturnValue4 + ReturnValue_5
        self.mAttackLocation = ReturnValue1_2
        ReturnValue_6: Ptr[Actor] = self.GetOwner()
        ReturnValue_7: Transform = self.GetTransform()
        
        ReturnValue_8: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_SpitterProjectileSplit, 0, ReturnValue_6, Ref[ReturnValue_7])
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_8, "Instigator", self.Instigator)
        ReturnValue_7 = self.GetTransform()
        
        ReturnValue_9: Ptr[BP_SpitterProjectileSplit] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_8, Ref[ReturnValue_7])
        ReturnValue_10: Vector = self.K2_GetActorLocation()
        ReturnValue2_0: Vector = Subtract_VectorVector(self.mAttackLocation, ReturnValue_10)
        ReturnValue1_3: Vector = Normal(ReturnValue2_0, 9.999999747378752e-05)
        ReturnValue1_4: Vector = self.mTargetPawn.GetVelocity()
        ReturnValue1_5: float = VSize(ReturnValue1_4)
        ReturnValue_11: float = ReturnValue1_5 / self.mSplitConeHalfAngle
        ReturnValue_12: float = ReturnValue_11 + 3
        ReturnValue_13: float = DegreesToRadians(ReturnValue_12)
        ReturnValue_14: Vector = RandomUnitVectorInConeInRadians(ReturnValue1_3, ReturnValue_13)
        ReturnValue2_1: Vector = ReturnValue_14 * self.mSpeedAdjustment
        ReturnValue_9.mProjectileMovement.Velocity = ReturnValue2_1
        ReturnValue_9.SetInitialVelocity(ReturnValue_9.mProjectileMovement.Velocity)
        Default__KismetSystemLibrary.Delay(self, self.SplitDelay, LatentActionInfo(Linkage = 1837, UUID = 523142578, ExecutionFunction = "ExecuteUbergraph_BP_SpitterProjectileBig", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1822
        self.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        self.SplitProjectile()
        goto(ExecutionFlow.Pop())
        self.mProjectileMovement.Activate(False)
        self.GetNewTarget()
        OutputDelegate1.BindUFunction(self, OnTakeAnyDamage_Event_0)
        self.OnTakeAnyDamage.AddUnique(OutputDelegate1)
        goto(ExecutionFlow.Pop())
        if not self.mActive:
           goto(ExecutionFlow.Pop())
        goto('L548')
        self.ReceiveTick(DeltaSeconds)
        ReturnValue_15: float = VSize(self.mProjectileMovement.Velocity)
        ReturnValue_16: bool = ReturnValue_15 <= 50
        ReturnValue_17: bool = ReturnValue_16 and self.mDoSplit
        ReturnValue_18: bool = self.HasAuthority()
        ReturnValue1_6: bool = ReturnValue_17 and ReturnValue_18
        if not ReturnValue1_6:
            goto('L2198')
        self.SplitProjectile()
        goto(ExecutionFlow.Pop())
        # Label 2198
        if not self.mDoSplit:
           goto(ExecutionFlow.Pop())
        ReturnValue_19: Vector = self.mProjectileMovement.Velocity * 0.949999988079071
        self.mProjectileMovement.Velocity = ReturnValue_19
        goto(ExecutionFlow.Pop())
        # Label 2322
        ReturnValue_20: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Spitter_Projectile_Loop, self, True)
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 1852, UUID = -61613411, ExecutionFunction = "ExecuteUbergraph_BP_SpitterProjectileBig", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 2452
        self.ReceiveBeginPlay()
        ExecutionFlow.Push("L2472")
        goto('L2322')
        # Label 2472
        ReturnValue1_7: Ptr[Actor] = self.GetOwner()
        Base: Ptr[FGCharacterBase] = Cast[FGCharacterBase](ReturnValue1_7)
        bSuccess: bool = Base
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        OutputDelegate.BindUFunction(self, SpitterDied)
        ReturnValue_21: Ptr[FGHealthComponent] = Base.GetHealthComponent()
        ReturnValue_21.DeathDelegate.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        ReturnValue_22: Vector = self.GetProjectileTargetLocation()
        ReturnValue1_8: Vector = self.K2_GetActorLocation()
        ReturnValue_23: Vector = Subtract_VectorVector(ReturnValue_22, ReturnValue1_8)
        ReturnValue_24: Vector = Normal(ReturnValue_23, 9.999999747378752e-05)
        ReturnValue_25: Vector = ReturnValue_24 + Vector(0, 0, 0.8999999761581421)
        ReturnValue1_9: Vector = ReturnValue_25 * 900
        self.mProjectileMovement.Velocity = ReturnValue1_9
        goto(ExecutionFlow.Pop())
        goto('L2452')
        goto('L26')
        # Label 2970
        if not False:
           goto(ExecutionFlow.Pop())
        Variable_0: bool = True
        goto(ExecutionFlow.Pop())
        # Label 2984
        ExecutionFlow.Push("L3020")
        if not Variable_1:
            goto('L3004')
        goto(ExecutionFlow.Pop())
        # Label 3004
        Variable_1: bool = True
        goto('L2970')
        # Label 3020
        if not Variable_0:
            goto('L3035')
        goto(ExecutionFlow.Pop())
        # Label 3035
        Variable_0 = True
        ReturnValue5: Vector = self.K2_GetActorLocation()
        ReturnValue1_10: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, C4Explosion, ReturnValue5, Rotator::FromPitchYawRoll(0, 0, 0), Vector(3, 3, 3), True, 0)
        ReturnValue5 = self.K2_GetActorLocation()
        
        Variable_2 = None
        ReturnValue_26: bool = Default__GameplayStatics.ApplyRadialDamage(self, 40, 500, DamageType_C4, None, None, False, 3, Ref[ReturnValue5], Ref[Variable_2])
        self.DestroySelf()
        goto(ExecutionFlow.Pop())
        goto('L2984')
        goto('L15')
        goto('L15')
    
