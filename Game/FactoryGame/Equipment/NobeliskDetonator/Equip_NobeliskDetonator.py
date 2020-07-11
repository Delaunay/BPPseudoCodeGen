
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.Play_E_Nobelisk_Equip import Play_E_Nobelisk_Equip
from Script.Engine import Delay
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Character.Player.Animation.FirstPerson.NobeliskDetonatorEquipExplosive_01_Montage import NobeliskDetonatorEquipExplosive_01_Montage
from Game.FactoryGame.Character.Player.Animation.FirstPerson.NobeliskDetonatorLongThrow_01_Montage import NobeliskDetonatorLongThrow_01_Montage
from Script.FactoryGame import GetInstigatorCharacter
from Game.FactoryGame.Character.Player.Animation.FirstPerson.NobeliskDetonatorEquip_01_Montage import NobeliskDetonatorEquip_01_Montage
from Script.FactoryGame import WasEquipped
from Script.FactoryGame import PlayFireEffect
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.Play_E_Nobelisk_Equip_With_Bomb import Play_E_Nobelisk_Equip_With_Bomb
from Game.FactoryGame.Equipment.NobeliskDetonator.Animation.NobeliskDetonatorThrow_01_Montage import NobeliskDetonatorThrow_01_Montage
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.Stop_E_Nobelisk_StopEquips import Stop_E_Nobelisk_StopEquips
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.Play_E_Nobelisk_Reload import Play_E_Nobelisk_Reload
from Script.FactoryGame import GetIsReloading
from Script.FactoryGame import FGNobeliskDetonator
from Game.FactoryGame.Character.Player.Animation.FirstPerson.NobeliskDetonatorDetonate_02_Montage import NobeliskDetonatorDetonate_02_Montage
from Game.FactoryGame.Equipment.NobeliskDetonator.Animation.NobeliskDetonatorReload_01_Montage import NobeliskDetonatorReload_01_Montage
from Script.FactoryGame import PlayReloadEffects
from Script.Engine import IsValid
from Script.FactoryGame import IsLocalInstigator
from Game.FactoryGame.Character.Player.Animation.FirstPerson.NobeliskDetonatorDetonate_noexpl_02_Montage import NobeliskDetonatorDetonate_noexpl_02_Montage
from Script.FactoryGame import PlayFireReleasedEffects
from Game.FactoryGame.Character.Player.Animation.FirstPerson.NobeliskDetonatorMiddleThrow_01_Montage import NobeliskDetonatorMiddleThrow_01_Montage
from Script.FactoryGame import GetMesh1P
from Game.FactoryGame.Character.Player.Animation.FirstPerson.NobeliskDetonatorReload_01_Montage import NobeliskDetonatorReload_01_Montage
from Script.Engine import BooleanOR
from Game.FactoryGame.Character.Player.Animation.FirstPerson.NobeliskDetonatorStinger_01_Montage import NobeliskDetonatorStinger_01_Montage
from Game.FactoryGame.Equipment.NobeliskDetonator.Animation.NobeliskDetonatorEquip_01_Montage import NobeliskDetonatorEquip_01_Montage
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.Play_E_Nobelisk_Explosion_Beep_With_Bomb import Play_E_Nobelisk_Explosion_Beep_With_Bomb
from Script.FactoryGame import HasAmmunition
from Script.Engine import Montage_Play
from Game.FactoryGame.Equipment.NobeliskDetonator.Animation.NobeliskDetonatorStinger_01_Montage import NobeliskDetonatorStinger_01_Montage
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.NobeliskDetonator.Animation.NobeliskDetonatorDetonate_noexpl_01_Montage import NobeliskDetonatorDetonate_noexpl_01_Montage
from Game.FactoryGame.Equipment.NobeliskDetonator.Animation.NobeliskDetonatorEquipExplosive_01_Montage import NobeliskDetonatorEquipExplosive_01_Montage
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.Play_E_Nobelisk_Explosion_Beep import Play_E_Nobelisk_Explosion_Beep
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.FactoryGame import ShouldShowStinger
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.Play_E_Nobelisk_Equip_Stinger import Play_E_Nobelisk_Equip_Stinger
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Equipment.NobeliskDetonator.Equip_NobeliskDetonator import ExecuteUbergraph_Equip_NobeliskDetonator
from Game.FactoryGame.Equipment.NobeliskDetonator.Animation.NobeliskDetonatorDetonate_02_Montage import NobeliskDetonatorDetonate_02_Montage

