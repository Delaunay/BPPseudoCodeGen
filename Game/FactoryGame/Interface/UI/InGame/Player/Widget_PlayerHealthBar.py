
from codegen.ue4_stub import *

from Script.FactoryGame import FGHealthComponent
from Script.FactoryGame import GetHealthComponent
from Script.Engine import Delay
from Script.Engine import FClamp
from Script.Engine import K2_SetTimerDelegate
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Pawn
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_PlayerHealthBar import ExecuteUbergraph_Widget_PlayerHealthBar.K2Node_Event_InDeltaTime
from Script.Engine import MapRangeUnclamped
from Script.UMG import GetEndTime
from Script.FactoryGame import IsDead
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import K2_GetPawn
from Script.UMG import PlayAnimation
from Script.UMG import ESlateVisibility
from Script.Engine import TimerHandle
from Script.UMG import StopAnimation
from Script.Engine import IsValid
from Script.FactoryGame import GetDriver
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_PlayerHealthBar import ExecuteUbergraph_Widget_PlayerHealthBar
from Script.FactoryGame import FGVehicle
from Script.UMG import SetFillColorAndOpacity
from Script.UMG import Construct
from Script.Engine import NotEqual_FloatFloat
from Script.UMG import Tick
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_PlayerHealthBar import ExecuteUbergraph_Widget_PlayerHealthBar.K2Node_Event_MyGeometry
from Script.Engine import LinearColorLerp
from Script.UMG import WidgetAnimation
from Script.FactoryGame import GetCurrentHealth
from Script.UMG import UserWidget
from Script.UMG import UMGSequencePlayer
from Script.FactoryGame import GetMaxHealth
from Script.CoreUObject import LinearColor

