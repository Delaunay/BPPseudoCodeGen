
from codegen.ue4_stub import *

from Script.Engine import FClamp
from Script.AkAudio import SetActorRTPCValue
from Game.FactoryGame.Buildable.Factory.GeneratorFuel.Audio.Play_F_Generator_Fuel_Start_Quick import Play_F_Generator_Fuel_Start_Quick
from Script.Engine import SpawnEmitterAttached
from Script.FactoryGame import TryStopProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.GeneratorFuel.Audio.Stop_F_Generator_Fuel_Stop import Stop_F_Generator_Fuel_Stop
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Buildable.Factory.GeneratorFuel.Audio.Play_F_Generator_Fuel_Start import Play_F_Generator_Fuel_Start
from Script.FactoryGame import StartProductionLoopEffects
from Script.FactoryGame import FGBuildableGeneratorFuel
from Script.FactoryGame import TryStartProductionLoopEffects
from Script.Engine import IsValid
from Script.FactoryGame import HasFuel
from Game.FactoryGame.Buildable.Factory.GeneratorFuel.Build_GeneratorFuel import ExecuteUbergraph_Build_GeneratorFuel.K2Node_Event_didStartProducing
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Generators_Shared.Stop_F_Generator_Fuel_Exhaust import Stop_F_Generator_Fuel_Exhaust
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Generators_Shared.Play_F_Generator_Fuel_Exhaust import Play_F_Generator_Fuel_Exhaust
from Game.FactoryGame.VFX.Factory.Generator_Fuel.P_Generator_Fuel import P_Generator_Fuel
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.Factory.GeneratorFuel.Audio.Stop_F_Generator_Fuel_Stop_Quick import Stop_F_Generator_Fuel_Stop_Quick
from Script.AkAudio import PostAkEventAttached
from Script.Engine import K2_DestroyComponent
from Game.FactoryGame.Buildable.Factory.GeneratorFuel.Build_GeneratorFuel import ExecuteUbergraph_Build_GeneratorFuel.K2Node_Event_didStopProducing
from Script.FactoryGame import LostSignificance
from Script.Engine import ParticleSystemComponent
from Script.Engine import SetFloatParameter
from Game.FactoryGame.Buildable.Factory.GeneratorFuel.Build_GeneratorFuel import ExecuteUbergraph_Build_GeneratorFuel.K2Node_Event_DeltaSeconds
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.FactoryGame import FGFAnimInstanceFactory
from Game.FactoryGame.Buildable.Factory.GeneratorFuel.Build_GeneratorFuel import ExecuteUbergraph_Build_GeneratorFuel
from Script.FactoryGame import GainedSignificance
from Script.FactoryGame import StopProductionLoopEffects

