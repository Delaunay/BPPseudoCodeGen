
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Equipment.ColorGun.Audio.Play_3P_ColorGun_Equip import Play_3P_ColorGun_Equip
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import SpawnEmitterAtLocation
from Script.Engine import SpawnEmitterAttached
from Game.FactoryGame.Equipment.ColorGun.Animation.Thirdperson.ColorgunReload_01_Montage import ColorgunReload_01_Montage
from Game.FactoryGame.Equipment.ColorGun.Audio.Play_3P_ColorGun_Fire import Play_3P_ColorGun_Fire
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.RebargunEquip_01_Montage import RebargunEquip_01_Montage
from Script.FactoryGame import PlayFireEffect
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Script.FactoryGame import PlayAttachEffects3P
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.ColorgunReload_01_Montage import ColorgunReload_01_Montage
from Script.Engine import IsValid
from Game.FactoryGame.Equipment.ColorGun.Particle.ColorgunHit_01 import ColorgunHit_01
from Script.FactoryGame import FGWeaponAttachment
from Script.FactoryGame import ClientPlayReloadEffect
from Game.FactoryGame.Equipment.ColorGun.Attach_ColorGun import ExecuteUbergraph_Attach_ColorGun.K2Node_Event_flashLocation
from Script.Engine import Default__GameplayStatics
from Script.Engine import Montage_Play
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.ColorGun.Audio.Play_3P_ColorGun_Reload import Play_3P_ColorGun_Reload
from Script.Engine import ParticleSystemComponent
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.ColorgunPrimary_01_Montage import ColorgunPrimary_01_Montage
from Script.FactoryGame import GetAttachedTo
from Game.FactoryGame.Equipment.ColorGun.Attach_ColorGun import ExecuteUbergraph_Attach_ColorGun
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Game.FactoryGame.Equipment.ColorGun.Particle.ColorgunMuzzleflash_01 import ColorgunMuzzleflash_01
from Script.Engine import SkeletalMeshComponent

class Attach_ColorGun(FGWeaponAttachment):
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_RebarGun
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def ClientPlayReloadEffect(self):
        self.ExecuteUbergraph_Attach_ColorGun(15)
    

    def PlayFireEffect(self):
        ExecuteUbergraph_Attach_ColorGun.K2Node_Event_flashLocation = flashLocation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Attach_ColorGun(661)
    

    def PlayAttachEffects3P(self):
        self.ExecuteUbergraph_Attach_ColorGun(1872)
    

    def ExecuteUbergraph_Attach_ColorGun(self):
        goto(ComputedJump("EntryPoint"))
        self.ClientPlayReloadEffect()
        ExecutionFlow.Push("L204")
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_0: Ptr[SkeletalMeshComponent] = ReturnValue.GetMesh3P()
        ReturnValue1: Ptr[AnimInstance] = ReturnValue_0.GetAnimInstance()
        ReturnValue_1: bool = ReturnValue1.Montage_IsPlaying(ColorgunReload_01_Montage)
        if not ReturnValue_1:
            goto('L427')
        goto(ExecutionFlow.Pop())
        # Label 204
        ReturnValue_2: Ptr[AnimInstance] = self.Colorgun_skl.GetAnimInstance()
        ReturnValue1_0: bool = ReturnValue_2.Montage_IsPlaying(ColorgunReload_01_Montage)
        if not ReturnValue1_0:
            goto('L312')
        goto(ExecutionFlow.Pop())
        # Label 312
        ReturnValue_2 = self.Colorgun_skl.GetAnimInstance()
        ReturnValue_3: float = ReturnValue_2.Montage_Play(ColorgunReload_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 427
        ReturnValue = self.GetAttachedTo()
        ReturnValue_0 = ReturnValue.GetMesh3P()
        ReturnValue1 = ReturnValue_0.GetAnimInstance()
        ReturnValue1_1: float = ReturnValue1.Montage_Play(ColorgunReload_01_Montage, 1, 0, 0, True)
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_3P_ColorGun_Reload, self, True)
        goto(ExecutionFlow.Pop())
        self.PlayFireEffect(flashLocation)
        ReturnValue_4: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, ColorgunHit_01, flashLocation, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        ReturnValue_5: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(ColorgunMuzzleflash_01, self.Colorgun_skl, "muzzleVfxSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        ReturnValue2_0: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue2_1: Ptr[SkeletalMeshComponent] = ReturnValue2_0.GetMesh3P()
        ReturnValue3: Ptr[AnimInstance] = ReturnValue2_1.GetAnimInstance()
        ReturnValue3_0: bool = ReturnValue3.Montage_IsPlaying(ColorgunPrimary_01_Montage)
        if not ReturnValue3_0:
            goto('L1061')
        goto(ExecutionFlow.Pop())
        # Label 1061
        ReturnValue2_0 = self.GetAttachedTo()
        ReturnValue2_1 = ReturnValue2_0.GetMesh3P()
        ReturnValue3 = ReturnValue2_1.GetAnimInstance()
        ReturnValue3_1: float = ReturnValue3.Montage_Play(ColorgunPrimary_01_Montage, 1, 0, 0, True)
        ReturnValue_6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_3P_ColorGun_Fire, self, True)
        goto(ExecutionFlow.Pop())
        # Label 1295
        ReturnValue1_2: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue1_3: Ptr[SkeletalMeshComponent] = ReturnValue1_2.GetMesh3P()
        ReturnValue2_2: Ptr[AnimInstance] = ReturnValue1_3.GetAnimInstance()
        ReturnValue2_3: float = ReturnValue2_2.Montage_Play(RebargunEquip_01_Montage, 1, 0, 0, True)
        ReturnValue1_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_3P_ColorGun_Equip, self, True)
        goto(ExecutionFlow.Pop())
        # Label 1529
        ReturnValue1_2 = self.GetAttachedTo()
        ReturnValue1_3 = ReturnValue1_2.GetMesh3P()
        ReturnValue2_2 = ReturnValue1_3.GetAnimInstance()
        ReturnValue_7: bool = Default__KismetSystemLibrary.IsValid(ReturnValue2_2)
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        ReturnValue1_2 = self.GetAttachedTo()
        ReturnValue1_3 = ReturnValue1_2.GetMesh3P()
        ReturnValue2_2 = ReturnValue1_3.GetAnimInstance()
        ReturnValue2_4: bool = ReturnValue2_2.Montage_IsPlaying(RebargunEquip_01_Montage)
        if not ReturnValue2_4:
            goto('L1295')
        goto(ExecutionFlow.Pop())
        self.PlayAttachEffects3P()
        goto('L1529')
    
