
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Wall_Door_8x4_03_Steel(FGRecipe):
    mDisplayName = NSLOCTEXT("", "98EF2A0A4E78ED06C284BB92479A6A58", "Wall 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 3}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Wall/Desc_Wall_Door_8x4_03_Steel.Desc_Wall_Door_8x4_03_Steel_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
