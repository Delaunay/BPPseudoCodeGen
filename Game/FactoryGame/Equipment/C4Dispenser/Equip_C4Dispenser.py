
from codegen.ue4_stub import *

from Script.Engine import GetAnimInstance
from Game.FactoryGame.Equipment.NobeliskDetonator.Animation.NobeliskDetonatorEquip_01_Montage import NobeliskDetonatorEquip_01_Montage
from Script.FactoryGame import FGC4Dispenser
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import GetInstigatorCharacter
from Game.FactoryGame.Character.Player.Animation.FirstPerson.NobeliskDetonatorEquip_01_Montage import NobeliskDetonatorEquip_01_Montage
from Game.FactoryGame.Equipment.C4Dispenser.Equip_C4Dispenser import ExecuteUbergraph_Equip_C4Dispenser
from Script.FactoryGame import WasEquipped
from Script.Engine import AnimInstance
from Script.Engine import Montage_IsPlaying
from Script.Engine import Montage_Play
from Script.FactoryGame import GetMesh1P
from Script.Engine import SkeletalMeshComponent

class Equip_C4Dispenser(FGC4Dispenser):
    mC4ExplosiveClass = NewObject[BP_C4Explosive]()
    mMaxChargeTime = 1
    mMaxThrowForce = 300000
    mDelayBetweenExplosions = 0.25
    mMagSize = 1
    mAmmunitionClass = NewObject[Desc_Nobelisk]()
    mDamageTypeClass = NewObject[FGDamageType]()
    mReloadTime = 1.5
    mFireRate = 0.5
    mAttachmentClass = NewObject[Attach_C4Dispenser]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mEquipmentWidget = NewObject[Widget_C4Dispenser]()
    m1PAnimClass = NewObject[Anim_1p]()
    mAttachSocket = hand_lSocket
    mArmAnimation = EArmEquipment::AE_Nobelisk
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Equip_C4Dispenser(15)
    

    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_C4Dispenser(16)
    

    def ExecuteUbergraph_Equip_C4Dispenser(self):
        goto(ComputedJump("EntryPoint"))
        goto(ExecutionFlow.Pop())
        self.WasEquipped()
        ExecutionFlow.Push("L201")
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_0: Ptr[SkeletalMeshComponent] = ReturnValue.GetMesh1P()
        ReturnValue1: Ptr[AnimInstance] = ReturnValue_0.GetAnimInstance()
        ReturnValue1_0: bool = ReturnValue1.Montage_IsPlaying(NobeliskDetonatorEquip_01_Montage)
        if not ReturnValue1_0:
            goto('L424')
        goto(ExecutionFlow.Pop())
        # Label 201
        ReturnValue_1: Ptr[AnimInstance] = self.NobeliskDetonator_Skl_01.GetAnimInstance()
        ReturnValue_2: bool = ReturnValue_1.Montage_IsPlaying(NobeliskDetonatorEquip_01_Montage)
        if not ReturnValue_2:
            goto('L309')
        goto(ExecutionFlow.Pop())
        # Label 309
        ReturnValue_1 = self.NobeliskDetonator_Skl_01.GetAnimInstance()
        ReturnValue_3: float = ReturnValue_1.Montage_Play(NobeliskDetonatorEquip_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 424
        ReturnValue = self.GetInstigatorCharacter()
        ReturnValue_0 = ReturnValue.GetMesh1P()
        ReturnValue1 = ReturnValue_0.GetAnimInstance()
        ReturnValue1_1: float = ReturnValue1.Montage_Play(NobeliskDetonatorEquip_01_Montage, 1, 1, 0, True)
        goto(ExecutionFlow.Pop())
    
