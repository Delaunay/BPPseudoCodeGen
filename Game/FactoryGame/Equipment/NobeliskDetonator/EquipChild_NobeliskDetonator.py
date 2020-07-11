
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import SetVisibility
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Character.Player.Animation.FirstPerson.NobeliskDetonatorLongThrow_01_Montage import NobeliskDetonatorLongThrow_01_Montage
from Game.FactoryGame.Equipment.NobeliskDetonator.EquipChild_NobeliskDetonator import ExecuteUbergraph_EquipChild_NobeliskDetonator.K2Node_Event_character
from Script.Engine import Controller
from Script.FactoryGame import GetInstigatorCharacter
from Game.FactoryGame.Character.Player.Animation.FirstPerson.NobeliskDetonatorThrowCharge_01_Montage import NobeliskDetonatorThrowCharge_01_Montage
from Game.FactoryGame.Equipment.NobeliskDetonator.Animation.NobeliskDetonatorThrow_01_Montage import NobeliskDetonatorThrow_01_Montage
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.Stop_E_Nobelisk_StopEquips import Stop_E_Nobelisk_StopEquips
from Script.Engine import GetAnimInstance
from Script.Engine import PlayerController
from Script.FactoryGame import FGNobeliskDetonator
from Game.FactoryGame.Character.Player.Animation.FirstPerson.NobeliskDetonatorShortThrow_01_Montage import NobeliskDetonatorShortThrow_01_Montage
from Game.FactoryGame.Character.Player.CameraShake.NobeliskLongThrow_01_CameraAnim import NobeliskLongThrow_01_CameraAnim
from Game.FactoryGame.Equipment.NobeliskDetonator.Animation.NobeliskDetonatorReload_01_Montage import NobeliskDetonatorReload_01_Montage
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.Play_E_Nobelisk_Release import Play_E_Nobelisk_Release
from Script.FactoryGame import IsLocalInstigator
from Script.Engine import InRange_FloatFloat
from Game.FactoryGame.Character.Player.Animation.FirstPerson.NobeliskDetonatorMiddleThrow_01_Montage import NobeliskDetonatorMiddleThrow_01_Montage
from Script.FactoryGame import GetMesh1P
from Script.FactoryGame import GetChargePct
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.Play_E_Nobelisk_Throw import Play_E_Nobelisk_Throw
from Script.FactoryGame import FGWeaponChild
from Script.FactoryGame import FGWeapon
from Game.FactoryGame.Equipment.NobeliskDetonator.EquipChild_NobeliskDetonator import ExecuteUbergraph_EquipChild_NobeliskDetonator
from Script.Engine import Montage_Play
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import GetInstigatorController
from Game.FactoryGame.Equipment.NobeliskDetonator.Animation.NobeliskDetonatorEquipExplosive_01_Montage import NobeliskDetonatorEquipExplosive_01_Montage
from Script.Engine import Actor
from Script.Engine import GetOwner
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.Engine import SkeletalMeshComponent

