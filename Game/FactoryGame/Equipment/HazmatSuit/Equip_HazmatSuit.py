
from codegen.ue4_stub import *

from Script.FactoryGame import FGSuitBase
from Script.FactoryGame import FGCharacterPlayer
from Script.FactoryGame import GetInstigatorCharacter
from Script.FactoryGame import WasEquipped
from Game.FactoryGame.Equipment.HazmatSuit.Equip_HazmatSuit import ExecuteUbergraph_Equip_HazmatSuit.K2Node_Event_DeltaSeconds
from Script.FactoryGame import IsEquipped
from Script.FactoryGame import WasUnEquipped
from Script.Engine import HasAuthority
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import ReceiveTick
from Script.Engine import GameStateBase
from Script.FactoryGame import CanAffordUse
from Script.FactoryGame import IsLocalInstigator
from Script.Engine import FMax
from Script.Engine import Default__GameplayStatics
from Script.FactoryGame import FGGameState
from Script.FactoryGame import ChargeForUse
from Script.FactoryGame import AdjustDamage
from Script.FactoryGame import SetRadiationImmunity
from Game.FactoryGame.-Shared.Blueprint.BP_DamageType import BP_DamageType
from Script.Engine import GetGameState
from Game.FactoryGame.Equipment.HazmatSuit.Equip_HazmatSuit import ExecuteUbergraph_Equip_HazmatSuit
from Script.FactoryGame import GetCheatNoCost
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class Equip_HazmatSuit(FGSuitBase):
    mImmunity: float
    mIsWorking: bool
    mHasNegatedDamage: bool
    mDamageNegated: float
    mFilterDuration: float = 240
    mCountdown: float
    mDisableEffectTimer: float
    mSuit1PMeshMaterials = [{'SlotName': 'Body_Details', 'Material': {'$AssetPath': '/Game/FactoryGame/Character/Player/Material/MI_Haz_Body_Details.MI_Haz_Body_Details'}}, {'SlotName': 'Body_01', 'Material': {'$AssetPath': '/Game/FactoryGame/Character/Player/Material/MI_Haz_Body_01.MI_Haz_Body_01'}}, {'SlotName': 'Body_02', 'Material': {'$AssetPath': '/Game/FactoryGame/Character/Player/Material/MI_Haz_Body_02.MI_Haz_Body_02'}}, {'SlotName': 'Body_Hands', 'Material': {'$AssetPath': '/Game/FactoryGame/Character/Player/Material/MI_Haz_Body_Hands.MI_Haz_Body_Hands'}}, {'SlotName': 'Body_Backpack', 'Material': {'$AssetPath': '/Game/FactoryGame/Character/Player/Material/MI_Haz_Body_Backpack.MI_Haz_Body_Backpack'}}]
    mAttachmentClass = NewObject[Attach_HazmatSuit]()
    mEquipmentSlot = EEquipmentSlot::ES_BACK
    mEquipSound = Namespace(AssetPath='/Game/FactoryGame/Equipment/HazmatSuit/Audio/Play_C_HazMatSuit_Equip.Play_C_HazMatSuit_Equip')
    mUnequipSound = Namespace(AssetPath='/Game/FactoryGame/Equipment/HazmatSuit/Audio/Play_C_HazMatSuit_UnEquip.Play_C_HazMatSuit_UnEquip')
    mCostToUse = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IodineInfusedFilter/Desc_HazmatFilter.Desc_HazmatFilter_C', 'amount': 1}]
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bOnlyRelevantToOwner = True
    bNetUseOwnerRelevancy = True
    bReplicates = True
    RemoteRole = 1
    
    def EnablePostProcessing(self, Enabled: bool):
        ReturnValue: bool = self.IsLocalInstigator()
        if not ReturnValue:
            goto('L34')
    

    def AdjustDamage(self):
        ReturnValue: float = self.AdjustDamage(damageAmount, DamageType, InstigatedBy, DamageCauser)
        damage: float = ReturnValue
        Type: Const[Ptr[BP_DamageType]] = Cast[BP_DamageType](DamageType)
        bSuccess: bool = Type
        if not bSuccess:
            goto('L409')
        ReturnValue_0: bool = self.IsEquipped()
        ReturnValue_1: bool = Type.mFromRadiation and ReturnValue_0
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
        self.ExecuteUbergraph_Equip_HazmatSuit(491)
    

    def ReceiveTick(self):
        ExecuteUbergraph_Equip_HazmatSuit.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Equip_HazmatSuit(597)
    

    def WasEquipped(self):
        self.ExecuteUbergraph_Equip_HazmatSuit(1331)
    

    def ExecuteUbergraph_Equip_HazmatSuit(self):
        # Label 10
        ReturnValue: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue.SetRadiationImmunity(1)
        # End
        # Label 72
        ReturnValue_0: bool = self.HasAuthority()
        if not ReturnValue_0:
            goto('L295')
        ReturnValue_1: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue_1)
        bSuccess: bool = State
        if not bSuccess:
            goto('L395')
        ReturnValue_2: bool = State.GetCheatNoCost()
        if not ReturnValue_2:
            goto('L395')
        # Label 284
        self.mHasNegatedDamage = False
        # Label 295
        ReturnValue2: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue2.SetRadiationImmunity(1)
        self.mCountdown = self.mFilterDuration
        self.mIsWorking = True
        # End
        # Label 395
        self.ChargeForUse()
        Default__KismetSystemLibrary.PrintString(self, "Hello", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto('L284')
        self.WasUnEquipped()
        ReturnValue1: bool = self.HasAuthority()
        if not ReturnValue1:
            goto('L1417')
        ReturnValue1_0: Ptr[FGCharacterPlayer] = self.GetInstigatorCharacter()
        ReturnValue1_0.SetRadiationImmunity(0)
        # End
        self.ReceiveTick(DeltaSeconds)
        ReturnValue_3: bool = self.IsEquipped()
        ReturnValue_4: bool = self.mHasNegatedDamage and ReturnValue_3
        if not ReturnValue_4:
            goto('L1010')
        ReturnValue1_1: bool = self.mDisableEffectTimer <= 0
        if not ReturnValue1_1:
            goto('L751')
        self.EnablePostProcessing(False)
        # Label 751
        self.mDisableEffectTimer = 6
        ReturnValue_5: float = self.mCountdown - self.mDamageNegated
        ReturnValue_6: float = FMax(ReturnValue_5, 0)
        self.mCountdown = ReturnValue_6
        self.mDamageNegated = 0
        self.mHasNegatedDamage = False
        ReturnValue_7: bool = self.mCountdown <= 0
        if not ReturnValue_7:
            goto('L1417')
        ReturnValue_8: bool = self.CanAffordUse()
        if not ReturnValue_8:
            goto('L1277')
        goto('L72')
        # Label 1010
        ReturnValue_3 = self.IsEquipped()
        if not ReturnValue_3:
            goto('L1417')
        ReturnValue1_2: bool = self.CanAffordUse()
        self.mIsWorking = ReturnValue1_2
        ReturnValue2_0: bool = self.mDisableEffectTimer <= 0
        if not ReturnValue2_0:
            goto('L1136')
        # End
        # Label 1136
        ReturnValue1_3: float = self.mDisableEffectTimer - DeltaSeconds
        self.mDisableEffectTimer = ReturnValue1_3
        ReturnValue3: bool = self.mDisableEffectTimer <= 0
        if not ReturnValue3:
            goto('L1417')
        self.EnablePostProcessing(False)
        # End
        # Label 1277
        self.mIsWorking = False
        self.EnablePostProcessing(False)
        self.mDisableEffectTimer = -1
        # End
        self.WasEquipped()
        self.mDisableEffectTimer = -1
        ReturnValue_9: bool = self.mCountdown > 0
        if not ReturnValue_9:
            goto('L1417')
        goto('L10')
    