class Equip_NobeliskDetonator(FGNobeliskDetonator):
    mExplosiveData = Namespace(CanTriggerExplodeBySameClass=False, DamageType='/Game/FactoryGame/Equipment/NobeliskDetonator/DamageType_NobeliskExplosiveImpact.DamageType_NobeliskExplosiveImpact_C', DamageTypeExplode='/Game/FactoryGame/Equipment/NobeliskDetonator/DamageType_NobeliskExplosive.DamageType_NobeliskExplosive_C', ExplodeAtEndOfLife=True, ExplosionDamage=50, ExplosionRadius=750, ImpactDamage=1, ProjectileClass='/Game/FactoryGame/Equipment/NobeliskDetonator/BP_NobeliskExplosive.BP_NobeliskExplosive_C', ProjectileLifeSpan=-1, ProjectileStickSpan=-1, ShouldExplodeOnImpact=False)
    mExplosiveClass = NewObject[BP_NobeliskExplosive]()
    mMaxChargeTime = 1
    mMaxThrowForce = 3000
    mMinThrowForce = 200
    mDelayBetweenExplosions = 0.15000000596046448
    mMagSize = 1
    mAmmunitionClass = NewObject[Desc_NobeliskExplosive]()
    mDamageTypeClass = NewObject[FGDamageType]()
    mReloadTime = 1
    mFireRate = 0.5
    mAttachmentClass = NewObject[Attach_NobeliskDetonator_L]()
    mSecondaryAttachmentClass = NewObject[Attach_NobeliskDetonator_R]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mAttachSocket = hand_lSocket
    mChildEquipmentClass = NewObject[EquipChild_NobeliskDetonator]()
    mArmAnimation = EArmEquipment::AE_Nobelisk
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def PlayFireEffect(self):
        self.ExecuteUbergraph_Equip_NobeliskDetonator(2642)
    

    def PlayReloadEffects(self):
        self.ExecuteUbergraph_Equip_NobeliskDetonator(1882)
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_Equip_NobeliskDetonator(2647)
    

    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_NobeliskDetonator(2648)
    

    def OnSecondaryFirePressed(self):
        self.ExecuteUbergraph_Equip_NobeliskDetonator(4001)
    

    def PlayFireReleasedEffects(self):
        self.ExecuteUbergraph_Equip_NobeliskDetonator(4756)
    

    def ExecuteUbergraph_Equip_NobeliskDetonator(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ExecutionFlow.Push("L190")
        ReturnValue6: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue6_0: Ptr[SkeletalMeshComponent] = ReturnValue6.GetMesh1P()
        ReturnValue13: Ptr[AnimInstance] = ReturnValue6_0.GetAnimInstance()
        ReturnValue13_0: bool = ReturnValue13.Montage_IsPlaying(NobeliskDetonatorEquipExplosive_01_Montage)
        if not ReturnValue13_0:
            goto('L413')
        goto(ExecutionFlow.Pop())
        # Label 190
        ReturnValue6_1: Ptr[AnimInstance] = self.NobeliskDetonator_Skl_01.GetAnimInstance()
        ReturnValue6_2: bool = ReturnValue6_1.Montage_IsPlaying(NobeliskDetonatorEquipExplosive_01_Montage)
        if not ReturnValue6_2:
            goto('L298')
        goto(ExecutionFlow.Pop())
        # Label 298
        ReturnValue6_1 = self.NobeliskDetonator_Skl_01.GetAnimInstance()
        ReturnValue6_3: float = ReturnValue6_1.Montage_Play(NobeliskDetonatorEquipExplosive_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 413
        ReturnValue6 = self.GetInstigatorCharacter()
        ReturnValue6_0 = ReturnValue6.GetMesh1P()
        ReturnValue13 = ReturnValue6_0.GetAnimInstance()
        ReturnValue13_1: float = ReturnValue13.Montage_Play(NobeliskDetonatorEquipExplosive_01_Montage, 1, 1, 0, True)
        ReturnValue4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Nobelisk_Equip_With_Bomb, self, True)
        goto(ExecutionFlow.Pop())
        ReturnValue5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Nobelisk_Explosion_Beep_With_Bomb, self, True)
        goto(ExecutionFlow.Pop())
        # Label 697
        ReturnValue: Ptr[AnimInstance] = self.NobeliskDetonator_Skl_01.GetAnimInstance()
        ReturnValue_0: float = ReturnValue.Montage_Play(NobeliskDetonatorEquip_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 812
        ReturnValue_1: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_2: Ptr[SkeletalMeshComponent] = ReturnValue_1.GetMesh1P()
        ReturnValue1: Ptr[AnimInstance] = ReturnValue_2.GetAnimInstance()
        ReturnValue1_0: float = ReturnValue1.Montage_Play(NobeliskDetonatorEquip_01_Montage, 1, 1, 0, True)
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Nobelisk_Equip, self, True)
        goto(ExecutionFlow.Pop())
        # Label 1042
        ReturnValue_1 = self.GetInstigatorCharacter()
        ReturnValue_2 = ReturnValue_1.GetMesh1P()
        ReturnValue1 = ReturnValue_2.GetAnimInstance()
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        ReturnValue_1 = self.GetInstigatorCharacter()
        ReturnValue_2 = ReturnValue_1.GetMesh1P()
        ReturnValue1 = ReturnValue_2.GetAnimInstance()
        ReturnValue_4: bool = ReturnValue1.Montage_IsPlaying(NobeliskDetonatorEquip_01_Montage)
        if not ReturnValue_4:
            goto('L812')
        goto(ExecutionFlow.Pop())
        # Label 1377
        ExecutionFlow.Push("L1387")
        goto('L1042')
        # Label 1387
        ReturnValue = self.NobeliskDetonator_Skl_01.GetAnimInstance()
        ReturnValue1_1: bool = ReturnValue.Montage_IsPlaying(NobeliskDetonatorEquip_01_Montage)
        if not ReturnValue1_1:
            goto('L697')
        goto(ExecutionFlow.Pop())
        # Label 1495
        self.PlayFireEffect()
        ReturnValue3_0: bool = self.IsLocalInstigator()
        if not ReturnValue3_0:
           goto(ExecutionFlow.Pop())
        ReturnValue1_2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_3: Ptr[SkeletalMeshComponent] = ReturnValue1_2.GetMesh1P()
        ReturnValue2: Ptr[AnimInstance] = ReturnValue1_3.GetAnimInstance()
        ReturnValue2_0: bool = ReturnValue2.Montage_IsPlaying(NobeliskDetonatorMiddleThrow_01_Montage)
        if not ReturnValue2_0:
            goto('L1705')
        goto(ExecutionFlow.Pop())
        # Label 1705
        ReturnValue1_2 = self.GetInstigatorCharacter()
        ReturnValue1_3 = ReturnValue1_2.GetMesh1P()
        ReturnValue2 = ReturnValue1_3.GetAnimInstance()
        ReturnValue2_1: float = ReturnValue2.Montage_Play(NobeliskDetonatorLongThrow_01_Montage, 1, 1, 0, True)
        goto(ExecutionFlow.Pop())
        self.PlayReloadEffects()
        ReturnValue_5: bool = self.IsLocalInstigator()
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L2380")
        ReturnValue2_2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue2_3: Ptr[SkeletalMeshComponent] = ReturnValue2_2.GetMesh1P()
        ReturnValue3_1: Ptr[AnimInstance] = ReturnValue2_3.GetAnimInstance()
        ReturnValue3_2: bool = ReturnValue3_1.Montage_IsPlaying(NobeliskDetonatorReload_01_Montage)
        if not ReturnValue3_2:
            goto('L2097')
        goto(ExecutionFlow.Pop())
        # Label 2097
        ReturnValue2_2 = self.GetInstigatorCharacter()
        ReturnValue2_3 = ReturnValue2_2.GetMesh1P()
        ReturnValue3_1 = ReturnValue2_3.GetAnimInstance()
        ReturnValue3_3: float = ReturnValue3_1.Montage_Play(NobeliskDetonatorReload_01_Montage, 1, 1, 0, True)
        ReturnValue1_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Nobelisk_Reload, self, True)
        ReturnValue_6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_Nobelisk_StopEquips, self, True)
        goto(ExecutionFlow.Pop())
        # Label 2380
        ReturnValue4_0: Ptr[AnimInstance] = self.NobeliskDetonator_Skl_01.GetAnimInstance()
        ReturnValue4_1: bool = ReturnValue4_0.Montage_IsPlaying(NobeliskDetonatorReload_01_Montage)
        if not ReturnValue4_1:
            goto('L2488')
        goto(ExecutionFlow.Pop())
        # Label 2488
        ReturnValue4_0 = self.NobeliskDetonator_Skl_01.GetAnimInstance()
        ReturnValue4_2: float = ReturnValue4_0.Montage_Play(NobeliskDetonatorReload_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 2603
        ReturnValue_7: bool = self.HasAmmunition()
        if not ReturnValue_7:
            goto('L1377')
        goto('L15')
        goto('L1495')
        goto(ExecutionFlow.Pop())
        self.WasEquipped()
        ReturnValue1_5: bool = self.IsLocalInstigator()
        if not ReturnValue1_5:
           goto(ExecutionFlow.Pop())
        ReturnValue_8: bool = self.ShouldShowStinger()
        if not ReturnValue_8:
            goto('L2603')
        ExecutionFlow.Push("L3127")
        ReturnValue5_0: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue5_1: Ptr[SkeletalMeshComponent] = ReturnValue5_0.GetMesh1P()
        ReturnValue12: Ptr[AnimInstance] = ReturnValue5_1.GetAnimInstance()
        ReturnValue11: bool = ReturnValue12.Montage_IsPlaying(NobeliskDetonatorStinger_01_Montage)
        if not ReturnValue11:
            goto('L2897')
        goto(ExecutionFlow.Pop())
        # Label 2897
        ReturnValue5_0 = self.GetInstigatorCharacter()
        ReturnValue5_1 = ReturnValue5_0.GetMesh1P()
        ReturnValue12 = ReturnValue5_1.GetAnimInstance()
        ReturnValue12_0: float = ReturnValue12.Montage_Play(NobeliskDetonatorStinger_01_Montage, 1, 1, 0, True)
        ReturnValue2_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Nobelisk_Equip_Stinger, self, True)
        goto(ExecutionFlow.Pop())
        # Label 3127
        ReturnValue11_0: Ptr[AnimInstance] = self.NobeliskDetonator_Skl_01.GetAnimInstance()
        ReturnValue12_1: bool = ReturnValue11_0.Montage_IsPlaying(NobeliskDetonatorStinger_01_Montage)
        if not ReturnValue12_1:
            goto('L3235')
        goto(ExecutionFlow.Pop())
        # Label 3235
        ReturnValue11_0 = self.NobeliskDetonator_Skl_01.GetAnimInstance()
        ReturnValue11_1: float = ReturnValue11_0.Montage_Play(NobeliskDetonatorStinger_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 3350
        ExecutionFlow.Push("L3778")
        ReturnValue3_4: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue3_5: Ptr[SkeletalMeshComponent] = ReturnValue3_4.GetMesh1P()
        ReturnValue5_2: Ptr[AnimInstance] = ReturnValue3_5.GetAnimInstance()
        ReturnValue5_3: bool = ReturnValue5_2.Montage_IsPlaying(NobeliskDetonatorDetonate_02_Montage)
        if not ReturnValue5_3:
            goto('L3525')
        goto(ExecutionFlow.Pop())
        # Label 3525
        ReturnValue3_4 = self.GetInstigatorCharacter()
        ReturnValue3_5 = ReturnValue3_4.GetMesh1P()
        ReturnValue5_2 = ReturnValue3_5.GetAnimInstance()
        ReturnValue5_4: float = ReturnValue5_2.Montage_Play(NobeliskDetonatorDetonate_02_Montage, 1, 1, 0, True)
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 643, UUID = -800153213, ExecutionFunction = "ExecuteUbergraph_Equip_NobeliskDetonator", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 3778
        ReturnValue7: Ptr[AnimInstance] = self.NobeliskDetonator_Skl_01.GetAnimInstance()
        ReturnValue7_0: bool = ReturnValue7.Montage_IsPlaying(NobeliskDetonatorDetonate_02_Montage)
        if not ReturnValue7_0:
            goto('L3886')
        goto(ExecutionFlow.Pop())
        # Label 3886
        ReturnValue7 = self.NobeliskDetonator_Skl_01.GetAnimInstance()
        ReturnValue7_1: float = ReturnValue7.Montage_Play(NobeliskDetonatorDetonate_02_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        ReturnValue4_3: bool = self.IsLocalInstigator()
        if not ReturnValue4_3:
           goto(ExecutionFlow.Pop())
        ReturnValue1_6: bool = self.HasAmmunition()
        ReturnValue_9: bool = self.GetIsReloading()
        ReturnValue_10: bool = BooleanOR(ReturnValue1_6, ReturnValue_9)
        if not ReturnValue_10:
            goto('L4128')
        goto('L3350')
        # Label 4128
        ExecutionFlow.Push("L4533")
        ReturnValue4_4: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue4_5: Ptr[SkeletalMeshComponent] = ReturnValue4_4.GetMesh1P()
        ReturnValue8: Ptr[AnimInstance] = ReturnValue4_5.GetAnimInstance()
        ReturnValue9: bool = ReturnValue8.Montage_IsPlaying(NobeliskDetonatorDetonate_noexpl_02_Montage)
        if not ReturnValue9:
            goto('L4303')
        goto(ExecutionFlow.Pop())
        # Label 4303
        ReturnValue4_4 = self.GetInstigatorCharacter()
        ReturnValue4_5 = ReturnValue4_4.GetMesh1P()
        ReturnValue8 = ReturnValue4_5.GetAnimInstance()
        ReturnValue8_0: float = ReturnValue8.Montage_Play(NobeliskDetonatorDetonate_noexpl_02_Montage, 1, 1, 0.10000000149011612, True)
        ReturnValue6_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Nobelisk_Explosion_Beep, self, True)
        goto(ExecutionFlow.Pop())
        # Label 4533
        ReturnValue9_0: Ptr[AnimInstance] = self.NobeliskDetonator_Skl_01.GetAnimInstance()
        ReturnValue8_1: bool = ReturnValue9_0.Montage_IsPlaying(NobeliskDetonatorDetonate_noexpl_01_Montage)
        if not ReturnValue8_1:
            goto('L4641')
        goto(ExecutionFlow.Pop())
        # Label 4641
        ReturnValue9_0 = self.NobeliskDetonator_Skl_01.GetAnimInstance()
        ReturnValue9_1: float = ReturnValue9_0.Montage_Play(NobeliskDetonatorDetonate_noexpl_01_Montage, 1, 0, 0.10000000149011612, True)
        goto(ExecutionFlow.Pop())
        self.PlayFireReleasedEffects()
        ReturnValue2_5: bool = self.IsLocalInstigator()
        if not ReturnValue2_5:
           goto(ExecutionFlow.Pop())
        ReturnValue10: Ptr[AnimInstance] = self.NobeliskDetonator_Skl_01.GetAnimInstance()
        ReturnValue10_0: bool = ReturnValue10.Montage_IsPlaying(NobeliskDetonatorThrow_01_Montage)
        if not ReturnValue10_0:
            goto('L4904')
        goto(ExecutionFlow.Pop())
        # Label 4904
        ReturnValue10 = self.NobeliskDetonator_Skl_01.GetAnimInstance()
        ReturnValue10_1: float = ReturnValue10.Montage_Play(NobeliskDetonatorThrow_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
    
