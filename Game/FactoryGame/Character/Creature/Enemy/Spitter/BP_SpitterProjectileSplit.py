
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Play_E_Spitter_Projectile_Split import Play_E_Spitter_Projectile_Split
from Script.AkAudio import PostAkEventAtLocation
from Script.Engine import SpawnEmitterAtLocation
from Game.FactoryGame.VFX.Character.Creature.Spitter.P_SpitImpact_01 import P_SpitImpact_01
from Script.Engine import ReceiveBeginPlay
from Script.Engine import SphereComponent
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Stop_E_Spitter_Projectile_Loop import Stop_E_Spitter_Projectile_Loop
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Play_E_Spitter_Projectile_Land import Play_E_Spitter_Projectile_Land
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterProjectileSplit import ExecuteUbergraph_BP_SpitterProjectileSplit
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Play_E_Spitter_Projectile_Loop import Play_E_Spitter_Projectile_Loop
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import GetCollisionSphere
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import ParticleSystemComponent
from Script.Engine import K2_GetActorLocation
from Script.AkAudio import AkComponent
from Script.FactoryGame import FGProjectile

class BP_SpitterProjectileSplit(FGProjectile):
    mProjectileData = Namespace(CanTriggerExplodeBySameClass=True, DamageType='/Game/FactoryGame/Character/Creature/Enemy/Spitter/DamageType_SpitterProjectile.DamageType_SpitterProjectile_C', DamageTypeExplode='/Script/FactoryGame.FGDamageType', ExplodeAtEndOfLife=False, ExplosionDamage=20, ExplosionRadius=200, ImpactDamage=0, ProjectileClass='/Game/FactoryGame/Character/Creature/Enemy/Spitter/BP_SpitterProjectileSplit.BP_SpitterProjectileSplit_C', ProjectileLifeSpan=10, ProjectileStickSpan=0, ShouldExplodeOnImpact=True)
    mCollisionComp = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 14, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Projectile', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', OnComponentHit=0, SphereRadius=16, bCanEverAffectNavigation=False)
    mProjectileMovement = Namespace(InitialSpeed=2000, MaxSpeed=4000, ObjectClass='/Script/Engine.ProjectileMovementComponent', ObjectFlags=2883617, ObjectName='ProjectileComp', ProjectileGravityScale=0.10000000149011612, Velocity={'X': 0, 'Y': 0, 'Z': 1}, bRotationFollowsVelocity=True)
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicateMovement = True
    bReplicates = True
    RemoteRole = 1
    InitialLifeSpan = 3
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 14, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Projectile', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', OnComponentHit=0, SphereRadius=16, bCanEverAffectNavigation=False)
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_SpitterProjectileSplit(10)
    

    def PlayExplosionEffects(self):
        self.ExecuteUbergraph_BP_SpitterProjectileSplit(672)
    

    def ExecuteUbergraph_BP_SpitterProjectileSplit(self):
        self.ReceiveBeginPlay()
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Spitter_Projectile_Split, self, True)
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Spitter_Projectile_Loop, self, True)
        # End
        # Label 131
        ReturnValue_0: Ptr[SphereComponent] = self.GetCollisionSphere()
        ReturnValue_0.SetCollisionEnabled(0)
        # End
        # Label 194
        self.SetLifeSpan(1)
        goto('L131')
        # Label 218
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_Spitter_Projectile_Loop, self, True)
        ReturnValue_1: Vector = self.K2_GetActorLocation()
        ReturnValue_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_E_Spitter_Projectile_Land, ReturnValue_1, Rotator::FromPitchYawRoll(0, 0, 0))
        goto('L194')
        # Label 378
        self.Projectile.Deactivate()
        ReturnValue_1 = self.K2_GetActorLocation()
        ReturnValue1_0: Ptr[SphereComponent] = self.GetCollisionSphere()
        ReturnValue_3: Vector = Vector(0, 0, ReturnValue1_0.SphereRadius)
        ReturnValue_4: Vector = Subtract_VectorVector(ReturnValue_1, ReturnValue_3)
        ReturnValue_5: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_SpitImpact_01, ReturnValue_4, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        goto('L218')
        goto('L378')
    
