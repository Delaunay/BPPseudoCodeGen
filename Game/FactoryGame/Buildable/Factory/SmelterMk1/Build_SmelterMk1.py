
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Smelter_Shared.Stop_Smelter_Shared_EngineLoop import Stop_Smelter_Shared_EngineLoop
from Script.Engine import SpawnEmitterAttached
from Game.FactoryGame.Buildable.Factory.SmelterMk1.Build_SmelterMk1 import ExecuteUbergraph_Build_SmelterMk1.K2Node_Event_didStopProducing
from Game.FactoryGame.Buildable.Factory.SmelterMk1.Build_SmelterMk1 import ExecuteUbergraph_Build_SmelterMk1.K2Node_Event_didLosePower
from Script.FactoryGame import TryStopProductionLoopEffects
from Script.FactoryGame import FGBuildableManufacturer
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Smelter_Shared.Play_Smelter_Shared_Offline_Ticks import Play_Smelter_Shared_Offline_Ticks
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Smelter_Shared.Play_Smelter_Shared_ShutDown import Play_Smelter_Shared_ShutDown
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Smelter_Shared.Play_Smelter_Shared_ExhaustLoop import Play_Smelter_Shared_ExhaustLoop
from Script.FactoryGame import StartProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Smelter_Shared.Stop_Smelter_Shared_ExhaustLoop import Stop_Smelter_Shared_ExhaustLoop
from Script.FactoryGame import TryStartProductionLoopEffects
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.FoundryMk1.Particle.Heatglow import Heatglow
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Smelter_Shared.Stop_Smelter_Shared_Press_Steam import Stop_Smelter_Shared_Press_Steam
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Smelter_Shared.Play_Smelter_Shared_EngineLoop import Play_Smelter_Shared_EngineLoop
from Game.FactoryGame.VFX.Factory.Smelter.P_SmelterSmoke_01 import P_SmelterSmoke_01
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import TryStartIdlingLoopEffects
from Script.FactoryGame import GetIsSignificant
from Game.FactoryGame.Buildable.Factory.SmelterMk1.Build_SmelterMk1 import ExecuteUbergraph_Build_SmelterMk1.K2Node_Event_didStartProducing
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Smelter_Shared.Stop_Smelter_Shared_Offline_Ticks import Stop_Smelter_Shared_Offline_Ticks
from Script.AkAudio import PostAkEventAttached
from Script.FactoryGame import TryStopIdlingLoopEffects
from Script.Engine import K2_DestroyComponent
from Script.FactoryGame import LostSignificance
from Script.Engine import ParticleSystemComponent
from Script.FactoryGame import StartIdlingLoopEffects
from Game.FactoryGame.Buildable.Factory.SmelterMk1.Build_SmelterMk1 import ExecuteUbergraph_Build_SmelterMk1
from Game.FactoryGame.Buildable.Factory.SmelterMk1.Build_SmelterMk1 import ExecuteUbergraph_Build_SmelterMk1.K2Node_Event_didGainPower
from Script.FactoryGame import StopIdlingLoopEffects
from Script.Engine import SetFloatParameter
from Script.AkAudio import AkComponent
from Script.FactoryGame import GainedSignificance
from Game.FactoryGame.Buildable.Factory.-Shared.Audio.Smelter_Shared.Play_Smelter_Shared_StartUp import Play_Smelter_Shared_StartUp
from Script.FactoryGame import StopProductionLoopEffects

