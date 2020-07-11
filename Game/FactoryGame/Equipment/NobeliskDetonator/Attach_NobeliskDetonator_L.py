
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.NobeliskDetonatorReload_01_Montage import NobeliskDetonatorReload_01_Montage
from Script.FactoryGame import FGNobeliskDetonatorAttachment
from Game.FactoryGame.Equipment.NobeliskDetonator.Attach_NobeliskDetonator_L import ExecuteUbergraph_Attach_NobeliskDetonator_L
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Equipment.NobeliskDetonator.Animation.NobeliskDetonatorReload_01_Montage import NobeliskDetonatorReload_01_Montage
from Script.FactoryGame import PlayAttachEffects3P
from Script.FactoryGame import ClientPlayReloadEffect
from Game.FactoryGame.Equipment.NobeliskDetonator.Attach_NobeliskDetonator_L import ExecuteUbergraph_Attach_NobeliskDetonator_L.K2Node_Event_flashLocation
from Game.FactoryGame.Equipment.NobeliskDetonator.Animation.NobeliskDetonatorEquip_01_Montage import NobeliskDetonatorEquip_01_Montage
from Script.Engine import Montage_Play
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.3P.Play_E_Nobelisk_Reload_3P import Play_E_Nobelisk_Reload_3P
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.NobeliskDetonatorEquip_01_Montage import NobeliskDetonatorEquip_01_Montage
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.NobeliskDetonatorDetonateNoexpl_01_Montage import NobeliskDetonatorDetonateNoexpl_01_Montage
from Script.FactoryGame import GetAttachedTo
from Game.FactoryGame.Equipment.NobeliskDetonator.Audio.3P.Play_E_Nobelisk_Trigger_3P import Play_E_Nobelisk_Trigger_3P
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Game.FactoryGame.Character.Player.Animation.ThirdPerson.NobeliskDetonatorDetonate_01_Montage import NobeliskDetonatorDetonate_01_Montage
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Equipment.NobeliskDetonator.Animation.NobeliskDetonatorDetonate_02_Montage import NobeliskDetonatorDetonate_02_Montage

