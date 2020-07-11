
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_Icon_truck import MapCompass_Icon_truck
from Script.FactoryGame import ShowOutline
from Script.Engine import Delay
from Script.Engine import SetVisibility
from Game.FactoryGame.Buildable.Vehicle.VehicleWorkbench.Animation.CloseWorkbench_01_Montage import CloseWorkbench_01_Montage
from Script.Engine import Not_PreBool
from Game.FactoryGame.Buildable.Vehicle.Truck.BP_Truck import ExecuteUbergraph_BP_Truck.K2Node_InputActionEvent_Key
from Script.Engine import LatentActionInfo
from Script.Engine import SetIntensity
from Script.Engine import HasAuthority
from Game.FactoryGame.Buildable.Vehicle.VehicleWorkbench.Animation.OpenWorkbench_01_Montage import OpenWorkbench_01_Montage
from Script.Engine import GetAnimInstance
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Vehicle.Truck.BP_Truck import ExecuteUbergraph_BP_Truck.K2Node_CustomEvent_FlashlightOn
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import UpdateOutline
from Game.FactoryGame.Buildable.Vehicle.Truck.BP_Truck import ExecuteUbergraph_BP_Truck
from Script.Engine import FlushNetDormancy
from Script.CoreUObject import Vector
from Script.Engine import Montage_Play
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.FactoryGame import LostSignificance
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle6W import BP_WheeledVehicle6W
from Script.FactoryGame import EOutlineColor
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.FactoryGame import GainedSignificance

