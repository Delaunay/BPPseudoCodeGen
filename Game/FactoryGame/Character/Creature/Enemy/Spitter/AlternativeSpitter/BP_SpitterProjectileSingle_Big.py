
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Character.Creature.Enemy.Spitter.AlternativeSpitter.BP_SpitterProjectileSingle_Big import ExecuteUbergraph_BP_SpitterProjectileSingle_Big.K2Node_ComponentBoundEvent_Component
from Script.Engine import Delay
from Game.FactoryGame.Character.Creature.Enemy.Spitter.AlternativeSpitter.BP_SpitterProjectileSingle_Big import ExecuteUbergraph_BP_SpitterProjectileSingle_Big.K2Node_ComponentBoundEvent_bReset
from Script.AkAudio import PostAkEventAtLocation
from Script.Engine import SpawnEmitterAtLocation
from Script.Engine import VSize
from Script.Engine import ReceiveBeginPlay
from Script.Engine import SphereComponent
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Stop_E_Spitter_Projectile_Loop import Stop_E_Spitter_Projectile_Loop
from Script.Engine import LatentActionInfo
from Game.FactoryGame.VFX.Character.Creature.Spitter.P_SpitImpact_01 import P_SpitImpact_01
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Creature.Enemy.Spitter.AlternativeSpitter.BP_SpitterProjectileSingle_Big import ExecuteUbergraph_BP_SpitterProjectileSingle_Big
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Play_E_Spitter_Projectile_Land import Play_E_Spitter_Projectile_Land
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Play_E_Spitter_Projectile_Loop import Play_E_Spitter_Projectile_Loop
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import GetCollisionSphere
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.Engine import Normal
from Script.FactoryGame import GetProjectileTargetLocation
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import ParticleSystemComponent
from Script.Engine import K2_GetActorLocation
from Script.Engine import SetVectorParameter
from Script.AkAudio import AkComponent
from Script.FactoryGame import FGProjectile
from Script.Engine import RandomFloatInRange

