
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.FoundryMk1.Build_FoundryMk1 import ExecuteUbergraph_Build_FoundryMk1
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Smelter_Shared.Stop_Smelter_Shared_EngineLoop import Stop_Smelter_Shared_EngineLoop
from Script.Engine import SpawnEmitterAttached
from Script.FactoryGame import TryStopProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.FoundryMk1.Build_FoundryMk1 import ExecuteUbergraph_Build_FoundryMk1.K2Node_Event_didGainPower
from Script.FactoryGame import FGBuildableManufacturer
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Smelter_Shared.Play_Smelter_Shared_Offline_Ticks import Play_Smelter_Shared_Offline_Ticks
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Smelter_Shared.Play_Smelter_Shared_ShutDown import Play_Smelter_Shared_ShutDown
from Game.FactoryGame.Buildable.Factory.FoundryMk1.Build_FoundryMk1 import ExecuteUbergraph_Build_FoundryMk1.K2Node_Event_didStopProducing
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Smelter_Shared.Play_Smelter_Shared_ExhaustLoop import Play_Smelter_Shared_ExhaustLoop
from Script.FactoryGame import StartProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Smelter_Shared.Stop_Smelter_Shared_ExhaustLoop import Stop_Smelter_Shared_ExhaustLoop
from Script.FactoryGame import TryStartProductionLoopEffects
from Script.Engine import SetScalarParameterValueOnMaterials
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.FoundryMk1.Particle.Heatglow import Heatglow
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Smelter_Shared.Stop_Smelter_Shared_Press_Steam import Stop_Smelter_Shared_Press_Steam
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Smelter_Shared.Play_Smelter_Shared_EngineLoop import Play_Smelter_Shared_EngineLoop
from Game.FactoryGame.VFX.Factory.Smelter.P_SmelterSmoke_01 import P_SmelterSmoke_01
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import TryStartIdlingLoopEffects
from Game.FactoryGame.Buildable.Factory.FoundryMk1.Build_FoundryMk1 import ExecuteUbergraph_Build_FoundryMk1.K2Node_Event_didLosePower
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Smelter_Shared.Stop_Smelter_Shared_Offline_Ticks import Stop_Smelter_Shared_Offline_Ticks
from Script.AkAudio import PostAkEventAttached
from Script.FactoryGame import TryStopIdlingLoopEffects
from Script.Engine import K2_DestroyComponent
from Game.FactoryGame.Buildable.Factory.FoundryMk1.Build_FoundryMk1 import ExecuteUbergraph_Build_FoundryMk1.K2Node_Event_didStartProducing
from Script.FactoryGame import LostSignificance
from Script.Engine import ParticleSystemComponent
from Script.FactoryGame import StartIdlingLoopEffects
from Script.FactoryGame import StopIdlingLoopEffects
from Script.Engine import SetFloatParameter
from Script.AkAudio import AkComponent
from Script.FactoryGame import GainedSignificance
from Script.FactoryGame import StopProductionLoopEffects