class Attach_NobeliskDetonator_L(FGNobeliskDetonatorAttachment):
    mAttachSocket = hand_lSocket
    mArmAnimation = EArmEquipment::AE_Nobelisk
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def ClientPlayReloadEffect(self):
        self.ExecuteUbergraph_Attach_NobeliskDetonator_L(15)
    

    def PlayFireEffect(self):
        ExecuteUbergraph_Attach_NobeliskDetonator_L.K2Node_Event_flashLocation = flashLocation #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Attach_NobeliskDetonator_L(2485)
    

    def PlayAttachEffects3P(self):
        self.ExecuteUbergraph_Attach_NobeliskDetonator_L(2504)
    

    def ExecuteUbergraph_Attach_NobeliskDetonator_L(self):
        goto(ComputedJump("EntryPoint"))
        self.ClientPlayReloadEffect()
        self.mIsLoaded = True
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue_0: Ptr[SkeletalMeshComponent] = ReturnValue.GetMesh3P()
        ReturnValue2: Ptr[AnimInstance] = ReturnValue_0.GetAnimInstance()
        ReturnValue2_0: bool = ReturnValue2.Montage_IsPlaying(NobeliskDetonatorReload_01_Montage)
        if not ReturnValue2_0:
            goto('L210')
        goto(ExecutionFlow.Pop())
        # Label 210
        ReturnValue = self.GetAttachedTo()
        ReturnValue_0 = ReturnValue.GetMesh3P()
        ReturnValue2 = ReturnValue_0.GetAnimInstance()
        ReturnValue2_1: float = ReturnValue2.Montage_Play(NobeliskDetonatorReload_01_Montage, 1, 0, 0, True)
        ReturnValue1: Ptr[AnimInstance] = self.Detonator_skel.GetAnimInstance()
        ReturnValue_1: bool = ReturnValue1.Montage_IsPlaying(NobeliskDetonatorReload_01_Montage)
        if not ReturnValue_1:
            goto('L498')
        goto(ExecutionFlow.Pop())
        # Label 498
        ReturnValue1 = self.Detonator_skel.GetAnimInstance()
        ReturnValue1_0: float = ReturnValue1.Montage_Play(NobeliskDetonatorReload_01_Montage, 1, 0, 0, True)
        # Label 612
        ReturnValue_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Nobelisk_Reload_3P, self, True)
        goto(ExecutionFlow.Pop())
        # Label 666
        ReturnValue_3: Ptr[AnimInstance] = self.Detonator_skel.GetAnimInstance()
        ReturnValue_4: float = ReturnValue_3.Montage_Play(NobeliskDetonatorEquip_01_Montage, 1, 0, 0, True)
        goto('L612')
        # Label 785
        ReturnValue_3 = self.Detonator_skel.GetAnimInstance()
        ReturnValue1_1: bool = ReturnValue_3.Montage_IsPlaying(NobeliskDetonatorEquip_01_Montage)
        if not ReturnValue1_1:
            goto('L666')
        goto(ExecutionFlow.Pop())
        # Label 893
        self.PlayAttachEffects3P()
        ReturnValue1_2: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue1_3: Ptr[SkeletalMeshComponent] = ReturnValue1_2.GetMesh3P()
        ReturnValue4: Ptr[AnimInstance] = ReturnValue1_3.GetAnimInstance()
        ReturnValue3: bool = ReturnValue4.Montage_IsPlaying(NobeliskDetonatorEquip_01_Montage)
        if not ReturnValue3:
            goto('L1077')
        goto(ExecutionFlow.Pop())
        # Label 1077
        ReturnValue1_2 = self.GetAttachedTo()
        ReturnValue1_3 = ReturnValue1_2.GetMesh3P()
        ReturnValue4 = ReturnValue1_3.GetAnimInstance()
        ReturnValue4_0: float = ReturnValue4.Montage_Play(NobeliskDetonatorEquip_01_Montage, 1, 0, 0, True)
        goto('L785')
        # Label 1262
        ExecutionFlow.Push("L1441")
        ReturnValue2_2: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue2_3: Ptr[SkeletalMeshComponent] = ReturnValue2_2.GetMesh3P()
        ReturnValue6: Ptr[AnimInstance] = ReturnValue2_3.GetAnimInstance()
        ReturnValue6_0: bool = ReturnValue6.Montage_IsPlaying(NobeliskDetonatorDetonate_01_Montage)
        if not ReturnValue6_0:
            goto('L1664')
        goto(ExecutionFlow.Pop())
        # Label 1441
        ReturnValue3_0: Ptr[AnimInstance] = self.Detonator_skel.GetAnimInstance()
        ReturnValue4_1: bool = ReturnValue3_0.Montage_IsPlaying(NobeliskDetonatorDetonate_02_Montage)
        if not ReturnValue4_1:
            goto('L1549')
        goto(ExecutionFlow.Pop())
        # Label 1549
        ReturnValue3_0 = self.Detonator_skel.GetAnimInstance()
        ReturnValue3_1: float = ReturnValue3_0.Montage_Play(NobeliskDetonatorDetonate_02_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 1664
        ReturnValue2_2 = self.GetAttachedTo()
        ReturnValue2_3 = ReturnValue2_2.GetMesh3P()
        ReturnValue6 = ReturnValue2_3.GetAnimInstance()
        ReturnValue6_1: float = ReturnValue6.Montage_Play(NobeliskDetonatorDetonate_01_Montage, 1, 1, 0, True)
        # Label 1844
        ReturnValue1_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_Nobelisk_Trigger_3P, self, True)
        goto(ExecutionFlow.Pop())
        # Label 1898
        ExecutionFlow.Push("L2262")
        ReturnValue3_2: Ptr[FGCharacterPlayer] = self.GetAttachedTo()
        ReturnValue3_3: Ptr[SkeletalMeshComponent] = ReturnValue3_2.GetMesh3P()
        ReturnValue7: Ptr[AnimInstance] = ReturnValue3_3.GetAnimInstance()
        ReturnValue7_0: bool = ReturnValue7.Montage_IsPlaying(NobeliskDetonatorDetonateNoexpl_01_Montage)
        if not ReturnValue7_0:
            goto('L2077')
        goto(ExecutionFlow.Pop())
        # Label 2077
        ReturnValue3_2 = self.GetAttachedTo()
        ReturnValue3_3 = ReturnValue3_2.GetMesh3P()
        ReturnValue7 = ReturnValue3_3.GetAnimInstance()
        ReturnValue7_1: float = ReturnValue7.Montage_Play(NobeliskDetonatorDetonateNoexpl_01_Montage, 1, 1, 0.10000000149011612, True)
        goto('L1844')
        # Label 2262
        ReturnValue5: Ptr[AnimInstance] = self.Detonator_skel.GetAnimInstance()
        ReturnValue5_0: bool = ReturnValue5.Montage_IsPlaying(NobeliskDetonatorDetonate_02_Montage)
        if not ReturnValue5_0:
            goto('L2370')
        goto(ExecutionFlow.Pop())
        # Label 2370
        ReturnValue5 = self.Detonator_skel.GetAnimInstance()
        ReturnValue5_1: float = ReturnValue5.Montage_Play(NobeliskDetonatorDetonate_02_Montage, 1, 0, 0.10000000149011612, True)
        goto(ExecutionFlow.Pop())
        if not self.mIsLoaded:
            goto('L1898')
        goto('L1262')
        goto('L893')
    
