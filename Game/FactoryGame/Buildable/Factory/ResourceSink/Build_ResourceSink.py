
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.ResourceSink.Audio.Play_ResourceSink_Engine import Play_ResourceSink_Engine
from Script.Engine import ReceiveDestroyed
from Script.AkAudio import PostAkEvent
from Script.Engine import PlayFromStart
from Script.AkAudio import SetActorRTPCValue
from Game.FactoryGame.Buildable.Factory.ResourceSink.Build_ResourceSink import ExecuteUbergraph_Build_ResourceSink.K2Node_Event_didGainPower
from Script.Engine import SpawnEmitterAttached
from Script.CoreUObject import Rotator
from Game.FactoryGame.Buildable.Factory.ResourceSink.Build_ResourceSink import ExecuteUbergraph_Build_ResourceSink.K2Node_Event_didStopProducing
from Script.Engine import MaterialInstanceDynamic
from Script.Engine import SetComponentTickInterval
from Script.FactoryGame import TryStopProductionLoopEffects
from Script.Engine import ReceiveBeginPlay
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import EqualEqual_FloatFloat
from Script.Engine import ETimelineDirection
from Script.FactoryGame import StartProductionLoopEffects
from Script.FactoryGame import FGBuildableResourceSink
from Script.FactoryGame import TryStartProductionLoopEffects
from Script.Engine import IsValid
from Script.Engine import Play
from Game.FactoryGame.Buildable.Factory.ResourceSink.Audio.Play_ResourceSink_Debris import Play_ResourceSink_Debris
from Game.FactoryGame.Buildable.Factory.ResourceSink.Build_ResourceSink import ExecuteUbergraph_Build_ResourceSink.K2Node_Event_newHasPower
from Game.FactoryGame.Buildable.Factory.ResourceSink.Audio.Stop_ResourceSink_Engine import Stop_ResourceSink_Engine
from Game.FactoryGame.Buildable.Factory.ResourceSink.Audio.Play_ResourceSink_Grinder import Play_ResourceSink_Grinder
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import TryStartIdlingLoopEffects
from Game.FactoryGame.Buildable.Factory.ResourceSink.Audio.Stop_ResourceSink_Debris import Stop_ResourceSink_Debris
from Game.FactoryGame.Buildable.Factory.ResourceSink.Build_ResourceSink import ExecuteUbergraph_Build_ResourceSink.K2Node_CustomEvent_didLosePower
from Script.FactoryGame import OnHasPowerChanged
from Script.FactoryGame import GetIsSignificant
from Script.CoreUObject import Vector
from Game.FactoryGame.Buildable.Factory.ResourceSink.Build_ResourceSink import ExecuteUbergraph_Build_ResourceSink.K2Node_Event_didLosePower
from Game.FactoryGame.VFX.Factory.ResourceSink.P_ResourceSink_Producing_01 import P_ResourceSink_Producing_01
from Script.Engine import Reverse
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.Factory.ResourceSink.Build_ResourceSink import ExecuteUbergraph_Build_ResourceSink.K2Node_Event_didStartProducing
from Script.Engine import SetPlayRate
from Script.FactoryGame import TryStopIdlingLoopEffects
from Script.AkAudio import PostAkEventAttached
from Script.Engine import K2_DestroyComponent
from Game.FactoryGame.Buildable.Factory.ResourceSink.Audio.Stop_ResourceSink_Grinder import Stop_ResourceSink_Grinder
from Script.FactoryGame import LostSignificance
from Script.Engine import ParticleSystemComponent
from Script.FactoryGame import StartIdlingLoopEffects
from Script.FactoryGame import StopIdlingLoopEffects
from Script.Engine import SetFloatParameter
from Script.Engine import MapRangeClamped
from Script.AkAudio import AkComponent
from Script.FactoryGame import GainedSignificance
from Script.FactoryGame import StopProductionLoopEffects
from Script.AkAudio import SetRTPCValue
from Game.FactoryGame.Buildable.Factory.ResourceSink.Build_ResourceSink import ExecuteUbergraph_Build_ResourceSink
from Game.FactoryGame.Buildable.Factory.ResourceSink.Build_ResourceSink import ExecuteUbergraph_Build_ResourceSink.K2Node_CustomEvent_didGainPower

