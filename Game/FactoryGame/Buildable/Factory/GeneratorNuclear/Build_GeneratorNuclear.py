
from codegen.ue4_stub import *

from Script.Engine import SetVisibility
from Script.Engine import SpawnEmitterAttached
from Script.FactoryGame import TryStopProductionLoopEffects
from Script.Engine import ReceiveBeginPlay
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Buildable.Factory.GeneratorNuclear.Build_GeneratorNuclear import ExecuteUbergraph_Build_GeneratorNuclear.K2Node_Event_didStopProducing
from Script.FactoryGame import StartProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.GeneratorNuclear.Build_GeneratorNuclear import ExecuteUbergraph_Build_GeneratorNuclear
from Game.FactoryGame.Buildable.Factory.GeneratorNuclear.Audio.Play_F_GeneratorNuclear_StartUp_Quick import Play_F_GeneratorNuclear_StartUp_Quick
from Script.FactoryGame import TryStartProductionLoopEffects
from Script.FactoryGame import FGBuildableGeneratorNuclear
from Game.FactoryGame.Buildable.Factory.GeneratorNuclear.Build_GeneratorNuclear import ExecuteUbergraph_Build_GeneratorNuclear.K2Node_Event_didGainPower
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.GeneratorNuclear.Audio.Stop_F_GeneratorNuclear_Quick import Stop_F_GeneratorNuclear_Quick
from Game.FactoryGame.Buildable.Factory.GeneratorNuclear.Audio.Stop_F_GeneratorNuclear import Stop_F_GeneratorNuclear
from Script.FactoryGame import HasFuel
from Game.FactoryGame.Buildable.Factory.GeneratorNuclear.Build_GeneratorNuclear import ExecuteUbergraph_Build_GeneratorNuclear.K2Node_Event_didStartProducing
from Game.FactoryGame.VFX.Factory.Generator_Nuclear.P_Generator_Nuclear import P_Generator_Nuclear
from Game.FactoryGame.Buildable.Factory.GeneratorNuclear.Audio.Play_F_GeneratorNuclear_StartUp import Play_F_GeneratorNuclear_StartUp
from Game.FactoryGame.Buildable.Factory.GeneratorNuclear.Build_GeneratorNuclear import ExecuteUbergraph_Build_GeneratorNuclear.K2Node_Event_DeltaSeconds
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import TryStartIdlingLoopEffects
from Game.FactoryGame.Buildable.Factory.GeneratorNuclear.Particle.BoilingWater_01 import BoilingWater_01
from Game.FactoryGame.Buildable.Factory.GeneratorNuclear.Anim_GeneratorNuclear import Anim_GeneratorNuclear
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import TryStopIdlingLoopEffects
from Script.AkAudio import PostAkEventAttached
from Script.Engine import K2_DestroyComponent
from Script.FactoryGame import LostSignificance
from Script.Engine import ParticleSystemComponent
from Script.FactoryGame import ReceiveUpdateEffects
from Script.FactoryGame import StartIdlingLoopEffects
from Script.FactoryGame import StopIdlingLoopEffects
from Game.FactoryGame.Buildable.Factory.GeneratorNuclear.Build_GeneratorNuclear import ExecuteUbergraph_Build_GeneratorNuclear.K2Node_Event_didLosePower
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.FactoryGame import GainedSignificance
from Script.FactoryGame import StopProductionLoopEffects

