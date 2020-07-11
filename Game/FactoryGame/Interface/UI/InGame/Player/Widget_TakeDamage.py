
from codegen.ue4_stub import *

from Script.FactoryGame import FGHealthComponent
from Script.FactoryGame import GetHealthComponent
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_TakeDamage import ExecuteUbergraph_Widget_TakeDamage.K2Node_CustomEvent_damageCauser
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_TakeDamage import ExecuteUbergraph_Widget_TakeDamage.K2Node_CustomEvent_RadiationActive
from Script.Engine import SetVectorPropertyByName
from Script.Engine import Delay
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import SetObjectPropertyByName
from Script.Engine import Pawn
from Script.UMG import GetChildrenCount
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_TakeDamageIndicator import Widget_TakeDamageIndicator
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_TakeDamage import ExecuteUbergraph_Widget_TakeDamage.K2Node_CustomEvent_amount
from Script.FactoryGame import FGCharacterBase
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_TakeDamage import ExecuteUbergraph_Widget_TakeDamage.K2Node_CustomEvent_damageType
from Script.Engine import Ease
from Script.Engine import PlayerController
from Script.Engine import SetStructurePropertyByName
from Script.Engine import K2_GetPawn
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_TakeDamage import ExecuteUbergraph_Widget_TakeDamage.K2Node_CustomEvent_Damage
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_TakeDamage import ExecuteUbergraph_Widget_TakeDamage
from Script.UMG import StopAnimation
from Script.Engine import IsValid
from Script.UMG import SetPercent
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import SetColorAndOpacity
from Script.Engine import SetBoolPropertyByName
from Script.CoreUObject import Vector
from Script.UMG import WidgetAnimation
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_TakeDamage import ExecuteUbergraph_Widget_TakeDamage.K2Node_CustomEvent_instigatedBy
from Script.FactoryGame import GetCurrentHealth
from Script.Engine import RetriggerableDelay
from Script.UMG import UserWidget
from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_TakeDamage import ExecuteUbergraph_Widget_TakeDamage.K2Node_CustomEvent_damagedActor
from Script.Engine import Actor
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import K2_GetActorLocation
from Script.UMG import UMGSequencePlayer
from Script.UMG import Create
from Game.FactoryGame.Resource.DamageType_Radiation import DamageType_Radiation
from Script.UMG import IsAnimationPlaying
from Script.FactoryGame import GetMaxHealth
from Game.FactoryGame.Character.Player.BP_PlayerController import BP_PlayerController
from Game.FactoryGame.World.Environment.DamageType_FallDamage import DamageType_FallDamage
from Script.CoreUObject import LinearColor

