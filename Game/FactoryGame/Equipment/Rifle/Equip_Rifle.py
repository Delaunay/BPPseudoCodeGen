
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Game.FactoryGame.Character.Player.Animation.FirstPerson.RifleReload_01_Montage import RifleReload_01_Montage
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Game.FactoryGame.Equipment.Rifle.Audio.Stop_E_Rifle_All import Stop_E_Rifle_All
from Script.FactoryGame import GetInstigatorCharacter
from Script.Engine import Pawn
from Script.FactoryGame import WasEquipped
from Script.Engine import SpawnEmitterAttached
from Script.FactoryGame import WasUnEquipped
from Script.Engine import GetInstigator
from Game.FactoryGame.Character.Player.CameraShake.RifleReload_01_CameraAnim import RifleReload_01_CameraAnim
from Script.FactoryGame import PlayFireEffect
from Script.Engine import Conv_IntToFloat
from Script.Engine import ReceiveBeginPlay
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Equipment.Rifle.Audio.Play_E_Rifle_Equip import Play_E_Rifle_Equip
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Character.Player.Animation.FirstPerson.RiflePrimary_01_Montage import RiflePrimary_01_Montage
from Script.Engine import PlayerController
from Game.FactoryGame.Character.Player.Animation.FirstPerson.RifleLoad_01_Montage import RifleLoad_01_Montage
from Game.FactoryGame.Equipment.Rifle.Audio.Play_E_Rifle_Equip_Stinger import Play_E_Rifle_Equip_Stinger
from Script.Engine import GetController
from Game.FactoryGame.Equipment.Rifle.Animation.RifleLoad_01_Montage import RifleLoad_01_Montage
from Game.FactoryGame.Character.Player.Animation.FirstPerson.RifleEquip_01_Montage import RifleEquip_01_Montage
from Game.FactoryGame.Character.Player.CameraShake.RiflePrimary_01_CameraAnim import RiflePrimary_01_CameraAnim
from Script.FactoryGame import PlayReloadEffects
from Script.Engine import IsValid
from Game.FactoryGame.Character.Player.Animation.FirstPerson.RifleStinger_01_Montage import RifleStinger_01_Montage
from Script.FactoryGame import IsLocalInstigator
from Game.FactoryGame.Equipment.Rifle.Animation.RiflePrimary_01_Montage import RiflePrimary_01_Montage
from Game.FactoryGame.Equipment.Rifle.Animation.RifleReload_01_Montage import RifleReload_01_Montage
from Game.FactoryGame.Equipment.Rifle.Animation.RifleStinger_01_Montage import RifleStinger_01_Montage
from Script.FactoryGame import GetMesh1P
from Game.FactoryGame.Equipment.Rifle.Audio.Play_E_Rifle_GunShot import Play_E_Rifle_GunShot
from Game.FactoryGame.Equipment.Rifle.Audio.Play_E_Rifle_Reload_NoClip import Play_E_Rifle_Reload_NoClip
from Script.Engine import Default__GameplayStatics
from Script.Engine import FlushNetDormancy
from Script.FactoryGame import FGWeaponInstantFire
from Game.FactoryGame.Equipment.Rifle.Particle.RifleMuzzleFlash import RifleMuzzleFlash
from Script.Engine import Montage_Play
from Script.AkAudio import Default__AkGameplayStatics
from Script.FactoryGame import GetCurrentAmmo
from Game.FactoryGame.Equipment.Rifle.Audio.Play_E_Rifle_Reload import Play_E_Rifle_Reload
from Game.FactoryGame.Equipment.Rifle.Animation.RifleEquip_01_Montage import RifleEquip_01_Montage
from Script.Engine import ParticleSystemComponent
from Script.AkAudio import SetGlobalRTPCValue
from Script.Engine import Min
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.FactoryGame import ShouldShowStinger
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Equipment.Rifle.Equip_Rifle import ExecuteUbergraph_Equip_Rifle