class Build_ResourceSink(FGBuildableResourceSink):
    SFXEngineTimeline_EngineAlpha_073E1D2A4BAD246B3958E183E210FAAE: float
    SFXEngineTimeline__Direction_073E1D2A4BAD246B3958E183E210FAAE: uint8
    VFX_SFX_Timeline_EngineAlpha_A2CB706E440839665A39888572D206AA: float
    VFX_SFX_Timeline__Direction_A2CB706E440839665A39888572D206AA: uint8
    mP_Production_VFX: Ptr[ParticleSystemComponent]
    VFX_Material: Ptr[MaterialInstanceDynamic]
    SFX_ResourceSinkEngine: Ptr[AkComponent]
    SFX_ResourceSinkGrinder: Ptr[AkComponent]
    HastLostSignificance: bool
    SFX_ResourceSinkDebris: Ptr[AkComponent]
    mProcessingTime = 3
    mPowerConsumption = 30
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
    mHologramClass = NewObject[FGFactoryHologram]()
    mDisplayName = NSLOCTEXT("", "7EF9CDA1441086A8E94D6A984AF35EE8", "AWESOME Sink")
    mDescription = NSLOCTEXT("", "EBCE338946258919C03A0BB706968BC4", "Got excess resources? Fear not, for FICSIT does not waste! The newly developed AWESOME Sink turns any useful part straight into research data, as fast as you can supply it! \r\nParticipating pioneers will be compensated with Coupons to be spend at the AWESOME Shop.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[BPW_ResourceSink]()
    mIsUseable = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def VFX/SFX_Timeline__FinishedFunc(self):
        self.ExecuteUbergraph_Build_ResourceSink(3526)
    

    def VFX/SFX_Timeline__UpdateFunc(self):
        self.ExecuteUbergraph_Build_ResourceSink(3521)
    

    def SFXEngineTimeline__FinishedFunc(self):
        self.ExecuteUbergraph_Build_ResourceSink(1110)
    

    def SFXEngineTimeline__UpdateFunc(self):
        self.ExecuteUbergraph_Build_ResourceSink(10)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_ResourceSink(75)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Build_ResourceSink(188)
    

    def OnHasPowerChanged(self):
        ExecuteUbergraph_Build_ResourceSink.K2Node_Event_newHasPower = newHasPower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_ResourceSink(1314)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Build_ResourceSink(1413)
    

    def StartProductionLoopEffects(self):
        ExecuteUbergraph_Build_ResourceSink.K2Node_Event_didStartProducing = didStartProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_ResourceSink(1836)
    

    def StopProductionLoopEffects(self):
        ExecuteUbergraph_Build_ResourceSink.K2Node_Event_didStopProducing = didStopProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_ResourceSink(2109)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_Build_ResourceSink(2650)
    

    def StartSFXEngineOnPower(self, didGainPower: bool):
        ExecuteUbergraph_Build_ResourceSink.K2Node_CustomEvent_didGainPower = didGainPower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_ResourceSink(3345)
    

    def StopSFXEngineOnPower(self, didLosePower: bool):
        ExecuteUbergraph_Build_ResourceSink.K2Node_CustomEvent_didLosePower = didLosePower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_ResourceSink(3350)
    

    def StartIdlingLoopEffects(self):
        ExecuteUbergraph_Build_ResourceSink.K2Node_Event_didGainPower = didGainPower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_ResourceSink(3427)
    

    def StopIdlingLoopEffects(self):
        ExecuteUbergraph_Build_ResourceSink.K2Node_Event_didLosePower = didLosePower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_ResourceSink(3474)
    

    def ExecuteUbergraph_Build_ResourceSink(self):
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_ResourceSink_Engine", self.SFXEngineTimeline_EngineAlpha_073E1D2A4BAD246B3958E183E210FAAE, 0, self)
        # End
        self.GainedSignificance()
        ReturnValue1: bool = self.HasPower()
        if not ReturnValue1:
            goto('L3531')
        self.TryStartIdlingLoopEffects(False)
        ReturnValue: bool = self.IsProducing()
        if not ReturnValue:
            goto('L3531')
        self.TryStartProductionLoopEffects(False)
        # End
        self.LostSignificance()
        ReturnValue2: bool = self.HasPower()
        ReturnValue1_0: bool = self.IsProducing()
        ReturnValue_0: bool = ReturnValue1_0 and ReturnValue2
        if not ReturnValue_0:
            goto('L325')
        self.TryStopProductionLoopEffects(False)
        # Label 309
        self.TryStopIdlingLoopEffects(False)
        # End
        # Label 325
        ReturnValue2 = self.HasPower()
        if not ReturnValue2:
            goto('L3531')
        goto('L309')
        # Label 368
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(self.mP_Production_VFX)
        if not ReturnValue_1:
            goto('L3531')
        ReturnValue_2: float = 1 / 5
        self.VFX/SFX_Timeline.SetPlayRate(ReturnValue_2)
        self.VFX/SFX_Timeline.Reverse()
        # End
        # Label 549
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValid(self.mP_Production_VFX)
        if not ReturnValue1_1:
            goto('L843')
        # Label 614
        Variable: bool = self.HastLostSignificance
        Variable2: float = 5
        Variable3: float = 0.10000000149011612
        
        switch = {
            False: Variable2,
            True: Variable3
        }
        ReturnValue3: float = 1 / switch.get(Variable, None)
        self.VFX/SFX_Timeline.SetPlayRate(ReturnValue3)
        self.VFX/SFX_Timeline.PlayFromStart()
        # End
        # Label 843
        ReturnValue_3: Rotator = self.MainMesh.GetSocketRotation("VFX_Socket_Grinder")
        ReturnValue_4: Vector = self.MainMesh.GetSocketLocation("VFX_Socket_Grinder")
        ReturnValue_5: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_ResourceSink_Producing_01, self.MainMesh, "VFX_Socket_Grinder", ReturnValue_4, ReturnValue_3, Vector(1, 1, 1), 1, True, 0)
        self.mP_Production_VFX = ReturnValue_5
        goto('L614')
        ReturnValue1_2: bool = EqualEqual_FloatFloat(self.SFXEngineTimeline_EngineAlpha_073E1D2A4BAD246B3958E183E210FAAE, 0)
        if not ReturnValue1_2:
            goto('L3531')
        ReturnValue1_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_ResourceSink_Engine, self, True)
        ReturnValue9: bool = Default__KismetSystemLibrary.IsValid(self.mP_Production_VFX)
        if not ReturnValue9:
            goto('L3531')
        self.mP_Production_VFX.K2_DestroyComponent(self)
        # End
        self.OnHasPowerChanged(newHasPower)
        ReturnValue_6: bool = self.GetIsSignificant()
        if not ReturnValue_6:
            goto('L3531')
        if not newHasPower:
            goto('L1397')
        self.TryStartIdlingLoopEffects(True)
        # End
        # Label 1397
        self.TryStopIdlingLoopEffects(True)
        # End
        self.ReceiveBeginPlay()
        self.VFX/SFX_Timeline.SetComponentTickInterval(0.10000000149011612)
        # End
        # Label 1465
        ReturnValue_7: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_ResourceSink_Engine, self, True)
        self.SFX_ResourceSinkEngine = ReturnValue_7
        # Label 1537
        Variable_0: float = 6
        Variable1: float = 0.10000000149011612
        Variable1_0: bool = self.HastLostSignificance
        
        switch_0 = {
            False: Variable_0,
            True: Variable1
        }
        ReturnValue2_0: float = 1 / switch_0.get(Variable1_0, None)
        self.SFXEngineTimeline.SetPlayRate(ReturnValue2_0)
        self.SFXEngineTimeline.Play()
        # End
        # Label 1766
        ReturnValue2_1: bool = Default__KismetSystemLibrary.IsValid(self.SFX_ResourceSinkEngine)
        if not ReturnValue2_1:
            goto('L1465')
        goto('L1537')
        self.StartProductionLoopEffects(didStartProducing)
        ReturnValue_8: bool = Not_PreBool(didStartProducing)
        self.HastLostSignificance = ReturnValue_8
        ReturnValue_9: bool = self.HasPower()
        if not ReturnValue_9:
            goto('L3531')
        ReturnValue5: bool = Default__KismetSystemLibrary.IsValid(self.SFX_ResourceSinkGrinder)
        if not ReturnValue5:
            goto('L2011')
        goto('L549')
        # Label 2011
        ReturnValue_10: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_ResourceSink_Grinder, self.GrinderSFXRef, "None", True)
        self.SFX_ResourceSinkGrinder = ReturnValue_10
        goto('L549')
        self.StopProductionLoopEffects(didStopProducing)
        ReturnValue1_4: bool = Not_PreBool(didStopProducing)
        self.HastLostSignificance = ReturnValue1_4
        if not didStopProducing:
            goto('L2334')
        ReturnValue7: bool = Default__KismetSystemLibrary.IsValid(self.SFX_ResourceSinkGrinder)
        if not ReturnValue7:
            goto('L368')
        ReturnValue2_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_ResourceSink_Debris, self.GrinderSFXRef, "None", True)
        goto('L368')
        # Label 2334
        ReturnValue8: bool = Default__KismetSystemLibrary.IsValid(self.SFX_ResourceSinkGrinder)
        if not ReturnValue8:
            goto('L2547')
        ReturnValue3_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_ResourceSink_Debris, self.GrinderSFXRef, "None", True)
        ReturnValue4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_ResourceSink_Grinder, self.GrinderSFXRef, "None", True)
        # Label 2547
        ReturnValue10: bool = Default__KismetSystemLibrary.IsValid(self.mP_Production_VFX)
        if not ReturnValue10:
            goto('L3531')
        self.mP_Production_VFX.K2_DestroyComponent(self)
        # End
        self.ReceiveDestroyed()
        ReturnValue3_1: bool = Default__KismetSystemLibrary.IsValid(self.mP_Production_VFX)
        if not ReturnValue3_1:
            goto('L3531')
        self.mP_Production_VFX.K2_DestroyComponent(self)
        # End
        # Label 2763
        self.SFXEngineTimeline.Reverse()
        # End
        # Label 2800
        ReturnValue1_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_ResourceSink_Debris, self.GrinderSFXRef, "None", True)
        # End
        # Label 2879
        ReturnValue4_0: bool = Default__KismetSystemLibrary.IsValid(self.SFX_ResourceSinkDebris)
        if not ReturnValue4_0:
            goto('L2800')
        # End
        # Label 2949
        ReturnValue_11: bool = EqualEqual_FloatFloat(self.VFX_SFX_Timeline_EngineAlpha_A2CB706E440839665A39888572D206AA, 100)
        if not ReturnValue_11:
            goto('L3531')
        goto('L2879')
        # Label 3002
        ReturnValue_12: float = MapRangeClamped(self.VFX_SFX_Timeline_EngineAlpha_A2CB706E440839665A39888572D206AA, 0, 100, 0, 1)
        self.mP_Production_VFX.SetFloatParameter("Opacity_Fade", ReturnValue_12)
        # End
        # Label 3118
        self.SFX_ResourceSinkGrinder.SetRTPCValue("RTPC_ResourceSink_Grinder", self.VFX_SFX_Timeline_EngineAlpha_A2CB706E440839665A39888572D206AA, 0)
        goto('L3002')
        # Label 3196
        ReturnValue6: bool = Default__KismetSystemLibrary.IsValid(self.SFX_ResourceSinkEngine)
        if not ReturnValue6:
            goto('L3531')
        ReturnValue1_6: float = 1 / 6
        self.SFXEngineTimeline.SetPlayRate(ReturnValue1_6)
        goto('L2763')
        goto('L1766')
        if not didLosePower:
            goto('L3369')
        goto('L3196')
        # Label 3369
        ReturnValue2_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_ResourceSink_Engine, self, True)
        # End
        self.StartIdlingLoopEffects(didGainPower)
        self.StartSFXEngineOnPower(didGainPower)
        # End
        self.StopIdlingLoopEffects(didLosePower)
        self.StopSFXEngineOnPower(didLosePower)
        # End
        goto('L3118')
        goto('L2949')
    
