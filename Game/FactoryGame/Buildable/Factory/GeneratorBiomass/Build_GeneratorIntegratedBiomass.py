
from codegen.ue4_stub import *

from Script.Engine import FClamp
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Audio.Play_F_Generator_Biomass_Grinder import Play_F_Generator_Biomass_Grinder
from Script.AkAudio import SetActorRTPCValue
from Script.Engine import SpawnEmitterAttached
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Particle.FoliageFunnel import FoliageFunnel
from Script.Engine import ActorHasTag
from Script.FactoryGame import TryStopProductionLoopEffects
from Script.Engine import Not_PreBool
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Build_GeneratorIntegratedBiomass import ExecuteUbergraph_Build_GeneratorIntegratedBiomass.K2Node_Event_DeltaSeconds
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Particle.Grinder import Grinder
from Script.FactoryGame import StartProductionLoopEffects
from Script.FactoryGame import FGBuildableGeneratorFuel
from Script.FactoryGame import TryStartProductionLoopEffects
from Script.Engine import SetScalarParameterValueOnMaterials
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Audio.Play_F_Generator_Biomass_LavaFire import Play_F_Generator_Biomass_LavaFire
from Script.FactoryGame import HasFuel
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Audio.Play_F_Generator_Biomass_Funnel import Play_F_Generator_Biomass_Funnel
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import GetLoadPercentage
from Game.FactoryGame.VFX.Factory.Generator_Biomass.P_Generator_Biomass_Smoke import P_Generator_Biomass_Smoke
from Script.AkAudio import Default__AkGameplayStatics
from Script.AkAudio import PostAkEventAttached
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Build_GeneratorIntegratedBiomass import ExecuteUbergraph_Build_GeneratorIntegratedBiomass.K2Node_Event_didStopProducing
from Script.Engine import K2_DestroyComponent
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Build_GeneratorIntegratedBiomass import ExecuteUbergraph_Build_GeneratorIntegratedBiomass.K2Node_Event_didStartProducing
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Audio.Stop_F_Generator_Biomass_Grinder import Stop_F_Generator_Biomass_Grinder
from Script.FactoryGame import LostSignificance
from Script.Engine import ParticleSystemComponent
from Script.FactoryGame import ReceiveUpdateEffects
from Script.Engine import NearlyEqual_FloatFloat
from Script.Engine import SetFloatParameter
from Script.AkAudio import AkComponent
from Script.FactoryGame import GainedSignificance
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Audio.Stop_F_Generator_Biomass_LavaFire import Stop_F_Generator_Biomass_LavaFire
from Script.FactoryGame import StopProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Audio.Stop_F_Generator_Biomass_Funnel import Stop_F_Generator_Biomass_Funnel
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Build_GeneratorIntegratedBiomass import ExecuteUbergraph_Build_GeneratorIntegratedBiomass

