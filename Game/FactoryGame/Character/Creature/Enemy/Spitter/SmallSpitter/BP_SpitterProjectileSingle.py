
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Game.FactoryGame.Character.Creature.Enemy.Spitter.SmallSpitter.BP_SpitterProjectileSingle import ExecuteUbergraph_BP_SpitterProjectileSingle
from Script.Engine import SceneComponent
from Script.Engine import PlayFromStart
from Script.AkAudio import PostAkEventAtLocation
from Script.Engine import SpawnEmitterAtLocation
from Script.Engine import VSize
from Script.Engine import FMin
from Script.Engine import ReceiveBeginPlay
from Script.Engine import SphereComponent
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Stop_E_Spitter_Projectile_Loop import Stop_E_Spitter_Projectile_Loop
from Script.Engine import LatentActionInfo
from Game.FactoryGame.VFX.Character.Creature.Spitter.P_SpitImpact_01 import P_SpitImpact_01
from Script.FactoryGame import GetCurrentAggroTarget
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import ETimelineDirection
from Script.Engine import PlayerController
from Game.FactoryGame.Character.Creature.Enemy.Spitter.SmallSpitter.BP_SpitterProjectileSingle import ExecuteUbergraph_BP_SpitterProjectileSingle.K2Node_ComponentBoundEvent_bReset
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Play_E_Spitter_Projectile_Land import Play_E_Spitter_Projectile_Land
from Script.Engine import IsValid
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Audio.Play_E_Spitter_Projectile_Loop import Play_E_Spitter_Projectile_Loop
from Script.Engine import K2_GetRootComponent
from Script.Engine import GetPlayerController
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import GetGameUI
from Script.FactoryGame import GetCollisionSphere
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.Engine import Normal
from Script.FactoryGame import FGEnemy
from Script.Engine import MakeLiteralText
from Game.FactoryGame.Character.Creature.Enemy.Spitter.SmallSpitter.BP_SpitterProjectileSingle import ExecuteUbergraph_BP_SpitterProjectileSingle.K2Node_ComponentBoundEvent_Component
from Script.FactoryGame import FGGameUI
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import GetProjectileTargetLocation
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.Engine import Actor
from Script.Engine import ParticleSystemComponent
from Script.Engine import K2_GetActorLocation
from Script.Engine import GetOwner
from Script.Engine import SetVectorParameter
from Script.AkAudio import AkComponent
from Script.FactoryGame import FGProjectile

