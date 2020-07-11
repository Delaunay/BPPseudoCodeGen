
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Foundation_8x1_01(FGRecipe):
    mDisplayName = NSLOCTEXT("", "6196F47D4A927C899F24AC9138504B2D", "Foundation 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 6}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Foundation/Desc_Foundation_8x1_01.Desc_Foundation_8x1_01_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
