
from codegen.ue4_stub import *

from Script.Engine import Actor
from Script.Engine import Abs
from Script.FactoryGame import FGRailroadVehicle
from Script.FactoryGame import FGRailroadVehicleMovementComponent
from Script.FactoryGame import GetForwardSpeed
from Script.FactoryGame import FGBuildableTrainPlatformCargo

class Build_TrainDockingStation(FGBuildableTrainPlatformCargo):
    mPotentialDockers: List[Ptr[Actor]]
    mFreightCargoType = EFreightCargoType::FCT_Standard
    mStorageSizeX = 8
    mStorageSizeY = 6
    mTimeToCompleteLoad = 27
    mTimeToSwapLoadVisibility = 20
    mTimeToCompleteUnload = 27
    mTimeToSwapUnloadVisibility = 6
    mIsInLoadMode = True
    mPlatformConnections = [{'$ObjectClass': '/Script/FactoryGame.FGTrainPlatformConnection', '$ObjectFlags': 2883617, '$ObjectName': 'PlatformConnection0', 'AttachParent': {'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, 'RelativeLocation': {'X': 800, 'Y': 0, 'Z': 0}, 'RelativeRotation': {'Pitch': 0, 'Yaw': 180, 'Roll': 0}, 'Mobility': 0}, {'$ObjectClass': '/Script/FactoryGame.FGTrainPlatformConnection', '$ObjectFlags': 2883617, '$ObjectName': 'PlatformConnection1', 'AttachParent': {'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, 'RelativeLocation': {'X': -800, 'Y': 0, 'Z': 0}, 'Mobility': 0}]
    mPlatformConnection0 = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGTrainPlatformConnection', ObjectFlags=2883617, ObjectName='PlatformConnection0', RelativeLocation={'X': 800, 'Y': 0, 'Z': 0}, RelativeRotation={'Pitch': 0, 'Yaw': 180, 'Roll': 0})
    mPlatformConnection1 = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGTrainPlatformConnection', ObjectFlags=2883617, ObjectName='PlatformConnection1', RelativeLocation={'X': -800, 'Y': 0, 'Z': 0})
    mPowerConsumption = 50
    mPowerConsumptionExponent = 1.600000023841858
    mPowerInfoClass = NewObject[FGPowerInfoComponent]()
    mMinimumProducingTime = 2
    mMinimumStoppedTime = 5
    mNumCyclesForProductivity = 20
    mCurrentPotential = 1
    mPendingPotential = 1
    mMinPotential = 0.009999999776482582
    mMaxPotential = 1
    mMaxPotentialIncreasePerCrystal = 0.5
    mFluidStackSizeDefault = EStackSize::SS_FLUID
    mFluidStackSizeMultiplier = 1
    mAddToSignificanceManager = True
    mSignificanceRange = 18000
    mHologramClass = NewObject[Holo_TrainPlatformCargo]()
    mDisplayName = NSLOCTEXT("", "0D1A72E0436B6897015DE88BF4B385D0", "Freight Platform")
    mDescription = NSLOCTEXT("", "879A50B64430DA44C2942FA0A3284771", "As Freight Cars stop this they will either unload or load their goods, depending on what you\'ve set it to.\r\nThe Freight Platform snaps to Railway, each other and Train Stations.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_Train_DockingStation]()
    mIsUseable = True
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def IsMoving(self, Actor: Ptr[Actor]):
        Vehicle: Ptr[FGRailroadVehicle] = Cast[FGRailroadVehicle](Actor)
        bSuccess: bool = Vehicle
        if not bSuccess:
            goto('L270')
        ReturnValue: Ptr[FGRailroadVehicleMovementComponent] = Vehicle.GetRailroadVehicleMovementComponent()
        ReturnValue_0: float = ReturnValue.GetForwardSpeed()
        ReturnValue_1: float = Abs(ReturnValue_0)
        ReturnValue_2: bool = ReturnValue_1 > 1
        IsMoving = ReturnValue_2
        # End
        # Label 270
        IsMoving = False
    
