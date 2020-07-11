
from codegen.ue4_stub import *

from Script.Engine import GetAnimInstance
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.GasMaskEquip_01_Montage import GasMaskEquip_01_Montage
from Script.FactoryGame import GetAttachedTo
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import PlayAttachEffects3P
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.Engine import Montage_Play
from Script.FactoryGame import FGGasMaskAttachment
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Equipment.HazardSuit.Attach_HazardSuit import ExecuteUbergraph_Attach_HazardSuit

class Attach_HazardSuit(FGGasMaskAttachment):
    mAttachSocket = helmetSocket
    mEquipmentSlot = EEquipmentSlot::ES_BACK
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def PlayAttachEffects3P(self):
        self.ExecuteUbergraph_Attach_HazardSuit(383)
    

    def ExecuteUbergraph_Attach_HazardSuit(self):
        # Label 10
        self.PlayAttachEffects3P()
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_0: Ptr[SkeletalMeshComponent] = ReturnValue.GetMesh3P()
        ReturnValue_1: Ptr[AnimInstance] = ReturnValue_0.GetAnimInstance()
        ReturnValue_2: bool = ReturnValue_1.Montage_IsPlaying(GasMaskEquip_01_Montage)
        if not ReturnValue_2:
            goto('L198')
        # End
        # Label 198
        ReturnValue = self.GetAttachedTo()
        ReturnValue_0 = ReturnValue.GetMesh3P()
        ReturnValue_1 = ReturnValue_0.GetAnimInstance()
        ReturnValue_3: float = ReturnValue_1.Montage_Play(GasMaskEquip_01_Montage, 1, 0, 0, True)
        # End
        goto('L10')
    