class BP_SpitterProjectileSingle_Big(FGProjectile):
    mSpeedAdjustment: float = 2000
    mDoSplit: bool = True
    mNumberofSplitProjectiles: int32 = 7
    mSplitConeHalfAngle: float = 5
    mProjectileData = Namespace(CanTriggerExplodeBySameClass=True, DamageType='/Game/FactoryGame/Character/Creature/Enemy/Spitter/DamageType_SpitterProjectile.DamageType_SpitterProjectile_C', DamageTypeExplode='/Script/FactoryGame.FGDamageType', ExplodeAtEndOfLife=False, ExplosionDamage=20, ExplosionRadius=400, ImpactDamage=15, ProjectileClass='/Game/FactoryGame/Character/Creature/Enemy/Spitter/AlternativeSpitter/BP_SpitterProjectileSingle_Big.BP_SpitterProjectileSingle_Big_C', ProjectileLifeSpan=10, ProjectileStickSpan=0, ShouldExplodeOnImpact=True)
    mCollisionComp = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 14, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Projectile', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', OnComponentHit=0, RelativeScale3D={'X': 1.100000023841858, 'Y': 1.100000023841858, 'Z': 1.100000023841858}, SphereRadius=16, bCanEverAffectNavigation=False)
    mProjectileMovement = Namespace(InitialSpeed=250, MaxSpeed=10000, ObjectClass='/Script/Engine.ProjectileMovementComponent', ObjectFlags=2883617, ObjectName='ProjectileComp', ProjectileGravityScale=0, Velocity={'X': 0, 'Y': 0, 'Z': 1}, bAutoActivate=False, bRotationFollowsVelocity=True)
    mCanTriggerExplodeBySameClass = True
    mExplodeAtEndOfLife = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bReplicateMovement = True
    bReplicates = True
    RemoteRole = 1
    InitialLifeSpan = 3
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 14, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Projectile', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', OnComponentHit=0, RelativeScale3D={'X': 1.100000023841858, 'Y': 1.100000023841858, 'Z': 1.100000023841858}, SphereRadius=16, bCanEverAffectNavigation=False)
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_SpitterProjectileSingle_Big(99)
    

    def BndEvt__mProjectileMovement_K2Node_ComponentBoundEvent_0_ActorComponentActivatedSignature__DelegateSignature(self, component: Ptr[ActorComponent], bReset: bool):
        ExecuteUbergraph_BP_SpitterProjectileSingle_Big.K2Node_ComponentBoundEvent_Component = component #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SpitterProjectileSingle_Big.K2Node_ComponentBoundEvent_bReset = bReset #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SpitterProjectileSingle_Big(259)
    

    def PlayExplosionEffects(self):
        self.ExecuteUbergraph_BP_SpitterProjectileSingle_Big(1805)
    

    def ExecuteUbergraph_BP_SpitterProjectileSingle_Big(self):
        goto(ComputedJump("EntryPoint"))
        self.mProjectileMovement.Activate(False)
        goto(ExecutionFlow.Pop())
        self.mProjectileMovement.ProjectileGravityScale = 2
        goto(ExecutionFlow.Pop())
        self.ReceiveBeginPlay()
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Spitter_Projectile_Loop, self, True)
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 15, UUID = -1842781912, ExecutionFunction = "ExecuteUbergraph_BP_SpitterProjectileSingle_Big", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 239
        self.SetLifeSpan(1)
        goto(ExecutionFlow.Pop())
        ReturnValue_0: Vector = self.GetProjectileTargetLocation()
        ReturnValue_1: Vector = self.K2_GetActorLocation()
        ReturnValue_2: Vector = Subtract_VectorVector(ReturnValue_0, ReturnValue_1)
        ReturnValue_3: float = VSize(ReturnValue_2)
        ReturnValue_4: Vector = Normal(ReturnValue_2, 9.999999747378752e-05)
        ReturnValue_5: float = ReturnValue_3 * 0.699999988079071
        ReturnValue1: float = ReturnValue_5 + 4000
        ReturnValue_6: float = RandomFloatInRange(-0.05000000074505806, 0.05000000074505806)
        ReturnValue1_0: Vector = Vector(ReturnValue_6, ReturnValue_6, 0.009999999776482582)
        ReturnValue_7: Vector = ReturnValue_4 + ReturnValue1_0
        ReturnValue_8: Vector = ReturnValue_7 * ReturnValue1
        self.mProjectileMovement.Velocity = ReturnValue_8
        ReturnValue_0 = self.GetProjectileTargetLocation()
        ReturnValue_1 = self.K2_GetActorLocation()
        ReturnValue_2 = Subtract_VectorVector(ReturnValue_0, ReturnValue_1)
        ReturnValue_3 = VSize(ReturnValue_2)
        ReturnValue_9: float = ReturnValue_3 / 10000
        ReturnValue_10: float = 1.100000023841858 - ReturnValue_9
        self.mProjectileMovement.ProjectileGravityScale = ReturnValue_10
        ReturnValue_0 = self.GetProjectileTargetLocation()
        ReturnValue_1 = self.K2_GetActorLocation()
        ReturnValue_2 = Subtract_VectorVector(ReturnValue_0, ReturnValue_1)
        ReturnValue_3 = VSize(ReturnValue_2)
        ReturnValue_11: bool = ReturnValue_3 <= 2500
        if not ReturnValue_11:
            goto('L1527')
        ReturnValue_0 = self.GetProjectileTargetLocation()
        ReturnValue_1 = self.K2_GetActorLocation()
        ReturnValue_2 = Subtract_VectorVector(ReturnValue_0, ReturnValue_1)
        ReturnValue_3 = VSize(ReturnValue_2)
        ReturnValue_9 = ReturnValue_3 / 10000
        ReturnValue_10 = 1.100000023841858 - ReturnValue_9
        ReturnValue_12: float = ReturnValue_10 + 0.20000000298023224
        self.mProjectileMovement.ProjectileGravityScale = ReturnValue_12
        # Label 1527
        Default__KismetSystemLibrary.Delay(self, 1, LatentActionInfo(Linkage = 53, UUID = -1502835256, ExecutionFunction = "ExecuteUbergraph_BP_SpitterProjectileSingle_Big", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1604
        ReturnValue1_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_Spitter_Projectile_Loop, self, True)
        ReturnValue1_2: Vector = self.K2_GetActorLocation()
        ReturnValue_13: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_E_Spitter_Projectile_Land, ReturnValue1_2, Rotator::FromPitchYawRoll(0, 0, 0))
        goto('L239')
        # Label 1764
        self.Projectile.Deactivate()
        goto('L1604')
        ReturnValue2: Vector = self.K2_GetActorLocation()
        ReturnValue_14: Ptr[SphereComponent] = self.GetCollisionSphere()
        ReturnValue_15: Vector = Vector(0, 0, ReturnValue_14.SphereRadius)
        ReturnValue1_3: Vector = Subtract_VectorVector(ReturnValue2, ReturnValue_15)
        ReturnValue_16: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_SpitImpact_01, ReturnValue1_3, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1.2000000476837158, 1.2000000476837158, 1.2000000476837158), True, 0)
        ReturnValue_16.SetVectorParameter("Color", Vector(0, 5, 3))
        goto('L1764')
    
