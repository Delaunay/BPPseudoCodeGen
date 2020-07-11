
from codegen.ue4_stub import *

from Script.Engine import ReceiveDestroyed
from Script.FactoryGame import CreateAndAddNewRepresentation
from Script.FactoryGame import FGPlayerController
from Script.Engine import Controller
from Game.FactoryGame.Buildable.Vehicle.Train.Wagon.BP_FreightWagon import ExecuteUbergraph_BP_FreightWagon.K2Node_Event_byCharacter
from Game.FactoryGame.Buildable.Vehicle.Train.Wagon.BP_FreightWagon import ExecuteUbergraph_BP_FreightWagon.K2Node_Event_newColor
from Script.Engine import ReceiveBeginPlay
from Script.Engine import HUD
from Script.Engine import HasAuthority
from Script.FactoryGame import Get
from Game.FactoryGame.Buildable.Vehicle.Train.Wagon.BP_FreightWagon import ExecuteUbergraph_BP_FreightWagon
from Script.Engine import PlayerController
from Script.Engine import GetController
from Script.FactoryGame import FGFreightWagon
from Script.Engine import FormatArgumentData
from Game.FactoryGame.Buildable.Vehicle.Train.Wagon.Widget_FreightWagon import Widget_FreightWagon
from Script.FactoryGame import Default__FGActorRepresentationManager
from Script.Engine import GetHUD
from Game.FactoryGame.Interface.UI.Assets.Map.MapCompass_Icon_train import MapCompass_Icon_train
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import FGInteractWidget
from Script.Engine import FlushNetDormancy
from Script.CoreUObject import Vector
from Script.Engine import Format
from Script.FactoryGame import FGActorRepresentationManager
from Script.FactoryGame import FGHUD
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.Buildable.Vehicle.Train.Wagon.BP_FreightWagon import ExecuteUbergraph_BP_FreightWagon.K2Node_Event_state
from Script.FactoryGame import RemoveRepresentationOfActor

