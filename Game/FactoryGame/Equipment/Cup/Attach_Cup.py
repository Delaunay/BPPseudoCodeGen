
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Equipment.Cup.Attach_Cup import ExecuteUbergraph_Attach_Cup
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.CupEquip_01_Montage import CupEquip_01_Montage
from Script.FactoryGame import PlayUseEffect
from Script.FactoryGame import Get3PMesh
from Script.FactoryGame import GetAttachedTo
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import PlayAttachEffects3P
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.CupDrink_01_Montage import CupDrink_01_Montage
from Script.FactoryGame import FGEquipmentAttachment
from Script.Engine import IsValid
from Script.Engine import AnimInstance
from Script.Engine import Montage_Play
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Equipment.Cup.Attach_Cup import ExecuteUbergraph_Attach_Cup.K2Node_Event_useLocation

class Attach_Cup(FGEquipmentAttachment):
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_Generic1Hand
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def PlayAttachEffects3P(self):
        self.ExecuteUbergraph_Attach_Cup(10)
    

    def PlayUseEffect(self):
        ExecuteUbergraph_Attach_Cup.K2Node_Event_useLocation = UseLocation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Attach_Cup(725)
    

    def ExecuteUbergraph_Attach_Cup(self):
        self.PlayAttachEffects3P()
        ReturnValue1: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue1_0: Ptr[SkeletalMeshComponent] = ReturnValue1.Get3PMesh()
        ReturnValue1_1: Ptr[AnimInstance] = ReturnValue1_0.GetAnimInstance()
        ReturnValue1_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_1)
        if not ReturnValue1_2:
            goto('L749')
        ReturnValue1 = self.GetAttachedTo()
        ReturnValue1_0 = ReturnValue1.Get3PMesh()
        ReturnValue1_1 = ReturnValue1_0.GetAnimInstance()
        ReturnValue1_3: float = ReturnValue1_1.Montage_Play(CupEquip_01_Montage, 1, 0, 0, True)
        # End
        # Label 370
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_0: Ptr[SkeletalMeshComponent] = ReturnValue.Get3PMesh()
        ReturnValue_1: Ptr[AnimInstance] = ReturnValue_0.GetAnimInstance()
        ReturnValue_2: float = ReturnValue_1.Montage_Play(CupDrink_01_Montage, 1, 0, 0, True)
        # End
        # Label 551
        ReturnValue = self.GetAttachedTo()
        ReturnValue_0 = ReturnValue.Get3PMesh()
        ReturnValue_1 = ReturnValue_0.GetAnimInstance()
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_1)
        if not ReturnValue_3:
            goto('L749')
        goto('L370')
        self.PlayUseEffect(useLocation)
        goto('L551')
    
