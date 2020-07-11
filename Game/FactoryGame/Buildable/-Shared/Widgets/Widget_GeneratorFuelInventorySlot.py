
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetFuelAmount
from Script.FactoryGame import FGBuildableGeneratorFuel
from Script.FactoryGame import GetFuelInventory
from Script.FactoryGame import FGInventoryComponent
from Script.Engine import IsValid
from Script.UMG import UserWidget

class Widget_GeneratorFuelInventorySlot(UserWidget):
    mGenerator: Ptr[FGBuildableGeneratorFuel]
    
    def Init(self, Generator: Ptr[FGBuildableGeneratorFuel]):
        self.mGenerator = Generator
        ReturnValue: Ptr[FGInventoryComponent] = self.mGenerator.GetFuelInventory()
        self.Widget_InventorySlot.mCachedInventoryComponent = ReturnValue
    

    def GetFuelPercent(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mGenerator)
        if not ReturnValue:
            goto('L147')
        ReturnValue_0: float = self.mGenerator.GetFuelAmount()
        ReturnValue_1: float = ReturnValue_0
        goto('L170')
        # Label 147
        ReturnValue_1 = 0
    
