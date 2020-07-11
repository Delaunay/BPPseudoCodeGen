
from codegen.ue4_stub import *

from Script.Engine import Delay
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Pawn
from Script.Engine import VSize
from Script.Engine import ReceiveBeginPlay
from Script.Engine import LatentActionInfo
from Script.Engine import GetPlayerPawn
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Creature.Enemy.Spitter.DamageType_SpitterMelee import DamageType_SpitterMelee
from Script.Engine import IsValid
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterMelee import ExecuteUbergraph_BP_SpitterMelee.K2Node_CustomEvent_PSystem
from Script.Engine import CurveFloat
from Script.Engine import Default__GameplayStatics
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterMelee import ExecuteUbergraph_BP_SpitterMelee.K2Node_CustomEvent_PSystem1
from Script.Engine import ApplyDamage
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterMelee import ExecuteUbergraph_BP_SpitterMelee.K2Node_CustomEvent_PSystem2
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Script.FactoryGame import RagdollCharacter
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterMelee import ExecuteUbergraph_BP_SpitterMelee.K2Node_Event_OtherActor
from Script.Engine import GetOwner
from Game.FactoryGame.Character.Creature.Enemy.Spitter.BP_SpitterMelee import ExecuteUbergraph_BP_SpitterMelee
from Script.Engine import GetDirectionUnitVector
from Script.FactoryGame import FGProjectile
from Script.Engine import ReceiveActorBeginOverlap

