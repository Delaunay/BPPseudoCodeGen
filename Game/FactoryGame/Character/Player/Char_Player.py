
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.Anim_3p import Anim_3p
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player
from Script.Engine import Conv_StringToName
from Game.FactoryGame.Character.Player.Anim_1p import Anim_1p
from Script.Engine import Texture2D
from Script.Engine import FinishSpawningActor
from Script.Engine import ReceiveDestroyed
from Script.FactoryGame import FGCharacterPlayer
from Script.AkAudio import PostAkEventAtLocation
from Script.Engine import GetTransform
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.FlashLight.Play_FlashLight_On import Play_FlashLight_On
from Script.CoreUObject import Rotator
from Script.Engine import Conv_ByteToInt
from Script.InputCore import Key
from Script.Engine import AddOrUpdateBlendable
from Game.FactoryGame.Character.Player.Widget_PlayerInventory import Widget_PlayerInventory
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.DamageTypes.Stop_C_Damage_Radiation import Stop_C_Damage_Radiation
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.Slide.Play_P_StartSlide import Play_P_StartSlide
from Script.Engine import Ease
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import EqualEqual_FloatFloat
from Script.FactoryGame import FGDamageType
from Script.Engine import VInterpTo
from Script.Engine import K2_TeleportTo
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_InputActionEvent_Key2
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_Event_boostJump
from Script.Engine import DecalComponent
from Script.FactoryGame import GetPipeHyperDataRef
from Script.FactoryGame import FGCameraModifierLimitLook
from Script.FactoryGame import GetDisabledInputGate
from Script.Engine import EPhysicalSurface
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Audio.Play_FastJunctionsTube import Play_FastJunctionsTube
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.Engine import BlendableInterface
from Script.Engine import GetValidValue
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.Slide.Play_P_SlideSpeedwind import Play_P_SlideSpeedwind
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_Event_OldController
from Game.FactoryGame.VFX.Character.Player.Anim.P_PlayerSliding_Gravel import P_PlayerSliding_Gravel
from Script.Engine import Conv_StringToText
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_CustomEvent_damageType
from Script.Engine import FMax
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_InputActionEvent_Key3
from Script.FactoryGame import StopFreeRotate3P
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_InputActionEvent_Key4
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.DamageTypes.Play_C_Damage_Radiation import Play_C_Damage_Radiation
from Script.Engine import FlushNetDormancy
from Script.FactoryGame import GetSpringArmComponent
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.Play_P_Suit_Damage_Warning_Flatline import Play_P_Suit_Damage_Warning_Flatline
from Game.FactoryGame.VFX.Character.Player.Anim.P_PlayerSliding_Grass import P_PlayerSliding_Grass
from Script.Engine import Normal
from Script.Engine import ReceiveUnpossessed
from Game.FactoryGame.Character.Player.Animation.FirstPerson.Clap_01_Montage import Clap_01_Montage
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_Event_byCharacter1
from Script.FactoryGame import StopFocusAim
from Script.Engine import GetSurfaceType
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import ECameraMode
from Script.Engine import Montage_Play
from Script.FactoryGame import StartFocusAim
from Script.Engine import CreateDynamicMaterialInstance
from Script.FactoryGame import GetCurrentHealth
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_Event_state1
from Script.UMG import UserWidget
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_InputActionEvent_Key6
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.-Shared.Blueprint.BP_DamageType import BP_DamageType
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_Event_NewMovementMode
from Script.Engine import CameraModifier
from Script.AkAudio import SetGlobalRTPCValue
from Script.FactoryGame import FGBuildGun
from Script.UMG import Create
from Game.FactoryGame.Character.Player.Animation.FirstPerson.Pickup_01_Montage import Pickup_01_Montage
from Script.Engine import MakeRotFromX
from Script.Engine import MapRangeClamped
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_CustomEvent_instigatedBy
from Game.FactoryGame.Equipment.BuildGun.Mesh.BuildGun_Skl_01 import BuildGun_Skl_01
from Script.Engine import GetActorRightVector
from Script.Engine import Montage_IsPlaying
from Script.FactoryGame import ReceiveDied
from Script.FactoryGame import CameraZoomIn
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import K2_SetRelativeRotation
from Script.Engine import GetActorForwardVector
from Script.CoreUObject import LinearColor
from Game.FactoryGame.Character.Player.CM_Slide import CM_Slide
from Script.FactoryGame import FGHealthComponent
from Script.Engine import GetPlayerCameraManager
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_Event_NewCustomMode
from Script.Engine import GetPlayerName
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_Event_Hit
from Script.Engine import SetXScale
from Script.FactoryGame import SetFirstPersonMode
from Script.Engine import SetVisibility
from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import GetPumpiMode
from Script.Engine import Controller
from Script.Engine import FClamp
from Script.AkAudio import SetActorRTPCValue
from Script.Engine import EqualEqual_ByteByte
from Game.FactoryGame.Equipment.BuildGun.Animation.BuildgunSpinEmote_01_Montage import BuildgunSpinEmote_01_Montage
from Script.Engine import Pawn
from Script.FactoryGame import StartIsLookedAt
from Script.FactoryGame import StopIsLookedAt
from Script.Engine import VSize
from Script.FactoryGame import SetThirdPersonMode
from Script.Engine import MaterialInstanceDynamic
from Script.Engine import FMin
from Script.Engine import Default__KismetNodeHelperLibrary
from Script.Engine import HUD
from Script.Engine import RotateAngleAxis
from Script.Engine import SelectFloat
from Game.FactoryGame.Interface.UI.Material.Material_RadiationNoise import Material_RadiationNoise
from Script.FactoryGame import GetCameraComponent
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Audio.Play_EnterTube import Play_EnterTube
from Script.Engine import StaticMeshComponent
from Script.FactoryGame import DisabledInputGate
from Script.CoreUObject import Object
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_Event_NewController
from Script.Engine import GetHUD
from Script.Engine import GetRealTimeSeconds
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_CustomEvent_AudioTick
from Script.FactoryGame import GetCameraMode
from Script.FactoryGame import GetMesh1P
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_CustomEvent_damageAmount
from Script.FactoryGame import ECustomMovementMode
from Script.Engine import MakeNoise
from Script.Engine import Default__KismetMaterialLibrary
from Script.Engine import Conv_VectorToRotator
from Script.FactoryGame import FGActorRepresentationManager
from Script.Engine import K2_GetComponentLocation
from Game.FactoryGame.Character.Player.Animation.FirstPerson.BuildgunSpinEmote_01_Montage import BuildgunSpinEmote_01_Montage
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.Pickup_02_Montage import Pickup_02_Montage
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import NotEqual_ByteByte
from Game.FactoryGame.VFX.Character.Player.MI.MI_SlideDecal_Sand import MI_SlideDecal_Sand
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.BuildgunSpinEmote_01_Montage import BuildgunSpinEmote_01_Montage
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.Pickup_01_Montage import Pickup_01_Montage
from Script.FactoryGame import CameraZoomOut
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.Slide.Stop_P_SlideSpeedWind import Stop_P_SlideSpeedWind
from Game.FactoryGame.PostProcess.BloodFX.deathBloodFX import deathBloodFX
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_CustomEvent_inController
from Script.Engine import K2_AttachToComponent
from Script.Engine import Abs
from Game.FactoryGame.Character.Player.CameraShake.EmoteSignCameraANim import EmoteSignCameraANim
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Audio.Play_TurbineWindTube import Play_TurbineWindTube
from Script.AkAudio import AkComponent
from Script.Engine import SkeletalMeshComponent
from Script.Engine import BreakHitResult
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_Event_newValue
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGCharacterMovementComponent
from Script.Engine import PlayerCameraManager
from Script.Engine import Delay
from Script.Engine import ReceivePossessed
from Script.FactoryGame import CreateAndAddNewRepresentation
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.Character.Player.Animation.FirstPerson.Pickup_02_Montage import Pickup_02_Montage
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_Event_PrevCustomMode
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Audio.Play_AmbienceTube_Client import Play_AmbienceTube_Client
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_CustomEvent_doLimit
from Game.FactoryGame.Interface.UI.BP_InteractablesMarker import BP_InteractablesMarker
from Script.FactoryGame import FGPlayerState
from Script.Engine import SpawnEmitterAttached
from Script.Engine import K2_SetText
from Script.LevelSequence import LevelSequence
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_CustomEvent_FlashlightOn
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_Event_radiationImmunity
from Script.FactoryGame import SetMeshVisibility
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Character.Player.CM_RestrictedLook import CM_RestrictedLook
from Script.Engine import HasAuthority
from Script.AkAudio import SetSwitch
from Script.FactoryGame import Get
from Script.Engine import PlayerController
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.SpeedWind.Play_Player_SpeedWind import Play_Player_SpeedWind
from Script.Engine import GetController
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_CustomEvent_EmoteIndex
from Script.Engine import SetScalarParameterValueOnMaterials
from Script.FactoryGame import SetDefaultLookRotator
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_Icon_player import MapCompass_Icon_player
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import EqualEqual_NameName
from Script.Engine import OnLanded
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import ToggleBuildGun
from Script.Engine import BreakRotator
from Script.FactoryGame import AddPawnHUD
from Script.FactoryGame import GetGameUI
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.Slide.Play_P_JumpSlide import Play_P_JumpSlide
from Script.Engine import Subtract_VectorVector
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_CustomEvent_damagedActor
from Script.Engine import K2_GetActorRotation
from Script.FactoryGame import FGGameUI
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_InputActionEvent_Key
from Script.Engine import MakeRotator
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.Slide.Play_P_LoopSlide import Play_P_LoopSlide
from Script.Engine import SetTextRenderColor
from Game.FactoryGame.Character.Player.BP_DeathMarker import BP_DeathMarker
from Script.Engine import K2_DestroyComponent
from Script.FactoryGame import PlayerPipeHyperData
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.Engine import NearlyEqual_FloatFloat
from Script.Engine import RandomIntegerInRange
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_Event_PrevMovementMode
from Game.FactoryGame.Interface.UI.InGame.Codex.Widget_Codex_Container import Widget_Codex_Container
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Audio.Stop_AllSoundsInsideTube import Stop_AllSoundsInsideTube
from Game.FactoryGame.Character.Player.Animation.FirstPerson.Pickup_Montage import Pickup_Montage
from Script.FactoryGame import RemoveRepresentationOfActor
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_Event_state
from Script.FactoryGame import PlayPickupEffects
from Script.Engine import K2_SetWorldRotation
from Script.FactoryGame import OnDisabledInputGateChanged
from Script.Engine import SpawnDecalAtLocation
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.FlashLight.Play_FlashLight_Off import Play_FlashLight_Off
from Script.FactoryGame import IsAliveAndWell
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.Play_P_Suit_Damage_Warning import Play_P_Suit_Damage_Warning
from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.FactoryGame import GetHealthComponent
from Game.FactoryGame.VFX.Character.Player.Anim.P_PlayerSliding_Sand import P_PlayerSliding_Sand
from Script.Engine import SpringArmComponent
from Script.Engine import SetScalarParameterValue
from Script.FactoryGame import GetDefaultLookRotator
from Script.FactoryGame import ShowOutline
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Audio.Play_AmbienceTube import Play_AmbienceTube
from Script.FactoryGame import SetPartialPumpiMode
from Script.Engine import SetFadeOut
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.SpeedWind.Stop_Player_SpeedWind import Stop_Player_SpeedWind
from Game.FactoryGame.Interface.UI.InGame.Widget_EmoteMenu import Widget_EmoteMenu
from Script.Engine import MapRangeUnclamped
from Script.Engine import AddComponent
from Script.FactoryGame import IsEquipped
from Game.FactoryGame.Character.Player.Audio.SB_CharacterEssentials.Slide.Stop_P_Slide import Stop_P_Slide
from Script.FactoryGame import IsDead
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_Event_radiationIntensity
from Script.Engine import GetInstigator
from Script.Engine import K2_SetTimer
from Script.Engine import ReceiveBeginPlay
from Script.FactoryGame import SetDisabledInputGate
from Script.Engine import Not_PreBool
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_Event_byCharacter
from Game.FactoryGame.Equipment.BuildGun.Anim_BuildGun import Anim_BuildGun
from Script.Engine import SetYScale
from Script.FactoryGame import StartFreeRotate3P
from Script.Engine import GetAnimInstance
from Script.CoreUObject import Color
from Game.FactoryGame.VFX.Character.Player.Anim.P_PlayerSliding_Moist import P_PlayerSliding_Moist
from Script.Engine import Montage_JumpToSection
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_Event_newColor
from Script.Engine import GreaterEqual_FloatFloat
from Script.FactoryGame import Default__FGActorRepresentationManager
from Game.FactoryGame.-Shared.Blueprint.BP_HUD import BP_HUD
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_Icon_playerdead import MapCompass_Icon_playerdead
from Script.Engine import BeginDeferredActorSpawnFromClass
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.EmoteSigns_01_Montage import EmoteSigns_01_Montage
from Game.FactoryGame.Character.Player.Animation.FirstPerson.EmoteSigns_01_Montage import EmoteSigns_01_Montage
from Script.FactoryGame import HideOutline
from Script.Engine import Conv_LinearColorToColor
from Script.FactoryGame import GetNametagColor
from Script.Engine import FInterpTo
from Script.FactoryGame import UpdateRepresentation
from Game.FactoryGame.Interface.UI.HUDHelpers.BPFL_HudHelperBadRef import Default__BPFL_HudHelperBadRef
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_Event_dt
from Script.Engine import GetPlayerController
from Script.Engine import BooleanOR
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_InputActionEvent_Key5
from Game.FactoryGame.VFX.Character.Player.Anim.P_PlayerSliding_Rock import P_PlayerSliding_Rock
from Script.Engine import GetSocketBoneName
from Script.CoreUObject import Vector
from Script.FactoryGame import GetBuildGun
from Script.Engine import EqualExactly_VectorVector
from Script.FactoryGame import FGHUD
from Script.FactoryGame import GetIsSprinting
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_InputActionEvent_Key1
from Script.Engine import ParticleSystemComponent
from Game.FactoryGame.Character.Player.Char_Player import ExecuteUbergraph_Char_Player.K2Node_CustomEvent_damageCauser
from Script.Engine import K2_GetActorLocation
from Script.FactoryGame import OccludeOutlineByComponent
from Script.Engine import Actor
from Script.Engine import Montage_GetCurrentSection
from Script.FactoryGame import GetMaxHealth
from Script.Engine import AnimInstance
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Audio.Play_ExitTube import Play_ExitTube
from Script.Engine import IsValidClass
from Script.CoreUObject import Transform
from Script.Engine import SetOwnerNoSee
from Script.FactoryGame import EFogOfWarRevealType
from Script.Engine import CameraComponent
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Audio.Play_HitTube import Play_HitTube
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.Clap_01_Montage import Clap_01_Montage

