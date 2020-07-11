
from codegen.ue4_stub import *

from Script.Engine import ParticleSystemComponent
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import Default__FGResourceDescriptor
from Script.FactoryGame import IsDepositEmpty
from Game.FactoryGame.Resource.BP_ResourceDeposit import ExecuteUbergraph_BP_ResourceDeposit.K2Node_Event_descriptor
from Script.Engine import ParticleSystem
from Script.FactoryGame import GetDestroyedParticle
from Script.FactoryGame import FGResourceDeposit
from Script.CoreUObject import Vector
from Script.AkAudio import PostAkEventAtLocation
from Script.Engine import SpawnEmitterAtLocation
from Script.Engine import K2_GetComponentLocation
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import ReceiveBeginPlay
from Game.FactoryGame.Resource.BP_ResourceDeposit import ExecuteUbergraph_BP_ResourceDeposit
from Script.Engine import SetHiddenInGame
from Game.FactoryGame.Equipment.ResourceCollector.Audio.Play_ManualMining_Explosion import Play_ManualMining_Explosion

class BP_ResourceDeposit(FGResourceDeposit):
    mResourceDepositTableIndex = -1
    mDepositMeshComponent = Namespace(BodyInstance={'ObjectType': 1, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'VehicleWheelQuery', 'Response': 2}, {'Channel': 'Clearance', 'Response': 1}, {'Channel': 'HologramClearance', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CachedMaxDrawDistance=62500, LDMaxDrawDistance=62500, Mobility=0, ObjectClass='/Script/Engine.StaticMeshComponent', ObjectFlags=2883617, ObjectName='DepositMesh', OverrideMaterials=[{'$AssetPath': '/Game/FactoryGame/Resource/RawResources/Deposits/Materials/Deposit_Bauxite_Inst.Deposit_Bauxite_Inst'}], StaticMesh={'$AssetPath': '/Game/FactoryGame/Resource/RawResources/Deposits/Deposit_01.Deposit_01'})
    mPurity = 1
    mAmount = 3
    mExtractMultiplier = 2
    mPurityTextArray = [{'text': 'NSLOCTEXT("", "50EB38D644C570283BC30ABC48A1643E", "Inpure")', 'Purity': 0}, {'text': 'NSLOCTEXT("", "FE107A5642BD3DC43503A99FD87EB93A", "Normal")', 'Purity': 1}, {'text': 'NSLOCTEXT("", "B57D3BC14B88B888E0D37DB7249DB5FB", "Pure")', 'Purity': 2}]
    mDoSpawnParticle = True
    bReplicates = True
    RemoteRole = 1
    RootComponent = Namespace(BodyInstance={'ObjectType': 1, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'VehicleWheelQuery', 'Response': 2}, {'Channel': 'Clearance', 'Response': 1}, {'Channel': 'HologramClearance', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CachedMaxDrawDistance=62500, LDMaxDrawDistance=62500, Mobility=0, ObjectClass='/Script/Engine.StaticMeshComponent', ObjectFlags=2883617, ObjectName='DepositMesh', OverrideMaterials=[{'$AssetPath': '/Game/FactoryGame/Resource/RawResources/Deposits/Materials/Deposit_Bauxite_Inst.Deposit_Bauxite_Inst'}], StaticMesh={'$AssetPath': '/Game/FactoryGame/Resource/RawResources/Deposits/Deposit_01.Deposit_01'})
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_ResourceDeposit(265)
    

    def PlayDepletedEffect(self):
        ExecuteUbergraph_BP_ResourceDeposit.K2Node_Event_descriptor = Descriptor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_ResourceDeposit(270)
    

    def ExecuteUbergraph_BP_ResourceDeposit(self):
        # Label 10
        ReturnValue: bool = self.IsDepositEmpty()
        if not ReturnValue:
            goto('L538')
        self.mDepositMeshComponent.SetHiddenInGame(True, False)
        self.mDepositMeshComponent.SetCollisionEnabled(0)
        # End
        # Label 121
        self.ReceiveBeginPlay()
        goto('L10')
        # Label 136
        ReturnValue_0: Vector = self.mDepositMeshComponent.K2_GetComponentLocation()
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_ManualMining_Explosion, ReturnValue_0, Rotator::FromPitchYawRoll(0, 0, 0))
        # End
        goto('L121')
        ReturnValue_0 = self.mDepositMeshComponent.K2_GetComponentLocation()
        ReturnValue_2: Ptr[ParticleSystem] = Default__FGResourceDescriptor.GetDestroyedParticle(descriptor)
        ReturnValue_3: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, ReturnValue_2, ReturnValue_0, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        self.mDepositMeshComponent.SetHiddenInGame(True, False)
        self.mDepositMeshComponent.SetCollisionEnabled(0)
        goto('L136')
    
