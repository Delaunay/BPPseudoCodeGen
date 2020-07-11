
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import SetVisibility
from Script.FactoryGame import FGNobeliskExplosiveAttachment
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Equipment.NobeliskDetonator.Attach_NobeliskDetonator_R import ExecuteUbergraph_Attach_NobeliskDetonator_R.K2Node_Event_location
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Equipment.NobeliskDetonator.Animation.NobeliskDetonatorReload_01_Montage import NobeliskDetonatorReload_01_Montage
from Script.FactoryGame import OnAttach
from Script.Engine import IsValid
from Script.FactoryGame import ClientPlayReloadEffect
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.3P.Play_E_Nobelisk_ThrowCharge_3P import Play_E_Nobelisk_ThrowCharge_3P
from Script.Engine import Montage_Play
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.NobeliskDetonator.Attach_NobeliskDetonator_R import ExecuteUbergraph_Attach_NobeliskDetonator_R.K2Node_Event_flashLocation
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.3P.Play_E_Nobelisk_Reload_3P import Play_E_Nobelisk_Reload_3P
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.3P.Play_E_Nobelisk_ThrowRelease_3P import Play_E_Nobelisk_ThrowRelease_3P
from Script.FactoryGame import GetAttachedTo
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.NobeliskDetonatorMiddleThrow_01_Montage import NobeliskDetonatorMiddleThrow_01_Montage
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Game.FactoryGame.Equipment.NobeliskDetonator.Attach_NobeliskDetonator_R import ExecuteUbergraph_Attach_NobeliskDetonator_R
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.NobeliskDetonatorThrowCharge_01_Montage import NobeliskDetonatorThrowCharge_01_Montage

class Attach_NobeliskDetonator_R(FGNobeliskExplosiveAttachment):
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_Nobelisk
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def OnIsLoadedSet(self):
        self.ExecuteUbergraph_Attach_NobeliskDetonator_R(865)
    

    def PlayFireEffect(self):
        ExecuteUbergraph_Attach_NobeliskDetonator_R.K2Node_Event_flashLocation = flashLocation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Attach_NobeliskDetonator_R(912)
    

    def OnBeginFireEffect(self):
        ExecuteUbergraph_Attach_NobeliskDetonator_R.K2Node_Event_location = Location #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Attach_NobeliskDetonator_R(985)
    

    def ClientPlayReloadEffect(self):
        self.ExecuteUbergraph_Attach_NobeliskDetonator_R(1486)
    

    def OnAttach(self):
        self.ExecuteUbergraph_Attach_NobeliskDetonator_R(1491)
    

    def ExecuteUbergraph_Attach_NobeliskDetonator_R(self):
        # Label 10
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Nobelisk_ThrowRelease_3P, self, True)
        # End
        # Label 68
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.NobeliskExplosive_Skl_01)
        if not ReturnValue_0:
            goto('L1543')
        ReturnValue_1: Ptr[AnimInstance] = self.NobeliskExplosive_Skl_01.GetAnimInstance()
        ReturnValue_2: bool = ReturnValue_1.Montage_IsPlaying(NobeliskDetonatorReload_01_Montage)
        if not ReturnValue_2:
            goto('L245')
        # End
        # Label 245
        ReturnValue_1 = self.NobeliskExplosive_Skl_01.GetAnimInstance()
        ReturnValue_3: float = ReturnValue_1.Montage_Play(NobeliskDetonatorReload_01_Montage, 1, 0, 0, True)
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Nobelisk_Reload_3P, self, True)
        # End
        # Label 417
        ReturnValue_4: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_4)
        if not ReturnValue1_0:
            goto('L1543')
        ReturnValue_4 = self.GetAttachedTo()
        ReturnValue_5: Ptr[SkeletalMeshComponent] = ReturnValue_4.GetMesh3P()
        ReturnValue1_1: Ptr[AnimInstance] = ReturnValue_5.GetAnimInstance()
        ReturnValue1_2: bool = ReturnValue1_1.Montage_IsPlaying(NobeliskDetonatorMiddleThrow_01_Montage)
        if not ReturnValue1_2:
            goto('L680')
        # End
        # Label 680
        ReturnValue_4 = self.GetAttachedTo()
        ReturnValue_5 = ReturnValue_4.GetMesh3P()
        ReturnValue1_1 = ReturnValue_5.GetAnimInstance()
        ReturnValue1_3: float = ReturnValue1_1.Montage_Play(NobeliskDetonatorMiddleThrow_01_Montage, 1, 0, 0, True)
        goto('L10')
        self.NobeliskExplosive_Skl_01.SetVisibility(self.mIsLoaded, True)
        # End
        goto('L417')
        # Label 917
        self.ClientPlayReloadEffect()
        self.mIsLoaded = True
        self.NobeliskExplosive_Skl_01.SetVisibility(self.mIsLoaded, True)
        goto('L68')
        ReturnValue1_4: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_4)
        if not ReturnValue2:
            goto('L1543')
        ReturnValue1_4 = self.GetAttachedTo()
        ReturnValue1_5: Ptr[SkeletalMeshComponent] = ReturnValue1_4.GetMesh3P()
        ReturnValue2_0: Ptr[AnimInstance] = ReturnValue1_5.GetAnimInstance()
        ReturnValue2_1: bool = ReturnValue2_0.Montage_IsPlaying(NobeliskDetonatorMiddleThrow_01_Montage)
        if not ReturnValue2_1:
            goto('L1248')
        # End
        # Label 1248
        ReturnValue1_4 = self.GetAttachedTo()
        ReturnValue1_5 = ReturnValue1_4.GetMesh3P()
        ReturnValue2_0 = ReturnValue1_5.GetAnimInstance()
        ReturnValue2_2: float = ReturnValue2_0.Montage_Play(NobeliskDetonatorThrowCharge_01_Montage, 1, 0, 0, True)
        ReturnValue2_3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Nobelisk_ThrowCharge_3P, self, True)
        # End
        goto('L917')
        self.OnAttach()
        self.NobeliskExplosive_Skl_01.SetVisibility(self.mIsLoaded, True)
    
