
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.CameraShake.ShockShankAttack_04_CameraAnim import ShockShankAttack_04_CameraAnim
from Script.AkAudio import PostAkEvent
from Game.FactoryGame.Character.Player.Animation.FirstPerson.ShockShankEquip_01_Montage import ShockShankEquip_01_Montage
from Game.FactoryGame.Character.Player.Animation.FirstPerson.ShockShankStinger_02_Montage import ShockShankStinger_02_Montage
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Script.FactoryGame import GetInstigatorCharacter
from Script.Engine import Pawn
from Script.FactoryGame import WasEquipped
from Script.FactoryGame import WasUnEquipped
from Script.Engine import GreaterEqual_IntInt
from Script.Engine import GetInstigator
from Game.FactoryGame.Character.Player.Animation.FirstPerson.ShockShankStinger_03_Montage import ShockShankStinger_03_Montage
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Script.Engine import PlayerController
from Script.Engine import GetController
from Game.FactoryGame.Equipment.ShockShank.Audio.Rework.Stop_EQ_ShockShank_EquipStinger import Stop_EQ_ShockShank_EquipStinger
from Game.FactoryGame.Character.Player.Animation.FirstPerson.ShockShankAttack_01_Montage import ShockShankAttack_01_Montage
from Game.FactoryGame.Equipment.ShockShank.Audio.Rework.Play_EQ_ShockShank_StingerV2_02 import Play_EQ_ShockShank_StingerV2_02
from Script.Engine import GetCurrentActiveMontage
from Script.Engine import IsValid
from Script.Engine import Montage_Stop
from Script.FactoryGame import GetMesh1P
from Script.Engine import EqualEqual_IntInt
from Game.FactoryGame.Equipment.ShockShank.Animation.ShockShankAttack_01_Montage import ShockShankAttack_01_Montage
from Game.FactoryGame.Equipment.ShockShank.Animation.ShockShankStinger_02_Montage import ShockShankStinger_02_Montage
from Script.FactoryGame import PlayStunEffects
from Game.FactoryGame.Equipment.ShockShank.Equip_ShockShank import ExecuteUbergraph_Equip_ShockShank
from Game.FactoryGame.Character.Player.Animation.FirstPerson.ShockShankAttack_04_Montage import ShockShankAttack_04_Montage
from Script.Engine import AnimMontage
from Script.FactoryGame import GetShouldPlaySecondSwing
from Script.Engine import Montage_Play
from Game.FactoryGame.Character.Player.CameraShake.ShockShankAttack_03_CamerAnim import ShockShankAttack_03_CamerAnim
from Game.FactoryGame.Equipment.ShockShank.Animation.ShockShankEquip_01_Montage import ShockShankEquip_01_Montage
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.ShockShank.Audio.Rework.Play_EQ_ShockShank_StingerV2_01 import Play_EQ_ShockShank_StingerV2_01
from Script.FactoryGame import FGEquipmentStunSpear
from Game.FactoryGame.Equipment.ShockShank.Audio.Rework.Play_EQ_ShockShank_EquipV2 import Play_EQ_ShockShank_EquipV2
from Game.FactoryGame.Character.Player.Animation.FirstPerson.ShockShankAttack_03_Montage import ShockShankAttack_03_Montage
from Script.Engine import RandomIntegerInRange
from Game.FactoryGame.Equipment.ShockShank.Audio.Rework.Play_EQ_ShockShank_Punch import Play_EQ_ShockShank_Punch
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.FactoryGame import ShouldShowStinger
from Game.FactoryGame.Equipment.ShockShank.Audio.Rework.Play_EQ_ShockShank_HitRattle import Play_EQ_ShockShank_HitRattle
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Character.Player.CameraShake.ShockShankAttack_01_CameraAnim import ShockShankAttack_01_CameraAnim

