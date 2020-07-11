
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.OilPump.Build_OilPump import ExecuteUbergraph_Build_OilPump.K2Node_Event_didStopProducing
from Script.FactoryGame import FGBuildableResourceExtractor
from Script.FactoryGame import FGResourceDescriptor
from Script.FactoryGame import GetExtractableResource
from Game.FactoryGame.Buildable.Factory.OilPump.Audio.Stop_F_Pump_Oil_Pump_Rattle_Bass import Stop_F_Pump_Oil_Pump_Rattle_Bass
from Game.FactoryGame.Buildable.Factory.OilPump.Particle.BurnerFire import BurnerFire
from Game.FactoryGame.Buildable.Factory.OilPump.Audio.Play_F_Pump_Oil_Liquid_Bubbles import Play_F_Pump_Oil_Liquid_Bubbles
from Script.Engine import SpawnEmitterAttached
from Script.FactoryGame import TryStopProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.OilPump.Audio.Stop_F_Pump_Oil_Liquid_Bubbles import Stop_F_Pump_Oil_Liquid_Bubbles
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Factory.OilPump.Build_OilPump import ExecuteUbergraph_Build_OilPump.K2Node_Event_didGainPower
from Script.FactoryGame import StartProductionLoopEffects
from Script.FactoryGame import TryStartProductionLoopEffects
from Script.Engine import SetScalarParameterValueOnMaterials
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.OilPump.Build_OilPump import ExecuteUbergraph_Build_OilPump
from Game.FactoryGame.Buildable.Factory.OilPump.Audio.Stop_F_Pump_Oil_GasFire_Small import Stop_F_Pump_Oil_GasFire_Small
from Game.FactoryGame.Buildable.Factory.OilPump.Audio.Stop_F_Pump_Oil_Pump_Rattle_Light import Stop_F_Pump_Oil_Pump_Rattle_Light
from Script.FactoryGame import FGExtractableResourceInterface
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import TryStartIdlingLoopEffects
from Game.FactoryGame.Buildable.Factory.OilPump.Build_OilPump import ExecuteUbergraph_Build_OilPump.K2Node_Event_didStartProducing
from Game.FactoryGame.Buildable.Factory.OilPump.Audio.Play_F_Pump_Oil_Pump_Rattle_Light import Play_F_Pump_Oil_Pump_Rattle_Light
from Game.FactoryGame.Buildable.Factory.OilPump.Audio.Play_F_Pump_Oil_Pump_Rattle_Bass import Play_F_Pump_Oil_Pump_Rattle_Bass
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.Factory.OilPump.Audio.Stop_F_Pump_Oil_Liquid_Loop_LPF import Stop_F_Pump_Oil_Liquid_Loop_LPF
from Script.AkAudio import PostAkEventAttached
from Script.FactoryGame import TryStopIdlingLoopEffects
from Script.Engine import K2_DestroyComponent
from Game.FactoryGame.Buildable.Factory.OilPump.Audio.Play_F_Pump_Oil_Liquid_Loop_LPF import Play_F_Pump_Oil_Liquid_Loop_LPF
from Script.FactoryGame import LostSignificance
from Script.Engine import ParticleSystemComponent
from Script.FactoryGame import StartIdlingLoopEffects
from Script.FactoryGame import StopIdlingLoopEffects
from Game.FactoryGame.Buildable.Factory.OilPump.Audio.Stop_F_Pump_Oil_Pump_Engine import Stop_F_Pump_Oil_Pump_Engine
from Game.FactoryGame.Buildable.Factory.OilPump.Audio.Play_F_Pump_Oil_GasFire_Small import Play_F_Pump_Oil_GasFire_Small
from Script.AkAudio import AkComponent
from Script.FactoryGame import GainedSignificance
from Script.FactoryGame import StopProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.OilPump.Build_OilPump import ExecuteUbergraph_Build_OilPump.K2Node_Event_didLosePower
from Game.FactoryGame.Buildable.Factory.OilPump.Audio.Play_F_Pump_Oil_Pump_Engine import Play_F_Pump_Oil_Pump_Engine

