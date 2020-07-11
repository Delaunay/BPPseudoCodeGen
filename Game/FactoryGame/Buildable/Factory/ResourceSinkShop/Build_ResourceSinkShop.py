
from codegen.ue4_stub import *

from Script.FactoryGame import LostSignificance
from Script.FactoryGame import FGBuildableResourceSinkShop
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.Audio.Play_Shop import Play_Shop
from Script.AkAudio import AkComponent
from Script.FactoryGame import GainedSignificance
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.Build_ResourceSinkShop import ExecuteUbergraph_Build_ResourceSinkShop
from Game.FactoryGame.Buildable.Factory.ResourceSinkShop.Audio.Stop_Shop import Stop_Shop

class Build_ResourceSinkShop(FGBuildableResourceSinkShop):
    mShopInventoryDefaultSize = 30
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
    mHologramClass = NewObject[FGFactoryHologram]()
    mDisplayName = NSLOCTEXT("", "98E1AF4D447BF9A6276B8CB41AC520DA", "AWESOME Shop")
    mDescription = NSLOCTEXT("", "17DF3A07473A1711573D6C8558546356", "Redeem your FICSIT Coupons here! \r\nFor those employees going the extra kilometer we have set aside special bonus milestones and rewards! Get your Coupons in the AWESOME Sink program now!\r\n\r\n*No refunds possible.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[BPW_ResourceSinkShop]()
    mIsUseable = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def LostSignificance(self):
        self.ExecuteUbergraph_Build_ResourceSinkShop(10)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_ResourceSinkShop(146)
    

    def ExecuteUbergraph_Build_ResourceSinkShop(self):
        self.LostSignificance()
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_Shop, self, True)
        # End
        # Label 78
        self.GainedSignificance()
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_Shop, self, True)
        # End
        goto('L78')
    
