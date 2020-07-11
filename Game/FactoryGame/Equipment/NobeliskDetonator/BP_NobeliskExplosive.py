
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import GetDisplayName
from Script.AkAudio import PostAkEventAtLocation
from Script.Engine import SpawnEmitterAtLocation
from Game.FactoryGame.VFX.Equipment.Weapons.Nobelisk.P_Nobelisk_Explosion_01 import P_Nobelisk_Explosion_01
from Game.FactoryGame.Equipment.NobeliskDetonator.BP_NobeliskExplosive import ExecuteUbergraph_BP_NobeliskExplosive
from Game.FactoryGame.Character.Player.CameraShake.NobeliskExplosion_01 import NobeliskExplosion_01
from Script.Engine import SetHiddenInGame
from Script.FactoryGame import FGNobeliskExplosive
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Equipment.NobeliskDetonator.BP_NobeliskExplosive import ExecuteUbergraph_BP_NobeliskExplosive.K2Node_Event_NormalImpulse
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.Play_E_Nobelisk_Explosion import Play_E_Nobelisk_Explosion
from Script.CoreUObject import Object
from Script.Engine import IsValid
from Script.Engine import PlayWorldCameraShake
from Script.Engine import EqualEqual_StrStr
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.WorldDestruction.Play_Nobelisk_WorldDestruction_SmallRock import Play_Nobelisk_WorldDestruction_SmallRock
from Script.Engine import Default__GameplayStatics
from Script.Engine import BooleanOR
from Script.Engine import ReceiveHit
from Script.CoreUObject import Vector
from Script.Engine import MaterialInterface
from Script.Engine import Default__KismetStringLibrary
from Game.FactoryGame.Equipment.NobeliskDetonator.BP_NobeliskExplosive import ExecuteUbergraph_BP_NobeliskExplosive.K2Node_Event_Other
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.NobeliskDetonator.BP_NobeliskExplosive import ExecuteUbergraph_BP_NobeliskExplosive.K2Node_Event_bSelfMoved
from Game.FactoryGame.Equipment.NobeliskDetonator.BP_NobeliskExplosive import ExecuteUbergraph_BP_NobeliskExplosive.K2Node_Event_Hit
from Game.FactoryGame.Equipment.NobeliskDetonator.BP_NobeliskExplosive import ExecuteUbergraph_BP_NobeliskExplosive.K2Node_Event_OtherComp
from Script.Engine import PhysicalMaterial
from Script.Engine import ParticleSystemComponent
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.Equipment.NobeliskDetonator.BP_NobeliskExplosive import ExecuteUbergraph_BP_NobeliskExplosive.K2Node_Event_HitLocation
from Game.FactoryGame.Equipment.NobeliskDetonator.BP_NobeliskExplosive import ExecuteUbergraph_BP_NobeliskExplosive.K2Node_Event_MyComp
from Script.AkAudio import AkComponent
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.WorldDestruction.Play_Nobelisk_WorldDestruction_Tree import Play_Nobelisk_WorldDestruction_Tree
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.Play_E_Nobelisk_Explosion_StickBump import Play_E_Nobelisk_Explosion_StickBump
from Game.FactoryGame.Equipment.NobeliskDetonator.BP_NobeliskExplosive import ExecuteUbergraph_BP_NobeliskExplosive.K2Node_Event_HitNormal
from Script.Engine import NotEqual_StriStri

