
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
from Script.Engine import GetController
from Script.Engine import GameStateBase
from Game.FactoryGame.Equipment.HazardSuit.Equip_HazardSuit import ExecuteUbergraph_Equip_HazardSuit
from Script.FactoryGame import CanAffordUse
from Script.FactoryGame import IsLocalInstigator
from Script.FactoryGame import GetMesh1P
from Game.FactoryGame.Equipment.GasMask.Audio.Stop_EQ_GasMask import Stop_EQ_GasMask
from Script.Engine import FMax
from Script.Engine import BooleanOR
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGGameState
from Game.FactoryGame.Character.Player.CameraShake.GasMaskEquip_01_CameraAnim import GasMaskEquip_01_CameraAnim
from Script.FactoryGame import ChargeForUse
from Script.Engine import Montage_Play
from Script.FactoryGame import AdjustDamage
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Equipment.HazardSuit.Equip_HazardSuit import ExecuteUbergraph_Equip_HazardSuit.K2Node_Event_DeltaSeconds
from Game.FactoryGame.Equipment.GasMask.Audio.Bus_LowPass_GasMask_Reset import Bus_LowPass_GasMask_Reset
from Game.FactoryGame.-Shared.Blueprint.BP_DamageType import BP_DamageType
from Game.FactoryGame.Equipment.GasMask.Audio.Play_EQ_GasMask import Play_EQ_GasMask
from Script.Engine import GetGameState
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Script.Engine import Montage_IsPlaying
from Script.Engine import AnimInstance
from Script.AkAudio import AkComponent
from Script.FactoryGame import GetCheatNoCost
from Script.Engine import SkeletalMeshComponent

class Equip_HazardSuit(FGGasMask):
    mCountdown: float
    mFilterDuration: float = 300
    mFuelConsumed: bool
    mAttachmentClass = NewObject[Attach_HazardSuit]()
    mEquipmentSlot = EEquipmentSlot::ES_BACK
    mAttachSocket = helmetSocket
    mCostToUse = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IodineInfusedFilter/Desc_HazmatFilter.Desc_HazmatFilter_C', 'amount': 1}]
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def EnablePostProcessing(self, mEnabled: bool):
        ReturnValue: bool = self.IsLocalInstigator()
        if not ReturnValue:
            goto('L420')
        if not mEnabled:
            goto('L89')
        if not self.PPComponent.bEnabled:
            goto('L275')
        # End
        # Label 89
        if not self.PPComponent.bEnabled:
            goto('L420')
        self.PPComponent.bEnabled = False
        ReturnValue1: int32 = self.Ak.PostAkEvent(Stop_EQ_GasMask)
        ReturnValue3: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Bus_LowPass_GasMask_Reset, self, True)
        # End
        # Label 275
        self.PPComponent.bEnabled = True
        ReturnValue2: int32 = self.Ak.PostAkEvent(Play_EQ_GasMask)
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Bus_LowPass_GasMask, self, True)
    

    def AdjustDamage(self):
        ReturnValue: float = self.AdjustDamage(damageAmount, DamageType, InstigatedBy, DamageCauser)
        damage: float = ReturnValue
        Type: Const[Ptr[BP_DamageType]] = Cast[BP_DamageType](DamageType)
        bSuccess: bool = Type
        if not bSuccess:
            goto('L521')
        ReturnValue_0: bool = self.IsEquipped()
        ReturnValue_1: bool = Type.mFromGas and self.mFuelConsumed
        ReturnValue1: bool = Type.mFromHeat and ReturnValue_0
        ReturnValue2: bool = ReturnValue_1 and ReturnValue_0
        ReturnValue3: bool = Type.mFromRadiation and ReturnValue_0
        ReturnValue_2: bool = BooleanOR(ReturnValue2, ReturnValue3)
        ReturnValue1_0: bool = BooleanOR(ReturnValue_2, ReturnValue1)
        if not ReturnValue1_0:
            goto('L521')
        damage = 0
        # Label 521
        ReturnValue_3: float = damage
    

    def WasUnEquipped(self):
        self.ExecuteUbergraph_Equip_HazardSuit(1199)
    

    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_HazardSuit(1194)
    

    def ReceiveTick(self):
        ExecuteUbergraph_Equip_HazardSuit.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_HazardSuit(1169)
    

    def ExecuteUbergraph_Equip_HazardSuit(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        ReturnValue: bool = self.mCountdown <= 0
        if not ReturnValue:
            goto('L363')
        ReturnValue_0: bool = self.CanAffordUse()
        if not ReturnValue_0:
            goto('L479')
        ReturnValue_1: bool = self.HasAuthority()
        if not ReturnValue_1:
            goto('L309')
        ReturnValue_2: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue_2)
        bSuccess: bool = State
        if not bSuccess:
            goto('L506')
        ReturnValue_3: bool = State.GetCheatNoCost()
        if not ReturnValue_3:
            goto('L506')
        # Label 309
        self.mCountdown = self.mFilterDuration
        self.mFuelConsumed = True
        self.EnablePostProcessing(True)
        goto(ExecutionFlow.Pop())
        # Label 363
        ReturnValue_4: float = self.mCountdown - DeltaSeconds
        ReturnValue_5: float = FMax(ReturnValue_4, 0)
        self.mCountdown = ReturnValue_5
        goto(ExecutionFlow.Pop())
        # Label 479
        self.mFuelConsumed = False
        self.EnablePostProcessing(False)
        goto(ExecutionFlow.Pop())
        # Label 506
        self.ChargeForUse()
        goto('L309')
        # Label 521
        ReturnValue_6: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue_7: Ptr[SkeletalMeshComponent] = ReturnValue_6.GetMesh1P()
        ReturnValue_8: Ptr[AnimInstance] = ReturnValue_7.GetAnimInstance()
        ReturnValue_9: float = ReturnValue_8.Montage_Play(GasMaskEquip_01_Montage, 1, 0, 0, True)
        ReturnValue_10: Ptr[Pawn] = self.GetInstigator()
        ReturnValue_11: Ptr[Controller] = ReturnValue_10.GetController()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue_11)
        bSuccess1: bool = Controller
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Controller.ClientPlayCameraAnim(GasMaskEquip_01_CameraAnim, 1, 1, 0, 0, False, False, 0, Rotator::FromPitchYawRoll(0, 0, 0))
        goto(ExecutionFlow.Pop())
        # Label 917
        ReturnValue_6 = self.GetInstigatorCharacter()
        ReturnValue_7 = ReturnValue_6.GetMesh1P()
        ReturnValue_8 = ReturnValue_7.GetAnimInstance()
        ReturnValue_12: bool = ReturnValue_8.Montage_IsPlaying(GasMaskEquip_01_Montage)
        if not ReturnValue_12:
            goto('L521')
        goto(ExecutionFlow.Pop())
        # Label 1087
        self.EnablePostProcessing(False)
        goto(ExecutionFlow.Pop())
        # Label 1103
        ReturnValue_13: bool = self.IsEquipped()
        if not ReturnValue_13:
           goto(ExecutionFlow.Pop())
        goto('L15')
        # Label 1138
        self.EnablePostProcessing(True)
        goto(ExecutionFlow.Pop())
        # Label 1154
        if not self.mFuelConsumed:
           goto(ExecutionFlow.Pop())
        goto('L1138')
        goto('L1103')
        # Label 1174
        self.WasEquipped()
        ExecutionFlow.Push("L917")
        goto('L1154')
        goto('L1174')
        goto('L1087')
    
