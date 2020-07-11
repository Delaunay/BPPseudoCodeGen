
from codegen.ue4_stub import *

from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Pawn
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_TakeDamageIndicator import ExecuteUbergraph_Widget_TakeDamageIndicator
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_TakeDamageIndicator import ExecuteUbergraph_Widget_TakeDamageIndicator.K2Node_Event_InDeltaTime
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.InGame.Player.Widget_TakeDamageIndicator import ExecuteUbergraph_Widget_TakeDamageIndicator.K2Node_Event_MyGeometry
from Script.Engine import IsValid
from Script.UMG import SetColorAndOpacity
from Script.Engine import DegAtan2
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.Engine import Normal
from Script.UMG import SetRenderAngle
from Script.UMG import WidgetAnimation
from Script.UMG import UserWidget
from Script.UMG import GetOwningPlayerPawn
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Script.UMG import UMGSequencePlayer
from Script.Engine import Multiply_VectorVector
from Script.FactoryGame import GetRadiationDamageAngle
from Script.Engine import GetActorForwardVector
from Script.CoreUObject import LinearColor

class Widget_TakeDamageIndicator(UserWidget):
    FadeOutAnim: Ptr[WidgetAnimation]
    DamageCauser: Ptr[Actor]
    mColor: LinearColor
    mDamagePosition: Vector
    mPlayerPosition: Vector
    mIsRadiation: bool
    
    def SetRotation(self):
        ReturnValue2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue2)
        if not ReturnValue1:
            goto('L182')
        ReturnValue2 = self.GetOwningPlayerPawn()
        ReturnValue1_0: Vector = ReturnValue2.K2_GetActorLocation()
        self.mPlayerPosition = ReturnValue1_0
        # Label 182
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.DamageCauser)
        if not ReturnValue:
            goto('L324')
        ReturnValue_0: Vector = self.DamageCauser.K2_GetActorLocation()
        self.mDamagePosition = ReturnValue_0
        # Label 324
        ReturnValue_1: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_1)
        bSuccess: bool = Player
        ReturnValue_2: float = Player.GetRadiationDamageAngle()
        ReturnValue_3: Vector = Multiply_VectorVector(self.mPlayerPosition, Vector(1, 1, 0))
        Variable: bool = self.mIsRadiation
        ReturnValue1_1: Vector = Multiply_VectorVector(self.mDamagePosition, Vector(1, 1, 0))
        ReturnValue1_2: Ptr[Pawn] = self.GetOwningPlayerPawn()
        ReturnValue_4: Vector = Subtract_VectorVector(ReturnValue1_1, ReturnValue_3)
        ReturnValue_5: Vector = ReturnValue1_2.GetActorForwardVector()
        ReturnValue_6: Vector = Normal(ReturnValue_4, 9.999999747378752e-05)
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_5)
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(ReturnValue_6)
        ReturnValue_7: float = DegAtan2(Y, X)
        ReturnValue1_3: float = DegAtan2(Y1, X1)
        ReturnValue_8: float = ReturnValue1_3 - ReturnValue_7
        
        switch = {
            False: ReturnValue_8,
            True: ReturnValue_2
        }
        self.Image_0.SetRenderAngle(switch.get(Variable, None))
    

    def DestroySelf(self):
        self.ExecuteUbergraph_Widget_TakeDamageIndicator(29)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_TakeDamageIndicator(48)
    

    def Tick(self):
        ExecuteUbergraph_Widget_TakeDamageIndicator.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_TakeDamageIndicator.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_TakeDamageIndicator(140)
    

    def ExecuteUbergraph_Widget_TakeDamageIndicator(self):
        # Label 10
        self.SetRotation()
        # End
        self.RemoveFromParent()
        # End
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.FadeOutAnim, 0, 1, 0, 1)
        self.Image_0.SetColorAndOpacity(self.mColor)
        # End
        goto('L10')
    
