
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.OilRefinery.Build_OilRefinery import ExecuteUbergraph_Build_OilRefinery.K2Node_Event_didGainPower
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Buildable.Factory.OilRefinery.Build_OilRefinery import ExecuteUbergraph_Build_OilRefinery.K2Node_Event_didStopProducing
from Game.FactoryGame.Buildable.Factory.OilRefinery.Audio.Play_F_OilRefinery_Tank_MixDown import Play_F_OilRefinery_Tank_MixDown
from Script.Engine import SpawnEmitterAttached
from Script.FactoryGame import TryStopProductionLoopEffects
from Script.FactoryGame import FGBuildableManufacturer
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import StartProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.GeneratorCoal.Audio.Play_B_Generator_Coal_MixDown_Exhaust import Play_B_Generator_Coal_MixDown_Exhaust
from Script.FactoryGame import TryStartProductionLoopEffects
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.OilRefinery.Audio.Play_F_OilRefinery_Furnace_Quick import Play_F_OilRefinery_Furnace_Quick
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import TryStartIdlingLoopEffects
from Game.FactoryGame.Buildable.Factory.OilRefinery.Audio.Stop_F_OilRefinery_Furnace import Stop_F_OilRefinery_Furnace
from Script.AkAudio import Default__AkGameplayStatics
from Script.AkAudio import PostAkEventAttached
from Script.FactoryGame import TryStopIdlingLoopEffects
from Script.Engine import K2_DestroyComponent
from Script.FactoryGame import LostSignificance
from Script.Engine import ParticleSystemComponent
from Game.FactoryGame.VFX.Factory.Oil_Refinery.P_OilRefineryExhaust import P_OilRefineryExhaust
from Script.FactoryGame import StartIdlingLoopEffects
from Script.FactoryGame import StopIdlingLoopEffects
from Script.Engine import SetFloatParameter
from Script.AkAudio import StopAndDestroyComponent
from Game.FactoryGame.Buildable.Factory.OilRefinery.Build_OilRefinery import ExecuteUbergraph_Build_OilRefinery
from Game.FactoryGame.Buildable.Factory.GeneratorCoal.Audio.Stop_B_Generator_Coal_MixDown_Exhaust import Stop_B_Generator_Coal_MixDown_Exhaust
from Script.AkAudio import AkComponent
from Game.FactoryGame.Buildable.Factory.OilRefinery.Build_OilRefinery import ExecuteUbergraph_Build_OilRefinery.K2Node_Event_didStartProducing
from Script.FactoryGame import StopProductionLoopEffects
from Script.FactoryGame import GainedSignificance
from Game.FactoryGame.Buildable.Factory.OilRefinery.Audio.Stop_F_OilRefinery_Furnace_Quick import Stop_F_OilRefinery_Furnace_Quick
from Game.FactoryGame.Buildable.Factory.OilRefinery.Audio.Play_F_OilRefinery_Furnace import Play_F_OilRefinery_Furnace
from Game.FactoryGame.Buildable.Factory.OilRefinery.Build_OilRefinery import ExecuteUbergraph_Build_OilRefinery.K2Node_Event_didLosePower
from Game.FactoryGame.Buildable.Factory.OilRefinery.Audio.Stop_F_OilRefinery_Tank_MixDown import Stop_F_OilRefinery_Tank_MixDown

