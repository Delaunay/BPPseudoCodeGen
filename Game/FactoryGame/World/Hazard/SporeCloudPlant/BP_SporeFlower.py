
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import SetActorTickEnabled
from Script.FactoryGame import FGSporeFlower
from Script.Engine import Delay
from Script.Engine import K2_SetTimerDelegate
from Game.FactoryGame.World.Hazard.SporeCloudPlant.BP_SporeFlower import ExecuteUbergraph_BP_SporeFlower
from Script.Engine import EqualEqual_ByteByte
from Script.Engine import GetScaledSphereRadius
from Script.Engine import SetPosition
from Script.AkAudio import PostAkEventAtLocation
from Script.Engine import ActorComponent
from Game.FactoryGame.World.Hazard.SporeCloudPlant.Audio.Play_SporeFlower_Gas import Play_SporeFlower_Gas
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.WorldDestruction.Play_Nobelisk_WorldDestruction_GasFlower import Play_Nobelisk_WorldDestruction_GasFlower
from Script.Engine import SpawnEmitterAttached
from Script.FactoryGame import AddGainSignificanceObjectToSignificanceManager
from Script.Engine import ReceiveBeginPlay
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import HasAuthority
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import SetAnimation
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.World.Hazard.SporeCloudPlant.Audio.Stop_SporeFlower_Gas import Stop_SporeFlower_Gas
from Script.Engine import TimerHandle
from Script.Engine import K2_TimerExistsHandle
from Script.Engine import IsValid
from Game.FactoryGame.World.Hazard.SporeCloudPlant.BP_SporeFlower import ExecuteUbergraph_BP_SporeFlower.K2Node_Event_EndPlayReason
from Script.Engine import Play
from Game.FactoryGame.World.Hazard.SporeCloudPlant.BP_SporeFlower import ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_OverlappedComponent
from Game.FactoryGame.World.Hazard.SporeCloudPlant.BP_SporeFlower import ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_SweepResult
from Script.FactoryGame import ActorShouldTriggerFlower
from Script.Engine import EqualEqual_IntInt
from Game.FactoryGame.World.Hazard.SporeCloudPlant.BP_SporeFlower import ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_OtherActor1
from Game.FactoryGame.World.Hazard.SporeCloudPlant.Audio.Play_SporeFlower_Bloom import Play_SporeFlower_Bloom
from Game.FactoryGame.World.Hazard.SporeCloudPlant.BP_SporeFlower import ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_OtherActor
from Game.FactoryGame.World.Hazard.SporeCloudPlant.BP_SporeFlower import ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_OtherBodyIndex
from Script.Engine import BooleanOR
from Script.Engine import Default__GameplayStatics
from Script.Engine import FlushNetDormancy
from Script.Engine import OverrideAnimationData
from Script.Engine import ParticleSystem
from Script.Engine import PlayAnimation
from Game.FactoryGame.World.Hazard.SporeCloudPlant.BP_SporeFlower import ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_bFromSweep
from Script.Engine import AnimSequence
from Script.Engine import Stop
from Script.CoreUObject import Vector
from Script.Engine import Array_AddUnique
from Script.Engine import Array_RemoveItem
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import NotEqual_ByteByte
from Script.Engine import SetPlayRate
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.Engine import GetPosition
from Script.Engine import Actor
from Script.Engine import ParticleSystemComponent
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.World.Hazard.SporeCloudPlant.BP_SporeFlower import ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_OtherBodyIndex1
from Game.FactoryGame.World.Hazard.SporeCloudPlant.ESporeFlowerGasState import ESporeFlowerGasState
from Script.Engine import ReceiveEndPlay
from Game.FactoryGame.World.Hazard.SporeCloudPlant.BP_SporeFlower import ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_OverlappedComponent1
from Script.Engine import SetFloatParameter
from Game.FactoryGame.World.Hazard.SporeCloudPlant.BP_SporeFlower import ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_OtherComp
from Script.FactoryGame import RemoveGainSignificanceObjectFromSignificanceManager
from Game.FactoryGame.World.Hazard.SporeCloudPlant.BP_SporeFlower import ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_OtherComp1
from Script.AkAudio import SeekOnEventBySeconds
from Script.AkAudio import AkComponent
from Game.FactoryGame.World.Hazard.SporeCloudPlant.ESporeFlowerState import ESporeFlowerState
from Script.Engine import GetComponentsByClass
from Game.FactoryGame.World.Hazard.SporeCloudPlant.Audio.Play_SporeFlower_Retract import Play_SporeFlower_Retract
from Script.Engine import MakeLiteralByte

