
from codegen.ue4_stub import *

from Script.Engine import ReceiveDestroyed
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.BP_Locomotive import ExecuteUbergraph_BP_Locomotive.K2Node_InputKeyEvent_Key1
from Script.InputCore import Key
from Script.CoreUObject import Rotator
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.BP_Locomotive import ExecuteUbergraph_BP_Locomotive.K2Node_Event_OldController
from Script.Engine import FormatArgumentData
from Script.FactoryGame import GetDisabledInputGate
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.FactoryGame import IsInputDisabled
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.BP_Locomotive import ExecuteUbergraph_BP_Locomotive.K2Node_InputKeyEvent_Key
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import FlushNetDormancy
from Script.Engine import ReceiveUnpossessed
from Script.FactoryGame import GetLocomotiveMovementComponent
from Script.Engine import RetriggerableDelay
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.FactoryGame import LostSignificance
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.BP_Locomotive import ExecuteUbergraph_BP_Locomotive.K2Node_Event_newColor
from Script.Engine import K2_SetRelativeRotation
from Script.FactoryGame import SetThrottleInput
from Script.CoreUObject import LinearColor
from Script.Engine import FClamp
from Script.FactoryGame import FGPlayerController
from Script.Engine import Controller
from Script.Engine import GetInputAxisValue
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.BP_Locomotive import ExecuteUbergraph_BP_Locomotive.K2Node_Event_NewController
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Stop_Train_Rework_Horn_02 import Stop_Train_Rework_Horn_02
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.BP_Locomotive import ExecuteUbergraph_BP_Locomotive.K2Node_Event_DeltaSeconds
from Script.Engine import HUD
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.BP_Locomotive import ExecuteUbergraph_BP_Locomotive.K2Node_InputActionEvent_Key2
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.BP_Locomotive import ExecuteUbergraph_BP_Locomotive.K2Node_InputActionEvent_Key3
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.BP_Locomotive import ExecuteUbergraph_BP_Locomotive
from Script.FactoryGame import DisabledInputGate
from Script.Engine import GetHUD
from Script.FactoryGame import GetTrainName
from Script.FactoryGame import FGActorRepresentationManager
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Play_Train_Rework_Horn_01 import Play_Train_Rework_Horn_01
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import RandomInteger
from Script.FactoryGame import FGLocomotive
from Script.Engine import Abs
from Script.FactoryGame import FGTrain
from Script.AkAudio import AkComponent
from Script.FactoryGame import GainedSignificance
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.BP_Locomotive import ExecuteUbergraph_BP_Locomotive.K2Node_InputAxisEvent_AxisValue
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Stop_Train_Rework_Horn_01 import Stop_Train_Rework_Horn_01
from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Script.Engine import ReceivePossessed
from Script.FactoryGame import CreateAndAddNewRepresentation
from Script.Engine import K2_SetTimerDelegate
from Script.FactoryGame import FGPlayerState
from Script.Engine import TextIsEmpty
from Script.Engine import LatentActionInfo
from Script.Engine import HasAuthority
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.BP_Locomotive import ExecuteUbergraph_BP_Locomotive.K2Node_InputActionEvent_Key
from Script.FactoryGame import Get
from Script.Engine import GetController
from Script.FactoryGame import SetReverserInput
from Script.Engine import SetScalarParameterValueOnMaterials
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_Icon_train import MapCompass_Icon_train
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.BP_Locomotive import ExecuteUbergraph_BP_Locomotive.K2Node_InputAxisEvent_AxisValue1
from Script.Engine import CurveFloat
from Script.FactoryGame import GetTrain
from Script.Engine import BreakRotator
from Script.FactoryGame import FGLocomotiveMovementComponent
from Script.FactoryGame import IsMoving
from Script.Engine import Format
from Script.Engine import ClampAngle
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Locomotive_Menu import Widget_Locomotive_Menu
from Script.Engine import MakeRotator
from Script.FactoryGame import GetRemoteCallObjectOfClass
from Script.FactoryGame import RemoveRepresentationOfActor
from Game.FactoryGame.Character.Player.BP_RemoteCallObject import BP_RemoteCallObject
from Script.FactoryGame import SetSteeringInput
from Script.FactoryGame import GetReverser
from Script.FactoryGame import SetAirBrakeInput
from Script.Engine import ReceiveBeginPlay
from Script.Engine import Not_PreBool
from Script.Engine import ReceiveTick
from Script.FactoryGame import Default__FGActorRepresentationManager
from Script.Engine import NotEqual_TextText
from Script.FactoryGame import GetNametagColor
from Script.FactoryGame import UpdateRepresentation
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.BP_Locomotive import ExecuteUbergraph_BP_Locomotive.K2Node_InputActionEvent_Key1
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Rework.Play_Train_Rework_Horn_02 import Play_Train_Rework_Horn_02
from Script.CoreUObject import Vector
from Script.FactoryGame import FGHUD
from Script.Engine import SelectInt
from Script.Engine import K2_GetActorLocation
from Script.Engine import SetFloatParameter
from Script.FactoryGame import GetForwardSpeed
from Script.Engine import GetFloatValue

