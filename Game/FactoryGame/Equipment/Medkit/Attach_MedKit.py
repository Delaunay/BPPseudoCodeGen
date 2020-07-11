
from codegen.ue4_stub import *

from Script.Engine import GetAnimInstance
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.MedkitEquip_01_Montage import MedkitEquip_01_Montage
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.MedkitUse_01_Montage import MedkitUse_01_Montage
from Script.FactoryGame import GetAttachedTo
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Equipment.Medkit.Attach_MedKit import ExecuteUbergraph_Attach_MedKit.K2Node_Event_useLocation
from Script.FactoryGame import PlayAttachEffects3P
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.Engine import Montage_Play
from Game.FactoryGame.Equipment.Medkit.Attach_MedKit import ExecuteUbergraph_Attach_MedKit
from Script.Engine import SkeletalMeshComponent
from Script.FactoryGame import FGEquipmentAttachment

class Attach_MedKit(FGEquipmentAttachment):
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_Generic1Hand
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def PlayUseEffect(self):
        ExecuteUbergraph_Attach_MedKit.K2Node_Event_useLocation = UseLocation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Attach_MedKit(383)
    

    def PlayAttachEffects3P(self):
        self.ExecuteUbergraph_Attach_MedKit(746)
    

    def ExecuteUbergraph_Attach_MedKit(self):
        # Label 10
        self.PlayAttachEffects3P()
        ReturnValue1: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue1_0: Ptr[SkeletalMeshComponent] = ReturnValue1.GetMesh3P()
        ReturnValue1_1: Ptr[AnimInstance] = ReturnValue1_0.GetAnimInstance()
        ReturnValue1_2: bool = ReturnValue1_1.Montage_IsPlaying(MedkitEquip_01_Montage)
        if not ReturnValue1_2:
            goto('L198')
        # End
        # Label 198
        ReturnValue1 = self.GetAttachedTo()
        ReturnValue1_0 = ReturnValue1.GetMesh3P()
        ReturnValue1_1 = ReturnValue1_0.GetAnimInstance()
        ReturnValue1_3: float = ReturnValue1_1.Montage_Play(MedkitEquip_01_Montage, 1, 0, 0, True)
        # End
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_0: Ptr[SkeletalMeshComponent] = ReturnValue.GetMesh3P()
        ReturnValue_1: Ptr[AnimInstance] = ReturnValue_0.GetAnimInstance()
        ReturnValue_2: bool = ReturnValue_1.Montage_IsPlaying(MedkitUse_01_Montage)
        if not ReturnValue_2:
            goto('L561')
        # End
        # Label 561
        ReturnValue = self.GetAttachedTo()
        ReturnValue_0 = ReturnValue.GetMesh3P()
        ReturnValue_1 = ReturnValue_0.GetAnimInstance()
        ReturnValue_3: float = ReturnValue_1.Montage_Play(MedkitUse_01_Montage, 1, 0, 0, True)
        # End
        goto('L10')
    
