
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.Chainsaw.Equip_Chainsaw import ExecuteUbergraph_Equip_Chainsaw
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import EqualEqual_ByteByte
from Script.FactoryGame import SawProgress
from Script.FactoryGame import GetInstigatorCharacter
from Script.FactoryGame import WasEquipped
from Script.FactoryGame import FGChainsaw
from Script.Engine import SpawnEmitterAttached
from Script.FactoryGame import IsEquipped
from Script.Engine import Conv_ByteToInt
from Script.FactoryGame import WasUnEquipped
from Script.Engine import FMin
from Script.FactoryGame import IsSawing
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Play_E_ChainsawRework_EngageToIdle import Play_E_ChainsawRework_EngageToIdle
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Script.Engine import ReceiveTick
from Game.FactoryGame.Equipment.Chainsaw.Equip_Chainsaw import ExecuteUbergraph_Equip_Chainsaw.K2Node_Event_DeltaSeconds
from Script.FactoryGame import IsSawEngaged
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Play_E_ChainsawRework_Idle_loop import Play_E_ChainsawRework_Idle_loop
from Script.Engine import GetCurrentActiveMontage
from Script.CoreUObject import Object
from Script.Engine import IsValid
from Script.FactoryGame import IsLocalInstigator
from Game.FactoryGame.Equipment.Chainsaw.Animation.ChainsawStinger_01_Montage import ChainsawStinger_01_Montage
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Play_E_ChainsawRework_SawToEngage import Play_E_ChainsawRework_SawToEngage
from Script.Engine import Montage_Stop
from Script.FactoryGame import GetMesh1P
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Stop_E_ChainSawRework_NoFuel import Stop_E_ChainSawRework_NoFuel
from Game.FactoryGame.Character.Player.Animation.FirstPerson.ChainsawSawingComplete_01_Montage import ChainsawSawingComplete_01_Montage
from Game.FactoryGame.Equipment.Chainsaw.Audio.Play_E_Chainsaw_Add_Equip_NoFuel import Play_E_Chainsaw_Add_Equip_NoFuel
from Script.Engine import BooleanOR
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Play_E_ChainsawRework_Stinger import Play_E_ChainsawRework_Stinger
from Game.FactoryGame.Equipment.Chainsaw.Audio.Play_E_Chainsaw_Add_Stinger_NoFuel import Play_E_Chainsaw_Add_Stinger_NoFuel
from Script.Engine import AnimMontage
from Game.FactoryGame.Character.Player.Animation.FirstPerson.ChainsawSawing_01_Montage import ChainsawSawing_01_Montage
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Stop_E_ChainSawRework_All import Stop_E_ChainSawRework_All
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Play_E_ChainsawRework_IdleToEngage import Play_E_ChainsawRework_IdleToEngage
from Script.Engine import Montage_Play
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import NotEqual_ByteByte
from Game.FactoryGame.Character.Player.Animation.FirstPerson.ChainsawEquip_01_Montage import ChainsawEquip_01_Montage
from Script.Engine import FInterpTo_Constant
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Play_E_ChainsawRework_IdleToSaw import Play_E_ChainsawRework_IdleToSaw
from Script.Engine import ParticleSystemComponent
from Game.FactoryGame.Equipment.Chainsaw.Particle.SawingTree_01 import SawingTree_01
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Play_E_ChainsawRework_SawToIdle import Play_E_ChainsawRework_SawToIdle
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Play_E_ChainsawRework_EngageToIdleToggle import Play_E_ChainsawRework_EngageToIdleToggle
from Game.FactoryGame.Equipment.Chainsaw.EChainsawUseState import EChainsawUseState
from Script.Engine import Montage_SetPosition
from Game.FactoryGame.Equipment.Chainsaw.Animation.ChainsawEquip_01_Montage import ChainsawEquip_01_Montage
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Play_E_ChainsawRework_Equip import Play_E_ChainsawRework_Equip
from Script.FactoryGame import ShouldShowStinger
from Script.FactoryGame import HasAnyFuel
from Game.FactoryGame.Character.Player.Animation.FirstPerson.ChainsawStinger_01_Montage import ChainsawStinger_01_Montage
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Play_E_ChainsawRework_EngageToSaw import Play_E_ChainsawRework_EngageToSaw

