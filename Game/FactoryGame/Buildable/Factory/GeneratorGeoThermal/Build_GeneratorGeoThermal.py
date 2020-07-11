
from codegen.ue4_stub import *

from Script.FactoryGame import LostSignificance
from Script.FactoryGame import StartProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.GeneratorGeoThermal.Audio.Stop_GeoThermal_Producing import Stop_GeoThermal_Producing
from Script.AkAudio import PostAkEventAttached
from Game.FactoryGame.Buildable.Factory.GeneratorGeoThermal.Audio.Stop_GeoThermal_Turbine_Loop import Stop_GeoThermal_Turbine_Loop
from Game.FactoryGame.Buildable.Factory.GeneratorGeoThermal.Build_GeneratorGeoThermal import ExecuteUbergraph_Build_GeneratorGeoThermal
from Script.FactoryGame import TryStartProductionLoopEffects
from Script.AkAudio import AkComponent
from Game.FactoryGame.Buildable.Factory.GeneratorGeoThermal.Audio.Play_GeoThermal_Turbine_Loop import Play_GeoThermal_Turbine_Loop
from Game.FactoryGame.Buildable.Factory.GeneratorGeoThermal.Build_GeneratorGeoThermal import ExecuteUbergraph_Build_GeneratorGeoThermal.K2Node_Event_didStopProducing
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import TryStopProductionLoopEffects
from Script.FactoryGame import GainedSignificance
from Script.FactoryGame import StopProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.GeneratorGeoThermal.Build_GeneratorGeoThermal import ExecuteUbergraph_Build_GeneratorGeoThermal.K2Node_Event_didStartProducing
from Script.FactoryGame import FGBuildableGeneratorGeoThermal

class Build_GeneratorGeoThermal(FGBuildableGeneratorGeoThermal):
    mProductionEffectsRunning: bool
    mPowerProduction = 200
    mPowerProductionExponent = 1.2999999523162842
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
    mHologramClass = NewObject[FGGeoThermalGeneratorHologram]()
    mDisplayName = NSLOCTEXT("", "9709F0E848E7F6F0655F698AE49B11DE", "Geothermal Generator")
    mDescription = NSLOCTEXT("", "268D4D8B4EBC299186C1AE87E8CE962C", "Can only be built on geyser nodes.\r\nGenerates electricity for your power grid.\r\nDoes not require any resources to be input.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_GeoThermal_Generator]()
    mIsUseable = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_GeneratorGeoThermal(263)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Build_GeneratorGeoThermal(289)
    

    def StartProductionLoopEffects(self):
        ExecuteUbergraph_Build_GeneratorGeoThermal.K2Node_Event_didStartProducing = didStartProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorGeoThermal(304)
    

    def StopProductionLoopEffects(self):
        ExecuteUbergraph_Build_GeneratorGeoThermal.K2Node_Event_didStopProducing = didStopProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_GeneratorGeoThermal(358)
    

    def ExecuteUbergraph_Build_GeneratorGeoThermal(self):
        # Label 10
        self.TryStopProductionLoopEffects(False)
        # End
        # Label 26
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_GeoThermal_Turbine_Loop, self.MainMesh_skl, "AudioSocket_Turbine", True)
        # End
        # Label 105
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_GeoThermal_Producing, self.MainMesh_skl, "AudioSocket_Barrels", True)
        # End
        # Label 184
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_GeoThermal_Turbine_Loop, self.MainMesh_skl, "AudioSocket_Turbine", True)
        goto('L105')
        self.GainedSignificance()
        self.TryStartProductionLoopEffects(False)
        # End
        self.LostSignificance()
        goto('L10')
        self.StartProductionLoopEffects(didStartProducing)
        if not self.mProductionEffectsRunning:
            goto('L342')
        # End
        # Label 342
        self.mProductionEffectsRunning = True
        goto('L26')
        self.StopProductionLoopEffects(didStopProducing)
        if not self.mProductionEffectsRunning:
            goto('L407')
        self.mProductionEffectsRunning = False
        goto('L184')
    