class Build_GeneratorIntegratedBiomass(FGBuildableGeneratorFuel):
    mFunnelVfx: Ptr[ParticleSystemComponent]
    mBioGenVfx01: Ptr[ParticleSystemComponent]
    mBioGenVfx02: Ptr[ParticleSystemComponent]
    mCachedLoadPercentage: float
    mFuelInventoryHandler = Namespace(ObjectClass='/Script/FactoryGame.FGReplicationDetailInventoryComponent', ObjectFlags=2883617, ObjectName='FuelInventoryHandler')
    mDefaultFuelClasses = ['/Script/FactoryGame.FGItemDescriptorBiomass']
    mFuelResourceForm = EResourceForm::RF_SOLID
    mPowerProduction = 20
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
    mEffectUpdateInterval = 1
    mAddToSignificanceManager = True
    mSignificanceRange = 18000
    mHologramClass = NewObject[FGFactoryHologram]()
    mDisplayName = NSLOCTEXT("", "F99CD0B44EDA7F3729703EA9D53A8429", "Biomass Burner")
    mDescription = NSLOCTEXT("", "2DD400DF4B20B30420BDC09440952EBE", "Burns Biomass to produce power. Biomass must be loaded manually and is obtained by picking up flora in the world. Produces up to 20MW of power while operating.")
    MaxRenderDistance = -1
    mHighlightVector = Namespace(X=-39.38166046142578, Y=41.12388610839844, Z=446.2125549316406)
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
    mInteractWidgetClass = NewObject[Widget_Generator]()
    mIsUseable = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
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
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_GeneratorIntegratedBiomass(2678)
    

    def StartProductionLoopEffects(self):
        ExecuteUbergraph_Build_GeneratorIntegratedBiomass.K2Node_Event_didStartProducing = didStartProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorIntegratedBiomass(2589)
    

    def StopProductionLoopEffects(self):
        ExecuteUbergraph_Build_GeneratorIntegratedBiomass.K2Node_Event_didStopProducing = didStopProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorIntegratedBiomass(2565)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Build_GeneratorIntegratedBiomass(941)
    

    def ReceiveUpdateEffects(self):
        ExecuteUbergraph_Build_GeneratorIntegratedBiomass.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorIntegratedBiomass(990)
    

    def ExecuteUbergraph_Build_GeneratorIntegratedBiomass(self):
        # Label 10
        self.TryStopProductionLoopEffects(False)
        # End
        # Label 26
        self.mFunnelVfx.K2_DestroyComponent(self)
        self.mBioGenVfx01.K2_DestroyComponent(self)
        self.mBioGenVfx02.K2_DestroyComponent(self)
        ReturnValue5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Generator_Biomass_Funnel, self.MainMesh_skl, "AudioSocketGrinder", True)
        ReturnValue4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Generator_Biomass_Grinder, self.MainMesh_skl, "AudioSocketGrinder", True)
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Generator_Biomass_LavaFire, self.MainMesh_skl, "burnerVfxSocket", True)
        # End
        # Label 352
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Generator_Biomass_LavaFire, self.MainMesh_skl, "burnerVfxSocket", True)
        # End
        # Label 431
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Generator_Biomass_Grinder, self.MainMesh_skl, "AudioSocketGrinder", True)
        goto('L352')
        # Label 510
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Generator_Biomass_Funnel, self.MainMesh_skl, "AudioSocketGrinder", True)
        goto('L431')
        # Label 589
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mFunnelVfx)
        if not ReturnValue_0:
            goto('L2683')
        goto('L26')
        # Label 659
        ReturnValue_1: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(Grinder, self.MainMesh_skl, "grinderVfxSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mBioGenVfx02 = ReturnValue_1
        goto('L510')
        # Label 800
        ReturnValue1_0: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_Generator_Biomass_Smoke, self.MainMesh_skl, "burnerVfxSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mBioGenVfx01 = ReturnValue1_0
        goto('L659')
        self.LostSignificance()
        ReturnValue_2: bool = self.HasFuel()
        if not ReturnValue_2:
            goto('L2683')
        goto('L10')
        self.ReceiveUpdateEffects(DeltaSeconds)
        ReturnValue2_0: float = self.GetLoadPercentage()
        ReturnValue_3: bool = NearlyEqual_FloatFloat(ReturnValue2_0, self.mCachedLoadPercentage, 9.999999747378752e-05)
        ReturnValue_4: bool = Not_PreBool(ReturnValue_3)
        if not ReturnValue_4:
            goto('L2683')
        ReturnValue1_1: float = self.GetLoadPercentage()
        self.mCachedLoadPercentage = ReturnValue1_1
        ReturnValue_5: float = self.mCachedLoadPercentage * 2
        ReturnValue1_2: float = FClamp(ReturnValue_5, 0.10000000149011612, 2)
        self.MainMesh_skl.SetScalarParameterValueOnMaterials("MoltenEmissive", ReturnValue1_2)
        ReturnValue_6: float = self.GetLoadPercentage()
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_B_LoadPercentage", ReturnValue_6, 0, self)
        ReturnValue3_0: bool = Default__KismetSystemLibrary.IsValid(self.mBioGenVfx01)
        if not ReturnValue3_0:
            goto('L2683')
        ReturnValue_7: float = FClamp(self.mCachedLoadPercentage, 0.20000000298023224, 1)
        self.mBioGenVfx01.SetFloatParameter("SmokeShortRateScale", ReturnValue_7)
        ReturnValue2_1: float = FClamp(self.mCachedLoadPercentage, 0.20000000298023224, 1)
        self.mBioGenVfx01.SetFloatParameter("SparksRateScale", ReturnValue2_1)
        ReturnValue3_1: float = FClamp(self.mCachedLoadPercentage, 0.20000000298023224, 1)
        self.mBioGenVfx01.SetFloatParameter("DistortionRateScale", ReturnValue3_1)
        self.mBioGenVfx01.SetFloatParameter("LightsRateScale", self.mCachedLoadPercentage)
        self.mBioGenVfx01.SetFloatParameter("SmokeLongRateScale", self.mCachedLoadPercentage)
        ReturnValue1_3: float = self.mCachedLoadPercentage * 10
        self.mBioGenVfx01.SetFloatParameter("SmokeLongLifetime", ReturnValue1_3)
        ReturnValue2_2: bool = Default__KismetSystemLibrary.IsValid(self.mFunnelVfx)
        if not ReturnValue2_2:
            goto('L2683')
        ReturnValue4_0: float = FClamp(self.mCachedLoadPercentage, 0.20000000298023224, 1)
        self.mFunnelVfx.SetFloatParameter("FoliageRateScale", ReturnValue4_0)
        ReturnValue4_0 = FClamp(self.mCachedLoadPercentage, 0.20000000298023224, 1)
        self.mFunnelVfx.SetFloatParameter("LeavesRateScale", ReturnValue4_0)
        ReturnValue4_0 = FClamp(self.mCachedLoadPercentage, 0.20000000298023224, 1)
        self.mFunnelVfx.SetFloatParameter("SmokeRateScale", ReturnValue4_0)
        # End
        # Label 2354
        ReturnValue1_4: bool = Default__KismetSystemLibrary.IsValid(self.mFunnelVfx)
        if not ReturnValue1_4:
            goto('L2424')
        # End
        # Label 2424
        ReturnValue2_3: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(FoliageFunnel, self.MainMesh_skl, "funnelVfxSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mFunnelVfx = ReturnValue2_3
        goto('L800')
        self.StopProductionLoopEffects(didStopProducing)
        goto('L589')
        self.StartProductionLoopEffects(didStartProducing)
        goto('L2354')
        # Label 2613
        ReturnValue1_5: bool = self.HasFuel()
        if not ReturnValue1_5:
            goto('L2683')
        self.TryStartProductionLoopEffects(False)
        # End
        # Label 2663
        self.GainedSignificance()
        goto('L2613')
        goto('L2663')
    
