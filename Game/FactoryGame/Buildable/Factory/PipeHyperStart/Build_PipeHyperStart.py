
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import TransformLocation
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Build_PipeHyperStart import ExecuteUbergraph_Build_PipeHyperStart.K2Node_ComponentBoundEvent_OtherBodyIndex
from Script.FactoryGame import FGCharacterMovementComponent
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Build_PipeHyperStart import ExecuteUbergraph_Build_PipeHyperStart.K2Node_Event_didStopProducing
from Script.AkAudio import SetActorRTPCValue
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Build_PipeHyperStart import ExecuteUbergraph_Build_PipeHyperStart
from Script.Engine import SpawnEmitterAttached
from Script.FactoryGame import TryStopProductionLoopEffects
from Script.Engine import ReceiveBeginPlay
from Script.FactoryGame import FGPipeHyperStart
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Build_PipeHyperStart import ExecuteUbergraph_Build_PipeHyperStart.K2Node_ComponentBoundEvent_bFromSweep
from Script.Engine import GetRelativeTransform
from Script.Engine import ETimelineDirection
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Build_PipeHyperStart import ExecuteUbergraph_Build_PipeHyperStart.K2Node_Event_newHasPower
from Script.Engine import EqualEqual_FloatFloat
from Script.FactoryGame import StartProductionLoopEffects
from Script.FactoryGame import GetConnection
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Audio.Play_StartUpEngineTubeLoop import Play_StartUpEngineTubeLoop
from Script.FactoryGame import TryStartProductionLoopEffects
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Build_PipeHyperStart import ExecuteUbergraph_Build_PipeHyperStart.K2Node_Event_newIsProducing
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Audio.Stop_EngineTubeLoop import Stop_EngineTubeLoop
from Game.FactoryGame.VFX.Factory.Hypertube.P_Hypetube_Entrance import P_Hypetube_Entrance
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Build_PipeHyperStart import ExecuteUbergraph_Build_PipeHyperStart.K2Node_ComponentBoundEvent_SweepResult
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Build_PipeHyperStart import ExecuteUbergraph_Build_PipeHyperStart.K2Node_ComponentBoundEvent_OtherActor
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Build_PipeHyperStart import ExecuteUbergraph_Build_PipeHyperStart.K2Node_Event_didStartProducing
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import GetIsSignificant
from Script.FactoryGame import OnHasPowerChanged
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.FactoryGame import EnterPipeHyper
from Game.FactoryGame.Buildable.Factory.ConveyorBeltMk1.Audio.Play_F_Construction_ConveyorBelt import Play_F_Construction_ConveyorBelt
from Script.Engine import PawnMovementComponent
from Script.AkAudio import Default__AkGameplayStatics
from Script.AkAudio import PostAkEventAttached
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Audio.Stop_OnlyEngineTubeLoop import Stop_OnlyEngineTubeLoop
from Script.Engine import K2_DestroyComponent
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Build_PipeHyperStart import ExecuteUbergraph_Build_PipeHyperStart.K2Node_ComponentBoundEvent_OtherComp
from Script.FactoryGame import LostSignificance
from Script.Engine import ParticleSystemComponent
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Build_PipeHyperStart import ExecuteUbergraph_Build_PipeHyperStart.K2Node_ComponentBoundEvent_OverlappedComponent
from Script.FactoryGame import OnIsProducingChanged
from Script.FactoryGame import FGPipeConnectionComponentBase
from Script.Engine import Abs
from Script.AkAudio import AkComponent
from Script.FactoryGame import GainedSignificance
from Game.FactoryGame.Buildable.Factory.PipeHyperStart.Audio.Play_OnlyEngineTubeLoop import Play_OnlyEngineTubeLoop
from Script.FactoryGame import StopProductionLoopEffects
from Script.CoreUObject import Transform
from Script.Engine import GetLocalBounds

