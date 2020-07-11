
from codegen.ue4_stub import *

from Script.Engine import ReceiveDestroyed
from Script.FactoryGame import FGTargetPointLinkedList
from Script.Engine import FinishSpawningActor
from Script.FactoryGame import ReceiveOnDriverLeave
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputAxisEvent_AxisValue
from Script.FactoryGame import FGCharacterPlayer
from Script.AkAudio import PostAkEventAtLocation
from Script.Engine import SpawnEmitterAtLocation
from Script.Engine import GetTransform
from Script.InputCore import Key
from Script.CoreUObject import Rotator
from Script.FactoryGame import SetNextTarget
from Script.Engine import FTrunc
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_destroyAudioEvent
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import EqualEqual_FloatFloat
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_OldController
from Script.FactoryGame import GetIsInAir
from Script.FactoryGame import InsertItem
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetDisabledInputGate
from Script.Engine import EPhysicalSurface
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.FactoryGame import GetDriver
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.AkAudio import AkAudioEvent
from Script.Engine import FMax
from Script.Engine import NotEqual_FloatFloat
from Script.PhysXVehicles import GetThrottle
from Script.Engine import FlushNetDormancy
from Script.PhysXVehicles import GetSteering
from Script.FactoryGame import GetSimulationComponent
from Script.FactoryGame import GetIsSignificant
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputActionEvent_Key
from Script.Engine import ReceiveUnpossessed
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputActionEvent_Key1
from Script.FactoryGame import SetAddedAngularVelocityYaw
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_NewController
from Script.Engine import Default__KismetStringLibrary
from Script.PhysXVehicles import WheeledVehicleMovementComponent
from Script.Engine import SetIntPropertyByName
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputActionEvent_Key2
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle
from Script.AkAudio import PostAkEventAttached
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import GetTargetSpeed
from Script.UMG import Create
from Script.Engine import MapRangeClamped
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import K2_SetRelativeRotation
from Script.PhysXVehicles import SetThrottleInput
from Script.FactoryGame import GetVehicleMovementComponent
from Script.FactoryGame import IsTargetSpeedStill
from Script.CoreUObject import LinearColor
from Script.FactoryGame import IsDriving
from Script.Engine import EqualEqual_ClassClass
from Game.FactoryGame.Buildable.Vehicle.BP_VehicleTargetPoint import BP_VehicleTargetPoint
from Script.Engine import FClamp
from Script.FactoryGame import FGPlayerController
from Script.Engine import Controller
from Script.AkAudio import SetActorRTPCValue
from Script.Engine import SetObjectPropertyByName
from Script.Engine import GetInputAxisValue
from Script.Engine import GetComponentByClass
from Script.Engine import GreaterEqual_IntInt
from Script.Engine import VSize
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_byCharacter
from Script.Engine import FMin
from Script.Engine import Max
from Script.Engine import HUD
from Script.Engine import SelectFloat
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_player1
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_DeltaSeconds
from Script.FactoryGame import DisabledInputGate
from Script.Engine import GetHUD
from Script.Engine import InRange_FloatFloat
from Script.FactoryGame import ReceiveOnDriverEnter
from Script.FactoryGame import FGInteractWidget
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_newColor
from Script.FactoryGame import FGActorRepresentationManager
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_atStation
from Script.Engine import K2_GetComponentLocation
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.Engine import GetDistanceTo
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputActionEvent_Key5
from Script.Engine import Abs
from Script.FactoryGame import ReceiveOnVehicleStartup
from Script.AkAudio import AkComponent
from Script.Engine import VLerp
from Script.FactoryGame import IsSelfDriving
from Script.FactoryGame import FGWheeledVehicle
from Script.Engine import Conv_BoolToFloat
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_location
from Script.FactoryGame import GetCachedSurfaceMaterial
from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Script.Engine import ReceivePossessed
from Script.FactoryGame import CreateAndAddNewRepresentation
from Script.Engine import K2_SetTimerDelegate
from Script.PhysXVehicles import SetHandbrakeInput
from Script.FactoryGame import SetCrosshairState
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_destroyEffect
from Script.FactoryGame import FGPlayerState
from Script.Engine import Conv_IntToFloat
from Script.FactoryGame import GetLastTarget
from Script.Engine import LatentActionInfo
from Script.Engine import FindLookAtRotation
from Script.Engine import HasAuthority
from Script.AkAudio import SetSwitch
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Script.Engine import GetController
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputActionEvent_Key4
from Script.FactoryGame import SetIsDrifting
from Script.FactoryGame import HasFuel
from Script.PhysXVehicles import SetSteeringInput
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_CustomEvent_menuOpen
from Script.PhysXVehicles import GetCurrentGear
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputActionEvent_Key6
from Script.FactoryGame import WasDocked
from Script.FactoryGame import WasUndocked
from Script.Engine import Default__GameplayStatics
from Script.Engine import BreakRotator
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_HitLocation
from Script.Engine import K2_SetActorRotation
from Script.Engine import Subtract_VectorVector
from Script.Engine import Format
from Script.Engine import EqualEqual_ObjectObject
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_player
from Script.Engine import ClampAngle
from Script.Engine import K2_GetActorRotation
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.Engine import Abs_Int
from Script.PhysXVehicles import SetBrakeInput
from Script.Engine import MakeRotator
from Script.FactoryGame import SetAddedAngularVelocityPitch
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_Other
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.Engine import PhysicalMaterial
from Script.Engine import NearlyEqual_FloatFloat
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_NormalImpulse
from Script.FactoryGame import EOutlineColor
from Script.AkAudio import StopAndDestroyComponent
from Script.Engine import GetForwardVector
from Script.FactoryGame import RemoveRepresentationOfActor
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_Hit
from Script.FactoryGame import GetTargetNodeLinkedList
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputActionEvent_Key3
from Script.Engine import RandomFloatInRange
from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_Icon_tractor import MapCompass_Icon_tractor
from Script.Engine import SpringArmComponent
from Script.Engine import Conv_NameToString
from Game.FactoryGame.Buildable.Vehicle.UseState_WorkBench import UseState_WorkBench
from Script.FactoryGame import ShowOutline
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputAxisEvent_AxisValue1
from Script.Engine import NormalizedDeltaRotator
from Script.FactoryGame import SetPathVisibility
from Script.Engine import MapRangeUnclamped
from Script.Engine import K2_IsValidTimerHandle
from Script.Engine import ReceiveBeginPlay
from Script.Engine import Not_PreBool
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_bSelfMoved
from Script.Engine import ReceiveTick
from Script.FactoryGame import IncreaseWaitTime
from Script.Engine import GreaterEqual_FloatFloat
from Script.FactoryGame import Default__FGActorRepresentationManager
from Script.FactoryGame import FGTargetPoint
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.FactoryGame import OnUse
from Script.FactoryGame import GetNametagColor
from Script.FactoryGame import UpdateRepresentation
from Script.FactoryGame import GetCurrentTarget
from Script.Engine import BooleanOR
from Script.PhysXVehicles import GetEngineRotationSpeed
from Game.FactoryGame.Buildable.Vehicle.Widget_RecordMenu import Widget_RecordMenu
from Script.FactoryGame import ClearRecording
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_MyComp
from Script.CoreUObject import Vector
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_state
from Script.FactoryGame import GetIsDrifting
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_HitNormal
from Script.FactoryGame import GetLookAtDecription
from Script.FactoryGame import FGHUD
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_CustomEvent_dt
from Script.FactoryGame import GetPathVisibility
from Script.Engine import FloatingPawnMovement
from Script.Engine import K2_SetActorLocationAndRotation
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_OtherComp
from Script.Engine import Actor
from Script.Engine import ParticleSystemComponent
from Script.Engine import K2_GetActorLocation
from Script.FactoryGame import IsSimulated
from Script.FactoryGame import SetOwningVehicle
from Script.FactoryGame import ReceiveOnVehicleShutDown
from Script.FactoryGame import UpdateUseState
from Script.FactoryGame import GetForwardSpeed
from Script.CoreUObject import Transform
from Script.FactoryGame import EFogOfWarRevealType

