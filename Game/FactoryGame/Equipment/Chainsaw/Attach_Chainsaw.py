
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.Animation.ThirdPerson.ChainsawSawing_01_Montage import ChainsawSawing_01_Montage
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import EqualEqual_ByteByte
from Game.FactoryGame.Equipment.Chainsaw.Attach_Chainsaw import ExecuteUbergraph_Attach_Chainsaw.K2Node_Event_newUseState
from Script.Engine import SpawnEmitterAttached
from Script.Engine import Default__KismetNodeHelperLibrary
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Play_E_ChainsawRework_EngageToIdle import Play_E_ChainsawRework_EngageToIdle
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.ChainsawEngaged_01_Montage import ChainsawEngaged_01_Montage
from Script.FactoryGame import PlayAttachEffects3P
from Script.FactoryGame import OnAttachmentUseStateUpdated
from Script.Engine import IsValid
from Script.Engine import GetValidValue
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Play_E_ChainsawRework_SawToEngage import Play_E_ChainsawRework_SawToEngage
from Script.Engine import Montage_Stop
from Script.FactoryGame import IsFirstPerson
from Script.FactoryGame import FGEquipmentAttachment
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.ChainsawEquip_01_Montage import ChainsawEquip_01_Montage
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Stop_E_ChainSawRework_All import Stop_E_ChainSawRework_All
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Play_E_ChainsawRework_IdleToEngage import Play_E_ChainsawRework_IdleToEngage
from Script.Engine import Montage_Play
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import NotEqual_ByteByte
from Script.Engine import Conv_IntToByte
from Script.FactoryGame import PlayDetachEffects3P
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Play_E_ChainsawRework_IdleToSaw import Play_E_ChainsawRework_IdleToSaw
from Script.Engine import ParticleSystemComponent
from Game.FactoryGame.Equipment.Chainsaw.Particle.SawingTree_01 import SawingTree_01
from Script.Engine import Actor
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Play_E_ChainsawRework_SawToIdle import Play_E_ChainsawRework_SawToIdle
from Script.FactoryGame import GetAttachedTo
from Game.FactoryGame.Equipment.Chainsaw.EChainsawUseState import EChainsawUseState
from Script.Engine import GetOwner
from Game.FactoryGame.Equipment.Chainsaw.Animation.ChainsawEquip_01_Montage import ChainsawEquip_01_Montage
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Play_E_ChainsawRework_Equip import Play_E_ChainsawRework_Equip
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Equipment.Chainsaw.Audio.Rework.Play_E_ChainsawRework_EngageToSaw import Play_E_ChainsawRework_EngageToSaw
from Game.FactoryGame.Equipment.Chainsaw.Attach_Chainsaw import ExecuteUbergraph_Attach_Chainsaw

