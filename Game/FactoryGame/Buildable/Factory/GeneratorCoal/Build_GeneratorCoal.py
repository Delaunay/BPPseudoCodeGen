
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.GeneratorCoal.Audio.Play_B_Generator_Coal_MixDown_TurbineLoop import Play_B_Generator_Coal_MixDown_TurbineLoop
from Game.FactoryGame.VFX.Factory.Generator_Coal.P_Generator_Coal_01 import P_Generator_Coal_01
from Script.Engine import SpawnEmitterAttached
from Game.FactoryGame.Buildable.Factory.GeneratorCoal.Audio.Play_B_Generator_Coal_MixDown_Furnace_Quick import Play_B_Generator_Coal_MixDown_Furnace_Quick
from Game.FactoryGame.Buildable.Factory.GeneratorCoal.Audio.Stop_B_Generator_Coal_MixDown_Furnace import Stop_B_Generator_Coal_MixDown_Furnace
from Script.FactoryGame import TryStopProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.GeneratorCoal.Audio.Play_B_Generator_Coal_MixDown_Furnace import Play_B_Generator_Coal_MixDown_Furnace
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Factory.GeneratorCoal.Build_GeneratorCoal import ExecuteUbergraph_Build_GeneratorCoal
from Script.FactoryGame import StartProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.GeneratorCoal.Audio.Play_B_Generator_Coal_MixDown_Exhaust import Play_B_Generator_Coal_MixDown_Exhaust
from Script.FactoryGame import FGBuildableGeneratorFuel
from Script.FactoryGame import TryStartProductionLoopEffects
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.GeneratorCoal.Audio.Play_B_Generator_Coal_MixDown_Exhaust_Quick import Play_B_Generator_Coal_MixDown_Exhaust_Quick
from Game.FactoryGame.Buildable.Factory.GeneratorCoal.Audio.Stop_B_Generator_Coal_MixDown_TurbineLoop_Quick import Stop_B_Generator_Coal_MixDown_TurbineLoop_Quick
from Script.Engine import Default__GameplayStatics
from Script.AkAudio import Default__AkGameplayStatics
from Script.AkAudio import PostAkEventAttached
from Script.Engine import K2_DestroyComponent
from Script.FactoryGame import LostSignificance
from Script.Engine import ParticleSystemComponent
from Game.FactoryGame.Buildable.Factory.GeneratorCoal.Audio.Play_B_Generator_Coal_MixDown_TurbineLoop_Quick import Play_B_Generator_Coal_MixDown_TurbineLoop_Quick
from Game.FactoryGame.Buildable.Factory.GeneratorCoal.Build_GeneratorCoal import ExecuteUbergraph_Build_GeneratorCoal.K2Node_Event_didStartProducing
from Game.FactoryGame.Buildable.Factory.GeneratorCoal.Audio.Stop_B_Generator_Coal_MixDown_TurbineLoop import Stop_B_Generator_Coal_MixDown_TurbineLoop
from Game.FactoryGame.Buildable.Factory.GeneratorCoal.Audio.Stop_B_Generator_Coal_MixDown_Exhaust import Stop_B_Generator_Coal_MixDown_Exhaust
from Game.FactoryGame.Buildable.Factory.GeneratorCoal.Audio.Stop_B_Generator_Coal_MixDown_Furnace_Quick import Stop_B_Generator_Coal_MixDown_Furnace_Quick
from Game.FactoryGame.Buildable.Factory.GeneratorCoal.Build_GeneratorCoal import ExecuteUbergraph_Build_GeneratorCoal.K2Node_Event_didStopProducing
from Script.AkAudio import AkComponent
from Script.FactoryGame import GainedSignificance
from Script.FactoryGame import StopProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.GeneratorCoal.Audio.Stop_B_Generator_Coal_MixDown_Exhaust_Quick import Stop_B_Generator_Coal_MixDown_Exhaust_Quick

