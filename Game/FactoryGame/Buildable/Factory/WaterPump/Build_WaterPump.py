
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.WaterPump.Build_WaterPump import ExecuteUbergraph_Build_WaterPump
from Script.FactoryGame import FGBuildableResourceExtractor
from Script.Engine import ReceiveDestroyed
from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Script.Engine import SceneComponent
from Game.FactoryGame.Buildable.Factory.WaterPump.Build_WaterPump import ExecuteUbergraph_Build_WaterPump.K2Node_Event_didStopProducing
from Script.Engine import PlayFromStart
from Game.FactoryGame.Buildable.Factory.WaterPump.Audio.Stop_WaterPump_UnderWater_Turbine import Stop_WaterPump_UnderWater_Turbine
from Script.Engine import SpawnEmitterAtLocation
from Script.Engine import SpawnEmitterAttached
from Script.CoreUObject import Rotator
from Script.Engine import SetComponentTickInterval
from Script.Engine import K2_SetTimer
from Script.FactoryGame import TryStopProductionLoopEffects
from Game.FactoryGame.VFX.Factory.Waterpump.P_WaterPump_Chimney import P_WaterPump_Chimney
from Script.Engine import ReceiveBeginPlay
from Game.FactoryGame.VFX.Factory.Waterpump.P_WaterPump_Production import P_WaterPump_Production
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Script.Engine import ETimelineDirection
from Script.FactoryGame import StartProductionLoopEffects
from Game.FactoryGame.Buildable.Factory.WaterPump.Audio.Stop_WaterPump_Loop import Stop_WaterPump_Loop
from Game.FactoryGame.Buildable.Factory.WaterPump.Build_WaterPump import ExecuteUbergraph_Build_WaterPump.K2Node_Event_newIsProducing
from Script.FactoryGame import TryStartProductionLoopEffects
from Game.FactoryGame.VFX.Factory.Waterpump.P_WaterPumpSplash import P_WaterPumpSplash
from Script.Engine import TimerHandle
from Script.Engine import GreaterEqual_FloatFloat
from Script.Engine import IsValid
from Script.Engine import K2_GetRootComponent
from Game.FactoryGame.Buildable.Factory.WaterPump.Audio.Play_WaterPump_UnderWater_Turbine import Play_WaterPump_UnderWater_Turbine
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import GetIsSignificant
from Script.CoreUObject import Vector
from Script.Engine import Stop
from Script.Engine import K2_GetComponentRotation
from Script.Engine import K2_GetComponentLocation
from Game.FactoryGame.Buildable.Factory.WaterPump.Build_WaterPump import ExecuteUbergraph_Build_WaterPump.K2Node_Event_didStartProducing
from Script.Engine import Reverse
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import SetPlayRate
from Script.AkAudio import PostAkEventAttached
from Script.Engine import K2_DestroyComponent
from Game.FactoryGame.Buildable.Factory.WaterPump.Audio.Play_WaterPump_Loop import Play_WaterPump_Loop
from Script.FactoryGame import LostSignificance
from Script.Engine import ParticleSystemComponent
from Script.FactoryGame import OnIsProducingChanged
from Script.Engine import SetFloatParameter
from Script.Engine import MapRangeClamped
from Script.AkAudio import SeekOnEventBySeconds
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.FactoryGame import FGFAnimInstanceFactory
from Script.FactoryGame import StopProductionLoopEffects
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.AkAudio import SetRTPCValue
from Game.FactoryGame.VFX.Factory.Waterpump.P_WaterPump_Waves import P_WaterPump_Waves
from Script.FactoryGame import GainedSignificance
from Game.FactoryGame.Buildable.Factory.WaterPump.Audio.Stop_WaterPump_LostSignificance import Stop_WaterPump_LostSignificance

