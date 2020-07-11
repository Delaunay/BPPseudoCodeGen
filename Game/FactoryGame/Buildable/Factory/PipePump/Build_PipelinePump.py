
from codegen.ue4_stub import *

from Script.Engine import SetScalarParameterValue
from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Script.FactoryGame import StopIsLookedAtForDismantle
from Script.AkAudio import SetActorRTPCValue
from Script.FactoryGame import GetIndicatorFlowPct
from Game.FactoryGame.Buildable.Factory.PipePump.Audio.Stop_PipelinePump_Engine import Stop_PipelinePump_Engine
from Script.Engine import MaterialInstanceDynamic
from Script.Engine import K2_SetTimer
from Script.Engine import ReceiveBeginPlay
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetIndicatorHeadLift
from Script.Engine import Default__KismetArrayLibrary
from Script.CoreUObject import Color
from Script.Engine import SetVectorParameterValue
from Script.FactoryGame import FGBuildablePipelinePump
from Script.Engine import TimerHandle
from Script.Engine import GreaterEqual_FloatFloat
from Script.Engine import IsValid
from Script.Engine import UserConstructionScript
from Game.FactoryGame.Buildable.Factory.PipePump.Build_PipelinePump import ExecuteUbergraph_Build_PipelinePump.K2Node_Event_byCharacter
from Game.FactoryGame.Buildable.Factory.PipePump.Build_PipelinePump import ExecuteUbergraph_Build_PipelinePump
from Script.Engine import Conv_ColorToLinearColor
from Game.FactoryGame.Buildable.Factory.PipePump.Build_PipelinePump import ExecuteUbergraph_Build_PipelinePump.K2Node_Event_newHasPower
from Script.Engine import MaterialInterface
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import LostSignificance
from Game.FactoryGame.Buildable.Factory.PipePump.Build_PipelinePump import ExecuteUbergraph_Build_PipelinePump.K2Node_Event_fluidDesc
from Script.FactoryGame import GetIndicatorHeadLiftPct
from Script.FactoryGame import Default__FGItemDescriptor
from Game.FactoryGame.Buildable.Factory.PipePump.Build_PipelinePump import ExecuteUbergraph_Build_PipelinePump.K2Node_Event_DeltaSeconds
from Script.FactoryGame import FGItemDescriptor
from Game.FactoryGame.Buildable.Factory.PipePump.Audio.Play_PipelinePump_Pistons import Play_PipelinePump_Pistons
from Script.FactoryGame import GetFluidColor
from Script.AkAudio import AkComponent
from Script.FactoryGame import GainedSignificance
from Script.Engine import IsValidClass
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor
from Game.FactoryGame.Buildable.Factory.PipePump.Audio.Play_PipelinePump_Engine import Play_PipelinePump_Engine

