
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.Rifle.Audio.Play_E_Rifle_Reload_3P import Play_E_Rifle_Reload_3P
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import SpawnEmitterAttached
from Script.FactoryGame import PlayFireEffect
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Equipment.Rifle.Audio.Play_E_Rifle_GunShot_3P import Play_E_Rifle_GunShot_3P
from Script.FactoryGame import PlayAttachEffects3P
from Game.FactoryGame.Equipment.Rifle.Animation.RiflePrimary_01_Montage import RiflePrimary_01_Montage
from Script.FactoryGame import FGWeaponAttachment
from Script.FactoryGame import ClientPlayReloadEffect
from Game.FactoryGame.Equipment.Rifle.Attach_Rifle import ExecuteUbergraph_Attach_Rifle
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.RifleReload_01_Montage import RifleReload_01_Montage
from Script.Engine import Default__GameplayStatics
from Script.Engine import Montage_Play
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.Rifle.Animation.RifleEquip_01_Montage import RifleEquip_01_Montage
from Script.Engine import ParticleSystemComponent
from Script.FactoryGame import GetAttachedTo
from Game.FactoryGame.Equipment.Rifle.Animation.ThirdPerson.RifleReload_01_Montage import RifleReload_01_Montage
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.RiflePrimary_01_Montage import RiflePrimary_01_Montage
from Game.FactoryGame.Equipment.Rifle.Particle.RifleMuzzleFlash_3p import RifleMuzzleFlash_3p
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Game.FactoryGame.Equipment.Rifle.Audio.Play_E_Rifle_Equip_3P import Play_E_Rifle_Equip_3P
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.RifleEquip_01_Montage import RifleEquip_01_Montage
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Equipment.Rifle.Attach_Rifle import ExecuteUbergraph_Attach_Rifle.K2Node_Event_flashLocation

class Attach_Rifle(FGWeaponAttachment):
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_Rifle
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def ClientPlayReloadEffect(self):
        self.ExecuteUbergraph_Attach_Rifle(486)
    

    def PlayAttachEffects3P(self):
        self.ExecuteUbergraph_Attach_Rifle(850)
    

    def PlayFireEffect(self):
        ExecuteUbergraph_Attach_Rifle.K2Node_Event_flashLocation = flashLocation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Attach_Rifle(1214)
    

    def ExecuteUbergraph_Attach_Rifle(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L254")
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_0: Ptr[SkeletalMeshComponent] = ReturnValue.GetMesh3P()
        ReturnValue_1: Ptr[AnimInstance] = ReturnValue_0.GetAnimInstance()
        ReturnValue_2: float = ReturnValue_1.Montage_Play(RiflePrimary_01_Montage, 1, 0, 0, True)
        ReturnValue_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Rifle_GunShot_3P, self, True)
        goto(ExecutionFlow.Pop())
        # Label 254
        ReturnValue1: Ptr[AnimInstance] = self.Rifle.GetAnimInstance()
        ReturnValue1_0: float = ReturnValue1.Montage_Play(RiflePrimary_01_Montage, 1, 0, 0, True)
        ReturnValue_4: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(RifleMuzzleFlash_3p, self.Rifle, "muzzleSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        goto(ExecutionFlow.Pop())
        self.ClientPlayReloadEffect()
        ExecutionFlow.Push("L735")
        ReturnValue1_1: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue1_2: Ptr[SkeletalMeshComponent] = ReturnValue1_1.GetMesh3P()
        ReturnValue3: Ptr[AnimInstance] = ReturnValue1_2.GetAnimInstance()
        ReturnValue3_0: float = ReturnValue3.Montage_Play(RifleReload_01_Montage, 1, 0, 0, True)
        ReturnValue1_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Rifle_Reload_3P, self, True)
        goto(ExecutionFlow.Pop())
        # Label 735
        ReturnValue2: Ptr[AnimInstance] = self.Rifle.GetAnimInstance()
        ReturnValue2_0: float = ReturnValue2.Montage_Play(RifleReload_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        self.PlayAttachEffects3P()
        ExecutionFlow.Push("L1099")
        ReturnValue2_1: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue2_2: Ptr[SkeletalMeshComponent] = ReturnValue2_1.GetMesh3P()
        ReturnValue5: Ptr[AnimInstance] = ReturnValue2_2.GetAnimInstance()
        ReturnValue5_0: float = ReturnValue5.Montage_Play(RifleEquip_01_Montage, 1, 0, 0, True)
        ReturnValue2_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Rifle_Equip_3P, self, True)
        goto(ExecutionFlow.Pop())
        # Label 1099
        ReturnValue4: Ptr[AnimInstance] = self.Rifle.GetAnimInstance()
        ReturnValue4_0: float = ReturnValue4.Montage_Play(RifleEquip_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        self.PlayFireEffect(flashLocation)
        goto('L15')
    
