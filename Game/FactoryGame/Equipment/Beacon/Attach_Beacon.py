
from codegen.ue4_stub import *

from Script.Engine import GetAnimInstance
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.MedkitEquip_01_Montage import MedkitEquip_01_Montage
from Script.FactoryGame import GetAttachedTo
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Equipment.Beacon.Attach_Beacon import ExecuteUbergraph_Attach_Beacon
from Script.FactoryGame import PlayAttachEffects3P
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.Engine import Montage_Play
from Script.Engine import SkeletalMeshComponent
from Script.FactoryGame import FGEquipmentAttachment

class Attach_Beacon(FGEquipmentAttachment):
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_Generic1Hand
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def PlayAttachEffects3P(self):
        self.ExecuteUbergraph_Attach_Beacon(383)
    

    def ExecuteUbergraph_Attach_Beacon(self):
        # Label 10
        self.PlayAttachEffects3P()
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_0: Ptr[SkeletalMeshComponent] = ReturnValue.GetMesh3P()
        ReturnValue_1: Ptr[AnimInstance] = ReturnValue_0.GetAnimInstance()
        ReturnValue_2: bool = ReturnValue_1.Montage_IsPlaying(MedkitEquip_01_Montage)
        if not ReturnValue_2:
            goto('L198')
        # End
        # Label 198
        ReturnValue = self.GetAttachedTo()
        ReturnValue_0 = ReturnValue.GetMesh3P()
        ReturnValue_1 = ReturnValue_0.GetAnimInstance()
        ReturnValue_3: float = ReturnValue_1.Montage_Play(MedkitEquip_01_Montage, 1, 0, 0, True)
        # End
        goto('L10')
    
