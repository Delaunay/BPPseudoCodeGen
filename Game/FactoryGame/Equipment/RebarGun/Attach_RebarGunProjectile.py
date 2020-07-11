
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.Animation.ThirdPerson.RebargunPrimary_01_Montage import RebargunPrimary_01_Montage
from Script.FactoryGame import FGCharacterPlayer
from Script.AkAudio import PostAkEventAtLocation
from Script.Engine import SpawnEmitterAttached
from Game.FactoryGame.Equipment.Rifle.Audio.Play_EQ_Rifle_Fire import Play_EQ_Rifle_Fire
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.RebargunEquip_01_Montage import RebargunEquip_01_Montage
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.RebargunReload_01_Montage import RebargunReload_01_Montage
from Script.FactoryGame import PlayAttachEffects3P
from Script.FactoryGame import ClientPlayReloadEffect
from Game.FactoryGame.Equipment.RebarGun.Animation.ThirdPerson.RebargunPrimary_01_Montage import RebargunPrimary_01_Montage
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.Equipment.RebarGun.Particle.MuzzleFlash_3p import MuzzleFlash_3p
from Script.Engine import Montage_Play
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.RebarGun.Attach_RebarGunProjectile import ExecuteUbergraph_Attach_RebarGunProjectile.K2Node_Event_flashLocation
from Script.FactoryGame import FGWeaponAttachmentProjectile
from Script.Engine import ParticleSystemComponent
from Script.FactoryGame import GetAttachedTo
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Game.FactoryGame.Equipment.RebarGun.Animation.ThirdPerson.RebargunReload_01_Montage import RebargunReload_01_Montage
from Game.FactoryGame.Equipment.RebarGun.Attach_RebarGunProjectile import ExecuteUbergraph_Attach_RebarGunProjectile
from Script.Engine import SkeletalMeshComponent

class Attach_RebarGunProjectile(FGWeaponAttachmentProjectile):
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_RebarGun
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def PlayFireEffect(self):
        ExecuteUbergraph_Attach_RebarGunProjectile.K2Node_Event_flashLocation = flashLocation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Attach_RebarGunProjectile(1759)
    

    def ClientPlayReloadEffect(self):
        self.ExecuteUbergraph_Attach_RebarGunProjectile(1166)
    

    def PlayAttachEffects3P(self):
        self.ExecuteUbergraph_Attach_RebarGunProjectile(1764)
    

    def ExecuteUbergraph_Attach_RebarGunProjectile(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.PlayAttachEffects3P()
        ReturnValue2: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue2_0: Ptr[SkeletalMeshComponent] = ReturnValue2.GetMesh3P()
        ReturnValue4: Ptr[AnimInstance] = ReturnValue2_0.GetAnimInstance()
        ReturnValue4_0: bool = ReturnValue4.Montage_IsPlaying(RebargunEquip_01_Montage)
        if not ReturnValue4_0:
            goto('L199')
        goto(ExecutionFlow.Pop())
        # Label 199
        ReturnValue2 = self.GetAttachedTo()
        ReturnValue2_0 = ReturnValue2.GetMesh3P()
        ReturnValue4 = ReturnValue2_0.GetAnimInstance()
        ReturnValue4_1: float = ReturnValue4.Montage_Play(RebargunEquip_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 380
        ReturnValue: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(MuzzleFlash_3p, self.RebarGun_skl, "muzzleSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        goto(ExecutionFlow.Pop())
        # Label 498
        ReturnValue_0: Ptr[AnimInstance] = self.RebarGun_skl.GetAnimInstance()
        ReturnValue_1: float = ReturnValue_0.Montage_Play(RebargunPrimary_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 613
        ReturnValue_2: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_3: Ptr[SkeletalMeshComponent] = ReturnValue_2.GetMesh3P()
        ReturnValue1: Ptr[AnimInstance] = ReturnValue_3.GetAnimInstance()
        ReturnValue1_0: float = ReturnValue1.Montage_Play(RebargunPrimary_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 794
        ReturnValue_2 = self.GetAttachedTo()
        ReturnValue_3 = ReturnValue_2.GetMesh3P()
        ReturnValue1 = ReturnValue_3.GetAnimInstance()
        ReturnValue_4: bool = ReturnValue1.Montage_IsPlaying(RebargunPrimary_01_Montage)
        if not ReturnValue_4:
            goto('L613')
        goto(ExecutionFlow.Pop())
        # Label 968
        ReturnValue_0 = self.RebarGun_skl.GetAnimInstance()
        ReturnValue1_1: bool = ReturnValue_0.Montage_IsPlaying(RebargunPrimary_01_Montage)
        if not ReturnValue1_1:
            goto('L498')
        goto(ExecutionFlow.Pop())
        # Label 1076
        ExecutionFlow.Push("L380")
        ExecutionFlow.Push("L968")
        ExecutionFlow.Push("L794")
        ReturnValue_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEventAtLocation(self, Play_EQ_Rifle_Fire, flashLocation, Rotator::FromPitchYawRoll(0, 0, 0))
        goto(ExecutionFlow.Pop())
        self.ClientPlayReloadEffect()
        ExecutionFlow.Push("L1355")
        ReturnValue1_2: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue1_3: Ptr[SkeletalMeshComponent] = ReturnValue1_2.GetMesh3P()
        ReturnValue3: Ptr[AnimInstance] = ReturnValue1_3.GetAnimInstance()
        ReturnValue2_1: bool = ReturnValue3.Montage_IsPlaying(RebargunReload_01_Montage)
        if not ReturnValue2_1:
            goto('L1578')
        goto(ExecutionFlow.Pop())
        # Label 1355
        ReturnValue2_2: Ptr[AnimInstance] = self.RebarGun_skl.GetAnimInstance()
        ReturnValue3_0: bool = ReturnValue2_2.Montage_IsPlaying(RebargunReload_01_Montage)
        if not ReturnValue3_0:
            goto('L1463')
        goto(ExecutionFlow.Pop())
        # Label 1463
        ReturnValue2_2 = self.RebarGun_skl.GetAnimInstance()
        ReturnValue2_3: float = ReturnValue2_2.Montage_Play(RebargunReload_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 1578
        ReturnValue1_2 = self.GetAttachedTo()
        ReturnValue1_3 = ReturnValue1_2.GetMesh3P()
        ReturnValue3 = ReturnValue1_3.GetAnimInstance()
        ReturnValue3_1: float = ReturnValue3.Montage_Play(RebargunReload_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        goto('L1076')
        goto('L15')
    
