
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.RebarScatterGun.BP_RebarScatterProjectile import ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_OtherComp
from Script.Engine import FinishSpawningActor
from Script.Engine import Delay
from Script.Engine import SetActorEnableCollision
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Equipment.RebarScatterGun.BP_RebarScatterProjectile import ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_HitNormal
from Game.FactoryGame.Equipment.RebarScatterGun.BP_RebarScatterProjectile import ExecuteUbergraph_BP_RebarScatterProjectile
from Script.Engine import GetTransform
from Script.CoreUObject import Rotator
from Script.Engine import SpawnEmitterAtLocation
from Script.Engine import BreakTransform
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import ReceiveTick
from Game.FactoryGame.Equipment.RebarScatterGun.BP_RebarScatterProjectile import ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_CustomEvent_Player
from Game.FactoryGame.Equipment.RebarScatterGun.BP_RebarScatterProjectile import ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_Hit
from Game.FactoryGame.Equipment.RebarScatterGun.BP_RebarScatterProjectile import ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_HitLocation
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.Engine import DegreesToRadians
from Game.FactoryGame.Equipment.RebarScatterGun.BP_RebarScatterProjectile import ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_MyComp
from Game.FactoryGame.Equipment.RebarScatterGun.BP_RebarScatterProjectile import ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_NormalImpulse
from Script.Engine import SetBoolPropertyByName
from Script.Engine import Default__GameplayStatics
from Script.Engine import VInterpTo_Constant
from Script.Engine import ReceiveHit
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.Engine import Normal
from Script.Engine import EqualEqual_ObjectObject
from Script.Engine import ComposeRotators
from Script.Engine import K2_GetActorRotation
from Script.Engine import MakeRotator
from Game.FactoryGame.Equipment.RebarScatterGun.BP_RebarScatterProjectile import ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_DeltaSeconds
from Script.Engine import MakeTransform
from Script.Engine import Actor
from Script.Engine import ParticleSystemComponent
from Game.FactoryGame.Equipment.RebarScatterGun.BP_RebarScatterProjectile import ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_bSelfMoved
from Script.Engine import K2_GetActorLocation
from Script.Engine import K2_SetRelativeLocation
from Script.FactoryGame import RagdollCharacter
from Script.Engine import GetOwner
from Script.Engine import GetForwardVector
from Game.FactoryGame.VFX.Equipment.Weapons.RebarGun.P_RebarScatterSparks_01 import P_RebarScatterSparks_01
from Game.FactoryGame.Equipment.RebarScatterGun.BP_RebarScatterProjectile import ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_Other
from Game.FactoryGame.Equipment.RebarScatterGun.BP_RebarScatterProjectile import ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_CustomEvent_HitNormal
from Game.FactoryGame.Equipment.RebarScatterGun.BP_RebarScatterProjectile import BP_RebarScatterProjectile
from Script.CoreUObject import Transform
from Script.FactoryGame import FGProjectile
from Script.Engine import RandomUnitVectorInConeInRadians
from Script.Engine import RandomFloatInRange

