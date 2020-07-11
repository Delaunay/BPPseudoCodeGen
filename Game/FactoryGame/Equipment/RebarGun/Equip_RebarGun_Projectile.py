
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.Animation.FirstPerson.RebargunStinger_03_Montage import RebargunStinger_03_Montage
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Equipment.RebarGun.Audio.Play_T_RebarGun_Fire import Play_T_RebarGun_Fire
from Script.Engine import Delay
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Script.FactoryGame import GetInstigatorCharacter
from Script.Engine import Pawn
from Script.Engine import SpawnEmitterAttached
from Script.FactoryGame import WasUnEquipped
from Script.Engine import GetInstigator
from Game.FactoryGame.Character.Player.Animation.FirstPerson.RebargunEquip_01_Montage import RebargunEquip_01_Montage
from Game.FactoryGame.Equipment.RebarGun.Audio.Stop_T_RebarGun_Stinger import Stop_T_RebarGun_Stinger
from Game.FactoryGame.Character.Player.Animation.FirstPerson.RebargunReload_02_Montage import RebargunReload_02_Montage
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Character.Player.CameraShake.RebargunReload_CameraAnim import RebargunReload_CameraAnim
from Game.FactoryGame.Equipment.RebarGun.Animation.RebargunPrimary_01_Montage import RebargunPrimary_01_Montage
from Game.FactoryGame.Equipment.RebarGun.Audio.Play_T_RebarGun_Dry_Shot_01 import Play_T_RebarGun_Dry_Shot_01
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Character.Player.CameraShake.RebargunPrimary_02_CameraAnim import RebargunPrimary_02_CameraAnim
from Script.Engine import PlayerController
from Script.FactoryGame import GetIsReloading
from Script.FactoryGame import FGWeaponProjectileFire
from Script.Engine import GetController
from Game.FactoryGame.Equipment.RebarGun.Equip_RebarGun_Projectile import ExecuteUbergraph_Equip_RebarGun_Projectile
from Script.Engine import GetCurrentActiveMontage
from Script.FactoryGame import PlayReloadEffects
from Script.Engine import IsValid
from Script.FactoryGame import IsLocalInstigator
from Script.Engine import Montage_Stop
from Script.FactoryGame import GetMesh1P
from Game.FactoryGame.Equipment.RebarGun.Animation.RebargunReload_01_Montage import RebargunReload_01_Montage
from Game.FactoryGame.Character.Player.Animation.FirstPerson.RebargunPrimary_02_Montage import RebargunPrimary_02_Montage
from Script.Engine import Default__GameplayStatics
from Script.Engine import AnimMontage
from Script.FactoryGame import HasAmmunition
from Game.FactoryGame.Character.Player.Animation.FirstPerson.RebargunReload_01_Montage import RebargunReload_01_Montage
from Script.Engine import Montage_Play
from Game.FactoryGame.VFX.Equipment.Weapons.RebarGun.P_MuzzleFlash_01 import P_MuzzleFlash_01
from Game.FactoryGame.Equipment.RebarGun.Audio.Play_T_RebarGun_Equip_V2 import Play_T_RebarGun_Equip_V2
from Game.FactoryGame.Equipment.RebarGun.Anim_Rebargun import Anim_Rebargun
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.RebarGun.Animation.RebargunStinger_03_Montage import RebargunStinger_03_Montage
from Script.Engine import RandomIntegerInRange
from Script.Engine import ParticleSystemComponent
from Game.FactoryGame.Equipment.RebarGun.Audio.Play_T_RebarGun_Stinger import Play_T_RebarGun_Stinger
from Game.FactoryGame.Equipment.RebarGun.Animation.RebargunReload_02_Montage import RebargunReload_02_Montage
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.FactoryGame import ShouldShowStinger
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Equipment.RebarGun.Animation.RebargunEquip_01_Montage import RebargunEquip_01_Montage

