
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Vehicle.Tractor.BP_Tractor import ExecuteUbergraph_BP_Tractor
from Script.FactoryGame import ShowOutline
from Game.FactoryGame.Buildable.Vehicle.Tractor.Animation.exhaustlockMontage import exhaustlockMontage
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ToggleFreeCamera
from Script.Engine import Delay
from Script.Engine import SetVisibility
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ReceiveOnVehicleShutDown
from Game.FactoryGame.Buildable.Vehicle.Tractor.Particle.ExhaustSmoke import ExhaustSmoke
from Script.Engine import SpawnEmitterAttached
from Script.CoreUObject import Rotator
from Game.FactoryGame.Buildable.Vehicle.VehicleWorkbench.Animation.CloseWorkbench_01_Montage import CloseWorkbench_01_Montage
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ReceiveOnVehicleStartup
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import SetIntensity
from Script.Engine import HasAuthority
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Buildable.Vehicle.VehicleWorkbench.Animation.OpenWorkbench_01_Montage import OpenWorkbench_01_Montage
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ReceiveBeginPlay
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Vehicle.Tractor.BP_Tractor import ExecuteUbergraph_BP_Tractor.K2Node_CustomEvent_FlashlightOn
from Script.Engine import Montage_Stop
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import UpdateOutline
from Script.Engine import Default__GameplayStatics
from Script.Engine import BreakRotator
from Script.Engine import FlushNetDormancy
from Script.FactoryGame import GetIsSignificant
from Script.CoreUObject import Vector
from Script.Engine import Montage_Play
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.Engine import MakeRotator
from Script.Engine import K2_DestroyComponent
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle4W import BP_WheeledVehicle4W
from Script.FactoryGame import LostSignificance
from Script.Engine import ParticleSystemComponent
from Script.Engine import K2_GetActorLocation
from Script.FactoryGame import EOutlineColor
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.FactoryGame import GainedSignificance
from Game.FactoryGame.Buildable.Vehicle.Tractor.BP_Tractor import ExecuteUbergraph_BP_Tractor.K2Node_InputActionEvent_Key
from Script.FactoryGame import IsDriving

