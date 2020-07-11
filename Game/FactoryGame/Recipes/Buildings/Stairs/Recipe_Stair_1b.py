
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Stair_1b(FGRecipe):
    mDisplayName = NSLOCTEXT("", "C46AA59748505BC3D87B4DBD36BD444A", "Stair 2")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 4}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Stair/Desc_Stair_1b.Desc_Stair_1b_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