class BP_FreightWagon(FGFreightWagon):
    mWidget: TSubclassOf[FGInteractWidget] = NewObject[Widget_FreightWagon]()
    mMapText: FText = NSLOCTEXT("", "484C242D4A43EEC9A4AB069BB2117681", "Freight Car")
    mVehicleMovement = Namespace(ObjectClass='/Script/FactoryGame.FGRailroadVehicleMovementComponent', ObjectFlags=2883617, ObjectName='MovementComp', bReplicates=True, mChassisHeight=700, mChassisWidth=450, mCouplerSetups=[{'BoneName': 'connector_front', 'Length': 115}, {'BoneName': 'connector_back', 'Length': 115}], mCurvatureResistanceCoefficient=3.199999991920777e-05, mMaxAirBrakingEffort=200, mWheelsetSetups=[{'BoneName': 'wheelbase_front', 'CanSwivel': True}, {'BoneName': 'wheelbase_back', 'CanSwivel': True}])
    mContainerMeshStandard = NewObject[SM_Freight_Cargo]()
    mContainerMeshLiquid = NewObject[SM_Freight_Fuel]()
    mInventorySize = 32
    mFluidStackSizeDefault = EStackSize::SS_FLUID
    mFluidStackSizeMultiplier = 32
    mLaunchCharacterScalar = 1000
    mCargoOverlapCollision = Namespace(AreaClass='/Script/NavigationSystem.NavArea_Obstacle', AttachParent={'$ObjectClass': '/Script/Engine.SkeletalMeshComponent', '$ObjectFlags': 2883617, '$ObjectName': 'VehicleMesh', 'AnimClass': '/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/BP_FreightWagonAnim_Child.BP_FreightWagonAnim_Child_C', 'ClothingSimulationFactory': '/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', 'SkeletalMesh': {'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Train/Wagon/Mesh/SK_Freight_Wagon.SK_Freight_Wagon'}, 'bAllowCullDistanceVolume': False, 'bAffectDynamicIndirectLighting': False, 'bAffectDistanceFieldLighting': False, 'BodyInstance': {'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 9372.1826171875, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}}, BodyInstance={'ObjectType': 1, 'CollisionEnabled': 0, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': True, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'WorldStatic', 'Response': 1}, {'Channel': 'WorldDynamic', 'Response': 1}, {'Channel': 'Pawn', 'Response': 1}, {'Channel': 'Visibility', 'Response': 1}, {'Channel': 'Camera', 'Response': 1}, {'Channel': 'PhysicsBody', 'Response': 0}, {'Channel': 'Vehicle', 'Response': 1}, {'Channel': 'Destructible', 'Response': 1}, {'Channel': 'Projectile', 'Response': 1}, {'Channel': 'BuildGun', 'Response': 1}, {'Channel': 'WeaponInstantHit', 'Response': 1}, {'Channel': 'VehicleWheelQuery', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, BoxExtent={'X': 670, 'Y': 200, 'Z': 220}, ObjectClass='/Script/Engine.BoxComponent', ObjectFlags=2883617, ObjectName='cargoCollision', RelativeLocation={'X': -0.000244140625, 'Y': 0, 'Z': 488.7671203613281}, bCanEverAffectNavigation=False)
    mLength = 1600
    mDisplayName = NSLOCTEXT("", "1DD9189A481937D2C37424A91F954D26", "Freight Car")
    mDescription = NSLOCTEXT("", "486951E04FAAA61B8864C887961A94DC", "The Freight Car is used to transport large quantities of resources from one place to another. Resources are loaded and unloaded at Freight Platforms.\r\nMust be built on railway.")
    mHologramClass = NewObject[FGRailroadVehicleHologram]()
    mMesh = Namespace(AnimClass='/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/BP_FreightWagonAnim_Child.BP_FreightWagonAnim_Child_C', BodyInstance={'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 9372.1826171875, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='VehicleMesh', SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Train/Wagon/Mesh/SK_Freight_Wagon.SK_Freight_Wagon'}, bAffectDistanceFieldLighting=False, bAffectDynamicIndirectLighting=False, bAllowCullDistanceVolume=False)
    mHealthComponent = Namespace(ObjectClass='/Script/FactoryGame.FGHealthComponent', ObjectFlags=2883617, ObjectName='HealthComponent', bNetAddressable=True)
    mDisabledByWaterLocations = [{'X': 0, 'Y': 0, 'Z': 0}]
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSubmergedAngularDamping = 6
    mSubmergedLinearDamping = 15
    mSubmergedBouyantForce = 1000
    mAddToSignificanceManager = True
    mSignificanceRange = 20000
    mShouldAttachDriver = True
    RootComponent = Namespace(AnimClass='/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/BP_FreightWagonAnim_Child.BP_FreightWagonAnim_Child_C', BodyInstance={'ObjectType': 6, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': True, 'bNotifyRigidBodyCollision': True, 'bSimulatePhysics': True, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Vehicle', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'HologramClearance', 'Response': 1}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 9372.1826171875, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, ClothingSimulationFactory='/Script/ClothingSystemRuntime.ClothingSimulationFactoryNv', ObjectClass='/Script/Engine.SkeletalMeshComponent', ObjectFlags=2883617, ObjectName='VehicleMesh', SkeletalMesh={'$AssetPath': '/Game/FactoryGame/Buildable/Vehicle/Train/Wagon/Mesh/SK_Freight_Wagon.SK_Freight_Wagon'}, bAffectDistanceFieldLighting=False, bAffectDynamicIndirectLighting=False, bAllowCullDistanceVolume=False)
    
    def GetActorCompassViewDistance(self):
        ReturnValue = 4
    

    def SetActorCompassViewDistance(self):
        ReturnValue = 0
    

    def SetActorRepresentationText(self):
        self.FlushNetDormancy()
        self.mMapText = newText
        ReturnValue = self.mMapText
    

    def UpdateRepresentation(self):
        ReturnValue = False
    

    def GetActorFogOfWarRevealRadius(self):
        ReturnValue = 0
    

    def GetActorFogOfWarRevealType(self):
        ReturnValue = 0
    

    def GetActorRepresentationColor(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Graphics
    

    def GetActorRepresentationText(self):
        ReturnValue = self.mMapText
    

    def GetActorRepresentationTexture(self):
        ReturnValue = MapCompass_Icon_train
    

    def GetActorRepresentationType(self):
        ReturnValue = 12
    

    def GetActorShouldShowInCompass(self):
        ReturnValue = False
    

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
        ReturnValue = False
    

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
    

    def GetLookAtDecription(self):
        UseText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': 'Press [{BUTTON}] to open inventory'}"
        ReturnValue: Ptr[Controller] = self.GetController()
        
        button = None
        Default__HUDHelpers.GetKeyNameForActionSimple(ReturnValue, "Use", self, Ref[button])
        FormatArgumentData.ArgumentName = "BUTTON"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = button
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_0: FText = Default__KismetTextLibrary.Format(UseText, Array)
        ReturnValue_1: FText = ReturnValue_0
    

    def SetActorRepresentationColor(self):
        ExecuteUbergraph_BP_FreightWagon.K2Node_Event_newColor = NewColor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_FreightWagon(10)
    

    def OnUse(self):
        ExecuteUbergraph_BP_FreightWagon.K2Node_Event_byCharacter = byCharacter #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_FreightWagon.K2Node_Event_state = State #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_FreightWagon(15)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_FreightWagon(387)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_BP_FreightWagon(426)
    

    def ExecuteUbergraph_BP_FreightWagon(self):
        # End
        ReturnValue: Ptr[Controller] = byCharacter.GetController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L460')
        Controller_0: Ptr[FGPlayerController] = Cast[FGPlayerController](Controller)
        bSuccess1: bool = Controller_0
        if not bSuccess1:
            goto('L460')
        ReturnValue_0: Ptr[HUD] = Controller_0.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_0)
        bSuccess2: bool = AsFGHUD
        if not bSuccess2:
            goto('L460')
        AsFGHUD.OpenInteractUI(Widget_FreightWagon, self)
        # End
        self.ReceiveBeginPlay()
        ReturnValue_1: bool = self.AddAsRepresentation()
        # End
        self.ReceiveDestroyed()
        ReturnValue_2: bool = self.RemoveAsRepresentation()
    
