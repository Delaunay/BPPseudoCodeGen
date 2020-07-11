
from codegen.ue4_stub import *

from Script.UMG import GetOwningPlayerPawn
from Game.FactoryGame.Equipment.C4Dispenser.Equip_C4Dispenser import Equip_C4Dispenser
from Script.UMG import ESlateVisibility
from Script.FactoryGame import GetEquipmentInSlot
from Game.FactoryGame.Character.Player.Char_Player import Char_Player
from Script.Engine import Pawn
from Script.FactoryGame import FGEquipment
from Script.Engine import LinearColorLerp
from Script.FactoryGame import GetChargePct
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class Widget_C4Dispenser(UserWidget):
    
    
    def Get_mC4Throwbar_Visibility_0(self):
        Variable: uint8 = 0
        Variable1: uint8 = 2
        ReturnValue: float = self.GetThrowPercent()
        ReturnValue_0: bool = ReturnValue > 0
        Variable_0: bool = ReturnValue_0
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_1: uint8 = switch.get(Variable_0, None)
    

    def Get_mC4Throwbar_FillColorAndOpacity_0(self):
        ReturnValue: float = self.GetThrowPercent()
        ReturnValue_0: LinearColor = LinearColorLerp(LinearColor(R = 0, G = 1, B = 0, A = 1), LinearColor(R = 1, G = 0, B = 0, A = 1), ReturnValue)
        ReturnValue_1: LinearColor = ReturnValue_0
    

    def GetThrowPercent(self):
        ReturnValue: Ptr[Pawn] = self.GetOwningPlayerPawn()
        Player: Ptr[Char_Player] = Cast[Char_Player](ReturnValue)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L304')
        ReturnValue_0: Ptr[FGEquipment] = Player.GetEquipmentInSlot(1)
        C4Dispenser: Ptr[Equip_C4Dispenser] = Cast[Equip_C4Dispenser](ReturnValue_0)
        bSuccess1: bool = C4Dispenser
        if not bSuccess1:
            goto('L332')
        ReturnValue_1: float = C4Dispenser.GetChargePct()
        ReturnValue_2: float = ReturnValue_1
        goto('L355')
        # Label 304
        ReturnValue_2 = 0
        goto('L355')
        # Label 332
        ReturnValue_2 = 0
    
