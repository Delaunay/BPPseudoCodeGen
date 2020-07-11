
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.FactoryGame import ShowOutline
from Script.Engine import Delay
from Script.Engine import SetVisibility
from Game.FactoryGame.Buildable.Vehicle.VehicleWorkbench.Animation.CloseWorkbench_01_Montage import CloseWorkbench_01_Montage
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_Icon_explorer import MapCompass_Icon_explorer
from Script.Engine import Not_PreBool
from Game.FactoryGame.Buildable.Vehicle.Explorer.BP_Explorer import ExecuteUbergraph_BP_Explorer.K2Node_InputAxisEvent_AxisValue
from Script.Engine import LatentActionInfo
from Script.Engine import SetIntensity
from Script.Engine import HasAuthority
from Game.FactoryGame.Buildable.Vehicle.VehicleWorkbench.Animation.OpenWorkbench_01_Montage import OpenWorkbench_01_Montage
from Script.Engine import GetAnimInstance
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Vehicle.-Shared.Audio.Play_V_Suspension_Pneumatic_Light import Play_V_Suspension_Pneumatic_Light
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ReceiveTick
from Script.Engine import GreaterEqual_FloatFloat
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import UpdateOutline
from Game.FactoryGame.Buildable.Vehicle.Explorer.BP_Explorer import ExecuteUbergraph_BP_Explorer.K2Node_Event_DeltaSeconds
from Script.Engine import FlushNetDormancy
from Script.FactoryGame import GetIsSignificant
from Game.FactoryGame.Buildable.Vehicle.Explorer.BP_Explorer import ExecuteUbergraph_BP_Explorer.K2Node_InputActionEvent_Key
from Script.CoreUObject import Vector
from Game.FactoryGame.Buildable.Vehicle.Explorer.BP_Explorer import ExecuteUbergraph_BP_Explorer
from Game.FactoryGame.Buildable.Vehicle.Explorer.BP_Explorer import ExecuteUbergraph_BP_Explorer.K2Node_CustomEvent_FlashlightOn
from Script.Engine import Montage_Play
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle4W import BP_WheeledVehicle4W
from Script.FactoryGame import LostSignificance
from Script.Engine import K2_GetActorLocation
from Script.FactoryGame import EOutlineColor
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.FactoryGame import GetLargestTireLoadValue
from Script.FactoryGame import GainedSignificance