class Attach_Chainsaw(FGEquipmentAttachment):
    IsSawing: bool
    IsEquipedFirstTime: bool
    mSawingVfx: Ptr[ParticleSystemComponent]
    mAnim3pInstance: Ptr[AnimInstance]
    mIsSawToIdle: Ptr[AkComponent]
    mChainsawStates: uint8
    mAttachSocket = hand_lSocket
    mArmAnimation = EArmEquipment::AE_ChainSaw
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def OnAttachmentUseStateUpdated(self):
        ExecuteUbergraph_Attach_Chainsaw.K2Node_Event_newUseState = newUseState #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Attach_Chainsaw(3708)
    

    def PlayAttachEffects3P(self):
        self.ExecuteUbergraph_Attach_Chainsaw(3526)
    

    def PlayDetachEffects3P(self):
        self.ExecuteUbergraph_Attach_Chainsaw(3617)
    

    def ExecuteUbergraph_Attach_Chainsaw(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: bool = EqualEqual_ByteByte(self.mChainsawStates, 1)
        if not ReturnValue:
            goto('L61')
        goto(ExecutionFlow.Pop())
        # Label 61
        ReturnValue1: bool = EqualEqual_ByteByte(self.mChainsawStates, 3)
        if not ReturnValue1:
            goto('L180')
        ReturnValue6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ChainsawRework_SawToIdle, self, True)
        # Label 159
        self.mChainsawStates = 1
        goto(ExecutionFlow.Pop())
        # Label 180
        ReturnValue5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ChainsawRework_EngageToIdle, self, True)
        goto('L159')
        # Label 238
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mSawingVfx)
        if not ReturnValue_0:
            goto('L304')
        goto(ExecutionFlow.Pop())
        # Label 304
        ReturnValue_1: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(SawingTree_01, self.Chainsaw_skl, "vfxSocket_01", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        self.mSawingVfx = ReturnValue_1
        ReturnValue1_0: Ptr[Actor] = self.GetOwner()
        Player1: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue1_0)
        bSuccess1: bool = Player1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue1_1: bool = Player1.IsFirstPerson()
        if not ReturnValue1_1:
            goto('L592')
        goto(ExecutionFlow.Pop())
        # Label 592
        ReturnValue4: bool = EqualEqual_ByteByte(self.mChainsawStates, 3)
        if not ReturnValue4:
            goto('L638')
        goto(ExecutionFlow.Pop())
        # Label 638
        ReturnValue5_0: bool = EqualEqual_ByteByte(self.mChainsawStates, 2)
        if not ReturnValue5_0:
            goto('L757')
        ReturnValue7: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ChainsawRework_EngageToSaw, self, True)
        # Label 736
        self.mChainsawStates = 3
        goto(ExecutionFlow.Pop())
        # Label 757
        ReturnValue4_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ChainsawRework_IdleToSaw, self, True)
        goto('L736')
        # Label 815
        self.mSawingVfx.Deactivate()
        self.mSawingVfx = None
        # Label 862
        ReturnValue_2: Ptr[Actor] = self.GetOwner()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_2)
        bSuccess: bool = Player
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_3: bool = Player.IsFirstPerson()
        if not ReturnValue_3:
            goto('L1014')
        goto(ExecutionFlow.Pop())
        # Label 1014
        if not self.IsEquipedFirstTime:
            goto('L15')
        self.IsEquipedFirstTime = False
        goto(ExecutionFlow.Pop())
        # Label 1040
        self.mSawingVfx.Deactivate()
        self.mSawingVfx = None
        # Label 1087
        ReturnValue3: Ptr[Actor] = self.GetOwner()
        Player3: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue3)
        bSuccess3: bool = Player3
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        ReturnValue3_0: bool = Player3.IsFirstPerson()
        if not ReturnValue3_0:
            goto('L1239')
        goto(ExecutionFlow.Pop())
        # Label 1239
        ReturnValue2: bool = EqualEqual_ByteByte(self.mChainsawStates, 2)
        if not ReturnValue2:
            goto('L1285')
        goto(ExecutionFlow.Pop())
        # Label 1285
        ReturnValue3_1: bool = EqualEqual_ByteByte(self.mChainsawStates, 3)
        if not ReturnValue3_1:
            goto('L1404')
        ReturnValue3_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ChainsawRework_SawToEngage, self, True)
        # Label 1383
        self.mChainsawStates = 2
        goto(ExecutionFlow.Pop())
        # Label 1404
        ReturnValue2_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ChainsawRework_IdleToEngage, self, True)
        goto('L1383')
        # Label 1462
        ReturnValue1_2: bool = Default__KismetSystemLibrary.IsValid(self.mSawingVfx)
        if not ReturnValue1_2:
            goto('L862')
        goto('L815')
        # Label 1532
        ReturnValue2_1: bool = Default__KismetSystemLibrary.IsValid(self.mSawingVfx)
        if not ReturnValue2_1:
            goto('L1087')
        goto('L1040')
        # Label 1602
        self.IsSawing = True
        ReturnValue2_2: float = self.mAnim3pInstance.Montage_Play(ChainsawSawing_01_Montage, 1, 0, 0, True)
        goto('L238')
        # Label 1690
        self.IsSawing = True
        ReturnValue3_3: float = self.mAnim3pInstance.Montage_Play(ChainsawEngaged_01_Montage, 1, 0, 0, True)
        goto('L1532')
        # Label 1778
        self.IsSawing = False
        self.mAnim3pInstance.Montage_Stop(0.20000000298023224, ChainsawSawing_01_Montage)
        self.mAnim3pInstance.Montage_Stop(0.20000000298023224, ChainsawEngaged_01_Montage)
        goto('L1462')
        # Label 1886
        ExecutionFlow.Push("L2065")
        ReturnValue_4: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_5: Ptr[SkeletalMeshComponent] = ReturnValue_4.GetMesh3P()
        ReturnValue1_3: Ptr[AnimInstance] = ReturnValue_5.GetAnimInstance()
        ReturnValue1_4: bool = ReturnValue1_3.Montage_IsPlaying(ChainsawEquip_01_Montage)
        if not ReturnValue1_4:
            goto('L2280')
        goto(ExecutionFlow.Pop())
        # Label 2065
        ReturnValue_6: Ptr[AnimInstance] = self.Chainsaw_skl.GetAnimInstance()
        ReturnValue_7: bool = ReturnValue_6.Montage_IsPlaying(None)
        if not ReturnValue_7:
            goto('L2165')
        goto(ExecutionFlow.Pop())
        # Label 2165
        ReturnValue_6 = self.Chainsaw_skl.GetAnimInstance()
        ReturnValue_8: float = ReturnValue_6.Montage_Play(ChainsawEquip_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 2280
        ReturnValue_4 = self.GetAttachedTo()
        ReturnValue_5 = ReturnValue_4.GetMesh3P()
        ReturnValue1_3 = ReturnValue_5.GetAnimInstance()
        ReturnValue1_5: float = ReturnValue1_3.Montage_Play(ChainsawEquip_01_Montage, 1, 0, 0, True)
        ReturnValue2_3: Ptr[Actor] = self.GetOwner()
        Player2: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue2_3)
        bSuccess2: bool = Player2
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        ReturnValue2_4: bool = Player2.IsFirstPerson()
        if not ReturnValue2_4:
            goto('L2612')
        goto(ExecutionFlow.Pop())
        # Label 2612
        ReturnValue1_6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ChainsawRework_Equip, self, True)
        self.IsEquipedFirstTime = True
        self.mChainsawStates = 1
        goto(ExecutionFlow.Pop())
        # Label 2697
        ReturnValue1_7: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue3_4: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_7)
        if not ReturnValue3_4:
           goto(ExecutionFlow.Pop())
        ReturnValue1_7 = self.GetAttachedTo()
        ReturnValue1_8: Ptr[SkeletalMeshComponent] = ReturnValue1_7.GetMesh3P()
        ReturnValue4_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_8)
        if not ReturnValue4_1:
           goto(ExecutionFlow.Pop())
        ReturnValue1_7 = self.GetAttachedTo()
        ReturnValue1_8 = ReturnValue1_7.GetMesh3P()
        ReturnValue2_5: Ptr[AnimInstance] = ReturnValue1_8.GetAnimInstance()
        self.mAnim3pInstance = ReturnValue2_5
        ReturnValue_9: uint8 = Conv_IntToByte(newUseState)
        ReturnValue_10: uint8 = Default__KismetNodeHelperLibrary.GetValidValue(EChainsawUseState, ReturnValue_9)
        CmpSuccess: bool = NotEqual_ByteByte(ReturnValue_10, 1)
        if not CmpSuccess:
            goto('L1778')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_10, 2)
        if not CmpSuccess:
            goto('L1690')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_10, 3)
        if not CmpSuccess:
            goto('L1602')
        CmpSuccess = NotEqual_ByteByte(ReturnValue_10, 4)
        if not CmpSuccess:
            goto('L1778')
        goto(ExecutionFlow.Pop())
        # Label 3318
        ReturnValue_11: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_ChainSawRework_All, self, True)
        ReturnValue2_6: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue2_7: Ptr[SkeletalMeshComponent] = ReturnValue2_6.GetMesh3P()
        ReturnValue3_5: Ptr[AnimInstance] = ReturnValue2_7.GetAnimInstance()
        ReturnValue3_5.Montage_Stop(0.10000000149011612, ChainsawEquip_01_Montage)
        goto(ExecutionFlow.Pop())
        self.PlayAttachEffects3P()
        ReturnValue4_2: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_12: bool = ReturnValue4_2.IsLocallyControlled()
        if not ReturnValue_12:
            goto('L1886')
        goto(ExecutionFlow.Pop())
        self.PlayDetachEffects3P()
        ReturnValue6_0: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue2_8: bool = ReturnValue6_0.IsLocallyControlled()
        if not ReturnValue2_8:
            goto('L3318')
        goto(ExecutionFlow.Pop())
        self.OnAttachmentUseStateUpdated(newUseState)
        ReturnValue3_6: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue5_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue3_6)
        if not ReturnValue5_1:
           goto(ExecutionFlow.Pop())
        ReturnValue5_2: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue1_9: bool = ReturnValue5_2.IsLocallyControlled()
        if not ReturnValue1_9:
            goto('L2697')
        goto(ExecutionFlow.Pop())
    
