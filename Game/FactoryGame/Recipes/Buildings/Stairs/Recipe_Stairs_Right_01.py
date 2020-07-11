
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Stairs_Right_01(FGRecipe):
    mDisplayName = NSLOCTEXT("", "C037515B497E474060EF919F0C9EC336", "Stair 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 4}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Stair/Desc_Stairs_Right_01.Desc_Stairs_Right_01_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