class Widget_TakeDamage(UserWidget):
    CriticalHealth: Ptr[WidgetAnimation]
    WarningPulse: Ptr[WidgetAnimation]
    FallFade: Ptr[WidgetAnimation]
    RadiationFade: Ptr[WidgetAnimation]
    RadiationPulse: Ptr[WidgetAnimation]
    mDamageCauser: Ptr[Actor]
    
    def GetIsHealthCritical(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue)
        bSuccess: bool = Player
        ReturnValue_0: float = Player.mHealthComponent.GetCurrentHealth()
        ReturnValue_1: float = Player.mHealthComponent.GetMaxHealth()
        ReturnValue_2: float = ReturnValue_0 / ReturnValue_1
        ReturnValue_3: bool = ReturnValue_2 > 0.3333300054073334
        ReturnValue_4: bool = Not_PreBool(ReturnValue_3)
        IsHealthCritical = ReturnValue_4
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_TakeDamage(1983)
    

    def SpawnPointer(self, DamagedActor: Ptr[Actor], Damage: float, DamageType: Const[Ptr[DamageType]], InstigatedBy: Ptr[Controller], DamageCauser: Ptr[Actor]):
        ExecuteUbergraph_Widget_TakeDamage.K2Node_CustomEvent_damagedActor = DamagedActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_TakeDamage.K2Node_CustomEvent_Damage = Damage #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_TakeDamage.K2Node_CustomEvent_damageType = DamageType #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_TakeDamage.K2Node_CustomEvent_instigatedBy = InstigatedBy #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_TakeDamage.K2Node_CustomEvent_damageCauser = DamageCauser #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TakeDamage(2207)
    

    def OnRadiationDamage(self):
        self.ExecuteUbergraph_Widget_TakeDamage(3065)
    

    def SetPlayerPawn(self):
        self.ExecuteUbergraph_Widget_TakeDamage(3274)
    

    def ShowWarningMessage(self):
        self.ExecuteUbergraph_Widget_TakeDamage(3279)
    

    def UpdateRadiation(self, RadiationActive: bool, amount: float):
        ExecuteUbergraph_Widget_TakeDamage.K2Node_CustomEvent_RadiationActive = RadiationActive #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_TakeDamage.K2Node_CustomEvent_amount = amount #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TakeDamage(3417)
    

    def ExecuteUbergraph_Widget_TakeDamage(self):
        goto(ComputedJump("EntryPoint"))
        self.StopAnimation(self.RadiationPulse)
        ReturnValue2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.RadiationFade, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 81
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.CriticalHealth, 0, 1, 0, 1)
        # Label 127
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 147, 'Value': 'IMMINENT DESTRUCTION OF\r\nFICSIT PROPERTY DETECTED'}"
        Variable1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 254, 'Value': 'DAMAGE TO FICSIT\r\nPROPERTY DETECTED'}"
        
        IsHealthCritical = None
        self.GetIsHealthCritical(Ref[IsHealthCritical])
        Variable1_0: bool = IsHealthCritical
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mDamageWarningText.SetText(switch.get(Variable1_0, None))
        Variable_0: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        
        IsHealthCritical1 = None
        self.GetIsHealthCritical(Ref[IsHealthCritical1])
        Variable_1: bool = IsHealthCritical1
        
        Orange2 = None
        OrangeText2 = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange2], Ref[OrangeText2])
        
        switch_0 = {
            False: Variable_0,
            True: Orange2
        }
        self.mDamageWarningIcon.SetColorAndOpacity(switch_0.get(Variable_1, None))
        Variable_0 = LinearColor(R = 1, G = 1, B = 1, A = 1)
        
        IsHealthCritical1 = None
        self.GetIsHealthCritical(Ref[IsHealthCritical1])
        Variable_1 = IsHealthCritical1
        
        Orange2 = None
        OrangeText2 = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange2], Ref[OrangeText2])
        
        switch_1 = {
            False: Variable_0,
            True: Orange2
        }
        SlateColor.SpecifiedColor = switch_1.get(Variable_1, None)
        SlateColor.ColorUseRule = 0
        self.mDamageWarningText.SetColorAndOpacity(SlateColor)
        self.mDamageWarning.SetVisibility(0)
        Default__KismetSystemLibrary.RetriggerableDelay(self, 3, LatentActionInfo(Linkage = 1106, UUID = 2051014059, ExecutionFunction = "ExecuteUbergraph_Widget_TakeDamage", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.mDamageWarning.SetVisibility(2)
        goto(ExecutionFlow.Pop())
        # Label 1145
        self.mRadiationContainer.ClearChildren()
        ReturnValue2_0: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1: Ptr[Widget_TakeDamageIndicator] = Default__WidgetBlueprintLibrary.Create(self, Widget_TakeDamageIndicator, ReturnValue2_0)
        
        Orange1 = None
        OrangeText1 = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange1], Ref[OrangeText1])
        
        Orange1 = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue1, "mColor", Ref[Orange1])
        Default__KismetSystemLibrary.SetBoolPropertyByName(ReturnValue1, "mIsRadiation", True)
        ReturnValue1_0: Ptr[PanelSlot] = self.mRadiationContainer.AddChild(ReturnValue1)
        goto(ExecutionFlow.Pop())
        # Label 1491
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mDamageCauser)
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Widget_TakeDamageIndicator] = Default__WidgetBlueprintLibrary.Create(self, Widget_TakeDamageIndicator, ReturnValue_1)
        Default__KismetSystemLibrary.SetObjectPropertyByName(ReturnValue_2, "DamageCauser", self.mDamageCauser)
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        
        Orange = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_2, "mColor", Ref[Orange])
        ReturnValue_3: Vector = self.mDamageCauser.K2_GetActorLocation()
        
        Default__KismetSystemLibrary.SetVectorPropertyByName(ReturnValue_2, "mDamagePosition", Ref[ReturnValue_3])
        ReturnValue_4: Ptr[PanelSlot] = self.mContainer.AddChild(ReturnValue_2)
        goto(ExecutionFlow.Pop())
        self.SetPlayerPawn()
        ReturnValue1_1: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[BP_PlayerController] = Cast[BP_PlayerController](ReturnValue1_1)
        bSuccess3: bool = Controller
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        OutputDelegate1.BindUFunction(self, SetPlayerPawn)
        Controller.OnRespawnEnd.AddUnique(OutputDelegate1)
        ReturnValue4: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.WarningPulse, 0, 0, 0, 1)
        goto(ExecutionFlow.Pop())
        self.ShowWarningMessage()
        Radiation: Const[Ptr[DamageType_Radiation]] = Cast[DamageType_Radiation](damageType)
        bSuccess2: bool = Radiation
        if not bSuccess2:
            goto('L2475')
        ReturnValue_5: int32 = self.mRadiationContainer.GetChildrenCount()
        ReturnValue_6: bool = ReturnValue_5 > 0
        if not ReturnValue_6:
            goto('L1145')
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 1145, UUID = 476003142, ExecutionFunction = "ExecuteUbergraph_Widget_TakeDamage", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 2475
        Damage: Const[Ptr[DamageType_FallDamage]] = Cast[DamageType_FallDamage](damageType)
        bSuccess1: bool = Damage
        if not bSuccess1:
            goto('L2601')
        ReturnValue3: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.FallFade, 0, 1, 0, 1)
        goto(ExecutionFlow.Pop())
        # Label 2601
        ReturnValue1_2: bool = Default__KismetSystemLibrary.IsValid(instigatedBy)
        if not ReturnValue1_2:
            goto('L2839')
        ReturnValue_7: Ptr[Pawn] = instigatedBy.K2_GetPawn()
        ReturnValue2_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_7)
        if not ReturnValue2_1:
            goto('L2839')
        ReturnValue_7 = instigatedBy.K2_GetPawn()
        self.mDamageCauser = ReturnValue_7
        goto('L1491')
        # Label 2839
        self.mDamageCauser = damageCauser
        goto('L1491')
        # Label 2863
        ReturnValue_8: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Base: Ptr[FGCharacterBase] = Cast[FGCharacterBase](ReturnValue_8)
        bSuccess: bool = Base
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue_9: Ptr[FGHealthComponent] = Base.GetHealthComponent()
        OutputDelegate.BindUFunction(self, SpawnPointer)
        ReturnValue_9.OnTakeAnyDamageDelegate.AddUnique(OutputDelegate)
        goto(ExecutionFlow.Pop())
        ReturnValue_10: bool = self.IsAnimationPlaying(self.RadiationPulse)
        if not ReturnValue_10:
            goto('L3185')
        # Label 3108
        Default__KismetSystemLibrary.RetriggerableDelay(self, 1, LatentActionInfo(Linkage = 15, UUID = 964063419, ExecutionFunction = "ExecuteUbergraph_Widget_TakeDamage", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 3185
        self.mRadiation.SetVisibility(3)
        ReturnValue1_3: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.RadiationPulse, 0, 0, 0, 1)
        goto('L3108')
        goto('L2863')
        
        IsHealthCritical2 = None
        self.GetIsHealthCritical(Ref[IsHealthCritical2])
        if not IsHealthCritical2:
            goto('L3393')
        ReturnValue1_4: bool = self.IsAnimationPlaying(self.CriticalHealth)
        ReturnValue_11: bool = Not_PreBool(ReturnValue1_4)
        if not ReturnValue_11:
            goto('L127')
        goto('L81')
        # Label 3393
        self.StopAnimation(self.CriticalHealth)
        goto('L127')
        Variable_2: uint8 = 2
        Variable1_1: uint8 = 3
        Variable2: bool = RadiationActive
        
        switch_2 = {
            False: Variable_2,
            True: Variable1_1
        }
        self.mRadiationWarning.SetVisibility(switch_2.get(Variable2, None))
        ReturnValue_12: float = Ease(0.029999999329447746, 1, amount, 6, 20, 2)
        self.mRadationAmount.mProgressBar.SetPercent(ReturnValue_12)
        goto(ExecutionFlow.Pop())
    