class BP_SpitterMelee(FGProjectile):
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
    Triggered: bool
    mPlayerAirControl: float
    mLimitAirControl: bool
    mRagdollPlayer: bool
    mProjectileData = Namespace(CanTriggerExplodeBySameClass=True, DamageType='/Game/FactoryGame/Character/Creature/Enemy/Spitter/DamageType_SpitterProjectile.DamageType_SpitterProjectile_C', DamageTypeExplode='/Script/FactoryGame.FGDamageType', ExplodeAtEndOfLife=False, ExplosionDamage=40, ExplosionRadius=250, ImpactDamage=20, ProjectileClass='/Game/FactoryGame/Character/Creature/Enemy/Spitter/BP_SpitterMelee.BP_SpitterMelee_C', ProjectileLifeSpan=10, ProjectileStickSpan=0, ShouldExplodeOnImpact=True)
    mCollisionComp = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 0, 'CollisionEnabled': 0, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'NoCollision', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WorldStatic', 'Response': 0}, {'Channel': 'WorldDynamic', 'Response': 0}, {'Channel': 'Pawn', 'Response': 0}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Camera', 'Response': 0}, {'Channel': 'PhysicsBody', 'Response': 0}, {'Channel': 'Vehicle', 'Response': 0}, {'Channel': 'Destructible', 'Response': 0}, {'Channel': 'Projectile', 'Response': 0}, {'Channel': 'Resource', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', OnComponentHit=0, RelativeScale3D={'X': 2, 'Y': 2, 'Z': 2}, SphereRadius=16, bCanEverAffectNavigation=False)
    mProjectileMovement = Namespace(ObjectClass='/Script/Engine.ProjectileMovementComponent', ObjectFlags=2883617, ObjectName='ProjectileComp', ProjectileGravityScale=0, bAutoActivate=False, bInitialVelocityInLocalSpace=False)
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicateMovement = True
    bReplicates = True
    RemoteRole = 1
    InitialLifeSpan = 3
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 0, 'CollisionEnabled': 0, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'NoCollision', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WorldStatic', 'Response': 0}, {'Channel': 'WorldDynamic', 'Response': 0}, {'Channel': 'Pawn', 'Response': 0}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Camera', 'Response': 0}, {'Channel': 'PhysicsBody', 'Response': 0}, {'Channel': 'Vehicle', 'Response': 0}, {'Channel': 'Destructible', 'Response': 0}, {'Channel': 'Projectile', 'Response': 0}, {'Channel': 'Resource', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', OnComponentHit=0, RelativeScale3D={'X': 2, 'Y': 2, 'Z': 2}, SphereRadius=16, bCanEverAffectNavigation=False)
    
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
    

    def ReceiveActorBeginOverlap(self):
        ExecuteUbergraph_BP_SpitterMelee.K2Node_Event_OtherActor = OtherActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SpitterMelee(1275)
    

    def DestroyOnParticleDone(self, PSystem: Ptr[ParticleSystemComponent]):
        ExecuteUbergraph_BP_SpitterMelee.K2Node_CustomEvent_PSystem2 = PSystem #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SpitterMelee(1389)
    

    def DestroyWithRagdoll(self, PSystem: Ptr[ParticleSystemComponent]):
        ExecuteUbergraph_BP_SpitterMelee.K2Node_CustomEvent_PSystem1 = PSystem #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SpitterMelee(1394)
    

    def DestroyWithAirC(self, PSystem: Ptr[ParticleSystemComponent]):
        ExecuteUbergraph_BP_SpitterMelee.K2Node_CustomEvent_PSystem = PSystem #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SpitterMelee(1486)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_SpitterMelee(1563)
    

    def ExecuteUbergraph_BP_SpitterMelee(self):
        goto(ComputedJump("EntryPoint"))
        if not self.Triggered:
            goto('L30')
        goto(ExecutionFlow.Pop())
        # Label 30
        self.Triggered = True
        # Label 41
        self.Sphere1.SetCollisionEnabled(0)
        OutputDelegate2.BindUFunction(self, DestroyOnParticleDone)
        self.ParticleSystem.OnSystemFinished.AddUnique(OutputDelegate2)
        goto(ExecutionFlow.Pop())
        Player.RagdollCharacter(True)
        self.Sphere1.SetCollisionEnabled(0)
        OutputDelegate1.BindUFunction(self, DestroyWithRagdoll)
        self.ParticleSystem.OnSystemFinished.AddUnique(OutputDelegate1)
        goto(ExecutionFlow.Pop())
        Player.RagdollCharacter(False)
        self.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        Player.CharacterMovement.AirControl = self.mPlayerAirControl
        self.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        # Label 414
        Default__KismetSystemLibrary.Delay(self, 0, LatentActionInfo(Linkage = 15, UUID = 1415966430, ExecutionFunction = "ExecuteUbergraph_BP_SpitterMelee", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 491
        self.Triggered = True
        ReturnValue: float = Default__GameplayStatics.ApplyDamage(Player, 10, None, None, DamageType_SpitterMelee)
        ReturnValue_0: Vector = Player.K2_GetActorLocation()
        ReturnValue_1: Ptr[Actor] = self.GetOwner()
        ReturnValue1: Vector = ReturnValue_1.K2_GetActorLocation()
        ReturnValue_2: Vector = GetDirectionUnitVector(ReturnValue1, ReturnValue_0)
        ReturnValue_3: Vector = ReturnValue_2 * 1500
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_3)
        ReturnValue_4: Vector = Vector(X, Y, 1000)
        Player.LaunchCharacter(ReturnValue_4, True, True)
        if not self.mRagdollPlayer:
            goto('L1020')
        Default__KismetSystemLibrary.Delay(self, 0.05000000074505806, LatentActionInfo(Linkage = 144, UUID = 2107533048, ExecutionFunction = "ExecuteUbergraph_BP_SpitterMelee", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1020
        if not self.mLimitAirControl:
            goto('L41')
        self.mPlayerAirControl = Player.CharacterMovement.AirControl
        Player.CharacterMovement.AirControl = 0
        self.Sphere1.SetCollisionEnabled(0)
        OutputDelegate.BindUFunction(self, DestroyWithAirC)
        self.ParticleSystem.OnSystemFinished.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        self.ReceiveActorBeginOverlap(OtherActor)
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](OtherActor)
        bSuccess: bool = Player
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        goto('L491')
        # Label 1374
        self.K2_DestroyActor()
        goto(ExecutionFlow.Pop())
        goto('L1374')
        Default__KismetSystemLibrary.Delay(self, 1.5, LatentActionInfo(Linkage = 280, UUID = -953419367, ExecutionFunction = "ExecuteUbergraph_BP_SpitterMelee", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1471
        self.ReceiveBeginPlay()
        goto('L414')
        Default__KismetSystemLibrary.Delay(self, 1, LatentActionInfo(Linkage = 328, UUID = 94626385, ExecutionFunction = "ExecuteUbergraph_BP_SpitterMelee", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        goto('L1471')
    
