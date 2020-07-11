
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.GasMask.Attach_GasMask import ExecuteUbergraph_Attach_GasMask
from Script.Engine import GetAnimInstance
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.GasMaskEquip_01_Montage import GasMaskEquip_01_Montage
from Game.FactoryGame.Equipment.GasMask.Audio.Play_P_GasMask_Equip_3P import Play_P_GasMask_Equip_3P
from Script.FactoryGame import GetAttachedTo
from Script.Engine import SkeletalMeshComponent
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import PlayAttachEffects3P
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.Engine import Montage_Play
from Script.AkAudio import AkComponent
from Script.FactoryGame import FGGasMaskAttachment
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.GasMask.Attach_GasMask import ExecuteUbergraph_Attach_GasMask.K2Node_Event_DeltaSeconds

class Attach_GasMask(FGGasMaskAttachment):
    mAttachSocket = helmetSocket
    mEquipmentSlot = EEquipmentSlot::ES_BACK
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def ReceiveTick(self):
        ExecuteUbergraph_Attach_GasMask.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Attach_GasMask(436)
    

    def PlayAttachEffects3P(self):
        self.ExecuteUbergraph_Attach_GasMask(441)
    

    def ExecuteUbergraph_Attach_GasMask(self):
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
        ReturnValue_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_P_GasMask_Equip_3P, self, True)
        # End
        # End
        goto('L10')
    
