
from codegen.ue4_stub import *

from Script.Engine import Not_PreBool
from Script.FactoryGame import FGBuildableStorage
from Script.Engine import ActorHasTag

class Build_StorageIntegrated(FGBuildableStorage):
    mInventorySizeX = 5
    mInventorySizeY = 5
    mPowerConsumptionExponent = 1.600000023841858
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
    mSignificanceRange = 18000
    mHologramClass = NewObject[FGBuildableHologram]()
    mDisplayName = NSLOCTEXT("", "9A1FB991446CCCB04C279980B845C7F9", "Personal Storage Box")
    mDescription = NSLOCTEXT("", "B542BFF7454C7FD6C6E36D9EC37F722D", "A box you can put things in.                                          Has 25 inventory slots.")
    MaxRenderDistance = -1
    mHighlightVector = Namespace(X=0, Y=0.00010699999984353781, Z=88.28619384765625)
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/TradingPost/BP_MaterialEffect_Build_Hub.BP_MaterialEffect_Build_Hub_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mHighlightParticleSystemTemplate = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing')
    mShouldShowHighlight = True
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_Storage]()
    mIsUseable = True
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def CanBeSampled(self):
        ReturnValue = False
    

    def CanDismantle(self):
        ReturnValue: bool = self.ActorHasTag("Integrated")
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        ReturnValue_1: bool = ReturnValue_0
    
