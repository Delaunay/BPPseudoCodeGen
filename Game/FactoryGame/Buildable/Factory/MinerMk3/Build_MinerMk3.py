
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Buildable.Factory.MinerMk2.Build_MinerMk2 import Build_MinerMk2
from Game.FactoryGame.Buildable.Factory.MinerMk2.EMinerState import EMinerState
from Script.Engine import TimerHandle
from Script.Engine import AnimInstance
from Game.FactoryGame.Buildable.Factory.MinerMk2.Build_MinerMk2 import ReceiveDestroyed
from Script.Engine import ReceiveBeginPlay
from Game.FactoryGame.Buildable.Factory.MinerMk3.Anim_MinerMk3 import Anim_MinerMk3
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor
from Game.FactoryGame.Buildable.Factory.MinerMk3.Build_MinerMk3 import ExecuteUbergraph_Build_MinerMk3

class Build_MinerMk3(Build_MinerMk2):
    mInternalMiningState_0: uint8
    mToggleMiningStateHandle_0: TimerHandle
    mMinimumDrillTime_0: float
    mMaximumDrillTime_0: float
    mExtractStartupTimer = 10
    mExtractCycleTime = 0.25
    mItemsPerCycle = 1
    mMustPlaceOnResourceDisqualifier = NewObject[FGCDNeedsResourceNode]()
    mPowerConsumption = 30
    mPowerConsumptionExponent = 1.600000023841858
    mPowerInfoClass = NewObject[FGPowerInfoComponent]()
    mMinimumProducingTime = 2
    mMinimumStoppedTime = 5
    mNumCyclesForProductivity = 20
    mCanChangePotential = True
    mCurrentPotential = 1
    mPendingPotential = 1
    mMinPotential = 0.009999999776482582
    mMaxPotential = 1
    mMaxPotentialIncreasePerCrystal = 0.5
    mFluidStackSizeDefault = EStackSize::SS_FLUID
    mFluidStackSizeMultiplier = 1
    mAddToSignificanceManager = True
    mSignificanceRange = 18000
    mHologramClass = NewObject[FGResourceExtractorHologram]()
    mDisplayName = NSLOCTEXT("", "A2AB562348446A4E3597008E684808AF", "Miner Mk.3")
    mDescription = NSLOCTEXT("", "C13C347446285495914418AEABB15647", "Extracts solid resources from the resource node it is built on. \r\nThe normal extraction rate is 240 resources per minute. \r\nThe extraction rate is modified depending on resource node purity. Outputs all extracted resources onto connected conveyor belts.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_Build_MinerMk3(546)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Build_MinerMk3(10)
    

    def ExecuteUbergraph_Build_MinerMk3(self):
        self.ReceiveBeginPlay()
        ReturnValue1: Ptr[AnimInstance] = self.MainMesh.GetAnimInstance()
        31: Ptr[Anim_MinerMk3] = Cast[Anim_MinerMk3](ReturnValue1)
        bSuccess1: bool = 31
        if not bSuccess1:
            goto('L182')
        31.SetupReloadTimer()
        # End
        # Label 182
        Default__KismetSystemLibrary.PrintString(self, "No minerindustrial animinstance", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        # End
        # Label 294
        self.ReceiveDestroyed()
        ReturnValue: Ptr[AnimInstance] = self.MainMesh.GetAnimInstance()
        3: Ptr[Anim_MinerMk3] = Cast[Anim_MinerMk3](ReturnValue)
        bSuccess: bool = 3
        if not bSuccess:
            goto('L551')
        3.mDrillingVfx_01.Deactivate()
        3.mDrillingVfx_02.Deactivate()
        # End
        goto('L294')
    
