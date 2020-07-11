
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Build_GeneratorBiomass import ExecuteUbergraph_Build_GeneratorBiomass.K2Node_Event_didStopProducing
from Script.Engine import FClamp
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Build_GeneratorBiomass import ExecuteUbergraph_Build_GeneratorBiomass.K2Node_Event_didStartProducing
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Audio.Play_F_Generator_Biomass_Grinder import Play_F_Generator_Biomass_Grinder
from Script.AkAudio import SetActorRTPCValue
from Script.Engine import SpawnEmitterAttached
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Particle.FoliageFunnel import FoliageFunnel
from Script.FactoryGame import TryStopProductionLoopEffects
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Particle.Grinder import Grinder
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import StartProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Build_GeneratorBiomass import ExecuteUbergraph_Build_GeneratorBiomass.K2Node_Event_DeltaSeconds
from Script.FactoryGame import FGBuildableGeneratorFuel
from Script.FactoryGame import TryStartProductionLoopEffects
from Script.Engine import SetScalarParameterValueOnMaterials
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Audio.Play_F_Generator_Biomass_LavaFire import Play_F_Generator_Biomass_LavaFire
from Script.FactoryGame import HasFuel
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Audio.Play_F_Generator_Biomass_Funnel import Play_F_Generator_Biomass_Funnel
from Script.Engine import Default__GameplayStatics
from Script.AkAudio import Stop
from Script.FactoryGame import GetLoadPercentage
from Game.FactoryGame.VFX.Factory.Generator_Biomass.P_Generator_Biomass_Smoke import P_Generator_Biomass_Smoke
from Script.AkAudio import Default__AkGameplayStatics
from Script.AkAudio import PostAkEventAttached
from Script.Engine import K2_DestroyComponent
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Audio.Stop_F_Generator_Biomass_Grinder import Stop_F_Generator_Biomass_Grinder
from Script.Engine import NearlyEqual_FloatFloat
from Script.Engine import ParticleSystemComponent
from Script.FactoryGame import ReceiveUpdateEffects
from Script.FactoryGame import LostSignificance
from Script.Engine import SetFloatParameter
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Build_GeneratorBiomass import ExecuteUbergraph_Build_GeneratorBiomass
from Script.AkAudio import AkComponent
from Script.FactoryGame import GainedSignificance
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Audio.Stop_F_Generator_Biomass_LavaFire import Stop_F_Generator_Biomass_LavaFire
from Script.FactoryGame import StopProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.GeneratorBiomass.Audio.Stop_F_Generator_Biomass_Funnel import Stop_F_Generator_Biomass_Funnel
from Script.Engine import GetComponentsByClass