class BP_NobeliskExplosive(FGNobeliskExplosive):
    mPhysicalMaterialExplosion: FString
    mRotatingMovementComp = Namespace(ObjectClass='/Script/Engine.RotatingMovementComponent', ObjectFlags=2883617, ObjectName='RotatingMovementComponent', PrimaryComponentTick={'TickGroup': 0, 'EndTickGroup': 0, 'bTickEvenWhenPaused': False, 'bCanEverTick': True, 'bStartWithTickEnabled': False, 'bAllowTickOnDedicatedServer': True, 'TickInterval': 0}, bAutoActivate=False)
    mThrowRotation = Namespace(Pitch=-360, Roll=-180, Yaw=-35)
    mDestructionCollisionComp = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', AttachParent={'$ObjectClass': '/Script/Engine.SphereComponent', '$ObjectFlags': 2883617, '$ObjectName': 'SphereComp', 'SphereRadius': 12, 'AreaClass': '/Script/NavigationSystem.NavArea_Obstacle', 'CanCharacterStepUpOn': 0, 'BodyInstance': {'ObjectType': 14, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WeaponInstantHit', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}}, BodyInstance={'ObjectType': 1, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WorldStatic', 'Response': 1}, {'Channel': 'WorldDynamic', 'Response': 1}, {'Channel': 'Pawn', 'Response': 1}, {'Channel': 'Visibility', 'Response': 1}, {'Channel': 'Camera', 'Response': 1}, {'Channel': 'PhysicsBody', 'Response': 1}, {'Channel': 'Vehicle', 'Response': 1}, {'Channel': 'Destructible', 'Response': 1}, {'Channel': 'Projectile', 'Response': 1}, {'Channel': 'Resource', 'Response': 1}, {'Channel': 'BuildGun', 'Response': 1}, {'Channel': 'WeaponInstantHit', 'Response': 1}, {'Channel': 'VehicleWheelQuery', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='DestructionSphere', SphereRadius=750)
    mDestroysRelevantActors = True
    mDestroysFoliage = True
    mMaxParticleSpawnsPerDetonation = 10
    mCollisionComp = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 14, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WeaponInstantHit', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', SphereRadius=12)
    mProjectileMovement = Namespace(MaxSpeed=5000, ObjectClass='/Script/Engine.ProjectileMovementComponent', ObjectFlags=2883617, ObjectName='ProjectileComp', bInitialVelocityInLocalSpace=False)
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicateMovement = True
    bReplicates = True
    RemoteRole = 1
    InitialLifeSpan = 3
    RootComponent = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', BodyInstance={'ObjectType': 14, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': True, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WeaponInstantHit', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 3, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ObjectClass='/Script/Engine.SphereComponent', ObjectFlags=2883617, ObjectName='SphereComp', SphereRadius=12)
    
    def ShouldSave(self):
        ReturnValue = True
    

    def GatherDependencies(self):
        Array: List[Ptr[Object]] = []
        dependentObjects: List[Ptr[Object]] = Array
    

    def NeedTransform(self):
        ReturnValue = False
    

    def PlayExplosionEffects(self):
        self.ExecuteUbergraph_BP_NobeliskExplosive(1741)
    

    def ReceiveHit(self):
        ExecuteUbergraph_BP_NobeliskExplosive.K2Node_Event_MyComp = MyComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_NobeliskExplosive.K2Node_Event_Other = Other #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_NobeliskExplosive.K2Node_Event_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_NobeliskExplosive.K2Node_Event_bSelfMoved = bSelfMoved #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_NobeliskExplosive.K2Node_Event_HitLocation = HitLocation #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_NobeliskExplosive.K2Node_Event_HitNormal = HitNormal #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_NobeliskExplosive.K2Node_Event_NormalImpulse = NormalImpulse #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_NobeliskExplosive.K2Node_Event_Hit = Hit #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_NobeliskExplosive(964)
    

    def ExecuteUbergraph_BP_NobeliskExplosive(self):
        # Label 10
        CmpSuccess: bool = Default__KismetStringLibrary.NotEqual_StriStri(self.mPhysicalMaterialExplosion, "PhysMat_Rock")
        if not CmpSuccess:
            goto('L173')
        CmpSuccess = Default__KismetStringLibrary.NotEqual_StriStri(self.mPhysicalMaterialExplosion, "PhysMat_Tree")
        if not CmpSuccess:
            goto('L280')
        # End
        # Label 173
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_Nobelisk_WorldDestruction_SmallRock, ReturnValue, Rotator::FromPitchYawRoll(0, 0, 0))
        # End
        # Label 280
        ReturnValue = self.K2_GetActorLocation()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_Nobelisk_WorldDestruction_Tree, ReturnValue, Rotator::FromPitchYawRoll(0, 0, 0))
        # End
        # Label 387
        self.NobelisExplosive_Skel.SetHiddenInGame(True, True)
        self.RadialForce.FireImpulse()
        ReturnValue2_0: Vector = self.K2_GetActorLocation()
        ReturnValue_1: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_Nobelisk_Explosion_01, ReturnValue2_0, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        ReturnValue1: Vector = self.K2_GetActorLocation()
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_E_Nobelisk_Explosion, ReturnValue1, Rotator::FromPitchYawRoll(0, 0, 0))
        ReturnValue1 = self.K2_GetActorLocation()
        Default__GameplayStatics.PlayWorldCameraShake(self, NobeliskExplosion_01, ReturnValue1, 0, 10000, 1, 1, False)
        ReturnValue_2: bool = Default__KismetStringLibrary.EqualEqual_StrStr(self.mPhysicalMaterialExplosion, "PhysMat_Tree")
        ReturnValue3: bool = Default__KismetStringLibrary.EqualEqual_StrStr(self.mPhysicalMaterialExplosion, "PhysMat_Rock")
        ReturnValue1_1: bool = BooleanOR(ReturnValue3, ReturnValue_2)
        if not ReturnValue1_1:
            goto('L1746')
        goto('L10')
        
        Hit = None
        self.ReceiveHit(MyComp, Other, OtherComp, bSelfMoved, HitLocation, HitNormal, NormalImpulse, Ref[Hit])
        ReturnValue_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Nobelisk_Explosion_StickBump, self, True)
        ReturnValue_4: Ptr[MaterialInterface] = OtherComp.GetMaterial(0)
        ReturnValue_5: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_4)
        if not ReturnValue_5:
            goto('L1746')
        ReturnValue_4 = OtherComp.GetMaterial(0)
        ReturnValue_6: Ptr[PhysicalMaterial] = ReturnValue_4.GetPhysicalMaterial()
        ReturnValue_7: FString = Default__KismetSystemLibrary.GetDisplayName(ReturnValue_6)
        ReturnValue1_2: bool = Default__KismetStringLibrary.EqualEqual_StrStr(ReturnValue_7, "PhysMat_Tree")
        ReturnValue2_1: bool = Default__KismetStringLibrary.EqualEqual_StrStr(ReturnValue_7, "PhysMat_Rock")
        ReturnValue_8: bool = BooleanOR(ReturnValue2_1, ReturnValue1_2)
        if not ReturnValue_8:
            goto('L1746')
        ReturnValue_4 = OtherComp.GetMaterial(0)
        ReturnValue_6 = ReturnValue_4.GetPhysicalMaterial()
        ReturnValue_7 = Default__KismetSystemLibrary.GetDisplayName(ReturnValue_6)
        self.mPhysicalMaterialExplosion = ReturnValue_7
        # End
        goto('L387')
    