class BP_SpitterProjectileSingle(FGProjectile):
    Gravity_Scale_over_Time_Gravity_Scale_02A6598A4993DE75B793A890687A4F4F: float
    Gravity_Scale_over_Time__Direction_02A6598A4993DE75B793A890687A4F4F: uint8
    mSpeedAdjustment: float = 2000
    mDoSplit: bool = True
    mNumberofSplitProjectiles: int32 = 7
    mSplitConeHalfAngle: float = 18
    mProjectileData = Namespace(CanTriggerExplodeBySameClass=True, DamageType='/Game/FactoryGame/Character/Creature/Enemy/Spitter/DamageType_SpitterProjectile.DamageType_SpitterProjectile_C', DamageTypeExplode='/Script/FactoryGame.FGDamageType', ExplodeAtEndOfLife=False, ExplosionDamage=15, ExplosionRadius=200, ImpactDamage=5, ProjectileClass='/Game/FactoryGame/Character/Creature/Enemy/Spitter/SmallSpitter/BP_SpitterProjectileSingle.BP_SpitterProjectileSingle_C', ProjectileLifeSpan=10, ProjectileStickSpan=5, ShouldExplodeOnImpact=True)
    mCollisionComp = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 14, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Projectile', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', OnComponentHit=0, RelativeScale3D={'X': 0.5, 'Y': 0.5, 'Z': 0.5}, SphereRadius=16, bCanEverAffectNavigation=False)
    mProjectileMovement = Namespace(InitialSpeed=1700, MaxSpeed=2000, ObjectClass='/Script/Engine.ProjectileMovementComponent', ObjectFlags=2883617, ObjectName='ProjectileComp', ProjectileGravityScale=0.699999988079071, Velocity={'X': 0, 'Y': 0, 'Z': 1}, bAutoActivate=False, bRotationFollowsVelocity=True)
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bReplicateMovement = True
    bReplicates = True
    RemoteRole = 1
    InitialLifeSpan = 3
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 14, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Projectile', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', OnComponentHit=0, RelativeScale3D={'X': 0.5, 'Y': 0.5, 'Z': 0.5}, SphereRadius=16, bCanEverAffectNavigation=False)
    
    def Gravity Scale over Time__FinishedFunc(self):
        self.ExecuteUbergraph_BP_SpitterProjectileSingle(15)
    

    def Gravity Scale over Time__UpdateFunc(self):
        self.ExecuteUbergraph_BP_SpitterProjectileSingle(2524)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_SpitterProjectileSingle(2469)
    

    def BndEvt__mProjectileMovement_K2Node_ComponentBoundEvent_0_ActorComponentActivatedSignature__DelegateSignature(self, component: Ptr[ActorComponent], bReset: bool):
        ExecuteUbergraph_BP_SpitterProjectileSingle.K2Node_ComponentBoundEvent_Component = component #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SpitterProjectileSingle.K2Node_ComponentBoundEvent_bReset = bReset #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SpitterProjectileSingle(856)
    

    def PlayExplosionEffects(self):
        self.ExecuteUbergraph_BP_SpitterProjectileSingle(2153)
    

    def ExecuteUbergraph_BP_SpitterProjectileSingle(self):
        goto(ComputedJump("EntryPoint"))
        goto(ExecutionFlow.Pop())
        self.mProjectileMovement.Activate(False)
        ReturnValue1: Ptr[Actor] = self.GetOwner()
        AsFGEnemy1: Ptr[FGEnemy] = Cast[FGEnemy](ReturnValue1)
        bSuccess1: bool = AsFGEnemy1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue1_0: Ptr[Actor] = AsFGEnemy1.GetCurrentAggroTarget()
        ReturnValue: Ptr[SceneComponent] = ReturnValue1_0.K2_GetRootComponent()
        self.mProjectileMovement.HomingTargetComponent = ReturnValue
        goto(ExecutionFlow.Pop())
        # Label 274
        self.SetLifeSpan(1)
        ReturnValue1_1: Ptr[SphereComponent] = self.GetCollisionSphere()
        ReturnValue1_1.SetCollisionEnabled(0)
        goto(ExecutionFlow.Pop())
        # Label 352
        self.ReceiveBeginPlay()
        ExecutionFlow.Push("L726")
        ReturnValue_0: Ptr[PlayerController] = Default__GameplayStatics.GetPlayerController(self, 0)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue_0 = Default__GameplayStatics.GetPlayerController(self, 0)
        
        AsFGHUD = None
        Default__BPHUDHelpers.GetFGHud(ReturnValue_0, self, Ref[AsFGHUD])
        ReturnValue_2: Ptr[FGGameUI] = AsFGHUD.GetGameUI()
        ReturnValue_3: FText = Default__KismetSystemLibrary.MakeLiteralText()
        
        ReturnValue_2.ShowDirectionalSubtitle(self, 0, False, Ref[ReturnValue_3])
        goto(ExecutionFlow.Pop())
        # Label 726
        ReturnValue_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Spitter_Projectile_Loop, self, True)
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 16, UUID = 1270434869, ExecutionFunction = "ExecuteUbergraph_BP_SpitterProjectileSingle", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue_5: Ptr[Actor] = self.GetOwner()
        AsFGEnemy: Ptr[FGEnemy] = Cast[FGEnemy](ReturnValue_5)
        bSuccess: bool = AsFGEnemy
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_6: Vector = self.GetProjectileTargetLocation()
        ReturnValue_7: Vector = self.K2_GetActorLocation()
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_6)
        ReturnValue_8: Ptr[Actor] = AsFGEnemy.GetCurrentAggroTarget()
        ReturnValue_9: Vector = ReturnValue_8.GetVelocity()
        ReturnValue_10: float = VSize(ReturnValue_9)
        ReturnValue_11: float = FMin(ReturnValue_10, 800)
        ReturnValue_12: Vector = Normal(ReturnValue_9, 9.999999747378752e-05)
        ReturnValue_13: Vector = ReturnValue_12 * ReturnValue_11
        ReturnValue1_2: Vector = self.GetProjectileTargetLocation()
        ReturnValue3: Vector = self.K2_GetActorLocation()
        ReturnValue1_3: Vector = Subtract_VectorVector(ReturnValue1_2, ReturnValue3)
        ReturnValue1_4: float = VSize(ReturnValue1_3)
        ReturnValue_14: float = ReturnValue1_4 / 2000
        ReturnValue1_5: Vector = ReturnValue_13 * ReturnValue_14
        ReturnValue_15: Vector = ReturnValue1_5 + ReturnValue_6
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(ReturnValue_15)
        ReturnValue1_6: Vector = Vector(X1, Y1, Z)
        ReturnValue2: Vector = Subtract_VectorVector(ReturnValue1_6, ReturnValue_7)
        ReturnValue1_7: Vector = Normal(ReturnValue2, 9.999999747378752e-05)
        ReturnValue1_8: Vector = ReturnValue1_7 + Vector(0, 0, 0.05000000074505806)
        ReturnValue2_0: Vector = ReturnValue1_8 * 2000
        self.mProjectileMovement.Velocity = ReturnValue2_0
        self.Gravity_Scale_over_Time.PlayFromStart()
        goto(ExecutionFlow.Pop())
        # Label 1952
        ReturnValue1_9: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_Spitter_Projectile_Loop, self, True)
        ReturnValue1_10: Vector = self.K2_GetActorLocation()
        ReturnValue_16: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_E_Spitter_Projectile_Land, ReturnValue1_10, Rotator::FromPitchYawRoll(0, 0, 0))
        goto('L274')
        # Label 2112
        self.Projectile.Deactivate()
        goto('L1952')
        ReturnValue2_1: Vector = self.K2_GetActorLocation()
        ReturnValue_17: Ptr[SphereComponent] = self.GetCollisionSphere()
        ReturnValue_18: Vector = Vector(0, 0, ReturnValue_17.SphereRadius)
        ReturnValue_19: Vector = Subtract_VectorVector(ReturnValue2_1, ReturnValue_18)
        ReturnValue_20: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_SpitImpact_01, ReturnValue_19, Rotator::FromPitchYawRoll(0, 0, 0), Vector(0.699999988079071, 0.699999988079071, 0.699999988079071), True, 0)
        ReturnValue_20.SetVectorParameter("Color", Vector(3, 0.5, 0))
        goto('L2112')
        goto('L352')
        # Label 2474
        self.mProjectileMovement.ProjectileGravityScale = self.Gravity_Scale_over_Time_Gravity_Scale_02A6598A4993DE75B793A890687A4F4F
        goto(ExecutionFlow.Pop())
        goto('L2474')
    
