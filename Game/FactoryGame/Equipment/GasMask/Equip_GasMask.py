
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Player.Animation.FirstPerson.GasMaskEquip_01_Montage import GasMaskEquip_01_Montage
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Script.FactoryGame import GetInstigatorCharacter
from Script.Engine import Pawn
from Script.FactoryGame import WasEquipped
from Script.FactoryGame import IsEquipped
from Script.Engine import GetInstigator
from Game.FactoryGame.Equipment.GasMask.Audio.Bus_LowPass_GasMask import Bus_LowPass_GasMask
from Script.Engine import HasAuthority
from Script.Engine import GetAnimInstance
from Script.FactoryGame import FGGasMask
from Script.Engine import PlayerController
from Script.Engine import GetController
from Script.Engine import GameStateBase
from Script.FactoryGame import CanAffordUse
from Script.Engine import GetCurrentActiveMontage
from Script.FactoryGame import IsLocalInstigator
from Script.Engine import Montage_Stop
from Script.FactoryGame import GetMesh1P
from Game.FactoryGame.Equipment.GasMask.Audio.Stop_EQ_GasMask import Stop_EQ_GasMask
from Script.Engine import FMax
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGGameState
from Game.FactoryGame.Character.Player.CameraShake.GasMaskEquip_01_CameraAnim import GasMaskEquip_01_CameraAnim
from Script.Engine import AnimMontage
from Script.FactoryGame import ChargeForUse
from Script.Engine import Montage_Play
from Script.FactoryGame import AdjustDamage
from Game.FactoryGame.Equipment.GasMask.Equip_GasMask import ExecuteUbergraph_Equip_GasMask
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.GasMask.Audio.Bus_LowPass_GasMask_Reset import Bus_LowPass_GasMask_Reset
from Game.FactoryGame.-Shared.Blueprint.BP_DamageType import BP_DamageType
from Game.FactoryGame.Equipment.GasMask.Audio.Play_EQ_GasMask import Play_EQ_GasMask
from Game.FactoryGame.Equipment.GasMask.Equip_GasMask import ExecuteUbergraph_Equip_GasMask.K2Node_Event_DeltaSeconds
from Script.Engine import GetGameState
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.FactoryGame import GetCheatNoCost
from Script.Engine import SkeletalMeshComponent

