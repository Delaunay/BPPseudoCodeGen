
from codegen.ue4_stub import *

from Script.Engine import Delay
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Script.Engine import GetDisplayName
from Script.FactoryGame import GetInstigatorCharacter
from Game.FactoryGame.Character.Player.Animation.FirstPerson.OneHandEquipmentEquip_01_Montage import OneHandEquipmentEquip_01_Montage
from Script.Engine import Pawn
from Script.FactoryGame import WasEquipped
from Game.FactoryGame.Equipment.Medkit.MedkitAnimationData import MedkitAnimationData
from Script.FactoryGame import WasUnEquipped
from Script.Engine import GetInstigator
from Game.FactoryGame.Equipment.Medkit.Animation.MedkitUse_02_Montage import MedkitUse_02_Montage
from Script.Engine import LatentActionInfo
from Script.FactoryGame import FGConsumableEquipment
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Script.Engine import PlayerController
from Script.Engine import GetController
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import PlayConsumeEffects
from Game.FactoryGame.Equipment.Medkit.Equip_MedKit import ExecuteUbergraph_Equip_MedKit
from Script.Engine import GetCurrentActiveMontage
from Script.FactoryGame import IsLocalInstigator
from Script.FactoryGame import OnPrimaryFire
from Script.Engine import Montage_Stop
from Script.FactoryGame import GetMesh1P
from Game.FactoryGame.Equipment.Medkit.Equip_MedKit import ExecuteUbergraph_Equip_MedKit.K2Node_Event_consumable
from Script.Engine import AnimMontage
from Script.Engine import Montage_Play
from Script.Engine import RandomIntegerInRange
from Script.Engine import Min
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.Engine import SkeletalMeshComponent
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class Equip_MedKit(FGConsumableEquipment):
    mRandomAnim: int32
    mCanPress: bool
    mAnimData: List[MedkitAnimationData] = [{'Montage_7_2E66F6A948A8606E71185682EA2AC4EC': {'$AssetPath': '/Game/FactoryGame/Character/Player/Animation/FirstPerson/MedkitUse_01_Montage.MedkitUse_01_Montage'}, 'CameraAnim_8_AA01C2B248FF438D6C2816B2FA94F1BD': {'$AssetPath': '/Game/FactoryGame/Character/Player/CameraShake/MedkitUse_01_CameraAnim.MedkitUse_01_CameraAnim'}}, {'Montage_7_2E66F6A948A8606E71185682EA2AC4EC': {'$AssetPath': '/Game/FactoryGame/Character/Player/Animation/FirstPerson/MedkitUse_02_Montage.MedkitUse_02_Montage'}, 'CameraAnim_8_AA01C2B248FF438D6C2816B2FA94F1BD': {'$AssetPath': '/Game/FactoryGame/Character/Player/CameraShake/MedkitUse_02_CameraAnim.MedkitUse_02_CameraAnim'}}, {'Montage_7_2E66F6A948A8606E71185682EA2AC4EC': {'$AssetPath': '/Game/FactoryGame/Character/Player/Animation/FirstPerson/MedkitUse_03_Montage.MedkitUse_03_Montage'}, 'CameraAnim_8_AA01C2B248FF438D6C2816B2FA94F1BD': {'$AssetPath': '/Game/FactoryGame/Character/Player/CameraShake/MedkitUse_03_CameraAnim.MedkitUse_03_CameraAnim'}}]
    mCurrentAnimData: MedkitAnimationData
    mAttachmentClass = NewObject[Attach_MedKit]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_OneHandEquipment
    mIdlePoseAnimation3p = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Animation/ThirdPerson/MedkitIdle_01.MedkitIdle_01')
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    
    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_MedKit(1460)
    

    def PlayConsumeEffects(self):
        ExecuteUbergraph_Equip_MedKit.K2Node_Event_consumable = consumable #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_MedKit(1808)
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_Equip_MedKit(1853)
    

    def ExecuteUbergraph_Equip_MedKit(self):
        goto(ComputedJump("EntryPoint"))
        self.OnPrimaryFire()
        self.mCanPress = True
        ReturnValue3: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue2: Ptr[SkeletalMeshComponent] = ReturnValue3.GetMesh1P()
        ReturnValue3_0: Ptr[AnimInstance] = ReturnValue2.GetAnimInstance()
        ReturnValue1: float = ReturnValue3_0.Montage_Play(OneHandEquipmentEquip_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 213
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_0: FString = Default__KismetSystemLibrary.GetDisplayName(ReturnValue)
        Default__KismetSystemLibrary.PrintString(self, ReturnValue_0, True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        self.mCanPress = True
        ReturnValue2_0: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_0: Ptr[SkeletalMeshComponent] = ReturnValue2_0.GetMesh1P()
        ReturnValue2_1: Ptr[AnimInstance] = ReturnValue1_0.GetAnimInstance()
        ReturnValue1_1: bool = ReturnValue2_1.Montage_IsPlaying(OneHandEquipmentEquip_01_Montage)
        if not ReturnValue1_1:
            goto('L556')
        goto(ExecutionFlow.Pop())
        # Label 556
        ReturnValue2_0 = self.GetInstigatorCharacter()
        ReturnValue1_0 = ReturnValue2_0.GetMesh1P()
        ReturnValue2_1 = ReturnValue1_0.GetAnimInstance()
        ReturnValue2_2: float = ReturnValue2_1.Montage_Play(OneHandEquipmentEquip_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 733
        ReturnValue_1: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_2: Ptr[Controller] = ReturnValue_1.GetController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Controller.ClientPlayCameraAnim(self.mCurrentAnimData.CameraAnim_8_AA01C2B248FF438D6C2816B2FA94F1BD, 1, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        Default__KismetSystemLibrary.Delay(self, ReturnValue3_1, LatentActionInfo(Linkage = 15, UUID = -1892485871, ExecutionFunction = "ExecuteUbergraph_Equip_MedKit", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1042
        ExecutionFlow.Push("L1237")
        ReturnValue1_2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_3: Ptr[SkeletalMeshComponent] = ReturnValue1_2.GetMesh1P()
        ReturnValue1_3: Ptr[AnimInstance] = ReturnValue_3.GetAnimInstance()
        ReturnValue3_1: float = ReturnValue1_3.Montage_Play(self.mCurrentAnimData.Montage_7_2E66F6A948A8606E71185682EA2AC4EC, 1, 0, 0, True)
        goto('L733')
        # Label 1237
        ReturnValue_4: Ptr[AnimInstance] = self.Medkit_skl.GetAnimInstance()
        ReturnValue_5: bool = ReturnValue_4.Montage_IsPlaying(MedkitUse_02_Montage)
        if not ReturnValue_5:
            goto('L1345')
        goto(ExecutionFlow.Pop())
        # Label 1345
        ReturnValue_4 = self.Medkit_skl.GetAnimInstance()
        ReturnValue_6: float = ReturnValue_4.Montage_Play(MedkitUse_02_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        self.WasEquipped()
        ReturnValue_7: bool = self.IsLocalInstigator()
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        goto('L213')
        # Label 1505
        ReturnValue_8: int32 = RandomIntegerInRange(0, 2)
        self.mRandomAnim = ReturnValue_8
        
        ReturnValue_9: int32 = len(self.mAnimData)
        ReturnValue_10: int32 = ReturnValue_9 - 1
        ReturnValue_11: int32 = Min(self.mRandomAnim, ReturnValue_10)
        
        Item = None
        Item = self.mAnimData[ReturnValue_11]
        self.mCurrentAnimData = Item
        goto('L1042')
        self.PlayConsumeEffects(consumable)
        if not self.mCanPress:
           goto(ExecutionFlow.Pop())
        self.mCanPress = False
        goto('L1505')
        self.WasUnEquipped()
        ReturnValue4: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue3_2: Ptr[SkeletalMeshComponent] = ReturnValue4.GetMesh1P()
        ReturnValue4_0: Ptr[AnimInstance] = ReturnValue3_2.GetAnimInstance()
        ReturnValue_12: Ptr[AnimMontage] = ReturnValue4_0.GetCurrentActiveMontage()
        ReturnValue4_0.Montage_Stop(0, ReturnValue_12)
        goto(ExecutionFlow.Pop())
    
