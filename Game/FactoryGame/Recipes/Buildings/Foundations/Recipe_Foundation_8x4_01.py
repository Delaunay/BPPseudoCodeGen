
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Foundation_8x4_01(FGRecipe):
    mDisplayName = NSLOCTEXT("", "4CB64EA14AEC1E4E2EF846816B7EEF2B", "Foundation 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 6}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Foundation/Desc_Foundation_8x4_01.Desc_Foundation_8x4_01_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