class Equip_Chainsaw(FGChainsaw):
    mUIWidget: Ptr[Object]
    mSawingVfx: Ptr[ParticleSystemComponent]
    mMontageLength: float
    mInterpSawProgress: float
    mWasSawing: bool
    mCurrentState: uint8
    mPlayingSound: bool
    mAnim1pInstance: Ptr[AnimInstance]
    mCurrentAudioState: uint8
    mSawToEngage: Ptr[AkComponent]
    mPreviousAudioState: uint8
    mFuelClass = NewObject[Desc_Biofuel]()
    mEnergyConsumption = 75
    mSawDownTreeTime = 2
    mCollateralPickupRadius = 500
    mAttachmentClass = NewObject[Attach_Chainsaw]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mAttachSocket = hand_lSocket
    mArmAnimation = EArmEquipment::AE_ChainSaw
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def CanStartSawing(self):
        ReturnValue: bool = EqualEqual_ByteByte(self.mCurrentState, 1)
        ReturnValue_0: bool = ReturnValue
    

    def UpdateAttachmentState(self, ChainsawState: uint8, ForceUpdate: bool):
        ReturnValue: bool = NotEqual_ByteByte(ChainsawState, self.mCurrentState)
        ReturnValue_0: bool = BooleanOR(ReturnValue, ForceUpdate)
        if not ReturnValue_0:
            goto('L177')
        ReturnValue_1: int32 = Conv_ByteToInt(ChainsawState)
        # Label 127
        self.Server_UpdateAttachmentUseState(ReturnValue_1)
        self.mCurrentState = ChainsawState
    

    def InterpSawProgress(self, DeltaTime: float):
        ReturnValue1: float = self.SawProgress()
        ReturnValue: bool = ReturnValue1 > self.mInterpSawProgress
        if not ReturnValue:
            goto('L182')
        ReturnValue_0: float = self.SawProgress()
        ReturnValue_1: float = FMin(ReturnValue_0, 0.949999988079071)
        self.mInterpSawProgress = ReturnValue_1
        # Label 177
        # End
        # Label 182
        ReturnValue_2: float = FInterpTo_Constant(self.mInterpSawProgress, 0, DeltaTime, 2)
        self.mInterpSawProgress = ReturnValue_2
    

    def ReceiveTick(self):
        ExecuteUbergraph_Equip_Chainsaw.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_Chainsaw(4917)
    

    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_Chainsaw(4912)
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_Equip_Chainsaw(4892)
    

    def ExecuteUbergraph_Equip_Chainsaw(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ChainsawRework_EngageToIdle, self, True)
        # Label 68
        self.mPlayingSound = True
        self.mPreviousAudioState = self.mCurrentAudioState
        self.mCurrentAudioState = 1
        goto(ExecutionFlow.Pop())
        # Label 127
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ChainsawRework_EngageToIdleToggle, self, True)
        goto('L68')
        # Label 185
        ExecutionFlow.Push("L798")
        ExecutionFlow.Push("L562")
        ReturnValue3: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue3_0: Ptr[SkeletalMeshComponent] = ReturnValue3.GetMesh1P()
        ReturnValue6: Ptr[AnimInstance] = ReturnValue3_0.GetAnimInstance()
        self.mAnim1pInstance = ReturnValue6
        ReturnValue_0: bool = self.IsSawEngaged()
        if not ReturnValue_0:
            goto('L1148')
        ReturnValue_1: bool = self.mInterpSawProgress > 0
        if not ReturnValue_1:
            goto('L1456')
        ReturnValue7: bool = self.mAnim1pInstance.Montage_IsPlaying(ChainsawSawingComplete_01_Montage)
        if not ReturnValue7:
            goto('L1872')
        ReturnValue_2: float = self.mInterpSawProgress * self.mMontageLength
        self.mAnim1pInstance.Montage_SetPosition(ChainsawSawingComplete_01_Montage, ReturnValue_2)
        goto(ExecutionFlow.Pop())
        # Label 562
        ReturnValue1_0: bool = self.IsSawEngaged()
        ReturnValue_3: bool = self.IsSawing()
        ReturnValue_4: bool = ReturnValue_3 and ReturnValue1_0
        if not ReturnValue_4:
            goto('L674')
        ExecutionFlow.Push("L2232")
        if not Variable1:
            goto('L2412')
        goto(ExecutionFlow.Pop())
        # Label 674
        ReturnValue_5: bool = Default__KismetSystemLibrary.IsValid(self.mSawingVfx)
        if not ReturnValue_5:
            goto('L775')
        self.mSawingVfx.Deactivate()
        # Label 775
        Variable1: bool = False
        Variable1 = True
        goto(ExecutionFlow.Pop())
        # Label 798
        ReturnValue_6: bool = self.HasAnyFuel()
        if not ReturnValue_6:
            goto('L980')
        if not self.mPlayingSound:
            goto('L847')
        goto(ExecutionFlow.Pop())
        # Label 847
        ExecutionFlow.Push("L867")
        if not Variable2:
            goto('L2437')
        goto(ExecutionFlow.Pop())
        # Label 867
        if not Variable2:
            goto('L882')
        goto(ExecutionFlow.Pop())
        # Label 882
        Variable2: bool = True
        ReturnValue5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ChainsawRework_Idle_loop, self, True)
        self.mPlayingSound = True
        Variable: bool = False
        Variable_0: bool = True
        goto(ExecutionFlow.Pop())
        # Label 980
        if not self.mPlayingSound:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1035")
        if not Variable_0:
            goto('L1010')
        goto(ExecutionFlow.Pop())
        # Label 1010
        Variable_0 = True
        if not False:
           goto(ExecutionFlow.Pop())
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 1035
        if not Variable:
            goto('L1050')
        goto(ExecutionFlow.Pop())
        # Label 1050
        Variable = True
        ReturnValue4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_ChainSawRework_All, self, True)
        self.mPlayingSound = False
        Variable2 = False
        Variable2 = True
        goto(ExecutionFlow.Pop())
        # Label 1148
        self.mAnim1pInstance.Montage_Stop(0.6000000238418579, ChainsawSawing_01_Montage)
        self.mAnim1pInstance.Montage_Stop(0.6000000238418579, ChainsawSawingComplete_01_Montage)
        self.UpdateAttachmentState(1, False)
        ReturnValue3_1: bool = EqualEqual_ByteByte(self.mCurrentAudioState, 1)
        if not ReturnValue3_1:
            goto('L1303')
        goto(ExecutionFlow.Pop())
        # Label 1303
        ReturnValue6_0: bool = EqualEqual_ByteByte(self.mCurrentAudioState, 3)
        if not ReturnValue6_0:
            goto('L1406')
        ReturnValue12: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ChainsawRework_SawToIdle, self, True)
        goto('L68')
        # Label 1406
        ReturnValue7_0: bool = EqualEqual_ByteByte(self.mPreviousAudioState, 3)
        if not ReturnValue7_0:
            goto('L127')
        goto('L15')
        # Label 1456
        ReturnValue6_1: bool = self.mAnim1pInstance.Montage_IsPlaying(ChainsawSawing_01_Montage)
        if not ReturnValue6_1:
            goto('L1522')
        goto(ExecutionFlow.Pop())
        # Label 1522
        ReturnValue4_0: float = self.mAnim1pInstance.Montage_Play(ChainsawSawing_01_Montage, 1, 0, 0, True)
        self.UpdateAttachmentState(2, False)
        ReturnValue2: bool = EqualEqual_ByteByte(self.mCurrentAudioState, 2)
        if not ReturnValue2:
            goto('L1657')
        goto(ExecutionFlow.Pop())
        # Label 1657
        ReturnValue5_0: bool = EqualEqual_ByteByte(self.mCurrentAudioState, 3)
        if not ReturnValue5_0:
            goto('L1814')
        ReturnValue3_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ChainsawRework_SawToEngage, self, True)
        # Label 1755
        self.mPlayingSound = True
        self.mPreviousAudioState = self.mCurrentAudioState
        self.mCurrentAudioState = 2
        goto(ExecutionFlow.Pop())
        # Label 1814
        ReturnValue2_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ChainsawRework_IdleToEngage, self, True)
        goto('L1755')
        # Label 1872
        ReturnValue5_1: float = self.mAnim1pInstance.Montage_Play(ChainsawSawingComplete_01_Montage, 1, 0, 0, True)
        self.mMontageLength = ReturnValue5_1
        ReturnValue1_1: bool = EqualEqual_ByteByte(self.mCurrentAudioState, 3)
        if not ReturnValue1_1:
            goto('L2017')
        goto(ExecutionFlow.Pop())
        # Label 2017
        ReturnValue4_1: bool = EqualEqual_ByteByte(self.mCurrentAudioState, 2)
        if not ReturnValue4_1:
            goto('L2174')
        ReturnValue14: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ChainsawRework_EngageToSaw, self, True)
        # Label 2115
        self.mPlayingSound = True
        self.mPreviousAudioState = self.mCurrentAudioState
        self.mCurrentAudioState = 3
        goto(ExecutionFlow.Pop())
        # Label 2174
        ReturnValue13: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ChainsawRework_IdleToSaw, self, True)
        goto('L2115')
        # Label 2232
        if not Variable1:
            goto('L2247')
        goto(ExecutionFlow.Pop())
        # Label 2247
        Variable1 = True
        ReturnValue_7: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(SawingTree_01, self.Chainsaw_skl, "vfxSocket_01", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mSawingVfx = ReturnValue_7
        self.UpdateAttachmentState(3, True)
        goto(ExecutionFlow.Pop())
        # Label 2412
        Variable1 = True
        if not False:
           goto(ExecutionFlow.Pop())
        Variable1 = True
        goto(ExecutionFlow.Pop())
        # Label 2437
        Variable2 = True
        if not False:
           goto(ExecutionFlow.Pop())
        Variable2 = True
        goto(ExecutionFlow.Pop())
        # Label 2462
        ReturnValue_8: bool = self.IsEquipped()
        if not ReturnValue_8:
           goto(ExecutionFlow.Pop())
        self.InterpSawProgress(DeltaSeconds)
        ReturnValue_9: bool = EqualEqual_ByteByte(self.mCurrentState, 4)
        if not ReturnValue_9:
            goto('L185')
        ReturnValue2_1: Ptr[AnimInstance] = self.Chainsaw_skl.GetAnimInstance()
        ReturnValue2_2: bool = ReturnValue2_1.Montage_IsPlaying(ChainsawEquip_01_Montage)
        ReturnValue3_3: bool = ReturnValue2_1.Montage_IsPlaying(ChainsawStinger_01_Montage)
        ReturnValue_10: bool = BooleanOR(ReturnValue3_3, ReturnValue2_2)
        if not ReturnValue_10:
            goto('L2757')
        goto(ExecutionFlow.Pop())
        # Label 2757
        self.UpdateAttachmentState(1, False)
        self.mCurrentAudioState = 1
        goto(ExecutionFlow.Pop())
        # Label 2795
        ExecutionFlow.Push("L3147")
        ReturnValue2_3: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue2_4: Ptr[SkeletalMeshComponent] = ReturnValue2_3.GetMesh1P()
        ReturnValue5_2: Ptr[AnimInstance] = ReturnValue2_4.GetAnimInstance()
        ReturnValue5_3: bool = ReturnValue5_2.Montage_IsPlaying(ChainsawEquip_01_Montage)
        if not ReturnValue5_3:
            goto('L2970')
        goto(ExecutionFlow.Pop())
        # Label 2970
        ReturnValue2_3 = self.GetInstigatorCharacter()
        ReturnValue2_4 = ReturnValue2_3.GetMesh1P()
        ReturnValue5_2 = ReturnValue2_4.GetAnimInstance()
        ReturnValue3_4: float = ReturnValue5_2.Montage_Play(ChainsawEquip_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 3147
        ReturnValue1_2: Ptr[AnimInstance] = self.Chainsaw_skl.GetAnimInstance()
        ReturnValue1_3: bool = ReturnValue1_2.Montage_IsPlaying(ChainsawEquip_01_Montage)
        if not ReturnValue1_3:
            goto('L3255')
        goto(ExecutionFlow.Pop())
        # Label 3255
        ReturnValue1_2 = self.Chainsaw_skl.GetAnimInstance()
        ReturnValue1_4: float = ReturnValue1_2.Montage_Play(ChainsawEquip_01_Montage, 1, 0, 0, True)
        ReturnValue1_5: bool = self.HasAnyFuel()
        if not ReturnValue1_5:
            goto('L3468')
        ReturnValue8: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ChainsawRework_Equip, self, True)
        self.mPlayingSound = True
        goto(ExecutionFlow.Pop())
        # Label 3468
        ReturnValue9: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Chainsaw_Add_Equip_NoFuel, self, True)
        self.mPlayingSound = False
        goto(ExecutionFlow.Pop())
        # Label 3533
        ExecutionFlow.Push("L4310")
        ReturnValue_11: bool = self.ShouldShowStinger()
        if not ReturnValue_11:
            goto('L2795')
        ExecutionFlow.Push("L3924")
        ReturnValue1_6: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_7: Ptr[SkeletalMeshComponent] = ReturnValue1_6.GetMesh1P()
        ReturnValue4_2: Ptr[AnimInstance] = ReturnValue1_7.GetAnimInstance()
        ReturnValue4_3: bool = ReturnValue4_2.Montage_IsPlaying(ChainsawStinger_01_Montage)
        if not ReturnValue4_3:
            goto('L3747')
        goto(ExecutionFlow.Pop())
        # Label 3747
        ReturnValue1_6 = self.GetInstigatorCharacter()
        ReturnValue1_7 = ReturnValue1_6.GetMesh1P()
        ReturnValue4_2 = ReturnValue1_7.GetAnimInstance()
        ReturnValue2_5: float = ReturnValue4_2.Montage_Play(ChainsawStinger_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 3924
        ReturnValue_12: Ptr[AnimInstance] = self.Chainsaw_skl.GetAnimInstance()
        ReturnValue_13: bool = ReturnValue_12.Montage_IsPlaying(ChainsawStinger_01_Montage)
        if not ReturnValue_13:
            goto('L4032')
        goto(ExecutionFlow.Pop())
        # Label 4032
        ReturnValue_12 = self.Chainsaw_skl.GetAnimInstance()
        ReturnValue_14: float = ReturnValue_12.Montage_Play(ChainsawStinger_01_Montage, 1, 0, 0, True)
        ReturnValue2_6: bool = self.HasAnyFuel()
        if not ReturnValue2_6:
            goto('L4245')
        ReturnValue10: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ChainsawRework_Stinger, self, True)
        self.mPlayingSound = True
        goto(ExecutionFlow.Pop())
        # Label 4245
        ReturnValue11: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Chainsaw_Add_Stinger_NoFuel, self, True)
        self.mPlayingSound = False
        goto(ExecutionFlow.Pop())
        # Label 4310
        self.UpdateAttachmentState(4, False)
        goto(ExecutionFlow.Pop())
        # Label 4328
        ReturnValue_15: bool = self.IsLocalInstigator()
        if not ReturnValue_15:
           goto(ExecutionFlow.Pop())
        goto('L3533')
        # Label 4363
        ReturnValue_16: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_17: Ptr[SkeletalMeshComponent] = ReturnValue_16.GetMesh1P()
        ReturnValue3_5: Ptr[AnimInstance] = ReturnValue_17.GetAnimInstance()
        ReturnValue_18: Ptr[AnimMontage] = ReturnValue3_5.GetCurrentActiveMontage()
        ReturnValue3_5.Montage_Stop(0, ReturnValue_18)
        ReturnValue7_1: Ptr[AnimInstance] = self.Chainsaw_skl.GetAnimInstance()
        ReturnValue1_8: Ptr[AnimMontage] = ReturnValue7_1.GetCurrentActiveMontage()
        ReturnValue7_1.Montage_Stop(0, ReturnValue1_8)
        if not self.mPlayingSound:
            goto('L4753')
        ReturnValue7_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_ChainSawRework_All, self, True)
        goto(ExecutionFlow.Pop())
        # Label 4753
        ReturnValue6_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_ChainSawRework_NoFuel, self, True)
        goto(ExecutionFlow.Pop())
        # Label 4807
        ReturnValue1_9: bool = self.IsLocalInstigator()
        if not ReturnValue1_9:
           goto(ExecutionFlow.Pop())
        goto('L4363')
        # Label 4842
        ReturnValue2_7: bool = self.IsLocalInstigator()
        if not ReturnValue2_7:
           goto(ExecutionFlow.Pop())
        goto('L2462')
        # Label 4877
        self.WasUnEquipped()
        goto('L4807')
        goto('L4877')
        # Label 4897
        self.WasEquipped()
        goto('L4328')
        goto('L4897')
        self.ReceiveTick(DeltaSeconds)
        goto('L4842')
    
