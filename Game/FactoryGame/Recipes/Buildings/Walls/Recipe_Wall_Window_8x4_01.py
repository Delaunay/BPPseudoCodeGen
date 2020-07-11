﻿
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Wall_Window_8x4_01(FGRecipe):
    mDisplayName = NSLOCTEXT("", "03C87EB8434E950EE50E6593BF258F6B", "Wall 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 3}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Wall/Desc_Wall_Window_8x4_01.Desc_Wall_Window_8x4_01_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
