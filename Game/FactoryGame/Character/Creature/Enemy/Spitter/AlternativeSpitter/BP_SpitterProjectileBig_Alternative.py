
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.C4Dispenser.DamageType_C4 import DamageType_C4
from Game.FactoryGame.Character.Creature.Enemy.Spitter.AlternativeSpitter.BP_SpitterProjectileBig_Alternative import ExecuteUbergraph_BP_SpitterProjectileBig_Alternative.K2Node_CustomEvent_damageCauser
from Script.Engine import FinishSpawningActor
from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Script.Engine import SpawnEmitterAtLocation
from Script.Engine import GetTransform
from Script.AkAudio import PostAkEventAtLocation
from Script.Engine import VSize
from Script.Engine import Conv_IntToFloat
from Script.Engine import BreakTransform
from Game.FactoryGame.VFX.Character.Creature.Spitter.P_SpitImpact_01 import P_SpitImpact_01
from Script.Engine import SphereComponent
from Script.Engine import ReceiveBeginPlay
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Stop_E_Spitter_Projectile_Loop import Stop_E_Spitter_Projectile_Loop
from Game.FactoryGame.Character.Creature.Enemy.Spitter.AlternativeSpitter.BP_SpitterProjectileBig_Alternative import ExecuteUbergraph_BP_SpitterProjectileBig_Alternative.K2Node_CustomEvent_damagedActor
from Script.Engine import GetPlayerPawn
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import HasAuthority
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Particle.C4ExplosionBlue import C4ExplosionBlue
from Script.Engine import ReceiveTick
from Game.FactoryGame.Character.Creature.Enemy.Spitter.AlternativeSpitter.BP_SpitterProjectileBig_Alternative import ExecuteUbergraph_BP_SpitterProjectileBig_Alternative.K2Node_CustomEvent_damageType
from Script.Engine import ApplyRadialDamage
from Game.FactoryGame.Character.Creature.Enemy.Spitter.AlternativeSpitter.BP_SpitterProjectileBig_Alternative import ExecuteUbergraph_BP_SpitterProjectileBig_Alternative.K2Node_Event_DeltaSeconds
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Play_E_Spitter_Projectile_Land import Play_E_Spitter_Projectile_Land
from Script.Engine import IsValid
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.Engine import DegreesToRadians
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Play_E_Spitter_Projectile_Loop import Play_E_Spitter_Projectile_Loop
from Game.FactoryGame.Character.Creature.Enemy.Spitter.AlternativeSpitter.BP_SpitterProjectileBig_Alternative import ExecuteUbergraph_BP_SpitterProjectileBig_Alternative.K2Node_ComponentBoundEvent_bReset
from Script.Engine import Divide_IntInt
from Script.Engine import Default__GameplayStatics
from Script.Engine import FlushNetDormancy
from Script.FactoryGame import GetCollisionSphere
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.Engine import Normal
from Script.FactoryGame import GetProjectileTargetLocation
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Character.Creature.Enemy.Spitter.AlternativeSpitter.BP_SpitterProjectileBig_Alternative import ExecuteUbergraph_BP_SpitterProjectileBig_Alternative.K2Node_CustomEvent_Damage
from Script.Engine import MakeTransform
from Script.FactoryGame import SetInitialVelocity
from Script.Engine import Actor
from Script.Engine import ParticleSystemComponent
from Script.Engine import K2_GetActorLocation
from Script.Engine import Multiply_VectorVector
from Game.FactoryGame.Character.Creature.Enemy.Spitter.AlternativeSpitter.BP_SpitterProjectileBig_Alternative import ExecuteUbergraph_BP_SpitterProjectileBig_Alternative
from Script.Engine import GetOwner
from Script.Engine import SetVectorParameter
from Game.FactoryGame.Character.Creature.Enemy.Spitter.AlternativeSpitter.BP_SpitterProjectileBig_Alternative import ExecuteUbergraph_BP_SpitterProjectileBig_Alternative.K2Node_CustomEvent_instigatedBy
from Script.AkAudio import AkComponent
from Game.FactoryGame.Character.Creature.Enemy.Spitter.AlternativeSpitter.BP_SpitterProjectileSplitAlt import BP_SpitterProjectileSplitAlt
from Game.FactoryGame.Character.Creature.Enemy.Spitter.AlternativeSpitter.BP_SpitterProjectileBig_Alternative import ExecuteUbergraph_BP_SpitterProjectileBig_Alternative.K2Node_ComponentBoundEvent_Component
from Script.CoreUObject import Transform
from Script.FactoryGame import FGProjectile
from Script.Engine import RandomUnitVectorInConeInRadians