class Build_GeneratorBiomass(FGBuildableGeneratorFuel):
    mFunnelVfx: Ptr[ParticleSystemComponent]
    mBioGenVfx01: Ptr[ParticleSystemComponent]
    mBioGenVfx02: Ptr[ParticleSystemComponent]
    mCachedLoadPercentage: float
    mFuelInventoryHandler = Namespace(ObjectClass='/Script/FactoryGame.FGReplicationDetailInventoryComponent', ObjectFlags=2883617, ObjectName='FuelInventoryHandler')
    mDefaultFuelClasses = ['/Script/FactoryGame.FGItemDescriptorBiomass']
    mFuelResourceForm = EResourceForm::RF_SOLID
    mPowerProduction = 30
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
    mSignificanceRange = 12000
    mHologramClass = NewObject[FGFactoryHologram]()
    mDisplayName = NSLOCTEXT("", "F99CD0B44EDA7F3729703EA9D53A8429", "Biomass Burner")
    mDescription = NSLOCTEXT("", "869B742B470C99E70DCC068CC7F11E91", "Burns various forms of biomass to generate electricity for the power grid.\r\nHas no input and must therefore be fed biomass manually.\r\n\r\nResource consumption will automatically be lowered to meet power demands.")
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
    
    def HandleStartEffects(self, bStartProducing: bool):
        ExecutionFlow.Push("L852")
        ExecutionFlow.Push("L233")
        # Label 10
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Generator_Biomass_Funnel, self.MainMesh_skl, "AudioSocketGrinder", True)
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Generator_Biomass_Grinder, self.MainMesh_skl, "AudioSocketGrinder", True)
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Generator_Biomass_LavaFire, self.MainMesh_skl, "burnerVfxSocket", True)
        goto(ExecutionFlow.Pop())
        # Label 233
        ExecutionFlow.Push("L512")
        ExecutionFlow.Push("L309")
        ReturnValue2_0: bool = Default__KismetSystemLibrary.IsValid(self.mFunnelVfx)
        if not ReturnValue2_0:
            goto('L715')
        goto(ExecutionFlow.Pop())
        # Label 309
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(self.mBioGenVfx01)
        if not ReturnValue1_0:
            goto('L375')
        goto(ExecutionFlow.Pop())
        # Label 375
        ReturnValue1_1: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_Generator_Biomass_Smoke, self.MainMesh_skl, "burnerVfxSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mBioGenVfx01 = ReturnValue1_1
        goto(ExecutionFlow.Pop())
        # Label 512
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mBioGenVfx02)
        if not ReturnValue_0:
            goto('L578')
        goto(ExecutionFlow.Pop())
        # Label 578
        ReturnValue2_1: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(Grinder, self.MainMesh_skl, "grinderVfxSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mBioGenVfx02 = ReturnValue2_1
        goto(ExecutionFlow.Pop())
        # Label 715
        ReturnValue_1: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(FoliageFunnel, self.MainMesh_skl, "funnelVfxSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mFunnelVfx = ReturnValue_1
        goto(ExecutionFlow.Pop())
    

    def HandleStopEffects(self, bStopProducing: bool):
        ExecutionFlow.Push("L1120")
        ExecutionFlow.Push("L247")
        # Label 10
        if not bStopProducing:
            goto('L538')
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Generator_Biomass_Funnel, self.MainMesh_skl, "AudioSocketGrinder", True)
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Generator_Biomass_Grinder, self.MainMesh_skl, "AudioSocketGrinder", True)
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Generator_Biomass_LavaFire, self.MainMesh_skl, "burnerVfxSocket", True)
        goto(ExecutionFlow.Pop())
        # Label 247
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(self.mFunnelVfx)
        if not ReturnValue1_0:
            goto('L345')
        self.mFunnelVfx.K2_DestroyComponent(self)
        # Label 345
        ReturnValue3: bool = Default__KismetSystemLibrary.IsValid(self.mBioGenVfx01)
        if not ReturnValue3:
            goto('L443')
        self.mBioGenVfx01.K2_DestroyComponent(self)
        # Label 443
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mBioGenVfx02)
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        self.mBioGenVfx02.K2_DestroyComponent(self)
        goto(ExecutionFlow.Pop())
        # Label 538
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 584
        ReturnValue_1: List[Ptr[AkComponent]] = self.GetComponentsByClass(AkComponent)
        
        ReturnValue_2: int32 = len(ReturnValue_1)
        ReturnValue_3: bool = Variable <= ReturnValue_2
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L1046")
        ReturnValue_1 = self.GetComponentsByClass(AkComponent)
        
        Item = None
        Item = ReturnValue_1[Variable_0]
        ReturnValue2_0: bool = Default__KismetSystemLibrary.IsValid(Item)
        if not ReturnValue2_0:
           goto(ExecutionFlow.Pop())
        ReturnValue_1 = self.GetComponentsByClass(AkComponent)
        
        Item = None
        Item = ReturnValue_1[Variable_0]
        Item.Stop()
        goto(ExecutionFlow.Pop())
        # Label 1046
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L584')
    

    def StartProductionLoopEffects(self):
        ExecuteUbergraph_Build_GeneratorBiomass.K2Node_Event_didStartProducing = didStartProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorBiomass(1566)
    

    def StopProductionLoopEffects(self):
        ExecuteUbergraph_Build_GeneratorBiomass.K2Node_Event_didStopProducing = didStopProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorBiomass(1519)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Build_GeneratorBiomass(1514)
    

    def ReceiveUpdateEffects(self):
        ExecuteUbergraph_Build_GeneratorBiomass.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorBiomass(443)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_GeneratorBiomass(1439)
    

    def ExecuteUbergraph_Build_GeneratorBiomass(self):
        # Label 10
        self.GainedSignificance()
        ReturnValue: bool = self.HasFuel()
        if not ReturnValue:
            goto('L1608')
        self.TryStartProductionLoopEffects(False)
        # End
        # Label 70
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mFunnelVfx)
        if not ReturnValue_0:
            goto('L1608')
        ReturnValue4: float = FClamp(self.mCachedLoadPercentage, 0.20000000298023224, 1)
        self.mFunnelVfx.SetFloatParameter("FoliageRateScale", ReturnValue4)
        ReturnValue4 = FClamp(self.mCachedLoadPercentage, 0.20000000298023224, 1)
        self.mFunnelVfx.SetFloatParameter("LeavesRateScale", ReturnValue4)
        ReturnValue4 = FClamp(self.mCachedLoadPercentage, 0.20000000298023224, 1)
        self.mFunnelVfx.SetFloatParameter("SmokeRateScale", ReturnValue4)
        # End
        # Label 443
        self.ReceiveUpdateEffects(DeltaSeconds)
        ReturnValue2: float = self.GetLoadPercentage()
        ReturnValue_1: bool = NearlyEqual_FloatFloat(ReturnValue2, self.mCachedLoadPercentage, 9.999999747378752e-05)
        ReturnValue_2: bool = Not_PreBool(ReturnValue_1)
        if not ReturnValue_2:
            goto('L1608')
        ReturnValue1: float = self.GetLoadPercentage()
        self.mCachedLoadPercentage = ReturnValue1
        ReturnValue_3: float = self.mCachedLoadPercentage * 2
        ReturnValue1_0: float = FClamp(ReturnValue_3, 0.10000000149011612, 2)
        self.MainMesh_skl.SetScalarParameterValueOnMaterials("MoltenEmissive", ReturnValue1_0)
        ReturnValue_4: float = self.GetLoadPercentage()
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_B_LoadPercentage", ReturnValue_4, 0, self)
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValid(self.mBioGenVfx01)
        if not ReturnValue1_1:
            goto('L1608')
        ReturnValue_5: float = FClamp(self.mCachedLoadPercentage, 0.20000000298023224, 1)
        self.mBioGenVfx01.SetFloatParameter("SmokeShortRateScale", ReturnValue_5)
        ReturnValue2_0: float = FClamp(self.mCachedLoadPercentage, 0.20000000298023224, 1)
        self.mBioGenVfx01.SetFloatParameter("SparksRateScale", ReturnValue2_0)
        ReturnValue3: float = FClamp(self.mCachedLoadPercentage, 0.20000000298023224, 1)
        self.mBioGenVfx01.SetFloatParameter("DistortionRateScale", ReturnValue3)
        self.mBioGenVfx01.SetFloatParameter("LightsRateScale", self.mCachedLoadPercentage)
        self.mBioGenVfx01.SetFloatParameter("SmokeLongRateScale", self.mCachedLoadPercentage)
        ReturnValue1_2: float = self.mCachedLoadPercentage * 10
        self.mBioGenVfx01.SetFloatParameter("SmokeLongLifetime", ReturnValue1_2)
        goto('L70')
        goto('L10')
        # Label 1444
        self.TryStopProductionLoopEffects(False)
        # End
        # Label 1460
        ReturnValue1_3: bool = self.HasFuel()
        if not ReturnValue1_3:
            goto('L1608')
        goto('L1444')
        # Label 1499
        self.LostSignificance()
        goto('L1460')
        goto('L1499')
        self.StopProductionLoopEffects(didStopProducing)
        self.HandleStopEffects(didStopProducing)
        # End
        self.StartProductionLoopEffects(didStartProducing)
        self.HandleStartEffects(didStartProducing)
    
