
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Equipment.BuildGun.Attach_BuildGun import ExecuteUbergraph_Attach_BuildGun
from Script.FactoryGame import GetAttachedTo
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.BuildgunEquip_01_Montage import BuildgunEquip_01_Montage
from Script.FactoryGame import PlayAttachEffects3P
from Script.FactoryGame import FGBuildGunAttachment
from Script.Engine import IsValid
from Script.Engine import AnimInstance
from Script.Engine import Montage_IsPlaying
from Script.Engine import Montage_Play
from Script.Engine import SkeletalMeshComponent

class Attach_BuildGun(FGBuildGunAttachment):
    mAttachSocket = buildgun_Socket
    mArmAnimation = EArmEquipment::AE_BuildGun
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def PlayAttachEffects3P(self):
        self.ExecuteUbergraph_Attach_BuildGun(556)
    

    def ExecuteUbergraph_Attach_BuildGun(self):
        # Label 10
        self.PlayAttachEffects3P()
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_0: Ptr[SkeletalMeshComponent] = ReturnValue.GetMesh3P()
        ReturnValue_1: Ptr[AnimInstance] = ReturnValue_0.GetAnimInstance()
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_1)
        if not ReturnValue_2:
            goto('L561')
        ReturnValue = self.GetAttachedTo()
        ReturnValue_0 = ReturnValue.GetMesh3P()
        ReturnValue_1 = ReturnValue_0.GetAnimInstance()
        ReturnValue_3: bool = ReturnValue_1.Montage_IsPlaying(BuildgunEquip_01_Montage)
        if not ReturnValue_3:
            goto('L371')
        # End
        # Label 371
        ReturnValue = self.GetAttachedTo()
        ReturnValue_0 = ReturnValue.GetMesh3P()
        ReturnValue_1 = ReturnValue_0.GetAnimInstance()
        ReturnValue_4: float = ReturnValue_1.Montage_Play(BuildgunEquip_01_Montage, 1, 0, 0, True)
        # End
        goto('L10')
    
