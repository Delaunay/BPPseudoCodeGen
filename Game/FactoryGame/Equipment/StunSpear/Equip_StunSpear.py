
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.Engine import Delay
from Game.FactoryGame.Character.Player.CameraShake.StunSpearStinger_01_CamerAnim import StunSpearStinger_01_CamerAnim
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Script.Engine import EqualEqual_ByteByte
from Game.FactoryGame.Equipment.StunSpear.Audio.Stop_E_ShockBaton_All import Stop_E_ShockBaton_All
from Script.FactoryGame import GetInstigatorCharacter
from Script.Engine import Pawn
from Script.FactoryGame import WasEquipped
from Game.FactoryGame.Character.Player.CameraShake.StunSpearAttackLeft_CamerAnim import StunSpearAttackLeft_CamerAnim
from Script.Engine import GreaterEqual_IntInt
from Game.FactoryGame.Equipment.StunSpear.Equip_StunSpear import ExecuteUbergraph_Equip_StunSpear.K2Node_ComponentBoundEvent_SweepResult
from Script.Engine import GetInstigator
from Game.FactoryGame.Character.Player.Animation.FirstPerson.StunSpearStinger_01_Montage import StunSpearStinger_01_Montage
from Script.FactoryGame import WasUnEquipped
from Game.FactoryGame.Equipment.StunSpear.Audio.Play_T_ShockBaton_Attack import Play_T_ShockBaton_Attack
from Game.FactoryGame.Equipment.StunSpear.Audio.Play_E_ShockBaton_Equip_03 import Play_E_ShockBaton_Equip_03
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Equipment.StunSpear.Equip_StunSpear import ExecuteUbergraph_Equip_StunSpear
from Game.FactoryGame.Character.Player.Animation.FirstPerson.StunSpearAttack_Right_02_Montage import StunSpearAttack_Right_02_Montage
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import GetAnimInstance
from Game.FactoryGame.Character.Player.Animation.FirstPerson.StunSpearAttack_Montage import StunSpearAttack_Montage
from Script.Engine import PlayerController
from Script.Engine import GetController
from Game.FactoryGame.Equipment.StunSpear.Audio.Play_E_ShockBaton_Equip_02 import Play_E_ShockBaton_Equip_02
from Script.Engine import Montage_JumpToSection
from Game.FactoryGame.Equipment.StunSpear.Audio.Play_E_ShockBaton_Equip_01 import Play_E_ShockBaton_Equip_01
from Script.Engine import GetCurrentActiveMontage
from Game.FactoryGame.Equipment.StunSpear.Audio.Play_E_ShockBaton_Stinger import Play_E_ShockBaton_Stinger
from Script.Engine import Montage_Stop
from Script.FactoryGame import GetMesh1P
from Game.FactoryGame.Character.Player.CameraShake.ShockShankHit_01_CameraAnim import ShockShankHit_01_CameraAnim
from Game.FactoryGame.Equipment.StunSpear.Equip_StunSpear import ExecuteUbergraph_Equip_StunSpear.K2Node_ComponentBoundEvent_bFromSweep
from Game.FactoryGame.Character.Player.Animation.FirstPerson.StunSpearEquip_02_Montage import StunSpearEquip_02_Montage
from Script.FactoryGame import PlayStunEffects
from Game.FactoryGame.Equipment.StunSpear.Animation.StunSpearAttack_Left_Montage import StunSpearAttack_Left_Montage
from Game.FactoryGame.Equipment.StunSpear.Equip_StunSpear import ExecuteUbergraph_Equip_StunSpear.K2Node_ComponentBoundEvent_OtherActor
from Game.FactoryGame.Character.Player.CameraShake.StunSpearAttackRight_CamerAnim import StunSpearAttackRight_CamerAnim
from Game.FactoryGame.Equipment.StunSpear.Animation.StunSpearEquip_01_Montage import StunSpearEquip_01_Montage
from Script.Engine import AnimMontage
from Game.FactoryGame.Equipment.StunSpear.Equip_StunSpear import ExecuteUbergraph_Equip_StunSpear.K2Node_ComponentBoundEvent_OtherBodyIndex
from Game.FactoryGame.Equipment.StunSpear.Equip_StunSpear import ExecuteUbergraph_Equip_StunSpear.K2Node_ComponentBoundEvent_OverlappedComponent
from Game.FactoryGame.Equipment.StunSpear.Equip_StunSpear import ExecuteUbergraph_Equip_StunSpear.K2Node_ComponentBoundEvent_OtherComp
from Script.FactoryGame import GetShouldPlaySecondSwing
from Script.Engine import Montage_Play
from Script.FactoryGame import FGEquipmentStunSpear
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.StunSpear.Equip_StunSpear import ExecuteUbergraph_Equip_StunSpear.K2Node_Event_DeltaSeconds
from Game.FactoryGame.Equipment.StunSpear.Animation.StunSpearEquip_02_Montage import StunSpearEquip_02_Montage
from Script.Engine import RandomIntegerInRange
from Script.Engine import Montage_GetCurrentSection
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.FactoryGame import ShouldShowStinger
from Script.FactoryGame import FGAnimPlayer
from Game.FactoryGame.Equipment.StunSpear.Animation.StunSpearStinger_01_Montage import StunSpearStinger_01_Montage
from Game.FactoryGame.Equipment.StunSpear.Animation.StunSpearAttack_Right_Montage import StunSpearAttack_Right_Montage
from Script.Engine import SkeletalMeshComponent
from Game.FactoryGame.Character.Player.Animation.FirstPerson.StunSpearEquip_01_Montage import StunSpearEquip_01_Montage