class BP_Locomotive(FGLocomotive):
    mIsThrottleZero: bool
    mMapText: FText = NSLOCTEXT("", "BBD4BB844C50A5194A59169DCD9BAD4D", "Locomotive")
    mDeltaSeconds: float
    mBrakeTime: float
    mHUDClass: TSubclassOf[UserWidget] = NewObject[Widget_Locomotive_HUD]()
    mPossessed: bool
    mEngineCurve: Ptr[CurveFloat] = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/Animation/LocomotiveEngineCurve.LocomotiveEngineCurve')
    mAllowEndHonk: bool
    mPlayHonkAlternative: bool
    mCachedName: FText
    mPowerConsumption = Namespace(Max=110, Min=25)
    mSlidingShoe = Namespace(ObjectClass='/Script/FactoryGame.FGPowerConnectionComponent', ObjectFlags=2883617, ObjectName='SlidingShoe', mIsHiddenConnection=True)
    mPowerInfo = Namespace(ObjectClass='/Script/FactoryGame.FGPowerInfoComponent', ObjectFlags=2883617, ObjectName='powerInfo')
    mVehicleMovement = Namespace(ObjectClass='/Script/FactoryGame.FGLocomotiveMovementComponent', ObjectFlags=2883617, ObjectName='MovementComp', bReplicates=True, mAirBrakeInputRate={'RiseRate': 2, 'FallRate': 2}, mChassisHeight=800, mChassisWidth=450, mCouplerSetups=[{'BoneName': 'connector_front', 'Length': 115}, {'BoneName': 'connector_back', 'Length': 115}], mCurvatureResistanceCoefficient=4.3000000005122274e-05, mDynamicBrakeInputRate={'RiseRate': 1, 'FallRate': 1}, mDynamicBrakeVelocityThreshold=30, mDynamicBrakingEffortCurve={'EditorCurveData': {'Keys': [{'InterpMode': 2, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 0, 'Value': 4500, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 1, 'TangentWeightMode': 0, 'Time': 10, 'Value': 1500, 'ArriveTangent': -82.04620361328125, 'ArriveTangentWeight': 0, 'LeaveTangent': -82.04620361328125, 'LeaveTangentWeight': 0}, {'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 25, 'Value': 1000, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, 'ExternalCurve': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/Curve_TrainBrake.Curve_TrainBrake'}}, mMass=300000, mMaxAirBrakingEffort=900, mThrottleInputRate={'RiseRate': 0.20000000298023224, 'FallRate': 2}, mTractiveEffortCurve={'EditorCurveData': {'Keys': [{'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 0, 'Value': 1500, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 70, 'Value': 1500, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 130, 'Value': 800, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 200, 'Value': 500, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 240, 'Value': 6.16668701171875, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, 'ExternalCurve': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/Curve_TrainAcceleration.Curve_TrainAcceleration'}}, mWheelsetSetups=[{'BoneName': 'wheelbase_front', 'CanSwivel': True}, {'BoneName': 'wheelbase_back', 'CanSwivel': True}])
    mLength = 1600
    mDisplayName = NSLOCTEXT("", "DFFC173544A8BBC2E259E09C3FE022E5", "Electric Locomotive")
    mDescription = NSLOCTEXT("", "B6E85D4F44F164F84706ABBB0D112199", "The Locomotive is used to move Freight Cars from station to station.\r\nRequires between 25-110 MW of power to drive. \r\nMust be built on railway.\r\n\r\nNicknamed \'Leif\' by FICSIT pioneers because of its reliability.")
    mHologramClass = NewObject[Holo_Locomotive]()
    mMesh = Namespace(AnimClass='/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/BP_LocomotiveAnim.BP_LocomotiveAnim_C', BodyInstance={'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 7360.171875, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='VehicleMesh', SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/Mesh/Locomotive.Locomotive'}, bAllowCullDistanceVolume=False, bGenerateOverlapEvents=True)
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True)
    mDisabledByWaterLocations = [{'X': 0, 'Y': 0, 'Z': 0}]
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mConstructSound = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Train/-Shared/Audio/Play_F_TrainTrack_Construct.Play_F_TrainTrack_Construct')
    mSubmergedAngularDamping = 6
    mSubmergedLinearDamping = 15
    mSubmergedBouyantForce = 1000
    mAddToSignificanceManager = True
    mSignificanceRange = 30000
    mShouldAttachDriver = True
    mDriverExitOffset = Namespace(X=0, Y=300, Z=0)
    RootComponent = Namespace(AnimClass='/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/BP_LocomotiveAnim.BP_LocomotiveAnim_C', BodyInstance={'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 7360.171875, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='VehicleMesh', SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/Mesh/Locomotive.Locomotive'}, bAllowCullDistanceVolume=False, bGenerateOverlapEvents=True)
    
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
    

    def GetActorFogOfWarRevealRadius(self):
        ReturnValue = 0
    

    def GetActorFogOfWarRevealType(self):
        ReturnValue = 0
    

    def GetActorRepresentationColor(self):
        if not self.mPossessed:
            goto('L175')
        State: Ptr[FGPlayerState] = Cast[FGPlayerState](self.PlayerState)
        bSuccess: bool = State
        if not bSuccess:
            goto('L175')
        ReturnValue: LinearColor = State.GetNametagColor()
        ReturnValue_0: LinearColor = ReturnValue
        goto('L257')
        
        Text = None
        Graphics = None
        # Label 175
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue_0 = Graphics
    

    def GetActorRepresentationText(self):
        ReturnValue: Ptr[FGTrain] = self.GetTrain()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L949')
        ReturnValue = self.GetTrain()
        ReturnValue1: Ptr[FGTrain] = self.GetTrain()
        ReturnValue_1: FText = ReturnValue1.GetTrainName()
        FormatArgumentData.ArgumentName = "B"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_1
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        ReturnValue1_0: FText = ReturnValue.GetTrainName()
        
        ReturnValue_2: bool = Default__KismetTextLibrary.TextIsEmpty(Ref[ReturnValue1_0])
        FormatArgumentData1.ArgumentName = "A"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = self.mMapText
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        ReturnValue_3: bool = Not_PreBool(ReturnValue_2)
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        Variable: bool = ReturnValue_3
        ReturnValue_4: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 822, 'Value': '{A}: {B}'}", Array)
        
        switch = {
            False: self.mMapText,
            True: ReturnValue_4
        }
        ReturnValue_5: FText = switch.get(Variable, None)
    

    def GetActorRepresentationTexture(self):
        ReturnValue = MapCompass_Icon_train
    

    def GetActorRepresentationType(self):
        ReturnValue = 12
    

    def GetActorShouldShowInCompass(self):
        ReturnValue = True
    

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
        ReturnValue: Vector = self.K2_GetActorLocation()
        ReturnValue_0: Vector = ReturnValue
    

    def GetRealActorRotation(self):
        ReturnValue = Rotator::FromPitchYawRoll(0, 0, 0)
    

    def IsActorStatic(self):
        ReturnValue = False
    

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
    

    def InpActEvt_Use_K2Node_InputActionEvent_3(self, Key: Key):
        ExecuteUbergraph_BP_Locomotive.K2Node_InputActionEvent_Key3 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Locomotive(15)
    

    def InpActEvt_Jump_Drift_K2Node_InputActionEvent_2(self, Key: Key):
        ExecuteUbergraph_BP_Locomotive.K2Node_InputActionEvent_Key2 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Locomotive(4882)
    

    def InpActEvt_Jump_Drift_K2Node_InputActionEvent_1(self, Key: Key):
        ExecuteUbergraph_BP_Locomotive.K2Node_InputActionEvent_Key1 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Locomotive(4802)
    

    def InpActEvt_ResourceScanner_ToggleVehicleRecording_K2Node_InputActionEvent_0(self, Key: Key):
        ExecuteUbergraph_BP_Locomotive.K2Node_InputActionEvent_Key = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Locomotive(4016)
    

    def InpActEvt_LeftMouseButton_K2Node_InputKeyEvent_1(self, Key: Key):
        ExecuteUbergraph_BP_Locomotive.K2Node_InputKeyEvent_Key1 = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Locomotive(1020)
    

    def InpActEvt_LeftMouseButton_K2Node_InputKeyEvent_0(self, Key: Key):
        ExecuteUbergraph_BP_Locomotive.K2Node_InputKeyEvent_Key = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Locomotive(4373)
    

    def SetActorRepresentationColor(self):
        ExecuteUbergraph_BP_Locomotive.K2Node_Event_newColor = NewColor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Locomotive(2752)
    

    def ReceiveTick(self):
        ExecuteUbergraph_BP_Locomotive.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Locomotive(2753)
    

    def UpdateCamera(self):
        self.ExecuteUbergraph_BP_Locomotive(3301)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_Locomotive(3306)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_BP_Locomotive(3653)
    

    def Server_Leave(self):
        self.ExecuteUbergraph_BP_Locomotive(3688)
    

    def InpAxisEvt_MoveRight_K2Node_InputAxisEvent_0(self, AxisValue: float):
        ExecuteUbergraph_BP_Locomotive.K2Node_InputAxisEvent_AxisValue1 = AxisValue #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Locomotive(3714)
    

    def InpAxisEvt_MoveForward_K2Node_InputAxisEvent_1(self, AxisValue: float):
        ExecuteUbergraph_BP_Locomotive.K2Node_InputAxisEvent_AxisValue = AxisValue #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Locomotive(3719)
    

    def ReceiveUnpossessed(self):
        ExecuteUbergraph_BP_Locomotive.K2Node_Event_OldController = OldController #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Locomotive(4834)
    

    def ReceivePossessed(self):
        ExecuteUbergraph_BP_Locomotive.K2Node_Event_NewController = NewController #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_Locomotive(4858)
    

    def MultiCast_TrainHorn_01(self):
        self.ExecuteUbergraph_BP_Locomotive(4914)
    

    def MultiCast_TrainHorn_01_Stop(self):
        self.ExecuteUbergraph_BP_Locomotive(5007)
    

    def MultiCast_TrainHorn_02(self):
        self.ExecuteUbergraph_BP_Locomotive(5100)
    

    def MultiCast_TrainHorn_02_Stop(self):
        self.ExecuteUbergraph_BP_Locomotive(5193)
    

    def Server_Horn_01(self):
        self.ExecuteUbergraph_BP_Locomotive(5286)
    

    def Server_Horn_01_Stop(self):
        self.ExecuteUbergraph_BP_Locomotive(5301)
    

    def Server_Horn_02(self):
        self.ExecuteUbergraph_BP_Locomotive(5316)
    

    def Server_Horn_02_Stop(self):
        self.ExecuteUbergraph_BP_Locomotive(5331)
    

    def OnNameChanged(self):
        self.ExecuteUbergraph_BP_Locomotive(5346)
    

    def UpdateTrainName(self):
        self.ExecuteUbergraph_BP_Locomotive(5468)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_BP_Locomotive(5704)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_BP_Locomotive(6015)
    

    def ExecuteUbergraph_BP_Locomotive(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue: Ptr[Controller] = self.GetController()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_0: DisabledInputGate = Controller.GetDisabledInputGate()
        ReturnValue4: bool = Not_PreBool(ReturnValue_0.mUse)
        if not ReturnValue4:
           goto(ExecutionFlow.Pop())
        self.Server_Leave()
        goto(ExecutionFlow.Pop())
        # Label 223
        ReturnValue1: Ptr[BP_RemoteCallObject] = Controller3.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue4_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        if not ReturnValue4_0:
            goto('L437')
        ReturnValue1 = Controller3.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue1.Client_AddPawnHUD(self.mHUDClass, self)
        goto(ExecutionFlow.Pop())
        # Label 437
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 223, UUID = -1829694571, ExecutionFunction = "ExecuteUbergraph_BP_Locomotive", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 514
        self.FlushNetDormancy()
        self.mPossessed = True
        ReturnValue1_0: bool = self.UpdateRepresentation()
        Controller3: Ptr[FGPlayerController] = Cast[FGPlayerController](NewController)
        bSuccess4: bool = Controller3
        if not bSuccess4:
           goto(ExecutionFlow.Pop())
        goto('L223')
        # Label 639
        self.FlushNetDormancy()
        self.mPossessed = False
        ReturnValue_1: bool = self.UpdateRepresentation()
        Controller2: Ptr[FGPlayerController] = Cast[FGPlayerController](OldController)
        bSuccess3: bool = Controller2
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: Ptr[BP_RemoteCallObject] = Controller2.GetRemoteCallObjectOfClass(BP_RemoteCallObject)
        ReturnValue_2.Client_RemovePawnHUD()
        goto(ExecutionFlow.Pop())
        self.mAllowEndHonk = False
        goto(ExecutionFlow.Pop())
        self.mAllowEndHonk = False
        goto(ExecutionFlow.Pop())
        # Label 871
        self.mIsThrottleZero = True
        # Label 882
        ReturnValue_3: int32 = self.mVehicleMovement.GetReverser()
        ReturnValue_4: float = ReturnValue_3 * AxisValue
        self.mVehicleMovement.SetThrottleInput(ReturnValue_4)
        goto(ExecutionFlow.Pop())
        Variable1: Key = Key1
        if not self.mPlayHonkAlternative:
            goto('L1150')
        self.mPlayHonkAlternative = False
        if not self.mAllowEndHonk:
           goto(ExecutionFlow.Pop())
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_Train_Rework_Horn_02, self, True)
        self.Server_Horn_02_Stop()
        goto(ExecutionFlow.Pop())
        # Label 1150
        if not self.mAllowEndHonk:
           goto(ExecutionFlow.Pop())
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_Train_Rework_Horn_01, self, True)
        self.Server_Horn_01_Stop()
        goto(ExecutionFlow.Pop())
        # Label 1228
        ReturnValue_5: Ptr[FGTrain] = self.GetTrain()
        ReturnValue_6: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_5)
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        ReturnValue_5 = self.GetTrain()
        ReturnValue_7: bool = ReturnValue_5.IsInputDisabled()
        ReturnValue_8: bool = Not_PreBool(ReturnValue_7)
        if not ReturnValue_8:
           goto(ExecutionFlow.Pop())
        self.mVehicleMovement.SetAirBrakeInput(1)
        goto(ExecutionFlow.Pop())
        # Label 1448
        ReturnValue1_1: Ptr[FGTrain] = self.GetTrain()
        ReturnValue1_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_1)
        if not ReturnValue1_2:
           goto(ExecutionFlow.Pop())
        ReturnValue1_1 = self.GetTrain()
        ReturnValue1_3: bool = ReturnValue1_1.IsInputDisabled()
        ReturnValue1_4: bool = Not_PreBool(ReturnValue1_3)
        if not ReturnValue1_4:
           goto(ExecutionFlow.Pop())
        self.mVehicleMovement.SetAirBrakeInput(0)
        goto(ExecutionFlow.Pop())
        # Label 1668
        self.ReceiveTick(self.mDeltaSeconds)
        self.UpdateCamera()
        ReturnValue_9: Ptr[FGLocomotiveMovementComponent] = self.GetLocomotiveMovementComponent()
        ReturnValue_10: float = ReturnValue_9.GetForwardSpeed()
        ReturnValue1_5: float = Abs(ReturnValue_10)
        ReturnValue_11: float = ReturnValue1_5 / 3000
        ReturnValue1_6: float = ReturnValue_11 * 15
        ReturnValue_12: float = self.mEngineCurve.GetFloatValue(ReturnValue1_6)
        self.mMesh.SetScalarParameterValueOnMaterials("GlowBoost", ReturnValue_12)
        ReturnValue5: bool = Default__KismetSystemLibrary.IsValid(self.EngineRunning_01)
        if not ReturnValue5:
           goto(ExecutionFlow.Pop())
        ReturnValue1_7: Ptr[FGLocomotiveMovementComponent] = self.GetLocomotiveMovementComponent()
        ReturnValue1_8: float = ReturnValue1_7.GetForwardSpeed()
        ReturnValue2_0: float = Abs(ReturnValue1_8)
        ReturnValue1_9: float = ReturnValue2_0 / 3000
        ReturnValue2_1: float = ReturnValue1_9 * 1.2999999523162842
        ReturnValue_13: float = FClamp(ReturnValue2_1, 0, 1)
        self.EngineRunning_02.SetFloatParameter("Spawn", ReturnValue_13)
        self.EngineRunning_01.SetFloatParameter("Spawn", ReturnValue_13)
        goto(ExecutionFlow.Pop())
        # Label 2413
        self.mVehicleMovement.SetAirBrakeInput(0)
        # Label 2450
        ReturnValue1_10: bool = self.mVehicleMovement.IsMoving()
        ReturnValue6: bool = Not_PreBool(ReturnValue1_10)
        if not ReturnValue6:
            goto('L882')
        ReturnValue_14: bool = AxisValue > 0
        ReturnValue_15: int32 = SelectInt(1, -1, ReturnValue_14)
        self.mVehicleMovement.SetReverserInput(ReturnValue_15)
        goto('L882')
        # Label 2662
        ReturnValue_16: bool = self.mVehicleMovement.IsMoving()
        ReturnValue2_2: bool = Not_PreBool(ReturnValue_16)
        if not ReturnValue2_2:
            goto('L2450')
        goto('L2413')
        goto(ExecutionFlow.Pop())
        self.mDeltaSeconds = DeltaSeconds
        goto('L1668')
        # Label 2785
        ReturnValue_17: bool = self.IsLocallyControlled()
        if not ReturnValue_17:
           goto(ExecutionFlow.Pop())
        ReturnValue_18: float = self.GetInputAxisValue("Turn")
        ReturnValue1_11: float = self.GetInputAxisValue("LookUp")
        ReturnValue_19: float = ReturnValue1_11 * -1
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(self.SpringArm.RelativeRotation, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_20: float = Yaw + ReturnValue_18
        ReturnValue1_12: float = ReturnValue_19 + Pitch
        ReturnValue_21: float = ClampAngle(ReturnValue_20, -179, 179)
        ReturnValue1_13: float = ClampAngle(ReturnValue1_12, -89, 89)
        ReturnValue_22: Rotator = MakeRotator(0, ReturnValue1_13, ReturnValue_21)
        
        SweepHitResult = None
        self.SpringArm.K2_SetRelativeRotation(ReturnValue_22, False, False, Ref[SweepHitResult])
        goto(ExecutionFlow.Pop())
        goto('L2785')
        self.ReceiveBeginPlay()
        ReturnValue_23: bool = self.AddAsRepresentation()
        OutputDelegate.BindUFunction(self, UpdateTrainName)
        ReturnValue_24: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.5, True)
        goto(ExecutionFlow.Pop())
        # Label 3429
        ReturnValue2_3: Ptr[FGTrain] = self.GetTrain()
        ReturnValue2_4: bool = Default__KismetSystemLibrary.IsValid(ReturnValue2_3)
        if not ReturnValue2_4:
           goto(ExecutionFlow.Pop())
        ReturnValue2_3 = self.GetTrain()
        ReturnValue2_5: bool = ReturnValue2_3.IsInputDisabled()
        ReturnValue3_0: bool = Not_PreBool(ReturnValue2_5)
        if not ReturnValue3_0:
           goto(ExecutionFlow.Pop())
        self.mVehicleMovement.SetSteeringInput(AxisValue1)
        goto(ExecutionFlow.Pop())
        self.ReceiveDestroyed()
        ReturnValue_25: bool = self.RemoveAsRepresentation()
        goto(ExecutionFlow.Pop())
        ReturnValue_26: bool = self.DriverLeave(False)
        goto(ExecutionFlow.Pop())
        goto('L3429')
        ReturnValue3_1: Ptr[FGTrain] = self.GetTrain()
        ReturnValue3_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue3_1)
        if not ReturnValue3_2:
           goto(ExecutionFlow.Pop())
        ReturnValue3_1 = self.GetTrain()
        ReturnValue3_3: bool = ReturnValue3_1.IsInputDisabled()
        ReturnValue7: bool = Not_PreBool(ReturnValue3_3)
        if not ReturnValue7:
           goto(ExecutionFlow.Pop())
        ReturnValue_27: float = Abs(AxisValue)
        ReturnValue1_14: bool = ReturnValue_27 > 0.10000000149011612
        if not ReturnValue1_14:
            goto('L871')
        if not self.mIsThrottleZero:
            goto('L882')
        self.mIsThrottleZero = False
        goto('L2662')
        ReturnValue1_15: Ptr[Controller] = self.GetController()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1_15)
        bSuccess1: bool = Controller1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue1_16: DisabledInputGate = Controller1.GetDisabledInputGate()
        ReturnValue5_0: bool = Not_PreBool(ReturnValue1_16.mVehicleRecording)
        if not ReturnValue5_0:
           goto(ExecutionFlow.Pop())
        ReturnValue_28: Ptr[HUD] = Controller1.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_28)
        bSuccess2: bool = AsFGHUD
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        AsFGHUD.OpenInteractUI(Widget_Locomotive_Menu, self)
        goto(ExecutionFlow.Pop())
        Variable1 = Key
        ReturnValue_29: int32 = RandomInteger(100)
        ReturnValue_30: bool = ReturnValue_29 > 1
        if not ReturnValue_30:
            goto('L4636')
        self.mAllowEndHonk = True
        ReturnValue1_17: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_Train_Rework_Horn_01, self, True)
        self.Server_Horn_01()
        Default__KismetSystemLibrary.RetriggerableDelay(self, 4, LatentActionInfo(Linkage = 847, UUID = -978469378, ExecutionFunction = "ExecuteUbergraph_BP_Locomotive", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 4636
        self.mAllowEndHonk = True
        ReturnValue_31: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_Train_Rework_Horn_02, self, True)
        self.Server_Horn_02()
        self.mPlayHonkAlternative = True
        Default__KismetSystemLibrary.RetriggerableDelay(self, 1.649999976158142, LatentActionInfo(Linkage = 859, UUID = 972325534, ExecutionFunction = "ExecuteUbergraph_BP_Locomotive", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        Variable: Key = Key1
        goto('L1228')
        self.ReceiveUnpossessed(OldController)
        goto('L639')
        self.ReceivePossessed(NewController)
        goto('L514')
        Variable = Key2
        goto('L1448')
        ReturnValue1_18: bool = self.IsLocallyControlled()
        if not ReturnValue1_18:
            goto('L4953')
        goto(ExecutionFlow.Pop())
        # Label 4953
        ReturnValue5_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_Train_Rework_Horn_01, self, True)
        goto(ExecutionFlow.Pop())
        ReturnValue2_6: bool = self.IsLocallyControlled()
        if not ReturnValue2_6:
            goto('L5046')
        goto(ExecutionFlow.Pop())
        # Label 5046
        ReturnValue4_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_Train_Rework_Horn_01, self, True)
        goto(ExecutionFlow.Pop())
        ReturnValue3_4: bool = self.IsLocallyControlled()
        if not ReturnValue3_4:
            goto('L5139')
        goto(ExecutionFlow.Pop())
        # Label 5139
        ReturnValue6_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_Train_Rework_Horn_02, self, True)
        goto(ExecutionFlow.Pop())
        ReturnValue4_2: bool = self.IsLocallyControlled()
        if not ReturnValue4_2:
            goto('L5232')
        goto(ExecutionFlow.Pop())
        # Label 5232
        ReturnValue7_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_Train_Rework_Horn_02, self, True)
        goto(ExecutionFlow.Pop())
        self.MultiCast_TrainHorn_01()
        goto(ExecutionFlow.Pop())
        self.MultiCast_TrainHorn_01_Stop()
        goto(ExecutionFlow.Pop())
        self.MultiCast_TrainHorn_02()
        goto(ExecutionFlow.Pop())
        self.MultiCast_TrainHorn_02_Stop()
        goto(ExecutionFlow.Pop())
        ReturnValue4_3: Ptr[FGTrain] = self.GetTrain()
        ReturnValue_32: FText = ReturnValue4_3.GetTrainName()
        self.mCachedName = ReturnValue_32
        ReturnValue2_7: bool = self.UpdateRepresentation()
        goto(ExecutionFlow.Pop())
        ReturnValue5_2: Ptr[FGTrain] = self.GetTrain()
        ReturnValue6_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue5_2)
        if not ReturnValue6_1:
           goto(ExecutionFlow.Pop())
        ReturnValue5_2 = self.GetTrain()
        ReturnValue1_19: FText = ReturnValue5_2.GetTrainName()
        
        ReturnValue_33: bool = Default__KismetTextLibrary.NotEqual_TextText(Ref[self.mCachedName], Ref[ReturnValue1_19])
        if not ReturnValue_33:
           goto(ExecutionFlow.Pop())
        self.OnNameChanged()
        goto(ExecutionFlow.Pop())
        self.GainedSignificance()
        self.EngineRunning_01.Activate(False)
        self.EngineRunning_01.SetComponentTickEnabled(True)
        self.EngineRunning_02.Activate(False)
        self.EngineRunning_02.SetComponentTickEnabled(True)
        goto(ExecutionFlow.Pop())
        # Label 5863
        self.EngineRunning_01.SetComponentTickEnabled(False)
        self.EngineRunning_02.Deactivate()
        self.EngineRunning_02.SetComponentTickEnabled(False)
        goto(ExecutionFlow.Pop())
        # Label 5974
        self.EngineRunning_01.Deactivate()
        goto('L5863')
        self.LostSignificance()
        goto('L5974')
    