class Build_FoundryMk1(FGBuildableManufacturer):
    mBurnerParticle: Ptr[ParticleSystemComponent]
    mHeatParticle01: Ptr[ParticleSystemComponent]
    mHeatParticle02: Ptr[ParticleSystemComponent]
    mProductionEffectsRunning: bool
    mManufacturingSpeed = 1
    mPowerConsumption = 16
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
    mDisplayName = NSLOCTEXT("", "89353AD14BCCDC9A82F5CDAA107A8940", "Foundry")
    mDescription = NSLOCTEXT("", "85DFA9F04DD65865F6A061B3D330D7BB", "Smelts two resources into alloy ingots.\r\n\r\nCan be automated by feeding ore into it with a conveyor belt connected to the inputs. The produced ingots can be automatically extracted by connecting a conveyor belt to the output.")
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
    
    def RemoveProductionEffects(self):
        if not self.mProductionEffectsRunning:
            goto('L471')
        self.mProductionEffectsRunning = False
        self.mBurnerParticle.SetFloatParameter("SmokeShortRateScale", 0.30000001192092896)
        self.mBurnerParticle.SetFloatParameter("SmokeLongRateScale", 0)
        self.MainMesh_skl.SetScalarParameterValueOnMaterials("MoltenEmissive", 0.20000000298023224)
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_Smelter_Shared_Offline_Ticks, self.MainMesh_skl, "tubes_01", True)
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_Smelter_Shared_ExhaustLoop, self.MainMesh_skl, "SmeltingTop", True)
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_Smelter_Shared_EngineLoop, self.MainMesh_skl, "SoundSocket_Foundry_Engine", True)
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_Smelter_Shared_Press_Steam, self.MainMesh_skl, "SoundSocket_Press", True)
    

    def SetupProductionEffects(self):
        if not self.mProductionEffectsRunning:
            goto('L19')
        # End
        # Label 19
        self.mProductionEffectsRunning = True
        self.mBurnerParticle.SetFloatParameter("SmokeShortRateScale", 1)
        self.mBurnerParticle.SetFloatParameter("SmokeLongRateScale", 1)
        self.MainMesh_skl.SetScalarParameterValueOnMaterials("MoltenEmissive", 2)
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_Smelter_Shared_Offline_Ticks, self.MainMesh_skl, "tubes_01", True)
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_Smelter_Shared_ExhaustLoop, self.MainMesh_skl, "SmeltingTop", True)
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_Smelter_Shared_EngineLoop, self.MainMesh_skl, "SoundSocket_Foundry_Engine", True)
    

    def RemoveIdleEffects(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mBurnerParticle)
        if not ReturnValue:
            goto('L362')
        self.mBurnerParticle.K2_DestroyComponent(self)
        self.mHeatParticle01.K2_DestroyComponent(self)
        self.mHeatParticle02.K2_DestroyComponent(self)
        self.MainMesh_skl.SetScalarParameterValueOnMaterials("MoltenEmissive", 0)
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_Smelter_Shared_Offline_Ticks, self.MainMesh_skl, "tubes_01", True)
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_Smelter_Shared_ShutDown, self.MainMesh_skl, "Smeltingbase", True)
    

    def SetupIdleEffects(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mBurnerParticle)
        if not ReturnValue:
            goto('L70')
        # End
        # Label 70
        ReturnValue2: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_SmelterSmoke_01, self.MainMesh_skl, "burnerVfxSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mBurnerParticle = ReturnValue2
        ReturnValue1: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(Heatglow, self.MainMesh_skl, "barrelVfxSocket_01", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mHeatParticle01 = ReturnValue1
        ReturnValue_0: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(Heatglow, self.MainMesh_skl, "barrelVfxSocket_02", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mHeatParticle02 = ReturnValue_0
        self.MainMesh_skl.SetScalarParameterValueOnMaterials("MoltenEmissive", 0.20000000298023224)
    

    def StartProductionLoopEffects(self):
        ExecuteUbergraph_Build_FoundryMk1.K2Node_Event_didStartProducing = didStartProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_FoundryMk1(75)
    

    def StopProductionLoopEffects(self):
        ExecuteUbergraph_Build_FoundryMk1.K2Node_Event_didStopProducing = didStopProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_FoundryMk1(113)
    

    def StartIdlingLoopEffects(self):
        ExecuteUbergraph_Build_FoundryMk1.K2Node_Event_didGainPower = didGainPower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_FoundryMk1(151)
    

    def StopIdlingLoopEffects(self):
        ExecuteUbergraph_Build_FoundryMk1.K2Node_Event_didLosePower = didLosePower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_FoundryMk1(189)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Build_FoundryMk1(460)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_FoundryMk1(465)
    

    def ExecuteUbergraph_Build_FoundryMk1(self):
        # Label 10
        self.TryStartIdlingLoopEffects(False)
        ReturnValue: bool = self.IsProducing()
        if not ReturnValue:
            goto('L470')
        self.TryStartProductionLoopEffects(False)
        # Label 70
        # End
        self.StartProductionLoopEffects(didStartProducing)
        self.SetupProductionEffects()
        # End
        self.StopProductionLoopEffects(didStopProducing)
        self.RemoveProductionEffects()
        # End
        self.StartIdlingLoopEffects(didGainPower)
        self.SetupIdleEffects()
        # End
        self.StopIdlingLoopEffects(didLosePower)
        self.RemoveIdleEffects()
        # End
        # Label 227
        self.GainedSignificance()
        ReturnValue_0: bool = self.HasPower()
        if not ReturnValue_0:
            goto('L470')
        goto('L10')
        # Label 280
        self.LostSignificance()
        ReturnValue1: bool = self.HasPower()
        ReturnValue1_0: bool = self.IsProducing()
        ReturnValue_1: bool = ReturnValue1 and ReturnValue1_0
        if not ReturnValue_1:
            goto('L417')
        self.TryStopProductionLoopEffects(False)
        # Label 401
        self.TryStopIdlingLoopEffects(False)
        # End
        # Label 417
        ReturnValue2: bool = self.HasPower()
        if not ReturnValue2:
            goto('L470')
        goto('L401')
        goto('L280')
        goto('L227')
    
