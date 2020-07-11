
from codegen.ue4_stub import *

from Script.Engine import GetAnimInstance
from Script.FactoryGame import GetAttachedTo
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Equipment.GolfCart.Attach_GolfCartDispenser import ExecuteUbergraph_Attach_GolfCartDispenser
from Script.Engine import AnimMontage
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.GolfcartEquip_01_Montage import GolfcartEquip_01_Montage
from Script.Engine import GetCurrentActiveMontage
from Script.FactoryGame import PlayAttachEffects3P
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.Engine import Montage_Play
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.PortableMinerEquip_01_Montage import PortableMinerEquip_01_Montage
from Script.Engine import Montage_Stop
from Script.Engine import SkeletalMeshComponent
from Script.FactoryGame import PlayDetachEffects3P
from Script.FactoryGame import FGEquipmentAttachment

class Attach_GolfCartDispenser(FGEquipmentAttachment):
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_Generic2Hand
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def PlayAttachEffects3P(self):
        self.ExecuteUbergraph_Attach_GolfCartDispenser(584)
    

    def PlayDetachEffects3P(self):
        self.ExecuteUbergraph_Attach_GolfCartDispenser(599)
    

    def ExecuteUbergraph_Attach_GolfCartDispenser(self):
        # Label 10
        self.PlayDetachEffects3P()
        ReturnValue1: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue1_0: Ptr[SkeletalMeshComponent] = ReturnValue1.GetMesh3P()
        ReturnValue1_1: Ptr[AnimInstance] = ReturnValue1_0.GetAnimInstance()
        ReturnValue: Ptr[AnimMontage] = ReturnValue1_1.GetCurrentActiveMontage()
        ReturnValue1_1.Montage_Stop(0, ReturnValue)
        # End
        # Label 221
        ReturnValue_0: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_1: Ptr[SkeletalMeshComponent] = ReturnValue_0.GetMesh3P()
        ReturnValue_2: Ptr[AnimInstance] = ReturnValue_1.GetAnimInstance()
        ReturnValue_3: float = ReturnValue_2.Montage_Play(GolfcartEquip_01_Montage, 1, 0, 0, True)
        # End
        # Label 406
        ReturnValue_0 = self.GetAttachedTo()
        ReturnValue_1 = ReturnValue_0.GetMesh3P()
        ReturnValue_2 = ReturnValue_1.GetAnimInstance()
        ReturnValue_4: bool = ReturnValue_2.Montage_IsPlaying(PortableMinerEquip_01_Montage)
        if not ReturnValue_4:
            goto('L221')
        # End
        self.PlayAttachEffects3P()
        goto('L406')
        goto('L10')
    