class Build_WaterPump(FGBuildableResourceExtractor):
    mWaterpumpTimeline_RTPC_B8FA6F944E717E3B7A286E84901F620E: float
    mWaterpumpTimeline__Direction_B8FA6F944E717E3B7A286E84901F620E: uint8
    PlayPitchAndVolumeRTPCTimeline_RTPC_2B435F41466C37D2AD809A88AA21BA89: float
    PlayPitchAndVolumeRTPCTimeline__Direction_2B435F41466C37D2AD809A88AA21BA89: uint8
    mAudioTimerCounter: float
    mAudioTimerMS: float = 0.10000000149011612
    mAudioTimerReference: TimerHandle
    P_WaterEngineTurbulence: Ptr[ParticleSystemComponent]
    P_WaterPump_Production: Ptr[ParticleSystemComponent]
    P_WaterPump_Chimney: Ptr[ParticleSystemComponent]
    P_WaterPump_Waves: Ptr[ParticleSystemComponent]
    mAudioTimelineCounter: float
    HasLostSignificance: bool
    SFXWaterPumpUnderwaterTurbine: Ptr[AkComponent]
    mSFXWaterPumpEngine: Ptr[AkComponent]
    mExtractStartupTime = 10
    mExtractStartupTimer = 10
    mExtractCycleTime = 1
    mItemsPerCycle = 2000
    mAllowedResourceForms = ['EResourceForm::RF_LIQUID']
    mRequireResourceAtMinimumDepthChecks = True
    mMinimumDepthForPlacement = 50
    mDepthTraceOriginOffset = Namespace(X=0, Y=300, Z=200)
    mOnlyAllowCertainResources = True
    mAllowedResources = ['/Game/FactoryGame/Resource/RawResources/Water/Desc_Water.Desc_Water_C']
    mMustPlaceOnResourceDisqualifier = NewObject[FGCDNeedsWaterVolume]()
    mPowerConsumption = 20
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
    mFluidStackSizeMultiplier = 4
    mAddToSignificanceManager = True
    mSignificanceRange = 18000
    mHologramClass = NewObject[FGResourceExtractorHologram]()
    mDisplayName = NSLOCTEXT("", "D8ACD2BE4630860B9B040696FFAE4FE1", "Water Extractor")
    mDescription = NSLOCTEXT("", "12DEA49B42343EB1FAC2B3B27C56FA4F", "Default extraction rate: 120m³ water per minute.\r\nHead Lift: 10 meters.\r\n(Allows fluids to be transported 10 meters upwards.)\r\n\r\nExtracts water from the body of water it is build on.\r\nNote that the water needs to be deep enough and that rivers do not commonly suffice.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/WaterPump/MaterialEffect_WaterPump.MaterialEffect_WaterPump_C', SubPathString='')
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
    
    def GetPlayRate(self):
        ReturnValue: Ptr[AnimInstance] = self.MainMesh.GetAnimInstance()
        Factory: Ptr[FGFAnimInstanceFactory] = Cast[FGFAnimInstanceFactory](ReturnValue)
        bSuccess: bool = Factory
        PlayRate = Factory.mProxy.mAnimPlayRate
    

    def mAudioTimer(self):
        ReturnValue: float = self.mAudioTimerCounter + self.mAudioTimerMS
        self.mAudioTimerCounter = ReturnValue
        ReturnValue_0: bool = GreaterEqual_FloatFloat(self.mAudioTimerCounter, 18.5)
        if not ReturnValue_0:
            goto('L163')
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mAudioTimerReference])
    

    def SetText(self, intText: FString):
        pass
    

    def PlayPitchAndVolumeRTPCTimeline__FinishedFunc(self):
        self.ExecuteUbergraph_Build_WaterPump(4753)
    

    def PlayPitchAndVolumeRTPCTimeline__UpdateFunc(self):
        self.ExecuteUbergraph_Build_WaterPump(4368)
    

    def mWaterpumpTimeline__FinishedFunc(self):
        self.ExecuteUbergraph_Build_WaterPump(3902)
    

    def mWaterpumpTimeline__UpdateFunc(self):
        self.ExecuteUbergraph_Build_WaterPump(3729)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Build_WaterPump(4363)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_Build_WaterPump(143)
    

    def StopProductionLoopEffects(self):
        ExecuteUbergraph_Build_WaterPump.K2Node_Event_didStopProducing = didStopProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_WaterPump(1646)
    

    def PlayProducingSounds(self):
        self.ExecuteUbergraph_Build_WaterPump(2380)
    

    def StartProductionLoopEffects(self):
        ExecuteUbergraph_Build_WaterPump.K2Node_Event_didStartProducing = didStartProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_WaterPump(2415)
    

    def StartVFXIteration(self):
        self.ExecuteUbergraph_Build_WaterPump(3724)
    

    def OnIsProducingChanged(self):
        ExecuteUbergraph_Build_WaterPump.K2Node_Event_newIsProducing = newIsProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_WaterPump(4169)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_WaterPump(4599)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Build_WaterPump(4748)
    

    def Start_VFX_Loop(self):
        self.ExecuteUbergraph_Build_WaterPump(4758)
    

    def Stop_VFX_Loop(self):
        self.ExecuteUbergraph_Build_WaterPump(4763)
    

    def ExecuteUbergraph_Build_WaterPump(self):
        goto(ComputedJump("EntryPoint"))
        ReturnValue4: bool = self.IsProducing()
        if not ReturnValue4:
            goto('L128')
        self.P_WaterPump_Chimney.Activate(False)
        self.P_WaterPump_Production.Activate(False)
        goto(ExecutionFlow.Pop())
        # Label 128
        self.Stop_VFX_Loop()
        goto(ExecutionFlow.Pop())
        self.ReceiveDestroyed()
        self.P_WaterPump_Waves.K2_DestroyComponent(self)
        self.P_WaterEngineTurbulence.K2_DestroyComponent(self)
        self.P_WaterPump_Production.K2_DestroyComponent(self)
        self.P_WaterPump_Chimney.K2_DestroyComponent(self)
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_WaterPump_UnderWater_Turbine, self.PumpSound, "None", True)
        goto(ExecutionFlow.Pop())
        # Label 360
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.P_WaterPump_Production)
        if not ReturnValue:
            goto('L426')
        goto(ExecutionFlow.Pop())
        # Label 426
        ReturnValue_0: Ptr[SceneComponent] = self.K2_GetRootComponent()
        ReturnValue_1: Rotator = ReturnValue_0.K2_GetComponentRotation()
        ReturnValue_2: Vector = ReturnValue_0.K2_GetComponentLocation()
        ReturnValue_3: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_WaterPump_Production, ReturnValue_2, ReturnValue_1, Vector(1, 1, 1), False, 0)
        self.P_WaterPump_Production = ReturnValue_3
        ReturnValue_4: Vector = self.FGColoredInstanceMeshProxy.GetSocketLocation("filter_VFX_Socket")
        ReturnValue_5: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_WaterPump_Chimney, self.FGColoredInstanceMeshProxy, "filter_VFX_Socket", ReturnValue_4, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 1, False, 0)
        self.P_WaterPump_Chimney = ReturnValue_5
        ReturnValue2: bool = Default__KismetSystemLibrary.IsValid(self.P_WaterEngineTurbulence)
        if not ReturnValue2:
            goto('L916')
        goto(ExecutionFlow.Pop())
        # Label 916
        ReturnValue2_0: Ptr[SceneComponent] = self.K2_GetRootComponent()
        ReturnValue2_1: Rotator = ReturnValue2_0.K2_GetComponentRotation()
        ReturnValue2_2: Vector = ReturnValue2_0.K2_GetComponentLocation()
        ReturnValue2_3: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_WaterPumpSplash, ReturnValue2_2, ReturnValue2_1, Vector(1, 1, 1), False, 0)
        self.P_WaterEngineTurbulence = ReturnValue2_3
        goto(ExecutionFlow.Pop())
        # Label 1142
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(self.P_WaterPump_Production)
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        self.P_WaterPump_Production.Activate(False)
        self.P_WaterPump_Chimney.Activate(False)
        self.P_WaterEngineTurbulence.Activate(False)
        goto(ExecutionFlow.Pop())
        # Label 1315
        ReturnValue_6: bool = self.PlayPitchAndVolumeRTPCTimeline_RTPC_2B435F41466C37D2AD809A88AA21BA89 <= 0
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        ReturnValue_7: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_WaterPump_UnderWater_Turbine, self.PumpSound, "None", True)
        self.P_WaterPump_Chimney.Deactivate()
        self.P_WaterPump_Production.Deactivate()
        self.P_WaterEngineTurbulence.Deactivate()
        goto(ExecutionFlow.Pop())
        # Label 1542
        self.mWaterpumpTimeline.Reverse()
        goto(ExecutionFlow.Pop())
        # Label 1575
        self.mWaterpumpTimeline.PlayFromStart()
        goto(ExecutionFlow.Pop())
        # Label 1608
        self.PlayPitchAndVolumeRTPCTimeline.SetComponentTickInterval(0.10000000149011612)
        goto(ExecutionFlow.Pop())
        self.StopProductionLoopEffects(didStopProducing)
        ReturnValue_8: bool = Not_PreBool(didStopProducing)
        self.HasLostSignificance = ReturnValue_8
        if not didStopProducing:
            goto('L2155')
        ReturnValue2_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_WaterPump_Loop, self, True)
        ReturnValue1_1: float = MapRangeClamped(self.mAudioTimerCounter, 0, 18.5, 0, 10.399999618530273)
        ReturnValue_9: float = 10.399999618530273 - ReturnValue1_1
        ReturnValue1_2: bool = ReturnValue2_4.SeekOnEventBySeconds(Stop_WaterPump_Loop, ReturnValue_9, False, 0)
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mAudioTimerReference])
        self.mAudioTimerCounter = 0
        ReturnValue7: bool = Default__KismetSystemLibrary.IsValid(self.SFXWaterPumpUnderwaterTurbine)
        if not ReturnValue7:
           goto(ExecutionFlow.Pop())
        ReturnValue_10: float = 1 / 10
        self.mWaterpumpTimeline.SetPlayRate(ReturnValue_10)
        goto('L1542')
        # Label 2155
        self.PlayPitchAndVolumeRTPCTimeline.Stop()
        ReturnValue_11: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_WaterPump_LostSignificance, self, True)
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mAudioTimerReference])
        ReturnValue2_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_WaterPump_UnderWater_Turbine, self.PumpSound, "None", True)
        self.mAudioTimerCounter = 0
        goto(ExecutionFlow.Pop())
        ReturnValue3: bool = self.IsProducing()
        if not ReturnValue3:
           goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        self.StartProductionLoopEffects(didStartProducing)
        ReturnValue1_3: bool = Not_PreBool(didStartProducing)
        self.HasLostSignificance = ReturnValue1_3
        ExecutionFlow.Push("L2502")
        self.Start_VFX_Loop()
        goto(ExecutionFlow.Pop())
        # Label 2502
        if not didStartProducing:
            goto('L2951')
        ReturnValue1_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_WaterPump_Loop, self, True)
        self.mSFXWaterPumpEngine = ReturnValue1_4
        ReturnValue_12: TimerHandle = Default__KismetSystemLibrary.K2_SetTimer(self, "mAudioTimer", self.mAudioTimerMS, True)
        self.mAudioTimerReference = ReturnValue_12
        # Label 2689
        ReturnValue6: bool = Default__KismetSystemLibrary.IsValid(self.SFXWaterPumpUnderwaterTurbine)
        if not ReturnValue6:
            goto('L3113')
        # Label 2754
        Variable: float = 18.5
        Variable1: float = 0.10000000149011612
        Variable_0: bool = self.HasLostSignificance
        
        switch = {
            False: Variable,
            True: Variable1
        }
        ReturnValue1_5: float = 1 / switch.get(Variable_0, None)
        self.mWaterpumpTimeline.SetPlayRate(ReturnValue1_5)
        goto('L1575')
        # Label 2951
        ReturnValue3_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_WaterPump_Loop, self, True)
        self.mSFXWaterPumpEngine = ReturnValue3_0
        ReturnValue_13: bool = self.mSFXWaterPumpEngine.SeekOnEventBySeconds(Play_WaterPump_Loop, 20, False, 0)
        self.mAudioTimerCounter = 18.5
        goto('L2689')
        # Label 3113
        ReturnValue3_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_WaterPump_UnderWater_Turbine, self.PumpSound, "None", True)
        self.SFXWaterPumpUnderwaterTurbine = ReturnValue3_1
        goto('L2754')
        # Label 3211
        ReturnValue_14: float = MapRangeClamped(self.PlayPitchAndVolumeRTPCTimeline_RTPC_2B435F41466C37D2AD809A88AA21BA89, 0, 100, 0, 1)
        self.P_WaterEngineTurbulence.SetFloatParameter("Opacity", ReturnValue_14)
        goto(ExecutionFlow.Pop())
        # Label 3323
        self.P_WaterEngineTurbulence.K2_DestroyComponent(self)
        # Label 3356
        ReturnValue4_0: bool = Default__KismetSystemLibrary.IsValid(self.P_WaterPump_Production)
        if not ReturnValue4_0:
            goto('L3454')
        self.P_WaterPump_Production.K2_DestroyComponent(self)
        # Label 3454
        ReturnValue5: bool = Default__KismetSystemLibrary.IsValid(self.P_WaterPump_Chimney)
        if not ReturnValue5:
           goto(ExecutionFlow.Pop())
        self.P_WaterPump_Chimney.K2_DestroyComponent(self)
        goto(ExecutionFlow.Pop())
        # Label 3549
        ReturnValue3_2: bool = Default__KismetSystemLibrary.IsValid(self.P_WaterEngineTurbulence)
        if not ReturnValue3_2:
            goto('L3356')
        goto('L3323')
        # Label 3619
        ReturnValue_15: bool = self.IsProducing()
        if not ReturnValue_15:
           goto(ExecutionFlow.Pop())
        goto('L360')
        # Label 3658
        self.SFXWaterPumpUnderwaterTurbine.SetRTPCValue("WaterPumpRTPC", self.PlayPitchAndVolumeRTPCTimeline_RTPC_2B435F41466C37D2AD809A88AA21BA89, 0)
        goto('L3211')
        goto('L1142')
        self.SFXWaterPumpUnderwaterTurbine.SetRTPCValue("WaterPumpRTPC", self.mWaterpumpTimeline_RTPC_B8FA6F944E717E3B7A286E84901F620E, 0)
        ReturnValue2_6: float = MapRangeClamped(self.mWaterpumpTimeline_RTPC_B8FA6F944E717E3B7A286E84901F620E, 0, 100, 0, 1)
        self.P_WaterEngineTurbulence.SetFloatParameter("Opacity", ReturnValue2_6)
        goto(ExecutionFlow.Pop())
        ReturnValue1_6: bool = self.mWaterpumpTimeline_RTPC_B8FA6F944E717E3B7A286E84901F620E <= 0
        if not ReturnValue1_6:
           goto(ExecutionFlow.Pop())
        self.P_WaterPump_Chimney.Deactivate()
        self.P_WaterPump_Production.Deactivate()
        ReturnValue4_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_WaterPump_UnderWater_Turbine, self.PumpSound, "None", True)
        Default__KismetSystemLibrary.Delay(self, 3, LatentActionInfo(Linkage = 15, UUID = -799117556, ExecutionFunction = "ExecuteUbergraph_Build_WaterPump", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.OnIsProducingChanged(newIsProducing)
        ReturnValue_16: bool = self.GetIsSignificant()
        if not ReturnValue_16:
           goto(ExecutionFlow.Pop())
        if not newIsProducing:
            goto('L4244')
        self.TryStartProductionLoopEffects(True)
        goto(ExecutionFlow.Pop())
        # Label 4244
        self.TryStopProductionLoopEffects(True)
        goto(ExecutionFlow.Pop())
        # Label 4256
        ReturnValue1_7: bool = self.IsProducing()
        if not ReturnValue1_7:
           goto(ExecutionFlow.Pop())
        self.TryStartProductionLoopEffects(False)
        goto(ExecutionFlow.Pop())
        # Label 4302
        ReturnValue2_7: bool = self.IsProducing()
        if not ReturnValue2_7:
           goto(ExecutionFlow.Pop())
        self.TryStopProductionLoopEffects(False)
        goto(ExecutionFlow.Pop())
        # Label 4348
        self.ReceiveBeginPlay()
        goto('L1608')
        goto('L4348')
        goto('L3658')
        # Label 4373
        ReturnValue1_8: Ptr[SceneComponent] = self.K2_GetRootComponent()
        ReturnValue1_9: Rotator = ReturnValue1_8.K2_GetComponentRotation()
        ReturnValue1_10: Vector = ReturnValue1_8.K2_GetComponentLocation()
        ReturnValue1_11: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_WaterPump_Waves, ReturnValue1_10, ReturnValue1_9, Vector(1, 1, 1), False, 0)
        self.P_WaterPump_Waves = ReturnValue1_11
        goto(ExecutionFlow.Pop())
        self.GainedSignificance()
        ExecutionFlow.Push("L4256")
        goto('L4373')
        # Label 4619
        self.LostSignificance()
        ExecutionFlow.Push("L4639")
        goto('L4302')
        # Label 4639
        ReturnValue8: bool = Default__KismetSystemLibrary.IsValid(self.P_WaterPump_Waves)
        if not ReturnValue8:
           goto(ExecutionFlow.Pop())
        self.P_WaterPump_Waves.K2_DestroyComponent(self)
        self.Stop_VFX_Loop()
        goto(ExecutionFlow.Pop())
        goto('L4619')
        goto('L1315')
        goto('L3619')
        goto('L3549')
    