class Equip_RebarGun_Projectile(FGWeaponProjectileFire):
    mMuteDryFire: bool
    mRandomReloadAnim: int32
    mRandomStingerAnim: int32
    mProjectileData = Namespace(CanTriggerExplodeBySameClass=True, DamageType='/Game/FactoryGame/Equipment/RebarGun/DamageType_RebarGunProjectile.DamageType_RebarGunProjectile_C', DamageTypeExplode='/Script/FactoryGame.FGDamageType', ExplodeAtEndOfLife=False, ExplosionDamage=15, ExplosionRadius=0, ImpactDamage=15, ProjectileClass='/Game/FactoryGame/Equipment/RebarGun/BP_RebarProjectile.BP_RebarProjectile_C', ProjectileLifeSpan=10, ProjectileStickSpan=5, ShouldExplodeOnImpact=False)
    mMagSize = 1
    mAmmunitionClass = NewObject[Desc_SpikedRebar]()
    mDamageTypeClass = NewObject[DamageType_RebarGunProjectile]()
    mReloadTime = 1.7999999523162842
    mFireRate = 1
    mAttachmentClass = NewObject[Attach_RebarGunProjectile]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_RebarGun
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def PlayFireEffect(self):
        self.ExecuteUbergraph_Equip_RebarGun_Projectile(1698)
    

    def PlayReloadEffects(self):
        self.ExecuteUbergraph_Equip_RebarGun_Projectile(2449)
    

    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_RebarGun_Projectile(2454)
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_Equip_RebarGun_Projectile(3939)
    

    def PlayFailedToFireEffects(self):
        self.ExecuteUbergraph_Equip_RebarGun_Projectile(4355)
    

    def ExecuteUbergraph_Equip_RebarGun_Projectile(self):
        goto(ComputedJump("EntryPoint"))
        self.mMuteDryFire = False
        goto(ExecutionFlow.Pop())
        # Label 27
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_T_RebarGun_Fire, self, True)
        self.mMuteDryFire = True
        Default__KismetSystemLibrary.Delay(self, 1.2000000476837158, LatentActionInfo(Linkage = 15, UUID = 203425631, ExecutionFunction = "ExecuteUbergraph_Equip_RebarGun_Projectile", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 168
        ExecutionFlow.Push("L356")
        ReturnValue1: Ptr[AnimInstance] = self.RebarGun_skl.GetAnimInstance()
        Rebargun: Ptr[Anim_Rebargun] = Cast[Anim_Rebargun](ReturnValue1)
        bSuccess: bool = Rebargun
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue1_0: bool = Rebargun.Montage_IsPlaying(RebargunReload_01_Montage)
        if not ReturnValue1_0:
            goto('L922')
        goto(ExecutionFlow.Pop())
        # Label 356
        ReturnValue5: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue5_0: Ptr[SkeletalMeshComponent] = ReturnValue5.GetMesh1P()
        ReturnValue10: Ptr[AnimInstance] = ReturnValue5_0.GetAnimInstance()
        ReturnValue7: bool = ReturnValue10.Montage_IsPlaying(RebargunReload_01_Montage)
        if not ReturnValue7:
            goto('L526')
        goto(ExecutionFlow.Pop())
        # Label 526
        ReturnValue5 = self.GetInstigatorCharacter()
        ReturnValue5_0 = ReturnValue5.GetMesh1P()
        ReturnValue10 = ReturnValue5_0.GetAnimInstance()
        ReturnValue9: float = ReturnValue10.Montage_Play(RebargunReload_01_Montage, 1, 0, 0, True)
        ReturnValue_0: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_1: Ptr[Controller] = ReturnValue_0.GetController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue_1)
        bSuccess1: bool = Controller
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Controller.ClientPlayCameraAnim(RebargunReload_CameraAnim, 1, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        goto(ExecutionFlow.Pop())
        # Label 922
        ReturnValue1_1: float = Rebargun.Montage_Play(RebargunReload_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 995
        self.PlayReloadEffects()
        ReturnValue_2: int32 = RandomIntegerInRange(0, 1000)
        self.mRandomReloadAnim = ReturnValue_2
        ReturnValue_3: bool = self.mRandomReloadAnim <= 999
        if not ReturnValue_3:
            goto('L1123')
        goto('L168')
        # Label 1123
        ExecutionFlow.Push("L1351")
        ReturnValue4: Ptr[AnimInstance] = self.RebarGun_skl.GetAnimInstance()
        ReturnValue4_0: bool = ReturnValue4.Montage_IsPlaying(RebargunReload_02_Montage)
        if not ReturnValue4_0:
            goto('L1236')
        goto(ExecutionFlow.Pop())
        # Label 1236
        ReturnValue4 = self.RebarGun_skl.GetAnimInstance()
        ReturnValue4_1: float = ReturnValue4.Montage_Play(RebargunReload_02_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 1351
        ReturnValue2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue2_0: Ptr[SkeletalMeshComponent] = ReturnValue2.GetMesh1P()
        ReturnValue7_0: Ptr[AnimInstance] = ReturnValue2_0.GetAnimInstance()
        ReturnValue6: bool = ReturnValue7_0.Montage_IsPlaying(RebargunReload_02_Montage)
        if not ReturnValue6:
            goto('L1521')
        goto(ExecutionFlow.Pop())
        # Label 1521
        ReturnValue2 = self.GetInstigatorCharacter()
        ReturnValue2_0 = ReturnValue2.GetMesh1P()
        ReturnValue7_0 = ReturnValue2_0.GetAnimInstance()
        ReturnValue6_0: float = ReturnValue7_0.Montage_Play(RebargunReload_02_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1816")
        ExecutionFlow.Push("L1938")
        ReturnValue_4: Ptr[AnimInstance] = self.RebarGun_skl.GetAnimInstance()
        ReturnValue_5: bool = ReturnValue_4.Montage_IsPlaying(RebargunPrimary_01_Montage)
        if not ReturnValue_5:
            goto('L2334')
        goto(ExecutionFlow.Pop())
        # Label 1816
        ReturnValue_6: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(P_MuzzleFlash_01, self.RebarGun_skl, "muzzleSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        goto('L27')
        # Label 1938
        ReturnValue3: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue3_0: Ptr[SkeletalMeshComponent] = ReturnValue3.GetMesh1P()
        ReturnValue8: Ptr[AnimInstance] = ReturnValue3_0.GetAnimInstance()
        ReturnValue7_1: float = ReturnValue8.Montage_Play(RebargunPrimary_02_Montage, 1, 0, 0, True)
        ReturnValue1_2: Ptr[Pawn] = self.GetInstigator()
        ReturnValue1_3: Ptr[Controller] = ReturnValue1_2.GetController()
        Controller1: Ptr[PlayerController] = Cast[PlayerController](ReturnValue1_3)
        bSuccess2: bool = Controller1
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        Controller1.ClientPlayCameraAnim(RebargunPrimary_02_CameraAnim, 1.100000023841858, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        goto(ExecutionFlow.Pop())
        # Label 2334
        ReturnValue_4 = self.RebarGun_skl.GetAnimInstance()
        ReturnValue_7: float = ReturnValue_4.Montage_Play(RebargunPrimary_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        goto('L995')
        ReturnValue_8: bool = self.IsLocalInstigator()
        if not ReturnValue_8:
           goto(ExecutionFlow.Pop())
        ReturnValue_9: bool = self.ShouldShowStinger()
        if not ReturnValue_9:
            goto('L3146')
        ExecutionFlow.Push("L2923")
        ReturnValue1_4: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_5: Ptr[SkeletalMeshComponent] = ReturnValue1_4.GetMesh1P()
        ReturnValue6_1: Ptr[AnimInstance] = ReturnValue1_5.GetAnimInstance()
        ReturnValue5_1: bool = ReturnValue6_1.Montage_IsPlaying(RebargunStinger_03_Montage)
        if not ReturnValue5_1:
            goto('L2693')
        goto(ExecutionFlow.Pop())
        # Label 2693
        ReturnValue1_4 = self.GetInstigatorCharacter()
        ReturnValue1_5 = ReturnValue1_4.GetMesh1P()
        ReturnValue6_1 = ReturnValue1_5.GetAnimInstance()
        ReturnValue5_2: float = ReturnValue6_1.Montage_Play(RebargunStinger_03_Montage, 1, 0, 0, True)
        ReturnValue2_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_T_RebarGun_Stinger, self, True)
        goto(ExecutionFlow.Pop())
        # Label 2923
        ReturnValue3_1: Ptr[AnimInstance] = self.RebarGun_skl.GetAnimInstance()
        ReturnValue3_2: bool = ReturnValue3_1.Montage_IsPlaying(RebargunStinger_03_Montage)
        if not ReturnValue3_2:
            goto('L3031')
        goto(ExecutionFlow.Pop())
        # Label 3031
        ReturnValue3_1 = self.RebarGun_skl.GetAnimInstance()
        ReturnValue3_3: float = ReturnValue3_1.Montage_Play(RebargunStinger_03_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 3146
        ExecutionFlow.Push("L3716")
        ReturnValue4_2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue4_3: Ptr[SkeletalMeshComponent] = ReturnValue4_2.GetMesh1P()
        ReturnValue9_0: Ptr[AnimInstance] = ReturnValue4_3.GetAnimInstance()
        ReturnValue_10: bool = Default__KismetSystemLibrary.IsValid(ReturnValue9_0)
        if not ReturnValue_10:
           goto(ExecutionFlow.Pop())
        ReturnValue4_2 = self.GetInstigatorCharacter()
        ReturnValue4_3 = ReturnValue4_2.GetMesh1P()
        ReturnValue9_0 = ReturnValue4_3.GetAnimInstance()
        ReturnValue8_0: bool = ReturnValue9_0.Montage_IsPlaying(RebargunEquip_01_Montage)
        if not ReturnValue8_0:
            goto('L3486')
        goto(ExecutionFlow.Pop())
        # Label 3486
        ReturnValue4_2 = self.GetInstigatorCharacter()
        ReturnValue4_3 = ReturnValue4_2.GetMesh1P()
        ReturnValue9_0 = ReturnValue4_3.GetAnimInstance()
        ReturnValue8_1: float = ReturnValue9_0.Montage_Play(RebargunEquip_01_Montage, 1, 0, 0, True)
        ReturnValue3_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_T_RebarGun_Equip_V2, self, True)
        goto(ExecutionFlow.Pop())
        # Label 3716
        ReturnValue2_2: Ptr[AnimInstance] = self.RebarGun_skl.GetAnimInstance()
        ReturnValue2_3: bool = ReturnValue2_2.Montage_IsPlaying(RebargunEquip_01_Montage)
        if not ReturnValue2_3:
            goto('L3824')
        goto(ExecutionFlow.Pop())
        # Label 3824
        ReturnValue2_2 = self.RebarGun_skl.GetAnimInstance()
        ReturnValue2_4: float = ReturnValue2_2.Montage_Play(RebargunEquip_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        self.WasUnEquipped()
        ReturnValue1_6: bool = self.IsLocalInstigator()
        if not ReturnValue1_6:
           goto(ExecutionFlow.Pop())
        ReturnValue4_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_T_RebarGun_Stinger, self, True)
        ReturnValue_11: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_12: Ptr[SkeletalMeshComponent] = ReturnValue_11.GetMesh1P()
        ReturnValue5_3: Ptr[AnimInstance] = ReturnValue_12.GetAnimInstance()
        ReturnValue_13: Ptr[AnimMontage] = ReturnValue5_3.GetCurrentActiveMontage()
        ReturnValue5_3.Montage_Stop(0, ReturnValue_13)
        ReturnValue11: Ptr[AnimInstance] = self.RebarGun_skl.GetAnimInstance()
        ReturnValue1_7: Ptr[AnimMontage] = ReturnValue11.GetCurrentActiveMontage()
        ReturnValue11.Montage_Stop(0, ReturnValue1_7)
        goto(ExecutionFlow.Pop())
        ReturnValue_14: bool = self.HasAmmunition()
        ReturnValue_15: bool = Not_PreBool(ReturnValue_14)
        ReturnValue_16: bool = self.GetIsReloading()
        ReturnValue1_8: bool = Not_PreBool(ReturnValue_16)
        ReturnValue_17: bool = ReturnValue_15 and ReturnValue1_8
        ReturnValue2_5: bool = Not_PreBool(self.mMuteDryFire)
        ReturnValue1_9: bool = ReturnValue_17 and ReturnValue2_5
        if not ReturnValue1_9:
           goto(ExecutionFlow.Pop())
        ReturnValue1_10: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_T_RebarGun_Dry_Shot_01, self, True)
        goto(ExecutionFlow.Pop())
    