class Equip_GasMask(FGGasMask):
    mCountdown: float
    mFilterDuration: float = 240
    mIsWorking: bool
    mHasNegatedDamage: bool
    mDamageNegated: float
    mDisableEffectTimer: float
    mAttachmentClass = NewObject[Attach_GasMask]()
    mEquipmentSlot = EEquipmentSlot::ES_BACK
    mAttachSocket = helmetSocket
    mCostToUse = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Filter/Desc_Filter.Desc_Filter_C', 'amount': 1}]
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def EnablePostProcessing(self, mEnabled: bool):
        ReturnValue: bool = self.IsLocalInstigator()
        if not ReturnValue:
            goto('L408')
        if not mEnabled:
            goto('L89')
        if not self.PPComponent.bEnabled:
            goto('L269')
        # End
        # Label 89
        if not self.PPComponent.bEnabled:
            goto('L408')
        self.PPComponent.bEnabled = False
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Stop_EQ_GasMask, self, True)
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Bus_LowPass_GasMask_Reset, self, True)
        # End
        # Label 269
        self.PPComponent.bEnabled = True
        ReturnValue1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_EQ_GasMask, self, True)
        ReturnValue2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Bus_LowPass_GasMask, self, True)
    

    def AdjustDamage(self):
        ReturnValue: float = self.AdjustDamage(damageAmount, DamageType, InstigatedBy, DamageCauser)
        damage: float = ReturnValue
        Type: Const[Ptr[BP_DamageType]] = Cast[BP_DamageType](DamageType)
        bSuccess: bool = Type
        if not bSuccess:
            goto('L409')
        ReturnValue_0: bool = self.IsEquipped()
        ReturnValue_1: bool = Type.mFromGas and ReturnValue_0
        ReturnValue1: bool = ReturnValue_1 and self.mIsWorking
        if not ReturnValue1:
            goto('L409')
        self.mHasNegatedDamage = True
        ReturnValue_2: float = damage + self.mDamageNegated
        self.mDamageNegated = ReturnValue_2
        damage = 0
        # Label 409
        ReturnValue_3: float = damage
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_Equip_GasMask(1826)
    

    def ReceiveTick(self):
        ExecuteUbergraph_Equip_GasMask.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_GasMask(1514)
    

    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_GasMask(628)
    

    def ExecuteUbergraph_Equip_GasMask(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.ChargeForUse()
        # Label 25
        self.mHasNegatedDamage = False
        # Label 36
        self.mCountdown = self.mFilterDuration
        self.mIsWorking = True
        goto(ExecutionFlow.Pop())
        # Label 75
        ReturnValue: bool = self.mCountdown <= 0
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        ReturnValue_0: bool = self.CanAffordUse()
        if not ReturnValue_0:
            goto('L370')
        ReturnValue_1: bool = self.HasAuthority()
        if not ReturnValue_1:
            goto('L36')
        ReturnValue_2: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue_2)
        bSuccess: bool = State
        if not bSuccess:
            goto('L15')
        ReturnValue_3: bool = State.GetCheatNoCost()
        if not ReturnValue_3:
            goto('L15')
        goto('L25')
        # Label 370
        self.mIsWorking = False
        self.EnablePostProcessing(False)
        self.mDisableEffectTimer = -1
        goto(ExecutionFlow.Pop())
        # Label 420
        self.EnablePostProcessing(False)
        ReturnValue1: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_0: Ptr[SkeletalMeshComponent] = ReturnValue1.GetMesh1P()
        ReturnValue1_1: Ptr[AnimInstance] = ReturnValue1_0.GetAnimInstance()
        ReturnValue_4: Ptr[AnimMontage] = ReturnValue1_1.GetCurrentActiveMontage()
        ReturnValue1_1.Montage_Stop(0, ReturnValue_4)
        goto(ExecutionFlow.Pop())
        self.WasEquipped()
        ExecutionFlow.Push("L667")
        self.mDisableEffectTimer = -1
        goto(ExecutionFlow.Pop())
        # Label 667
        ReturnValue1_2: bool = self.IsLocalInstigator()
        if not ReturnValue1_2:
           goto(ExecutionFlow.Pop())
        ReturnValue_5: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_6: Ptr[SkeletalMeshComponent] = ReturnValue_5.GetMesh1P()
        ReturnValue_7: Ptr[AnimInstance] = ReturnValue_6.GetAnimInstance()
        ReturnValue_8: bool = ReturnValue_7.Montage_IsPlaying(GasMaskEquip_01_Montage)
        if not ReturnValue_8:
            goto('L867')
        goto(ExecutionFlow.Pop())
        # Label 867
        ReturnValue_5 = self.GetInstigatorCharacter()
        ReturnValue_6 = ReturnValue_5.GetMesh1P()
        ReturnValue_7 = ReturnValue_6.GetAnimInstance()
        ReturnValue_9: float = ReturnValue_7.Montage_Play(GasMaskEquip_01_Montage, 1, 0, 0, True)
        ReturnValue_10: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_11: Ptr[Controller] = ReturnValue_10.GetController()
        Controller: Ptr[PlayerController] = Cast[PlayerController](ReturnValue_11)
        bSuccess1: bool = Controller
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Controller.ClientPlayCameraAnim(GasMaskEquip_01_CameraAnim, 1, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        goto(ExecutionFlow.Pop())
        # Label 1263
        ReturnValue_12: bool = self.IsEquipped()
        if not ReturnValue_12:
           goto(ExecutionFlow.Pop())
        ReturnValue1_3: bool = self.CanAffordUse()
        self.mIsWorking = ReturnValue1_3
        ReturnValue3: bool = self.mDisableEffectTimer <= 0
        if not ReturnValue3:
            goto('L1381')
        goto(ExecutionFlow.Pop())
        # Label 1381
        ReturnValue1_4: float = self.mDisableEffectTimer - DeltaSeconds
        self.mDisableEffectTimer = ReturnValue1_4
        ReturnValue2: bool = self.mDisableEffectTimer <= 0
        if not ReturnValue2:
           goto(ExecutionFlow.Pop())
        self.EnablePostProcessing(False)
        goto(ExecutionFlow.Pop())
        ReturnValue_12 = self.IsEquipped()
        ReturnValue_13: bool = ReturnValue_12 and self.mHasNegatedDamage
        if not ReturnValue_13:
            goto('L1263')
        ReturnValue1_5: bool = self.mDisableEffectTimer <= 0
        if not ReturnValue1_5:
            goto('L1649')
        self.EnablePostProcessing(True)
        # Label 1649
        self.mDisableEffectTimer = 6
        ReturnValue_14: float = self.mCountdown - self.mDamageNegated
        ReturnValue_15: float = FMax(ReturnValue_14, 0)
        self.mCountdown = ReturnValue_15
        self.mDamageNegated = 0
        self.mHasNegatedDamage = False
        goto('L75')
        ReturnValue_16: bool = self.IsLocalInstigator()
        if not ReturnValue_16:
           goto(ExecutionFlow.Pop())
        goto('L420')
    
