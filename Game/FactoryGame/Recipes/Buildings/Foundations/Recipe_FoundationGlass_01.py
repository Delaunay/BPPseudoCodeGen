
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_FoundationGlass_01(FGRecipe):
    mDisplayName = NSLOCTEXT("", "0868403A4B11F84E983CA58953EE3F6B", "Foundation 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 6}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Foundation/Desc_FoundationGlass_01.Desc_FoundationGlass_01_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
