
from codegen.ue4_stub import *

from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import GetInstigatorCharacter
from Script.FactoryGame import WasEquipped
from Script.Engine import GreaterEqual_IntInt
from Game.FactoryGame.Character.Player.Animation.FirstPerson.CupDrink_02_Montage import CupDrink_02_Montage
from Game.FactoryGame.Equipment.Cup.Equip_Cup import ExecuteUbergraph_Equip_Cup
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Script.FactoryGame import FGEquipment
from Script.Engine import IsValid
from Script.FactoryGame import IsLocalInstigator
from Script.FactoryGame import GetMesh1P
from Script.FactoryGame import DoDefaultPrimaryFireEffects
from Script.Engine import Montage_Play
from Script.Engine import RandomIntegerInRange
from Game.FactoryGame.Character.Player.Animation.FirstPerson.CupEquip_01_Montage import CupEquip_01_Montage
from Script.Engine import AnimInstance
from Game.FactoryGame.Character.Player.Animation.FirstPerson.CupDrink_03_Montage import CupDrink_03_Montage
from Script.Engine import SkeletalMeshComponent

class Equip_Cup(FGEquipment):
    mAttachmentClass = NewObject[Attach_Cup]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_Generic1Hand
    mIdlePoseAnimation = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Animation/FirstPerson/CupIdle_01.CupIdle_01')
    mIdlePoseAnimation3p = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Animation/ThirdPerson/CupIdle_01.CupIdle_01')
    mUseDefaultPrimaryFire = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_Cup(10)
    

    def DoDefaultPrimaryFireEffects(self):
        self.ExecuteUbergraph_Equip_Cup(857)
    

    def ExecuteUbergraph_Equip_Cup(self):
        self.WasEquipped()
        ReturnValue: bool = self.IsLocalInstigator()
        if not ReturnValue:
            goto('L872')
        ReturnValue_0: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_1: Ptr[SkeletalMeshComponent] = ReturnValue_0.GetMesh1P()
        ReturnValue_2: Ptr[AnimInstance] = ReturnValue_1.GetAnimInstance()
        ReturnValue_3: float = ReturnValue_2.Montage_Play(CupEquip_01_Montage, 1, 0, 0, True)
        # End
        # Label 235
        ReturnValue_4: int32 = RandomIntegerInRange(0, 10)
        ReturnValue_5: bool = GreaterEqual_IntInt(ReturnValue_4, 8)
        if not ReturnValue_5:
            goto('L502')
        ReturnValue1: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_0: Ptr[SkeletalMeshComponent] = ReturnValue1.GetMesh1P()
        ReturnValue1_1: Ptr[AnimInstance] = ReturnValue1_0.GetAnimInstance()
        ReturnValue1_2: float = ReturnValue1_1.Montage_Play(CupDrink_03_Montage, 1, 0, 0, True)
        # End
        # Label 502
        ReturnValue1 = self.GetInstigatorCharacter()
        ReturnValue1_0 = ReturnValue1.GetMesh1P()
        ReturnValue1_1 = ReturnValue1_0.GetAnimInstance()
        ReturnValue2: float = ReturnValue1_1.Montage_Play(CupDrink_02_Montage, 1, 0, 0, True)
        # End
        # Label 683
        ReturnValue1 = self.GetInstigatorCharacter()
        ReturnValue1_0 = ReturnValue1.GetMesh1P()
        ReturnValue1_1 = ReturnValue1_0.GetAnimInstance()
        ReturnValue_6: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_1)
        if not ReturnValue_6:
            goto('L872')
        goto('L235')
        self.DoDefaultPrimaryFireEffects()
        goto('L683')
    
