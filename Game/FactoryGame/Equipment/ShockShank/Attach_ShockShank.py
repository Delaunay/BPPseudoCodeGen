
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.Animation.ThirdPerson.ShockShankAttack_01_Montage import ShockShankAttack_01_Montage
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Equipment.ShockShank.Audio.Rework.3P.Play_EQ_ShockShank_EquipV2_3P import Play_EQ_ShockShank_EquipV2_3P
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Equipment.ShockShank.Attach_ShockShank import ExecuteUbergraph_Attach_ShockShank
from Script.Engine import GetAnimInstance
from Script.FactoryGame import PlayAttachEffects3P
from Script.Engine import IsValid
from Script.FactoryGame import FGEquipmentAttachment
from Game.FactoryGame.Equipment.ShockShank.Audio.Rework.3P.Play_EQ_ShockShank_HitRattle_3P import Play_EQ_ShockShank_HitRattle_3P
from Script.Engine import Montage_Play
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.ShockShank.Attach_ShockShank import ExecuteUbergraph_Attach_ShockShank.K2Node_Event_useLocation
from Script.FactoryGame import GetAttachedTo
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.StunSpearEquip_02_Montage import StunSpearEquip_02_Montage

class Attach_ShockShank(FGEquipmentAttachment):
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_StunSpear
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def PlayUseEffect(self):
        ExecuteUbergraph_Attach_ShockShank.K2Node_Event_useLocation = UseLocation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Attach_ShockShank(609)
    

    def PlayAttachEffects3P(self):
        self.ExecuteUbergraph_Attach_ShockShank(1020)
    

    def ExecuteUbergraph_Attach_ShockShank(self):
        # Label 10
        self.PlayAttachEffects3P()
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_0: Ptr[SkeletalMeshComponent] = ReturnValue.GetMesh3P()
        ReturnValue_1: Ptr[AnimInstance] = ReturnValue_0.GetAnimInstance()
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_1)
        if not ReturnValue_2:
            goto('L1025')
        ReturnValue = self.GetAttachedTo()
        ReturnValue_0 = ReturnValue.GetMesh3P()
        ReturnValue_1 = ReturnValue_0.GetAnimInstance()
        ReturnValue_3: bool = ReturnValue_1.Montage_IsPlaying(StunSpearEquip_02_Montage)
        if not ReturnValue_3:
            goto('L371')
        # End
        # Label 371
        ReturnValue = self.GetAttachedTo()
        ReturnValue_0 = ReturnValue.GetMesh3P()
        ReturnValue_1 = ReturnValue_0.GetAnimInstance()
        ReturnValue_4: float = ReturnValue_1.Montage_Play(StunSpearEquip_02_Montage, 1, 0, 0, True)
        ReturnValue_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_ShockShank_EquipV2_3P, self, True)
        # End
        ReturnValue1: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue1_0: Ptr[SkeletalMeshComponent] = ReturnValue1.GetMesh3P()
        ReturnValue1_1: Ptr[AnimInstance] = ReturnValue1_0.GetAnimInstance()
        ReturnValue1_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_1)
        if not ReturnValue1_2:
            goto('L1025')
        ReturnValue1 = self.GetAttachedTo()
        ReturnValue1_0 = ReturnValue1.GetMesh3P()
        ReturnValue1_1 = ReturnValue1_0.GetAnimInstance()
        ReturnValue1_3: float = ReturnValue1_1.Montage_Play(ShockShankAttack_01_Montage, 1, 0, 0, True)
        ReturnValue1_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_ShockShank_HitRattle_3P, self, True)
        # End
        goto('L10')
    