class Build_PipeHyperStart(FGPipeHyperStart):
    InterpolateEngineSound_InterpolateEngineAlpha_064FA8194B7224F6F187999413D1C8A6: float
    InterpolateEngineSound__Direction_064FA8194B7224F6F187999413D1C8A6: uint8
    mWindDirectionFromTurbine: TimerHandle
    mIsWindSoundPlaying?: bool
    mAudioTimerCounter: float
    AudioCounterTimer: TimerHandle
    P_Entrance_VFX: Ptr[ParticleSystemComponent]
    IsEnginePlaying: bool
    mStartUpHyperTubeRef: Ptr[AkComponent]
    SFXEngine: Ptr[AkComponent]
    mOpeningOffset = 350
    mInitialMinSpeedFactor = 1.2000000476837158
    mLength = 200
    mSupportComponentDefaultMesh = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, ComponentTags=['PoleMesh'], Mobility=0, ObjectClass='/Script/FactoryGame.FGColoredInstanceMeshProxy', ObjectFlags=2883617, ObjectName='SupportMeshCompProxyHolder', RelativeLocation={'X': 0, 'Y': 0, 'Z': 80}, bGenerateOverlapEvents=False)
    mPowerConsumption = 10
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
    mHologramClass = NewObject[Holo_PipeHyperStart]()
    mDisplayName = NSLOCTEXT("", "FD7771FA4E57AA3B7A75ABB27A5F2C61", "Hyper Tube Entrance")
    mDescription = NSLOCTEXT("", "1488FA97497870EACC9FF896C78804DF", "Used to enter and power a Hyper Tube.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=4, TickGroup=2, TickInterval=5, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Build.BP_MaterialEffect_Build_C', SubPathString='')
    mBuildEffectSpeed = 300
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=2, TickInterval=0.5, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    bReplicates = True
    RemoteRole = 1
    NetDormancy = 4
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def CanProduce(self):
        ReturnValue: Ptr[FGPipeConnectionComponentBase] = self.PipeHyperStartConnection.GetConnection()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        ReturnValue_1: bool = ReturnValue_0
    

    def UserConstructionScript(self):
        self.mConnection0 = self.PipeHyperStartConnection
        ReturnValue: Transform = self.FGColoredInstanceMeshProxy.GetRelativeTransform()
        
        Min = None
        Max = None
        self.FGColoredInstanceMeshProxy.GetLocalBounds(Ref[Min], Ref[Max])
        
        ReturnValue_0: Vector = TransformLocation(Min, Ref[ReturnValue])
        ReturnValue_1: Vector = Subtract_VectorVector(self.PipeHyperStartConnection.RelativeLocation, ReturnValue_0)
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_1)
        ReturnValue_2: float = Abs(X)
        ReturnValue_3: float = ReturnValue_2 + 20
        self.mOpeningOffset = ReturnValue_3
    

    def InterpolateEngineSound__FinishedFunc(self):
        self.ExecuteUbergraph_Build_PipeHyperStart(2010)
    

    def InterpolateEngineSound__UpdateFunc(self):
        self.ExecuteUbergraph_Build_PipeHyperStart(2005)
    

    def OnHasPowerChanged(self):
        ExecuteUbergraph_Build_PipeHyperStart.K2Node_Event_newHasPower = newHasPower #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_PipeHyperStart(1863)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_Build_PipeHyperStart(43)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_Build_PipeHyperStart(169)
    

    def StartUpHypertube(self):
        self.ExecuteUbergraph_Build_PipeHyperStart(776)
    

    def StopHyperTube(self):
        self.ExecuteUbergraph_Build_PipeHyperStart(846)
    

    def StartEngineSoundTimelineEvent(self):
        self.ExecuteUbergraph_Build_PipeHyperStart(1255)
    

    def EndEngineSoundTimelineEvent(self):
        self.ExecuteUbergraph_Build_PipeHyperStart(1325)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Build_PipeHyperStart(1486)
    

    def BndEvt__OverlapSphere_K2Node_ComponentBoundEvent_0_ComponentBeginOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32, bFromSweep: bool, SweepResult: Const[Ref[HitResult]]):
        ExecuteUbergraph_Build_PipeHyperStart.K2Node_ComponentBoundEvent_OverlappedComponent = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_PipeHyperStart.K2Node_ComponentBoundEvent_OtherActor = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_PipeHyperStart.K2Node_ComponentBoundEvent_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_PipeHyperStart.K2Node_ComponentBoundEvent_OtherBodyIndex = OtherBodyIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_PipeHyperStart.K2Node_ComponentBoundEvent_bFromSweep = bFromSweep #  PERSISTENT_FRAME(
        ExecuteUbergraph_Build_PipeHyperStart.K2Node_ComponentBoundEvent_SweepResult = SweepResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_PipeHyperStart(1501)
    

    def PlayConstructSound_1(self):
        self.ExecuteUbergraph_Build_PipeHyperStart(1805)
    

    def OnIsProducingChanged(self):
        ExecuteUbergraph_Build_PipeHyperStart.K2Node_Event_newIsProducing = newIsProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_PipeHyperStart(2015)
    

    def StartProductionLoopEffects(self):
        ExecuteUbergraph_Build_PipeHyperStart.K2Node_Event_didStartProducing = didStartProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_PipeHyperStart(2039)
    

    def StopProductionLoopEffects(self):
        ExecuteUbergraph_Build_PipeHyperStart.K2Node_Event_didStopProducing = didStopProducing #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Build_PipeHyperStart(2077)
    

    def PlayOnSi(self):
        self.ExecuteUbergraph_Build_PipeHyperStart(2148)
    

    def ExecuteUbergraph_Build_PipeHyperStart(self):
        # Label 10
        self.StartEngineSoundTimelineEvent()
        self.StartUpHypertube()
        # End
        self.GainedSignificance()
        ReturnValue: bool = self.HasPower()
        ReturnValue_0: bool = self.CanProduce()
        ReturnValue_1: bool = ReturnValue and ReturnValue_0
        if not ReturnValue_1:
            goto('L2148')
        self.TryStartProductionLoopEffects(False)
        # End
        self.LostSignificance()
        ReturnValue3: bool = self.HasPower()
        ReturnValue2: bool = self.CanProduce()
        ReturnValue2_0: bool = ReturnValue3 and ReturnValue2
        if not ReturnValue2_0:
            goto('L2148')
        self.TryStopProductionLoopEffects(False)
        # End
        # Label 295
        ReturnValue_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Stop_EngineTubeLoop, self.TurbineFront, "None", True)
        # Label 369
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.P_Entrance_VFX)
        if not ReturnValue1:
            goto('L2148')
        self.P_Entrance_VFX.K2_DestroyComponent(self)
        # End
        # Label 472
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAttached(Play_StartUpEngineTubeLoop, self.TurbineFront, "None", True)
        self.mStartUpHyperTubeRef = ReturnValue1_0
        # Label 565
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(self.P_Entrance_VFX)
        if not ReturnValue_3:
            goto('L635')
        # End
        # Label 635
        ReturnValue_4: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_Hypetube_Entrance, self.FGColoredInstanceMeshProxy, "VFX_Socket_01", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.P_Entrance_VFX = ReturnValue_4
        # End
        ReturnValue2_1: bool = Default__KismetSystemLibrary.IsValid(self.mStartUpHyperTubeRef)
        if not ReturnValue2_1:
            goto('L472')
        goto('L565')
        ReturnValue3_0: bool = Default__KismetSystemLibrary.IsValid(self.mStartUpHyperTubeRef)
        if not ReturnValue3_0:
            goto('L369')
        goto('L295')
        # Label 916
        self.StartUpHypertube()
        # End
        # Label 935
        self.StopHyperTube()
        # End
        # Label 954
        ReturnValue_5: bool = self.GetIsSignificant()
        if not ReturnValue_5:
            goto('L2148')
        ReturnValue2_2: bool = self.HasPower()
        ReturnValue1_1: bool = self.CanProduce()
        ReturnValue1_2: bool = ReturnValue2_2 and ReturnValue1_1
        if not ReturnValue1_2:
            goto('L1104')
        self.TryStartProductionLoopEffects(True)
        # End
        # Label 1104
        self.TryStopProductionLoopEffects(True)
        # End
        # Label 1120
        ReturnValue_6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_OnlyEngineTubeLoop, self, True)
        self.SFXEngine = ReturnValue_6
        # End
        # Label 1197
        ReturnValue1_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_OnlyEngineTubeLoop, self, True)
        # End
        ReturnValue4: bool = Default__KismetSystemLibrary.IsValid(self.SFXEngine)
        if not ReturnValue4:
            goto('L1120')
        # End
        ReturnValue5: bool = Default__KismetSystemLibrary.IsValid(self.SFXEngine)
        if not ReturnValue5:
            goto('L2148')
        ReturnValue3_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_OnlyEngineTubeLoop, self, True)
        # End
        # Label 1448
        self.StartEngineSoundTimelineEvent()
        goto('L916')
        # Label 1467
        self.EndEngineSoundTimelineEvent()
        goto('L935')
        self.ReceiveBeginPlay()
        # End
        ReturnValue1_4: bool = self.HasPower()
        if not ReturnValue1_4:
            goto('L2148')
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](OtherActor)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L2148')
        ReturnValue_7: Ptr[PawnMovementComponent] = Player.GetMovementComponent()
        Component: Ptr[FGCharacterMovementComponent] = Cast[FGCharacterMovementComponent](ReturnValue_7)
        bSuccess1: bool = Component
        if not bSuccess1:
            goto('L2148')
        ReturnValue_8: bool = Component.EnterPipeHyper(self)
        if not ReturnValue_8:
            goto('L2148')
        # End
        ReturnValue2_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_F_Construction_ConveyorBelt, self, True)
        # End
        self.OnHasPowerChanged(newHasPower)
        goto('L954')
        # Label 1887
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_TubeEngine", self.InterpolateEngineSound_InterpolateEngineAlpha_064FA8194B7224F6F187999413D1C8A6, 0, None)
        # End
        # Label 1952
        ReturnValue_9: bool = EqualEqual_FloatFloat(self.InterpolateEngineSound_InterpolateEngineAlpha_064FA8194B7224F6F187999413D1C8A6, 0)
        if not ReturnValue_9:
            goto('L2148')
        goto('L1197')
        goto('L1887')
        goto('L1952')
        self.OnIsProducingChanged(newIsProducing)
        goto('L954')
        self.StartProductionLoopEffects(didStartProducing)
        if not didStartProducing:
            goto('L10')
        goto('L1448')
        self.StopProductionLoopEffects(didStopProducing)
        if not didStopProducing:
            goto('L2115')
        goto('L1467')
        # Label 2115
        self.EndEngineSoundTimelineEvent()
        self.StopHyperTube()
        # End
    