class Build_GeneratorNuclear(FGBuildableGeneratorNuclear):
    mExhaustSmoke01: Ptr[ParticleSystemComponent]
    mBoilingWater01: Ptr[ParticleSystemComponent]
    mBoilingWater02: Ptr[ParticleSystemComponent]
    mLightning01: Ptr[ParticleSystemComponent]
    mLightning02: Ptr[ParticleSystemComponent]
    mCachedLoadPercentage: float
    mOutputInventoryHandler = Namespace(ObjectClass='/Script/FactoryGame.FGReplicationDetailInventoryComponent', ObjectFlags=2883617, ObjectName='WasteInventoryHandler')
    mFuelInventoryHandler = Namespace(ObjectClass='/Script/FactoryGame.FGReplicationDetailInventoryComponent', ObjectFlags=2883617, ObjectName='FuelInventoryHandler')
    mDefaultFuelClasses = ['/Game/FactoryGame/Resource/Parts/NuclearFuelRod/Desc_NuclearFuelRod.Desc_NuclearFuelRod_C']
    mFuelResourceForm = EResourceForm::RF_SOLID
    mRequiresSupplementalResource = True
    mSupplementalResourceClass = NewObject[Desc_Water]()
    mSupplementalLoadAmount = 10000
    mSupplementalToPowerRatio = 2
    mPowerProduction = 2500
    mPowerProductionExponent = 1.3219280242919922
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
    mEffectUpdateInterval = 2
    mAddToSignificanceManager = True
    mSignificanceRange = 48000
    mHologramClass = NewObject[FGFactoryHologram]()
    mDisplayName = NSLOCTEXT("", "A519D24944F564E90A5B108D65CCDEE6", "Nuclear Power Plant")
    mDescription = NSLOCTEXT("", "948765F042C8CFF5B5E4E291A94F8611", "Consumes Nuclear Fuel Rods and Water to produce electricty for the power grid.\r\n\r\nProduces Nuclear Waste, which is extracted from the conveyor belt output.\r\n\r\nResource consumption will automatically be lowered to meet power demands.")
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
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Build_GeneratorNuclear(1598)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_GeneratorNuclear(198)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Build_GeneratorNuclear(307)
    

    def StartProductionLoopEffects(self):
        ExecuteUbergraph_Build_GeneratorNuclear.K2Node_Event_didStartProducing = didStartProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorNuclear(468)
    

    def StopProductionLoopEffects(self):
        ExecuteUbergraph_Build_GeneratorNuclear.K2Node_Event_didStopProducing = didStopProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorNuclear(899)
    

    def StartIdlingLoopEffects(self):
        ExecuteUbergraph_Build_GeneratorNuclear.K2Node_Event_didGainPower = didGainPower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorNuclear(1222)
    

    def StopIdlingLoopEffects(self):
        ExecuteUbergraph_Build_GeneratorNuclear.K2Node_Event_didLosePower = didLosePower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorNuclear(1452)
    

    def ReceiveUpdateEffects(self):
        ExecuteUbergraph_Build_GeneratorNuclear.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorNuclear(1574)
    

    def ExecuteUbergraph_Build_GeneratorNuclear(self):
        # Label 10
        self.TryStopIdlingLoopEffects(False)
        # End
        # Label 26
        self.ReceiveBeginPlay()
        ReturnValue: Ptr[AnimInstance] = self.GeneratorNuclear_Skl.GetAnimInstance()
        Nuclear: Ptr[Anim_GeneratorNuclear] = Cast[Anim_GeneratorNuclear](ReturnValue)
        bSuccess: bool = Nuclear
        if not bSuccess:
            goto('L1603')
        Nuclear.SetupReloadTimer()
        # End
        self.GainedSignificance()
        ReturnValue_0: bool = self.HasFuel()
        if not ReturnValue_0:
            goto('L1603')
        self.TryStartIdlingLoopEffects(False)
        ReturnValue_1: bool = self.IsProducing()
        if not ReturnValue_1:
            goto('L1603')
        self.TryStartProductionLoopEffects(False)
        # End
        self.LostSignificance()
        ReturnValue1: bool = self.IsProducing()
        ReturnValue1_0: bool = self.HasFuel()
        ReturnValue_2: bool = ReturnValue1_0 and ReturnValue1
        if not ReturnValue_2:
            goto('L429')
        self.TryStopProductionLoopEffects(False)
        goto('L10')
        # Label 429
        ReturnValue2: bool = self.HasFuel()
        if not ReturnValue2:
            goto('L1603')
        goto('L10')
        self.StartProductionLoopEffects(didStartProducing)
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(self.mExhaustSmoke01)
        if not ReturnValue_3:
            goto('L557')
        # End
        # Label 557
        ReturnValue_4: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_Generator_Nuclear, self.FGColoredInstanceMeshProxy, "exhaustVfxSocket_01", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mExhaustSmoke01 = ReturnValue_4
        self.NuclearSmokeLOD.SetVisibility(True, False)
        if not didStartProducing:
            goto('L820')
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_GeneratorNuclear_StartUp, self.StaticMesh, "SFX_Socket_Core", True)
        # End
        # Label 820
        ReturnValue_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_GeneratorNuclear_StartUp_Quick, self.StaticMesh, "SFX_Socket_Core", True)
        # End
        self.StopProductionLoopEffects(didStopProducing)
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValid(self.mExhaustSmoke01)
        if not ReturnValue1_1:
            goto('L1603')
        self.mExhaustSmoke01.K2_DestroyComponent(self)
        self.NuclearSmokeLOD.SetVisibility(False, False)
        if not didStopProducing:
            goto('L1143')
        ReturnValue2_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_GeneratorNuclear, self.StaticMesh, "SFX_Socket_Core", True)
        # End
        # Label 1143
        ReturnValue1_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_GeneratorNuclear_Quick, self.StaticMesh, "SFX_Socket_Core", True)
        # End
        self.StartIdlingLoopEffects(didGainPower)
        ReturnValue2_1: bool = Default__KismetSystemLibrary.IsValid(self.mBoilingWater01)
        if not ReturnValue2_1:
            goto('L1311')
        # End
        # Label 1311
        ReturnValue1_3: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(BoilingWater_01, self.GeneratorNuclear_Skl, "waterVfxSocket_01", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mBoilingWater01 = ReturnValue1_3
        # End
        self.StopIdlingLoopEffects(didLosePower)
        ReturnValue3_0: bool = Default__KismetSystemLibrary.IsValid(self.mBoilingWater01)
        if not ReturnValue3_0:
            goto('L1603')
        self.mBoilingWater01.K2_DestroyComponent(self)
        # End
        self.ReceiveUpdateEffects(DeltaSeconds)
        # End
        goto('L26')
    