class BP_SpitterProjectileBig_Alternative(FGProjectile):
    mSpeedAdjustment: float = 2000
    mDoSplit: bool = True
    mNumberofSplitProjectiles: int32 = 15
    mSplitConeHalfAngle: float = 15
    mAttackLocation: Vector
    mTargetPawn: Ptr[Pawn]
    mProjectileData = Namespace(CanTriggerExplodeBySameClass=True, DamageType='/Game/FactoryGame/Character/Creature/Enemy/Spitter/DamageType_SpitterProjectile.DamageType_SpitterProjectile_C', DamageTypeExplode='/Script/FactoryGame.FGDamageType', ExplodeAtEndOfLife=False, ExplosionDamage=30, ExplosionRadius=500, ImpactDamage=10, ProjectileClass='/Game/FactoryGame/Character/Creature/Enemy/Spitter/AlternativeSpitter/BP_SpitterProjectileBig_Alternative.BP_SpitterProjectileBig_Alternative_C', ProjectileLifeSpan=10, ProjectileStickSpan=0, ShouldExplodeOnImpact=True)
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
        self.ExecuteUbergraph_BP_SpitterProjectileBig_Alternative(2413)
    

    def SplitProjectile(self):
        self.ExecuteUbergraph_BP_SpitterProjectileBig_Alternative(2553)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_SpitterProjectileBig_Alternative.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SpitterProjectileBig_Alternative(2601)
    

    def BndEvt__mProjectileMovement_K2Node_ComponentBoundEvent_0_ActorComponentActivatedSignature__DelegateSignature(self, component: Ptr[ActorComponent], bReset: bool):
        ExecuteUbergraph_BP_SpitterProjectileBig_Alternative.K2Node_ComponentBoundEvent_Component = component #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SpitterProjectileBig_Alternative.K2Node_ComponentBoundEvent_bReset = bReset #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SpitterProjectileBig_Alternative(2693)
    

    def PlayExplosionEffects(self):
        self.ExecuteUbergraph_BP_SpitterProjectileBig_Alternative(3180)
    

    def OnTakeAnyDamage_Event_0(self, DamagedActor: Ptr[Actor], Damage: float, DamageType: Const[Ptr[DamageType]], InstigatedBy: Ptr[Controller], DamageCauser: Ptr[Actor]):
        ExecuteUbergraph_BP_SpitterProjectileBig_Alternative.K2Node_CustomEvent_damagedActor = DamagedActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SpitterProjectileBig_Alternative.K2Node_CustomEvent_Damage = Damage #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SpitterProjectileBig_Alternative.K2Node_CustomEvent_damageType = DamageType #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SpitterProjectileBig_Alternative.K2Node_CustomEvent_instigatedBy = InstigatedBy #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SpitterProjectileBig_Alternative.K2Node_CustomEvent_damageCauser = DamageCauser #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SpitterProjectileBig_Alternative(3804)
    

    def ExecuteUbergraph_BP_SpitterProjectileBig_Alternative(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.FlushNetDormancy()
        self.mDoSplit = False
        ReturnValue: bool = self.mNumberofSplitProjectiles > 0
        if not ReturnValue:
            goto('L1796')
        ReturnValue_0: int32 = self.mNumberofSplitProjectiles - 1
        Variable: int32 = ReturnValue_0
        self.mNumberofSplitProjectiles = Variable
        ReturnValue4: Vector = self.mTargetPawn.K2_GetActorLocation()
        self.mAttackLocation = ReturnValue4
        ReturnValue_1: Transform = self.GetTransform()
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_1], Ref[Location], Ref[Rotation], Ref[Scale])
        ReturnValue_2: Ptr[Actor] = self.GetOwner()
        ReturnValue2: Vector = Normal(self.mProjectileMovement.Velocity, 9.999999747378752e-05)
        ReturnValue2_0: Vector = ReturnValue2 * 100
        ReturnValue1: Vector = Location + ReturnValue2_0
        ReturnValue_3: Transform = MakeTransform(ReturnValue1, Rotation, Scale)
        
        ReturnValue_4: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_SpitterProjectileSplitAlt, 0, ReturnValue_2, Ref[ReturnValue_3])
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_4, "Instigator", self.Instigator)
        ReturnValue_1 = self.GetTransform()
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_1], Ref[Location], Ref[Rotation], Ref[Scale])
        ReturnValue2 = Normal(self.mProjectileMovement.Velocity, 9.999999747378752e-05)
        ReturnValue2_0 = ReturnValue2 * 100
        ReturnValue1 = Location + ReturnValue2_0
        ReturnValue_3 = MakeTransform(ReturnValue1, Rotation, Scale)
        
        ReturnValue_5: Ptr[BP_SpitterProjectileSplitAlt] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_4, Ref[ReturnValue_3])
        ReturnValue_6: Vector = self.K2_GetActorLocation()
        ReturnValue_7: float = DegreesToRadians(self.mSplitConeHalfAngle)
        ReturnValue2_1: Vector = Subtract_VectorVector(self.mAttackLocation, ReturnValue_6)
        ReturnValue1_0: Vector = Normal(ReturnValue2_1, 9.999999747378752e-05)
        ReturnValue_8: Vector = RandomUnitVectorInConeInRadians(ReturnValue1_0, ReturnValue_7)
        ReturnValue_9: Vector = Multiply_VectorVector(ReturnValue_8, Vector(1, 1, 0.30000001192092896))
        ReturnValue1_1: Vector = ReturnValue_9 * self.mSpeedAdjustment
        ReturnValue_5.mProjectileMovement.Velocity = ReturnValue1_1
        ReturnValue_5.SetInitialVelocity(ReturnValue_5.mProjectileMovement.Velocity)
        ReturnValue_5.mProjectileMovement.ProjectileGravityScale = 0
        ReturnValue_10: int32 = Divide_IntInt(self.mNumberofSplitProjectiles, 5)
        ReturnValue_11: float = Conv_IntToFloat(ReturnValue_10)
        ReturnValue_12: float = ReturnValue_11 / 10
        ReturnValue_13: float = ReturnValue_12 + 0.20000000298023224
        Default__KismetSystemLibrary.Delay(self, ReturnValue_13, LatentActionInfo(Linkage = 2122, UUID = -1942778634, ExecutionFunction = "ExecuteUbergraph_BP_SpitterProjectileBig_Alternative", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1796
        ReturnValue6: Vector = self.K2_GetActorLocation()
        ReturnValue1_2: Ptr[SphereComponent] = self.GetCollisionSphere()
        ReturnValue1_3: Vector = Vector(0, 0, ReturnValue1_2.SphereRadius)
        ReturnValue3: Vector = Subtract_VectorVector(ReturnValue6, ReturnValue1_3)
        ReturnValue2_2: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_SpitImpact_01, ReturnValue3, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        ReturnValue2_2.SetVectorParameter("Color", Vector(0, 5, 3))
        self.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        self.SplitProjectile()
        goto(ExecutionFlow.Pop())
        self.mProjectileMovement.Activate(False)
        self.GetNewTarget()
        OutputDelegate.BindUFunction(self, OnTakeAnyDamage_Event_0)
        self.OnTakeAnyDamage.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        self.SplitProjectile()
        goto(ExecutionFlow.Pop())
        # Label 2246
        if not Variable_0:
            goto('L2261')
        goto(ExecutionFlow.Pop())
        # Label 2261
        Variable_0: bool = True
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 2231, UUID = -752057316, ExecutionFunction = "ExecuteUbergraph_BP_SpitterProjectileBig_Alternative", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 2349
        Variable_0 = True
        goto(ExecutionFlow.Pop())
        # Label 2361
        if not False:
           goto(ExecutionFlow.Pop())
        Variable1: bool = True
        goto(ExecutionFlow.Pop())
        # Label 2375
        ExecutionFlow.Push("L2246")
        if not Variable_1:
            goto('L2395')
        goto(ExecutionFlow.Pop())
        # Label 2395
        Variable_1: bool = True
        if not False:
           goto(ExecutionFlow.Pop())
        goto('L2349')
        self.ReceiveBeginPlay()
        ReturnValue_14: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Spitter_Projectile_Loop, self, True)
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 2137, UUID = -2441045, ExecutionFunction = "ExecuteUbergraph_BP_SpitterProjectileBig_Alternative", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L15')
        # Label 2558
        self.SetLifeSpan(1)
        self.mNumberofSplitProjectiles = 0
        goto(ExecutionFlow.Pop())
        self.ReceiveTick(DeltaSeconds)
        ReturnValue_15: bool = self.HasAuthority()
        ReturnValue_16: bool = self.mDoSplit and ReturnValue_15
        if not ReturnValue_16:
           goto(ExecutionFlow.Pop())
        goto('L2375')
        ReturnValue_17: Vector = self.GetProjectileTargetLocation()
        ReturnValue1_4: Vector = self.K2_GetActorLocation()
        ReturnValue_18: Vector = Subtract_VectorVector(ReturnValue_17, ReturnValue1_4)
        ReturnValue_19: Vector = Normal(ReturnValue_18, 9.999999747378752e-05)
        ReturnValue_20: Vector = ReturnValue_19 + Vector(0, 0, 0.009999999776482582)
        ReturnValue_21: Vector = ReturnValue_20 * 500
        self.mProjectileMovement.Velocity = ReturnValue_21
        goto(ExecutionFlow.Pop())
        # Label 2979
        ReturnValue1_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_Spitter_Projectile_Loop, self, True)
        ReturnValue2_3: Vector = self.K2_GetActorLocation()
        ReturnValue_22: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_E_Spitter_Projectile_Land, ReturnValue2_3, Rotator::FromPitchYawRoll(0, 0, 0))
        goto('L2558')
        # Label 3139
        self.Projectile.Deactivate()
        goto('L2979')
        ReturnValue3_0: Vector = self.K2_GetActorLocation()
        ReturnValue_23: Ptr[SphereComponent] = self.GetCollisionSphere()
        ReturnValue_24: Vector = Vector(0, 0, ReturnValue_23.SphereRadius)
        ReturnValue1_6: Vector = Subtract_VectorVector(ReturnValue3_0, ReturnValue_24)
        ReturnValue_25: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_SpitImpact_01, ReturnValue1_6, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        ReturnValue_25.SetVectorParameter("Color", Vector(0, 5, 3))
        goto('L3139')
        # Label 3496
        ExecutionFlow.Push("L3532")
        if not Variable1_0:
            goto('L3516')
        goto(ExecutionFlow.Pop())
        # Label 3516
        Variable1_0: bool = True
        goto('L2361')
        # Label 3532
        if not Variable1:
            goto('L3547')
        goto(ExecutionFlow.Pop())
        # Label 3547
        Variable1 = True
        ReturnValue5: Vector = self.K2_GetActorLocation()
        ReturnValue1_7: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, C4ExplosionBlue, ReturnValue5, Rotator::FromPitchYawRoll(0, 0, 0), Vector(3, 3, 3), True, 0)
        ReturnValue5 = self.K2_GetActorLocation()
        
        Variable_2 = None
        ReturnValue_26: bool = Default__GameplayStatics.ApplyRadialDamage(self, 40, 500, DamageType_C4, None, None, False, 3, Ref[ReturnValue5], Ref[Variable_2])
        self.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        goto('L3496')
    
