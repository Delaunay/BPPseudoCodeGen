
from codegen.ue4_stub import *

from Script.Engine import Delay
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Equipment.RebarGun.BP_RebarProjectile import ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_HitNormal
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import ReceiveTick
from Game.FactoryGame.Equipment.RebarGun.BP_RebarProjectile import ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_OtherComp
from Game.FactoryGame.Equipment.RebarGun.BP_RebarProjectile import ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_HitLocation
from Game.FactoryGame.Equipment.RebarGun.BP_RebarProjectile import ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_DeltaSeconds
from Game.FactoryGame.Equipment.RebarGun.BP_RebarProjectile import ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_Hit
from Script.Engine import VInterpTo_Constant
from Game.FactoryGame.Equipment.RebarGun.BP_RebarProjectile import ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_Other
from Script.Engine import ReceiveHit
from Script.CoreUObject import Vector
from Script.Engine import EqualEqual_ObjectObject
from Game.FactoryGame.Equipment.RebarGun.BP_RebarProjectile import ExecuteUbergraph_BP_RebarProjectile.K2Node_CustomEvent_Player
from Script.Engine import Actor
from Game.FactoryGame.Equipment.RebarGun.BP_RebarProjectile import ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_MyComp
from Game.FactoryGame.Equipment.RebarGun.BP_RebarProjectile import ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_bSelfMoved
from Script.Engine import K2_SetRelativeLocation
from Script.FactoryGame import RagdollCharacter
from Script.Engine import GetOwner
from Game.FactoryGame.Equipment.RebarGun.BP_RebarProjectile import ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_NormalImpulse
from Game.FactoryGame.Equipment.RebarGun.BP_RebarProjectile import ExecuteUbergraph_BP_RebarProjectile.K2Node_CustomEvent_HitNormal
from Game.FactoryGame.Equipment.RebarGun.BP_RebarProjectile import ExecuteUbergraph_BP_RebarProjectile
from Script.FactoryGame import FGProjectile

class BP_RebarProjectile(FGProjectile):
    mGravityScale: float = 0.5
    mGravityDelay: float = 0.10000000149011612
    mTargetRelativeTranslation: Vector = Namespace(X=-25, Y=0, Z=0)
    mProjectileData = Namespace(CanTriggerExplodeBySameClass=True, DamageType='/Game/FactoryGame/Equipment/RebarGun/DamageType_RebarGunProjectile.DamageType_RebarGunProjectile_C', DamageTypeExplode='/Script/FactoryGame.FGDamageType', ExplodeAtEndOfLife=False, ExplosionDamage=100, ExplosionRadius=300, ImpactDamage=0, ProjectileClass='None', ProjectileLifeSpan=10, ProjectileStickSpan=5, ShouldExplodeOnImpact=True)
    mCollisionComp = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 14, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Projectile', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WeaponInstantHit', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', SphereRadius=8)
    mProjectileMovement = Namespace(InitialSpeed=5000, MaxSpeed=5000, ObjectClass='/Script/Engine.ProjectileMovementComponent', ObjectFlags=2883617, ObjectName='ProjectileComp', ProjectileGravityScale=0, bRotationFollowsVelocity=True)
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    RemoteRole = 1
    InitialLifeSpan = 5
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 14, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Projectile', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WeaponInstantHit', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', SphereRadius=8)
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_RebarProjectile(1112)
    

    def PlayAttachEffect(self):
        self.ExecuteUbergraph_BP_RebarProjectile(372)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_RebarProjectile(425)
    

    def ReceiveHit(self):
        ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_MyComp = MyComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_Other = Other #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_bSelfMoved = bSelfMoved #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_HitLocation = HitLocation #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_HitNormal = HitNormal #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_NormalImpulse = NormalImpulse #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_RebarProjectile.K2Node_Event_Hit = Hit #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_RebarProjectile(712)
    

    def Shot Player(self, Player: Ptr[FGCharacterPlayer], HitNormal: Vector):
        ExecuteUbergraph_BP_RebarProjectile.K2Node_CustomEvent_Player = Player #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_RebarProjectile.K2Node_CustomEvent_HitNormal = HitNormal #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_RebarProjectile(799)
    

    def ExecuteUbergraph_BP_RebarProjectile(self):
        goto(ComputedJump("EntryPoint"))
        self.mProjectileMovement.ProjectileGravityScale = self.mGravityScale
        goto(ExecutionFlow.Pop())
        # Label 65
        self.Sparks_01.Deactivate()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](Other)
        bSuccess: bool = Player
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue: Ptr[Actor] = self.GetOwner()
        ReturnValue1: Ptr[Actor] = ReturnValue.GetOwner()
        ReturnValue_0: bool = EqualEqual_ObjectObject(Player, ReturnValue1)
        if not ReturnValue_0:
            goto('L291')
        goto(ExecutionFlow.Pop())
        # Label 291
        self.Shot Player(Player, HitNormal)
        goto(ExecutionFlow.Pop())
        Player_0.RagdollCharacter(True)
        self.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        
        SweepHitResult = None
        self.Rebar.K2_SetRelativeLocation(self.mTargetRelativeTranslation, False, True, Ref[SweepHitResult])
        goto(ExecutionFlow.Pop())
        self.ReceiveTick(DeltaSeconds)
        ReturnValue_1: Vector = VInterpTo_Constant(self.Rebar.RelativeLocation, self.mTargetRelativeTranslation, DeltaSeconds, 100)
        
        SweepHitResult1 = None
        self.Rebar.K2_SetRelativeLocation(ReturnValue_1, True, False, Ref[SweepHitResult1])
        
        SweepHitResult1 = None
        self.Sparks_01.K2_SetRelativeLocation(ReturnValue_1, True, False, Ref[SweepHitResult1])
        goto(ExecutionFlow.Pop())
        # Label 631
        Default__KismetSystemLibrary.Delay(self, self.mGravityDelay, LatentActionInfo(Linkage = 15, UUID = 284149783, ExecutionFunction = "ExecuteUbergraph_BP_RebarProjectile", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        
        Hit = None
        self.ReceiveHit(MyComp, Other, OtherComp, bSelfMoved, HitLocation, HitNormal, NormalImpulse, Ref[Hit])
        goto('L65')
        ReturnValue_2: Vector = HitNormal * -500
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_2)
        ReturnValue_3: Vector = Vector(X, Y, 0)
        ReturnValue_4: Vector = ReturnValue_3 + Vector(0, 0, 400)
        Player_0.LaunchCharacter(ReturnValue_4, False, False)
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 324, UUID = 1312010289, ExecutionFunction = "ExecuteUbergraph_BP_RebarProjectile", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L631')
    
