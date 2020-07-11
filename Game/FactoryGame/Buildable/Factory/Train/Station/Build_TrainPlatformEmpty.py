
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildableTrainPlatformEmpty

class Build_TrainPlatformEmpty(FGBuildableTrainPlatformEmpty):
    mPlatformConnections = [{'$ObjectClass': '/Script/FactoryGame.FGTrainPlatformConnection', '$ObjectFlags': 2883617, '$ObjectName': 'PlatformConnection0', 'AttachParent': {'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, 'RelativeLocation': {'X': 800, 'Y': 0, 'Z': 0}, 'RelativeRotation': {'Pitch': 0, 'Yaw': 180, 'Roll': 0}, 'Mobility': 0}, {'$ObjectClass': '/Script/FactoryGame.FGTrainPlatformConnection', '$ObjectFlags': 2883617, '$ObjectName': 'PlatformConnection1', 'AttachParent': {'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, 'RelativeLocation': {'X': -800, 'Y': 0, 'Z': 0}, 'Mobility': 0}]
    mPlatformConnection0 = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGTrainPlatformConnection', ObjectFlags=2883617, ObjectName='PlatformConnection0', RelativeLocation={'X': 800, 'Y': 0, 'Z': 0}, RelativeRotation={'Pitch': 0, 'Yaw': 180, 'Roll': 0})
    mPlatformConnection1 = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGTrainPlatformConnection', ObjectFlags=2883617, ObjectName='PlatformConnection1', RelativeLocation={'X': -800, 'Y': 0, 'Z': 0})
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
    mHologramClass = NewObject[Holo_TrainPlatformEmpty]()
    mDisplayName = NSLOCTEXT("", "3763BE324A7CE633C1FEACA891CF080E", "Empty Platform")
    mDescription = NSLOCTEXT("", "38FD107C4A183AA47073F78064292460", "An empty train platform for when you need to create some empty space.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