class BP_Truck(BP_WheeledVehicle6W):
    mFlashlightOn: bool
    mEngineSocketName = Truck_AudioSocket_Engine
    mEngineLoopStart = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Truck/Audio/Rework/Play_Truck_Rework_Engine.Play_Truck_Rework_Engine')
    mEngineLoopStop = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Truck/Audio/Rework/Stop_Truck_Rework_Engine.Stop_Truck_Rework_Engine')
    mExhaustSocketName = Truck_AudioSocket_Exhaust
    mTireLoopStart = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Truck/Audio/Rework/Play_Truck_Rework_Tires.Play_Truck_Rework_Tires')
    mTireLoopStop = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Truck/Audio/Rework/Stop_Truck_Rework_Tires.Stop_Truck_Rework_Tires')
    mVehicleSpeedRTPC = RTPC_Truck_Speed
    mVehicleAccelerationStateRTPC = RTPC_Truck_Load
    mHonkSound = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/-Shared/Audio/Play_Vehicle_Honks_Truck.Play_Vehicle_Honks_Truck')
    mMapText = NSLOCTEXT("", "C6E446454C28565CE598B6BE33DEF086", "Truck")
    mIsUsingNewAudioGears = True
    mAudioGearRTPC = RTPC_Truck_Gears
    mRTPCOffloadState = RTPC_Truck_OffloadState
    MPlayVehicleTransmission = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Truck/Audio/Rework/Play_Truck_Rework_Transmission.Play_Truck_Rework_Transmission')
    mFuelConsumption = 75
    mDistBetweenDecals = 80
    mDecalLifespan = 5
    mTireTrackDecals = [{'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Cement.PhysMat_Cement'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Coral.PhysMat_Coral'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Grass.PhysMat_Grass'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Decal.Tiretrack_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Grass_High.PhysMat_Grass_High'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Decal.Tiretrack_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Gravel.PhysMat_Gravel'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Metal.PhysMat_Metal'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Moist.PhysMat_Moist'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Sand_Decal.Tiretrack_Sand_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Rock.PhysMat_Rock'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Rock_Gravel.PhysMat_Rock_Gravel'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Sand.PhysMat_Sand'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Sand_Decal.Tiretrack_Sand_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Sand_Cracked.PhysMat_Sand_Cracked'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Soil.PhysMat_Soil'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Decal.Tiretrack_Decal'}}]
    mDecalSize = Namespace(X=10, Y=110, Z=120)
    mFoliageDestroyRadius = 575
    mAddedGroundAngularVelocityStrengthYaw = 45
    mAddedGroundAngularVelocityStrengthPitch = 60
    mAddedAirControlAngularVelocityStrengthYaw = 75
    mAddedAirControlAngularVelocityStrengthPitch = 50
    mNaturalAngularVelocityStrengthYaw = 25
    mNaturalAngularVelocityStrengthPitch = 15
    mNaturalAirAngularVelocityStrengthYaw = 20
    mNaturalAirAngularVelocityStrengthPitch = 10
    mAddedAngularVelocityInputSmoothingSpeed = 0.10000000149011612
    mFoliageCollideBox = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', AttachParent={'$ObjectClass': '/Script/Engine.SkeletalMeshComponent', '$ObjectFlags': 2883617, '$ObjectName': 'VehicleMesh', 'AnimClass': '/Game/FactoryGame/Buildable/Vehicle/Truck/Anim_Truck.Anim_Truck_C', 'ClothingSimulationFactory': '/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', 'SkeletalMesh': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Truck/Mesh/Truck.Truck'}, 'bGenerateOverlapEvents': True, 'bAllowCullDistanceVolume': False, 'BodyInstance': {'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 2401, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 100, 'Y': 0, 'Z': 0}, 'MassScale': 10, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}}, BodyInstance={'ObjectType': 1, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WorldStatic', 'Response': 1}, {'Channel': 'WorldDynamic', 'Response': 1}, {'Channel': 'Pawn', 'Response': 1}, {'Channel': 'Visibility', 'Response': 1}, {'Channel': 'Camera', 'Response': 1}, {'Channel': 'PhysicsBody', 'Response': 1}, {'Channel': 'Vehicle', 'Response': 1}, {'Channel': 'Destructible', 'Response': 1}, {'Channel': 'Projectile', 'Response': 1}, {'Channel': 'BuildGun', 'Response': 1}, {'Channel': 'WeaponInstantHit', 'Response': 1}, {'Channel': 'VehicleWheelQuery', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, BoxExtent={'X': 560, 'Y': 370, 'Z': 320}, ObjectClass='/Script/Engine.BoxComponent', ObjectFlags=2883617, ObjectName='FoliageBox', RelativeLocation={'X': -90, 'Y': 0, 'Z': 280})
    mSimulationDistance = 20000
    mSimulationMovementComponent = Namespace(Acceleration=0, MaxSpeed=0, ObjectClass='/Script/Engine.FloatingPawnMovement', ObjectFlags=2883617, ObjectName='SimulationComponent', bReplicates=True)
    mInventorySize = 48
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
    mMaxAssistedAcceleration = 500
    mDriftingLateralForce = 2057680
    mDriftingUpwardForce = 800000000
    mDriftForwardForceStrengthCurve = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Truck/TruckDriftForwardForceCurve.TruckDriftForwardForceCurve')
    mDriftForceBones = ['drift_force_r', 'drift_force_l', 'Root']
    mMinAngleForDrift = 7
    mNeedsFuelToDrive = True
    mDisplayName = NSLOCTEXT("", "4E99961D424677421EF8F19BF61C314F", "Truck")
    mDescription = NSLOCTEXT("", "EF0DEB594BDC94DC4CD59097330BD008", "Fuel: Any fuel type\r\n\r\n48 slot inventory. Has a built in craft bench.\r\nCan be automated to pick up and deliver resources at truck stations.\r\n\r\nNicknamed \'the Unit\' by FICSIT pioneers because of its massive frame.")
    mHologramClass = NewObject[FGVehicleHologram]()
    mMesh = Namespace(AnimClass='/Game/FactoryGame/Buildable/Vehicle/Truck/Anim_Truck.Anim_Truck_C', BodyInstance={'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 2401, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 100, 'Y': 0, 'Z': 0}, 'MassScale': 10, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='VehicleMesh', SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Truck/Mesh/Truck.Truck'}, bAllowCullDistanceVolume=False, bGenerateOverlapEvents=True)
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True, mCurrentHealth=100, mMaxHealth=100)
    mDisabledByWaterLocations = [{'X': -30, 'Y': 0, 'Z': 250}]
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSubmergedAngularDamping = 6
    mSubmergedLinearDamping = 15
    mSubmergedBouyantForce = 1000
    mAddToSignificanceManager = True
    mShouldAttachDriver = True
    mDriverSeatSocket = driverSocket
    mDriverExitOffset = Namespace(X=0, Y=500, Z=0)
    RootComponent = Namespace(AnimClass='/Game/FactoryGame/Buildable/Vehicle/Truck/Anim_Truck.Anim_Truck_C', BodyInstance={'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 2401, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 100, 'Y': 0, 'Z': 0}, 'MassScale': 10, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='VehicleMesh', SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Truck/Mesh/Truck.Truck'}, bAllowCullDistanceVolume=False, bGenerateOverlapEvents=True)
    
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
    

    def GetActorRepresentationTexture(self):
        ReturnValue = MapCompass_Icon_truck
    

    def OnRep_mFlashlightOn(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L39')
        # End
        # Label 39
        self.SpotLight.SetVisibility(self.mFlashlightOn, False)
    

    def GetAttackLocation(self):
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue_0: Vector = ReturnValue + Vector(0, 0, 200)
        ReturnValue_1: Vector = ReturnValue_0
    

    def GetEnemyTargetDesirability(self):
        ReturnValue = 0.5
    

    def ShouldAutoregisterAsTargetable(self):
        ReturnValue = True
    

    def InpActEvt_Flashlight_K2Node_InputActionEvent_0(self, Key: Key):
        ExecuteUbergraph_BP_Truck.K2Node_InputActionEvent_Key = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Truck(995)
    

    def Server_SetFlashlightOn(self, FlashlightOn: bool):
        ExecuteUbergraph_BP_Truck.K2Node_CustomEvent_FlashlightOn = FlashlightOn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Truck(990)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_BP_Truck(1000)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_BP_Truck(1090)
    

    def Multicast_OpenTrunk(self):
        self.ExecuteUbergraph_BP_Truck(1180)
    

    def Multicast_CloseTrunk(self):
        self.ExecuteUbergraph_BP_Truck(15)
    

    def ExecuteUbergraph_BP_Truck(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue: Ptr[AnimInstance] = self.Workbench.GetAnimInstance()
        ReturnValue_0: bool = ReturnValue.Montage_IsPlaying(CloseWorkbench_01_Montage)
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue = self.Workbench.GetAnimInstance()
        ReturnValue1: float = ReturnValue.Montage_Play(CloseWorkbench_01_Montage, 1, 0, 0, True)
        self.SpotLight.SetIntensity(0)
        goto(ExecutionFlow.Pop())
        self.SpotLight.SetIntensity(100)
        goto(ExecutionFlow.Pop())
        # Label 337
        self.OnRep_mFlashlightOn()
        self.SpotLight.SetVisibility(self.mFlashlightOn, False)
        goto(ExecutionFlow.Pop())
        # Label 394
        self.FlushNetDormancy()
        self.mFlashlightOn = FlashlightOn
        goto('L337')
        # Label 428
        self.OnRep_mFlashlightOn()
        self.SpotLight.SetVisibility(self.mFlashlightOn, False)
        goto(ExecutionFlow.Pop())
        # Label 485
        self.FlushNetDormancy()
        ReturnValue2: bool = Not_PreBool(self.mFlashlightOn)
        self.mFlashlightOn = ReturnValue2
        goto('L428')
        # Label 548
        ReturnValue = self.Workbench.GetAnimInstance()
        ReturnValue_2: float = ReturnValue.Montage_Play(OpenWorkbench_01_Montage, 1, 1, 0, True)
        Default__KismetSystemLibrary.Delay(self, ReturnValue_2, LatentActionInfo(Linkage = 299, UUID = 2070779011, ExecutionFunction = "ExecuteUbergraph_BP_Truck", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 743
        ReturnValue = self.Workbench.GetAnimInstance()
        ReturnValue1_0: bool = ReturnValue.Montage_IsPlaying(OpenWorkbench_01_Montage)
        ReturnValue1_1: bool = Not_PreBool(ReturnValue1_0)
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        goto('L548')
        # Label 880
        ReturnValue_3: bool = self.HasAuthority()
        if not ReturnValue_3:
            goto('L919')
        goto('L485')
        # Label 919
        ReturnValue3: bool = Not_PreBool(self.mFlashlightOn)
        self.Server_SetFlashlightOn(ReturnValue3)
        goto('L485')
        goto('L394')
        goto('L880')
        self.GainedSignificance()
        self.mMesh.VisibilityBasedAnimTickOption = 0
        self.mMesh.SetComponentTickEnabled(True)
        goto(ExecutionFlow.Pop())
        self.LostSignificance()
        self.mMesh.VisibilityBasedAnimTickOption = 3
        self.mMesh.SetComponentTickEnabled(False)
        goto(ExecutionFlow.Pop())
        goto('L743')
    
