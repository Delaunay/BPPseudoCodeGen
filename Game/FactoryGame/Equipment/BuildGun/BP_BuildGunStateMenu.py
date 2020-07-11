
from codegen.ue4_stub import *

from Script.FactoryGame import FGPlayerController
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Controller
from Script.FactoryGame import FGBuildGunState
from Script.FactoryGame import GetInstigatorCharacter
from Script.Engine import Pawn
from Script.Engine import GetInstigator
from Script.Engine import HUD
from Script.Engine import GetController
from Script.FactoryGame import FGBuildSubCategory
from Script.FactoryGame import IsLocalInstigator
from Script.Engine import GetHUD
from Game.FactoryGame.Equipment.BuildGun.BP_BuildGunStateMenu import ExecuteUbergraph_BP_BuildGunStateMenu
from Script.FactoryGame import ToggleBuildGun
from Script.FactoryGame import GetGameUI
from Script.FactoryGame import EndState
from Script.FactoryGame import GetBuildGun
from Script.FactoryGame import FGHUD
from Script.FactoryGame import FGGameUI
from Script.FactoryGame import FGBuildGun
from Script.FactoryGame import FGBuildCategory
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.Prototype.Widget_BuildMenu import Widget_BuildMenu
from Script.FactoryGame import SecondaryFire
from Script.FactoryGame import BeginState

class BP_BuildGunStateMenu(FGBuildGunState):
    mLastSelectedBuildCategory: TSubclassOf[FGBuildCategory] = NewObject[BC_TradingPost]()
    mLastSelectedSubCategories: List[TSubclassOf[FGBuildSubCategory]]
    
    def EndState(self):
        self.ExecuteUbergraph_BP_BuildGunStateMenu(473)
    

    def SecondaryFire(self):
        self.ExecuteUbergraph_BP_BuildGunStateMenu(488)
    

    def BeginState(self):
        self.ExecuteUbergraph_BP_BuildGunStateMenu(673)
    

    def ExecuteUbergraph_BP_BuildGunStateMenu(self):
        # Label 10
        ReturnValue: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue_0: bool = ReturnValue.IsLocalInstigator()
        if not ReturnValue_0:
            goto('L1109')
        ReturnValue = self.GetBuildGun()
        ReturnValue_1: Ptr[Pawn] = ReturnValue.GetInstigator()
        ReturnValue_2: Ptr[Controller] = ReturnValue_1.GetController()
        Controller: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue_2)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L1109')
        ReturnValue_3: Ptr[HUD] = Controller.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue_3)
        bSuccess1: bool = AsFGHUD
        if not bSuccess1:
            goto('L1109')
        ReturnValue_4: Ptr[FGGameUI] = AsFGHUD.GetGameUI()
        ReturnValue_4.PopAllWidgets()
        # End
        self.EndState()
        goto('L10')
        self.SecondaryFire()
        ReturnValue1: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue1_0: bool = ReturnValue1.IsLocalInstigator()
        if not ReturnValue1_0:
            goto('L1109')
        ReturnValue1 = self.GetBuildGun()
        ReturnValue_5: Ptr[FGCharacterPlayer] = ReturnValue1.GetInstigatorCharacter()
        ReturnValue_5.ToggleBuildGun()
        # End
        self.BeginState()
        ReturnValue2: Ptr[FGBuildGun] = self.GetBuildGun()
        ReturnValue2_0: bool = ReturnValue2.IsLocalInstigator()
        if not ReturnValue2_0:
            goto('L1109')
        ReturnValue2 = self.GetBuildGun()
        ReturnValue1_1: Ptr[Pawn] = ReturnValue2.GetInstigator()
        ReturnValue1_2: Ptr[Controller] = ReturnValue1_1.GetController()
        Controller1: Ptr[FGPlayerController] = Cast[FGPlayerController](ReturnValue1_2)
        bSuccess2: bool = Controller1
        if not bSuccess2:
            goto('L1109')
        ReturnValue1_3: Ptr[HUD] = Controller1.GetHUD()
        AsFGHUD1: Ptr[FGHUD] = Cast[FGHUD](ReturnValue1_3)
        bSuccess3: bool = AsFGHUD1
        if not bSuccess3:
            goto('L1109')
        AsFGHUD1.OpenInteractUI(Widget_BuildMenu, self)
    