class Build_GeneratorFuel(FGBuildableGeneratorFuel):
    mSmokeVfx01: Ptr[ParticleSystemComponent]
    mSmokeVfx02: Ptr[ParticleSystemComponent]
    mSmokeVfx03: Ptr[ParticleSystemComponent]
    mSmokeVfx04: Ptr[ParticleSystemComponent]
    mRTPCInterval: float
    mCachedLoadPercentage: float
    mFuelInventoryHandler = Namespace(ObjectClass='/Script/FactoryGame.FGReplicationDetailInventoryComponent', ObjectFlags=2883617, ObjectName='FuelInventoryHandler')
    mDefaultFuelClasses = ['/Game/FactoryGame/Resource/Parts/Fuel/Desc_LiquidFuel.Desc_LiquidFuel_C', '/Game/FactoryGame/Resource/Parts/Turbofuel/Desc_LiquidTurboFuel.Desc_LiquidTurboFuel_C', '/Game/FactoryGame/Resource/Parts/BioFuel/Desc_LiquidBiofuel.Desc_LiquidBiofuel_C']
    mFuelResourceForm = EResourceForm::RF_LIQUID
    mPowerProduction = 150
    mPowerProductionExponent = 1.2999999523162842
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
    mEffectUpdateInterval = 2
    mAddToSignificanceManager = True
    mSignificanceRange = 18000
    mHologramClass = NewObject[FGFactoryHologram]()
    mDisplayName = NSLOCTEXT("", "AA728F1D41C142BC9F2CA2AC66B4ADE6", "Fuel Generator")
    mDescription = NSLOCTEXT("", "652554D7475B7CA70B0508A85DF7D1EC", "Consumes Fuel to generate electricity for the power grid.\r\nHas a Pipe input so the Fuel supply can be automated.\r\n\r\nResource consumption will automatically be lowered to meet power demands.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_Generator]()
    mIsUseable = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_GeneratorFuel(996)
    

    def StartProductionLoopEffects(self):
        ExecuteUbergraph_Build_GeneratorFuel.K2Node_Event_didStartProducing = didStartProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorFuel(1056)
    

    def StopProductionLoopEffects(self):
        ExecuteUbergraph_Build_GeneratorFuel.K2Node_Event_didStopProducing = didStopProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorFuel(2009)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Build_GeneratorFuel(2545)
    

    def ReceiveUpdateEffects(self):
        ExecuteUbergraph_Build_GeneratorFuel.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorFuel(2594)
    

    def ExecuteUbergraph_Build_GeneratorFuel(self):
        # Label 10
        self.TryStopProductionLoopEffects(False)
        # End
        # Label 26
        self.mRTPCInterval = 0
        # Label 49
        ReturnValue2: bool = Default__KismetSystemLibrary.IsValid(self.mSmokeVfx01)
        if not ReturnValue2:
            goto('L2599')
        ReturnValue1: float = FClamp(self.mCachedLoadPercentage, 0.30000001192092896, 1)
        self.mSmokeVfx01.SetFloatParameter("SmokeShortSpawnRate", ReturnValue1)
        self.mSmokeVfx02.SetFloatParameter("SmokeShortSpawnRate", ReturnValue1)
        self.mSmokeVfx03.SetFloatParameter("SmokeShortSpawnRate", ReturnValue1)
        self.mSmokeVfx04.SetFloatParameter("SmokeShortSpawnRate", ReturnValue1)
        ReturnValue: float = FClamp(self.mCachedLoadPercentage, 0, 1)
        self.mSmokeVfx01.SetFloatParameter("SmokeLongSpawnRate", ReturnValue)
        self.mSmokeVfx02.SetFloatParameter("SmokeLongSpawnRate", ReturnValue)
        self.mSmokeVfx03.SetFloatParameter("SmokeLongSpawnRate", ReturnValue)
        self.mSmokeVfx04.SetFloatParameter("SmokeLongSpawnRate", ReturnValue)
        # End
        # Label 645
        ReturnValue_0: Ptr[AnimInstance] = self.MainMesh.GetAnimInstance()
        Factory: Ptr[FGFAnimInstanceFactory] = Cast[FGFAnimInstanceFactory](ReturnValue_0)
        bSuccess: bool = Factory
        self.mCachedLoadPercentage = Factory.mProxy.mLoadPercentage
        ReturnValue_1: float = self.mRTPCInterval + DeltaSeconds
        self.mRTPCInterval = ReturnValue_1
        ReturnValue_2: bool = self.mRTPCInterval > 10
        if not ReturnValue_2:
            goto('L49')
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_B_LoadPercentage", self.mCachedLoadPercentage, 0, self)
        goto('L26')
        self.GainedSignificance()
        ReturnValue_3: bool = self.HasFuel()
        if not ReturnValue_3:
            goto('L2599')
        self.TryStartProductionLoopEffects(False)
        # End
        self.StartProductionLoopEffects(didStartProducing)
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(self.mSmokeVfx01)
        if not ReturnValue_4:
            goto('L1145')
        # End
        # Label 1145
        ReturnValue3: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_Generator_Fuel, self.MainMesh, "smokeVfxSocket_01", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mSmokeVfx01 = ReturnValue3
        ReturnValue2_0: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_Generator_Fuel, self.MainMesh, "smokeVfxSocket_02", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mSmokeVfx02 = ReturnValue2_0
        ReturnValue1_0: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_Generator_Fuel, self.MainMesh, "smokeVfxSocket_03", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mSmokeVfx03 = ReturnValue1_0
        ReturnValue_5: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_Generator_Fuel, self.MainMesh, "smokeVfxSocket_04", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mSmokeVfx04 = ReturnValue_5
        if not didStartProducing:
            goto('L1856')
        ReturnValue1_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Generator_Fuel_Exhaust, self.MainMesh, "AudioSocket_Exhaust", True)
        ReturnValue_6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Generator_Fuel_Start, self.MainMesh, "AudioSocket_Root", True)
        # End
        # Label 1856
        ReturnValue5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Generator_Fuel_Exhaust, self.MainMesh, "AudioSocket_Exhaust", True)
        ReturnValue4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Generator_Fuel_Start_Quick, self.MainMesh, "AudioSocket_Root", True)
        # End
        self.StopProductionLoopEffects(didStopProducing)
        ReturnValue1_2: bool = Default__KismetSystemLibrary.IsValid(self.mSmokeVfx01)
        if not ReturnValue1_2:
            goto('L2599')
        self.mSmokeVfx01.K2_DestroyComponent(self)
        self.mSmokeVfx02.K2_DestroyComponent(self)
        self.mSmokeVfx03.K2_DestroyComponent(self)
        self.mSmokeVfx04.K2_DestroyComponent(self)
        if not didStopProducing:
            goto('L2392')
        ReturnValue3_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Generator_Fuel_Exhaust, self.MainMesh, "AudioSocket_Exhaust", True)
        ReturnValue2_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Generator_Fuel_Stop, self.MainMesh, "AudioSocket_Root", True)
        # End
        # Label 2392
        ReturnValue7: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Generator_Fuel_Exhaust, self.MainMesh, "AudioSocket_Exhaust", True)
        ReturnValue6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Generator_Fuel_Stop_Quick, self.MainMesh, "AudioSocket_Root", True)
        # End
        self.LostSignificance()
        ReturnValue1_3: bool = self.HasFuel()
        if not ReturnValue1_3:
            goto('L2599')
        goto('L10')
        goto('L645')
    