class Build_SmelterMk1(FGBuildableManufacturer):
    mBurnerParticle: Ptr[ParticleSystemComponent]
    mHeatParticle: Ptr[ParticleSystemComponent]
    mProductionEffectsRunning: bool
    mManufacturingSpeed = 1
    mPowerConsumption = 4
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
    mDisplayName = NSLOCTEXT("", "3CA150EE4C2EBEDE9D0F87891C4A5080", "Smelter")
    mDescription = NSLOCTEXT("", "D21370CD45DDE70B1D9C728BFAC366B8", "Smelts ore into ingots.\r\n\r\nCan be automated by feeding ore into it with a conveyor belt connected to the input. The produced ingots can be automatically extracted by connecting a conveyor belt to the output.")
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
    
    def SpawnProductionParticles(self):
        ReturnValue1: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_SmelterSmoke_01, self.MainMesh_skl, "burnerVfxSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mBurnerParticle = ReturnValue1
        ReturnValue: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(Heatglow, self.MainMesh_skl, "barrelVfxSocket_01", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mHeatParticle = ReturnValue
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_SmelterMk1(10)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Build_SmelterMk1(2204)
    

    def StartProductionLoopEffects(self):
        ExecuteUbergraph_Build_SmelterMk1.K2Node_Event_didStartProducing = didStartProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_SmelterMk1(2165)
    

    def StartIdlingLoopEffects(self):
        ExecuteUbergraph_Build_SmelterMk1.K2Node_Event_didGainPower = didGainPower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_SmelterMk1(2141)
    

    def StopIdlingLoopEffects(self):
        ExecuteUbergraph_Build_SmelterMk1.K2Node_Event_didLosePower = didLosePower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_SmelterMk1(992)
    

    def StopProductionLoopEffects(self):
        ExecuteUbergraph_Build_SmelterMk1.K2Node_Event_didStopProducing = didStopProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_SmelterMk1(1363)
    

    def ExecuteUbergraph_Build_SmelterMk1(self):
        self.GainedSignificance()
        ReturnValue: bool = self.HasPower()
        if not ReturnValue:
            goto('L2209')
        self.TryStartIdlingLoopEffects(False)
        ReturnValue_0: bool = self.IsProducing()
        if not ReturnValue_0:
            goto('L2209')
        self.TryStartProductionLoopEffects(False)
        # End
        # Label 123
        self.mBurnerParticle.K2_DestroyComponent(self)
        self.mHeatParticle.K2_DestroyComponent(self)
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_Smelter_Shared_Offline_Ticks, self.MainMesh_skl, "AudioSocket_Tubes", True)
        ReturnValue8: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_Smelter_Shared_ShutDown, self.MainMesh_skl, "AudioSocket_SmeltingPlate", True)
        # End
        # Label 342
        self.mBurnerParticle.SetFloatParameter("SmokeShortRateScale", 1)
        self.mBurnerParticle.SetFloatParameter("SmokeLongRateScale", 1)
        ReturnValue4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_Smelter_Shared_EngineLoop, self.MainMesh_skl, "AudioSocket_Rotator", True)
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_Smelter_Shared_ExhaustLoop, self.MainMesh_skl, "SmeltingTop", True)
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_Smelter_Shared_Offline_Ticks, self.MainMesh_skl, "AudioSocket_Tubes", True)
        # End
        # Label 669
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(self.mBurnerParticle)
        if not ReturnValue_2:
            goto('L2209')
        goto('L123')
        # Label 739
        self.mBurnerParticle.SetFloatParameter("SmokeShortRateScale", 1)
        self.mBurnerParticle.SetFloatParameter("SmokeLongRateScale", 0)
        ReturnValue9: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_Smelter_Shared_StartUp, self.MainMesh_skl, "AudioSocket_SmeltingPlate", True)
        ReturnValue10: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_Smelter_Shared_StartUp, self.MainMesh_skl, "Smeltingbase", True)
        # End
        self.StopIdlingLoopEffects(didLosePower)
        goto('L669')
        # Label 1016
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mBurnerParticle)
        if not ReturnValue1:
            goto('L1086')
        # End
        # Label 1086
        ReturnValue_3: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_SmelterSmoke_01, self.MainMesh_skl, "burnerVfxSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mBurnerParticle = ReturnValue_3
        ReturnValue1_0: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(Heatglow, self.MainMesh_skl, "barrelVfxSocket_01", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mHeatParticle = ReturnValue1_0
        goto('L739')
        self.StopProductionLoopEffects(didStopProducing)
        if not self.mProductionEffectsRunning:
            goto('L2209')
        self.mProductionEffectsRunning = False
        ReturnValue2_0: bool = Default__KismetSystemLibrary.IsValid(self.mBurnerParticle)
        if not ReturnValue2_0:
            goto('L1572')
        self.mBurnerParticle.SetFloatParameter("SmokeShortRateScale", 1)
        self.mBurnerParticle.SetFloatParameter("SmokeLongRateScale", 0)
        # Label 1572
        ReturnValue7: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_Smelter_Shared_EngineLoop, self.MainMesh_skl, "AudioSocket_Rotator", True)
        ReturnValue6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_Smelter_Shared_ExhaustLoop, self.MainMesh_skl, "SmeltingTop", True)
        ReturnValue5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_Smelter_Shared_Press_Steam, self.MainMesh_skl, "Press", True)
        ReturnValue_4: bool = self.GetIsSignificant()
        if not ReturnValue_4:
            goto('L2209')
        ReturnValue1_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_Smelter_Shared_Offline_Ticks, self.MainMesh_skl, "AudioSocket_Tubes", True)
        # End
        # Label 1907
        ReturnValue2_1: bool = self.HasPower()
        if not ReturnValue2_1:
            goto('L2209')
        # Label 1945
        self.TryStopIdlingLoopEffects(False)
        # End
        # Label 1961
        ReturnValue1_2: bool = self.HasPower()
        ReturnValue1_3: bool = self.IsProducing()
        ReturnValue_5: bool = ReturnValue1_2 and ReturnValue1_3
        if not ReturnValue_5:
            goto('L1907')
        self.TryStopProductionLoopEffects(False)
        goto('L1945')
        # Label 2077
        self.mProductionEffectsRunning = True
        goto('L342')
        # Label 2093
        ReturnValue_6: bool = Not_PreBool(self.mProductionEffectsRunning)
        if not ReturnValue_6:
            goto('L2209')
        goto('L2077')
        self.StartIdlingLoopEffects(didGainPower)
        goto('L1016')
        self.StartProductionLoopEffects(didStartProducing)
        goto('L2093')
        # Label 2189
        self.LostSignificance()
        goto('L1961')
        goto('L2189')
    