class BP_SporeFlower(FGSporeFlower):
    mGasDuration: float = 30
    mReleaseGasCooldown: float = 15
    mTriggeredActors: List[Ptr[Actor]]
    mState: uint8
    mGasState: uint8
    mGasParticle: Ptr[ParticleSystem] = Namespace(AssetPath='/Game/FactoryGame/World/Hazard/SporeCloudPlant/Particle/GroundGas_01.GroundGas_01')
    mGasPSC: Ptr[ParticleSystemComponent]
    mParticleParameterName: FName = CloudRadius
    mReplicatedAnimPosition: float
    mGrowAnimation: Ptr[AnimSequence] = Namespace(AssetPath='/Game/FactoryGame/World/Hazard/SporeCloudPlant/Animation/Grow_01.Grow_01')
    mSporeAnimation: Ptr[AnimSequence] = Namespace(AssetPath='/Game/FactoryGame/World/Hazard/SporeCloudPlant/Animation/ReleaseSpores_01.ReleaseSpores_01')
    mUpdateAnimPositionTimer: TimerHandle
    mIsSignificant: bool
    mTriggerActorClasses = ['/Script/Engine.Pawn']
    bGenerateOverlapEventsDuringLevelStreaming = True
    bReplicates = True
    NetCullDistanceSquared = 500000000
    NetUpdateFrequency = 200
    MinNetUpdateFrequency = 1
    
    def SetTickStatus(self, doTick: bool):
        ExecutionFlow.Push("L462")
        self.SetActorTickEnabled(doTick)
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 70
        ReturnValue: List[Ptr[ActorComponent]] = self.GetComponentsByClass(ActorComponent)
        
        ReturnValue_0: int32 = len(ReturnValue)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L388")
        ReturnValue = self.GetComponentsByClass(ActorComponent)
        
        Item = None
        Item = ReturnValue[Variable_0]
        Item.SetComponentTickEnabled(doTick)
        goto(ExecutionFlow.Pop())
        # Label 388
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L70')
    

    def OnRep_mReplicatedAnimPosition(self):
        CmpSuccess: bool = NotEqual_ByteByte(self.mState, 1)
        if not CmpSuccess:
            goto('L95')
        CmpSuccess = NotEqual_ByteByte(self.mState, 2)
        if not CmpSuccess:
            goto('L95')
        # End
        
        playRate = None
        # Label 95
        self.GetStatePlayRate(Ref[playRate])
        self.SkeletalMesh.OverrideAnimationData(self.mGrowAnimation, False, True, self.mReplicatedAnimPosition, playRate)
    

    def OnRep_mState(self):
        ExecutionFlow.Push("L312")
        
        playRate = None
        self.GetStatePlayRate(Ref[playRate])
        self.SkeletalMesh.SetPlayRate(playRate)
        ExecutionFlow.Push("L195")
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        CmpSuccess: bool = NotEqual_ByteByte(self.mState, 1)
        if not CmpSuccess:
            goto('L210')
        CmpSuccess = NotEqual_ByteByte(self.mState, 2)
        if not CmpSuccess:
            goto('L210')
        goto(ExecutionFlow.Pop())
        # Label 195
        self.UpdateAnimationFromState()
        goto(ExecutionFlow.Pop())
        # Label 210
        self.FlushNetDormancy()
        ReturnValue_0: float = self.SkeletalMesh.GetPosition()
        # Label 270
        self.mReplicatedAnimPosition = ReturnValue_0
        self.OnRep_mReplicatedAnimPosition()
        goto(ExecutionFlow.Pop())
    

    def OnRep_mGasState(self):
        CmpSuccess: bool = NotEqual_ByteByte(self.mGasState, 0)
        if not CmpSuccess:
            goto('L140')
        CmpSuccess = NotEqual_ByteByte(self.mGasState, 1)
        if not CmpSuccess:
            goto('L257')
        CmpSuccess = NotEqual_ByteByte(self.mGasState, 2)
        if not CmpSuccess:
            goto('L140')
        # End
        # Label 140
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mGasPSC)
        if not ReturnValue1:
            goto('L341')
        self.mGasPSC.Deactivate()
        self.mGasPSC = None
        # End
        # Label 257
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mGasPSC)
        if not ReturnValue:
            goto('L327')
        # End
        # Label 327
        self.SpawnGasParticles()
    

    def StopSporeAnimation(self):
        self.FlushNetDormancy()
        self.mState = 2
        self.OnRep_mState()
        ReturnValue: float = self.mGrowAnimation.GetPlayLength()
        self.SkeletalMesh.SetAnimation(self.mGrowAnimation)
        ReturnValue_0: float = ReturnValue - 0.4000000059604645
        self.SkeletalMesh.SetPosition(ReturnValue_0, False)
        
        playRate = None
        self.GetStatePlayRate(Ref[playRate])
        self.SkeletalMesh.SetPlayRate(playRate)
        self.SkeletalMesh.Play(False)
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_SporeFlower_Gas, self, True)
    

    def UpdateAnimationFromState(self):
        ReturnValue: bool = self.HasAuthority()
        ReturnValue_0: bool = BooleanOR(self.mIsSignificant, ReturnValue)
        if not ReturnValue_0:
            goto('L1017')
        CmpSuccess: bool = NotEqual_ByteByte(self.mState, 0)
        if not CmpSuccess:
            goto('L257')
        CmpSuccess = NotEqual_ByteByte(self.mState, 1)
        if not CmpSuccess:
            goto('L368')
        CmpSuccess = NotEqual_ByteByte(self.mState, 2)
        if not CmpSuccess:
            goto('L688')
        CmpSuccess = NotEqual_ByteByte(self.mState, 3)
        if not CmpSuccess:
            goto('L975')
        # End
        # Label 257
        self.SkeletalMesh.SetAnimation(self.mGrowAnimation)
        self.SkeletalMesh.Play(False)
        self.SkeletalMesh.Stop()
        # End
        # Label 368
        if not self.mIsSignificant:
            goto('L566')
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_SporeFlower_Bloom, self, True)
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        if not ReturnValue1_0:
            goto('L566')
        ReturnValue1_1: bool = ReturnValue1.SeekOnEventBySeconds(Play_SporeFlower_Bloom, self.mReplicatedAnimPosition, False, 0)
        
        playRate = None
        # Label 566
        self.GetStatePlayRate(Ref[playRate])
        self.SkeletalMesh.OverrideAnimationData(self.mGrowAnimation, False, True, self.mReplicatedAnimPosition, playRate)
        self.SkeletalMesh.Play(False)
        # End
        # Label 688
        if not self.mIsSignificant:
            goto('L566')
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_SporeFlower_Retract, self, True)
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_1)
        if not ReturnValue_2:
            goto('L566')
        ReturnValue_3: float = 9.970000267028809 - self.mReplicatedAnimPosition
        ReturnValue_4: float = ReturnValue_3 * 2
        ReturnValue_5: bool = ReturnValue_1.SeekOnEventBySeconds(Play_SporeFlower_Retract, ReturnValue_4, False, 0)
        goto('L566')
        # Label 975
        self.SkeletalMesh.PlayAnimation(self.mSporeAnimation, True)
    

    def StartSporeAnimation(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L131')
        self.FlushNetDormancy()
        self.mState = 3
        self.OnRep_mState()
        # Label 78
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_SporeFlower_Gas, self, True)
    

    def GetStatePlayRate(self):
        Variable: float = 0
        Variable1: float = -0.5
        Variable2: float = 1
        Variable3: float = 0
        Variable_0: uint8 = self.mState
        
        switch = {
            0: Variable3,
            1: Variable2,
            2: Variable1,
            3: Variable
        }
        PlayRate = switch.get(Variable_0, None)
    

    def GetOffCooldown(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L78')
        self.FlushNetDormancy()
        self.mGasState = 0
        self.OnRep_mGasState()
    

    def StartReleasingGas(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L116')
        self.DotComponent.SetActive(True, False)
        self.FlushNetDormancy()
        self.mGasState = 1
        self.OnRep_mGasState()
    

    def StopExpanding(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L78')
        self.FlushNetDormancy()
        self.mState = 0
        self.OnRep_mState()
    

    def StopReleasingGas(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L116')
        self.DotComponent.SetActive(False, False)
        self.FlushNetDormancy()
        self.mGasState = 2
        self.OnRep_mGasState()
    

    def CondintionallyReverseExpanding(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L123')
        ReturnValue_0: bool = EqualEqual_ByteByte(self.mState, 1)
        if not ReturnValue_0:
            goto('L123')
        self.FlushNetDormancy()
        self.mState = 2
        self.OnRep_mState()
    

    def ConditionallyStartExpanding(self):
        ReturnValue: bool = self.HasAuthority()
        if not ReturnValue:
            goto('L694')
        
        Variable = None
        ReturnValue_0: bool = Default__KismetArrayLibrary.Array_RemoveItem(Ref[self.mTriggeredActors], Ref[Variable])
        ReturnValue_1: uint8 = Default__KismetSystemLibrary.MakeLiteralByte(1)
        ReturnValue_2: bool = EqualEqual_ByteByte(self.mGasState, 0)
        
        ReturnValue_3: int32 = len(self.mTriggeredActors)
        ReturnValue_4: bool = ReturnValue_3 > 0
        # Label 270
        ReturnValue_5: bool = NotEqual_ByteByte(self.mState, ReturnValue_1)
        ReturnValue_6: bool = ReturnValue_5 and ReturnValue_4
        ReturnValue1: bool = ReturnValue_6 and ReturnValue_2
        if not ReturnValue1:
            goto('L694')
        self.FlushNetDormancy()
        self.mState = 1
        self.OnRep_mState()
        ReturnValue_7: bool = Default__KismetSystemLibrary.K2_TimerExistsHandle(self, self.mUpdateAnimPositionTimer)
        ReturnValue_8: bool = Not_PreBool(ReturnValue_7)
        if not ReturnValue_8:
            goto('L694')
        OutputDelegate.BindUFunction(self, UpdateAnimPosition)
        ReturnValue_9: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, 0.30000001192092896, True)
        self.mUpdateAnimPositionTimer = ReturnValue_9
        self.SkeletalMesh.VisibilityBasedAnimTickOption = 1
    

    def ActivateDamage(self):
        self.ExecuteUbergraph_BP_SporeFlower(1219)
    

    def BndEvt__TriggerSphere_K2Node_ComponentBoundEvent_0_ComponentBeginOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32, bFromSweep: bool, SweepResult: Const[Ref[HitResult]]):
        ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_OverlappedComponent1 = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_OtherActor1 = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_OtherComp1 = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_OtherBodyIndex1 = OtherBodyIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_bFromSweep = bFromSweep #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_SweepResult = SweepResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SporeFlower(648)
    

    def BndEvt__TriggerSphere_K2Node_ComponentBoundEvent_1_ComponentEndOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32):
        ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_OverlappedComponent = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_OtherActor = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_BP_SporeFlower.K2Node_ComponentBoundEvent_OtherBodyIndex = OtherBodyIndex #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SporeFlower(918)
    

    def SpawnGasParticles(self):
        self.ExecuteUbergraph_BP_SporeFlower(1527)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_SporeFlower(1830)
    

    def UpdateAnimPosition(self):
        self.ExecuteUbergraph_BP_SporeFlower(1894)
    

    def ReceiveEndPlay(self):
        ExecuteUbergraph_BP_SporeFlower.K2Node_Event_EndPlayReason = EndPlayReason #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SporeFlower(2085)
    

    def GainedSignificance(self):
        self.ExecuteUbergraph_BP_SporeFlower(2139)
    

    def LostSignificance(self):
        self.ExecuteUbergraph_BP_SporeFlower(2169)
    

    def ReceiveDestroyed(self):
        self.ExecuteUbergraph_BP_SporeFlower(2185)
    

    def ExecuteUbergraph_BP_SporeFlower(self):
        goto(ComputedJump("EntryPoint"))
        self.StopReleasingGas()
        self.StopSporeAnimation()
        Default__KismetSystemLibrary.Delay(self, self.mReleaseGasCooldown, LatentActionInfo(Linkage = 124, UUID = 2124541931, ExecutionFunction = "ExecuteUbergraph_BP_SporeFlower", CallbackTarget = self))
        # Label 123
        goto(ExecutionFlow.Pop())
        self.GetOffCooldown()
        self.ConditionallyStartExpanding()
        goto(ExecutionFlow.Pop())
        # Label 153
        ReturnValue: Vector = self.K2_GetActorLocation()
        # Label 195
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_Nobelisk_WorldDestruction_GasFlower, ReturnValue, Rotator::FromPitchYawRoll(0, 0, 0))
        goto(ExecutionFlow.Pop())
        # Label 270
        self.OnRep_mReplicatedAnimPosition()
        ReturnValue4: bool = self.HasAuthority()
        if not ReturnValue4:
           goto(ExecutionFlow.Pop())
        ReturnValue_1: bool = EqualEqual_ByteByte(self.mState, 2)
        ReturnValue_2: bool = self.mReplicatedAnimPosition <= 0.10000000149011612
        ReturnValue_3: bool = ReturnValue_1 and ReturnValue_2
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        self.FlushNetDormancy()
        self.mState = 0
        self.OnRep_mState()
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mUpdateAnimPositionTimer])
        self.SkeletalMesh.VisibilityBasedAnimTickOption = 3
        goto(ExecutionFlow.Pop())
        # Label 556
        self.FlushNetDormancy()
        # Label 566
        ReturnValue_4: float = self.SkeletalMesh.GetPosition()
        self.mReplicatedAnimPosition = ReturnValue_4
        goto('L270')
        ReturnValue3: bool = self.HasAuthority()
        if not ReturnValue3:
           goto(ExecutionFlow.Pop())
        ReturnValue_5: bool = self.ActorShouldTriggerFlower(OtherActor1)
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        
        OtherActor1 = None
        ReturnValue_6: int32 = Default__KismetArrayLibrary.Array_AddUnique(Ref[self.mTriggeredActors], Ref[OtherActor1])
        self.ConditionallyStartExpanding()
        
        ReturnValue_7: int32 = len(self.mTriggeredActors)
        ReturnValue_8: bool = EqualEqual_IntInt(ReturnValue_7, 1)
        if not ReturnValue_8:
           goto(ExecutionFlow.Pop())
        self.SetTickStatus(True)
        goto(ExecutionFlow.Pop())
        ReturnValue_9: bool = self.HasAuthority()
        if not ReturnValue_9:
           goto(ExecutionFlow.Pop())
        ReturnValue1: bool = self.ActorShouldTriggerFlower(OtherActor)
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        
        OtherActor = None
        ReturnValue_10: bool = Default__KismetArrayLibrary.Array_RemoveItem(Ref[self.mTriggeredActors], Ref[OtherActor])
        
        ReturnValue1_0: int32 = len(self.mTriggeredActors)
        ReturnValue1_1: bool = EqualEqual_IntInt(ReturnValue1_0, 0)
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        self.CondintionallyReverseExpanding()
        ReturnValue_11: bool = Not_PreBool(self.mIsSignificant)
        if not ReturnValue_11:
           goto(ExecutionFlow.Pop())
        self.SetTickStatus(False)
        goto(ExecutionFlow.Pop())
        ReturnValue1_2: bool = self.HasAuthority()
        if not ReturnValue1_2:
           goto(ExecutionFlow.Pop())
        self.StartSporeAnimation()
        self.StartReleasingGas()
        Default__KismetSystemLibrary.Delay(self, self.mGasDuration, LatentActionInfo(Linkage = 15, UUID = -1880554308, ExecutionFunction = "ExecuteUbergraph_BP_SporeFlower", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1358
        ReturnValue2: bool = self.HasAuthority()
        if not ReturnValue2:
            goto('L1511')
        
        ReturnValue2_0: int32 = len(self.mTriggeredActors)
        ReturnValue2_1: bool = EqualEqual_IntInt(ReturnValue2_0, 0)
        if not ReturnValue2_1:
           goto(ExecutionFlow.Pop())
        self.SetTickStatus(False)
        goto(ExecutionFlow.Pop())
        # Label 1511
        self.SetTickStatus(False)
        goto(ExecutionFlow.Pop())
        ReturnValue_12: bool = Default__KismetSystemLibrary.IsValid(self.mGasPSC)
        if not ReturnValue_12:
            goto('L1593')
        goto(ExecutionFlow.Pop())
        # Label 1593
        ReturnValue_13: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(self.mGasParticle, self.SkeletalMesh, "Root", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 2, True, 0)
        self.mGasPSC = ReturnValue_13
        ReturnValue_14: float = self.DamageSphere.GetScaledSphereRadius()
        self.mGasPSC.SetFloatParameter(self.mParticleParameterName, ReturnValue_14)
        goto(ExecutionFlow.Pop())
        self.ReceiveBeginPlay()
        self.UpdateAnimationFromState()
        Default__FGBlueprintFunctionLibrary.AddGainSignificanceObjectToSignificanceManager(self, self, 8000)
        goto(ExecutionFlow.Pop())
        goto('L556')
        # Label 1899
        self.FireFlies_01.Deactivate()
        self.FireFlies_02.Deactivate()
        goto('L1358')
        # Label 1976
        self.FireFlies_01.Activate(False)
        self.FireFlies_02.Activate(False)
        self.SetTickStatus(True)
        goto(ExecutionFlow.Pop())
        # Label 2066
        self.UpdateAnimationFromState()
        goto('L1899')
        self.ReceiveEndPlay(EndPlayReason)
        Default__FGBlueprintFunctionLibrary.RemoveGainSignificanceObjectFromSignificanceManager(self, self)
        goto(ExecutionFlow.Pop())
        self.mIsSignificant = True
        self.UpdateAnimationFromState()
        goto('L1976')
        self.mIsSignificant = False
        goto('L2066')
        goto('L153')
    