class Build_PipelinePump(FGBuildablePipelinePump):
    Mat: Ptr[MaterialInstanceDynamic]
    mLastFlowUpdate: float
    mUpdateFlowTime: float = 0.5
    mAnimSpeed: float
    mLastFlowValue: float
    mTimeScaleOffset: float
    mPlayPumpPistons01: Ptr[AkComponent]
    mPlayPumpEngine: Ptr[AkComponent]
    mPistonAudioTimer: TimerHandle
    mIsPlayingPistons: bool
    mPlayPumpPistons02: Ptr[AkComponent]
    mIsExceedingHeadLift: bool
    mFluidDesc: TSubclassOf[FGItemDescriptor]
    mMaxPressure = 22
    mDesignPressure = 20
    mFlowLimit = 5
    mMinimumFlowPercentForStandby = 0.05000000074505806
    mRadius = 65
    mFluidBoxVolumeScale = 1
    mPowerConsumption = 4
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
    mHologramClass = NewObject[FGPipelineAttachmentHologram]()
    mDisplayName = NSLOCTEXT("", "D6A592BE4F1AAFAD3C970FA0C99A4DC4", "Pipeline Pump")
    mDescription = NSLOCTEXT("", "E60BEFDA413E62FF8154B3BE66A34A3C", "Can be attached to a Pipeline to apply Head Lift.\r\nMaximum Head Lift: 20 meters\r\n(Allows fluids to be transported 20 meters upwards.)\r\nOutputs fluids at 300m³ per minute.\r\n\r\nNOTE: Has an in- and output direction.\r\nNOTE: Head Lift does not stack, so space between Pumps is recommended.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    mInteractWidgetClass = NewObject[Widget_PipelinePump]()
    mIsUseable = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def ApplyFluidDescriptorColor(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mFluidDesc)
        if not ReturnValue:
            goto('L215')
        ReturnValue_0: Color = Default__FGItemDescriptor.GetFluidColor(self.mFluidDesc)
        ReturnValue_1: LinearColor = Conv_ColorToLinearColor(ReturnValue_0)
        self.Mat.SetVectorParameterValue("LiquidColor", ReturnValue_1)
    

    def PlayPistonSound(self):
        ReturnValue: float = self.GetIndicatorHeadLift()
        ReturnValue_0: bool = GreaterEqual_FloatFloat(ReturnValue, 20)
        if not ReturnValue_0:
            goto('L148')
        if not self.mIsExceedingHeadLift:
            goto('L368')
        # Label 90
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_PipelinePump_Pistons, self, True)
        # End
        # Label 148
        if not self.mIsExceedingHeadLift:
            goto('L310')
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_Pipeline_Pump_Headlift", 0, 0, self)
        # Label 218
        self.mIsExceedingHeadLift = False
        Default__KismetSystemLibrary.PrintString(self, "Below", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        # Label 310
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_PipelinePump_Pistons, self, True)
        # End
        # Label 368
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_Pipeline_Pump_Headlift", 100, 0, self)
        self.mIsExceedingHeadLift = True
        Default__KismetSystemLibrary.PrintString(self, "Exceeds", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto('L90')
    

    def OnPumpStopped(self):
        self.Mat.SetScalarParameterValue("FlowRate", 0)
    

    def UserConstructionScript(self):
        self.UserConstructionScript()
        
        self.mExcludeFromMaterialInstancing = None
        self.PumpMesh = None
        ReturnValue: int32 = self.mExcludeFromMaterialInstancing.append(self.PumpMesh)
    

    def OnHasPowerChanged(self):
        ExecuteUbergraph_Build_PipelinePump.K2Node_Event_newHasPower = newHasPower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_PipelinePump(598)
    

    def StopIsLookedAtForDismantle(self):
        ExecuteUbergraph_Build_PipelinePump.K2Node_Event_byCharacter = byCharacter #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_PipelinePump(148)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Build_PipelinePump(680)
    

    def BuildEffectFinishedEvent(self):
        self.ExecuteUbergraph_Build_PipelinePump(836)
    

    def PlayProductionAudioChain(self):
        self.ExecuteUbergraph_Build_PipelinePump(913)
    

    def StopProductionAudioChain(self):
        self.ExecuteUbergraph_Build_PipelinePump(1134)
    

    def FluidDescriptorSetNotify(self):
        ExecuteUbergraph_Build_PipelinePump.K2Node_Event_fluidDesc = fluidDesc #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_PipelinePump(1217)
    

    def ReceiveTick(self):
        ExecuteUbergraph_Build_PipelinePump.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_PipelinePump(1270)
    

    def PlayEngineAudioChain(self):
        self.ExecuteUbergraph_Build_PipelinePump(1570)
    

    def StopEngineAudioChain(self):
        self.ExecuteUbergraph_Build_PipelinePump(1636)
    

    def Factory_ReceiveStopProducing(self):
        self.ExecuteUbergraph_Build_PipelinePump(1641)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Build_PipelinePump(1706)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_PipelinePump(1711)
    

    def OnMaterialInstancesUpdated(self):
        self.ExecuteUbergraph_Build_PipelinePump(1716)
    

    def ExecuteUbergraph_Build_PipelinePump(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Default__KismetSystemLibrary.PrintString(self, "Hello", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
        self.PumpMesh.SetMaterial(0, self.Mat)
        goto(ExecutionFlow.Pop())
        # Label 148
        self.StopIsLookedAtForDismantle(byCharacter)
        self.PumpMesh.SetMaterial(0, self.Mat)
        goto(ExecutionFlow.Pop())
        # Label 218
        self.mLastFlowUpdate = 0
        ReturnValue: float = self.GetIndicatorFlowPct()
        ReturnValue1: bool = GreaterEqual_FloatFloat(ReturnValue, 0.004999999888241291)
        if not ReturnValue1:
            goto('L428')
        ReturnValue_0: float = self.GetIndicatorHeadLiftPct()
        self.Mat.SetScalarParameterValue("FlowRate", ReturnValue_0)
        if not self.mIsPlayingPistons:
            goto('L471')
        goto(ExecutionFlow.Pop())
        # Label 428
        self.OnPumpStopped()
        self.StopProductionAudioChain()
        self.StopEngineAudioChain()
        goto(ExecutionFlow.Pop())
        # Label 471
        self.PlayProductionAudioChain()
        self.PlayEngineAudioChain()
        self.mIsPlayingPistons = True
        goto(ExecutionFlow.Pop())
        # Label 511
        ReturnValue_1: bool = self.IsProducing()
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ReturnValue_2: bool = GreaterEqual_FloatFloat(self.mLastFlowUpdate, self.mUpdateFlowTime)
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        goto('L218')
        ReturnValue_3: bool = Not_PreBool(newHasPower)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        self.OnPumpStopped()
        self.StopProductionAudioChain()
        self.StopEngineAudioChain()
        goto(ExecutionFlow.Pop())
        self.ReceiveBeginPlay()
        ReturnValue_4: Ptr[MaterialInterface] = self.PumpMesh.GetMaterial(0)
        Dynamic: Ptr[MaterialInstanceDynamic] = Cast[MaterialInstanceDynamic](ReturnValue_4)
        bSuccess: bool = Dynamic
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        self.Mat = Dynamic
        goto(ExecutionFlow.Pop())
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 97, UUID = 1070639759, ExecutionFunction = "ExecuteUbergraph_Build_PipelinePump", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue_5: bool = Default__KismetSystemLibrary.IsValid(self.mPlayPumpPistons01)
        if not ReturnValue_5:
            goto('L979')
        goto(ExecutionFlow.Pop())
        # Label 979
        ReturnValue_6: TimerHandle = Default__KismetSystemLibrary.K2_SetTimer(self, "PlayPistonSound", 0.3499999940395355, True)
        self.mPistonAudioTimer = ReturnValue_6
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_PipelinePump_Pistons, self, True)
        goto(ExecutionFlow.Pop())
        self.mIsPlayingPistons = False
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mPistonAudioTimer])
        goto(ExecutionFlow.Pop())
        # Label 1188
        self.StopProductionAudioChain()
        self.StopEngineAudioChain()
        goto(ExecutionFlow.Pop())
        self.mFluidDesc = fluidDesc
        self.ApplyFluidDescriptorColor()
        goto(ExecutionFlow.Pop())
        # Label 1251
        self.OnPumpStopped()
        goto('L1188')
        ReturnValue_7: float = DeltaSeconds + self.mLastFlowUpdate
        self.mLastFlowUpdate = ReturnValue_7
        goto('L511')
        # Label 1348
        ReturnValue_8: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_PipelinePump_Engine, self, True)
        goto(ExecutionFlow.Pop())
        # Label 1402
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(self.mPlayPumpEngine)
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        goto('L1348')
        # Label 1468
        self.StopProductionAudioChain()
        self.StopEngineAudioChain()
        goto(ExecutionFlow.Pop())
        # Label 1497
        ReturnValue1_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_PipelinePump_Engine, self, True)
        self.mPlayPumpEngine = ReturnValue1_1
        goto(ExecutionFlow.Pop())
        ReturnValue2_0: bool = Default__KismetSystemLibrary.IsValid(self.mPlayPumpEngine)
        if not ReturnValue2_0:
            goto('L1497')
        goto(ExecutionFlow.Pop())
        goto('L1402')
        goto('L1251')
        # Label 1646
        self.LostSignificance()
        ReturnValue_9: bool = self.HasPower()
        if not ReturnValue_9:
           goto(ExecutionFlow.Pop())
        goto('L1468')
        # Label 1695
        self.GainedSignificance()
        goto(ExecutionFlow.Pop())
        goto('L1646')
        goto('L1695')
        ReturnValue1_2: Ptr[MaterialInterface] = self.PumpMesh.GetMaterial(0)
        Dynamic1: Ptr[MaterialInstanceDynamic] = Cast[MaterialInstanceDynamic](ReturnValue1_2)
        bSuccess1: bool = Dynamic1
        if not bSuccess1:
            goto('L15')
        self.Mat = Dynamic1
        self.ApplyFluidDescriptorColor()
        goto(ExecutionFlow.Pop())
    