class Equip_ShockShank(FGEquipmentStunSpear):
    mRandomAttackAnim: int32
    mAKShockShankLoop: Ptr[AkComponent]
    mPlayingSound: bool
    mRandomStingerAnim: int32
    mDamageTypeClass = NewObject[DamageType_XenoZapper]()
    mSecondSwingMaxTime = 1.100000023841858
    mSecondSwingCooldDownTime = 1
    mDamage = 5
    mAttackDistance = 350
    mAttachmentClass = NewObject[Attach_ShockShank]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_ShockShank
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=1, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_ShockShank(2903)
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_Equip_ShockShank(5118)
    

    def PlayStunEffects(self):
        self.ExecuteUbergraph_Equip_ShockShank(2998)
    

    def OnHitTarget(self):
        self.ExecuteUbergraph_Equip_ShockShank(5123)
    

    def ExecuteUbergraph_Equip_ShockShank(self):
        # Label 10
        self.WasUnEquipped()
        ReturnValue1: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue: bool = ReturnValue1.IsLocallyControlled()
        if not ReturnValue:
            goto('L5123')
        ReturnValue1 = self.GetInstigatorCharacter()
        ReturnValue1_0: Ptr[SkeletalMeshComponent] = ReturnValue1.GetMesh1P()
        ReturnValue6: Ptr[AnimInstance] = ReturnValue1_0.GetAnimInstance()
        ReturnValue1_1: Ptr[AnimMontage] = ReturnValue6.GetCurrentActiveMontage()
        ReturnValue6.Montage_Stop(0, ReturnValue1_1)
        ReturnValue3: Ptr[AnimInstance] = self.ShockShank_skl.GetAnimInstance()
        ReturnValue_0: Ptr[AnimMontage] = ReturnValue3.GetCurrentActiveMontage()
        ReturnValue3.Montage_Stop(0, ReturnValue_0)
        ReturnValue3_0: Ptr[Pawn] = self.GetInstigator()
        ReturnValue3_1: Ptr[Controller] = ReturnValue3_0.GetController()
        Controller3: Ptr[PlayerController] = Cast[PlayerController](ReturnValue3_1)
        bSuccess3: bool = Controller3
        if not bSuccess3:
            goto('L5123')
        Controller3.PlayerCameraManager.StopAllCameraAnims(True)
        ReturnValue9: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue7: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_EQ_ShockShank_EquipStinger, ReturnValue9, True)
        # End
        # Label 708
        ReturnValue_1: bool = EqualEqual_IntInt(self.mRandomStingerAnim, 1)
        if not ReturnValue_1:
            goto('L1099')
        ReturnValue2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue2_0: Ptr[SkeletalMeshComponent] = ReturnValue2.GetMesh1P()
        ReturnValue7_0: Ptr[AnimInstance] = ReturnValue2_0.GetAnimInstance()
        ReturnValue1_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue7_0)
        if not ReturnValue1_2:
            goto('L5123')
        ReturnValue2 = self.GetInstigatorCharacter()
        ReturnValue2_0 = ReturnValue2.GetMesh1P()
        ReturnValue7_0 = ReturnValue2_0.GetAnimInstance()
        ReturnValue_2: bool = ReturnValue7_0.Montage_IsPlaying(ShockShankStinger_02_Montage)
        if not ReturnValue_2:
            goto('L1818')
        # End
        # Label 1099
        ReturnValue2 = self.GetInstigatorCharacter()
        ReturnValue2_0 = ReturnValue2.GetMesh1P()
        ReturnValue7_0 = ReturnValue2_0.GetAnimInstance()
        ReturnValue2_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue7_0)
        if not ReturnValue2_1:
            goto('L5123')
        ReturnValue2 = self.GetInstigatorCharacter()
        ReturnValue2_0 = ReturnValue2.GetMesh1P()
        ReturnValue7_0 = ReturnValue2_0.GetAnimInstance()
        ReturnValue1_3: bool = ReturnValue7_0.Montage_IsPlaying(ShockShankStinger_03_Montage)
        if not ReturnValue1_3:
            goto('L1442')
        # End
        # Label 1442
        ReturnValue2 = self.GetInstigatorCharacter()
        ReturnValue2_0 = ReturnValue2.GetMesh1P()
        ReturnValue7_0 = ReturnValue2_0.GetAnimInstance()
        ReturnValue8: float = ReturnValue7_0.Montage_Play(ShockShankStinger_03_Montage, 1, 1, 0, True)
        ReturnValue6_0: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_ShockShank_StingerV2_02, ReturnValue6_0, True)
        # Label 1699
        ReturnValue9_0: Ptr[AnimInstance] = self.ShockShank_skl.GetAnimInstance()
        ReturnValue10: float = ReturnValue9_0.Montage_Play(ShockShankStinger_02_Montage, 1, 0, 0, True)
        # End
        # Label 1818
        ReturnValue2 = self.GetInstigatorCharacter()
        ReturnValue2_0 = ReturnValue2.GetMesh1P()
        ReturnValue7_0 = ReturnValue2_0.GetAnimInstance()
        ReturnValue7_1: float = ReturnValue7_0.Montage_Play(ShockShankStinger_02_Montage, 1, 1, 0, True)
        ReturnValue4: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_ShockShank_StingerV2_01, ReturnValue4, True)
        goto('L1699')
        # Label 2080
        ReturnValue_4: bool = self.ShouldShowStinger()
        if not ReturnValue_4:
            goto('L2184')
        ReturnValue1_4: int32 = RandomIntegerInRange(0, 1)
        self.mRandomStingerAnim = ReturnValue1_4
        goto('L708')
        # Label 2184
        ReturnValue3_2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue3_3: Ptr[SkeletalMeshComponent] = ReturnValue3_2.GetMesh1P()
        ReturnValue8_0: Ptr[AnimInstance] = ReturnValue3_3.GetAnimInstance()
        ReturnValue3_4: bool = Default__KismetSystemLibrary.IsValid(ReturnValue8_0)
        if not ReturnValue3_4:
            goto('L5123')
        ReturnValue3_2 = self.GetInstigatorCharacter()
        ReturnValue3_3 = ReturnValue3_2.GetMesh1P()
        ReturnValue8_0 = ReturnValue3_3.GetAnimInstance()
        ReturnValue2_2: bool = ReturnValue8_0.Montage_IsPlaying(ShockShankEquip_01_Montage)
        if not ReturnValue2_2:
            goto('L2527')
        # End
        # Label 2527
        ReturnValue3_2 = self.GetInstigatorCharacter()
        ReturnValue3_3 = ReturnValue3_2.GetMesh1P()
        ReturnValue8_0 = ReturnValue3_3.GetAnimInstance()
        ReturnValue9_1: float = ReturnValue8_0.Montage_Play(ShockShankEquip_01_Montage, 1, 0, 0, True)
        ReturnValue2_3: Ptr[AnimInstance] = self.ShockShank_skl.GetAnimInstance()
        ReturnValue2_4: float = ReturnValue2_3.Montage_Play(ShockShankEquip_01_Montage, 1, 0, 0, True)
        ReturnValue5_0: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_ShockShank_EquipV2, ReturnValue5_0, True)
        # End
        self.WasEquipped()
        ReturnValue7_2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_6: bool = ReturnValue7_2.IsLocallyControlled()
        if not ReturnValue1_6:
            goto('L5123')
        goto('L2080')
        self.PlayStunEffects()
        ReturnValue8_1: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue6_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_EQ_ShockShank_EquipStinger, ReturnValue8_1, True)
        ReturnValue_5: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_6: Ptr[SkeletalMeshComponent] = ReturnValue_5.GetMesh1P()
        ReturnValue5_1: Ptr[AnimInstance] = ReturnValue_6.GetAnimInstance()
        ReturnValue_7: bool = Default__KismetSystemLibrary.IsValid(ReturnValue5_1)
        if not ReturnValue_7:
            goto('L5123')
        ReturnValue_8: int32 = RandomIntegerInRange(0, 50)
        self.mRandomAttackAnim = ReturnValue_8
        ReturnValue_9: bool = self.GetShouldPlaySecondSwing()
        if not ReturnValue_9:
            goto('L4547')
        ReturnValue_10: bool = GreaterEqual_IntInt(self.mRandomAttackAnim, 48)
        if not ReturnValue_10:
            goto('L3976')
        ReturnValue_5 = self.GetInstigatorCharacter()
        ReturnValue_6 = ReturnValue_5.GetMesh1P()
        ReturnValue5_1 = ReturnValue_6.GetAnimInstance()
        ReturnValue4_0: float = ReturnValue5_1.Montage_Play(ShockShankAttack_04_Montage, 1, 0, 0, True)
        ReturnValue2_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_ShockShank_Punch, self, True)
        ReturnValue4_1: Ptr[AnimInstance] = self.ShockShank_skl.GetAnimInstance()
        ReturnValue3_5: float = ReturnValue4_1.Montage_Play(ShockShankAttack_01_Montage, 1, 0, 0, True)
        ReturnValue2_6: Ptr[Pawn] = self.GetInstigator()
        ReturnValue2_7: Ptr[Controller] = ReturnValue2_6.GetController()
        Controller2: Ptr[PlayerController] = Cast[PlayerController](ReturnValue2_7)
        bSuccess2: bool = Controller2
        if not bSuccess2:
            goto('L5123')
        Controller2.ClientPlayCameraAnim(ShockShankAttack_04_CameraAnim, 1, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        # End
        # Label 3976
        ReturnValue_5 = self.GetInstigatorCharacter()
        ReturnValue_6 = ReturnValue_5.GetMesh1P()
        ReturnValue5_1 = ReturnValue_6.GetAnimInstance()
        ReturnValue6_2: float = ReturnValue5_1.Montage_Play(ShockShankAttack_03_Montage, 1, 0, 0, True)
        ReturnValue3_6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_ShockShank_HitRattle, self, True)
        ReturnValue_11: Ptr[AnimInstance] = self.ShockShank_skl.GetAnimInstance()
        ReturnValue_12: float = ReturnValue_11.Montage_Play(ShockShankAttack_01_Montage, 1, 0, 0, True)
        ReturnValue1_7: Ptr[Pawn] = self.GetInstigator()
        ReturnValue1_8: Ptr[Controller] = ReturnValue1_7.GetController()
        Controller1: Ptr[PlayerController] = Cast[PlayerController](ReturnValue1_8)
        bSuccess1: bool = Controller1
        if not bSuccess1:
            goto('L5123')
        Controller1.ClientPlayCameraAnim(ShockShankAttack_03_CamerAnim, 1, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        # End
        # Label 4547
        ReturnValue_5 = self.GetInstigatorCharacter()
        ReturnValue_6 = ReturnValue_5.GetMesh1P()
        ReturnValue5_1 = ReturnValue_6.GetAnimInstance()
        ReturnValue5_2: float = ReturnValue5_1.Montage_Play(ShockShankAttack_01_Montage, 1, 0, 0, True)
        ReturnValue4_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_ShockShank_HitRattle, self, True)
        ReturnValue1_9: Ptr[AnimInstance] = self.ShockShank_skl.GetAnimInstance()
        ReturnValue1_10: float = ReturnValue1_9.Montage_Play(ShockShankAttack_01_Montage, 1, 0, 0, True)
        ReturnValue_13: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_14: Ptr[Controller] = ReturnValue_13.GetController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue_14)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L5123')
        Controller.ClientPlayCameraAnim(ShockShankAttack_01_CameraAnim, 1, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        # End
        goto('L10')
    