class EquipChild_NobeliskDetonator(FGWeaponChild):
    mAttachSocket = hand_rSocket
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def NotifyReloadComplete(self):
        self.ExecuteUbergraph_EquipChild_NobeliskDetonator(10)
    

    def NotifyEndPrimaryFire(self):
        self.ExecuteUbergraph_EquipChild_NobeliskDetonator(3931)
    

    def NotifyReloading(self):
        self.ExecuteUbergraph_EquipChild_NobeliskDetonator(15)
    

    def NotifyBeginPrimaryFire(self):
        self.ExecuteUbergraph_EquipChild_NobeliskDetonator(336)
    

    def OnEquip(self):
        ExecuteUbergraph_EquipChild_NobeliskDetonator.K2Node_Event_character = Character #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_EquipChild_NobeliskDetonator(3714)
    

    def NotifyPrimaryFireExecuted(self):
        self.ExecuteUbergraph_EquipChild_NobeliskDetonator(3775)
    

    def ExecuteUbergraph_EquipChild_NobeliskDetonator(self):
        # End
        ReturnValue2: bool = self.mParentEquipment.IsLocalInstigator()
        if not ReturnValue2:
            goto('L3936')
        self.Explosive_skel.SetVisibility(True, True)
        ReturnValue6: Ptr[AnimInstance] = self.Explosive_skel.GetAnimInstance()
        ReturnValue6_0: bool = ReturnValue6.Montage_IsPlaying(NobeliskDetonatorReload_01_Montage)
        if not ReturnValue6_0:
            goto('L217')
        # End
        # Label 217
        ReturnValue6 = self.Explosive_skel.GetAnimInstance()
        ReturnValue6_1: float = ReturnValue6.Montage_Play(NobeliskDetonatorReload_01_Montage, 1, 0, 0, True)
        # End
        ReturnValue3: bool = self.mParentEquipment.IsLocalInstigator()
        if not ReturnValue3:
            goto('L3936')
        ReturnValue: Ptr[Actor] = self.GetOwner()
        AsFGWeapon: Ptr[FGWeapon] = Cast[FGWeapon](ReturnValue)
        bSuccess: bool = AsFGWeapon
        if not bSuccess:
            goto('L3936')
        ReturnValue_0: Ptr[FGCharacterPlayer] = AsFGWeapon.GetInstigatorCharacter()
        ReturnValue_1: Ptr[SkeletalMeshComponent] = ReturnValue_0.GetMesh1P()
        ReturnValue_2: Ptr[AnimInstance] = ReturnValue_1.GetAnimInstance()
        ReturnValue_3: bool = ReturnValue_2.Montage_IsPlaying(NobeliskDetonatorThrowCharge_01_Montage)
        if not ReturnValue_3:
            goto('L687')
        # End
        # Label 687
        ReturnValue_0 = AsFGWeapon.GetInstigatorCharacter()
        ReturnValue_1 = ReturnValue_0.GetMesh1P()
        ReturnValue_2 = ReturnValue_1.GetAnimInstance()
        ReturnValue_4: float = ReturnValue_2.Montage_Play(NobeliskDetonatorThrowCharge_01_Montage, 1, 1, 0, True)
        ReturnValue_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Nobelisk_Throw, self, True)
        ReturnValue2_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_Nobelisk_StopEquips, self.mParentEquipment, True)
        # End
        # Label 1004
        ReturnValue1: Ptr[Actor] = self.GetOwner()
        AsFGWeapon1: Ptr[FGWeapon] = Cast[FGWeapon](ReturnValue1)
        bSuccess1: bool = AsFGWeapon1
        if not bSuccess1:
            goto('L3936')
        ReturnValue1_0: Ptr[FGCharacterPlayer] = AsFGWeapon1.GetInstigatorCharacter()
        ReturnValue1_1: Ptr[SkeletalMeshComponent] = ReturnValue1_0.GetMesh1P()
        ReturnValue1_2: Ptr[AnimInstance] = ReturnValue1_1.GetAnimInstance()
        ReturnValue1_3: bool = ReturnValue1_2.Montage_IsPlaying(NobeliskDetonatorLongThrow_01_Montage)
        if not ReturnValue1_3:
            goto('L1299')
        # End
        # Label 1299
        ReturnValue1_0 = AsFGWeapon1.GetInstigatorCharacter()
        ReturnValue1_1 = ReturnValue1_0.GetMesh1P()
        ReturnValue1_2 = ReturnValue1_1.GetAnimInstance()
        ReturnValue1_4: float = ReturnValue1_2.Montage_Play(NobeliskDetonatorLongThrow_01_Montage, 1, 1, 0, True)
        ReturnValue1_0 = AsFGWeapon1.GetInstigatorCharacter()
        ReturnValue_6: Ptr[Controller] = ReturnValue1_0.GetInstigatorController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue_6)
        bSuccess2: bool = Controller
        if not bSuccess2:
            goto('L3936')
        Controller.ClientPlayCameraAnim(NobeliskLongThrow_01_CameraAnim, 2, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        # Label 1742
        ReturnValue5: Ptr[AnimInstance] = self.Explosive_skel.GetAnimInstance()
        ReturnValue5_0: bool = ReturnValue5.Montage_IsPlaying(NobeliskDetonatorThrow_01_Montage)
        if not ReturnValue5_0:
            goto('L1854')
        # End
        # Label 1854
        ReturnValue5 = self.Explosive_skel.GetAnimInstance()
        ReturnValue5_1: float = ReturnValue5.Montage_Play(NobeliskDetonatorThrow_01_Montage, 1, 0, 0, True)
        ReturnValue1_5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Nobelisk_Release, self, True)
        # End
        # Label 2026
        ReturnValue2_1: Ptr[Actor] = self.GetOwner()
        Detonator: Ptr[FGNobeliskDetonator] = Cast[FGNobeliskDetonator](ReturnValue2_1)
        bSuccess3: bool = Detonator
        if not bSuccess3:
            goto('L3936')
        ReturnValue_7: float = Detonator.GetChargePct()
        ReturnValue2_2: bool = InRange_FloatFloat(ReturnValue_7, 0, 0.30000001192092896, True, True)
        if not ReturnValue2_2:
            goto('L2525')
        ReturnValue4: Ptr[Actor] = self.GetOwner()
        AsFGWeapon3: Ptr[FGWeapon] = Cast[FGWeapon](ReturnValue4)
        bSuccess5: bool = AsFGWeapon3
        if not bSuccess5:
            goto('L3936')
        ReturnValue3_0: Ptr[FGCharacterPlayer] = AsFGWeapon3.GetInstigatorCharacter()
        ReturnValue3_1: Ptr[SkeletalMeshComponent] = ReturnValue3_0.GetMesh1P()
        ReturnValue4_0: Ptr[AnimInstance] = ReturnValue3_1.GetAnimInstance()
        ReturnValue3_2: bool = ReturnValue4_0.Montage_IsPlaying(NobeliskDetonatorShortThrow_01_Montage)
        if not ReturnValue3_2:
            goto('L3035')
        # End
        # Label 2525
        ReturnValue_7 = Detonator.GetChargePct()
        ReturnValue1_6: bool = InRange_FloatFloat(ReturnValue_7, 0.30000001192092896, 0.800000011920929, True, True)
        if not ReturnValue1_6:
            goto('L2925')
        ReturnValue3_3: Ptr[Actor] = self.GetOwner()
        AsFGWeapon2: Ptr[FGWeapon] = Cast[FGWeapon](ReturnValue3_3)
        bSuccess4: bool = AsFGWeapon2
        if not bSuccess4:
            goto('L3936')
        ReturnValue2_3: Ptr[FGCharacterPlayer] = AsFGWeapon2.GetInstigatorCharacter()
        ReturnValue2_4: Ptr[SkeletalMeshComponent] = ReturnValue2_3.GetMesh1P()
        ReturnValue3_4: Ptr[AnimInstance] = ReturnValue2_4.GetAnimInstance()
        ReturnValue4_1: bool = ReturnValue3_4.Montage_IsPlaying(NobeliskDetonatorMiddleThrow_01_Montage)
        if not ReturnValue4_1:
            goto('L3238')
        # End
        # Label 2925
        ReturnValue_7 = Detonator.GetChargePct()
        ReturnValue_8: bool = InRange_FloatFloat(ReturnValue_7, 0.800000011920929, 1, True, True)
        if not ReturnValue_8:
            goto('L3936')
        goto('L1004')
        # Label 3035
        ReturnValue3_0 = AsFGWeapon3.GetInstigatorCharacter()
        ReturnValue3_1 = ReturnValue3_0.GetMesh1P()
        ReturnValue4_0 = ReturnValue3_1.GetAnimInstance()
        ReturnValue4_2: float = ReturnValue4_0.Montage_Play(NobeliskDetonatorShortThrow_01_Montage, 1, 1, 0, True)
        goto('L1742')
        # Label 3238
        ReturnValue2_3 = AsFGWeapon2.GetInstigatorCharacter()
        ReturnValue2_4 = ReturnValue2_3.GetMesh1P()
        ReturnValue3_4 = ReturnValue2_4.GetAnimInstance()
        ReturnValue3_5: float = ReturnValue3_4.Montage_Play(NobeliskDetonatorMiddleThrow_01_Montage, 1, 1, 0, True)
        goto('L1742')
        # Label 3441
        ReturnValue2_5: Ptr[AnimInstance] = self.Explosive_skel.GetAnimInstance()
        ReturnValue2_6: float = ReturnValue2_5.Montage_Play(NobeliskDetonatorEquipExplosive_01_Montage, 1, 0, 0, True)
        # End
        # Label 3560
        self.Explosive_skel.SetVisibility(self.mIsLoaded, True)
        ReturnValue2_5 = self.Explosive_skel.GetAnimInstance()
        ReturnValue2_7: bool = ReturnValue2_5.Montage_IsPlaying(NobeliskDetonatorEquipExplosive_01_Montage)
        if not ReturnValue2_7:
            goto('L3441')
        # End
        ReturnValue4_3: bool = self.mParentEquipment.IsLocalInstigator()
        if not ReturnValue4_3:
            goto('L3936')
        goto('L3560')
        ReturnValue_9: bool = self.mParentEquipment.IsLocalInstigator()
        if not ReturnValue_9:
            goto('L3936')
        self.Explosive_skel.SetVisibility(False, True)
        # End
        # Label 3870
        ReturnValue1_7: bool = self.mParentEquipment.IsLocalInstigator()
        if not ReturnValue1_7:
            goto('L3936')
        goto('L2026')
        goto('L3870')
    
