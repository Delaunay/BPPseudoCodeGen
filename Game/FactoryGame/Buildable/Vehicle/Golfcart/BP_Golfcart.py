
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ToggleFreeCamera
from Script.Engine import Delay
from Script.FactoryGame import MakeInventoryStack
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import IsAnyMontagePlaying
from Game.FactoryGame.Resource.Equipment.GolfCart.Desc_GolfCart import Desc_GolfCart
from Script.Engine import SpawnEmitterAttached
from Script.CoreUObject import Rotator
from Script.Engine import HideBoneByName
from Script.FactoryGame import Default__FGInventoryLibrary
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Buildable.Vehicle.Golfcart.Animation.ActivateHonk_01_Montage import ActivateHonk_01_Montage
from Script.Engine import GetController
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Script.FactoryGame import Get3PMesh
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ReceiveBeginPlay
from Script.Engine import Array_Append
from Script.Engine import TimerHandle
from Script.FactoryGame import FGInventoryComponent
from Script.FactoryGame import GetDriver
from Game.FactoryGame.VFX.Vehicles.Golfcart.P_Golfcart_Light import P_Golfcart_Light
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.CartDeactivateHonk_01_Montage import CartDeactivateHonk_01_Montage
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Default__GameplayStatics
from Script.Engine import BreakRotator
from Script.Engine import FlushNetDormancy
from Script.FactoryGame import MakeInventoryItem
from Script.Engine import GetSocketBoneName
from Script.Engine import UnHideBoneByName
from Script.CoreUObject import Vector
from Script.Engine import Format
from Script.Engine import Montage_Play
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import Multicast_Honk
from Script.Engine import MakeRotator
from Script.Engine import SetForcedLOD
from Script.Engine import K2_DestroyComponent
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle4W import BP_WheeledVehicle4W
from Script.FactoryGame import GetInventoryStacks
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import ParticleSystemComponent
from Game.FactoryGame.Buildable.Vehicle.Golfcart.Animation.DeactivateHonk_01_Montage import DeactivateHonk_01_Montage
from Game.FactoryGame.Buildable.Vehicle.Golfcart.BP_Golfcart import ExecuteUbergraph_BP_Golfcart
from Script.FactoryGame import InventoryItem
from Game.FactoryGame.Buildable.Vehicle.Golfcart.Audio.Play_GolfCartUnfold import Play_GolfCartUnfold
from Script.FactoryGame import GetStorageInventory
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.Engine import Array_Clear
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.CartActivateHonk_01_Montage import CartActivateHonk_01_Montage
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Buildable.Vehicle.Golfcart.Animation.Unfold_01_Montage import Unfold_01_Montage
from Script.FactoryGame import InventoryStack