class Widget_PlayerHealthBar(UserWidget):
    beep_boop: Ptr[WidgetAnimation]
    RadiationStop: Ptr[WidgetAnimation]
    RadiationDamage: Ptr[WidgetAnimation]
    Ani_Damage: Ptr[WidgetAnimation]
    mCachedHealth: float
    mBaseHPBarColor: LinearColor = Namespace(A=1, B=1, G=1, R=1)
    mPlayerHealthComponent: Ptr[FGHealthComponent]
    mAmountOfHealthPerChunk: float = 10
    IsVehicleHud: bool
    mCharacterPlayer: Ptr[FGCharacterPlayer]
    
    def GetHealthFillColor(self):
        
        valid = None
        self.IsValidHealthComponent(Ref[valid])
        if not valid:
            goto('L266')
        ReturnValue: float = self.mPlayerHealthComponent.GetCurrentHealth()
        ReturnValue_0: float = FClamp(ReturnValue, 0, 1)
        ReturnValue_1: LinearColor = LinearColorLerp(LinearColor(R = 0.838798999786377, G = 0.8713669776916504, B = 0.887923002243042, A = 1), LinearColor(R = 1, G = 1, B = 1, A = 1), ReturnValue_0)
        ReturnValue_2: LinearColor = ReturnValue_1
    

    def IsValidHealthComponent(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mPlayerHealthComponent)
        if not ReturnValue:
            goto('L155')
        ReturnValue_0: bool = self.mPlayerHealthComponent.IsDead()
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        valid: bool = ReturnValue_1
        # Label 155
        Valid = valid
    

    def GetHealthbar(self):
        visibility: uint8 = 2
    

    def GetProgressbarPercent(self):
        
        valid = None
        self.IsValidHealthComponent(Ref[valid])
        if not valid:
            goto('L215')
        ReturnValue: float = self.mPlayerHealthComponent.GetCurrentHealth()
        ReturnValue_0: float = self.mPlayerHealthComponent.GetMaxHealth()
        ReturnValue_1: float = ReturnValue / ReturnValue_0
        ReturnValue_2: float = ReturnValue_1
        goto('L238')
        # Label 215
        ReturnValue_2 = 0
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_PlayerHealthBar(2119)
    

    def Tick(self):
        ExecuteUbergraph_Widget_PlayerHealthBar.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_PlayerHealthBar.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PlayerHealthBar(847)
    

    def ResetAnimGate(self):
        self.ExecuteUbergraph_Widget_PlayerHealthBar(2091)
    

    def SetupHealthComponent(self):
        self.ExecuteUbergraph_Widget_PlayerHealthBar(2114)
    

    def ExecuteUbergraph_Widget_PlayerHealthBar(self):
        goto(ComputedJump("EntryPoint"))
        self.SetupHealthComponent()
        goto(ExecutionFlow.Pop())
        # Label 30
        if not self.IsVehicleHud:
            goto('L400')
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[Pawn] = ReturnValue1.K2_GetPawn()
        AsFGVehicle: Ptr[FGVehicle] = Cast[FGVehicle](ReturnValue1_0)
        bSuccess1: bool = AsFGVehicle
        if not bSuccess1:
            goto('L684')
        ReturnValue: Ptr[FGCharacterPlayer] = AsFGVehicle.GetDriver()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L684')
        ReturnValue = AsFGVehicle.GetDriver()
        ReturnValue1_1: Ptr[FGHealthComponent] = ReturnValue.GetHealthComponent()
        self.mPlayerHealthComponent = ReturnValue1_1
        goto(ExecutionFlow.Pop())
        # Label 400
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[Pawn] = ReturnValue_1.K2_GetPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_2)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L607')
        ReturnValue_3: Ptr[FGHealthComponent] = Player.GetHealthComponent()
        self.mPlayerHealthComponent = ReturnValue_3
        goto(ExecutionFlow.Pop())
        # Label 607
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 15, UUID = -1458383184, ExecutionFunction = "ExecuteUbergraph_Widget_PlayerHealthBar", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 684
        Default__KismetSystemLibrary.Delay(self, 0.20000000298023224, LatentActionInfo(Linkage = 761, UUID = 1048239902, ExecutionFunction = "ExecuteUbergraph_Widget_PlayerHealthBar", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.SetupHealthComponent()
        goto(ExecutionFlow.Pop())
        # Label 776
        self.Construct()
        self.SetupHealthComponent()
        ReturnValue1_2: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.RadiationDamage, 0, 0, 0, 1)
        goto(ExecutionFlow.Pop())
        self.Tick(MyGeometry, InDeltaTime)
        
        valid = None
        self.IsValidHealthComponent(Ref[valid])
        if not valid:
            goto('L1836')
        ReturnValue_4: float = self.mPlayerHealthComponent.GetMaxHealth()
        ReturnValue_5: float = self.mPlayerHealthComponent.GetCurrentHealth()
        ReturnValue_6: float = MapRangeUnclamped(ReturnValue_5, 0, ReturnValue_4, 0, 100)
        ReturnValue_7: bool = NotEqual_FloatFloat(self.mCachedHealth, ReturnValue_6)
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        ReturnValue_4 = self.mPlayerHealthComponent.GetMaxHealth()
        ReturnValue_5 = self.mPlayerHealthComponent.GetCurrentHealth()
        ReturnValue_6 = MapRangeUnclamped(ReturnValue_5, 0, ReturnValue_4, 0, 100)
        self.mCachedHealth = ReturnValue_6
        ReturnValue_4 = self.mPlayerHealthComponent.GetMaxHealth()
        ReturnValue_5 = self.mPlayerHealthComponent.GetCurrentHealth()
        ReturnValue_6 = MapRangeUnclamped(ReturnValue_5, 0, ReturnValue_4, 0, 100)
        ReturnValue_8: bool = ReturnValue_6 <= 30
        if not ReturnValue_8:
            goto('L1538')
        ExecutionFlow.Push("L1851")
        if not Variable:
            goto('L2066')
        goto(ExecutionFlow.Pop())
        # Label 1538
        self.StopAnimation(self.Ani_Damage)
        ReturnValue_4 = self.mPlayerHealthComponent.GetMaxHealth()
        ReturnValue_5 = self.mPlayerHealthComponent.GetCurrentHealth()
        ReturnValue_6 = MapRangeUnclamped(ReturnValue_5, 0, ReturnValue_4, 0, 100)
        ReturnValue_9: bool = ReturnValue_6 > 30.010000228881836
        if not ReturnValue_9:
           goto(ExecutionFlow.Pop())
        ReturnValue_10: LinearColor = self.GetHealthFillColor()
        self.ProgressBarHealth.SetFillColorAndOpacity(ReturnValue_10)
        goto(ExecutionFlow.Pop())
        # Label 1836
        self.SetupHealthComponent()
        goto(ExecutionFlow.Pop())
        # Label 1851
        if not Variable:
            goto('L1866')
        goto(ExecutionFlow.Pop())
        # Label 1866
        Variable: bool = True
        ReturnValue_11: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.Ani_Damage, 0, 0, 0, 0.800000011920929)
        OutputDelegate.BindUFunction(self, ResetAnimGate)
        ReturnValue_12: float = self.Ani_Damage.GetEndTime()
        ReturnValue_13: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, ReturnValue_12, False)
        goto(ExecutionFlow.Pop())
        # Label 2066
        Variable = True
        if not False:
           goto(ExecutionFlow.Pop())
        Variable = True
        goto(ExecutionFlow.Pop())
        Variable = False
        Variable = True
        goto(ExecutionFlow.Pop())
        goto('L30')
        goto('L776')
    