class BP_RebarScatterProjectile(FGProjectile):
    mGravityScale: float = 0.75
    mGravityDelay: float = 0.15000000596046448
    mTargetRelativeTranslation: Vector = Namespace(X=-25, Y=0, Z=0)
    mScatterDelay: float = 0.05000000074505806
    mScatterAmountProjectiles: int32 = 5
    mSplitHalfAngle: float = 4
    mShouldSplit: bool = True
    mApplyGravity: bool
    mMinVelocityAdjustment: float = 0.5
    mMaxVelocityAdjustment: float = 1.5
    mProjectileData = Namespace(CanTriggerExplodeBySameClass=True, DamageType='/Script/FactoryGame.FGDamageType', DamageTypeExplode='/Script/FactoryGame.FGDamageType', ExplodeAtEndOfLife=False, ExplosionDamage=7, ExplosionRadius=0, ImpactDamage=7, ProjectileClass='/Game/FactoryGame/Equipment/RebarScatterGun/BP_RebarScatterProjectile.BP_RebarScatterProjectile_C', ProjectileLifeSpan=10, ProjectileStickSpan=5, ShouldExplodeOnImpact=False)
    mCollisionComp = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 14, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'Projectile', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', SphereRadius=8)
    mProjectileMovement = Namespace(InitialSpeed=5000, MaxSpeed=5000, ObjectClass='/Script/Engine.ProjectileMovementComponent', ObjectFlags=2883617, ObjectName='ProjectileComp', ProjectileGravityScale=0, bRotationFollowsVelocity=True)
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    RemoteRole = 1
    InitialLifeSpan = 3
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 14, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'Projectile', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', SphereRadius=8)
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_RebarScatterProjectile(167)
    

    def PlayAttachEffect(self):
        self.ExecuteUbergraph_BP_RebarScatterProjectile(416)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_RebarScatterProjectile(469)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_BP_RebarScatterProjectile(2343)
    

    def ReceiveHit(self):
        ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_MyComp = MyComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_Other = Other #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_bSelfMoved = bSelfMoved #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_HitLocation = HitLocation #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_HitNormal = HitNormal #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_NormalImpulse = NormalImpulse #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_Event_Hit = Hit #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_RebarScatterProjectile(2523)
    

    def Shot Player(self, Player: Ptr[FGCharacterPlayer], HitNormal: Vector):
        ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_CustomEvent_Player = Player #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_RebarScatterProjectile.K2Node_CustomEvent_HitNormal = HitNormal #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_RebarScatterProjectile(2864)
    

    def ExecuteUbergraph_BP_RebarScatterProjectile(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 92, UUID = 1007043278, ExecutionFunction = "ExecuteUbergraph_BP_RebarScatterProjectile", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        Player.RagdollCharacter(True)
        self.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        self.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        self.SetActorEnableCollision(True)
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L328")
        ExecutionFlow.Push("L237")
        if not self.mApplyGravity:
           goto(ExecutionFlow.Pop())
        self.mProjectileMovement.ProjectileGravityScale = self.mGravityScale
        goto(ExecutionFlow.Pop())
        # Label 237
        if not self.mShouldSplit:
           goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, self.mScatterDelay, LatentActionInfo(Linkage = 140, UUID = -1289208862, ExecutionFunction = "ExecuteUbergraph_BP_RebarScatterProjectile", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 328
        self.SetActorEnableCollision(False)
        Default__KismetSystemLibrary.Delay(self, 0.05000000074505806, LatentActionInfo(Linkage = 155, UUID = -1638801813, ExecutionFunction = "ExecuteUbergraph_BP_RebarScatterProjectile", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        
        SweepHitResult1 = None
        self.Rebar.K2_SetRelativeLocation(self.mTargetRelativeTranslation, False, True, Ref[SweepHitResult1])
        goto(ExecutionFlow.Pop())
        self.ReceiveTick(DeltaSeconds)
        ReturnValue: Vector = VInterpTo_Constant(self.Rebar.RelativeLocation, self.mTargetRelativeTranslation, DeltaSeconds, 100)
        
        SweepHitResult = None
        self.Rebar.K2_SetRelativeLocation(ReturnValue, True, False, Ref[SweepHitResult])
        goto(ExecutionFlow.Pop())
        # Label 623
        ExecutionFlow.Push("L2221")
        ReturnValue_0: Transform = self.GetTransform()
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_0], Ref[Location], Ref[Rotation], Ref[Scale])
        ReturnValue_1: Ptr[Actor] = self.GetOwner()
        ReturnValue_2: float = RandomFloatInRange(-10, 10)
        ReturnValue1: float = RandomFloatInRange(-10, 10)
        ReturnValue_3: Rotator = MakeRotator(0, ReturnValue_2, ReturnValue1)
        ReturnValue_4: Rotator = ComposeRotators(Rotation, ReturnValue_3)
        ReturnValue_5: Vector = GetForwardVector(ReturnValue_4)
        ReturnValue1_0: Vector = ReturnValue_5 * 20
        ReturnValue1_1: Vector = Location + ReturnValue1_0
        ReturnValue_6: Transform = MakeTransform(ReturnValue1_1, Rotation, Scale)
        
        ReturnValue_7: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_RebarScatterProjectile, 2, ReturnValue_1, Ref[ReturnValue_6])
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_7, "mShouldSplit", False)
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue_7, "mApplyGravity", True)
        ReturnValue_0 = self.GetTransform()
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_0], Ref[Location], Ref[Rotation], Ref[Scale])
        ReturnValue_2 = RandomFloatInRange(-10, 10)
        ReturnValue1 = RandomFloatInRange(-10, 10)
        ReturnValue_3 = MakeRotator(0, ReturnValue_2, ReturnValue1)
        ReturnValue_4 = ComposeRotators(Rotation, ReturnValue_3)
        ReturnValue_5 = GetForwardVector(ReturnValue_4)
        ReturnValue1_0 = ReturnValue_5 * 20
        ReturnValue1_1 = Location + ReturnValue1_0
        ReturnValue_6 = MakeTransform(ReturnValue1_1, Rotation, Scale)
        
        ReturnValue_8: Ptr[BP_RebarScatterProjectile] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_7, Ref[ReturnValue_6])
        ReturnValue_9: Vector = self.GetVelocity()
        ReturnValue_10: Vector = self.K2_GetActorLocation()
        ReturnValue1_2: Vector = self.K2_GetActorLocation()
        ReturnValue_11: Vector = ReturnValue1_2 + ReturnValue_9
        ReturnValue_12: Vector = Subtract_VectorVector(ReturnValue_11, ReturnValue_10)
        ReturnValue_13: float = self.mProjectileMovement.GetMaxSpeed()
        ReturnValue_14: Vector = Normal(ReturnValue_12, 9.999999747378752e-05)
        ReturnValue_15: float = DegreesToRadians(self.mSplitHalfAngle)
        ReturnValue_16: Vector = RandomUnitVectorInConeInRadians(ReturnValue_14, ReturnValue_15)
        ReturnValue_17: Vector = ReturnValue_16 * ReturnValue_13
        ReturnValue_8.mProjectileMovement.Velocity = ReturnValue_17
        goto(ExecutionFlow.Pop())
        # Label 2221
        ReturnValue_18: int32 = Variable + 1
        Variable: int32 = ReturnValue_18
        # Label 2290
        ReturnValue_19: bool = Variable <= self.mScatterAmountProjectiles
        if not ReturnValue_19:
           goto(ExecutionFlow.Pop())
        goto('L623')
        if not self.mShouldSplit:
           goto(ExecutionFlow.Pop())
        ReturnValue2: Vector = self.K2_GetActorLocation()
        ReturnValue_20: Rotator = self.K2_GetActorRotation()
        ReturnValue_21: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_RebarScatterSparks_01, ReturnValue2, ReturnValue_20, Vector(1, 1, 1), True, 0)
        Variable = 0
        goto('L2290')
        
        Hit = None
        self.ReceiveHit(MyComp, Other, OtherComp, bSelfMoved, HitLocation, HitNormal, NormalImpulse, Ref[Hit])
        self.Sparks_01.Deactivate()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](Other)
        bSuccess: bool = Player
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue1_3: Ptr[Actor] = self.GetOwner()
        ReturnValue2_0: Ptr[Actor] = ReturnValue1_3.GetOwner()
        ReturnValue_22: bool = EqualEqual_ObjectObject(Player, ReturnValue2_0)
        if not ReturnValue_22:
            goto('L2831')
        goto(ExecutionFlow.Pop())
        # Label 2831
        self.Shot Player(Player, HitNormal)
        goto(ExecutionFlow.Pop())
        ReturnValue2_1: Vector = HitNormal * -500
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue2_1)
        ReturnValue_23: Vector = Vector(X, Y, 0)
        ReturnValue2_2: Vector = ReturnValue_23 + Vector(0, 0, 400)
        Player.LaunchCharacter(ReturnValue2_2, False, False)
        goto('L15')
    