class BP_Golfcart(BP_WheeledVehicle4W):
    mIsHonking: bool
    Particle_Honk: Ptr[ParticleSystemComponent]
    mIsFoldAnimationDone: bool
    mEngineSocketName = Body
    mEngineLoopStart = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Golfcart/Audio/Play_GolfCart_StartUp.Play_GolfCart_StartUp')
    mEngineLoopStop = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Golfcart/Audio/Stop_GolfCart_Stop.Stop_GolfCart_Stop')
    mTireLoopStart = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Golfcart/Audio/Play_GolfCart_Tires.Play_GolfCart_Tires')
    mTireLoopStop = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Golfcart/Audio/Stop_GolfCart_Tires.Stop_GolfCart_Tires')
    mVehicleSpeedRTPC = RTPC_GolfCartEngineRev
    mHonkSound = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/-Shared/Audio/Play_Vehicle_Honks_Explorer.Play_Vehicle_Honks_Explorer')
    mIsUsingGolfCartRPM = True
    mSetMaxClampSpeed = 53
    mSetMaxClampRangeSpeed = 98
    mSetMaxClampRangeAirSpeed = 100
    mPlayBurnOutSound = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Golfcart/Audio/Play_GolfCart_BurnOut.Play_GolfCart_BurnOut')
    mStopBurnOutSound = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Golfcart/Audio/Stop_GolfCart_BurnOut.Stop_GolfCart_BurnOut')
    mBurnOutRTPC = RTPC_GolfCartBurnOut
    mBurnOutSpeedThres = 38
    mCarShouldNotHonk = True
    RTPCVehicleCrashSpeed = RTPC_GolfCart_Impacts
    mTireSoundSwitchGroup = GolfCart_Tires
    mInteractWidget = NewObject[Widget_GolfCart]()
    mLookAtText = NSLOCTEXT("", "77712EB34F346EE061D8B3AEF385B0CB", "Press {Button} to interact with Golf Cart")
    mShouldUpdateTireSurfaces = True
    mShouldUseAudioBurnout = True
    mPlayAudioTopDrift = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Golfcart/Audio/Play_GolfCart_Drift.Play_GolfCart_Drift')
    mStopAudioTopDrift = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Golfcart/Audio/Stop_GolfCart_Drift.Stop_GolfCart_Drift')
    mDistBetweenDecals = 5
    mDecalLifespan = 5
    mTireTrackDecals = [{'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Metal.PhysMat_Metal'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Metal_Decal.Tiretrack_Metal_Decal'}}, {'SurfacePhysicsMaterial': {'$AssetPath': '/Game/FactoryGame/-Shared/Material/PhysicalMaterial/PhysMat_Sand.PhysMat_Sand'}, 'DecalMaterialOverride': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Material/Tiretrack_Sand_Decal.Tiretrack_Sand_Decal'}}]
    mDecalSize = Namespace(X=5, Y=10, Z=15)
    mFoliageDestroyRadius = 200
    mAddedAirControlAngularVelocityStrengthYaw = 350
    mAddedAirControlAngularVelocityStrengthPitch = 400
    mNaturalAngularVelocityStrengthYaw = 1.5
    mNaturalAirAngularVelocityStrengthYaw = 50
    mAddedAngularVelocityInputSmoothingSpeed = 0.5
    mFoliageCollideBox = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', AttachParent={'$ObjectClass': '/Script/Engine.SkeletalMeshComponent', '$ObjectFlags': 2883617, '$ObjectName': 'VehicleMesh', 'AnimClass': '/Game/FactoryGame/Buildable/Vehicle/Golfcart/BPA_Golfcart.BPA_Golfcart_C', 'ClothingSimulationFactory': '/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', 'SkeletalMesh': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Golfcart/Mesh/SK_Golfcart_01.SK_Golfcart_01'}, 'bEnableUpdateRateOptimizations': False, 'bGenerateOverlapEvents': True, 'bAllowCullDistanceVolume': False, 'BodyInstance': {'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 0, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': -3, 'Y': 0, 'Z': -45}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 16, 'VelocitySolverIterationCount': 8}}, BodyInstance={'ObjectType': 1, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WorldStatic', 'Response': 1}, {'Channel': 'WorldDynamic', 'Response': 1}, {'Channel': 'Pawn', 'Response': 1}, {'Channel': 'Visibility', 'Response': 1}, {'Channel': 'Camera', 'Response': 1}, {'Channel': 'PhysicsBody', 'Response': 1}, {'Channel': 'Vehicle', 'Response': 1}, {'Channel': 'Destructible', 'Response': 1}, {'Channel': 'Projectile', 'Response': 1}, {'Channel': 'BuildGun', 'Response': 1}, {'Channel': 'WeaponInstantHit', 'Response': 1}, {'Channel': 'VehicleWheelQuery', 'Response': 1}, {'Channel': 'Resource', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, ObjectClass='/Script/Engine.BoxComponent', ObjectFlags=2883617, ObjectName='FoliageBox', RelativeLocation={'X': 0, 'Y': 0, 'Z': 70}, RelativeScale3D={'X': 1.8400787115097046, 'Y': 1, 'Z': 1.9796093702316284})
    mSimulationDistance = 20000
    mSimulationMovementComponent = Namespace(Acceleration=0, MaxSpeed=0, ObjectClass='/Script/Engine.FloatingPawnMovement', ObjectFlags=2883617, ObjectName='SimulationComponent', bReplicates=True)
    mInventorySize = 1
    mVehicleParticeMap = [{'EmitterTemplate': {'$AssetPath': '/Game/FactoryGame/VFX/Vehicles/Golfcart/P_Golfcart_MetalSmoke.P_Golfcart_MetalSmoke'}, 'Surface': 0}, {'EmitterTemplate': {'$AssetPath': '/Game/FactoryGame/VFX/Vehicles/Golfcart/P_Golfcart_MetalSmoke.P_Golfcart_MetalSmoke'}, 'Surface': 2}, {'EmitterTemplate': {'$AssetPath': '/Game/FactoryGame/VFX/Vehicles/Golfcart/P_Golfcart_RockSmoke.P_Golfcart_RockSmoke'}, 'Surface': 3}, {'EmitterTemplate': {'$AssetPath': '/Game/FactoryGame/VFX/Vehicles/Golfcart/P_Golfcart_GrassSmoke.P_Golfcart_GrassSmoke'}, 'Surface': 4}, {'EmitterTemplate': {'$AssetPath': '/Game/FactoryGame/VFX/Vehicles/Golfcart/P_Golfcart_Moist.P_Golfcart_Moist'}, 'Surface': 5}, {'EmitterTemplate': {'$AssetPath': '/Game/FactoryGame/VFX/Vehicles/Golfcart/P_Golfcart_GravelSmoke.P_Golfcart_GravelSmoke'}, 'Surface': 6}, {'EmitterTemplate': {'$AssetPath': '/Game/FactoryGame/VFX/Vehicles/Golfcart/P_Golfcart_SandSMoke.P_Golfcart_SandSmoke'}, 'Surface': 1}]
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
    mMinAngleForDrift = 7
    mHologramClass = NewObject[FGVehicleHologram]()
    mMesh = Namespace(AnimClass='/Game/FactoryGame/Buildable/Vehicle/Golfcart/BPA_Golfcart.BPA_Golfcart_C', BodyInstance={'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 0, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': -3, 'Y': 0, 'Z': -45}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 16, 'VelocitySolverIterationCount': 8}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='VehicleMesh', SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Golfcart/Mesh/SK_Golfcart_01.SK_Golfcart_01'}, bAllowCullDistanceVolume=False, bEnableUpdateRateOptimizations=False, bGenerateOverlapEvents=True)
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True, mCurrentHealth=100, mMaxHealth=100)
    mDisabledByWaterLocations = [{'X': 0, 'Y': 0, 'Z': 0}]
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSubmergedAngularDamping = 6
    mSubmergedLinearDamping = 15
    mSubmergedBouyantForce = 1000
    mAddToSignificanceManager = True
    mShouldAttachDriver = True
    mIsDriverVisible = True
    mDriverSeatSocket = driverSocket
    mDriverSeatAnimation = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Animation/ThirdPerson/CartDriving_01.CartDriving_01')
    mDriverExitOffset = Namespace(X=0, Y=300, Z=0)
    RootComponent = Namespace(AnimClass='/Game/FactoryGame/Buildable/Vehicle/Golfcart/BPA_Golfcart.BPA_Golfcart_C', BodyInstance={'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 0, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': -3, 'Y': 0, 'Z': -45}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 16, 'VelocitySolverIterationCount': 8}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='VehicleMesh', SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Golfcart/Mesh/SK_Golfcart_01.SK_Golfcart_01'}, bAllowCullDistanceVolume=False, bEnableUpdateRateOptimizations=False, bGenerateOverlapEvents=True)
    
    def GetLookAtDecription(self):
        ReturnValue: Ptr[Controller] = byCharacter.GetController()
        
        button = None
        Default__HUDHelpers.GetKeyNameForActionSimple(ReturnValue, "Use", self, Ref[button])
        FormatArgumentData.ArgumentName = "BUTTON"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = button
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_0: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_UnicodeStringConst', 'InstOffsetFromTop': 374, 'Value': 'Press [{BUTTON}] to use Factory Cart™'}", Array)
        ReturnValue_1: FText = ReturnValue_0
    

    def GetDismantleRefund(self):
        
        refund = None
        Default__KismetArrayLibrary.Array_Clear(Ref[refund])
        ReturnValue: InventoryItem = Default__FGInventoryLibrary.MakeInventoryItem(Desc_GolfCart)
        ReturnValue_0: InventoryStack = Default__FGInventoryLibrary.MakeInventoryStack(1, ReturnValue)
        
        refund = None
        ReturnValue_1: int32 = refund.append(ReturnValue_0)
        ReturnValue_2: Ptr[FGInventoryComponent] = self.GetStorageInventory()
        stacks: List[InventoryStack] = []
        
        ReturnValue_2.GetInventoryStacks(Ref[stacks])
        
        refund = None
        Default__KismetArrayLibrary.Array_Append(Ref[refund], Ref[stacks])
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_Golfcart(1723)
    

    def ToggleFreeCamera(self):
        self.ExecuteUbergraph_BP_Golfcart(80)
    

    def Multicast_Honk(self):
        self.ExecuteUbergraph_BP_Golfcart(650)
    

    def DisablePhysics(self):
        self.ExecuteUbergraph_BP_Golfcart(1786)
    

    def EnablePhysics(self):
        self.ExecuteUbergraph_BP_Golfcart(1843)
    

    def DoFoldAnimation(self):
        self.ExecuteUbergraph_BP_Golfcart(2092)
    

    def ExecuteUbergraph_BP_Golfcart(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.mIsFoldAnimationDone = True
        goto(ExecutionFlow.Pop())
        self.mMesh.SetForcedLOD(0)
        goto(ExecutionFlow.Pop())
        # Label 65
        self.FlushNetDormancy()
        goto('L15')
        self.ToggleFreeCamera()
        ReturnValue: bool = Not_PreBool(self.mIsFreeCamera)
        self.SpringArm.bEnableCameraLag = ReturnValue
        ReturnValue = Not_PreBool(self.mIsFreeCamera)
        self.SpringArm.bEnableCameraRotationLag = ReturnValue
        goto(ExecutionFlow.Pop())
        # Label 231
        self.ReceiveBeginPlay()
        if not self.mIsFoldAnimationDone:
            goto('L256')
        goto(ExecutionFlow.Pop())
        # Label 256
        self.DoFoldAnimation()
        goto(ExecutionFlow.Pop())
        # Label 271
        self.mMesh.SetForcedLOD(1)
        ReturnValue_0: Ptr[AnimInstance] = self.mMesh.GetAnimInstance()
        ReturnValue_1: float = ReturnValue_0.Montage_Play(Unfold_01_Montage, 1, 0, 0, True)
        Default__KismetSystemLibrary.Delay(self, ReturnValue_1, LatentActionInfo(Linkage = 27, UUID = -364596002, ExecutionFunction = "ExecuteUbergraph_BP_Golfcart", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        
        Roll = None
        Pitch = None
        Yaw = None
        # Label 503
        BreakRotator(self.SpringArm.RelativeRotation, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_2: Rotator = MakeRotator(0, Pitch, 0)
        self.mDefaultCameraRotation = ReturnValue_2
        goto('L271')
        self.Multicast_Honk()
        ReturnValue5: Ptr[AnimInstance] = self.mMesh.GetAnimInstance()
        ReturnValue_3: bool = ReturnValue5.IsAnyMontagePlaying()
        if not ReturnValue_3:
            goto('L759')
        goto(ExecutionFlow.Pop())
        # Label 759
        if not self.mIsHonking:
            goto('L1108')
        ReturnValue3: Ptr[AnimInstance] = self.mMesh.GetAnimInstance()
        ReturnValue3_0: float = ReturnValue3.Montage_Play(DeactivateHonk_01_Montage, 1, 0, 0, True)
        ReturnValue1: Ptr[FGCharacterPlayer] = self.GetDriver()
        ReturnValue1_0: Ptr[SkeletalMeshComponent] = ReturnValue1.Get3PMesh()
        ReturnValue4: Ptr[AnimInstance] = ReturnValue1_0.GetAnimInstance()
        ReturnValue4_0: float = ReturnValue4.Montage_Play(CartDeactivateHonk_01_Montage, 1, 0, 0, True)
        self.mIsHonking = False
        self.Particle_Honk.K2_DestroyComponent(self)
        goto(ExecutionFlow.Pop())
        # Label 1108
        ReturnValue1_1: Ptr[AnimInstance] = self.mMesh.GetAnimInstance()
        ReturnValue1_2: float = ReturnValue1_1.Montage_Play(ActivateHonk_01_Montage, 1, 0, 0, True)
        ReturnValue_4: Ptr[FGCharacterPlayer] = self.GetDriver()
        ReturnValue_5: Ptr[SkeletalMeshComponent] = ReturnValue_4.Get3PMesh()
        ReturnValue2: Ptr[AnimInstance] = ReturnValue_5.GetAnimInstance()
        ReturnValue2_0: float = ReturnValue2.Montage_Play(CartActivateHonk_01_Montage, 1, 0, 0, True)
        self.mIsHonking = True
        ReturnValue_6: FName = self.mMesh.GetSocketBoneName("siren_VFX_01")
        ReturnValue_7: Vector = self.mMesh.GetSocketLocation(ReturnValue_6)
        ReturnValue_8: Rotator = self.mMesh.GetSocketRotation(ReturnValue_6)
        ReturnValue_9: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_Golfcart_Light, self.mMesh, ReturnValue_6, ReturnValue_7, ReturnValue_8, Vector(1, 1, 1), 1, True, 0)
        self.Particle_Honk = ReturnValue_9
        goto(ExecutionFlow.Pop())
        goto('L231')
        # Label 1728
        ReturnValue_10: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_GolfCartUnfold, self, True)
        goto('L503')
        self.mForceSimulationMode = True
        self.mMesh.UnHideBoneByName("window_r")
        goto(ExecutionFlow.Pop())
        self.mForceSimulationMode = False
        goto('L65')
        # Label 1859
        OutputDelegate.BindUFunction(self, DisablePhysics)
        ReturnValue_11: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.019999999552965164, False)
        OutputDelegate1.BindUFunction(self, EnablePhysics)
        ReturnValue1_3: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate1, 5, False)
        goto('L1728')
        # Label 2040
        self.mMesh.HideBoneByName("window_r", 0)
        goto('L1859')
        goto('L2040')
    