class Equip_Rifle(FGWeaponInstantFire):
    Fire: FMulticastScriptDelegate
    mLockAngle: float
    mHasReloadedOnce: bool
    mInstantHitDamage = 6
    mWeaponTraceLength = 15000
    mHitParticleEffect = Namespace(AssetPath='/Game/FactoryGame/Equipment/Rifle/Particle/HitImpactGround.HitImpactGround')
    mMagSize = 10
    mAmmunitionClass = NewObject[Desc_CartridgeStandard]()
    mDamageTypeClass = NewObject[DamageType_Rifle]()
    mReloadTime = 3.200000047683716
    mFireRate = 0.20000000298023224
    mAttachmentClass = NewObject[Attach_Rifle]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_Rifle
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_Rifle(4541)
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_Equip_Rifle(4521)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Equip_Rifle(4516)
    

    def PlayReloadEffects(self):
        self.ExecuteUbergraph_Equip_Rifle(4500)
    

    def PlayFireEffect(self):
        self.ExecuteUbergraph_Equip_Rifle(1912)
    

    def ExecuteUbergraph_Equip_Rifle(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 92, UUID = 850435540, ExecutionFunction = "ExecuteUbergraph_Equip_Rifle", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 92
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_0: Ptr[SkeletalMeshComponent] = ReturnValue.GetMesh1P()
        ReturnValue1: Ptr[AnimInstance] = ReturnValue_0.GetAnimInstance()
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        if not ReturnValue1_0:
            goto('L15')
        ReturnValue = self.GetInstigatorCharacter()
        ReturnValue_0 = ReturnValue.GetMesh1P()
        ReturnValue1 = ReturnValue_0.GetAnimInstance()
        ReturnValue1_1: float = ReturnValue1.Montage_Play(RifleEquip_01_Montage, 1, 0, 0, True)
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Rifle_Equip, self, True)
        goto(ExecutionFlow.Pop())
        # Label 491
        self.FlushNetDormancy()
        self.mHasReloadedOnce = True
        ReturnValue_1: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_2: Ptr[Controller] = ReturnValue_1.GetController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Controller.ClientPlayCameraAnim(RifleReload_01_CameraAnim, 1, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        ReturnValue5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_Rifle_All, self, True)
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Rifle_Reload_NoClip, self, True)
        goto(ExecutionFlow.Pop())
        # Label 838
        ReturnValue2_0: Ptr[AnimInstance] = self.Rifle.GetAnimInstance()
        ReturnValue2_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue2_0)
        if not ReturnValue2_1:
            goto('L1060')
        ReturnValue2_0 = self.Rifle.GetAnimInstance()
        ReturnValue2_2: float = ReturnValue2_0.Montage_Play(RifleStinger_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 1060
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 838, UUID = -692211612, ExecutionFunction = "ExecuteUbergraph_Equip_Rifle", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1137
        ReturnValue1_2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_3: Ptr[SkeletalMeshComponent] = ReturnValue1_2.GetMesh1P()
        ReturnValue4: Ptr[AnimInstance] = ReturnValue1_3.GetAnimInstance()
        ReturnValue3_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue4)
        if not ReturnValue3_0:
            goto('L1536')
        ReturnValue1_2 = self.GetInstigatorCharacter()
        ReturnValue1_3 = ReturnValue1_2.GetMesh1P()
        ReturnValue4 = ReturnValue1_3.GetAnimInstance()
        ReturnValue4_0: float = ReturnValue4.Montage_Play(RifleStinger_01_Montage, 1, 0, 0, True)
        ReturnValue7: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Rifle_Equip_Stinger, self, True)
        goto(ExecutionFlow.Pop())
        # Label 1536
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 1137, UUID = 2103120640, ExecutionFunction = "ExecuteUbergraph_Equip_Rifle", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1613
        ReturnValue_3: Ptr[AnimInstance] = self.Rifle.GetAnimInstance()
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_3)
        if not ReturnValue_4:
            goto('L1835')
        ReturnValue_3 = self.Rifle.GetAnimInstance()
        ReturnValue_5: float = ReturnValue_3.Montage_Play(RifleEquip_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 1835
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 1613, UUID = 1748520165, ExecutionFunction = "ExecuteUbergraph_Equip_Rifle", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.PlayFireEffect()
        ReturnValue2_3: bool = self.IsLocalInstigator()
        if not ReturnValue2_3:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L2742")
        ReturnValue4_1: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue4_2: Ptr[SkeletalMeshComponent] = ReturnValue4_1.GetMesh1P()
        ReturnValue8: Ptr[AnimInstance] = ReturnValue4_2.GetAnimInstance()
        ReturnValue8_0: float = ReturnValue8.Montage_Play(RiflePrimary_01_Montage, 1, 0, 0, True)
        ReturnValue2_4: Ptr[Pawn] = self.GetInstigator()
        ReturnValue2_5: Ptr[Controller] = ReturnValue2_4.GetController()
        Controller2: Ptr[PlayerController] = Cast[PlayerController](ReturnValue2_5)
        bSuccess2: bool = Controller2
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        Controller2.ClientPlayCameraAnim(RiflePrimary_01_CameraAnim, 1, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        ReturnValue_6: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(RifleMuzzleFlash, self.Rifle, "muzzleSocket", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 0, True, 0)
        ReturnValue_7: int32 = self.GetCurrentAmmo()
        ReturnValue_8: int32 = Min(ReturnValue_7, 5)
        ReturnValue_9: float = Conv_IntToFloat(ReturnValue_8)
        Default__AkGameplayStatics.SetGlobalRTPCValue("RTPC_LastBullets", ReturnValue_9, 0)
        ReturnValue1_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Rifle_GunShot, self, True)
        ReturnValue_10: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_Rifle_All, self, True)
        goto(ExecutionFlow.Pop())
        # Label 2742
        ReturnValue9: Ptr[AnimInstance] = self.Rifle.GetAnimInstance()
        ReturnValue9_0: float = ReturnValue9.Montage_Play(RiflePrimary_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 2857
        ExecutionFlow.Push("L1613")
        goto('L92')
        # Label 2867
        ReturnValue_11: bool = self.ShouldShowStinger()
        if not ReturnValue_11:
            goto('L2857')
        ExecutionFlow.Push("L838")
        goto('L1137')
        # Label 2911
        ReturnValue3_1: Ptr[AnimInstance] = self.Rifle.GetAnimInstance()
        ReturnValue3_2: float = ReturnValue3_1.Montage_Play(RifleLoad_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 3026
        ExecutionFlow.Push("L3201")
        ReturnValue2_6: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue2_7: Ptr[SkeletalMeshComponent] = ReturnValue2_6.GetMesh1P()
        ReturnValue5_0: Ptr[AnimInstance] = ReturnValue2_7.GetAnimInstance()
        ReturnValue1_5: bool = ReturnValue5_0.Montage_IsPlaying(RifleLoad_01_Montage)
        if not ReturnValue1_5:
            goto('L3309')
        goto(ExecutionFlow.Pop())
        # Label 3201
        ReturnValue3_1 = self.Rifle.GetAnimInstance()
        ReturnValue_12: bool = ReturnValue3_1.Montage_IsPlaying(RifleLoad_01_Montage)
        if not ReturnValue_12:
            goto('L2911')
        goto(ExecutionFlow.Pop())
        # Label 3309
        ReturnValue2_6 = self.GetInstigatorCharacter()
        ReturnValue2_7 = ReturnValue2_6.GetMesh1P()
        ReturnValue5_0 = ReturnValue2_7.GetAnimInstance()
        ReturnValue5_1: float = ReturnValue5_0.Montage_Play(RifleLoad_01_Montage, 1, 0, 0, True)
        goto('L491')
        # Label 3490
        ReturnValue_13: bool = self.IsLocalInstigator()
        if not ReturnValue_13:
           goto(ExecutionFlow.Pop())
        goto('L2867')
        # Label 3525
        ExecutionFlow.Push("L4202")
        ReturnValue3_3: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue3_4: Ptr[SkeletalMeshComponent] = ReturnValue3_3.GetMesh1P()
        ReturnValue6: Ptr[AnimInstance] = ReturnValue3_4.GetAnimInstance()
        ReturnValue2_8: bool = ReturnValue6.Montage_IsPlaying(RifleReload_01_Montage)
        if not ReturnValue2_8:
            goto('L3700')
        goto(ExecutionFlow.Pop())
        # Label 3700
        ReturnValue3_3 = self.GetInstigatorCharacter()
        ReturnValue3_4 = ReturnValue3_3.GetMesh1P()
        ReturnValue6 = ReturnValue3_4.GetAnimInstance()
        ReturnValue7_0: float = ReturnValue6.Montage_Play(RifleReload_01_Montage, 1, 0, 0, True)
        ReturnValue1_6: Ptr[Pawn] = self.GetInstigator()
        ReturnValue1_7: Ptr[Controller] = ReturnValue1_6.GetController()
        Controller1: Ptr[PlayerController] = Cast[PlayerController](ReturnValue1_7)
        bSuccess1: bool = Controller1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Controller1.ClientPlayCameraAnim(RifleReload_01_CameraAnim, 1, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        ReturnValue6_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_Rifle_All, self, True)
        ReturnValue4_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Rifle_Reload, self, True)
        goto(ExecutionFlow.Pop())
        # Label 4202
        ReturnValue7_1: Ptr[AnimInstance] = self.Rifle.GetAnimInstance()
        ReturnValue3_5: bool = ReturnValue7_1.Montage_IsPlaying(RifleReload_01_Montage)
        if not ReturnValue3_5:
            goto('L4310')
        goto(ExecutionFlow.Pop())
        # Label 4310
        ReturnValue7_1 = self.Rifle.GetAnimInstance()
        ReturnValue6_1: float = ReturnValue7_1.Montage_Play(RifleReload_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 4425
        ReturnValue1_8: bool = self.IsLocalInstigator()
        if not ReturnValue1_8:
           goto(ExecutionFlow.Pop())
        if not self.mHasReloadedOnce:
            goto('L3026')
        goto('L3525')
        # Label 4474
        self.PlayReloadEffects()
        goto('L4425')
        # Label 4489
        self.WasUnEquipped()
        goto(ExecutionFlow.Pop())
        goto('L4474')
        # Label 4505
        self.ReceiveBeginPlay()
        goto(ExecutionFlow.Pop())
        goto('L4505')
        goto('L4489')
        # Label 4526
        self.WasEquipped()
        goto('L3490')
        goto('L4526')
    

    def Fire__DelegateSignature(self):
        pass
    