class BP_WheeledVehicle(FGWheeledVehicle):
    mIsRecording: bool
    mRecordCounter: float
    mRecordInterval: float = 1.5
    mCurrentDestination: Vector
    mObjectInFront: bool
    mReverseMaxDistance: float = 1000
    mCloseEnoughToReverse: bool
    mDesiredSteering: float
    LocationReached: FMulticastScriptDelegate
    mSpeedInKMH: int32
    mIsFollowingPath: bool
    mSpeedLimit: int32 = -1
    mJumpForce: Vector = Namespace(X=0, Y=0, Z=900000)
    mIsFreeCamera: bool = True
    mDefaultCameraRotation: Rotator
    mTrunkUser: Ptr[FGCharacterPlayer]
    mIsInventoryOpen: bool
    mTimeSpentOnTarget: float
    mUpdateDelta: float = 0.05000000074505806
    mEngineLoadTimer: float
    mAudioSign: float
    mPreviousThrottleValue: float
    mEngineSocketName: FName = drawbar
    mEngineLoopStart: Ptr[AkAudioEvent]
    mEngineLoopStop: Ptr[AkAudioEvent]
    mEngineRevUp: Ptr[AkAudioEvent]
    mEngineRevDown: Ptr[AkAudioEvent]
    mExhaustSocketName: FName = exhaustSocket
    mExhaustLoopStart: Ptr[AkAudioEvent]
    mExhaustLoopStop: Ptr[AkAudioEvent]
    mExhaustRevUp: Ptr[AkAudioEvent]
    mExhaustRevDown: Ptr[AkAudioEvent]
    mTireLoopStart: Ptr[AkAudioEvent]
    mTireLoopStop: Ptr[AkAudioEvent]
    mCrashSound: Ptr[AkAudioEvent] = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/-Shared/Audio/Play_V_Buggy_Crash.Play_V_Buggy_Crash')
    mCachedGear: int32 = 1
    mStopRevEngine: Ptr[AkAudioEvent]
    mStopRevExhaust: Ptr[AkAudioEvent]
    mEngineLoadRTPCName: FName = RTPC_Tractor_RPM
    mEngineLoadTimerMax: float = 9
    mDidSwitchThrottleState: bool = True
    mDidStartSoundLoops: bool
    mSpringArmComponent: Ptr[SpringArmComponent]
    mIsAtStation: bool
    mReverseSteering: float = 1000
    mMaxReverseTime: float = 1000
    mIsMenuOpen: bool
    mIsRecordSessionActive: bool
    mIsTransferingInventory: bool
    mIsAutoPilotEnabled: bool
    mHUDClass: TSubclassOf[UserWidget] = NewObject[Widget_Vehicle]()
    OnStopRecording: FMulticastScriptDelegate
    OnStartRecording: FMulticastScriptDelegate
    mRecordMenu: Ptr[Widget_RecordMenu]
    mVehicleSpeedRTPC: FName = RTPC_Tractor_RPM
    mVehicleAccelerationStateRTPC: FName = RTPC_Tractor_RPM
    mHonkSound: Ptr[AkAudioEvent]
    mPossessed: bool
    mMapText: FText = NSLOCTEXT("", "C22AEAC8465C49275172C1921929BADD", "Vehicle")
    mIsUsingGolfCartRPM: bool
    mSetMaxClampSpeed: float = 40
    mSetMaxClampRangeSpeed: float = 90
    mSetMaxClampRangeAirSpeed: float = 90
    mCheckValueForBurnOut: float
    mIsBurningOut: bool
    mPlayBurnOutSound: Ptr[AkAudioEvent] = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Golfcart/Audio/Play_GolfCart_BurnOut.Play_GolfCart_BurnOut')
    mStopBurnOutSound: Ptr[AkAudioEvent] = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Golfcart/Audio/Stop_GolfCart_BurnOut.Stop_GolfCart_BurnOut')
    mBurnOutRTPC: FName = RTPC_GolfCartBurnOut
    mBurnOutSpeedThres: int32
    BurnOutRTPCRange: float = 100
    mCarShouldNotHonk: bool
    AudioRPMLoadTimer: float
    RTPCVehicleCrashSpeed: FName = T_Vehicle_CrashSpeed
    mUseVehicleImpactForce: bool
    mTireSoundTimer: TimerHandle
    mTireSoundLoop: Ptr[AkComponent]
    mTireSoundSwitchGroup: FString
    mInteractWidget: TSubclassOf[FGInteractWidget] = NewObject[Widget_VehicleTrunk]()
    mPlayIsBurningOut: Ptr[AkComponent]
    StopIsBurningOut: Ptr[AkComponent]
    mLookAtText: FText = NSLOCTEXT("", "499CEBEA48F4D7E14FD2FAB926FEF875", "Press [{BUTTON}] to open workbench")
    mAudioPeakFlutter: float
    mPlayTopDrift: Ptr[AkComponent]
    StopTopDrift: Ptr[AkComponent]
    mIsTopDrifting: bool
    mThresholdForAudioFlutterKMH: float = 45
    mMinSteeringAudioFlutter: float = 24
    mMaxSteeringAudioFlutter: float = 30
    mMinAudioPeakFlutter: float = 5
    mMaxAudioPeakFlutter: float = 19
    mShouldUpdateTireSurfaces: bool
    mAudioCurrentGear: int32
    mIsUsingNewAudioGears: bool
    mAudioGearRTPC: FName
    mIsUsingNewAudioVehicleRPM: bool
    mShouldUseAudioBurnout: bool
    mPlayAudioTopDrift: Ptr[AkAudioEvent]
    mStopAudioTopDrift: Ptr[AkAudioEvent]
    mTopDriftRTPC: FName
    mEngineSoundLoop: Ptr[AkComponent]
    mIsAudioOnloading: bool
    mAudioPreviousGear: int32 = 10
    NewVar_0: float
    mRTPCOffloadState: FName = RTPC_Explorer_OffloadState
    MPlayVehicleTransmission: Ptr[AkAudioEvent] = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Explorer/Audio/Rework/Play_Vehicle_Explorer_Rework_Transmission.Play_Vehicle_Explorer_Rework_Transmission')
    mFuelConsumption = 150
    mDistBetweenDecals = 50
    mDecalLifespan = 5
    mDecalSize = Namespace(X=35, Y=50, Z=1)
    mFoliageDestroyRadius = 200
    mAddedGroundAngularVelocityStrengthYaw = 1.7000000476837158
    mAddedGroundAngularVelocityStrengthPitch = 1
    mAddedAirControlAngularVelocityStrengthYaw = 1.5
    mAddedAirControlAngularVelocityStrengthPitch = 1.399999976158142
    mNaturalAngularVelocityStrengthYaw = 1.5
    mNaturalAngularVelocityStrengthPitch = 0.800000011920929
    mNaturalAirAngularVelocityStrengthYaw = 1.5
    mNaturalAirAngularVelocityStrengthPitch = 1
    mAddedAngularVelocityInputSmoothingSpeed = 0.5
    mFoliageCollideBox = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', AttachParent={'$ObjectClass': '/Script/Engine.SkeletalMeshComponent', '$ObjectFlags': 2883617, '$ObjectName': 'VehicleMesh', 'ClothingSimulationFactory': '/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', 'bGenerateOverlapEvents': True, 'BodyInstance': {'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 0, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}}, BodyInstance={'ObjectType': 1, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WorldStatic', 'Response': 1}, {'Channel': 'WorldDynamic', 'Response': 1}, {'Channel': 'Pawn', 'Response': 1}, {'Channel': 'Visibility', 'Response': 1}, {'Channel': 'Camera', 'Response': 1}, {'Channel': 'PhysicsBody', 'Response': 1}, {'Channel': 'Vehicle', 'Response': 1}, {'Channel': 'Destructible', 'Response': 1}, {'Channel': 'Projectile', 'Response': 1}, {'Channel': 'BuildGun', 'Response': 1}, {'Channel': 'WeaponInstantHit', 'Response': 1}, {'Channel': 'VehicleWheelQuery', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, ObjectClass='/Script/Engine.BoxComponent', ObjectFlags=2883617, ObjectName='FoliageBox')
    mSimulationDistance = 20000
    mSimulationMovementComponent = Namespace(Acceleration=0, MaxSpeed=0, ObjectClass='/Script/Engine.FloatingPawnMovement', ObjectFlags=2883617, ObjectName='SimulationComponent', bReplicates=True)
    mVehicleParticeMap = [{'EmitterTemplate': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Particle/TiresmokeMetal.TiresmokeMetal'}, 'Surface': 0}, {'EmitterTemplate': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Particle/TiresmokeSand.TiresmokeSand'}, 'Surface': 1}, {'EmitterTemplate': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Particle/TiresmokeMetal.TiresmokeMetal'}, 'Surface': 2}, {'EmitterTemplate': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Particle/TiresmokeRock.TiresmokeRock'}, 'Surface': 3}, {'EmitterTemplate': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Particle/TiresmokeGrass.TiresmokeGrass'}, 'Surface': 4}, {'EmitterTemplate': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Particle/TiresmokeMoist.TiresmokeMoist'}, 'Surface': 5}, {'EmitterTemplate': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/-Shared/Particle/TiresmokeGravel.TiresmokeGravel'}, 'Surface': 6}]
    mTireEffectSocketName = particleSocket
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
    mNeedsFuelToDrive = True
    mHologramClass = NewObject[FGWheeledVehicleHologram]()
    mMesh = Namespace(BodyInstance={'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 0, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='VehicleMesh', bGenerateOverlapEvents=True)
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True, mCurrentHealth=100, mMaxHealth=100)
    mDisabledByWaterLocations = [{'X': 0, 'Y': 0, 'Z': 0}]
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSubmergedAngularDamping = 6
    mSubmergedLinearDamping = 15
    mSubmergedBouyantForce = 1000
    mGasDamageType = NewObject[DamageType_GasCloud]()
    mAddToSignificanceManager = True
    mSignificanceRange = 15000
    mShouldAttachDriver = True
    AIControllerClass = NewObject[BP_SelfDrivingController]()
    ReplicatedMovement = Namespace(LocationQuantizationLevel='EVectorQuantization::RoundTwoDecimals', RotationQuantizationLevel='ERotatorQuantization::ShortComponents', VelocityQuantizationLevel='EVectorQuantization::RoundTwoDecimals')
    RootComponent = Namespace(BodyInstance={'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 0, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='VehicleMesh', bGenerateOverlapEvents=True)
    
    def GetActorCompassViewDistance(self):
        ReturnValue = 4
    

    def SetActorCompassViewDistance(self):
        ReturnValue = 0
    

    def SetActorRepresentationText(self):
        self.FlushNetDormancy()
        self.mMapText = newText
        ReturnValue = self.mMapText
    

    def UpdateRepresentation(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L145')
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = ReturnValue_0.UpdateRepresentation(self, False)
        ReturnValue_2: bool = ReturnValue_1
        goto('L156')
        # Label 145
        ReturnValue_2 = False
    

    def GetActorRepresentationColor(self):
        if not self.mPossessed:
            goto('L175')
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](self.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
            goto('L175')
        # Label 93
        ReturnValue: LinearColor = State.GetNametagColor()
        ReturnValue_0: LinearColor = ReturnValue
        goto('L257')
        
        Text = None
        Graphics = None
        # Label 175
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        # Label 230
        ReturnValue_0 = Graphics
    

    def GetActorRepresentationText(self):
        ReturnValue = self.mMapText
    

    def GetActorRepresentationTexture(self):
        ReturnValue = MapCompass_Icon_tractor
    

    def GetActorRepresentationType(self):
        ReturnValue = 12
    

    def GetActorShouldShowInCompass(self):
        ReturnValue = True
    

    def GetActorFogOfWarRevealRadius(self):
        ReturnValue = 50000
    

    def GetActorFogOfWarRevealType(self):
        Variable: uint8 = 3
        Variable1: uint8 = 0
        Variable_0: bool = self.mPossessed
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue = switch.get(Variable_0, None)
    

    def RemoveAsRepresentation(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L144')
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = ReturnValue_0.RemoveRepresentationOfActor(self)
        ReturnValue_2: bool = ReturnValue_1
        goto('L155')
        # Label 144
        ReturnValue_2 = False
    

    def AddAsRepresentation(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L145')
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = ReturnValue_0.CreateAndAddNewRepresentation(self, False)
        ReturnValue_2: bool = ReturnValue_1
        goto('L156')
        # Label 145
        ReturnValue_2 = False
    

    def GetActorShouldShowOnMap(self):
        ReturnValue = True
    

    def GetRealActorLocation(self):
        ReturnValue: Ptr[FGTargetPointLinkedList] = self.GetTargetNodeLinkedList()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L590')
        ReturnValue2: Ptr[FGTargetPointLinkedList] = self.GetTargetNodeLinkedList()
        ReturnValue1: Ptr[FGTargetPoint] = ReturnValue2.GetCurrentTarget()
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        ReturnValue_1: bool = self.IsSimulated()
        ReturnValue_2: bool = ReturnValue_1 and ReturnValue1_0
        if not ReturnValue_2:
            goto('L650')
        ReturnValue1_1: Vector = self.K2_GetActorLocation()
        ReturnValue1_2: Ptr[FGTargetPointLinkedList] = self.GetTargetNodeLinkedList()
        ReturnValue_3: float = self.mTimeSpentOnTarget / self.mRecordInterval
        ReturnValue_4: Ptr[FGTargetPoint] = ReturnValue1_2.GetCurrentTarget()
        ReturnValue_5: float = FClamp(ReturnValue_3, 0, 1)
        # Label 453
        ReturnValue2_0: Vector = ReturnValue_4.K2_GetActorLocation()
        ReturnValue_6: Vector = VLerp(ReturnValue1_1, ReturnValue2_0, ReturnValue_5)
        ReturnValue_7: Vector = ReturnValue_6
        goto('L705')
        # Label 590
        ReturnValue_8: Vector = self.K2_GetActorLocation()
        ReturnValue_7 = ReturnValue_8
        goto('L705')
        # Label 650
        ReturnValue3: Vector = self.K2_GetActorLocation()
        ReturnValue_7 = ReturnValue3
    

    def GetRealActorRotation(self):
        ReturnValue = Rotator::FromPitchYawRoll(0, 0, 0)
    

    def IsActorStatic(self):
        ReturnValue = False
    

    def UpdateAudioGear(self):
        ReturnValue1: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue1_0: int32 = ReturnValue1.GetCurrentGear()
        ReturnValue: bool = ReturnValue1_0 != self.mAudioCurrentGear
        if not ReturnValue:
            goto('L751')
        ReturnValue1 = self.GetVehicleMovementComponent()
        ReturnValue1_0 = ReturnValue1.GetCurrentGear()
        self.mAudioCurrentGear = ReturnValue1_0
        if not self.mIsAudioOnloading:
            goto('L374')
        ReturnValue_0: float = self.GetInputAxisValue("MoveForward")
        ReturnValue_1: bool = ReturnValue_0 <= 0
        if not ReturnValue_1:
            goto('L476')
        Default__AkGameplayStatics.SetActorRTPCValue(self.mAudioGearRTPC, -1, 0, self)
        # Label 374
        ReturnValue_2: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue_3: int32 = ReturnValue_2.GetCurrentGear()
        self.mAudioPreviousGear = ReturnValue_3
        # End
        # Label 476
        ReturnValue_4: float = Conv_IntToFloat(self.mAudioCurrentGear)
        Default__AkGameplayStatics.SetActorRTPCValue(self.mAudioGearRTPC, ReturnValue_4, 0, self)
        ReturnValue_5: bool = self.mAudioCurrentGear > 1
        ReturnValue1_1: bool = self.mAudioCurrentGear > self.mAudioPreviousGear
        ReturnValue_6: bool = ReturnValue1_1 and ReturnValue_5
        if not ReturnValue_6:
            goto('L374')
        ReturnValue_7: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.MPlayVehicleTransmission, self, True)
        goto('L374')
    

    def UpdateOutline(self, aimingAtWorkbench: bool):
        Variable: bool = aimingAtWorkbench
        # Label 19
        Variable_0: uint8 = 0
        Variable1: uint8 = 252
        
        switch = {
            False: Variable1,
            True: Variable_0
        }
        Default__FGBlueprintFunctionLibrary.ShowOutline(self.mMesh, switch.get(Variable, None))
    

    def UpdateTireSound(self):
        ReturnValue: Ptr[PhysicalMaterial] = self.GetCachedSurfaceMaterial()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L1343')
        ReturnValue_1: float = RandomFloatInRange(self.mMinAudioPeakFlutter, self.mMaxAudioPeakFlutter)
        ReturnValue_2: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue1: float = RandomFloatInRange(self.mMinSteeringAudioFlutter, self.mMaxSteeringAudioFlutter)
        ReturnValue_3: float = ReturnValue_2.GetSteering()
        ReturnValue_4: float = Abs(ReturnValue_3)
        # Label 284
        ReturnValue_5: bool = EqualEqual_FloatFloat(ReturnValue_4, 1)
        Variable: bool = ReturnValue_5
        
        switch = {
            False: ReturnValue_1,
            True: ReturnValue1
        }
        self.mAudioPeakFlutter = switch.get(Variable, None)
        Variable_0: FName = "None"
        Variable1: FName = "Surface_Panel"
        Variable2: FName = "Surface_Coral"
        Variable3: FName = "Surface_Grate"
        Variable4: FName = "Surface_Cement"
        Variable5: FName = "Surface_Soil"
        Variable6: FName = "Surface_SandCracked"
        Variable7: FName = "Surface_RockGravel"
        Variable8: FName = "Surface_Grass_High"
        Variable9: FName = "Surface_Gravel"
        Variable10: FName = "Surface_Moist"
        Variable11: FName = "Surface_Grass"
        Variable12: FName = "Surface_Rock"
        Variable13: FName = "Surface_Metal"
        Variable14: FName = "Surface_Sand"
        Variable15: FName = "Surface_Default"
        ReturnValue = self.GetCachedSurfaceMaterial()
        Variable_1: uint8 = ReturnValue.SurfaceType
        
        switch_0 = {
            0: Variable15,
            1: Variable14,
            2: Variable13,
            3: Variable12,
            4: Variable11,
            5: Variable10,
            6: Variable9,
            7: Variable8,
            8: Variable7,
            9: Variable6,
            10: Variable5,
            11: Variable4,
            12: Variable3,
            13: Variable2,
            14: Variable1,
            15: Variable_0
        }
        ReturnValue_6: FString = Default__KismetStringLibrary.Conv_NameToString(switch_0.get(Variable_1, None))
        self.mTireSoundLoop.SetSwitch(self.mTireSoundSwitchGroup, ReturnValue_6)
        # End
        # Label 1343
        ReturnValue_7: bool = self.GetIsInAir()
        if not ReturnValue_7:
            goto('L1435')
        self.mTireSoundLoop.SetSwitch(self.mTireSoundSwitchGroup, "Surface_IsInAir")
    

    def BurnOutSound(self, ForwardInputInput: float):
        ExecutionFlow.Push("L1514")
        ExecutionFlow.Push("L375")
        ReturnValue: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        # Label 30
        ReturnValue_0: bool = GreaterEqual_IntInt(self.mSpeedInKMH, 25)
        ReturnValue_1: float = ReturnValue.GetSteering()
        ReturnValue_2: float = Abs(ReturnValue_1)
        ReturnValue_3: bool = EqualEqual_FloatFloat(ReturnValue_2, 1)
        ReturnValue_4: bool = ReturnValue_3 and ReturnValue_0
        ReturnValue1: Ptr[PhysicalMaterial] = self.GetCachedSurfaceMaterial()
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        ReturnValue1_1: bool = ReturnValue_4 and ReturnValue1_0
        if not ReturnValue1_1:
            goto('L1173')
        if not self.mIsUsingGolfCartRPM:
            goto('L1248')
        # Label 360
        if not self.mIsTopDrifting:
            goto('L1346')
        # Label 374
        goto(ExecutionFlow.Pop())
        # Label 375
        ReturnValue_5: bool = ForwardInputInput > 0
        ReturnValue_6: Ptr[PhysicalMaterial] = self.GetCachedSurfaceMaterial()
        ReturnValue_7: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_6)
        ReturnValue_8: bool = self.mSpeedInKMH <= self.mBurnOutSpeedThres
        ReturnValue2: bool = ReturnValue_5 and ReturnValue_8
        ReturnValue3: bool = ReturnValue2 and ReturnValue_7
        if not ReturnValue3:
            goto('L971')
        ReturnValue2_0: float = Conv_IntToFloat(self.mSpeedInKMH)
        ReturnValue_9: bool = GreaterEqual_FloatFloat(ReturnValue2_0, self.mCheckValueForBurnOut)
        if not ReturnValue_9:
            goto('L971')
        ReturnValue2_0 = Conv_IntToFloat(self.mSpeedInKMH)
        self.mCheckValueForBurnOut = ReturnValue2_0
        ReturnValue1_2: float = Conv_IntToFloat(self.mBurnOutSpeedThres)
        ReturnValue2_0 = Conv_IntToFloat(self.mSpeedInKMH)
        ReturnValue_10: float = MapRangeClamped(ReturnValue2_0, 0, ReturnValue1_2, 0, self.BurnOutRTPCRange)
        Default__AkGameplayStatics.SetActorRTPCValue(self.mBurnOutRTPC, ReturnValue_10, 0, self)
        if not self.mIsBurningOut:
            goto('L1430')
        goto(ExecutionFlow.Pop())
        # Label 971
        ReturnValue2_0 = Conv_IntToFloat(self.mSpeedInKMH)
        self.mCheckValueForBurnOut = ReturnValue2_0
        if not self.mIsBurningOut:
           goto(ExecutionFlow.Pop())
        ReturnValue_11: bool = ForwardInputInput <= 0
        if not ReturnValue_11:
           goto(ExecutionFlow.Pop())
        ReturnValue2_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mStopBurnOutSound, self, True)
        self.StopIsBurningOut = ReturnValue2_1
        self.mIsBurningOut = False
        goto(ExecutionFlow.Pop())
        # Label 1173
        if not self.mIsTopDrifting:
           goto(ExecutionFlow.Pop())
        ReturnValue1_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mStopAudioTopDrift, self, True)
        self.mIsTopDrifting = False
        goto(ExecutionFlow.Pop())
        # Label 1248
        ReturnValue_12: float = Conv_IntToFloat(self.mSpeedInKMH)
        Default__AkGameplayStatics.SetActorRTPCValue(self.mTopDriftRTPC, ReturnValue_12, 0, self)
        goto('L360')
        # Label 1346
        ReturnValue_13: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mPlayAudioTopDrift, self, True)
        self.mPlayTopDrift = ReturnValue_13
        self.mIsTopDrifting = True
        goto(ExecutionFlow.Pop())
        # Label 1430
        ReturnValue3_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mPlayBurnOutSound, self, True)
        self.mPlayIsBurningOut = ReturnValue3_0
        self.mIsBurningOut = True
        goto(ExecutionFlow.Pop())
    

    def GetDriftForceOffset(self):
        ReturnValue: Vector = self.DriftForceLocation.K2_GetComponentLocation()
        ReturnValue_0: Vector = ReturnValue
    

    def ShouldStopVehicle(self):
        ReturnValue: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue_0: bool = self.GetIsDrifting()
        ReturnValue_1: float = ReturnValue.GetThrottle()
        ReturnValue_2: bool = NearlyEqual_FloatFloat(ReturnValue_1, 0, 0.009999999776482582)
        ReturnValue_3: bool = ReturnValue_0 and ReturnValue_2
        ShouldStop = ReturnValue_3
    

    def TurnOverVehicle(self):
        ReturnValue: Rotator = self.K2_GetActorRotation()
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_0: Rotator = MakeRotator(0, 0, Yaw)
        ReturnValue_1: bool = self.K2_SetActorRotation(ReturnValue_0, True)
    

    def AdjustThrottle(self, Throttle: float):
        throttle: float = Throttle
        ReturnValue: bool = self.HasFuel()
        if not ReturnValue:
            goto('L93')
        # Label 61
        adjustedThrottle = throttle
        # End
        # Label 93
        throttle = 0
        goto('L61')
    

    def TogglePathVisibility(self):
        ReturnValue1: bool = self.GetPathVisibility()
        ReturnValue: bool = Not_PreBool(ReturnValue1)
        self.SetPathVisibility(ReturnValue)
        ReturnValue_0: bool = self.GetPathVisibility()
        ReturnValue_1: Ptr[FGTargetPointLinkedList] = self.GetTargetNodeLinkedList()
        ReturnValue_1.SetPathVisibility(ReturnValue_0)
    

    def ToggleAutoPilot(self):
        self.FlushNetDormancy()
        ReturnValue: bool = Not_PreBool(self.mIsAutoPilotEnabled)
        self.mIsAutoPilotEnabled = ReturnValue
    

    def TogglePauseRecording(self):
        self.FlushNetDormancy()
        ReturnValue: bool = Not_PreBool(self.mIsRecording)
        self.mIsRecording = ReturnValue
        self.OnRep_mIsRecording()
    

    def TickSimulationMovement(self):
        ReturnValue: bool = self.HasFuel()
        ReturnValue_0: bool = Default__KismetSystemLibrary.K2_IsValidTimerHandle(self.mUpdateMovementHandle)
        ReturnValue_1: bool = self.IsSimulated()
        ReturnValue_2: bool = ReturnValue_0 and ReturnValue_1
        ReturnValue1: bool = ReturnValue_2 and ReturnValue
        if not ReturnValue1:
            goto('L544')
        ReturnValue1_0: Ptr[FloatingPawnMovement] = self.GetSimulationComponent()
        ReturnValue_3: Rotator = self.K2_GetActorRotation()
        ReturnValue_4: Vector = GetForwardVector(ReturnValue_3)
        ReturnValue_5: Vector = ReturnValue_4 * 800
        ReturnValue1_0.AddInputVector(ReturnValue_5, False)
        ReturnValue_6: Ptr[FloatingPawnMovement] = self.GetSimulationComponent()
        # Label 374
        ReturnValue_7: float = Conv_IntToFloat(self.mSpeedLimit)
        ReturnValue_8: float = ReturnValue_7 / 3.5999999046325684
        # Label 453
        ReturnValue_9: float = ReturnValue_8 * 100
        ReturnValue_6.MaxSpeed = ReturnValue_9
    

    def CalculateReverseSteering(self):
        ReturnValue: float = RandomFloatInRange(-0.800000011920929, 0.800000011920929)
        # Label 38
        ReturnValue_0: Rotator = self.K2_GetActorRotation()
        # Label 66
        ReturnValue_1: Vector = self.K2_GetActorLocation()
        
        ReturnValue_2: Rotator = FindLookAtRotation(Ref[ReturnValue_1], Ref[self.mCurrentDestination])
        ReturnValue_3: Rotator = NormalizedDeltaRotator(ReturnValue_2, ReturnValue_0)
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_3, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_4: float = MapRangeUnclamped(Yaw, -180, 180, 1, -1)
        ReturnValue_5: float = Abs(ReturnValue_4)
        ReturnValue_6: bool = ReturnValue_5 <= 0.20000000298023224
        # Label 360
        ReturnValue_7: float = SelectFloat(ReturnValue, ReturnValue_4, ReturnValue_6)
        self.mReverseSteering = ReturnValue_7
    

    def StopVehicle(self):
        ReturnValue: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue.SetBrakeInput(1)
        ReturnValue = self.GetVehicleMovementComponent()
        ReturnValue.SetThrottleInput(0)
        ReturnValue = self.GetVehicleMovementComponent()
        ReturnValue.SetHandbrakeInput(True)
    

    def canMove(self):
        ReturnValue: Ptr[FGTargetPointLinkedList] = self.GetTargetNodeLinkedList()
        ReturnValue_0: Ptr[FGTargetPoint] = ReturnValue.GetCurrentTarget()
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L284')
        ReturnValue = self.GetTargetNodeLinkedList()
        ReturnValue_0 = ReturnValue.GetCurrentTarget()
        ReturnValue_2: bool = ReturnValue_0.IsTargetSpeedStill()
        ReturnValue_3: bool = Not_PreBool(ReturnValue_2)
        canMove = ReturnValue_3
        # End
        # Label 284
        canMove = False
    

    def UpdateEngineLoadSound(self, dt: float):
        ReturnValue: float = dt * 1
        ReturnValue1: float = ReturnValue * self.mAudioSign
        ReturnValue_0: float = self.mEngineLoadTimer + ReturnValue1
        ReturnValue_1: float = FMin(ReturnValue_0, self.mEngineLoadTimerMax)
        ReturnValue_2: float = FMax(ReturnValue_1, 0)
        self.mEngineLoadTimer = ReturnValue_2
        ReturnValue_3: bool = EqualEqual_FloatFloat(self.mEngineLoadTimer, self.mEngineLoadTimerMax)
        if not ReturnValue_3:
            goto('L315')
        # Label 301
        self.DidGearUp()
    

    def UpdateAccelerationSound(self):
        if not self.mDidSwitchThrottleState:
            goto('L483')
        ReturnValue: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue_0: float = ReturnValue.GetThrottle()
        ReturnValue_1: bool = ReturnValue_0 > 0
        if not ReturnValue_1:
            goto('L230')
        self.mAudioSign = 1
        # Label 155
        self.StartAccelerating()
        # Label 169
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_Industrial_Truck_AccelState", 1, 100, self)
        # End
        # Label 230
        ReturnValue1: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue1_0: float = ReturnValue1.GetThrottle()
        ReturnValue_2: bool = ReturnValue1_0 <= 0
        if not ReturnValue_2:
            goto('L390')
        self.mAudioSign = 1
        self.StartAccelerating()
        goto('L169')
        # Label 390
        self.mAudioSign = -1
        self.StopAccelerating()
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_Industrial_Truck_AccelState", 0, 100, self)
    

    def UpdateThrottleState(self):
        ReturnValue: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue_0: float = ReturnValue.GetThrottle()
        ReturnValue_1: bool = NotEqual_FloatFloat(self.mPreviousThrottleValue, ReturnValue_0)
        if not ReturnValue_1:
            goto('L235')
        ReturnValue = self.GetVehicleMovementComponent()
        ReturnValue_0 = ReturnValue.GetThrottle()
        self.mPreviousThrottleValue = ReturnValue_0
        self.mDidSwitchThrottleState = True
        # Label 230
        # End
        # Label 235
        self.mDidSwitchThrottleState = False
    

    def DidGearDown(self):
        ReturnValue: float = self.mEngineLoadTimer * 0.699999988079071
        self.mEngineLoadTimer = ReturnValue
        ReturnValue_0: bool = self.GetIsSignificant()
        ReturnValue_1: bool = self.HasFuel()
        ReturnValue_2: bool = ReturnValue_1 and ReturnValue_0
        if not ReturnValue_2:
            goto('L214')
        ReturnValue_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mEngineRevDown, self, True)
    

    def DidGearUp(self):
        ReturnValue: float = self.mEngineLoadTimer * 0.5
        ReturnValue1: float = self.mEngineLoadTimerMax * 0.800000011920929
        ReturnValue_0: bool = self.mEngineLoadTimer > ReturnValue1
        ReturnValue_1: float = SelectFloat(ReturnValue, self.mEngineLoadTimer, ReturnValue_0)
        self.mEngineLoadTimer = ReturnValue_1
        ReturnValue_2: bool = self.GetIsSignificant()
        ReturnValue_3: bool = self.HasFuel()
        ReturnValue_4: bool = ReturnValue_3 and ReturnValue_2
        if not ReturnValue_4:
            goto('L349')
        ReturnValue_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mEngineRevUp, self, True)
    

    def CheckCurrentGear(self):
        ReturnValue1: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue1_0: int32 = ReturnValue1.GetCurrentGear()
        ReturnValue: bool = ReturnValue1_0 != 0
        ReturnValue1_1: bool = ReturnValue1_0 != self.mCachedGear
        ReturnValue_0: bool = ReturnValue and ReturnValue1_1
        if not ReturnValue_0:
            goto('L451')
        ReturnValue1 = self.GetVehicleMovementComponent()
        # Label 214
        ReturnValue1_0 = ReturnValue1.GetCurrentGear()
        ReturnValue_1: bool = ReturnValue1_0 > self.mCachedGear
        if not ReturnValue_1:
            goto('L432')
        self.DidGearUp()
        # Label 330
        ReturnValue_2: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue_3: int32 = ReturnValue_2.GetCurrentGear()
        self.mCachedGear = ReturnValue_3
        # End
        # Label 432
        self.DidGearDown()
        goto('L330')
    

    def StopSoundLoops(self):
        if not self.mDidStartSoundLoops:
            goto('L455')
        self.mDidStartSoundLoops = False
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(self.mEngineLoopStop, self.mMesh, self.mEngineSocketName, True)
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mTireLoopStop, self, True)
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(self.mExhaustLoopStop, self.mMesh, self.mExhaustSocketName, True)
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(self.mStopRevEngine, self.mMesh, self.mExhaustSocketName, True)
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(self.mStopRevExhaust, self.mMesh, self.mEngineSocketName, True)
        if not self.mShouldUpdateTireSurfaces:
            goto('L414')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mTireSoundTimer])
        # Label 414
        Default__AkGameplayStatics.StopAndDestroyComponent(self.mTireSoundLoop)
    

    def StartSoundLoops(self):
        if not self.mDidStartSoundLoops:
            goto('L19')
        # End
        # Label 19
        ReturnValue: bool = self.HasFuel()
        if not ReturnValue:
            goto('L424')
        self.mDidStartSoundLoops = True
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(self.mEngineLoopStart, self.mMesh, self.mEngineSocketName, True)
        self.mEngineSoundLoop = ReturnValue1
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mTireLoopStart, self, True)
        self.mTireSoundLoop = ReturnValue_0
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(self.mExhaustLoopStart, self.mMesh, self.mExhaustSocketName, True)
        if not self.mShouldUpdateTireSurfaces:
            goto('L424')
        OutputDelegate.BindUFunction(self, UpdateTireSound)
        ReturnValue_2: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 1, True)
        self.mTireSoundTimer = ReturnValue_2
    

    def ToggleFreeCamera(self):
        ReturnValue: bool = Not_PreBool(self.mIsFreeCamera)
        self.mIsFreeCamera = ReturnValue
    

    def GetLookAtDecription(self):
        ReturnValue: bool = EqualEqual_ClassClass(State.State, UseState_WorkBench)
        if not ReturnValue:
            goto('L484')
        # Label 61
        ReturnValue_0: Ptr[Controller] = byCharacter.GetController()
        
        button = None
        Default__HUDHelpers.GetKeyNameForActionSimple(ReturnValue_0, "Use", self, Ref[button])
        FormatArgumentData.ArgumentName = "BUTTON"
        FormatArgumentData.ArgumentValueType = 4
        # Label 235
        FormatArgumentData.ArgumentValue = button
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_1: FText = Default__KismetTextLibrary.Format(self.mLookAtText, Array)
        ReturnValue_2: FText = ReturnValue_1
        goto('L557')
        
        # Label 484
        ReturnValue_3: FText = self.GetLookAtDecription(byCharacter, Ref[State])
        ReturnValue_2 = ReturnValue_3
    

    def OpenVehicleUI(self, inCharacter: Ptr[FGCharacterPlayer]):
        localCharacter = inCharacter
        # Label 19
        ReturnValue: Ptr[Controller] = inCharacter.GetController()
        # Label 61
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L525')
        ReturnValue_0: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_0.ServerOpenVehicleTrunk(self, localCharacter)
        ReturnValue1: Ptr[Controller] = localCharacter.GetController()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1)
        # Label 315
        bSuccess1: bool = Controller1
        if not bSuccess1:
            goto('L525')
        ReturnValue_1: Ptr[HUD] = Controller1.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_1)
        bSuccess2: bool = AsFGHUD
        if not bSuccess2:
            goto('L525')
        AsFGHUD.OpenInteractUI(self.mInteractWidget, self)
    

    def PonderOpeningTrunk(self, inCharacter: Ptr[FGCharacterPlayer]):
        localCharacter = inCharacter
        # Label 19
        ReturnValue: bool = localCharacter.IsLocallyControlled()
        ReturnValue_0: bool = EqualEqual_ObjectObject(self.mTrunkUser, None)
        ReturnValue1: bool = EqualEqual_ObjectObject(self.mTrunkUser, localCharacter)
        ReturnValue_1: bool = BooleanOR(ReturnValue1, ReturnValue_0)
        ReturnValue_2: bool = ReturnValue_1 and ReturnValue
        if not ReturnValue_2:
            goto('L265')
        if not self.mIsInventoryOpen:
            goto('L242')
        # End
        # Label 242
        self.OpenVehicleUI(localCharacter)
    

    def UpdateUseState(self):
        ReturnValue: bool = EqualEqual_ObjectObject(componentHit, self.Box)
        # Label 38
        if not ReturnValue:
            goto('L458')
        
        useState = None
        Default__FGBlueprintFunctionLibrary.UpdateUseState(UseState_WorkBench, Ref[useState])
        # Label 102
        ReturnValue_0: bool = byCharacter.IsLocallyControlled()
        if not ReturnValue_0:
            goto('L860')
        ReturnValue_1: Ptr[Controller] = byCharacter.GetController()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_1)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L860')
        ReturnValue_2: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_2)
        bSuccess2: bool = AsFGHUD
        # Label 390
        if not bSuccess2:
            goto('L860')
        AsFGHUD.SetCrosshairState(5)
        self.UpdateOutline(True)
        # Label 453
        # End
        
        useState = None
        # Label 458
        self.UpdateUseState(byCharacter, componentHit, Ref[atLocation], Ref[useState])
        ReturnValue_0 = byCharacter.IsLocallyControlled()
        if not ReturnValue_0:
            goto('L860')
        ReturnValue_1 = byCharacter.GetController()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_1)
        bSuccess1: bool = Controller1
        if not bSuccess1:
            goto('L860')
        ReturnValue1: Ptr[HUD] = Controller1.GetHUD()
        AsFGHUD1: Ptr[FGHUD] = Cast[FGHUD](ReturnValue1)
        bSuccess3: bool = AsFGHUD1
        if not bSuccess3:
            goto('L860')
        AsFGHUD1.SetCrosshairState(3)
        self.UpdateOutline(False)
        goto('L453')
    

    def OnRep_mIsFollowingPath(self):
        if not self.mIsFollowingPath:
            goto('L33')
        self.StartSoundLoops()
        # End
        # Label 33
        ReturnValue: bool = self.IsDriving()
        if not ReturnValue:
            goto('L72')
        # End
        # Label 72
        self.StopSoundLoops()
    

    def UpdateSpeedLimit(self, TargetPoint: Ptr[BP_VehicleTargetPoint]):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(TargetPoint)
        if not ReturnValue:
            goto('L199')
        self.FlushNetDormancy()
        ReturnValue_0: int32 = TargetPoint.GetTargetSpeed()
        ReturnValue_1: int32 = Max(ReturnValue_0, 10)
        self.mSpeedLimit = ReturnValue_1
        # End
        # Label 199
        self.FlushNetDormancy()
        self.mSpeedLimit = -1
    

    def DoReverseToFreedom(self):
        ReturnValue: float = self.mTimeSpentOnTarget + self.mUpdateDelta
        self.mTimeSpentOnTarget = ReturnValue
        ReturnValue_0: bool = self.mTimeSpentOnTarget <= self.mMaxReverseTime
        if not ReturnValue_0:
            goto('L280')
        
        adjustedThrottle = None
        self.AdjustThrottle(-0.699999988079071, Ref[adjustedThrottle])
        ReturnValue_1: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue_1.SetThrottleInput(adjustedThrottle)
        # Label 214
        ReturnValue1: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue1.SetSteeringInput(self.mReverseSteering)
        # End
        # Label 280
        self.StopVehicle()
        
        self.mUpdateMovementHandle = None
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mUpdateMovementHandle])
        self.LocationReached.ProcessMulticastDelegate()
    

    def ReverseToFreedom(self):
        self.mTimeSpentOnTarget = 0
        
        self.mUpdateMovementHandle = None
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mUpdateMovementHandle])
        ReturnValue: float = RandomFloatInRange(1.2999999523162842, 2.5)
        self.mMaxReverseTime = ReturnValue
        self.CalculateReverseSteering()
        # Label 144
        ReturnValue_0: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue_0.SetHandbrakeInput(False)
        OutputDelegate.BindUFunction(self, DoReverseToFreedom)
        ReturnValue_1: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mUpdateDelta, True)
        self.mUpdateMovementHandle = ReturnValue_1
    

    def CacheSpeedInKMH(self):
        ReturnValue: float = self.GetForwardSpeed()
        ReturnValue_0: float = ReturnValue * 0.035999998450279236
        ReturnValue_1: int32 = FTrunc(ReturnValue_0)
        self.mSpeedInKMH = ReturnValue_1
    

    def OnRep_mIsRecording(self):
        if not self.mIsRecording:
            goto('L38')
        self.OnStartRecording.ProcessMulticastDelegate()
        # Label 33
        # End
        # Label 38
        self.OnStopRecording.ProcessMulticastDelegate()
    

    def MoveToLocation(self):
        self.mTimeSpentOnTarget = 0
        OutputDelegate.BindUFunction(self, UpdateVehicleMovement)
        ReturnValue: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mUpdateDelta, True)
        self.mUpdateMovementHandle = ReturnValue
    

    def TickRecording(self, dt: float):
        ReturnValue: bool = Not_PreBool(self.mIsMenuOpen)
        ReturnValue_0: bool = self.HasAuthority()
        ReturnValue_1: bool = self.mIsRecording and ReturnValue_0
        ReturnValue1: bool = ReturnValue_1 and ReturnValue
        if not ReturnValue1:
            goto('L301')
        ReturnValue_2: float = self.mRecordCounter + dt
        self.mRecordCounter = ReturnValue_2
        ReturnValue_3: bool = GreaterEqual_FloatFloat(self.mRecordCounter, self.mRecordInterval)
        if not ReturnValue_3:
            goto('L301')
        self.mRecordCounter = 0
        self.PlaceTargetPoint()
    

    def UpdateVehicleMovement(self):
        ReturnValue: float = self.mTimeSpentOnTarget + self.mUpdateDelta
        self.mTimeSpentOnTarget = ReturnValue
        ReturnValue_0: Ptr[FGCharacterPlayer] = self.GetDriver()
        # Label 93
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        # Label 144
        if not ReturnValue_1:
            goto('L163')
        # End
        # Label 163
        ReturnValue1: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue1.SetHandbrakeInput(False)
        ReturnValue_2: bool = self.HasFuel()
        ReturnValue_3: bool = self.IsSimulated()
        ReturnValue_4: bool = ReturnValue_3 and ReturnValue_2
        if not ReturnValue_4:
            goto('L775')
        ReturnValue_5: bool = GreaterEqual_FloatFloat(self.mTimeSpentOnTarget, self.mRecordInterval)
        if not ReturnValue_5:
            goto('L822')
        # Label 360
        ReturnValue_6: Ptr[FGTargetPointLinkedList] = self.GetTargetNodeLinkedList()
        ReturnValue_7: Ptr[FGTargetPoint] = ReturnValue_6.GetCurrentTarget()
        ReturnValue_8: Vector = ReturnValue_7.K2_GetActorLocation()
        ReturnValue_9: Rotator = ReturnValue_7.K2_GetActorRotation()
        
        SweepHitResult = None
        ReturnValue_10: bool = self.K2_SetActorLocationAndRotation(ReturnValue_8, ReturnValue_9, False, True, Ref[SweepHitResult])
        
        distance = None
        # Label 571
        self.GetTargetDistance(Ref[distance])
        ReturnValue_11: bool = distance <= 500
        if not ReturnValue_11:
            goto('L822')
        ReturnValue_12: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue_12.SetHandbrakeInput(True)
        self.TargetReached()
        self.LocationReached.ProcessMulticastDelegate()
        
        self.mUpdateMovementHandle = None
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mUpdateMovementHandle])
        # Label 770
        # End
        # Label 775
        self.GatherData()
        self.UpdateSteering()
        self.UpdateThrottle()
        goto('L571')
    

    def StartRecording(self):
        self.FlushNetDormancy()
        self.mIsRecording = True
        self.OnRep_mIsRecording()
        self.FlushNetDormancy()
        self.mIsRecordSessionActive = True
        self.mRecordCounter = self.mRecordInterval
        self.RemoveOldTargets()
    

    def StopRecording(self):
        self.FlushNetDormancy()
        self.mIsRecordSessionActive = False
        self.FlushNetDormancy()
        self.mIsRecording = False
        self.OnRep_mIsRecording()
        self.mRecordCounter = 0
    

    def GatherData(self):
        ReturnValue: Rotator = self.K2_GetActorRotation()
        ReturnValue_0: Vector = self.K2_GetActorLocation()
        
        ReturnValue_1: Rotator = FindLookAtRotation(Ref[ReturnValue_0], Ref[self.mCurrentDestination])
        # Label 102
        ReturnValue_2: Rotator = NormalizedDeltaRotator(ReturnValue_1, ReturnValue)
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_2, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_3: float = MapRangeClamped(Yaw, -25, 25, -1, 1)
        self.mDesiredSteering = ReturnValue_3
        ReturnValue = self.K2_GetActorRotation()
        ReturnValue_0 = self.K2_GetActorLocation()
        
        ReturnValue_1 = FindLookAtRotation(Ref[ReturnValue_0], Ref[self.mCurrentDestination])
        ReturnValue_2 = NormalizedDeltaRotator(ReturnValue_1, ReturnValue)
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_2, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_4: bool = InRange_FloatFloat(Yaw, -120, 120, True, True)
        self.mObjectInFront = ReturnValue_4
        
        distance = None
        self.GetTargetDistance(Ref[distance])
        ReturnValue_5: bool = distance <= self.mReverseMaxDistance
        ReturnValue_6: bool = Not_PreBool(self.mObjectInFront)
        ReturnValue_7: bool = ReturnValue_6 and ReturnValue_5
        self.mCloseEnoughToReverse = ReturnValue_7
    

    def RemoveOldTargets(self):
        ReturnValue: Ptr[FGTargetPointLinkedList] = self.GetTargetNodeLinkedList()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L137')
        ReturnValue = self.GetTargetNodeLinkedList()
        ReturnValue.ClearRecording()
    

    def PlaceTargetPoint(self):
        ReturnValue2: Ptr[FGTargetPointLinkedList] = self.GetTargetNodeLinkedList()
        ReturnValue2_0: Ptr[FGTargetPoint] = ReturnValue2.GetLastTarget()
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(ReturnValue2_0)
        if not ReturnValue:
            goto('L476')
        ReturnValue1: Ptr[FGTargetPointLinkedList] = self.GetTargetNodeLinkedList()
        ReturnValue1_0: Ptr[FGTargetPoint] = ReturnValue1.GetLastTarget()
        ReturnValue_0: bool = ReturnValue1_0.IsTargetSpeedStill()
        ReturnValue_1: float = ReturnValue1_0.GetDistanceTo(self)
        ReturnValue_2: bool = ReturnValue_1 <= 100
        ReturnValue_3: bool = ReturnValue_0 and ReturnValue_2
        if not ReturnValue_3:
            goto('L476')
        ReturnValue_4: Ptr[FGTargetPointLinkedList] = self.GetTargetNodeLinkedList()
        ReturnValue_5: Ptr[FGTargetPoint] = ReturnValue_4.GetLastTarget()
        ReturnValue_5.IncreaseWaitTime(self.mRecordInterval)
        # End
        # Label 476
        ReturnValue_6: Transform = self.GetTransform()
        
        ReturnValue_7: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_VehicleTargetPoint, 0, None, Ref[ReturnValue_6])
        ReturnValue_8: int32 = Abs_Int(self.mSpeedInKMH)
        Default__KismetSystemLibrary.SetIntPropertyByName(ReturnValue_7, "mTargetSpeed", ReturnValue_8)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_7, "Instigator", self)
        ReturnValue_6 = self.GetTransform()
        
        # Label 751
        ReturnValue_9: Ptr[BP_VehicleTargetPoint] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_7, Ref[ReturnValue_6])
        localNewPoint = ReturnValue_9
        localNewPoint.SetOwningVehicle(self)
        localNewPoint.SetMeshRotation()
        ReturnValue3: Ptr[FGTargetPointLinkedList] = self.GetTargetNodeLinkedList()
        ReturnValue3.InsertItem(localNewPoint)
    

    def TargetReached(self):
        pass
    

    def SetNewPath(self):
        ReturnValue1: Ptr[FGTargetPointLinkedList] = self.GetTargetNodeLinkedList()
        ReturnValue1.SetNextTarget()
        self.mTimeSpentOnTarget = 0
        ReturnValue: Ptr[FGTargetPointLinkedList] = self.GetTargetNodeLinkedList()
        ReturnValue_0: Ptr[FGTargetPoint] = ReturnValue.GetCurrentTarget()
        # Label 137
        Point: Ptr[BP_VehicleTargetPoint] = Cast[BP_VehicleTargetPoint](ReturnValue_0)
        bSuccess: bool = Point
        localElement = Point
        self.UpdateSpeedLimit(localElement)
        ReturnValue_1: Vector = localElement.K2_GetActorLocation()
        self.mCurrentDestination = ReturnValue_1
        newTarget = localElement
    

    def GetTargetDistance(self):
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue_0: Vector = Subtract_VectorVector(ReturnValue, self.mCurrentDestination)
        ReturnValue_1: float = VSize(ReturnValue_0)
        Distance = ReturnValue_1
    

    def UpdateThrottle(self):
        ReturnValue: float = Abs(self.mDesiredSteering)
        ReturnValue_0: bool = ReturnValue > 0.5
        ReturnValue1: bool = GreaterEqual_IntInt(self.mSpeedInKMH, 10)
        ReturnValue_1: bool = ReturnValue1 and ReturnValue_0
        localSpeedToHighForTurn = ReturnValue_1
        ReturnValue_2: bool = self.mSpeedInKMH > self.mSpeedLimit
        ReturnValue_3: bool = self.mSpeedLimit != -1
        ReturnValue1_0: bool = ReturnValue_3 and ReturnValue_2
        if not ReturnValue1_0:
            goto('L529')
        ReturnValue2: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue2.SetThrottleInput(0)
        ReturnValue_4: bool = EqualEqual_IntInt(self.mSpeedLimit, 0)
        ReturnValue_5: bool = GreaterEqual_IntInt(self.mSpeedInKMH, self.mSpeedLimit)
        ReturnValue_6: bool = BooleanOR(ReturnValue_4, ReturnValue_5)
        # Label 453
        if not ReturnValue_6:
            goto('L994')
        ReturnValue_7: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue_7.SetBrakeInput(1)
        # End
        # Label 529
        ReturnValue_8: bool = Not_PreBool(self.mObjectInFront)
        ReturnValue2_0: bool = ReturnValue_8 and self.mCloseEnoughToReverse
        ReturnValue_9: float = SelectFloat(-1, 1, ReturnValue2_0)
        
        adjustedThrottle = None
        self.AdjustThrottle(ReturnValue_9, Ref[adjustedThrottle])
        localThrottle = adjustedThrottle
        ReturnValue1_1: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue1_1.SetThrottleInput(localThrottle)
        Variable: float = 1
        Variable1: float = 0
        Variable_0: bool = localSpeedToHighForTurn
        ReturnValue1_1 = self.GetVehicleMovementComponent()
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue1_1.SetBrakeInput(switch.get(Variable_0, None))
        ReturnValue1_1 = self.GetVehicleMovementComponent()
        ReturnValue1_1.SetHandbrakeInput(localSpeedToHighForTurn)
    

    def UpdateSteering(self):
        ReturnValue: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue_0: bool = Not_PreBool(self.mObjectInFront)
        ReturnValue_1: bool = ReturnValue_0 and self.mCloseEnoughToReverse
        ReturnValue_2: float = SelectFloat(0, self.mDesiredSteering, ReturnValue_1)
        ReturnValue.SetSteeringInput(ReturnValue_2)
    

    def InpActEvt_Use_K2Node_InputActionEvent_6(self, Key: Key):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputActionEvent_Key6 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(7756)
    

    def InpActEvt_Reload_K2Node_InputActionEvent_5(self, Key: Key):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputActionEvent_Key5 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(7103)
    

    def InpActEvt_Jump_Drift_K2Node_InputActionEvent_4(self, Key: Key):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputActionEvent_Key4 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(6462)
    

    def InpActEvt_Jump_Drift_K2Node_InputActionEvent_3(self, Key: Key):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputActionEvent_Key3 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(6423)
    

    def InpActEvt_ResourceScanner_ToggleVehicleRecording_K2Node_InputActionEvent_2(self, Key: Key):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputActionEvent_Key2 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(6156)
    

    def InpActEvt_ResourceScanner_ToggleVehicleRecording_K2Node_InputActionEvent_1(self, Key: Key):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputActionEvent_Key1 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(4698)
    

    def InpActEvt_PrimaryFire_K2Node_InputActionEvent_0(self, Key: Key):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputActionEvent_Key = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(4003)
    

    def SetActorRepresentationColor(self):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_newColor = NewColor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(6400)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(6395)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(6371)
    

    def TickVehicleSound(self, dt: float):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_CustomEvent_dt = dt #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(5035)
    

    def ServerToggleRecording(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(3257)
    

    def ReceiveUnpossessed(self):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_OldController = OldController #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(2163)
    

    def ReceiveHit(self):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_MyComp = MyComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_Other = Other #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_bSelfMoved = bSelfMoved #  PERSISTENT_FRAME(
        # Label 72
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_HitLocation = HitLocation #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_HitNormal = HitNormal #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_NormalImpulse = NormalImpulse #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_Hit = Hit #  PERSISTENT_FRAME(
        # Label 144
        self.ExecuteUbergraph_BP_WheeledVehicle(830)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(1532)
    

    def ResetImpactSound(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(1567)
    

    def OnUse(self):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_byCharacter = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(1807)
    

    def Multicast_OpenTrunk(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(2161)
    

    def Multicast_CloseTrunk(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(2162)
    

    def ReceivePossessed(self):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_NewController = NewController #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(2399)
    

    def ClientClearAIMovment(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(2438)
    

    def StartAccelerating(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(2481)
    

    def StopAccelerating(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(2560)
    

    def UpdateCamera(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(3934)
    

    def WasDocked(self):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_atStation = atStation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(3949)
    

    def ServerSetMenuOpen(self, menuOpen: bool):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_CustomEvent_menuOpen = menuOpen #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(4079)
    

    def ServerClearPathRecording(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(4421)
    

    def WasUndocked(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(4450)
    

    def ServerTogglePauseRecording(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(4495)
    

    def ServerToggleAutoPilot(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(4510)
    

    def ServerTogglePathVisibility(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(4525)
    

    def Server_Leave(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(4913)
    

    def ReceiveOnVehicleStartup(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(6106)
    

    def ReceiveOnVehicleShutDown(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(6131)
    

    def ReceiveOnDriverEnter(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(6401)
    

    def ReceiveOnDriverLeave(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(6412)
    

    def InpAxisEvt_MoveForward_K2Node_InputAxisEvent_1(self, AxisValue: float):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputAxisEvent_AxisValue1 = AxisValue #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(6657)
    

    def InpAxisEvt_MoveRight_K2Node_InputAxisEvent_2(self, AxisValue: float):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_InputAxisEvent_AxisValue = AxisValue #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(7016)
    

    def Server_Honk(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(7108)
    

    def Multicast_Honk(self):
        self.ExecuteUbergraph_BP_WheeledVehicle(7123)
    

    def Client_PlayFoliageDestroyedEffect(self):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_destroyEffect = destroyEffect #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_destroyAudioEvent = destroyAudioEvent #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_location = Location #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(7741)
    

    def OpenVehicleTrunk(self):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_player1 = Player #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(7746)
    

    def CloseVehicleTrunk(self):
        ExecuteUbergraph_BP_WheeledVehicle.K2Node_Event_player = Player #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_WheeledVehicle(7751)
    

    def ExecuteUbergraph_BP_WheeledVehicle(self):
        goto(ComputedJump("EntryPoint"))
        self.ResetImpactSound()
        goto(ExecutionFlow.Pop())
        # Label 30
        self.FlushNetDormancy()
        self.mIsInventoryOpen = True
        self.Multicast_OpenTrunk()
        goto(ExecutionFlow.Pop())
        # Label 66
        self.FlushNetDormancy()
        self.mIsInventoryOpen = False
        self.Multicast_CloseTrunk()
        goto(ExecutionFlow.Pop())
        # Label 102
        self.FlushNetDormancy()
        self.mIsAtStation = True
        goto(ExecutionFlow.Pop())
        # Label 124
        self.FlushNetDormancy()
        self.mIsAtStation = False
        # Label 145
        goto(ExecutionFlow.Pop())
        # Label 146
        ReturnValue1: Ptr[BP_RemoteCallObject] = Controller1.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        if not ReturnValue1_0:
            goto('L360')
        ReturnValue1 = Controller1.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue1.Client_AddPawnHUD(self.mHUDClass, self)
        goto(ExecutionFlow.Pop())
        # Label 360
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 146, UUID = 1114818605, ExecutionFunction = "ExecuteUbergraph_BP_WheeledVehicle", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 437
        self.FlushNetDormancy()
        self.mPossessed = True
        # Label 458
        ReturnValue1_1: bool = self.UpdateRepresentation()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](NewController)
        bSuccess1: bool = Controller1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        # Label 557
        goto('L146')
        # Label 562
        self.FlushNetDormancy()
        self.mPossessed = False
        ReturnValue: bool = self.UpdateRepresentation()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](OldController)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_0: Ptr[BP_RemoteCallObject] = Controller.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_0.Client_RemovePawnHUD()
        goto(ExecutionFlow.Pop())
        # Label 770
        self.FlushNetDormancy()
        self.mTrunkUser = player1
        goto('L30')
        # Label 804
        self.FlushNetDormancy()
        self.mTrunkUser = None
        goto('L66')
        ReturnValue_1: int32 = Abs_Int(self.mSpeedInKMH)
        ReturnValue_2: bool = ReturnValue_1 > 1
        ReturnValue_3: bool = self.GetIsSignificant()
        ReturnValue2: bool = ReturnValue_2 and ReturnValue_3
        if not ReturnValue2:
           goto(ExecutionFlow.Pop())
        ReturnValue_4: float = OtherComp.GetMass()
        ReturnValue1_2: int32 = Abs_Int(self.mSpeedInKMH)
        ReturnValue_5: float = Conv_IntToFloat(ReturnValue1_2)
        ReturnValue_6: Vector = self.GetVelocity()
        ReturnValue_7: float = VSize(ReturnValue_6)
        ReturnValue1_3: float = ReturnValue_7 * ReturnValue_4
        Variable4: bool = self.mUseVehicleImpactForce
        
        switch = {
            False: ReturnValue_5,
            True: ReturnValue1_3
        }
        Default__AkGameplayStatics.SetActorRTPCValue(self.RTPCVehicleCrashSpeed, switch.get(Variable4, None), 0, self)
        ExecutionFlow.Push("L1351")
        if not Variable:
            goto('L1507')
        goto(ExecutionFlow.Pop())
        # Label 1351
        if not Variable:
            goto('L1366')
        goto(ExecutionFlow.Pop())
        # Label 1366
        Variable: bool = True
        ReturnValue_8: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mCrashSound, self, True)
        # Label 1430
        Default__KismetSystemLibrary.Delay(self, 0.5, LatentActionInfo(Linkage = 15, UUID = 6232677, ExecutionFunction = "ExecuteUbergraph_BP_WheeledVehicle", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1507
        Variable = True
        if not False:
           goto(ExecutionFlow.Pop())
        Variable = True
        goto(ExecutionFlow.Pop())
        self.ReceiveDestroyed()
        ReturnValue_9: bool = self.RemoveAsRepresentation()
        goto(ExecutionFlow.Pop())
        Variable = False
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 1590
        self.UpdateCamera()
        self.CacheSpeedInKMH()
        self.CheckCurrentGear()
        ReturnValue_10: bool = self.IsSelfDriving()
        ReturnValue1_4: bool = Not_PreBool(ReturnValue_10)
        if not ReturnValue1_4:
           goto(ExecutionFlow.Pop())
        
        ShouldStop = None
        self.ShouldStopVehicle(Ref[ShouldStop])
        if not ShouldStop:
            goto('L1743')
        self.StopVehicle()
        goto(ExecutionFlow.Pop())
        # Label 1743
        if not self.mPossessed:
           goto(ExecutionFlow.Pop())
        ReturnValue2_0: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue2_0.SetHandbrakeInput(False)
        goto(ExecutionFlow.Pop())
        ReturnValue_11: Rotator = self.K2_GetActorRotation()
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_11, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_12: float = Abs(Roll)
        ReturnValue_13: bool = GreaterEqual_FloatFloat(ReturnValue_12, 80)
        if not ReturnValue_13:
            goto('L1981')
        self.TurnOverVehicle()
        goto(ExecutionFlow.Pop())
        # Label 1981
        ReturnValue_14: bool = EqualEqual_ClassClass(state.State, UseState_WorkBench)
        if not ReturnValue_14:
            goto('L2066')
        self.PonderOpeningTrunk(byCharacter)
        goto(ExecutionFlow.Pop())
        # Label 2066
        ReturnValue_15: bool = Default__KismetSystemLibrary.IsValid(self.mTrunkUser)
        if not ReturnValue_15:
            goto('L2132')
        goto(ExecutionFlow.Pop())
        
        state = None
        # Label 2132
        self.OnUse(byCharacter, Ref[state])
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        self.ReceiveUnpossessed(OldController)
        goto('L562')
        # Label 2187
        self.ReceiveBeginPlay()
        ReturnValue_16: bool = self.AddAsRepresentation()
        if not self.mIsAutoPilotEnabled:
            goto('L2260')
        ReturnValue1_5: bool = self.SelfDriverEnter(None)
        # Label 2260
        ReturnValue_17: Ptr[SpringArmComponent] = self.GetComponentByClass(SpringArmComponent)
        ReturnValue2_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_17)
        if not ReturnValue2_1:
           goto(ExecutionFlow.Pop())
        ReturnValue_17 = self.GetComponentByClass(SpringArmComponent)
        self.mSpringArmComponent = ReturnValue_17
        goto(ExecutionFlow.Pop())
        self.ReceivePossessed(NewController)
        goto('L437')
        # Label 2423
        self.ToggleFreeCamera()
        goto(ExecutionFlow.Pop())
        
        self.mUpdateMovementHandle = None
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mUpdateMovementHandle])
        goto(ExecutionFlow.Pop())
        if not self.mIsAudioOnloading:
            goto('L2496')
        goto(ExecutionFlow.Pop())
        # Label 2496
        Default__AkGameplayStatics.SetActorRTPCValue(self.mVehicleAccelerationStateRTPC, 1, 0, self)
        self.mIsAudioOnloading = True
        goto(ExecutionFlow.Pop())
        if not self.mIsUsingNewAudioGears:
            goto('L2764')
        Default__AkGameplayStatics.SetActorRTPCValue(self.mVehicleAccelerationStateRTPC, -1, 0, self)
        ReturnValue5: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue2_2: float = ReturnValue5.GetEngineRotationSpeed()
        Default__AkGameplayStatics.SetActorRTPCValue(self.mRTPCOffloadState, ReturnValue2_2, 0, self)
        self.mIsAudioOnloading = False
        goto(ExecutionFlow.Pop())
        # Label 2764
        Default__AkGameplayStatics.SetActorRTPCValue(self.mVehicleAccelerationStateRTPC, -1, 0, self)
        self.mIsAudioOnloading = False
        goto(ExecutionFlow.Pop())
        # Label 2828
        self.StartRecording()
        goto(ExecutionFlow.Pop())
        # Label 2843
        self.StopRecording()
        goto(ExecutionFlow.Pop())
        # Label 2858
        ReturnValue_18: bool = self.GetIsInAir()
        ReturnValue_19: float = Conv_BoolToFloat(ReturnValue_18)
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_Vehicle_IsFlying", ReturnValue_19, 0, self)
        self.UpdateEngineLoadSound(dt)
        self.UpdateAccelerationSound()
        if not self.mIsUsingNewAudioGears:
           goto(ExecutionFlow.Pop())
        self.UpdateAudioGear()
        goto(ExecutionFlow.Pop())
        # Label 3037
        self.UpdateThrottleState()
        self.TickVehicleSound(DeltaSeconds)
        self.TickRecording(DeltaSeconds)
        self.TickSimulationMovement()
        goto('L1590')
        # Label 3116
        if not self.mIsRecording:
            goto('L2828')
        goto('L2843')
        # Label 3135
        ReturnValue_20: float = MapRangeUnclamped(self.mEngineLoadTimer, 0, self.mEngineLoadTimerMax, 0, 11)
        Default__AkGameplayStatics.SetActorRTPCValue(self.mEngineLoadRTPCName, ReturnValue_20, 0, self)
        goto('L2858')
        goto('L3116')
        # Label 3262
        ReturnValue_21: bool = self.IsLocallyControlled()
        ReturnValue_22: bool = self.mIsFreeCamera and ReturnValue_21
        if not ReturnValue_22:
            goto('L3820')
        ReturnValue_23: float = self.GetInputAxisValue("Turn")
        ReturnValue1_6: float = self.GetInputAxisValue("LookUp")
        ReturnValue_24: float = ReturnValue1_6 * -1
        
        Roll1 = None
        Pitch1 = None
        Yaw1 = None
        BreakRotator(self.mSpringArmComponent.RelativeRotation, Ref[Roll1], Ref[Pitch1], Ref[Yaw1])
        ReturnValue_25: float = Yaw1 + ReturnValue_23
        ReturnValue1_7: float = ReturnValue_24 + Pitch1
        ReturnValue_26: float = ClampAngle(ReturnValue_25, -179, 179)
        ReturnValue1_8: float = ClampAngle(ReturnValue1_7, -89, 89)
        ReturnValue_27: Rotator = MakeRotator(0, ReturnValue1_8, ReturnValue_26)
        
        SweepHitResult = None
        self.mSpringArmComponent.K2_SetRelativeRotation(ReturnValue_27, False, False, Ref[SweepHitResult])
        goto(ExecutionFlow.Pop())
        # Label 3820
        ReturnValue3: bool = Default__KismetSystemLibrary.IsValid(self.mSpringArmComponent)
        if not ReturnValue3:
           goto(ExecutionFlow.Pop())
        
        SweepHitResult1 = None
        self.mSpringArmComponent.K2_SetRelativeRotation(self.mDefaultCameraRotation, False, False, Ref[SweepHitResult1])
        goto(ExecutionFlow.Pop())
        if not self.mIsMenuOpen:
            goto('L3262')
        goto(ExecutionFlow.Pop())
        self.WasDocked(atStation)
        ReturnValue_28: bool = self.HasAuthority()
        if not ReturnValue_28:
           goto(ExecutionFlow.Pop())
        goto('L102')
        ReturnValue7: bool = Default__KismetSystemLibrary.IsValid(self.mHonkSound)
        if not ReturnValue7:
           goto(ExecutionFlow.Pop())
        self.Server_Honk()
        goto(ExecutionFlow.Pop())
        self.mIsMenuOpen = menuOpen
        goto(ExecutionFlow.Pop())
        # Label 4099
        ReturnValue_29: Ptr[Controller] = self.GetController()
        Controller_0: Ptr[PlayerController] = Cast[PlayerController](ReturnValue_29)
        bSuccess2: bool = Controller_0
        ReturnValue_30: Ptr[Widget_RecordMenu] = Default__WidgetBlueprintLibrary.Create(self, Widget_RecordMenu, Controller_0)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_30, "mVehicle", self)
        self.mRecordMenu = ReturnValue_30
        ReturnValue1_9: Ptr[Controller] = self.GetController()
        Default__BPHUDHelpers.PushStackWidget(ReturnValue1_9, self.mRecordMenu, self)
        self.mIsMenuOpen = True
        self.ServerSetMenuOpen(True)
        goto(ExecutionFlow.Pop())
        self.StopRecording()
        self.RemoveOldTargets()
        goto(ExecutionFlow.Pop())
        self.WasUndocked()
        ReturnValue1_10: bool = self.HasAuthority()
        if not ReturnValue1_10:
           goto(ExecutionFlow.Pop())
        goto('L124')
        self.TogglePauseRecording()
        goto(ExecutionFlow.Pop())
        self.ToggleAutoPilot()
        goto(ExecutionFlow.Pop())
        self.TogglePathVisibility()
        goto(ExecutionFlow.Pop())
        # Label 4540
        if not self.mIsMenuOpen:
           goto(ExecutionFlow.Pop())
        ReturnValue4: bool = Default__KismetSystemLibrary.IsValid(self.mRecordMenu)
        if not ReturnValue4:
           goto(ExecutionFlow.Pop())
        ReturnValue2_3: Ptr[Controller] = self.GetController()
        Default__BPHUDHelpers.PopStackWidget(ReturnValue2_3, self.mRecordMenu, self)
        self.mRecordMenu = None
        goto(ExecutionFlow.Pop())
        Variable_0: Key = Key1
        ReturnValue5_0: Ptr[Controller] = self.GetController()
        Controller3: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue5_0)
        bSuccess4: bool = Controller3
        ReturnValue1_11: DisabledInputGate = Controller3.GetDisabledInputGate()
        ReturnValue3_0: bool = Not_PreBool(ReturnValue1_11.mVehicleRecording)
        if not ReturnValue3_0:
           goto(ExecutionFlow.Pop())
        goto('L4099')
        ReturnValue_31: bool = self.DriverLeave(self.mIsAutoPilotEnabled)
        ReturnValue1_12: bool = ReturnValue_31 and self.mIsAutoPilotEnabled
        if not ReturnValue1_12:
           goto(ExecutionFlow.Pop())
        ReturnValue_32: bool = self.SelfDriverEnter(None)
        goto(ExecutionFlow.Pop())
        # Label 5020
        self.Server_Leave()
        goto(ExecutionFlow.Pop())
        ReturnValue3_1: bool = self.GetIsSignificant()
        if not ReturnValue3_1:
           goto(ExecutionFlow.Pop())
        ReturnValue_33: Ptr[PhysicalMaterial] = self.GetCachedSurfaceMaterial()
        ReturnValue5_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_33)
        ReturnValue_34: float = self.mSetMaxClampRangeSpeed - self.mAudioPeakFlutter
        ReturnValue_35: bool = Not_PreBool(ReturnValue5_1)
        ReturnValue1_13: float = Conv_IntToFloat(self.mSpeedInKMH)
        ReturnValue_36: bool = ReturnValue1_13 > self.mThresholdForAudioFlutterKMH
        ReturnValue2_4: float = Conv_IntToFloat(self.mSpeedInKMH)
        ReturnValue_37: float = self.mSetMaxClampSpeed / 2
        ReturnValue3_2: float = Conv_IntToFloat(self.mSpeedInKMH)
        ReturnValue3_3: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue1_14: float = Abs(ReturnValue3_2)
        ReturnValue_38: float = ReturnValue3_3.GetEngineRotationSpeed()
        ReturnValue1_15: float = ReturnValue1_14 / 2
        ReturnValue_39: float = MapRangeClamped(ReturnValue_38, 0, 5700, 0, ReturnValue_37)
        ReturnValue2_5: float = ReturnValue_39 + ReturnValue1_15
        Variable_1: bool = self.mIsUsingGolfCartRPM
        Variable2: bool = ReturnValue_36
        ReturnValue4_0: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue1_16: float = ReturnValue4_0.GetEngineRotationSpeed()
        Variable1: bool = self.mIsUsingNewAudioVehicleRPM
        Variable3: bool = ReturnValue_35
        
        switch_0 = {
            False: self.mSetMaxClampRangeSpeed,
            True: ReturnValue_34
        }
        
        switch_1 = {
            False: switch_0.get(Variable2, None),
            True: self.mSetMaxClampRangeAirSpeed
        }
        ReturnValue1_17: float = MapRangeClamped(ReturnValue2_5, 0, self.mSetMaxClampSpeed, 0, switch_1.get(Variable3, None))
        
        switch_2 = {
            False: ReturnValue2_4,
            True: ReturnValue1_17
        }
        
        switch_3 = {
            False: switch_2.get(Variable_1, None),
            True: ReturnValue1_16
        }
        Default__AkGameplayStatics.SetActorRTPCValue(self.mVehicleSpeedRTPC, switch_3.get(Variable1, None), 0, self)
        goto('L3135')
        self.ReceiveOnVehicleStartup()
        self.StartSoundLoops()
        goto(ExecutionFlow.Pop())
        self.ReceiveOnVehicleShutDown()
        self.StopSoundLoops()
        goto(ExecutionFlow.Pop())
        Variable_0 = Key2
        ReturnValue5_0 = self.GetController()
        Controller3 = Cast[FGPlayerController](ReturnValue5_0)
        bSuccess4 = Controller3
        ReturnValue1_11 = Controller3.GetDisabledInputGate()
        ReturnValue3_0 = Not_PreBool(ReturnValue1_11.mVehicleRecording)
        if not ReturnValue3_0:
           goto(ExecutionFlow.Pop())
        goto('L4540')
        self.ReceiveTick(DeltaSeconds)
        goto('L3037')
        goto('L2187')
        goto(ExecutionFlow.Pop())
        self.ReceiveOnDriverEnter()
        goto(ExecutionFlow.Pop())
        self.ReceiveOnDriverLeave()
        goto(ExecutionFlow.Pop())
        Variable1_0: Key = Key3
        self.SetIsDrifting(True)
        goto(ExecutionFlow.Pop())
        Variable1_0 = Key4
        self.SetIsDrifting(False)
        goto(ExecutionFlow.Pop())
        # Label 6501
        ReturnValue6: bool = Default__KismetSystemLibrary.IsValid(self.mRecordMenu)
        if not ReturnValue6:
            goto('L5020')
        ReturnValue3_4: Ptr[Controller] = self.GetController()
        Default__BPHUDHelpers.PopStackWidget(ReturnValue3_4, self.mRecordMenu, self)
        self.mRecordMenu = None
        goto('L5020')
        ReturnValue6_0: Ptr[Controller] = self.GetController()
        Controller4: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue6_0)
        bSuccess5: bool = Controller4
        ReturnValue8: bool = Default__KismetSystemLibrary.IsValid(Controller4)
        if not ReturnValue8:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L6922")
        self.SetAddedAngularVelocityPitch(AxisValue1)
        ReturnValue11: bool = Default__KismetSystemLibrary.IsValid(self.mPlayBurnOutSound)
        if not ReturnValue11:
           goto(ExecutionFlow.Pop())
        if not self.mShouldUseAudioBurnout:
           goto(ExecutionFlow.Pop())
        self.BurnOutSound(AxisValue1)
        goto(ExecutionFlow.Pop())
        # Label 6922
        ReturnValue_40: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        
        adjustedThrottle = None
        self.AdjustThrottle(AxisValue1, Ref[adjustedThrottle])
        ReturnValue_40.SetThrottleInput(adjustedThrottle)
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L7041")
        self.SetAddedAngularVelocityYaw(AxisValue)
        goto(ExecutionFlow.Pop())
        # Label 7041
        ReturnValue1_18: Ptr[WheeledVehicleMovementComponent] = self.GetVehicleMovementComponent()
        ReturnValue1_18.SetSteeringInput(AxisValue)
        goto(ExecutionFlow.Pop())
        goto('L2423')
        self.Multicast_Honk()
        goto(ExecutionFlow.Pop())
        ReturnValue2_6: bool = self.GetIsSignificant()
        if not ReturnValue2_6:
           goto(ExecutionFlow.Pop())
        if not self.mCarShouldNotHonk:
            goto('L7168')
        goto(ExecutionFlow.Pop())
        # Label 7168
        ReturnValue1_19: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(self.mHonkSound, self, True)
        goto(ExecutionFlow.Pop())
        # Label 7222
        ReturnValue4_1: Ptr[Controller] = self.GetController()
        Controller2: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue4_1)
        bSuccess3: bool = Controller2
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        ReturnValue_41: DisabledInputGate = Controller2.GetDisabledInputGate()
        ReturnValue2_7: bool = Not_PreBool(ReturnValue_41.mUse)
        if not ReturnValue2_7:
           goto(ExecutionFlow.Pop())
        goto('L6501')
        # Label 7420
        ReturnValue1_20: bool = self.GetIsSignificant()
        if not ReturnValue1_20:
           goto(ExecutionFlow.Pop())
        ReturnValue10: bool = Default__KismetSystemLibrary.IsValid(destroyEffect)
        if not ReturnValue10:
            goto('L7605')
        ReturnValue_42: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, destroyEffect, location, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        # Label 7605
        ReturnValue9: bool = Default__KismetSystemLibrary.IsValid(destroyAudioEvent)
        if not ReturnValue9:
           goto(ExecutionFlow.Pop())
        ReturnValue_43: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, destroyAudioEvent, location, Rotator::FromPitchYawRoll(0, 0, 0))
        goto(ExecutionFlow.Pop())
        goto('L7420')
        goto('L770')
        goto('L804')
        goto('L7222')
    

    def OnStartRecording__DelegateSignature(self):
        pass
    

    def OnStopRecording__DelegateSignature(self):
        pass
    

    def LocationReached__DelegateSignature(self):
        pass
    