class Equip_StunSpear(FGEquipmentStunSpear):
    mCurrentMontageSection: FName
    mSecondAttackTimer: float
    mFirstAttackTimer: float
    mRandomAttackAnim: int32
    mRandomEquipAnim: int32
    mDamageTypeClass = NewObject[DamageType_StunSpear]()
    mSecondSwingMaxTime = 0.6000000238418579
    mSecondSwingCooldDownTime = 0.699999988079071
    mDamage = 7
    mAttackDistance = 400
    mAttachmentClass = NewObject[Attach_StunSpear]()
    mEquipmentSlot = EEquipmentSlot::ES_ARMS
    mAttachSocket = hand_rSocket
    mArmAnimation = EArmEquipment::AE_StunSpear
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def ReceiveTick(self):
        ExecuteUbergraph_Equip_StunSpear.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_StunSpear(5799)
    

    def SwordAttack(self):
        self.ExecuteUbergraph_Equip_StunSpear(5798)
    

    def PlayStunEffects(self):
        self.ExecuteUbergraph_Equip_StunSpear(5667)
    

    def BndEvt__Capsule_K2Node_ComponentBoundEvent_0_ComponentBeginOverlapSignature__DelegateSignature(self, OverlappedComponent: Ptr[PrimitiveComponent], OtherActor: Ptr[Actor], OtherComp: Ptr[PrimitiveComponent], OtherBodyIndex: int32, bFromSweep: bool, SweepResult: Const[Ref[HitResult]]):
        ExecuteUbergraph_Equip_StunSpear.K2Node_ComponentBoundEvent_OverlappedComponent = OverlappedComponent #  PERSISTENT_FRAME(
        ExecuteUbergraph_Equip_StunSpear.K2Node_ComponentBoundEvent_OtherActor = OtherActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Equip_StunSpear.K2Node_ComponentBoundEvent_OtherComp = OtherComp #  PERSISTENT_FRAME(
        ExecuteUbergraph_Equip_StunSpear.K2Node_ComponentBoundEvent_OtherBodyIndex = OtherBodyIndex #  PERSISTENT_FRAME(
        ExecuteUbergraph_Equip_StunSpear.K2Node_ComponentBoundEvent_bFromSweep = bFromSweep #  PERSISTENT_FRAME(
        ExecuteUbergraph_Equip_StunSpear.K2Node_ComponentBoundEvent_SweepResult = SweepResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_StunSpear(3237)
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_Equip_StunSpear(5697)
    

    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_StunSpear(5793)
    

    def OnHitTarget(self):
        self.ExecuteUbergraph_Equip_StunSpear(5800)
    

    def ExecuteUbergraph_Equip_StunSpear(self):
        goto(ComputedJump("EntryPoint"))
        self.StunSpearTrail_01.Deactivate()
        goto(ExecutionFlow.Pop())
        self.StunSpearTrail_01.Deactivate()
        goto(ExecutionFlow.Pop())
        # Label 89
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_0: bool = ReturnValue.IsLocallyControlled()
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ReturnValue3: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue2: Ptr[SkeletalMeshComponent] = ReturnValue3.GetMesh1P()
        ReturnValue7: Ptr[AnimInstance] = ReturnValue2.GetAnimInstance()
        ReturnValue_1: Ptr[AnimMontage] = ReturnValue7.GetCurrentActiveMontage()
        ReturnValue7.Montage_Stop(0, ReturnValue_1)
        ReturnValue10: Ptr[AnimInstance] = self.StunSpear_skl.GetAnimInstance()
        ReturnValue1: Ptr[AnimMontage] = ReturnValue10.GetCurrentActiveMontage()
        ReturnValue10.Montage_Stop(0, ReturnValue1)
        ReturnValue2_0: Ptr[Pawn] = self.GetInstigator()
        ReturnValue2_1: Ptr[Controller] = ReturnValue2_0.GetController()
        Controller2: Ptr[PlayerController] = Cast[PlayerController](ReturnValue2_1)
        bSuccess2: bool = Controller2
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        Controller2.PlayerCameraManager.StopAllCameraAnims(True)
        ReturnValue3_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_E_ShockBaton_All, self, True)
        goto(ExecutionFlow.Pop())
        # Label 737
        ReturnValue_2: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_3: Ptr[Controller] = ReturnValue_2.GetController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue_3)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Controller.ClientPlayCameraAnim(StunSpearAttackLeft_CamerAnim, 1, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        self.StunSpearTrail_01.Activate(False)
        Default__KismetSystemLibrary.Delay(self, ReturnValue10_0, LatentActionInfo(Linkage = 15, UUID = 733650783, ExecutionFunction = "ExecuteUbergraph_Equip_StunSpear", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1074
        ReturnValue_4: Ptr[AnimInstance] = self.StunSpear_skl.GetAnimInstance()
        ReturnValue_5: float = ReturnValue_4.Montage_Play(StunSpearEquip_02_Montage, 1, 0, 0, True)
        ReturnValue5: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ShockBaton_Equip_02, self, True)
        goto(ExecutionFlow.Pop())
        # Label 1242
        ReturnValue_4 = self.StunSpear_skl.GetAnimInstance()
        ReturnValue_6: bool = ReturnValue_4.Montage_IsPlaying(StunSpearEquip_02_Montage)
        if not ReturnValue_6:
            goto('L1074')
        goto(ExecutionFlow.Pop())
        # Label 1350
        self.StunSpearTrail_01.Activate(False)
        Default__KismetSystemLibrary.Delay(self, ReturnValue9, LatentActionInfo(Linkage = 52, UUID = -95534505, ExecutionFunction = "ExecuteUbergraph_Equip_StunSpear", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 1468
        ReturnValue_7: bool = self.GetShouldPlaySecondSwing()
        if not ReturnValue_7:
            goto('L2198')
        ReturnValue5_0: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue4: Ptr[SkeletalMeshComponent] = ReturnValue5_0.GetMesh1P()
        ReturnValue9: Ptr[AnimInstance] = ReturnValue4.GetAnimInstance()
        ReturnValue10_0: float = ReturnValue9.Montage_Play(StunSpearAttack_Montage, 1, 0, 0, True)
        ReturnValue5_0 = self.GetInstigatorCharacter()
        ReturnValue4 = ReturnValue5_0.GetMesh1P()
        ReturnValue9 = ReturnValue4.GetAnimInstance()
        ReturnValue9.Montage_JumpToSection("LeftStart", StunSpearAttack_Montage)
        ReturnValue5_0 = self.GetInstigatorCharacter()
        ReturnValue4 = ReturnValue5_0.GetMesh1P()
        ReturnValue9 = ReturnValue4.GetAnimInstance()
        ReturnValue_8: FName = ReturnValue9.Montage_GetCurrentSection(StunSpearAttack_Montage)
        self.mCurrentMontageSection = ReturnValue_8
        ReturnValue_9: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_T_ShockBaton_Attack, self, True)
        ReturnValue2_2: Ptr[AnimInstance] = self.StunSpear_skl.GetAnimInstance()
        ReturnValue2_3: float = ReturnValue2_2.Montage_Play(StunSpearAttack_Left_Montage, 1, 0, 0, True)
        goto('L737')
        # Label 2198
        ReturnValue_10: bool = GreaterEqual_IntInt(self.mRandomAttackAnim, 9)
        if not ReturnValue_10:
            goto('L2813')
        ReturnValue5_0 = self.GetInstigatorCharacter()
        ReturnValue4 = ReturnValue5_0.GetMesh1P()
        ReturnValue9 = ReturnValue4.GetAnimInstance()
        ReturnValue8: float = ReturnValue9.Montage_Play(StunSpearAttack_Right_02_Montage, 1, 0, 0, True)
        ReturnValue2_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_T_ShockBaton_Attack, self, True)
        # Label 2475
        ReturnValue3_1: Ptr[AnimInstance] = self.StunSpear_skl.GetAnimInstance()
        ReturnValue3_2: float = ReturnValue3_1.Montage_Play(StunSpearAttack_Right_Montage, 1, 0, 0, True)
        ReturnValue3_3: Ptr[Pawn] = self.GetInstigator()
        ReturnValue3_4: Ptr[Controller] = ReturnValue3_3.GetController()
        Controller3: Ptr[PlayerController] = Cast[PlayerController](ReturnValue3_4)
        bSuccess3: bool = Controller3
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        Controller3.ClientPlayCameraAnim(StunSpearAttackRight_CamerAnim, 1, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        goto('L1350')
        # Label 2813
        ReturnValue5_0 = self.GetInstigatorCharacter()
        ReturnValue4 = ReturnValue5_0.GetMesh1P()
        ReturnValue9 = ReturnValue4.GetAnimInstance()
        ReturnValue9 = ReturnValue9.Montage_Play(StunSpearAttack_Montage, 1, 0, 0, True)
        ReturnValue5_0 = self.GetInstigatorCharacter()
        ReturnValue4 = ReturnValue5_0.GetMesh1P()
        ReturnValue9 = ReturnValue4.GetAnimInstance()
        ReturnValue_8 = ReturnValue9.Montage_GetCurrentSection(StunSpearAttack_Montage)
        self.mCurrentMontageSection = ReturnValue_8
        ReturnValue1_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_T_ShockBaton_Attack, self, True)
        goto('L2475')
        goto(ExecutionFlow.Pop())
        # Label 3238
        ExecutionFlow.Push("L1242")
        # Label 3243
        ReturnValue1_1: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_11: Ptr[SkeletalMeshComponent] = ReturnValue1_1.GetMesh1P()
        ReturnValue5_1: Ptr[AnimInstance] = ReturnValue_11.GetAnimInstance()
        ReturnValue3_5: bool = ReturnValue5_1.Montage_IsPlaying(StunSpearEquip_02_Montage)
        if not ReturnValue3_5:
            goto('L3413')
        goto(ExecutionFlow.Pop())
        # Label 3413
        ReturnValue1_1 = self.GetInstigatorCharacter()
        ReturnValue_11 = ReturnValue1_1.GetMesh1P()
        ReturnValue5_1 = ReturnValue_11.GetAnimInstance()
        ReturnValue5_2: float = ReturnValue5_1.Montage_Play(StunSpearEquip_02_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 3590
        ReturnValue_12: bool = self.ShouldShowStinger()
        if not ReturnValue_12:
            goto('L3799')
        ExecutionFlow.Push("L4672")
        ReturnValue4_0: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue3_6: Ptr[SkeletalMeshComponent] = ReturnValue4_0.GetMesh1P()
        ReturnValue8_0: Ptr[AnimInstance] = ReturnValue3_6.GetAnimInstance()
        ReturnValue5_3: bool = ReturnValue8_0.Montage_IsPlaying(StunSpearStinger_01_Montage)
        if not ReturnValue5_3:
            goto('L4948')
        goto(ExecutionFlow.Pop())
        # Label 3799
        ReturnValue1_2: int32 = RandomIntegerInRange(0, 5)
        self.mRandomEquipAnim = ReturnValue1_2
        ReturnValue6: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue5_4: Ptr[SkeletalMeshComponent] = ReturnValue6.GetMesh1P()
        ReturnValue11: Ptr[AnimInstance] = ReturnValue5_4.GetAnimInstance()
        Player: Ptr[FGAnimPlayer] = Cast[FGAnimPlayer](ReturnValue11)
        bSuccess4: bool = Player
        if not bSuccess4:
           goto(ExecutionFlow.Pop())
        ReturnValue_13: bool = EqualEqual_ByteByte(Player.mArmSlotType, 3)
        if not ReturnValue_13:
            goto('L4168')
        ReturnValue7_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ShockBaton_Equip_03, self, True)
        goto('L3243')
        # Label 4168
        ReturnValue1_3: bool = GreaterEqual_IntInt(self.mRandomEquipAnim, 2)
        if not ReturnValue1_3:
            goto('L4221')
        goto('L3238')
        # Label 4221
        ExecutionFlow.Push("L4396")
        ReturnValue2_5: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_4: Ptr[SkeletalMeshComponent] = ReturnValue2_5.GetMesh1P()
        ReturnValue6_0: Ptr[AnimInstance] = ReturnValue1_4.GetAnimInstance()
        ReturnValue4_1: bool = ReturnValue6_0.Montage_IsPlaying(StunSpearEquip_01_Montage)
        if not ReturnValue4_1:
            goto('L5420')
        goto(ExecutionFlow.Pop())
        # Label 4396
        ReturnValue4_2: Ptr[AnimInstance] = self.StunSpear_skl.GetAnimInstance()
        ReturnValue2_6: bool = ReturnValue4_2.Montage_IsPlaying(StunSpearEquip_01_Montage)
        if not ReturnValue2_6:
            goto('L4504')
        goto(ExecutionFlow.Pop())
        # Label 4504
        ReturnValue4_2 = self.StunSpear_skl.GetAnimInstance()
        ReturnValue4_3: float = ReturnValue4_2.Montage_Play(StunSpearEquip_01_Montage, 1, 0, 0, True)
        ReturnValue4_4: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ShockBaton_Equip_01, self, True)
        goto(ExecutionFlow.Pop())
        # Label 4672
        ReturnValue1_5: Ptr[AnimInstance] = self.StunSpear_skl.GetAnimInstance()
        ReturnValue1_6: bool = ReturnValue1_5.Montage_IsPlaying(StunSpearStinger_01_Montage)
        if not ReturnValue1_6:
            goto('L4780')
        goto(ExecutionFlow.Pop())
        # Label 4780
        ReturnValue1_5 = self.StunSpear_skl.GetAnimInstance()
        ReturnValue1_7: float = ReturnValue1_5.Montage_Play(StunSpearStinger_01_Montage, 1, 0, 0, True)
        ReturnValue6_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_E_ShockBaton_Stinger, self, True)
        goto(ExecutionFlow.Pop())
        # Label 4948
        ReturnValue4_0 = self.GetInstigatorCharacter()
        ReturnValue3_6 = ReturnValue4_0.GetMesh1P()
        ReturnValue8_0 = ReturnValue3_6.GetAnimInstance()
        ReturnValue7_1: float = ReturnValue8_0.Montage_Play(StunSpearStinger_01_Montage, 1, 1, 0, True)
        ReturnValue1_8: Ptr[Pawn] = self.GetInstigator()
        ReturnValue1_9: Ptr[Controller] = ReturnValue1_8.GetController()
        Controller1: Ptr[PlayerController] = Cast[PlayerController](ReturnValue1_9)
        bSuccess1: bool = Controller1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Controller1.ClientPlayCameraAnim(StunSpearStinger_01_CamerAnim, 1, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        Default__KismetSystemLibrary.Delay(self, 6, LatentActionInfo(Linkage = -1, UUID = 1033899890, ExecutionFunction = "ExecuteUbergraph_Equip_StunSpear", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 5420
        ReturnValue2_5 = self.GetInstigatorCharacter()
        ReturnValue1_4 = ReturnValue2_5.GetMesh1P()
        ReturnValue6_0 = ReturnValue1_4.GetAnimInstance()
        ReturnValue6_2: float = ReturnValue6_0.Montage_Play(StunSpearEquip_01_Montage, 1, 0, 0, True)
        goto(ExecutionFlow.Pop())
        # Label 5597
        ReturnValue_14: int32 = RandomIntegerInRange(0, 10)
        self.mRandomAttackAnim = ReturnValue_14
        goto('L1468')
        self.PlayStunEffects()
        goto('L5597')
        # Label 5682
        self.WasUnEquipped()
        goto('L89')
        goto('L5682')
        # Label 5702
        self.WasEquipped()
        ReturnValue7_2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_10: bool = ReturnValue7_2.IsLocallyControlled()
        if not ReturnValue1_10:
           goto(ExecutionFlow.Pop())
        goto('L3590')
        goto('L5702')
        goto(ExecutionFlow.Pop())
        goto(ExecutionFlow.Pop())
        ReturnValue4_5: Ptr[Pawn] = self.GetInstigator()
        ReturnValue4_6: Ptr[Controller] = ReturnValue4_5.GetController()
        Controller4: Ptr[PlayerController] = Cast[PlayerController](ReturnValue4_6)
        bSuccess5: bool = Controller4
        if not bSuccess5:
           goto(ExecutionFlow.Pop())
        Controller4.ClientPlayCameraAnim(ShockShankHit_01_CameraAnim, 1, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        goto(ExecutionFlow.Pop())
    
