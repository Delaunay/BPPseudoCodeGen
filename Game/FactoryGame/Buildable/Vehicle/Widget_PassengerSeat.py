
from codegen.ue4_stub import *

from Script.Engine import PlayerController
from Script.UMG import UserWidget
from Script.FactoryGame import SetShowCrossHair
from Script.FactoryGame import FGPlayerController
from Game.FactoryGame.Buildable.Vehicle.Widget_PassengerSeat import ExecuteUbergraph_Widget_PassengerSeat
from Script.Engine import GetHUD
from Script.FactoryGame import FGHUD
from Script.Engine import HUD

class Widget_PassengerSeat(UserWidget):
    
    
    def Construct(self):
        self.ExecuteUbergraph_Widget_PassengerSeat(272)
    

    def ExecuteUbergraph_Widget_PassengerSeat(self):
        # Label 10
        ReturnValue: Ptr[PlayerController] = self.GetOwningPlayer()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L277')
        ReturnValue_0: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_0)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
            goto('L277')
        AsFGHUD.SetShowCrossHair(False)
        # End
        goto('L10')
    