class Char_Player(FGCharacterPlayer):
    EventScrollDown: FMulticastScriptDelegate
    EventScroll: FMulticastScriptDelegate
    EventScrollUp: FMulticastScriptDelegate
    EventFire: FMulticastScriptDelegate
    mDeltaTime: float
    mDesiredDamageIndicator: float
    mDamageIndicatorSpeed: float = 5
    mLowHealthIndicatorPower: float
    mCurrentDamageIndicator: float
    mMaxDamageIndicator: float = 2
    mLastDamageTime: float = -1
    mTargetCameraDistance: float = 300
    mSavedCameraDistance: float = 150
    mCameraDistanceMin: float = 130
    mCameraDistanceMax: float = 500
    mTransitionDelay: float = 0.4000000059604645
    mTargetCameraOffset: Vector
    mCameraOffset3P: Vector = Namespace(X=0, Y=40, Z=0)
    mDistanceInterpolationSpeed: float = 5
    mTargetCameraFOV: float = 90
    mSavedCameraFOV: float
    mIsFocusing: bool
    mMuteOnOff: bool
    mCameraDistanceDefault3P: float = 300
    mCameraDistanceFocus3P: float = 130
    mFocusInterpolationSpeed: float = 20
    mDefaultCameraInterpolationSpeed: float = 5
    mDefaultFOV: float = 90
    mFocusFOV: float = 60
    mCameraDistanceMin3P: float = 130
    mCameraDistanceMax3P: float = 400
    mSprintNoiseInterval: float = 0.30000001192092896
    mTimeSprinting: float = -1
    mPickupMontageSectionName: FName
    mPickupMontageSectionName3p: FName
    mReviveWidget: Ptr[Object]
    mPlayerHUDClass: TSubclassOf[UserWidget] = NewObject[Widget_PlayerHUD]()
    mFlashlightOn: bool
    mWaitingForPlayerState: bool
    mSequences: List[Ptr[LevelSequence]] = [{'$AssetPath': '/Game/FactoryGame/Cinematics/TestSequence/Master.Master'}]
    mInteractableMarker: Ptr[BP_InteractablesMarker]
    mMineSection: FName
    mLookModifier: Ptr[FGCameraModifierLimitLook]
    mLandingInputGate: DisabledInputGate = Namespace(mBuildGun=True, mChat=False, mDismantle=True, mFlashLight=True, mHotbar=True, mInventory=True, mJump=False, mOpenCodex=True, mResourceScanner=True, mToggleMap=True, mUse=False, mVehicleRecording=False)
    mEmoteBuildgun: Ptr[SkeletalMeshComponent]
    mEmoteTimer: TimerHandle
    mEmoteMenu: Ptr[Widget_EmoteMenu]
    mPossessed: bool
    mMapText: FText
    mRadiationNoise: Ptr[MaterialInstanceDynamic]
    mWarningPopupTimer: TimerHandle
    mPlaytimeWarningMessages: List[FText] = ['NSLOCTEXT("", "CBF46C354F9A8198F1BC3A8997AAC65E", "FICSIT Inc. recognizes that efficiency increases when frequent breaks are taken.")', 'NSLOCTEXT("", "146655354780F331610DEEB007D468E4", "FICSIT Inc. recommends stretching frequently. Optimally done outside and vertically.")', 'NSLOCTEXT("", "143371CC488AE5DEB9D7B6AF4803340F", "Please ensure your daily dose of fresh air is met.")', 'NSLOCTEXT("", "77DA17CF49BBD80ADB81CE89738EB0D9", "FICSIT Inc. would like to remind you that self-care matters. No-one else will do it for you!")', 'NSLOCTEXT("", "B474214E447996EA821230A7BFA6324E", "FICSIT Inc. urges you to drink some -insert beverage here-.")', 'NSLOCTEXT("", "8ED8BF0D449699644601F786CCCEE9C9", "Caution: you are approaching critical levels of -insert furniture here-potato.")', 'NSLOCTEXT("", "5BEA575244F64383AE478BBED9BB3420", "FICSIT Inc. would like to remind you all muscles exist to be used.")', 'NSLOCTEXT("", "E8C5BFF8422BAF2517EDA2A92325AE54", "FICSIT Inc. recommends its newest outside entertainment: Lizard Dog Go.")']
    mPlaytimeWarningMessageIndex: int32
    mSlideCameraModifier: Ptr[CM_Slide]
    mClearSlideVelocityTimer: TimerHandle
    mHypertube_VfxCap: Ptr[StaticMeshComponent]
    Hypertube_Vfx_Particle_02: Ptr[ParticleSystemComponent]
    Hypertube_Vfx_Particle_01: Ptr[ParticleSystemComponent]
    mClearSlideSpeedWindTimer: TimerHandle
    mCurrentSpeedWindTimer: float
    mLastSlideSurfaceType: int32
    mCurrentSlidingSurfaceType: FName
    mClearTubeTravelUpdateTimer: TimerHandle
    mLastFrameForwardDirection: Vector
    mLastFrameDirectionDegrees: float
    mClearSlideVFXTimer: TimerHandle
    Sliding_Particle: Ptr[ParticleSystemComponent]
    mCurrentWindSpeed: float
    mVFX_Capsule_Opacity: float
    mFGCharacterMovementCompRef: Ptr[FGCharacterMovementComponent]
    mSwitchingPipes: float
    mLastFrameEndPosTube: Vector
    mLastFrameEndRotTube: Rotator
    mSFXFastJUnction: Ptr[AkComponent]
    mPlaySpeedWind: bool
    mBaseTurnRate = 45
    mBaseLookUpRate = 45
    mMesh1PAnimClass = NewObject[Anim_1p]()
    mMesh3P = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 96, 'CapsuleRadius': 40, 'bReturnMaterialOnMove': True, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 238.15028381347656, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, BodyInstance={'ObjectType': 2, 'CollisionEnabled': 1, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'CharacterMesh', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Pawn', 'Response': 0}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Vehicle', 'Response': 0}, {'Channel': 'WeaponInstantHit', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=1, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='CharacterMesh3P', RelativeLocation={'X': 0, 'Y': 0, 'Z': -96.21900177001953}, RelativeRotation={'Pitch': 0, 'Yaw': -90, 'Roll': 0}, SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Character/Player/Mesh/Character.Character'}, bAutoActivate=False, bCastCapsuleDirectShadow=True, bEnableUpdateRateOptimizations=False, bReceivesDecals=False)
    mFoliagePickupProxyClass = NewObject[BP_FoilagePickup]()
    mAnimInstanceClass = NewObject[Anim_3p]()
    mAnimInstanceClass1P = NewObject[Anim_1p]()
    mReviveDuration = 5
    mStartingResources = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/ShockShank/BP_EquipmentDescriptorShockShank.BP_EquipmentDescriptorShockShank_C', 'amount': 1}]
    mStartingResourceForTesting = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/Rifle/BP_EquipmentDescriptorRifle.BP_EquipmentDescriptorRifle_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CartridgeStandard/Desc_CartridgeStandard.Desc_CartridgeStandard_C', 'amount': 60}, {'ItemClass': '/Game/FactoryGame/Resource/Equipment/JetPack/BP_EquipmentDescriptorJetPack.BP_EquipmentDescriptorJetPack_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Fuel/Desc_Fuel.Desc_Fuel_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Equipment/Chainsaw/Desc_Chainsaw.Desc_Chainsaw_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/BioFuel/Desc_Biofuel.Desc_Biofuel_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Equipment/NailGun/Desc_RebarGunProjectile.Desc_RebarGunProjectile_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SpikedRebar/Desc_SpikedRebar.Desc_SpikedRebar_C', 'amount': 20}, {'ItemClass': '/Game/FactoryGame/Resource/Equipment/JumpingStilts/BP_EquipmentDescriptorJumpingStilts.BP_EquipmentDescriptorJumpingStilts_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Equipment/StunSpear/BP_EquipmentDescriptorStunSpear.BP_EquipmentDescriptorStunSpear_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Equipment/HazmatSuit/BP_EquipmentDescriptorHazmatSuit.BP_EquipmentDescriptorHazmatSuit_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IodineInfusedFilter/Desc_HazmatFilter.Desc_HazmatFilter_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Equipment/GolfCart/Desc_GolfCart.Desc_GolfCart_C', 'amount': 1}]
    mDrownDamageDamageType = NewObject[DamageType_DrownDamage]()
    mDrownDamage = 10
    mDrownDamageInterval = 0.5
    m1PFootstepEffect = [{'Surface': 0, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 1, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': [{'$AssetPath': '/Game/FactoryGame/VFX/Character/Player/MI/MI_Sand_L_Foot.MI_Sand_L_Foot'}, {'$AssetPath': '/Game/FactoryGame/VFX/Character/Player/MI/MI_Sand_R_Foot.MI_Sand_R_Foot'}]}}, {'Surface': 2, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 3, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 4, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 5, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': [{'$AssetPath': '/Game/FactoryGame/VFX/Character/Player/MI/MI_Mud_L_Foot.MI_Mud_L_Foot'}, {'$AssetPath': '/Game/FactoryGame/VFX/Character/Player/MI/MI_Mud_R_Foot.MI_Mud_R_Foot'}]}}, {'Surface': 6, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 7, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 8, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 9, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 10, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': [{'$AssetPath': '/Game/FactoryGame/VFX/Character/Player/MI/MI_Soil_L_Foot.MI_Soil_L_Foot'}, {'$AssetPath': '/Game/FactoryGame/VFX/Character/Player/MI/MI_Soil_R_Foot.MI_Soil_R_Foot'}]}}, {'Surface': 11, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 14, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}]
    m1PFootstepEvent = [{'$AssetPath': '/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/FootStep_Rework/Play_FootStep_SwitchEvent.Play_FootStep_SwitchEvent'}, {'$AssetPath': '/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/FootStep_Rework/Play_FootStep_SwitchEvent.Play_FootStep_SwitchEvent'}]
    mCameraComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SpringArmComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CameraSpringArm', 'TargetArmLength': 0, 'bUsePawnControlRotation': True, 'bInheritRoll': False, 'CameraLagMaxDistance': 100, 'AttachParent': {'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 96, 'CapsuleRadius': 40, 'bReturnMaterialOnMove': True, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 238.15028381347656, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, 'RelativeLocation': {'X': 29, 'Y': 0, 'Z': 64}}, ObjectClass='/Script/Engine.CameraComponent', ObjectFlags=2883617, ObjectName=' PlayerCamera ', bUsePawnControlRotation=True)
    mSpringArmComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 96, 'CapsuleRadius': 40, 'bReturnMaterialOnMove': True, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 238.15028381347656, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, CameraLagMaxDistance=100, ObjectClass='/Script/Engine.SpringArmComponent', ObjectFlags=2883617, ObjectName='CameraSpringArm', RelativeLocation={'X': 29, 'Y': 0, 'Z': 64}, TargetArmLength=0, bInheritRoll=False, bUsePawnControlRotation=True)
    mPlayerPreferredCameraMode = ECameraMode::ECM_FirstPerson
    mAllowedResourceFormsInInventory = ['EResourceForm::RF_SOLID']
    mAllowCameraToggling = True
    mUseDistance = 450
    mDefaultWalkHeadBobShake = NewObject[WalkShake]()
    mDefaultSprintHeadBobShake = NewObject[RunShake]()
    mOutlineComponent = Namespace(ObjectClass='/Script/FactoryGame.FGOutlineComponent', ObjectFlags=2883617, ObjectIndex=1, ObjectName='OutlineComponent', mOutlineProxy={'$ObjectClass': '/Script/Engine.StaticMeshComponent', '$ObjectFlags': 2883617, '$ObjectName': 'OutlineProxy', 'bRenderInMainPass': False, 'CastShadow': False, 'BodyInstance': {'ObjectType': 1, 'CollisionEnabled': 0, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'VehicleWheelQuery', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'AttachParent': {'$ObjectRef': 1}, 'bVisible': False, 'bCanEverAffectNavigation': False})
    mHealthGenerationThreshold = 0.30000001192092896
    mHealthGenerationAmount = 1
    mHealthGenerationInterval = 0.5
    mHealthGenerationWaitTime = 3
    mCameraOffsetBlendSpeed = 3
    mCrouchSpeed = 4
    mStandSpeed = 4
    mSlideToCrouchSpeed = 3
    mFeetNames = ['foot_l', 'foot_r']
    mFootstepEffect = [{'Surface': 0, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 1, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': [{'$AssetPath': '/Game/FactoryGame/VFX/Character/Player/MI/MI_Sand_L_Foot.MI_Sand_L_Foot'}, {'$AssetPath': '/Game/FactoryGame/VFX/Character/Player/MI/MI_Sand_R_Foot.MI_Sand_R_Foot'}]}}, {'Surface': 2, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 3, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 4, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 5, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': [{'$AssetPath': '/Game/FactoryGame/VFX/Character/Player/MI/MI_Mud_L_Foot.MI_Mud_L_Foot'}, {'$AssetPath': '/Game/FactoryGame/VFX/Character/Player/MI/MI_Mud_R_Foot.MI_Mud_R_Foot'}]}}, {'Surface': 6, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 7, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 8, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 9, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 10, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': [{'$AssetPath': '/Game/FactoryGame/VFX/Character/Player/MI/MI_Soil_L_Foot.MI_Soil_L_Foot'}, {'$AssetPath': '/Game/FactoryGame/VFX/Character/Player/MI/MI_Soil_R_Foot.MI_Soil_R_Foot'}]}}, {'Surface': 11, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}, {'Surface': 14, 'Effect': {'Particle': {'$Empty': True}, 'GroundDecals': []}}]
    mFootstepAudioEvents = [{'$AssetPath': '/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/FootStep_Rework/Play_FootStep_SwitchEvent.Play_FootStep_SwitchEvent'}, {'$AssetPath': '/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/FootStep_Rework/Play_FootStep_SwitchEvent.Play_FootStep_SwitchEvent'}]
    mMaxFootstepParticleSpawnDistance = 2500
    mMaxFootstepDecalSpawnDistance = 1250
    mFootstepDecalSize = [{'X': -20, 'Y': -20, 'Z': 20}, {'X': 20, 'Y': 20, 'Z': 20}]
    mFootstepDecalLifetime = 15
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True, mCurrentHealth=100, mMaxHealth=100, mOnAdjustDamage=[0], mReplicateDamageEvents=True, mReplicateDeathEvents=True, mRespawnHealthFactor=0.30000001192092896)
    mFallDamageCurve = Namespace(AssetPath='/Game/FactoryGame/Character/Player/FallDamageCurve.FallDamageCurve')
    mFallDamageDamageType = NewObject[DamageType_FallDamage]()
    mMaxDeathStayTime = 60
    mDeathRemoveCheckTime = 5
    mEnemyTargetDesirability = 1
    mLandEvent = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/FootStep_Rework/Play_FootStep_Land_SwitchEvent.Play_FootStep_Land_SwitchEvent')
    mMinVehiclePushVelocityForRagdoll = 400
    mTimeToGetUpFromRagdoll = 3
    mMaxDistanceMovedToGetUp = 9
    mRagdollMeshLocBoneName = Pelvis
    mRagdollMeshPhysicsBoneName = Pelvis
    mSyncBodyMaxDistance = 6
    mApplyDamageMomentum = True
    mWeakspotMultiplier = 2
    mNormalDamageMultiplier = 1
    Mesh = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.CapsuleComponent', '$ObjectFlags': 2883617, '$ObjectName': 'CollisionCylinder', 'CapsuleHalfHeight': 96, 'CapsuleRadius': 40, 'bReturnMaterialOnMove': True, 'BodyInstance': {'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 238.15028381347656, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, 'bShouldUpdatePhysicsVolume': True, 'bCanEverAffectNavigation': False}, BodyInstance={'ObjectType': 0, 'CollisionEnabled': 0, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'NoCollision', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WorldStatic', 'Response': 0}, {'Channel': 'WorldDynamic', 'Response': 0}, {'Channel': 'Pawn', 'Response': 0}, {'Channel': 'Visibility', 'Response': 0}, {'Channel': 'Camera', 'Response': 0}, {'Channel': 'PhysicsBody', 'Response': 0}, {'Channel': 'Vehicle', 'Response': 0}, {'Channel': 'Destructible', 'Response': 0}, {'Channel': 'Projectile', 'Response': 0}, {'Channel': 'Resource', 'Response': 0}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 191.20346069335938, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CanCharacterStepUpOn=0, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', CustomDepthStencilValue=1, CustomDepthStencilWriteMask='ERendererStencilMask::ERSM_255', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='CharacterMesh0', RelativeLocation={'X': 0, 'Y': 0, 'Z': -96.52799987792969}, RelativeRotation={'Pitch': 0, 'Yaw': -90, 'Roll': 0}, SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Character/Player/Mesh/1PCharacter.1PCharacter'}, VisibilityBasedAnimTickOption='EVisibilityBasedAnimTickOption::AlwaysTickPose', bCastCapsuleDirectShadow=True, bCastCapsuleIndirectShadow=True, bEnableUpdateRateOptimizations=False, bOnlyOwnerSee=True, bReceivesDecals=False, mFOV=90)
    CharacterMovement = Namespace(AirControl=0.15000000596046448, BrakingDecelerationSwimming=100, Buoyancy=1.350000023841858, CrouchedHalfHeight=64, GravityScale=1.2000000476837158, JumpZVelocity=500, MaxAcceleration=10000, MaxStepHeight=50, MaxWalkSpeed=500, MaxWalkSpeedCrouched=240, NavAgentProps={'AgentRadius': -1, 'AgentHeight': -1, 'AgentStepHeight': -1, 'NavWalkingSearchHeightScale': 0.5, 'PreferredNavData': {'AssetPathName': 'None', 'SubPathString': ''}, 'bCanCrouch': True, 'bCanJump': True, 'bCanWalk': True, 'bCanSwim': True, 'bCanFly': False}, ObjectClass='/Script/FactoryGame.FGCharacterMovementComponent', ObjectFlags=2883617, ObjectName='CharMoveComp', WalkableFloorAngle=45, WalkableFloorZ=0.7071067690849304, bCanWalkOffLedgesWhenCrouching=True, bEnablePhysicsInteraction=False, mMaxSlideAngle=1.7000000476837158, mPipeData={'mTravelingPipeHyper': {'$Empty': True}, 'mMinPipeSpeed': 1250, 'mPipeGravityStrength': 1500, 'mPipeFriction': 0.05000000074505806, 'mPipeConstantAcceleration': 160, 'mPipeCurveDamping': 1.7999999523162842}, mSlideCurve={'$AssetPath': '/Game/FactoryGame/Character/Player/SlideCurve.SlideCurve'}, mSlopeCurve={'$AssetPath': '/Game/FactoryGame/Character/Player/SlopeCurveMultiplier.SlopeCurveMultiplier'}, mSprintMinDotResult=0.20000000298023224)
    CapsuleComponent = Namespace(BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 238.15028381347656, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CapsuleHalfHeight=96, CapsuleRadius=40, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bReturnMaterialOnMove=True, bShouldUpdatePhysicsVolume=True)
    CrouchedEyeHeight = 48
    JumpMaxHoldTime = 0.20000000298023224
    BaseEyeHeight = 80
    bNetUseOwnerRelevancy = True
    bBlockInput = True
    RootComponent = Namespace(BodyInstance={'ObjectType': 2, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Pawn', 'CollisionResponses': {'ResponseArray': [{'Channel': 'Visibility', 'Response': 0}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 238.15028381347656, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, CapsuleHalfHeight=96, CapsuleRadius=40, ObjectClass='/Script/Engine.CapsuleComponent', ObjectFlags=2883617, ObjectName='CollisionCylinder', bCanEverAffectNavigation=False, bReturnMaterialOnMove=True, bShouldUpdatePhysicsVolume=True)
    
    def GetActorCompassViewDistance(self):
        ReturnValue = 4
    

    def SetActorCompassViewDistance(self):
        ReturnValue = 0
    

    def SetActorRepresentationText(self):
        self.mMapText = newText
        ReturnValue = self.mMapText
    

    def UpdateRepresentation(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L145')
        # Label 34
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = ReturnValue_0.UpdateRepresentation(self, False)
        ReturnValue_2: bool = ReturnValue_1
        goto('L156')
        # Label 145
        ReturnValue_2 = False
    

    def GetActorRepresentationColor(self):
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](self.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
            goto('L161')
        ReturnValue: LinearColor = State.GetNametagColor()
        ReturnValue_0: LinearColor = ReturnValue
        # Label 156
        goto('L243')
        
        Text = None
        Graphics = None
        # Label 161
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_0 = Graphics
    

    def GetActorRepresentationText(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.PlayerState)
        if not ReturnValue:
            goto('L285')
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](self.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
            goto('L285')
        ReturnValue_0: FString = State.GetPlayerName()
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_0)
        # Label 253
        ReturnValue_2: FText = ReturnValue_1
        goto('L305')
        # Label 285
        ReturnValue_2 = 
    

    def GetActorRepresentationTexture(self):
        Variable: Ptr[Texture2D] = MapCompass_Icon_playerdead
        Variable1: Ptr[Texture2D] = MapCompass_Icon_player
        ReturnValue: Ptr[FGHealthComponent] = self.GetHealthComponent()
        ReturnValue_0: bool = ReturnValue.IsDead()
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_1: Ptr[Texture2D] = switch.get(Variable_0, None)
    

    def GetActorRepresentationType(self):
        ReturnValue = 5
    

    def GetActorShouldShowInCompass(self):
        ReturnValue = True
    

    def GetActorFogOfWarRevealRadius(self):
        ReturnValue = 20000
    

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
            goto('L244')
        # Label 34
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L244')
        ReturnValue_0 = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_2: bool = ReturnValue_0.RemoveRepresentationOfActor(self)
        # Label 228
        ReturnValue_3: bool = False
        # Label 239
        goto('L255')
        # Label 244
        ReturnValue_3 = False
    

    def GetRealActorRotation(self):
        ReturnValue: Rotator = self.K2_GetActorRotation()
        ReturnValue_0: Rotator = ReturnValue
    

    def AddAsRepresentation(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L145')
        # Label 34
        ReturnValue_0: Ptr[FGActorRepresentationManager] = Default__FGActorRepresentationManager.Get(self)
        ReturnValue_1: bool = ReturnValue_0.CreateAndAddNewRepresentation(self, False)
        ReturnValue_2: bool = ReturnValue_1
        goto('L156')
        # Label 145
        ReturnValue_2 = False
    

    def GetActorShouldShowOnMap(self):
        ReturnValue = True
    

    def GetRealActorLocation(self):
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue_0: Vector = Vector(0, 0, self.CapsuleComponent.CapsuleHalfHeight)
        # Label 97
        ReturnValue_1: Vector = ReturnValue + ReturnValue_0
        ReturnValue_2: Vector = ReturnValue_1
    

    def IsActorStatic(self):
        ReturnValue = False
    

    def TubeTravelHardCorners(self, CurveFloatValue: float):
        ReturnValue: bool = CurveFloatValue > 3
        # Label 34
        if not ReturnValue:
            goto('L239')
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mSFXFastJUnction)
        if not ReturnValue_0:
            goto('L118')
        # End
        # Label 118
        ReturnValue_1: Vector = self.K2_GetActorLocation()
        ReturnValue_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_HitTube, ReturnValue_1, Rotator::FromPitchYawRoll(0, 0, 0))
        self.mSFXFastJUnction = ReturnValue_2
    

    def AudioWindDirectionSpeedUpdate(self):
        pass
    

    def SlideVFX(self):
        
        self.CharacterMovement.CurrentFloor.HitResult = None
        ReturnValue: uint8 = Default__GameplayStatics.GetSurfaceType(Ref[self.CharacterMovement.CurrentFloor.HitResult])
        CmpSuccess: bool = NotEqual_ByteByte(ReturnValue, 1)
        if not CmpSuccess:
            goto('L545')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 2)
        if not CmpSuccess:
            goto('L1141')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 3)
        if not CmpSuccess:
            goto('L1141')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 4)
        # Label 256
        if not CmpSuccess:
            goto('L1326')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 5)
        if not CmpSuccess:
            goto('L1922')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 6)
        if not CmpSuccess:
            goto('L2375')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 7)
        if not CmpSuccess:
            goto('L1326')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 8)
        if not CmpSuccess:
            goto('L2375')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 9)
        if not CmpSuccess:
            goto('L956')
        CmpSuccess = NotEqual_ByteByte(ReturnValue, 10)
        if not CmpSuccess:
            goto('L545')
        # End
        
        Roll1 = None
        Pitch1 = None
        Yaw1 = None
        # Label 545
        BreakRotator(self.CapsuleComponent.RelativeRotation, Ref[Roll1], Ref[Pitch1], Ref[Yaw1])
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(self.CapsuleComponent.RelativeLocation)
        ReturnValue_0: float = Z - 45
        ReturnValue_1: Vector = Vector(X, Y, ReturnValue_0)
        ReturnValue3: Rotator = MakeRotator(0, -90, Yaw1)
        ReturnValue2: Ptr[DecalComponent] = Default__GameplayStatics.SpawnDecalAtLocation(self, MI_SlideDecal_Sand, Vector(15, 75, 125), ReturnValue_1, ReturnValue3, 6)
        ReturnValue2.SetFadeOut(5, 1, True)
        # Label 956
        ReturnValue1: Vector = self.Mesh.GetSocketLocation("Slide_VFX_Socket")
        ReturnValue4: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_PlayerSliding_Sand, self.Mesh, "None", ReturnValue1, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 1, True, 0)
        # End
        # Label 1141
        ReturnValue_2: Vector = self.Mesh.GetSocketLocation("Slide_VFX_Socket")
        ReturnValue_3: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_PlayerSliding_Rock, self.Mesh, "None", ReturnValue_2, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 1, True, 0)
        # End
        
        Roll1 = None
        Pitch1 = None
        Yaw1 = None
        # Label 1326
        BreakRotator(self.CapsuleComponent.RelativeRotation, Ref[Roll1], Ref[Pitch1], Ref[Yaw1])
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(self.CapsuleComponent.RelativeLocation)
        ReturnValue_0 = Z - 45
        ReturnValue2_0: Rotator = MakeRotator(0, -90, Yaw1)
        ReturnValue_1 = Vector(X, Y, ReturnValue_0)
        ReturnValue3_0: Ptr[DecalComponent] = Default__GameplayStatics.SpawnDecalAtLocation(self, MI_SlideDecal_Sand, Vector(55, 75, 125), ReturnValue_1, ReturnValue2_0, 5)
        ReturnValue3_0.SetFadeOut(2, 2, True)
        ReturnValue1 = self.Mesh.GetSocketLocation("Slide_VFX_Socket")
        ReturnValue3_1: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_PlayerSliding_Grass, self.Mesh, "None", ReturnValue1, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 1, True, 0)
        # End
        
        Roll = None
        Pitch = None
        Yaw = None
        # Label 1922
        BreakRotator(self.CapsuleComponent.RelativeRotation, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_4: Rotator = MakeRotator(0, -90, Yaw)
        ReturnValue_5: Ptr[DecalComponent] = Default__GameplayStatics.SpawnDecalAtLocation(self, MI_SlideDecal_Sand, Vector(55, 75, 125), self.CapsuleComponent.RelativeLocation, ReturnValue_4, 6)
        ReturnValue_5.SetFadeOut(5, 1, True)
        ReturnValue_2 = self.Mesh.GetSocketLocation("Slide_VFX_Socket")
        ReturnValue1_0: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_PlayerSliding_Moist, self.Mesh, "None", ReturnValue_2, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 1, True, 0)
        # End
        
        Roll1 = None
        Pitch1 = None
        Yaw1 = None
        # Label 2375
        BreakRotator(self.CapsuleComponent.RelativeRotation, Ref[Roll1], Ref[Pitch1], Ref[Yaw1])
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(self.CapsuleComponent.RelativeLocation)
        ReturnValue1_1: Rotator = MakeRotator(0, -90, Yaw1)
        ReturnValue_0 = Z - 45
        ReturnValue_1 = Vector(X, Y, ReturnValue_0)
        ReturnValue1_2: Ptr[DecalComponent] = Default__GameplayStatics.SpawnDecalAtLocation(self, MI_SlideDecal_Sand, Vector(55, 75, 125), ReturnValue_1, ReturnValue1_1, 5)
        ReturnValue1_2.SetFadeOut(2, 2, True)
        ReturnValue1 = self.Mesh.GetSocketLocation("Slide_VFX_Socket")
        ReturnValue2_1: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_PlayerSliding_Gravel, self.Mesh, "None", ReturnValue1, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 1, True, 0)
    

    def TubeTravelSpeedUpdate(self):
        ReturnValue1: Vector = self.GetVelocity()
        ReturnValue1_0: float = VSize(ReturnValue1)
        ReturnValue1_1: float = MapRangeClamped(ReturnValue1_0, 700, 2200, 0, 0.25)
        self.mVFX_Capsule_Opacity = ReturnValue1_1
        self.mHypertube_VfxCap.SetScalarParameterValueOnMaterials("Opacity", self.mVFX_Capsule_Opacity)
        ReturnValue1 = self.GetVelocity()
        # Label 239
        ReturnValue1_0 = VSize(ReturnValue1)
        ReturnValue: float = MapRangeClamped(ReturnValue1_0, 700, 2200, 0, 100)
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_TubeVelocity", ReturnValue, 0, self)
        ReturnValue_0: PlayerPipeHyperData = self.mFGCharacterMovementCompRef.GetPipeHyperDataRef()
        ReturnValue_1: float = ReturnValue_0.mMaxCurveDiffThisFrame * 100
        self.TubeTravelHardCorners(ReturnValue_1)
        ReturnValue_0 = self.mFGCharacterMovementCompRef.GetPipeHyperDataRef()
        # Label 567
        ReturnValue_2: bool = EqualEqual_FloatFloat(ReturnValue_0.mCombinedLengthTillEndOfPipesINcludingCurrent, self.mSwitchingPipes)
        ReturnValue_3: bool = Not_PreBool(ReturnValue_2)
        if not ReturnValue_3:
            goto('L989')
        ReturnValue_0 = self.mFGCharacterMovementCompRef.GetPipeHyperDataRef()
        self.mSwitchingPipes = ReturnValue_0.mCombinedLengthTillEndOfPipesINcludingCurrent
        ReturnValue_4: Vector = self.GetVelocity()
        ReturnValue_5: float = VSize(ReturnValue_4)
        ReturnValue_6: bool = GreaterEqual_FloatFloat(ReturnValue_5, 1800)
        if not ReturnValue_6:
            goto('L1445')
        ReturnValue_7: Vector = self.HelmetMesh.K2_GetComponentLocation()
        ReturnValue_8: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_FastJunctionsTube, ReturnValue_7, Rotator::FromPitchYawRoll(0, 0, 0))
        # End
        # Label 989
        ReturnValue_0 = self.mFGCharacterMovementCompRef.GetPipeHyperDataRef()
        ReturnValue_9: bool = ReturnValue_0.mDistanceToEndOfPipe <= 1000
        if not ReturnValue_9:
            goto('L1445')
        ReturnValue_0 = self.mFGCharacterMovementCompRef.GetPipeHyperDataRef()
        ReturnValue_10: bool = EqualExactly_VectorVector(self.mLastFrameEndPosTube, ReturnValue_0.mFulPipeEndPoint)
        ReturnValue1_2: bool = Not_PreBool(ReturnValue_10)
        if not ReturnValue1_2:
            goto('L1445')
        ReturnValue_0 = self.mFGCharacterMovementCompRef.GetPipeHyperDataRef()
        self.mLastFrameEndPosTube = ReturnValue_0.mFulPipeEndPoint
        ReturnValue_0 = self.mFGCharacterMovementCompRef.GetPipeHyperDataRef()
        
        ReturnValue_0.mFulPipeEndDir = None
        ReturnValue_11: Rotator = MakeRotFromX(Ref[ReturnValue_0.mFulPipeEndDir])
        self.mLastFrameEndRotTube = ReturnValue_11
    

    def SlideSpeedWindUpdate(self):
        ReturnValue: Vector = self.GetVelocity()
        ReturnValue_0: float = VSize(ReturnValue)
        ReturnValue1: bool = GreaterEqual_FloatFloat(ReturnValue_0, 850)
        if not ReturnValue1:
            goto('L292')
        ReturnValue_1: float = self.mCurrentSpeedWindTimer + 1
        self.mCurrentSpeedWindTimer = ReturnValue_1
        ReturnValue_2: bool = EqualEqual_FloatFloat(self.mCurrentSpeedWindTimer, 7)
        if not ReturnValue_2:
            goto('L416')
        ReturnValue_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_P_SlideSpeedwind, self, True)
        # End
        # Label 292
        ReturnValue_4: bool = GreaterEqual_FloatFloat(self.mCurrentSpeedWindTimer, 7)
        if not ReturnValue_4:
            goto('L416')
        self.mCurrentSpeedWindTimer = 0
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_P_SlideSpeedWind, self, True)
    

    def SlideVelocityUpdate(self):
        ReturnValue: Vector = self.GetVelocity()
        ReturnValue_0: float = VSize(ReturnValue)
        ReturnValue_1: float = MapRangeClamped(ReturnValue_0, 240, 900, 0, 100)
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_C_Slide", ReturnValue_1, 0, self)
        Variable: float = 100
        Variable1: float = 0
        ReturnValue = self.GetVelocity()
        ReturnValue_0 = VSize(ReturnValue)
        ReturnValue_2: bool = ReturnValue_0 <= 241
        Variable_0: bool = ReturnValue_2
        
        switch = {
            False: Variable,
            True: Variable1
        }
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_C_SlideVolume", switch.get(Variable_0, None), 0, self)
        
        self.CharacterMovement.CurrentFloor.HitResult = None
        ReturnValue_3: uint8 = Default__GameplayStatics.GetSurfaceType(Ref[self.CharacterMovement.CurrentFloor.HitResult])
        ReturnValue_4: int32 = Conv_ByteToInt(ReturnValue_3)
        ReturnValue_5: bool = EqualEqual_IntInt(self.mLastSlideSurfaceType, ReturnValue_4)
        if not ReturnValue_5:
            goto('L642')
        # End
        
        self.CharacterMovement.CurrentFloor.HitResult = None
        # Label 642
        ReturnValue_3 = Default__GameplayStatics.GetSurfaceType(Ref[self.CharacterMovement.CurrentFloor.HitResult])
        ReturnValue_4 = Conv_ByteToInt(ReturnValue_3)
        # Label 769
        self.mLastSlideSurfaceType = ReturnValue_4
        Variable_1: FString = ""
        Variable1_0: FString = "Panel"
        Variable2: FString = "Coral"
        Variable3: FString = "Grate"
        Variable4: FString = "Cement"
        Variable5: FString = "Soil"
        Variable6: FString = "SandCracked"
        Variable7: FString = "RockGravel"
        Variable8: FString = "GrassHigh"
        Variable9: FString = "Gravel"
        Variable10: FString = "Moist"
        Variable11: FString = "Grass"
        Variable12: FString = "Rock"
        Variable13: FString = "Metal"
        Variable14: FString = "Sand"
        Variable15: FString = "Default"
        
        self.CharacterMovement.CurrentFloor.HitResult = None
        ReturnValue_3 = Default__GameplayStatics.GetSurfaceType(Ref[self.CharacterMovement.CurrentFloor.HitResult])
        Variable_2: uint8 = ReturnValue_3
        
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
            14: Variable1_0,
            15: Variable_1
        }
        ReturnValue_6: FName = Default__KismetStringLibrary.Conv_StringToName(switch_0.get(Variable_2, None))
        self.mCurrentSlidingSurfaceType = ReturnValue_6
        Default__AkGameplayStatics.SetSwitch("Slide_Surface", self.mCurrentSlidingSurfaceType, self)
    

    def ToggleCodex(self):
        ReturnValue1: Ptr[Controller] = self.GetController()
        
        outHUD = None
        Default__BPFL_HudHelperBadRef.GetBPHUD(ReturnValue1, self, Ref[outHUD])
        ReturnValue: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L505')
        ReturnValue = self.GetBuildGun()
        ReturnValue_1: bool = ReturnValue.IsEquipped()
        if not ReturnValue_1:
            goto('L246')
        # Label 236
        self.ToggleBuildGun()
        # Label 246
        ReturnValue_2: Ptr[Controller] = self.GetController()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L505')
        ReturnValue_3: DisabledInputGate = Controller.GetDisabledInputGate()
        # Label 395
        if not ReturnValue_3.mOpenCodex:
            goto('L459')
        outHUD.CloseInteractUIIfOpen()
        # End
        # Label 459
        outHUD.OpenInteractUI(Widget_Codex_Container, None)
    

    def ToggleInventory(self):
        ReturnValue: Ptr[Controller] = self.GetController()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L769')
        ReturnValue_0: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_0)
        bSuccess2: bool = AsFGHUD
        if not bSuccess2:
            goto('L769')
        ReturnValue_0 = Controller.GetHUD()
        HUD: Ptr[BP_HUD] = Cast[BP_HUD](ReturnValue_0)
        bSuccess1: bool = HUD
        if not bSuccess1:
            goto('L769')
        ReturnValue_1: DisabledInputGate = Controller.GetDisabledInputGate()
        ReturnValue_2: bool = Not_PreBool(ReturnValue_1.mInventory)
        ReturnValue_3: Ptr[FGGameUI] = AsFGHUD.GetGameUI()
        
        Widget = None
        Default__BPHUDHelpers.FindWidgetOfClass(Widget_PlayerInventory, ReturnValue_3, self, Ref[Widget])
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(Widget)
        ReturnValue_5: bool = BooleanOR(ReturnValue_4, ReturnValue_2)
        if not ReturnValue_5:
            goto('L674')
        HUD.ToggleInventoryUI()
        
        IsOpen = None
        # Label 674
        HUD.IsInventoryOpen(Ref[IsOpen])
        Controller.OnToggleInventory.ProcessMulticastDelegate(IsOpen)
    

    def ToggleFlashlight(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L97')
        # Label 34
        self.FlushNetDormancy()
        ReturnValue1: bool = Not_PreBool(self.mFlashlightOn)
        self.mFlashlightOn = ReturnValue1
        # End
        # Label 97
        ReturnValue_0: bool = Not_PreBool(self.mFlashlightOn)
        self.Server_SetFlashlightOn(ReturnValue_0)
        goto('L34')
    

    def RemovePlayerHUD(self, OldController: Ptr[FGPlayerController]):
        
        outHUD = None
        Default__BPFL_HudHelperBadRef.GetBPHUD(OldController, self, Ref[outHUD])
        outHUD.RemovePawnHUD()
    

    def SetupPlayerHUD(self, PlayerController: Ptr[FGPlayerController]):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mPlayerHUDClass)
        if not ReturnValue:
            goto('L228')
        ReturnValue_0: Ptr[HUD] = PlayerController.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_0)
        bSuccess: bool = AsFGHUD
        # Label 172
        if not bSuccess:
            goto('L228')
        AsFGHUD.AddPawnHUD(self.mPlayerHUDClass, self)
    

    def HandleFlashlight(self):
        ReturnValue: bool = self.IsLocallyControlled()
        if not ReturnValue:
            goto('L384')
        ReturnValue_0: Ptr[SpringArmComponent] = self.GetSpringArmComponent()
        ReturnValue_1: bool = ReturnValue_0.TargetArmLength <= 50
        ReturnValue_2: bool = ReturnValue_1 and self.mFlashlightOn
        self.FlashLight1P.SetVisibility(ReturnValue_2, False)
        ReturnValue_0 = self.GetSpringArmComponent()
        ReturnValue_1 = ReturnValue_0.TargetArmLength <= 50
        ReturnValue_3: bool = Not_PreBool(ReturnValue_1)
        ReturnValue1: bool = ReturnValue_3 and self.mFlashlightOn
        self.FlashLight3P.SetVisibility(ReturnValue1, True)
        # End
        # Label 384
        self.FlashLight3P.SetVisibility(self.mFlashlightOn, True)
        self.FlashLight1P.SetVisibility(False, False)
    

    def UpdatePlayerTextVisibility(self):
        ReturnValue: Ptr[PlayerController] = Default__GameplayStatics.GetPlayerController(self, 0)
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L395')
        ReturnValue = Default__GameplayStatics.GetPlayerController(self, 0)
        # Label 161
        ReturnValue_1: Ptr[HUD] = ReturnValue.GetHUD()
        # Label 203
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_1)
        # Label 239
        bSuccess: bool = AsFGHUD
        if not bSuccess:
            goto('L395')
        ReturnValue_2: bool = AsFGHUD.GetPumpiMode()
        ReturnValue_3: bool = Not_PreBool(ReturnValue_2)
        self.PlayerText.SetVisibility(ReturnValue_3, False)
    

    def GetHealthPct(self):
        ReturnValue: Ptr[FGHealthComponent] = self.GetHealthComponent()
        ReturnValue_0: float = ReturnValue.GetMaxHealth()
        ReturnValue_1: float = ReturnValue.GetCurrentHealth()
        ReturnValue_2: float = ReturnValue_1 / ReturnValue_0
        healthPct = ReturnValue_2
    

    def UpdateDamageIndicator(self):
        
        healthPct = None
        self.GetHealthPct(Ref[healthPct])
        ReturnValue: float = healthPct * 100
        ReturnValue_0: float = FClamp(ReturnValue, 0, 100)
        ReturnValue_1: float = MapRangeUnclamped(ReturnValue_0, 0, 60, 3, 0)
        ReturnValue1: float = FClamp(ReturnValue_1, 0, 3)
        ReturnValue1_0: float = FInterpTo(self.mLowHealthIndicatorPower, ReturnValue1, self.mDeltaTime, 2)
        self.mLowHealthIndicatorPower = ReturnValue1_0
        ReturnValue1_1: float = self.mLowHealthIndicatorPower * self.PPTakeDamage.BlendWeight
        Default__KismetMaterialLibrary.SetScalarParameterValue(self, deathBloodFX, "Power", ReturnValue1_1)
        ReturnValue_2: float = FInterpTo(self.mCurrentDamageIndicator, self.mDesiredDamageIndicator, self.mDeltaTime, self.mDamageIndicatorSpeed)
        self.mCurrentDamageIndicator = ReturnValue_2
        Default__KismetMaterialLibrary.SetScalarParameterValue(self, deathBloodFX, "Blood2Power", self.mCurrentDamageIndicator)
        ReturnValue_2 = FInterpTo(self.mCurrentDamageIndicator, self.mDesiredDamageIndicator, self.mDeltaTime, self.mDamageIndicatorSpeed)
        ReturnValue_3: bool = NearlyEqual_FloatFloat(self.mCurrentDamageIndicator, ReturnValue_2, 0.009999999776482582)
        if not ReturnValue_3:
            goto('L757')
        self.mDesiredDamageIndicator = 0
        self.mDamageIndicatorSpeed = 3
    

    def PlayDamageVO(self, Damage Type: Const[Ptr[DamageType]]):
        Type: Const[Ptr[BP_DamageType]] = Cast[BP_DamageType](Damage Type)
        bSuccess: bool = Type
        if not bSuccess:
            goto('L256')
        
        healthPct = None
        self.GetHealthPct(Ref[healthPct])
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_C_Health", healthPct, 0, self)
        if not Type.mFromRadiation:
            goto('L203')
        # End
        # Label 203
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_P_Suit_Damage_Warning, self, True)
    

    def PlayDamageCameraShake(self):
        pass
    

    def ApplyDamagePP(self):
        ReturnValue: bool = self.IsLocallyControlled()
        if not ReturnValue:
            goto('L253')
        
        blendWeight = None
        self.CalculateOnscreenEffectBlendWeight(Ref[blendWeight])
        self.PPTakeDamage.BlendWeight = blendWeight
        self.mDamageIndicatorSpeed = 30
        ReturnValue_0: float = self.mCurrentDamageIndicator + 1
        ReturnValue_1: float = FClamp(ReturnValue_0, 0, self.mMaxDamageIndicator)
        self.mDesiredDamageIndicator = ReturnValue_1
    

    def PlayImpactEffectSound(self, DamageType: Const[Ptr[DamageType]]):
        Type: Const[Ptr[FGDamageType]] = Cast[FGDamageType](DamageType)
        bSuccess: bool = Type
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(Type.mImpactAudioEvent)
        if not ReturnValue:
            goto('L292')
        Type = Cast[FGDamageType](DamageType)
        bSuccess = Type
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Type.mImpactAudioEvent, self, True)
    

    def CalculateOnscreenEffectBlendWeight(self):
        BlendWeight = 1
    

    def UpdateWindParticle(self):
        pass
    

    def TickSprintNoise(self):
        Component: Ptr[FGCharacterMovementComponent] = Cast[FGCharacterMovementComponent](self.CharacterMovement)
        bSuccess: bool = Component
        if not bSuccess:
            goto('L382')
        ReturnValue: bool = Component.GetIsSprinting()
        if not ReturnValue:
            goto('L359')
        ReturnValue_0: float = self.mTimeSprinting + self.mDeltaTime
        self.mTimeSprinting = ReturnValue_0
        ReturnValue_1: bool = GreaterEqual_FloatFloat(self.mTimeSprinting, self.mSprintNoiseInterval)
        # Label 246
        if not ReturnValue_1:
            goto('L382')
        self.mTimeSprinting = 0
        ReturnValue_2: Vector = self.K2_GetActorLocation()
        self.MakeNoise(0.5, self, ReturnValue_2, 0, "PlayerSprinting")
        # End
        # Label 359
        self.mTimeSprinting = 0
    

    def GetPlayerCameraManager(self):
        ReturnValue: Ptr[Controller] = self.GetController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue)
        bSuccess: bool = Controller
        cameraManager = Controller.PlayerCameraManager
    

    def FadeDamageIndicator(self):
        ReturnValue: bool = self.mLastDamageTime <= 0
        # Label 34
        if not ReturnValue:
            goto('L53')
        # End
        # Label 53
        ReturnValue_0: float = self.PPTakeDamage.BlendWeight * 2
        ReturnValue1: float = self.mDeltaTime * ReturnValue_0
        ReturnValue_1: float = self.PPTakeDamage.BlendWeight - ReturnValue1
        ReturnValue_2: float = FClamp(ReturnValue_1, 0, 1)
        self.PPTakeDamage.BlendWeight = ReturnValue_2
    

    def TickPlayerNameText(self):
        ReturnValue: Ptr[PlayerController] = Default__GameplayStatics.GetPlayerController(self, 0)
        
        OutLocation = None
        OutRotation = None
        ReturnValue.GetActorEyesViewPoint(Ref[OutLocation], Ref[OutRotation])
        viewLocation: Vector = OutLocation
        ReturnValue_0: bool = self.IsLocallyControlled()
        if not ReturnValue_0:
            goto('L172')
        # Label 167
        # End
        # Label 172
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(self.PlayerState)
        if not ReturnValue_1:
            goto('L167')
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](self.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
            goto('L1282')
        ReturnValue_2: FString = State.GetPlayerName()
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_StringToText(ReturnValue_2)
        
        self.PlayerText.K2_SetText(Ref[ReturnValue_3])
        ReturnValue_4: LinearColor = State.GetNametagColor()
        ReturnValue_5: Color = Conv_LinearColorToColor(ReturnValue_4, True)
        self.PlayerText.SetTextRenderColor(ReturnValue_5)
        ReturnValue_6: Vector = self.K2_GetActorLocation()
        ReturnValue_7: Vector = Subtract_VectorVector(viewLocation, ReturnValue_6)
        ReturnValue_8: float = VSize(ReturnValue_7)
        ReturnValue_9: float = ReturnValue_8 / 500
        ReturnValue_10: float = FClamp(ReturnValue_9, 0, 3)
        self.PlayerText.SetYScale(ReturnValue_10)
        ReturnValue_6 = self.K2_GetActorLocation()
        ReturnValue_7 = Subtract_VectorVector(viewLocation, ReturnValue_6)
        ReturnValue_8 = VSize(ReturnValue_7)
        ReturnValue_9 = ReturnValue_8 / 500
        # Label 989
        ReturnValue_10 = FClamp(ReturnValue_9, 0, 3)
        self.PlayerText.SetXScale(ReturnValue_10)
        ReturnValue_6 = self.K2_GetActorLocation()
        ReturnValue_7 = Subtract_VectorVector(viewLocation, ReturnValue_6)
        ReturnValue_11: Vector = Normal(ReturnValue_7, 9.999999747378752e-05)
        ReturnValue_12: Rotator = Conv_VectorToRotator(ReturnValue_11)
        
        SweepHitResult = None
        self.PlayerText.K2_SetWorldRotation(ReturnValue_12, False, False, Ref[SweepHitResult])
    

    def InpActEvt_OpenCodex_K2Node_InputActionEvent_6(self, Key: Key):
        ExecuteUbergraph_Char_Player.K2Node_InputActionEvent_Key6 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(17139)
    

    def InpActEvt_Flashlight_K2Node_InputActionEvent_5(self, Key: Key):
        ExecuteUbergraph_Char_Player.K2Node_InputActionEvent_Key5 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(13687)
    

    def InpActEvt_PrimaryFire_K2Node_InputActionEvent_4(self, Key: Key):
        ExecuteUbergraph_Char_Player.K2Node_InputActionEvent_Key4 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(12591)
    

    def InpActEvt_Inventory_K2Node_InputActionEvent_3(self, Key: Key):
        ExecuteUbergraph_Char_Player.K2Node_InputActionEvent_Key3 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(12586)
    

    def InpActEvt_EmoteWheel_K2Node_InputActionEvent_2(self, Key: Key):
        ExecuteUbergraph_Char_Player.K2Node_InputActionEvent_Key2 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(19503)
    

    def InpActEvt_EmoteWheel_K2Node_InputActionEvent_1(self, Key: Key):
        ExecuteUbergraph_Char_Player.K2Node_InputActionEvent_Key1 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(19410)
    

    def InpActEvt_QuickSearch_K2Node_InputActionEvent_0(self, Key: Key):
        ExecuteUbergraph_Char_Player.K2Node_InputActionEvent_Key = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(14552)
    

    def SetFirstPersonMode(self):
        self.ExecuteUbergraph_Char_Player(3207)
    

    def SetThirdPersonMode(self):
        self.ExecuteUbergraph_Char_Player(1935)
    

    def CameraTick(self):
        self.ExecuteUbergraph_Char_Player(775)
    

    def StartFocusAim(self):
        self.ExecuteUbergraph_Char_Player(2056)
    

    def StopFocusAim(self):
        self.ExecuteUbergraph_Char_Player(2337)
    

    def StartFreeRotate3P(self):
        self.ExecuteUbergraph_Char_Player(2421)
    

    def StopFreeRotate3P(self):
        self.ExecuteUbergraph_Char_Player(2436)
    

    def CameraZoomOut(self):
        self.ExecuteUbergraph_Char_Player(2451)
    

    def CameraZoomIn(self):
        self.ExecuteUbergraph_Char_Player(2619)
    

    def ReceiveDied(self):
        self.ExecuteUbergraph_Char_Player(2873)
    

    def PlayPickupEffects(self):
        self.ExecuteUbergraph_Char_Player(3945)
    

    def OnLanded(self):
        ExecuteUbergraph_Char_Player.K2Node_Event_Hit = Hit #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(6588)
    

    def SnapSpringArmToDesiredLocation(self):
        self.ExecuteUbergraph_Char_Player(6608)
    

    def OnReviveComplete(self):
        self.ExecuteUbergraph_Char_Player(6678)
    

    def ClientSetupPlayerHUD(self, InController: Ptr[Controller]):
        ExecuteUbergraph_Char_Player.K2Node_CustomEvent_inController = InController #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(6703)
    

    def ReceiveUnpossessed(self):
        ExecuteUbergraph_Char_Player.K2Node_Event_OldController = OldController #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(6802)
    

    def ReceivePossessed(self):
        ExecuteUbergraph_Char_Player.K2Node_Event_NewController = NewController #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(6826)
    

    def OnReceiveRadiationStart(self):
        self.ExecuteUbergraph_Char_Player(6850)
    

    def OnReceiveRadiationStop(self):
        self.ExecuteUbergraph_Char_Player(6937)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_Char_Player(8102)
    

    def TakeDamageEvent(self, DamagedActor: Ptr[Actor], damageAmount: float, DamageType: Const[Ptr[DamageType]], InstigatedBy: Ptr[Controller], DamageCauser: Ptr[Actor]):
        ExecuteUbergraph_Char_Player.K2Node_CustomEvent_damagedActor = DamagedActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Player.K2Node_CustomEvent_damageAmount = damageAmount #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Player.K2Node_CustomEvent_damageType = DamageType #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Player.K2Node_CustomEvent_instigatedBy = InstigatedBy #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Player.K2Node_CustomEvent_damageCauser = DamageCauser #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(8107)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Char_Player(8655)
    

    def Server_PlayClap(self):
        self.ExecuteUbergraph_Char_Player(8680)
    

    def Multicast_PlayClap(self):
        self.ExecuteUbergraph_Char_Player(8695)
    

    def Server_SetFlashlightOn(self, FlashlightOn: bool):
        ExecuteUbergraph_Char_Player.K2Node_CustomEvent_FlashlightOn = FlashlightOn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(9173)
    

    def OnDisabledInputGateChanged(self):
        ExecuteUbergraph_Char_Player.K2Node_Event_newValue = NewValue #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(9193)
    

    def LimitLook(self, doLimit: bool):
        ExecuteUbergraph_Char_Player.K2Node_CustomEvent_doLimit = doLimit #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(10143)
    

    def StartCinematic(self):
        self.ExecuteUbergraph_Char_Player(11235)
    

    def EndCinematic(self):
        self.ExecuteUbergraph_Char_Player(11448)
    

    def DisableGravity(self):
        self.ExecuteUbergraph_Char_Player(11748)
    

    def Server_PlaySpinEmote(self):
        self.ExecuteUbergraph_Char_Player(11789)
    

    def Multicast_PlatSpinEmote(self):
        self.ExecuteUbergraph_Char_Player(12186)
    

    def ClearEmoteMesh(self):
        self.ExecuteUbergraph_Char_Player(12529)
    

    def OnSpawnDeathMarker(self):
        self.ExecuteUbergraph_Char_Player(12581)
    

    def ShowEmote(self, EmoteIndex: int32):
        ExecuteUbergraph_Char_Player.K2Node_CustomEvent_EmoteIndex = EmoteIndex #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(12905)
    

    def SkipIntro(self):
        self.ExecuteUbergraph_Char_Player(13456)
    

    def Server_playSignsEmote(self):
        self.ExecuteUbergraph_Char_Player(13667)
    

    def Multicast_PlaySignsEmote(self):
        self.ExecuteUbergraph_Char_Player(13682)
    

    def StartIsLookedAt(self):
        ExecuteUbergraph_Char_Player.K2Node_Event_byCharacter1 = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Player.K2Node_Event_state1 = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(13707)
    

    def StopIsLookedAt(self):
        ExecuteUbergraph_Char_Player.K2Node_Event_byCharacter = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Player.K2Node_Event_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(13821)
    

    def OnRadiationIntensityUpdated(self):
        ExecuteUbergraph_Char_Player.K2Node_Event_radiationIntensity = radiationIntensity #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Player.K2Node_Event_radiationImmunity = radiationImmunity #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(13873)
    

    def TickVisuals(self):
        ExecuteUbergraph_Char_Player.K2Node_Event_dt = dt #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(14834)
    

    def OnSlideStartLocal(self):
        self.ExecuteUbergraph_Char_Player(16165)
    

    def OnSlideEndLocal(self):
        self.ExecuteUbergraph_Char_Player(16235)
    

    def OnSlideEndSimulated(self):
        self.ExecuteUbergraph_Char_Player(16453)
    

    def OnSlideStartSimulated(self):
        self.ExecuteUbergraph_Char_Player(16591)
    

    def PlayJumpEffects(self):
        ExecuteUbergraph_Char_Player.K2Node_Event_boostJump = boostJump #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(16750)
    

    def SpeedWindEvent(self):
        self.ExecuteUbergraph_Char_Player(16829)
    

    def K2_OnMovementModeChanged(self):
        ExecuteUbergraph_Char_Player.K2Node_Event_PrevMovementMode = PrevMovementMode #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Player.K2Node_Event_NewMovementMode = NewMovementMode #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Player.K2Node_Event_PrevCustomMode = PrevCustomMode #  PERSISTENT_FRAME(
        ExecuteUbergraph_Char_Player.K2Node_Event_NewCustomMode = NewCustomMode #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(17144)
    

    def AudioTickEvent(self, AudioTick: float):
        ExecuteUbergraph_Char_Player.K2Node_CustomEvent_AudioTick = AudioTick #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(19404)
    

    def SetActorRepresentationColor(self):
        ExecuteUbergraph_Char_Player.K2Node_Event_newColor = NewColor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Char_Player(19409)
    

    def ExecuteUbergraph_Char_Player(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue1: uint8 = self.GetCameraMode()
        ReturnValue1_0: bool = EqualEqual_ByteByte(ReturnValue1, 1)
        self.SetMeshVisibility(ReturnValue1_0)
        ReturnValue1 = self.GetCameraMode()
        ReturnValue1_0 = EqualEqual_ByteByte(ReturnValue1, 1)
        self.HelmetMesh.SetOwnerNoSee(ReturnValue1_0)
        Default__FGBlueprintFunctionLibrary.OccludeOutlineByComponent(self.HelmetMesh, False)
        goto(ExecutionFlow.Pop())
        # Label 236
        ReturnValue: Ptr[Controller] = self.GetController()
        
        AsFGHUD = None
        # Label 256
        Default__BPHUDHelpers.GetFGHud(ReturnValue, self, Ref[AsFGHUD])
        ReturnValue_0: Ptr[FGGameUI] = AsFGHUD.GetGameUI()
        ReturnValue_0.PopAllWidgets()
        ReturnValue_0 = AsFGHUD.GetGameUI()
        ReturnValue_0.ShowQuickSearch()
        goto(ExecutionFlow.Pop())
        # Label 468
        self.FlushNetDormancy()
        self.mFlashlightOn = FlashlightOn
        goto(ExecutionFlow.Pop())
        # Label 498
        self.FlushNetDormancy()
        self.mPossessed = True
        ReturnValue_1: bool = self.AddAsRepresentation()
        self.ClientSetupPlayerHUD(NewController)
        goto(ExecutionFlow.Pop())
        # Label 567
        self.FlushNetDormancy()
        self.mPossessed = False
        ReturnValue1_1: bool = self.RemoveAsRepresentation()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](OldController)
        bSuccess2: bool = Controller1
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: Ptr[BP_RemoteCallObject] = Controller1.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_2.Client_RemovePawnHUD()
        goto(ExecutionFlow.Pop())
        ReturnValue1_2: Ptr[SpringArmComponent] = self.GetSpringArmComponent()
        ReturnValue2: Ptr[SpringArmComponent] = self.GetSpringArmComponent()
        ReturnValue1_3: float = FInterpTo(ReturnValue1_2.TargetArmLength, self.mTargetCameraDistance, self.mDeltaTime, self.mDistanceInterpolationSpeed)
        ReturnValue2.TargetArmLength = ReturnValue1_3
        ReturnValue2 = self.GetSpringArmComponent()
        ReturnValue_3: Vector = VInterpTo(ReturnValue2.SocketOffset, self.mTargetCameraOffset, self.mDeltaTime, self.mDistanceInterpolationSpeed)
        ReturnValue2.SocketOffset = ReturnValue_3
        ReturnValue_4: Ptr[CameraComponent] = self.GetCameraComponent()
        ReturnValue1_4: Ptr[CameraComponent] = self.GetCameraComponent()
        ReturnValue_5: float = FInterpTo(ReturnValue1_4.FieldOfView, self.mTargetCameraFOV, self.mDeltaTime, self.mFocusInterpolationSpeed)
        ReturnValue_4.FieldOfView = ReturnValue_5
        goto(ExecutionFlow.Pop())
        # Label 1281
        self.mTargetCameraDistance = self.mCameraDistanceDefault3P
        self.mTargetCameraOffset = self.mCameraOffset3P
        self.mDistanceInterpolationSpeed = self.mDefaultCameraInterpolationSpeed
        self.mCameraDistanceMin = self.mCameraDistanceMin3P
        self.mCameraDistanceMax = self.mCameraDistanceMax3P
        self.SetMeshVisibility(False)
        self.HelmetMesh.SetOwnerNoSee(False)
        Default__FGBlueprintFunctionLibrary.OccludeOutlineByComponent(self.HelmetMesh, True)
        goto(ExecutionFlow.Pop())
        # Label 1503
        self.mDistanceInterpolationSpeed = self.mDefaultCameraInterpolationSpeed
        self.mCameraDistanceMin = 0
        self.mCameraDistanceMax = 0
        self.mTargetCameraFOV = self.mDefaultFOV
        Default__KismetSystemLibrary.Delay(self, self.mTransitionDelay, LatentActionInfo(Linkage = 15, UUID = -384970618, ExecutionFunction = "ExecuteUbergraph_Char_Player", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1684
        self.mTargetCameraFOV = self.mDefaultFOV
        goto(ExecutionFlow.Pop())
        # Label 1712
        self.mTargetCameraDistance = self.mCameraDistanceFocus3P
        self.mTargetCameraFOV = self.mFocusFOV
        goto(ExecutionFlow.Pop())
        # Label 1767
        self.mDistanceInterpolationSpeed = self.mFocusInterpolationSpeed
        self.mIsFocusing = True
        self.mSavedCameraDistance = self.mTargetCameraDistance
        goto('L1712')
        # Label 1837
        self.mDistanceInterpolationSpeed = self.mFocusInterpolationSpeed
        self.mIsFocusing = False
        self.mTargetCameraDistance = self.mSavedCameraDistance
        goto('L1684')
        # Label 1907
        self.mTargetCameraOffset = self.mCameraOffset3P
        goto(ExecutionFlow.Pop())
        self.SetThirdPersonMode()
        ReturnValue3: Ptr[SpringArmComponent] = self.GetSpringArmComponent()
        ReturnValue3.bDoCollisionTest = True
        ReturnValue3 = self.GetSpringArmComponent()
        ReturnValue3.bEnableCameraLag = True
        goto('L1281')
        self.StartFocusAim()
        ReturnValue2_0: uint8 = self.GetCameraMode()
        ReturnValue7: bool = EqualEqual_ByteByte(ReturnValue2_0, 2)
        if not ReturnValue7:
           goto(ExecutionFlow.Pop())
        goto('L1767')
        # Label 2140
        ReturnValue_6: uint8 = self.GetCameraMode()
        ReturnValue_7: bool = EqualEqual_ByteByte(ReturnValue_6, 2)
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        self.bUseControllerRotationYaw = False
        self.mTargetCameraOffset = Vector(0, 0, 0)
        goto(ExecutionFlow.Pop())
        # Label 2252
        ReturnValue_6 = self.GetCameraMode()
        ReturnValue_7 = EqualEqual_ByteByte(ReturnValue_6, 2)
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        self.bUseControllerRotationYaw = True
        goto('L1907')
        self.StopFocusAim()
        ReturnValue2_0 = self.GetCameraMode()
        # Label 2375
        ReturnValue7 = EqualEqual_ByteByte(ReturnValue2_0, 2)
        if not ReturnValue7:
           goto(ExecutionFlow.Pop())
        goto('L1837')
        self.StartFreeRotate3P()
        goto('L2140')
        self.StopFreeRotate3P()
        goto('L2252')
        self.CameraZoomOut()
        ReturnValue_8: Ptr[SpringArmComponent] = self.GetSpringArmComponent()
        ReturnValue_9: float = ReturnValue_8.TargetArmLength + 50
        ReturnValue2_1: float = FMin(ReturnValue_9, self.mCameraDistanceMax)
        self.mTargetCameraDistance = ReturnValue2_1
        goto(ExecutionFlow.Pop())
        self.CameraZoomIn()
        ReturnValue_8 = self.GetSpringArmComponent()
        ReturnValue_10: float = ReturnValue_8.TargetArmLength - 50
        ReturnValue_11: float = FMax(ReturnValue_10, self.mCameraDistanceMin)
        self.mTargetCameraDistance = ReturnValue_11
        goto(ExecutionFlow.Pop())
        # Label 2787
        self.ApplyDamagePP()
        ReturnValue7_0: bool = self.IsLocallyControlled()
        if not ReturnValue7_0:
           goto(ExecutionFlow.Pop())
        self.PlayDamageCameraShake()
        self.PlayDamageVO(damageType)
        goto(ExecutionFlow.Pop())
        self.ReceiveDied()
        ExecutionFlow.Push("L2913")
        ReturnValue_12: bool = self.UpdateRepresentation()
        goto(ExecutionFlow.Pop())
        # Label 2913
        ReturnValue4: bool = self.IsLocallyControlled()
        if not ReturnValue4:
           goto(ExecutionFlow.Pop())
        ReturnValue_13: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_P_Suit_Damage_Warning_Flatline, self, True)
        ReturnValue2_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_C_Damage_Radiation, self, True)
        ReturnValue9: Ptr[Controller] = self.GetController()
        
        AsFGHUD1 = None
        Default__BPHUDHelpers.GetFGHud(ReturnValue9, self, Ref[AsFGHUD1])
        ReturnValue1_5: Ptr[FGGameUI] = AsFGHUD1.GetGameUI()
        ReturnValue1_5.PopAllWidgets()
        goto(ExecutionFlow.Pop())
        self.SetFirstPersonMode()
        ReturnValue3 = self.GetSpringArmComponent()
        ReturnValue3.bDoCollisionTest = False
        ReturnValue3 = self.GetSpringArmComponent()
        ReturnValue3.bEnableCameraLag = False
        self.mSavedCameraDistance = self.mTargetCameraDistance
        self.mTargetCameraDistance = 0
        self.mTargetCameraOffset = Vector(0, 0, 0)
        goto('L1503')
        # Label 3409
        ReturnValue_14: Transform = self.GetTransform()
        
        ReturnValue_15: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_DeathMarker, 1, None, Ref[ReturnValue_14])
        ReturnValue_14 = self.GetTransform()
        
        ReturnValue_16: Ptr[BP_DeathMarker] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_15, Ref[ReturnValue_14])
        goto(ExecutionFlow.Pop())
        # Label 3590
        ReturnValue_17: bool = Default__KismetSystemLibrary.IsValid(self.mEmoteMenu)
        if not ReturnValue_17:
           goto(ExecutionFlow.Pop())
        ReturnValue7_1: Ptr[Controller] = self.GetController()
        Default__BPHUDHelpers.PopStackWidget(ReturnValue7_1, self.mEmoteMenu, self)
        self.mEmoteMenu.ShowEmote.Clear()
        self.mEmoteMenu = None
        goto(ExecutionFlow.Pop())
        # Label 3784
        ReturnValue_18: bool = self.IsLocallyControlled()
        if not ReturnValue_18:
            goto('L3916')
        self.UpdateDamageIndicator()
        self.FadeDamageIndicator()
        self.CameraTick()
        self.TickSprintNoise()
        self.UpdateWindParticle()
        self.AudioTickEvent(self.mDeltaTime)
        goto(ExecutionFlow.Pop())
        # Label 3916
        self.TickPlayerNameText()
        self.UpdatePlayerTextVisibility()
        goto(ExecutionFlow.Pop())
        self.PlayPickupEffects()
        ReturnValue5: bool = self.IsLocallyControlled()
        if not ReturnValue5:
            goto('L4416')
        ReturnValue_19: Ptr[SkeletalMeshComponent] = self.GetMesh1P()
        ReturnValue_20: Ptr[AnimInstance] = ReturnValue_19.GetAnimInstance()
        1p: Ptr[Anim_1p] = Cast[Anim_1p](ReturnValue_20)
        bSuccess: bool = 1p
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue3_0: bool = EqualEqual_ByteByte(1p.mArmSlotType, 1)
        ReturnValue4_0: bool = EqualEqual_ByteByte(1p.mArmSlotType, 4)
        ReturnValue_21: bool = BooleanOR(ReturnValue3_0, ReturnValue4_0)
        if not ReturnValue_21:
            goto('L5118')
        ReturnValue_19 = self.GetMesh1P()
        ReturnValue_20 = ReturnValue_19.GetAnimInstance()
        ReturnValue2_3: bool = ReturnValue_20.Montage_IsPlaying(Pickup_02_Montage)
        if not ReturnValue2_3:
            goto('L6314')
        goto(ExecutionFlow.Pop())
        # Label 4416
        ReturnValue_22: Ptr[SkeletalMeshComponent] = self.GetMesh3P()
        ReturnValue2_4: Ptr[AnimInstance] = ReturnValue_22.GetAnimInstance()
        3p: Ptr[Anim_3p] = Cast[Anim_3p](ReturnValue2_4)
        bSuccess5: bool = 3p
        if not bSuccess5:
           goto(ExecutionFlow.Pop())
        ReturnValue5_0: bool = EqualEqual_ByteByte(3p.mArmSlotType, 1)
        ReturnValue6: bool = EqualEqual_ByteByte(3p.mArmSlotType, 4)
        ReturnValue1_6: bool = BooleanOR(ReturnValue5_0, ReturnValue6)
        if not ReturnValue1_6:
            goto('L4847')
        ReturnValue_22 = self.GetMesh3P()
        ReturnValue2_4 = ReturnValue_22.GetAnimInstance()
        ReturnValue4_1: bool = ReturnValue2_4.Montage_IsPlaying(Pickup_02_Montage)
        if not ReturnValue4_1:
            goto('L6449')
        goto(ExecutionFlow.Pop())
        # Label 4847
        ReturnValue_22 = self.GetMesh3P()
        ReturnValue2_4 = ReturnValue_22.GetAnimInstance()
        ReturnValue3_1: bool = ReturnValue2_4.Montage_IsPlaying(Pickup_01_Montage)
        if not ReturnValue3_1:
            goto('L4979')
        goto(ExecutionFlow.Pop())
        # Label 4979
        ReturnValue_22 = self.GetMesh3P()
        ReturnValue2_4 = ReturnValue_22.GetAnimInstance()
        ReturnValue5_1: float = ReturnValue2_4.Montage_Play(Pickup_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 5118
        ReturnValue2_5: bool = EqualEqual_ByteByte(1p.mArmSlotType, 0)
        if not ReturnValue2_5:
            goto('L6051')
        ReturnValue_19 = self.GetMesh1P()
        ReturnValue_20 = ReturnValue_19.GetAnimInstance()
        ReturnValue1_7: bool = ReturnValue_20.Montage_IsPlaying(Pickup_Montage)
        if not ReturnValue1_7:
            goto('L5313')
        goto(ExecutionFlow.Pop())
        # Label 5313
        ReturnValue_23: bool = EqualEqual_NameName(self.mPickupMontageSectionName, "Left")
        if not ReturnValue_23:
            goto('L5768')
        ReturnValue_19 = self.GetMesh1P()
        ReturnValue_20 = ReturnValue_19.GetAnimInstance()
        ReturnValue1_8: float = ReturnValue_20.Montage_Play(Pickup_Montage, 1, 0, 0, True)
        ReturnValue_19 = self.GetMesh1P()
        ReturnValue_20 = ReturnValue_19.GetAnimInstance()
        ReturnValue_20.Montage_JumpToSection("Right", Pickup_Montage)
        ReturnValue_19 = self.GetMesh1P()
        ReturnValue_20 = ReturnValue_19.GetAnimInstance()
        ReturnValue_24: FName = ReturnValue_20.Montage_GetCurrentSection(Pickup_Montage)
        self.mPickupMontageSectionName = ReturnValue_24
        goto(ExecutionFlow.Pop())
        # Label 5768
        ReturnValue_19 = self.GetMesh1P()
        ReturnValue_20 = ReturnValue_19.GetAnimInstance()
        ReturnValue_25: float = ReturnValue_20.Montage_Play(Pickup_Montage, 1, 0, 0, True)
        ReturnValue_19 = self.GetMesh1P()
        ReturnValue_20 = ReturnValue_19.GetAnimInstance()
        ReturnValue1_9: FName = ReturnValue_20.Montage_GetCurrentSection(Pickup_Montage)
        self.mPickupMontageSectionName = ReturnValue1_9
        goto(ExecutionFlow.Pop())
        # Label 6051
        ReturnValue_19 = self.GetMesh1P()
        ReturnValue_20 = ReturnValue_19.GetAnimInstance()
        ReturnValue_26: bool = ReturnValue_20.Montage_IsPlaying(Pickup_01_Montage)
        if not ReturnValue_26:
            goto('L6179')
        goto(ExecutionFlow.Pop())
        # Label 6179
        ReturnValue_19 = self.GetMesh1P()
        ReturnValue_20 = ReturnValue_19.GetAnimInstance()
        ReturnValue2_6: float = ReturnValue_20.Montage_Play(Pickup_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 6314
        ReturnValue_19 = self.GetMesh1P()
        ReturnValue_20 = ReturnValue_19.GetAnimInstance()
        ReturnValue3_2: float = ReturnValue_20.Montage_Play(Pickup_02_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 6449
        ReturnValue_22 = self.GetMesh3P()
        ReturnValue2_4 = ReturnValue_22.GetAnimInstance()
        ReturnValue7_2: float = ReturnValue2_4.Montage_Play(Pickup_02_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        
        Hit = None
        self.OnLanded(Ref[Hit])
        goto(ExecutionFlow.Pop())
        ReturnValue4_2: Ptr[SpringArmComponent] = self.GetSpringArmComponent()
        ReturnValue4_2.TargetArmLength = self.mTargetCameraDistance
        goto(ExecutionFlow.Pop())
        ReturnValue1_10: bool = self.UpdateRepresentation()
        goto(ExecutionFlow.Pop())
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](inController)
        bSuccess1: bool = Controller
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        self.SetupPlayerHUD(Controller)
        goto(ExecutionFlow.Pop())
        self.ReceiveUnpossessed(OldController)
        goto('L567')
        self.ReceivePossessed(NewController)
        goto('L498')
        ReturnValue3_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_C_Damage_Radiation, self, True)
        self.PPRadiationDamage.bEnabled = True
        goto(ExecutionFlow.Pop())
        ReturnValue1_11: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_C_Damage_Radiation, self, True)
        self.PPRadiationDamage.bEnabled = False
        self.mRadiationNoise.SetScalarParameterValue("amount", 0)
        self.mRadiationNoise.SetScalarParameterValue("Vignette", 0)
        goto(ExecutionFlow.Pop())
        # Label 7124
        self.ReceiveDestroyed()
        ReturnValue_27: Ptr[FGHealthComponent] = self.GetHealthComponent()
        OutputDelegate2.BindUFunction(self, TakeDamageEvent)
        ReturnValue_27.OnTakeAnyDamageDelegate.Remove(OutputDelegate2)
        ReturnValue_28: bool = self.RemoveAsRepresentation()
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mWarningPopupTimer])
        goto(ExecutionFlow.Pop())
        # Label 7285
        ReturnValue1_12: bool = self.IsLocallyControlled()
        if not ReturnValue1_12:
            goto('L7324')
        goto(ExecutionFlow.Pop())
        # Label 7324
        ReturnValue4_3: Ptr[SkeletalMeshComponent] = self.GetMesh3P()
        ReturnValue9_0: Ptr[AnimInstance] = ReturnValue4_3.GetAnimInstance()
        ReturnValue13: float = ReturnValue9_0.Montage_Play(EmoteSigns_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 7463
        ReturnValue2_7: bool = self.IsLocallyControlled()
        if not ReturnValue2_7:
            goto('L7502')
        goto(ExecutionFlow.Pop())
        
        # Label 7502
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mEmoteTimer])
        self.EmoteBuildGun.SetSkeletalMesh(BuildGun_Skl_01, True)
        self.EmoteBuildGun.K2_SetAnimInstanceClass(Anim_BuildGun)
        ReturnValue3_4: Ptr[SkeletalMeshComponent] = self.GetMesh3P()
        ReturnValue_29: bool = self.EmoteBuildGun.K2_AttachToComponent(ReturnValue3_4, "buildgun_Socket", 2, 0, 0, True)
        ReturnValue2_8: Ptr[SkeletalMeshComponent] = self.GetMesh3P()
        ReturnValue5_2: Ptr[AnimInstance] = ReturnValue2_8.GetAnimInstance()
        ReturnValue9_1: float = ReturnValue5_2.Montage_Play(BuildgunSpinEmote_01_Montage, 1, 0, 0, True)
        ReturnValue7_3: Ptr[AnimInstance] = self.EmoteBuildGun.GetAnimInstance()
        ReturnValue11: float = ReturnValue7_3.Montage_Play(BuildgunSpinEmote_01_Montage, 1, 1, 0, True)
        OutputDelegate.BindUFunction(self, ClearEmoteMesh)
        ReturnValue_30: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, ReturnValue9_1, False)
        self.mEmoteTimer = ReturnValue_30
        goto(ExecutionFlow.Pop())
        goto('L7124')
        ReturnValue_31: float = Default__GameplayStatics.GetRealTimeSeconds(self)
        self.mLastDamageTime = ReturnValue_31
        self.PlayImpactEffectSound(damageType)
        goto('L2787')
        # Label 8213
        self.ReceiveBeginPlay()
        self.Mesh.AddTickPrerequisiteActor(self)
        ReturnValue1_13: Ptr[FGHealthComponent] = self.GetHealthComponent()
        OutputDelegate2.BindUFunction(self, TakeDamageEvent)
        ReturnValue1_13.OnTakeAnyDamageDelegate.AddUnique(OutputDelegate2)
        ReturnValue_32: Ptr[MaterialInstanceDynamic] = Default__KismetMaterialLibrary.CreateDynamicMaterialInstance(self, Material_RadiationNoise, "None")
        self.mRadiationNoise = ReturnValue_32
        CastInput: TScriptInterface[BlendableInterface] = QueryInterface[BlendableInterface](self.mRadiationNoise)
        self.PPRadiationDamage.AddOrUpdateBlendable(CastInput, 1)
        self.mRadiationNoise.SetScalarParameterValue("Blend", 1)
        Component: Ptr[FGCharacterMovementComponent] = Cast[FGCharacterMovementComponent](self.CharacterMovement)
        bSuccess12: bool = Component
        if not bSuccess12:
           goto(ExecutionFlow.Pop())
        self.mFGCharacterMovementCompRef = Component
        goto(ExecutionFlow.Pop())
        goto('L8213')
        # Label 8660
        self.EventFire.ProcessMulticastDelegate()
        goto(ExecutionFlow.Pop())
        self.Multicast_PlayClap()
        goto(ExecutionFlow.Pop())
        ReturnValue3_5: bool = self.IsLocallyControlled()
        if not ReturnValue3_5:
            goto('L8734')
        goto(ExecutionFlow.Pop())
        # Label 8734
        ReturnValue1_14: Ptr[SkeletalMeshComponent] = self.GetMesh3P()
        ReturnValue3_6: Ptr[AnimInstance] = ReturnValue1_14.GetAnimInstance()
        ReturnValue6_0: float = ReturnValue3_6.Montage_Play(Clap_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 8873
        ReturnValue1_15: Ptr[SkeletalMeshComponent] = self.GetMesh1P()
        ReturnValue1_16: Ptr[AnimInstance] = ReturnValue1_15.GetAnimInstance()
        ReturnValue4_4: float = ReturnValue1_16.Montage_Play(Clap_01_Montage, 1, 0, 0, True)
        self.Server_PlayClap()
        goto(ExecutionFlow.Pop())
        # Label 9022
        self.ToggleFlashlight()
        if not self.mFlashlightOn:
            goto('L9104')
        ReturnValue7_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_FlashLight_On, self, True)
        goto(ExecutionFlow.Pop())
        # Label 9104
        ReturnValue6_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_FlashLight_Off, self, True)
        goto(ExecutionFlow.Pop())
        # Label 9158
        self.ToggleInventory()
        goto(ExecutionFlow.Pop())
        goto('L468')
        # Label 9178
        self.ToggleCodex()
        goto(ExecutionFlow.Pop())
        self.OnDisabledInputGateChanged(newValue)
        ReturnValue1_17: Ptr[Controller] = self.GetController()
        Controller2: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1_17)
        bSuccess3: bool = Controller2
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L9489")
        ExecutionFlow.Push("L9523")
        
        outHUD = None
        Default__BPFL_HudHelperBadRef.GetBPHUD(Controller2, self, Ref[outHUD])
        
        IsOpen = None
        outHUD.IsInventoryOpen(Ref[IsOpen])
        ReturnValue_33: bool = IsOpen and newValue.mInventory
        if not ReturnValue_33:
           goto(ExecutionFlow.Pop())
        self.ToggleInventory()
        goto(ExecutionFlow.Pop())
        # Label 9489
        if not newValue.mOpenCodex:
           goto(ExecutionFlow.Pop())
        self.ToggleCodex()
        goto(ExecutionFlow.Pop())
        # Label 9523
        ReturnValue1_18: bool = newValue.mFlashLight and self.mFlashlightOn
        if not ReturnValue1_18:
           goto(ExecutionFlow.Pop())
        self.Server_SetFlashlightOn(False)
        goto(ExecutionFlow.Pop())
        # Label 9596
        if not self.mFlashlightOn:
            goto('L9615')
        goto('L9022')
        # Label 9615
        ReturnValue2_9: Ptr[Controller] = self.GetController()
        Controller3: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue2_9)
        bSuccess4: bool = Controller3
        if not bSuccess4:
           goto(ExecutionFlow.Pop())
        ReturnValue_34: DisabledInputGate = Controller3.GetDisabledInputGate()
        ReturnValue_35: bool = Not_PreBool(ReturnValue_34.mFlashLight)
        if not ReturnValue_35:
           goto(ExecutionFlow.Pop())
        goto('L9022')
        # Label 9813
        ReturnValue_36: Vector = self.GetVelocity()
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_36)
        ReturnValue_37: float = Abs(Z)
        ReturnValue_38: float = ReturnValue_37 * 1.5
        ReturnValue_39: float = FClamp(ReturnValue_38, 0, 3500)
        Default__AkGameplayStatics.SetActorRTPCValue("MoveWindSpeed", ReturnValue_39, 0, self)
        goto(ExecutionFlow.Pop())
        # Label 10078
        ReturnValue4_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_Player_SpeedWind, self, True)
        self.mPlaySpeedWind = False
        goto(ExecutionFlow.Pop())
        ReturnValue1_19: bool = Not_PreBool(doLimit)
        self.bUseControllerRotationYaw = ReturnValue1_19
        ReturnValue3_7: Ptr[Controller] = self.GetController()
        ReturnValue3_7.SetIgnoreLookInput(False)
        ReturnValue3_7 = self.GetController()
        ReturnValue3_7.SetIgnoreMoveInput(doLimit)
        ReturnValue3_7 = self.GetController()
        Controller4: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue3_7)
        bSuccess6: bool = Controller4
        if not bSuccess6:
           goto(ExecutionFlow.Pop())
        DisabledInputGate.mBuildGun = doLimit
        DisabledInputGate.mDismantle = doLimit
        DisabledInputGate.mFlashLight = doLimit
        DisabledInputGate.mResourceScanner = doLimit
        DisabledInputGate.mOpenCodex = doLimit
        DisabledInputGate.mInventory = doLimit
        DisabledInputGate.mToggleMap = doLimit
        DisabledInputGate.mHotbar = doLimit
        DisabledInputGate.mJump = doLimit
        DisabledInputGate.mChat = doLimit
        DisabledInputGate.mUse = doLimit
        DisabledInputGate.mVehicleRecording = doLimit
        Controller4.SetDisabledInputGate(DisabledInputGate)
        if not doLimit:
            goto('L11070')
        ReturnValue_40: Ptr[PlayerCameraManager] = Default__GameplayStatics.GetPlayerCameraManager(self, 0)
        ReturnValue_41: Ptr[CameraModifier] = ReturnValue_40.AddNewCameraModifier(CM_RestrictedLook)
        Look: Ptr[FGCameraModifierLimitLook] = Cast[FGCameraModifierLimitLook](ReturnValue_41)
        bSuccess7: bool = Look
        if not bSuccess7:
           goto(ExecutionFlow.Pop())
        self.mLookModifier = Look
        
        OutLocation = None
        OutRotation = None
        self.GetActorEyesViewPoint(Ref[OutLocation], Ref[OutRotation])
        self.mLookModifier.SetDefaultLookRotator(OutRotation)
        goto(ExecutionFlow.Pop())
        # Label 11070
        ReturnValue1_20: bool = Default__KismetSystemLibrary.IsValid(self.mLookModifier)
        if not ReturnValue1_20:
           goto(ExecutionFlow.Pop())
        ReturnValue1_21: Ptr[PlayerCameraManager] = Default__GameplayStatics.GetPlayerCameraManager(self, 0)
        ReturnValue_42: bool = ReturnValue1_21.RemoveCameraModifier(self.mLookModifier)
        goto(ExecutionFlow.Pop())
        ReturnValue4_6: Ptr[Controller] = self.GetController()
        ReturnValue4_6.SetIgnoreLookInput(True)
        ReturnValue4_6 = self.GetController()
        ReturnValue_43: Rotator = self.mLookModifier.GetDefaultLookRotator()
        
        ReturnValue4_6.SetControlRotation(Ref[ReturnValue_43])
        self.CharacterMovement.SetMovementMode(1, 0)
        goto(ExecutionFlow.Pop())
        self.LimitLook(False)
        ReturnValue5_3: Ptr[Controller] = self.GetController()
        
        outHUD1 = None
        Default__BPFL_HudHelperBadRef.GetBPHUD(ReturnValue5_3, self, Ref[outHUD1])
        outHUD1.SetPartialPumpiMode(False)
        self.CharacterMovement.SetMovementMode(3, 0)
        ReturnValue5_3 = self.GetController()
        Controller5: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue5_3)
        bSuccess8: bool = Controller5
        if not bSuccess8:
           goto(ExecutionFlow.Pop())
        Controller5.SetDisabledInputGate(self.mLandingInputGate)
        goto(ExecutionFlow.Pop())
        self.CharacterMovement.SetMovementMode(0, 0)
        goto(ExecutionFlow.Pop())
        self.Multicast_PlatSpinEmote()
        goto(ExecutionFlow.Pop())
        # Label 11804
        ReturnValue2_10: Ptr[SkeletalMeshComponent] = self.GetMesh1P()
        ReturnValue4_7: Ptr[AnimInstance] = ReturnValue2_10.GetAnimInstance()
        ReturnValue8: float = ReturnValue4_7.Montage_Play(BuildgunSpinEmote_01_Montage, 1, 1, 0, True)
        ReturnValue6_2: Ptr[AnimInstance] = self.EmoteBuildGun.GetAnimInstance()
        ReturnValue10: float = ReturnValue6_2.Montage_Play(BuildgunSpinEmote_01_Montage, 1, 1, 0, True)
        self.Server_PlaySpinEmote()
        OutputDelegate1.BindUFunction(self, ClearEmoteMesh)
        ReturnValue1_22: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate1, ReturnValue8, False)
        self.mEmoteTimer = ReturnValue1_22
        goto(ExecutionFlow.Pop())
        goto('L7463')
        # Label 12191
        ReturnValue5_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_Player_SpeedWind, self, True)
        self.mPlaySpeedWind = True
        goto(ExecutionFlow.Pop())
        # Label 12256
        self.EmoteBuildGun.K2_SetAnimInstanceClass(Anim_BuildGun)
        ReturnValue3_8: Ptr[SkeletalMeshComponent] = self.GetMesh1P()
        ReturnValue1_23: bool = self.EmoteBuildGun.K2_AttachToComponent(ReturnValue3_8, "buildgun_Socket", 2, 0, 0, True)
        goto('L11804')
        # Label 12397
        self.EmoteBuildGun.SetSkeletalMesh(BuildGun_Skl_01, True)
        goto('L12256')
        # Label 12448
        self.EmoteBuildGun.K2_SetAnimInstanceClass(None)
        goto(ExecutionFlow.Pop())
        # Label 12486
        self.EmoteBuildGun.SetSkeletalMesh(None, True)
        goto('L12448')
        goto('L12486')
        
        # Label 12534
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mEmoteTimer])
        goto('L12397')
        goto('L3409')
        goto('L9158')
        goto('L8660')
        # Label 12596
        ReturnValue6_3: Ptr[Controller] = self.GetController()
        Controller_0: Ptr[PlayerController] = Cast[PlayerController](ReturnValue6_3)
        bSuccess9: bool = Controller_0
        if not bSuccess9:
           goto(ExecutionFlow.Pop())
        ReturnValue_44: Ptr[Widget_EmoteMenu] = Default__WidgetBlueprintLibrary.Create(self, Widget_EmoteMenu, Controller_0)
        self.mEmoteMenu = ReturnValue_44
        Default__BPHUDHelpers.PushStackWidget(Controller_0, self.mEmoteMenu, self)
        OutputDelegate3.BindUFunction(self, ShowEmote)
        self.mEmoteMenu.ShowEmote.AddUnique(OutputDelegate3)
        goto(ExecutionFlow.Pop())
        CmpSuccess: bool = EmoteIndex != 1
        if not CmpSuccess:
            goto('L13002')
        CmpSuccess = EmoteIndex != 2
        if not CmpSuccess:
            goto('L12534')
        goto(ExecutionFlow.Pop())
        # Label 13002
        ReturnValue_45: int32 = RandomIntegerInRange(0, 1000)
        ReturnValue_46: bool = EqualEqual_IntInt(ReturnValue_45, 332)
        if not ReturnValue_46:
            goto('L8873')
        ReturnValue4_8: Ptr[SkeletalMeshComponent] = self.GetMesh1P()
        ReturnValue8_0: Ptr[AnimInstance] = ReturnValue4_8.GetAnimInstance()
        ReturnValue12: float = ReturnValue8_0.Montage_Play(EmoteSigns_01_Montage, 1, 0, 0, True)
        ReturnValue_47: Ptr[Pawn] = self.GetInstigator()
        ReturnValue8_1: Ptr[Controller] = ReturnValue_47.GetController()
        Controller6: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue8_1)
        bSuccess10: bool = Controller6
        if not bSuccess10:
           goto(ExecutionFlow.Pop())
        Controller6.ClientPlayCameraAnim(EmoteSignCameraANim, 1, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        self.Server_playSignsEmote()
        goto(ExecutionFlow.Pop())
        ReturnValue_48: Vector = self.K2_GetActorLocation()
        ReturnValue_49: Vector = self.GetActorForwardVector()
        ReturnValue_50: Rotator = self.K2_GetActorRotation()
        ReturnValue_51: Vector = ReturnValue_49 * 250
        ReturnValue_52: Vector = ReturnValue_48 + ReturnValue_51
        ReturnValue_53: bool = self.K2_TeleportTo(ReturnValue_52, ReturnValue_50)
        goto(ExecutionFlow.Pop())
        self.Multicast_PlaySignsEmote()
        goto(ExecutionFlow.Pop())
        goto('L7285')
        goto('L9596')
        # Label 13692
        if not self.mPlaySpeedWind:
           goto(ExecutionFlow.Pop())
        goto('L10078')
        
        state1 = None
        self.StartIsLookedAt(byCharacter1, Ref[state1])
        Default__FGBlueprintFunctionLibrary.ShowOutline(self.HelmetMesh, 252)
        goto(ExecutionFlow.Pop())
        # Label 13779
        Default__FGBlueprintFunctionLibrary.HideOutline(self.HelmetMesh)
        goto(ExecutionFlow.Pop())
        
        state = None
        self.StopIsLookedAt(byCharacter, Ref[state])
        goto('L13779')
        # Label 13854
        if not self.mPlaySpeedWind:
            goto('L12191')
        goto('L9813')
        ReturnValue_54: bool = radiationImmunity > 0
        ReturnValue_55: float = FMin(radiationIntensity, 0.009999999776482582)
        ReturnValue_56: float = SelectFloat(ReturnValue_55, radiationIntensity, ReturnValue_54)
        Default__AkGameplayStatics.SetGlobalRTPCValue("RTPC_Hazard_Radiation", ReturnValue_56, 0)
        ReturnValue1_24: bool = radiationImmunity > 0
        ReturnValue_57: float = Ease(0.05000000074505806, 1, radiationIntensity, 6, 100, 2)
        ReturnValue1_25: float = FMin(ReturnValue_57, 0.15000000596046448)
        ReturnValue1_26: float = SelectFloat(ReturnValue1_25, ReturnValue_57, ReturnValue1_24)
        self.mRadiationNoise.SetScalarParameterValue("amount", ReturnValue1_26)
        ReturnValue1_24 = radiationImmunity > 0
        ReturnValue_57 = Ease(0.05000000074505806, 1, radiationIntensity, 6, 100, 2)
        ReturnValue1_25 = FMin(ReturnValue_57, 0.15000000596046448)
        ReturnValue1_26 = SelectFloat(ReturnValue1_25, ReturnValue_57, ReturnValue1_24)
        self.mRadiationNoise.SetScalarParameterValue("Vignette", ReturnValue1_26)
        goto(ExecutionFlow.Pop())
        goto('L236')
        # Label 14557
        Variable: Const[Transform] = Transform(Rotator(0, 0, 0, 1), Vector(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_58: Ptr[ParticleSystemComponent] = self.AddComponent("NODE_AddParticleSystemComponent-1", False, self, Ref[Variable])
        self.Hypertube_Vfx_Particle_02 = ReturnValue_58
        ReturnValue5_5: Ptr[SkeletalMeshComponent] = self.GetMesh3P()
        ReturnValue_59: FName = ReturnValue5_5.GetSocketBoneName("Hand_Socket_L")
        ReturnValue2_11: bool = self.Hypertube_Vfx_Particle_02.K2_AttachToComponent(ReturnValue5_5, ReturnValue_59, 0, 0, 0, True)
        goto(ExecutionFlow.Pop())
        self.mDeltaTime = dt
        self.HandleFlashlight()
        goto('L3784')
        # Label 14880
        ReturnValue2_12: Ptr[PlayerCameraManager] = Default__GameplayStatics.GetPlayerCameraManager(self, 0)
        ReturnValue1_27: Ptr[CameraModifier] = ReturnValue2_12.AddNewCameraModifier(CM_Slide)
        Slide: Ptr[CM_Slide] = Cast[CM_Slide](ReturnValue1_27)
        bSuccess11: bool = Slide
        if not bSuccess11:
           goto(ExecutionFlow.Pop())
        self.mSlideCameraModifier = Slide
        ReturnValue_60: Vector = self.GetActorRightVector()
        
        self.CharacterMovement.CurrentFloor.HitResult = None
        bBlockingHit = None
        bInitialOverlap = None
        Time = None
        Distance = None
        Location = None
        ImpactPoint = None
        Normal = None
        ImpactNormal = None
        PhysMat = None
        HitActor = None
        HitComponent = None
        HitBoneName = None
        HitItem = None
        FaceIndex = None
        TraceStart = None
        TraceEnd = None
        Default__GameplayStatics.BreakHitResult(Ref[self.CharacterMovement.CurrentFloor.HitResult], Ref[bBlockingHit], Ref[bInitialOverlap], Ref[Time], Ref[Distance], Ref[Location], Ref[ImpactPoint], Ref[Normal], Ref[ImpactNormal], Ref[PhysMat], Ref[HitActor], Ref[HitComponent], Ref[HitBoneName], Ref[HitItem], Ref[FaceIndex], Ref[TraceStart], Ref[TraceEnd])
        ReturnValue_61: Vector = RotateAngleAxis(ImpactNormal, 90, ReturnValue_60)
        ReturnValue_62: Rotator = Conv_VectorToRotator(ReturnValue_61)
        self.mSlideCameraModifier.SetDefaultLookRotator(ReturnValue_62)
        # Label 15450
        ReturnValue_63: TimerHandle = Default__KismetSystemLibrary.K2_SetTimer(self, "SlideVelocityUpdate", 0.10000000149011612, True)
        self.mClearSlideVelocityTimer = ReturnValue_63
        ReturnValue1_28: TimerHandle = Default__KismetSystemLibrary.K2_SetTimer(self, "SlideSpeedWindUpdate", 0.25, True)
        self.mClearSlideSpeedWindTimer = ReturnValue1_28
        ReturnValue8_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_P_LoopSlide, self, True)
        ReturnValue_64: Vector = self.Mesh.GetSocketLocation("Slide_VFX_Socket")
        ReturnValue_65: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_PlayerSliding_Sand, self.Mesh, "None", ReturnValue_64, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 1, True, 0)
        self.Sliding_Particle = ReturnValue_65
        ReturnValue4_9: TimerHandle = Default__KismetSystemLibrary.K2_SetTimer(self, "SlideVFX", 0.03999999910593033, True)
        self.mClearSlideVFXTimer = ReturnValue4_9
        goto(ExecutionFlow.Pop())
        # Label 16008
        ReturnValue2_12 = Default__GameplayStatics.GetPlayerCameraManager(self, 0)
        ReturnValue1_29: bool = ReturnValue2_12.RemoveCameraModifier(self.mSlideCameraModifier)
        self.mSlideCameraModifier = None
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mClearSlideVFXTimer])
        goto(ExecutionFlow.Pop())
        ReturnValue3_9: bool = Default__KismetSystemLibrary.IsValid(self.mSlideCameraModifier)
        if not ReturnValue3_9:
            goto('L14880')
        goto('L15450')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mClearSlideVelocityTimer])
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mClearSlideSpeedWindTimer])
        self.mCurrentSpeedWindTimer = 0
        ReturnValue11_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_P_SlideSpeedWind, self, True)
        ReturnValue9_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_P_Slide, self, True)
        goto('L16008')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mClearSlideVelocityTimer])
        ReturnValue13_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_P_Slide, self, True)
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mClearSlideVFXTimer])
        goto(ExecutionFlow.Pop())
        ReturnValue2_13: TimerHandle = Default__KismetSystemLibrary.K2_SetTimer(self, "SlideVelocityUpdate", 0.10000000149011612, True)
        self.mClearSlideVelocityTimer = ReturnValue2_13
        ReturnValue12_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_P_StartSlide, self, True)
        goto(ExecutionFlow.Pop())
        if not boostJump:
           goto(ExecutionFlow.Pop())
        ReturnValue10_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_P_JumpSlide, self, True)
        goto(ExecutionFlow.Pop())
        # Label 16814
        self.SpeedWindEvent()
        goto(ExecutionFlow.Pop())
        ReturnValue_66: bool = self.IsAliveAndWell()
        ReturnValue_67: bool = self.CharacterMovement.IsFalling()
        ReturnValue1_30: Vector = self.GetVelocity()
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(ReturnValue1_30)
        ReturnValue1_31: float = Abs(Z1)
        ReturnValue2_14: bool = ReturnValue1_31 > 1000
        ReturnValue2_15: bool = ReturnValue_67 and ReturnValue2_14
        ReturnValue3_10: bool = ReturnValue2_15 and ReturnValue_66
        if not ReturnValue3_10:
            goto('L13692')
        goto('L13854')
        goto('L9178')
        CmpSuccess_0: bool = NotEqual_ByteByte(PrevMovementMode, 0)
        if not CmpSuccess_0:
            goto('L17574')
        CmpSuccess_0 = NotEqual_ByteByte(PrevMovementMode, 1)
        if not CmpSuccess_0:
            goto('L17574')
        CmpSuccess_0 = NotEqual_ByteByte(PrevMovementMode, 2)
        if not CmpSuccess_0:
            goto('L17574')
        CmpSuccess_0 = NotEqual_ByteByte(PrevMovementMode, 3)
        if not CmpSuccess_0:
            goto('L17574')
        CmpSuccess_0 = NotEqual_ByteByte(PrevMovementMode, 4)
        if not CmpSuccess_0:
            goto('L17574')
        CmpSuccess_0 = NotEqual_ByteByte(PrevMovementMode, 5)
        if not CmpSuccess_0:
            goto('L17574')
        CmpSuccess_0 = NotEqual_ByteByte(PrevMovementMode, 6)
        if not CmpSuccess_0:
            goto('L17460')
        goto(ExecutionFlow.Pop())
        # Label 17460
        ReturnValue1_32: uint8 = Default__KismetNodeHelperLibrary.GetValidValue(ECustomMovementMode, PrevCustomMode)
        CmpSuccess_1: bool = NotEqual_ByteByte(ReturnValue1_32, 0)
        if not CmpSuccess_1:
            goto('L17574')
        goto(ExecutionFlow.Pop())
        # Label 17574
        CmpSuccess_2: bool = NotEqual_ByteByte(NewMovementMode, 0)
        if not CmpSuccess_2:
            goto('L18976')
        CmpSuccess_2 = NotEqual_ByteByte(NewMovementMode, 1)
        if not CmpSuccess_2:
            goto('L18976')
        CmpSuccess_2 = NotEqual_ByteByte(NewMovementMode, 2)
        if not CmpSuccess_2:
            goto('L18976')
        CmpSuccess_2 = NotEqual_ByteByte(NewMovementMode, 3)
        if not CmpSuccess_2:
            goto('L18976')
        CmpSuccess_2 = NotEqual_ByteByte(NewMovementMode, 4)
        if not CmpSuccess_2:
            goto('L18976')
        CmpSuccess_2 = NotEqual_ByteByte(NewMovementMode, 5)
        if not CmpSuccess_2:
            goto('L18976')
        CmpSuccess_2 = NotEqual_ByteByte(NewMovementMode, 6)
        if not CmpSuccess_2:
            goto('L17890')
        goto(ExecutionFlow.Pop())
        # Label 17890
        ReturnValue_68: uint8 = Default__KismetNodeHelperLibrary.GetValidValue(ECustomMovementMode, NewCustomMode)
        CmpSuccess_3: bool = NotEqual_ByteByte(ReturnValue_68, 2)
        if not CmpSuccess_3:
            goto('L18004')
        goto(ExecutionFlow.Pop())
        # Label 18004
        Variable2: Const[Transform] = Transform(Rotator(0, 0, 0, 1), Vector(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue2_16: Ptr[StaticMeshComponent] = self.AddComponent("NODE_AddStaticMeshComponent-0", False, self, Ref[Variable2])
        self.mHypertube_VfxCap = ReturnValue2_16
        ReturnValue5_5 = self.GetMesh3P()
        ReturnValue2_17: FName = ReturnValue5_5.GetSocketBoneName("PelvisCenterSocket")
        ReturnValue4_10: bool = self.mHypertube_VfxCap.K2_AttachToComponent(ReturnValue5_5, ReturnValue2_17, 0, 0, 0, True)
        
        SweepHitResult = None
        self.mHypertube_VfxCap.K2_SetRelativeRotation(Rotator::FromPitchYawRoll(0, 0, -90), False, False, Ref[SweepHitResult])
        ExecutionFlow.Push("L14557")
        Variable1: Const[Transform] = Transform(Rotator(0, 0, 0, 1), Vector(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue1_33: Ptr[ParticleSystemComponent] = self.AddComponent("NODE_AddParticleSystemComponent-0", False, self, Ref[Variable1])
        self.Hypertube_Vfx_Particle_01 = ReturnValue1_33
        ReturnValue5_5 = self.GetMesh3P()
        ReturnValue1_34: FName = ReturnValue5_5.GetSocketBoneName("Hand_Socket_R")
        ReturnValue3_11: bool = self.Hypertube_Vfx_Particle_01.K2_AttachToComponent(ReturnValue5_5, ReturnValue1_34, 0, 0, 0, True)
        ReturnValue2_18: Vector = self.K2_GetActorLocation()
        ReturnValue1_35: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_EnterTube, ReturnValue2_18, Rotator::FromPitchYawRoll(0, 0, 0))
        ReturnValue6_4: bool = self.IsLocallyControlled()
        if not ReturnValue6_4:
            goto('L18918')
        ReturnValue16: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_AmbienceTube, self, True)
        # Label 18810
        ReturnValue3_12: TimerHandle = Default__KismetSystemLibrary.K2_SetTimer(self, "TubeTravelSpeedUpdate", 0.05000000074505806, True)
        self.mClearTubeTravelUpdateTimer = ReturnValue3_12
        goto(ExecutionFlow.Pop())
        # Label 18918
        ReturnValue15: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_AmbienceTube_Client, self, True)
        goto('L18810')
        # Label 18976
        ReturnValue2_19: bool = Default__KismetSystemLibrary.IsValid(self.mHypertube_VfxCap)
        if not ReturnValue2_19:
           goto(ExecutionFlow.Pop())
        self.Hypertube_Vfx_Particle_01.K2_DestroyComponent(self)
        self.Hypertube_Vfx_Particle_02.K2_DestroyComponent(self)
        self.mHypertube_VfxCap.K2_DestroyComponent(self)
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mClearTubeTravelUpdateTimer])
        ReturnValue14: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_AllSoundsInsideTube, self, True)
        ReturnValue1_36: Vector = self.K2_GetActorLocation()
        ReturnValue_69: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_ExitTube, ReturnValue1_36, Rotator::FromPitchYawRoll(0, 0, 0))
        ReturnValue2_20: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_TurbineWindTube, self.mLastFrameEndPosTube, self.mLastFrameEndRotTube)
        goto(ExecutionFlow.Pop())
        goto('L16814')
        goto(ExecutionFlow.Pop())
        Variable3: Key = Key1
        ReturnValue4_11: bool = Default__KismetSystemLibrary.IsValid(self.mEmoteMenu)
        if not ReturnValue4_11:
            goto('L12596')
        goto(ExecutionFlow.Pop())
        Variable3 = Key2
        goto('L3590')
    

    def EventFire__DelegateSignature(self):
        pass
    

    def EventScroll__DelegateSignature(self, index: int32):
        pass
    

    def EventScrollDown__DelegateSignature(self):
        pass
    

    def EventScrollUp__DelegateSignature(self):
        pass
    