class Build_GeneratorCoal(FGBuildableGeneratorFuel):
    mCoalGenSmokeVfx: Ptr[ParticleSystemComponent]
    mFuelInventoryHandler = Namespace(ObjectClass='/Script/FactoryGame.FGReplicationDetailInventoryComponent', ObjectFlags=2883617, ObjectName='FuelInventoryHandler')
    mDefaultFuelClasses = ['/Game/FactoryGame/Resource/RawResources/Coal/Desc_Coal.Desc_Coal_C', '/Game/FactoryGame/Resource/Parts/CompactedCoal/Desc_CompactedCoal.Desc_CompactedCoal_C', '/Game/FactoryGame/Resource/Parts/PetroleumCoke/Desc_PetroleumCoke.Desc_PetroleumCoke_C']
    mFuelResourceForm = EResourceForm::RF_SOLID
    mRequiresSupplementalResource = True
    mSupplementalResourceClass = NewObject[Desc_Water]()
    mSupplementalLoadAmount = 1000
    mSupplementalToPowerRatio = 10
    mPowerProduction = 75
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
    mSignificanceBias = 0.5
    mAddToSignificanceManager = True
    mSignificanceRange = 48000
    mHologramClass = NewObject[FGFactoryHologram]()
    mDisplayName = NSLOCTEXT("", "C38B9BAA4A167E5A9E4FB5AB1E841F92", "Coal Generator")
    mDescription = NSLOCTEXT("", "2FB5A3B14E36C34D28A3E1B3FD0AE162", "Burns Coal to boil Water, the produced steam rotates turbines to generate electricty for the power grid.\r\nHas a Conveyor Belt and Pipe input, so both the Coal and Water supply can be automated.\r\n\r\nResource consumption will automatically be lowered to meet power demands.")
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
    
    def StartProductionLoopEffects(self):
        ExecuteUbergraph_Build_GeneratorCoal.K2Node_Event_didStartProducing = didStartProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorCoal(1527)
    

    def StopProductionLoopEffects(self):
        ExecuteUbergraph_Build_GeneratorCoal.K2Node_Event_didStopProducing = didStopProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorCoal(1503)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Build_GeneratorCoal(1498)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_GeneratorCoal(1381)
    

    def ExecuteUbergraph_Build_GeneratorCoal(self):
        # Label 10
        self.TryStopProductionLoopEffects(False)
        # End
        # Label 26
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_B_Generator_Coal_MixDown_Exhaust, self.MainMesh, "smokeVfxSocket", True)
        # End
        # Label 105
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mCoalGenSmokeVfx)
        if not ReturnValue_0:
            goto('L1551')
        self.mCoalGenSmokeVfx.K2_DestroyComponent(self)
        if not didStopProducing:
            goto('L444')
        ReturnValue5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_B_Generator_Coal_MixDown_TurbineLoop, self.MainMesh, "AudioSocketTurbine", True)
        ReturnValue4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_B_Generator_Coal_MixDown_Furnace, self.MainMesh, "AudioSocketFurnace", True)
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_B_Generator_Coal_MixDown_Exhaust, self.MainMesh, "smokeVfxSocket", True)
        # End
        # Label 444
        ReturnValue11: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_B_Generator_Coal_MixDown_TurbineLoop_Quick, self.MainMesh, "AudioSocketTurbine", True)
        ReturnValue10: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_B_Generator_Coal_MixDown_Furnace_Quick, self.MainMesh, "AudioSocketFurnace", True)
        ReturnValue9: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_B_Generator_Coal_MixDown_Exhaust_Quick, self.MainMesh, "smokeVfxSocket", True)
        # End
        # Label 671
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_B_Generator_Coal_MixDown_Furnace, self.MainMesh, "AudioSocketFurnace", True)
        goto('L26')
        # Label 750
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_B_Generator_Coal_MixDown_TurbineLoop, self.MainMesh, "AudioSocketTurbine", True)
        goto('L671')
        # Label 829
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(self.mCoalGenSmokeVfx)
        if not ReturnValue1_0:
            goto('L899')
        # End
        # Label 899
        ReturnValue_1: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_Generator_Coal_01, self.MainMesh, "smokeVfxSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mCoalGenSmokeVfx = ReturnValue_1
        self.mCoalGenSmokeVfx.SetEmitterEnable("Red", False)
        self.mCoalGenSmokeVfx.SetEmitterEnable("Sparks", False)
        if not didStartProducing:
            goto('L1154')
        goto('L750')
        # Label 1154
        ReturnValue8: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_B_Generator_Coal_MixDown_TurbineLoop_Quick, self.MainMesh, "AudioSocketTurbine", True)
        ReturnValue7: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_B_Generator_Coal_MixDown_Furnace_Quick, self.MainMesh, "AudioSocketFurnace", True)
        ReturnValue6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_B_Generator_Coal_MixDown_Exhaust_Quick, self.MainMesh, "smokeVfxSocket", True)
        # End
        self.GainedSignificance()
        ReturnValue_2: bool = self.CanStartPowerProduction()
        if not ReturnValue_2:
            goto('L1551')
        self.TryStartProductionLoopEffects(False)
        # End
        # Label 1445
        self.LostSignificance()
        ReturnValue1_1: bool = self.CanStartPowerProduction()
        if not ReturnValue1_1:
            goto('L1551')
        goto('L10')
        goto('L1445')
        self.StopProductionLoopEffects(didStopProducing)
        goto('L105')
        self.StartProductionLoopEffects(didStartProducing)
        goto('L829')
    
