
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.StunSpearAttack_02_Montage import StunSpearAttack_02_Montage
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Equipment.StunSpear.Audio.Play_T_ShockBaton_Attack import Play_T_ShockBaton_Attack
from Script.Engine import Not_PreBool
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Equipment.StunSpear.Audio.Play_E_ShockBaton_Equip_02 import Play_E_ShockBaton_Equip_02
from Game.FactoryGame.Equipment.StunSpear.Animation.Thirdperson.Equip_02_Montage import Equip_02_Montage
from Script.FactoryGame import PlayAttachEffects3P
from Script.FactoryGame import FGEquipmentAttachment
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.StunSpearAttack_01_Montage import StunSpearAttack_01_Montage
from Script.Engine import Montage_Play
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.StunSpear.Attach_StunSpear import ExecuteUbergraph_Attach_StunSpear
from Script.FactoryGame import GetAttachedTo
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Game.FactoryGame.Equipment.StunSpear.Attach_StunSpear import ExecuteUbergraph_Attach_StunSpear.K2Node_Event_useLocation
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.StunSpearEquip_02_Montage import StunSpearEquip_02_Montage

class Attach_StunSpear(FGEquipmentAttachment):
    mNextAttackAnim: bool
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_StunSpear
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def PlayUseEffect(self):
        ExecuteUbergraph_Attach_StunSpear.K2Node_Event_useLocation = UseLocation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Attach_StunSpear(553)
    

    def PlayAttachEffects3P(self):
        self.ExecuteUbergraph_Attach_StunSpear(1385)
    

    def ExecuteUbergraph_Attach_StunSpear(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.PlayAttachEffects3P()
        ReturnValue1: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue1_0: Ptr[SkeletalMeshComponent] = ReturnValue1.GetMesh3P()
        ReturnValue2: Ptr[AnimInstance] = ReturnValue1_0.GetAnimInstance()
        ReturnValue2_0: bool = ReturnValue2.Montage_IsPlaying(StunSpearEquip_02_Montage)
        if not ReturnValue2_0:
            goto('L199')
        goto(ExecutionFlow.Pop())
        # Label 199
        ExecutionFlow.Push("L385")
        ReturnValue1 = self.GetAttachedTo()
        ReturnValue1_0 = ReturnValue1.GetMesh3P()
        ReturnValue2 = ReturnValue1_0.GetAnimInstance()
        ReturnValue3: float = ReturnValue2.Montage_Play(StunSpearEquip_02_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 385
        ReturnValue: Ptr[AnimInstance] = self.SkeletalMesh.GetAnimInstance()
        ReturnValue_0: float = ReturnValue.Montage_Play(Equip_02_Montage, 1, 0, 0, True)
        ReturnValue_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ShockBaton_Equip_02, self, True)
        goto(ExecutionFlow.Pop())
        ReturnValue_2: bool = Not_PreBool(self.mNextAttackAnim)
        if not ReturnValue_2:
            goto('L770')
        ReturnValue_3: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_4: Ptr[SkeletalMeshComponent] = ReturnValue_3.GetMesh3P()
        ReturnValue1_1: Ptr[AnimInstance] = ReturnValue_4.GetAnimInstance()
        ReturnValue_5: bool = ReturnValue1_1.Montage_IsPlaying(StunSpearAttack_01_Montage)
        if not ReturnValue_5:
            goto('L1189')
        goto(ExecutionFlow.Pop())
        # Label 770
        ReturnValue_3 = self.GetAttachedTo()
        ReturnValue_4 = ReturnValue_3.GetMesh3P()
        ReturnValue1_1 = ReturnValue_4.GetAnimInstance()
        ReturnValue1_2: bool = ReturnValue1_1.Montage_IsPlaying(StunSpearAttack_02_Montage)
        if not ReturnValue1_2:
            goto('L944')
        goto(ExecutionFlow.Pop())
        # Label 944
        ReturnValue_3 = self.GetAttachedTo()
        ReturnValue_4 = ReturnValue_3.GetMesh3P()
        ReturnValue1_1 = ReturnValue_4.GetAnimInstance()
        ReturnValue1_3: float = ReturnValue1_1.Montage_Play(StunSpearAttack_02_Montage, 1, 0, 0, True)
        self.mNextAttackAnim = False
        # Label 1135
        ReturnValue1_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_T_ShockBaton_Attack, self, True)
        goto(ExecutionFlow.Pop())
        # Label 1189
        ReturnValue_3 = self.GetAttachedTo()
        ReturnValue_4 = ReturnValue_3.GetMesh3P()
        ReturnValue1_1 = ReturnValue_4.GetAnimInstance()
        ReturnValue2_1: float = ReturnValue1_1.Montage_Play(StunSpearAttack_01_Montage, 1, 0, 0, True)
        self.mNextAttackAnim = True
        goto('L1135')
        goto('L15')
    