class Build_OilPump(FGBuildableResourceExtractor):
    mBurnerFlameVfx: Ptr[ParticleSystemComponent]
    mExtractStartupTime = -10
    mExtractStartupTimer = 10
    mExtractCycleTime = 1
    mItemsPerCycle = 2000
    mAllowedResourceForms = ['EResourceForm::RF_LIQUID']
    mOnlyAllowCertainResources = True
    mAllowedResources = ['/Game/FactoryGame/Resource/RawResources/CrudeOil/Desc_LiquidOil.Desc_LiquidOil_C']
    mMustPlaceOnResourceDisqualifier = NewObject[FGCDNeedsResourceNode]()
    mPowerConsumption = 40
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
    mDisplayName = NSLOCTEXT("", "C86F1CAE473C8311D399909A494C8CF2", "Oil Extractor")
    mDescription = NSLOCTEXT("", "F4186916492BB7F4CE5AD89DB595A029", "Normal extraction rate: 120m³ oil per minute.\r\nHead Lift: 10 meters.\r\n(Allows fluids to be transported 10 meters upwards.)\r\n\r\nCan be build on an Oil Node to extract Crude Oil. Extraction rates depend on node purity.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[BPW_ExtractorPump]()
    mIsUseable = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def GetExtractedResource(self):
        ReturnValue: TScriptInterface[FGExtractableResourceInterface] = self.GetExtractableResource()
        ReturnValue_0: TSubclassOf[FGResourceDescriptor] = GetInterfaceUObject(ReturnValue).GetResourceClass()
        Resource = ReturnValue_0
    

    def SetDisplayText(self, newText: FText):
        pass
    

    def StopIdlingLoopEffects(self):
        ExecuteUbergraph_Build_OilPump.K2Node_Event_didLosePower = didLosePower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_OilPump(1772)
    

    def StopProductionLoopEffects(self):
        ExecuteUbergraph_Build_OilPump.K2Node_Event_didStopProducing = didStopProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_OilPump(120)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Build_OilPump(830)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_OilPump(895)
    

    def StartIdlingLoopEffects(self):
        ExecuteUbergraph_Build_OilPump.K2Node_Event_didGainPower = didGainPower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_OilPump(900)
    

    def StartProductionLoopEffects(self):
        ExecuteUbergraph_Build_OilPump.K2Node_Event_didStartProducing = didStartProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_OilPump(1636)
    

    def ExecuteUbergraph_Build_OilPump(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.TryStopProductionLoopEffects(False)
        # Label 26
        self.TryStopIdlingLoopEffects(False)
        goto(ExecutionFlow.Pop())
        # Label 38
        ReturnValue: bool = self.HasPower()
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        goto('L26')
        # Label 77
        ReturnValue_0: bool = self.IsProducing()
        if not ReturnValue_0:
            goto('L38')
        goto('L15')
        self.StopProductionLoopEffects(didStopProducing)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mBurnerFlameVfx)
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L250")
        self.mBurnerFlameVfx.K2_DestroyComponent(self)
        self.mBurnerFlameVfx = None
        goto(ExecutionFlow.Pop())
        # Label 250
        ReturnValue13: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Pump_Oil_GasFire_Small, self.MainMesh, "burnerVfxSocket", True)
        ReturnValue12: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Pump_Oil_Liquid_Bubbles, self.MainMesh, "DrillBottom", True)
        ReturnValue11: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Pump_Oil_Pump_Rattle_Bass, self.MainMesh, "drillside", True)
        ReturnValue10: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Pump_Oil_Liquid_Loop_LPF, self.MainMesh, "pipe_01", True)
        ReturnValue9: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Pump_Oil_Pump_Rattle_Light, self.MainMesh, "pipe_01", True)
        ReturnValue8: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Pump_Oil_Pump_Engine, self.MainMesh, "DrillBottom", True)
        ReturnValue7: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_F_Pump_Oil_Liquid_Loop_LPF, self.MainMesh, "AudioSocketGround", True)
        goto(ExecutionFlow.Pop())
        # Label 769
        ReturnValue1_0: bool = self.IsProducing()
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        self.TryStartProductionLoopEffects(False)
        goto(ExecutionFlow.Pop())
        # Label 815
        self.LostSignificance()
        goto('L77')
        goto('L815')
        # Label 835
        self.GainedSignificance()
        ReturnValue1_1: bool = self.HasPower()
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        self.TryStartIdlingLoopEffects(False)
        goto('L769')
        goto('L835')
        self.StartIdlingLoopEffects(didGainPower)
        self.MainMesh.SetScalarParameterValueOnMaterials("HasPower", 1)
        goto(ExecutionFlow.Pop())
        # Label 970
        ReturnValue_1: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(BurnerFire, self.MainMesh, "burnerVfxSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mBurnerFlameVfx = ReturnValue_1
        goto(ExecutionFlow.Pop())
        # Label 1107
        ExecutionFlow.Push("L1117")
        goto('L970')
        # Label 1117
        ReturnValue6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Pump_Oil_GasFire_Small, self.MainMesh, "burnerVfxSocket", True)
        ReturnValue5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Pump_Oil_Liquid_Loop_LPF, self.MainMesh, "AudioSocketGround", True)
        ReturnValue4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Pump_Oil_Liquid_Bubbles, self.MainMesh, "DrillBottom", True)
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Pump_Oil_Pump_Rattle_Bass, self.MainMesh, "drillside", True)
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Pump_Oil_Liquid_Loop_LPF, self.MainMesh, "pipe_01", True)
        ReturnValue1_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Pump_Oil_Pump_Rattle_Light, self.MainMesh, "pipe_01", True)
        ReturnValue_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_F_Pump_Oil_Pump_Engine, self.MainMesh, "DrillBottom", True)
        goto(ExecutionFlow.Pop())
        self.StartProductionLoopEffects(didStartProducing)
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(self.mBurnerFlameVfx)
        if not ReturnValue_3:
            goto('L1107')
        goto(ExecutionFlow.Pop())
        # Label 1721
        self.MainMesh.SetScalarParameterValueOnMaterials("HasPower", 0)
        goto(ExecutionFlow.Pop())
        self.StopIdlingLoopEffects(didLosePower)
        goto('L1721')
    