class Build_OilRefinery(FGBuildableManufacturer):
    IsPowered: bool
    mExhaustParticle: Ptr[ParticleSystemComponent]
    mProductionEffectsRunning: bool
    mManufacturingSpeed = 1
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
    mHologramClass = NewObject[FGFactoryHologram]()
    mDisplayName = NSLOCTEXT("", "EC74BA4B4881D9235260B7B2AB3088CF", "Refinery")
    mDescription = NewObject[ 10 meters.\r\n(Allows fluids to be transported 10 meters upwards.)\r\n\r\nContains both a Conveyor Belt and Pipe input and output, to allow for the automation of various recipes.")]()
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_Manufacturing]()
    mIsUseable = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def StartIdlingLoopEffects(self):
        ExecuteUbergraph_Build_OilRefinery.K2Node_Event_didGainPower = didGainPower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_OilRefinery(1548)
    

    def StopIdlingLoopEffects(self):
        ExecuteUbergraph_Build_OilRefinery.K2Node_Event_didLosePower = didLosePower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_OilRefinery(1524)
    

    def StartProductionLoopEffects(self):
        ExecuteUbergraph_Build_OilRefinery.K2Node_Event_didStartProducing = didStartProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_OilRefinery(1392)
    

    def StopProductionLoopEffects(self):
        ExecuteUbergraph_Build_OilRefinery.K2Node_Event_didStopProducing = didStopProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_OilRefinery(26)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_OilRefinery(926)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Build_OilRefinery(1039)
    

    def ExecuteUbergraph_Build_OilRefinery(self):
        # Label 10
        self.TryStopIdlingLoopEffects(False)
        # End
        self.StopProductionLoopEffects(didStopProducing)
        if not self.mProductionEffectsRunning:
            goto('L1572')
        self.mProductionEffectsRunning = False
        self.mExhaustParticle.SetFloatParameter("SmokeShortSpawnRate", 0.4000000059604645)
        self.mExhaustParticle.SetFloatParameter("SmokeLongSpawnRate", 0)
        if not didStopProducing:
            goto('L396')
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_OilRefinery_Furnace, self.MainMesh, "AudioSocketFurnace", True)
        ReturnValue1: int32 = self.FGSoundSpline.PostAkEvent(Stop_F_OilRefinery_Tank_MixDown)
        # Label 317
        ReturnValue5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_B_Generator_Coal_MixDown_Exhaust, self.MainMesh, "exhaustVfxSocket", True)
        # End
        # Label 396
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_OilRefinery_Furnace_Quick, self.MainMesh, "AudioSocketFurnace", True)
        Default__AkGameplayStatics.StopAndDestroyComponent(self.FGSoundSpline)
        goto('L317')
        # Label 516
        self.mExhaustParticle.SetFloatParameter("SmokeLongSpawnRate", 1)
        if not didStartProducing:
            goto('L792')
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_OilRefinery_Furnace, self.MainMesh, "AudioSocketFurnace", True)
        # Label 654
        ReturnValue_0: int32 = self.FGSoundSpline.PostAkEvent(Play_F_OilRefinery_Tank_MixDown)
        ReturnValue4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_B_Generator_Coal_MixDown_Exhaust, self.MainMesh, "exhaustVfxSocket", True)
        # End
        # Label 792
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_OilRefinery_Furnace_Quick, self.MainMesh, "AudioSocketFurnace", True)
        goto('L654')
        # Label 871
        self.mExhaustParticle.SetFloatParameter("SmokeShortSpawnRate", 1)
        goto('L516')
        self.GainedSignificance()
        ReturnValue_1: bool = self.HasPower()
        if not ReturnValue_1:
            goto('L1572')
        self.TryStartIdlingLoopEffects(False)
        ReturnValue_2: bool = self.IsProducing()
        if not ReturnValue_2:
            goto('L1572')
        self.TryStartProductionLoopEffects(False)
        # End
        self.LostSignificance()
        ReturnValue1_1: bool = self.IsProducing()
        if not ReturnValue1_1:
            goto('L1103')
        self.TryStopProductionLoopEffects(False)
        goto('L10')
        # Label 1103
        ReturnValue1_2: bool = self.HasPower()
        if not ReturnValue1_2:
            goto('L1572')
        # End
        # Label 1146
        ReturnValue_3: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_OilRefineryExhaust, self.MainMesh, "exhaustVfxSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mExhaustParticle = ReturnValue_3
        # End
        # Label 1287
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(self.mExhaustParticle)
        if not ReturnValue_4:
            goto('L1146')
        # End
        # Label 1357
        self.mProductionEffectsRunning = True
        goto('L871')
        # Label 1373
        if not self.mProductionEffectsRunning:
            goto('L1357')
        # End
        self.StartProductionLoopEffects(didStartProducing)
        goto('L1373')
        # Label 1416
        self.mExhaustParticle.K2_DestroyComponent(self)
        # End
        # Label 1454
        ReturnValue1_3: bool = Default__KismetSystemLibrary.IsValid(self.mExhaustParticle)
        if not ReturnValue1_3:
            goto('L1572')
        goto('L1416')
        self.StopIdlingLoopEffects(didLosePower)
        goto('L1454')
        self.StartIdlingLoopEffects(didGainPower)
        goto('L1287')
    