class BP_Tractor(BP_WheeledVehicle4W):
    mExhaustVfx: Ptr[ParticleSystemComponent]
    mFlashlightOn: bool
    mEngineLoopStart = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Tractor/Audio/Rework/Play_V_Tractor_Rework_Engine.Play_V_Tractor_Rework_Engine')
    mEngineLoopStop = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Tractor/Audio/Rework/Stop_V_Tractor_Rework_Engine.Stop_V_Tractor_Rework_Engine')
    mTireLoopStart = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Tractor/Audio/Rework/Play_V_Tractor_Rework_Tires.Play_V_Tractor_Rework_Tires')
    mTireLoopStop = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Tractor/Audio/Rework/Stop_V_Tractor_Rework_Tires.Stop_V_Tractor_Rework_Tires')
    mEngineLoadRTPCName = T_Vehicle_RPM
    mVehicleSpeedRTPC = RTPC_Tractor_Speed
    mVehicleAccelerationStateRTPC = RTPC_Tractor_Load
    mHonkSound = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/-Shared/Audio/Play_Vehicle_Honks_Tractor.Play_Vehicle_Honks_Tractor')
    mMapText = NSLOCTEXT("", "7B5B65704E16949794FD889EB20A0991", "Tractor")
    mIsUsingNewAudioGears = True
    mAudioGearRTPC = RTPC_Tractor_Gears
    mRTPCOffloadState = RTPC_Tractor_OffloadState
    MPlayVehicleTransmission = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Tractor/Audio/Rework/Play_V_Tractor_Rework_Transmission.Play_V_Tractor_Rework_Transmission')
    mFuelConsumption = 55
    mDistBetweenDecals = 20
    mDecalLifespan = 5
    mTireTrackDecals = [{'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Sand.PhysMat_Sand'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Sand_Decal.Tiretrack_Sand_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Metal.PhysMat_Metal'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Cement.PhysMat_Cement'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Moist.PhysMat_Moist'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Decal.Tiretrack_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Rock.PhysMat_Rock'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Rock_Gravel.PhysMat_Rock_Gravel'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Soil.PhysMat_Soil'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Decal.Tiretrack_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Sand_Cracked.PhysMat_Sand_Cracked'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Grass_High.PhysMat_Grass_High'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Decal.Tiretrack_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Grass.PhysMat_Grass'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Decal.Tiretrack_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Coral.PhysMat_Coral'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Gravel.PhysMat_Gravel'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}]
    mDecalSize = Namespace(X=10, Y=50, Z=60)
    mFoliageDestroyRadius = 5000
    mAddedGroundAngularVelocityStrengthYaw = 10
    mAddedGroundAngularVelocityStrengthPitch = 2
    mAddedAirControlAngularVelocityStrengthYaw = 5
    mAddedAirControlAngularVelocityStrengthPitch = 2
    mNaturalAngularVelocityStrengthYaw = 5
    mNaturalAirAngularVelocityStrengthYaw = 1.5
    mNaturalAirAngularVelocityStrengthPitch = 1
    mAddedAngularVelocityInputSmoothingSpeed = 0.5
    mFoliageCollideBox = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', AttachParent={'$ObjectClass': '/Script/Engine.SkeletalMeshComponent', '$ObjectFlags': 2883617, '$ObjectName': 'VehicleMesh', 'AnimClass': '/Game/FactoryGame/Buildable/Vehicle/Tractor/Anim_Tractor.Anim_Tractor_C', 'ClothingSimulationFactory': '/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', 'SkeletalMesh': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Tractor/Mesh/Tractor.Tractor'}, 'bCastCapsuleDirectShadow': True, 'bGenerateOverlapEvents': True, 'bAllowCullDistanceVolume': False, 'BodyInstance': {'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 10, 'MassInKgOverride': 2397.367919921875, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': -75}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 300, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 16, 'VelocitySolverIterationCount': 8}}, BodyInstance={'ObjectType': 1, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WorldStatic', 'Response': 1}, {'Channel': 'WorldDynamic', 'Response': 1}, {'Channel': 'Pawn', 'Response': 1}, {'Channel': 'Visibility', 'Response': 1}, {'Channel': 'Camera', 'Response': 1}, {'Channel': 'PhysicsBody', 'Response': 1}, {'Channel': 'Vehicle', 'Response': 1}, {'Channel': 'Destructible', 'Response': 1}, {'Channel': 'Projectile', 'Response': 1}, {'Channel': 'BuildGun', 'Response': 1}, {'Channel': 'WeaponInstantHit', 'Response': 1}, {'Channel': 'VehicleWheelQuery', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, BoxExtent={'X': 250, 'Y': 250, 'Z': 200}, ObjectClass='/Script/Engine.BoxComponent', ObjectFlags=2883617, ObjectName='FoliageBox', RelativeLocation={'X': 0, 'Y': 0, 'Z': 170})
    mSimulationDistance = 20000
    mSimulationMovementComponent = Namespace(Acceleration=0, MaxSpeed=0, ObjectClass='/Script/Engine.FloatingPawnMovement', ObjectFlags=2883617, ObjectName='SimulationComponent', bReplicates=True)
    mInventorySize = 25
    mIsPathVisible = True
    mReverseAddedAngularVelocityYawMultiplier = 1
    mHasAirControl = True
    mGroundTraceLength = 300
    mMaxDeltaLinearVelocity = 100
    mMaxDeltaAngularVelocity = 550
    mRollStabilisationStrength = 0.026000000536441803
    mMaxRollAngleForUpsideDown = 85
    mMaxFlatOnGroundRollAngleLimit = 5
    mMaxRollForActivationOfAssistedVelocities = 75
    mMaxSpeedForAddedAcceleration = 80
    mMaxAssistedAcceleration = 1000
    mHasAssistedVelocities = True
    mMinAngleForDrift = 7
    mNeedsFuelToDrive = True
    mDisplayName = NSLOCTEXT("", "3C80F6D2411B0D61F992838E07608B47", "Tractor")
    mDescription = NSLOCTEXT("", "52610A3043223FCA6562F0A78D3B4778", "Fuel: Any fuel type\r\n\r\n25 slot inventory. Has a built in craft bench.\r\nCan be automated to pick up and deliver resources at truck stations.\r\n\r\nNicknamed the Sugarcube by FICSIT pioneers with the justification “it’s pretty sweet, y’know”.")
    mHologramClass = NewObject[FGVehicleHologram]()
    mMesh = Namespace(AnimClass='/Game/FactoryGame/Buildable/Vehicle/Tractor/Anim_Tractor.Anim_Tractor_C', BodyInstance={'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 10, 'MassInKgOverride': 2397.367919921875, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': -75}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 300, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 16, 'VelocitySolverIterationCount': 8}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='VehicleMesh', SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Tractor/Mesh/Tractor.Tractor'}, bAllowCullDistanceVolume=False, bCastCapsuleDirectShadow=True, bGenerateOverlapEvents=True)
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True, mCurrentHealth=1000, mMaxHealth=1000)
    mDisabledByWaterLocations = [{'X': 0, 'Y': 0, 'Z': 165}]
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mIsDestructible = True
    mSubmergedAngularDamping = 6
    mSubmergedLinearDamping = 15
    mSubmergedBouyantForce = 1000
    mAddToSignificanceManager = True
    mSignificanceRange = 4000
    mShouldAttachDriver = True
    mIsDriverVisible = True
    mDriverSeatSocket = driverSocket
    mDriverSeatAnimation = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Animation/ThirdPerson/TruckDriving.TruckDriving')
    mDriverExitOffset = Namespace(X=0, Y=300, Z=0)
    BaseEyeHeight = 200
    RootComponent = Namespace(AnimClass='/Game/FactoryGame/Buildable/Vehicle/Tractor/Anim_Tractor.Anim_Tractor_C', BodyInstance={'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 10, 'MassInKgOverride': 2397.367919921875, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': -75}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 300, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 16, 'VelocitySolverIterationCount': 8}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='VehicleMesh', SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Tractor/Mesh/Tractor.Tractor'}, bAllowCullDistanceVolume=False, bCastCapsuleDirectShadow=True, bGenerateOverlapEvents=True)
    
    def UpdateOutline(self):
        self.UpdateOutline(aimingAtWorkbench)
        Variable: bool = aimingAtWorkbench
        Variable_0: uint8 = 252
        Variable1: uint8 = 0
        
        switch = {
            False: Variable1,
            True: Variable_0
        }
        Default__FGBlueprintFunctionLibrary.ShowOutline(self.Workbench, switch.get(Variable, None))
    

    def StopDrivingEffects(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mExhaustVfx)
        if not ReturnValue:
            goto('L293')
        self.mExhaustVfx.K2_DestroyComponent(self)
        ReturnValue_0: Ptr[AnimInstance] = self.mMesh.GetAnimInstance()
        ReturnValue_1: bool = ReturnValue_0.Montage_IsPlaying(exhaustlockMontage)
        if not ReturnValue_1:
            goto('L293')
        ReturnValue_0 = self.mMesh.GetAnimInstance()
        ReturnValue_0.Montage_Stop(0.20000000298023224, exhaustlockMontage)
    

    def StartDrivingEffects(self):
        ReturnValue: bool = self.GetIsSignificant()
        if not ReturnValue:
            goto('L396')
        # Label 34
        ReturnValue_0: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(ExhaustSmoke, self.mMesh, "exhaustSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mExhaustVfx = ReturnValue_0
        ReturnValue_1: Ptr[AnimInstance] = self.mMesh.GetAnimInstance()
        ReturnValue_2: bool = ReturnValue_1.Montage_IsPlaying(exhaustlockMontage)
        if not ReturnValue_2:
            goto('L282')
        # End
        # Label 282
        ReturnValue_1 = self.mMesh.GetAnimInstance()
        ReturnValue_3: float = ReturnValue_1.Montage_Play(exhaustlockMontage, 1, 0, 0, True)
    

    def OnRep_mFlashlightOn(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L39')
        # Label 34
        # End
        # Label 39
        self.SpotLight.SetVisibility(self.mFlashlightOn, False)
    

    def ToggleFlashlight(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L111')
        # Label 34
        self.FlushNetDormancy()
        ReturnValue1: bool = Not_PreBool(self.mFlashlightOn)
        self.mFlashlightOn = ReturnValue1
        self.OnRep_mFlashlightOn()
        # End
        # Label 111
        ReturnValue_0: bool = Not_PreBool(self.mFlashlightOn)
        self.Server_SetFlashlightOn(ReturnValue_0)
        goto('L34')
    

    def GetEnemyTargetDesirability(self):
        ReturnValue = 0.5
    

    def GetAttackLocation(self):
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue_0: Vector = ReturnValue + Vector(0, 0, 150)
        ReturnValue_1: Vector = ReturnValue_0
    

    def ShouldAutoregisterAsTargetable(self):
        ReturnValue = True
    

    def InpActEvt_Flashlight_K2Node_InputActionEvent_0(self, Key: Key):
        ExecuteUbergraph_BP_Tractor.K2Node_InputActionEvent_Key = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Tractor(1474)
    

    def ToggleFreeCamera(self):
        self.ExecuteUbergraph_BP_Tractor(471)
    

    def ReceiveOnVehicleStartup(self):
        self.ExecuteUbergraph_BP_Tractor(818)
    

    def ReceiveOnVehicleShutDown(self):
        self.ExecuteUbergraph_BP_Tractor(843)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_Tractor(883)
    

    def Server_SetFlashlightOn(self, FlashlightOn: bool):
        ExecuteUbergraph_BP_Tractor.K2Node_CustomEvent_FlashlightOn = FlashlightOn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Tractor(888)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_BP_Tractor(1206)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_BP_Tractor(1340)
    

    def Multicast_CloseTrunk(self):
        self.ExecuteUbergraph_BP_Tractor(1479)
    

    def Multicast_OpenTrunk(self):
        self.ExecuteUbergraph_BP_Tractor(15)
    

    def ExecuteUbergraph_BP_Tractor(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue: Ptr[AnimInstance] = self.Workbench.GetAnimInstance()
        ReturnValue1: bool = ReturnValue.Montage_IsPlaying(OpenWorkbench_01_Montage)
        ReturnValue2: bool = Not_PreBool(ReturnValue1)
        if not ReturnValue2:
           goto(ExecutionFlow.Pop())
        ReturnValue = self.Workbench.GetAnimInstance()
        ReturnValue_0: float = ReturnValue.Montage_Play(OpenWorkbench_01_Montage, 1, 1, 0, True)
        Default__KismetSystemLibrary.Delay(self, ReturnValue_0, LatentActionInfo(Linkage = 342, UUID = 353813860, ExecutionFunction = "ExecuteUbergraph_BP_Tractor", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.SpotLight.SetIntensity(100)
        goto(ExecutionFlow.Pop())
        # Label 380
        self.OnRep_mFlashlightOn()
        self.SpotLight.SetVisibility(self.mFlashlightOn, False)
        goto(ExecutionFlow.Pop())
        # Label 437
        self.FlushNetDormancy()
        self.mFlashlightOn = FlashlightOn
        goto('L380')
        self.ToggleFreeCamera()
        ReturnValue_1: bool = Not_PreBool(self.mIsFreeCamera)
        self.SpringArm.bEnableCameraLag = ReturnValue_1
        ReturnValue_1 = Not_PreBool(self.mIsFreeCamera)
        self.SpringArm.bEnableCameraRotationLag = ReturnValue_1
        goto(ExecutionFlow.Pop())
        
        Roll = None
        Pitch = None
        Yaw = None
        # Label 622
        BreakRotator(self.SpringArm.RelativeRotation, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_2: Rotator = MakeRotator(0, Pitch, 0)
        self.mDefaultCameraRotation = ReturnValue_2
        goto(ExecutionFlow.Pop())
        # Label 765
        self.ReceiveBeginPlay()
        goto('L622')
        # Label 780
        self.SpotLight.SetIntensity(0)
        goto(ExecutionFlow.Pop())
        self.ReceiveOnVehicleStartup()
        self.StartDrivingEffects()
        goto(ExecutionFlow.Pop())
        self.ReceiveOnVehicleShutDown()
        if not self.mIsFollowingPath:
            goto('L868')
        goto(ExecutionFlow.Pop())
        # Label 868
        self.StopDrivingEffects()
        goto(ExecutionFlow.Pop())
        goto('L765')
        goto('L437')
        # Label 893
        ReturnValue = self.Workbench.GetAnimInstance()
        ReturnValue1_0: float = ReturnValue.Montage_Play(CloseWorkbench_01_Montage, 1, 0, 0, True)
        goto('L780')
        # Label 1012
        ReturnValue = self.Workbench.GetAnimInstance()
        ReturnValue_3: bool = ReturnValue.Montage_IsPlaying(CloseWorkbench_01_Montage)
        ReturnValue1_1: bool = Not_PreBool(ReturnValue_3)
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        goto('L893')
        # Label 1149
        self.ToggleFlashlight()
        self.SpotLight.SetVisibility(self.mFlashlightOn, False)
        goto(ExecutionFlow.Pop())
        self.GainedSignificance()
        self.mMesh.VisibilityBasedAnimTickOption = 0
        self.mMesh.SetComponentTickEnabled(True)
        ReturnValue_4: bool = self.IsDriving()
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        self.StartDrivingEffects()
        goto(ExecutionFlow.Pop())
        self.LostSignificance()
        self.mMesh.VisibilityBasedAnimTickOption = 3
        self.mMesh.SetComponentTickEnabled(False)
        ReturnValue1_2: bool = self.IsDriving()
        if not ReturnValue1_2:
           goto(ExecutionFlow.Pop())
        self.StopDrivingEffects()
        goto(ExecutionFlow.Pop())
        goto('L1149')
        goto('L1012')
    