class BP_Explorer(BP_WheeledVehicle4W):
    throttleval: float
    mFlashlightOn: bool
    mSuspensionLoadTimer: float
    mSuspensionLoadTimerDefault: float = 0.20000000298023224
    mSuspensionTick: float = 0.10000000149011612
    mSuspensionTickDefault: float
    mEngineLoopStart = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Explorer/Audio/Rework/Play_Vehicle_Explorer_Rework_Engine.Play_Vehicle_Explorer_Rework_Engine')
    mEngineLoopStop = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Explorer/Audio/Rework/Stop_Vehicle_Explorer_Rework_Engine.Stop_Vehicle_Explorer_Rework_Engine')
    mTireLoopStart = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Explorer/Audio/Play_Vehicle_GroundEffect.Play_Vehicle_GroundEffect')
    mTireLoopStop = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Explorer/Audio/Stop_Vehicle_GroundEffect.Stop_Vehicle_GroundEffect')
    mEngineLoadRTPCName = RTPC_Explorer_RPM
    mVehicleSpeedRTPC = RTPC_Explorer_Speed
    mVehicleAccelerationStateRTPC = RTPC_Explorer_Load
    mHonkSound = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/-Shared/Audio/Play_Vehicle_Honks_Explorer.Play_Vehicle_Honks_Explorer')
    mMapText = NSLOCTEXT("", "0A2D77E44C08C8F95F95BB979CE9FB6B", "Explorer")
    mPlayBurnOutSound = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Explorer/Audio/Rework/Play_Vehicle_Explorer_Rework_Burnout.Play_Vehicle_Explorer_Rework_Burnout')
    mStopBurnOutSound = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Explorer/Audio/Rework/Stop_Vehicle_Explorer_Rework_Burnout.Stop_Vehicle_Explorer_Rework_Burnout')
    mBurnOutRTPC = RTPC_Exporer_Burnout
    mBurnOutSpeedThres = 60
    mIsUsingNewAudioGears = True
    mAudioGearRTPC = RTPC_Explorer_Gears
    mShouldUseAudioBurnout = True
    mPlayAudioTopDrift = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Explorer/Audio/Rework/Play_Vehicle_Explorer_Rework_Topdrift.Play_Vehicle_Explorer_Rework_Topdrift')
    mStopAudioTopDrift = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Explorer/Audio/Rework/Stop_Vehicle_Explorer_Rework_Topdrift.Stop_Vehicle_Explorer_Rework_Topdrift')
    mTopDriftRTPC = RTPC_Explorer_TopDrift
    mFuelConsumption = 90
    mDistBetweenDecals = 15
    mDecalLifespan = 5
    mTireTrackDecals = [{'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Cement.PhysMat_Cement'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Coral.PhysMat_Coral'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Grass.PhysMat_Grass'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Decal.Tiretrack_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Grass_High.PhysMat_Grass_High'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Decal.Tiretrack_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Gravel.PhysMat_Gravel'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Metal.PhysMat_Metal'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Moist.PhysMat_Moist'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Decal.Tiretrack_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Rock.PhysMat_Rock'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Rock_Gravel.PhysMat_Rock_Gravel'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Sand.PhysMat_Sand'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Sand_Decal.Tiretrack_Sand_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Sand_Cracked.PhysMat_Sand_Cracked'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Soil.PhysMat_Soil'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Decal.Tiretrack_Decal'}}]
    mDecalSize = Namespace(X=10, Y=65, Z=70)
    mFoliageDestroyRadius = 3750
    mAddedGroundAngularVelocityStrengthYaw = 240
    mAddedGroundAngularVelocityStrengthPitch = 80
    mAddedAirControlAngularVelocityStrengthYaw = 150
    mAddedAirControlAngularVelocityStrengthPitch = 150
    mNaturalAngularVelocityStrengthYaw = 85
    mNaturalAngularVelocityStrengthPitch = 50
    mNaturalAirAngularVelocityStrengthYaw = 30
    mAddedAngularVelocityInputSmoothingSpeed = 0.10000000149011612
    mFoliageCollideBox = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', AttachParent={'$ObjectClass': '/Script/Engine.SkeletalMeshComponent', '$ObjectFlags': 2883617, '$ObjectName': 'VehicleMesh', 'AnimClass': '/Game/FactoryGame/Buildable/Vehicle/Explorer/BP_ExplorerAnim.BP_ExplorerAnim_C', 'ClothingSimulationFactory': '/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', 'SkeletalMesh': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Explorer/Mesh/Explorer_skl.Explorer_skl'}, 'bGenerateOverlapEvents': True, 'bAllowCullDistanceVolume': False, 'BodyInstance': {'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 0, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 100, 'Y': 0, 'Z': -40}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 16, 'VelocitySolverIterationCount': 8}, 'bShouldUpdatePhysicsVolume': True}, BodyInstance={'ObjectType': 1, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WorldStatic', 'Response': 1}, {'Channel': 'WorldDynamic', 'Response': 1}, {'Channel': 'Pawn', 'Response': 1}, {'Channel': 'Visibility', 'Response': 1}, {'Channel': 'Camera', 'Response': 1}, {'Channel': 'PhysicsBody', 'Response': 1}, {'Channel': 'Vehicle', 'Response': 1}, {'Channel': 'Destructible', 'Response': 1}, {'Channel': 'Projectile', 'Response': 1}, {'Channel': 'BuildGun', 'Response': 1}, {'Channel': 'WeaponInstantHit', 'Response': 1}, {'Channel': 'VehicleWheelQuery', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, BoxExtent={'X': 370, 'Y': 250, 'Z': 180}, ObjectClass='/Script/Engine.BoxComponent', ObjectFlags=2883617, ObjectName='FoliageBox', RelativeLocation={'X': 40, 'Y': 0, 'Z': 130})
    mSimulationDistance = 20000
    mSimulationMovementComponent = Namespace(Acceleration=0, MaxSpeed=0, ObjectClass='/Script/Engine.FloatingPawnMovement', ObjectFlags=2883617, ObjectName='SimulationComponent', bReplicates=True)
    mInventorySize = 24
    mIsPathVisible = True
    mReverseAddedAngularVelocityYawMultiplier = 2
    mHasAirControl = True
    mGroundTraceLength = 300
    mMaxDeltaLinearVelocity = 100
    mMaxDeltaAngularVelocity = 550
    mRollStabilisationStrength = 5
    mMaxRollAngleForUpsideDown = 85
    mMaxFlatOnGroundRollAngleLimit = 5
    mMaxRollForActivationOfAssistedVelocities = 75
    mMaxSpeedForAddedAcceleration = 80
    mMaxAssistedAcceleration = 5000000
    mHasAssistedVelocities = True
    mHasRollStabilisation = True
    mDriftingLateralForce = 5202000
    mDriftingUpwardForce = 1002000
    mDriftForwardForceStrengthCurve = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Explorer/ExplorerDriftForwardForceCurve.ExplorerDriftForwardForceCurve')
    mDriftForceBones = ['drift_force_r', 'drift_force_l', 'Root']
    mMinAngleForDrift = 7
    mNeedsFuelToDrive = True
    mDisplayName = NSLOCTEXT("", "AD64301C48A0793A86E248A63A36452D", "Explorer")
    mDescription = NSLOCTEXT("", "B0A8D2CF478859AC825F36A95CE71B48", "Fuel: Any fuel type\r\n\r\n25 slot inventory. Has a built in craft bench.\r\nFast and nimble exploration vehicle. Tuned for really rough terrain and can climb almost vertical surfaces.")
    mHologramClass = NewObject[FGVehicleHologram]()
    mMesh = Namespace(AnimClass='/Game/FactoryGame/Buildable/Vehicle/Explorer/BP_ExplorerAnim.BP_ExplorerAnim_C', BodyInstance={'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 0, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 100, 'Y': 0, 'Z': -40}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 16, 'VelocitySolverIterationCount': 8}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='VehicleMesh', SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Explorer/Mesh/Explorer_skl.Explorer_skl'}, bAllowCullDistanceVolume=False, bGenerateOverlapEvents=True, bShouldUpdatePhysicsVolume=True)
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True, mCurrentHealth=100, mMaxHealth=100)
    mDisabledByWaterLocations = [{'X': -20, 'Y': 0, 'Z': 210}]
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSubmergedAngularDamping = 6
    mSubmergedLinearDamping = 15
    mSubmergedBouyantForce = 1000000
    mAddToSignificanceManager = True
    mShouldAttachDriver = True
    mIsDriverVisible = True
    mDriverSeatSocket = driverSocket
    mDriverSeatAnimation = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Animation/ThirdPerson/ExplorerDriving_01.ExplorerDriving_01')
    mDriverExitOffset = Namespace(X=0, Y=350, Z=0)
    RootComponent = Namespace(AnimClass='/Game/FactoryGame/Buildable/Vehicle/Explorer/BP_ExplorerAnim.BP_ExplorerAnim_C', BodyInstance={'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 0, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 100, 'Y': 0, 'Z': -40}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 16, 'VelocitySolverIterationCount': 8}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='VehicleMesh', SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Explorer/Mesh/Explorer_skl.Explorer_skl'}, bAllowCullDistanceVolume=False, bGenerateOverlapEvents=True, bShouldUpdatePhysicsVolume=True)
    
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
    

    def GetActorRepresentationText(self):
        ReturnValue = self.mMapText
    

    def GetActorRepresentationTexture(self):
        ReturnValue = MapCompass_Icon_explorer
    

    def CheckSuspension(self, InDeltaTime: float):
        ReturnValue: float = InDeltaTime + self.mSuspensionTick
        self.mSuspensionTick = ReturnValue
        ReturnValue_0: bool = GreaterEqual_FloatFloat(self.mSuspensionTick, self.mSuspensionTickDefault)
        if not ReturnValue_0:
            goto('L505')
        self.mSuspensionTick = 0
        ReturnValue_1: float = self.mSuspensionLoadTimer - InDeltaTime
        self.mSuspensionLoadTimer = ReturnValue_1
        ReturnValue_2: float = self.FGWheeledVehicleMovementComponent4W.GetLargestTireLoadValue()
        ReturnValue_3: bool = self.mSuspensionLoadTimer <= 0
        ReturnValue1: bool = GreaterEqual_FloatFloat(ReturnValue_2, 2.799999952316284)
        ReturnValue_4: bool = ReturnValue1 and ReturnValue_3
        if not ReturnValue_4:
            goto('L505')
        self.mSuspensionLoadTimer = self.mSuspensionLoadTimerDefault
        ReturnValue_5: bool = self.GetIsSignificant()
        if not ReturnValue_5:
            goto('L505')
        ReturnValue_6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_V_Suspension_Pneumatic_Light, self, True)
    

    def OnRep_mFlashlightOn(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L39')
        # End
        # Label 39
        self.SpotLight.SetVisibility(self.mFlashlightOn, False)
    

    def GetAttackLocation(self):
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue_0: Vector = ReturnValue + Vector(0, 0, 150)
        ReturnValue_1: Vector = ReturnValue_0
    

    def GetEnemyTargetDesirability(self):
        ReturnValue = 0.5
    

    def ShouldAutoregisterAsTargetable(self):
        ReturnValue = True
    

    def InpActEvt_Flashlight_K2Node_InputActionEvent_0(self, Key: Key):
        ExecuteUbergraph_BP_Explorer.K2Node_InputActionEvent_Key = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Explorer(956)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_Explorer.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Explorer(548)
    

    def InpAxisEvt_MoveForward_K2Node_InputAxisEvent_0(self, AxisValue: float):
        ExecuteUbergraph_BP_Explorer.K2Node_InputAxisEvent_AxisValue = AxisValue #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Explorer(591)
    

    def Server_SetFlashlightOn(self, FlashlightOn: bool):
        ExecuteUbergraph_BP_Explorer.K2Node_CustomEvent_FlashlightOn = FlashlightOn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Explorer(951)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_BP_Explorer(1066)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_BP_Explorer(1156)
    

    def Multicast_OpenTrunk(self):
        self.ExecuteUbergraph_BP_Explorer(1246)
    

    def Multicast_CloseTrunk(self):
        self.ExecuteUbergraph_BP_Explorer(15)
    

    def ExecuteUbergraph_BP_Explorer(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue: Ptr[AnimInstance] = self.Workbench.GetAnimInstance()
        ReturnValue_0: bool = ReturnValue.Montage_IsPlaying(CloseWorkbench_01_Montage)
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue = self.Workbench.GetAnimInstance()
        ReturnValue_2: float = ReturnValue.Montage_Play(CloseWorkbench_01_Montage, 1, 0, 0, True)
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
        self.ReceiveTick(DeltaSeconds)
        self.CheckSuspension(DeltaSeconds)
        goto(ExecutionFlow.Pop())
        self.throttleval = AxisValue
        goto(ExecutionFlow.Pop())
        # Label 619
        ReturnValue = self.Workbench.GetAnimInstance()
        ReturnValue1: float = ReturnValue.Montage_Play(OpenWorkbench_01_Montage, 1, 1, 0, True)
        Default__KismetSystemLibrary.Delay(self, ReturnValue1, LatentActionInfo(Linkage = 299, UUID = -1469939739, ExecutionFunction = "ExecuteUbergraph_BP_Explorer", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 814
        ReturnValue = self.Workbench.GetAnimInstance()
        ReturnValue1_0: bool = ReturnValue.Montage_IsPlaying(OpenWorkbench_01_Montage)
        ReturnValue1_1: bool = Not_PreBool(ReturnValue1_0)
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        goto('L619')
        goto('L394')
        ReturnValue_3: bool = self.HasAuthority()
        if not ReturnValue_3:
            goto('L995')
        goto('L485')
        # Label 995
        ReturnValue3: bool = Not_PreBool(self.mFlashlightOn)
        self.Server_SetFlashlightOn(ReturnValue3)
        goto('L485')
        self.GainedSignificance()
        self.mMesh.VisibilityBasedAnimTickOption = 0
        self.mMesh.SetComponentTickEnabled(True)
        goto(ExecutionFlow.Pop())
        self.LostSignificance()
        self.mMesh.VisibilityBasedAnimTickOption = 3
        self.mMesh.SetComponentTickEnabled(False)
        goto(ExecutionFlow.Pop())
        goto('L814')
    
