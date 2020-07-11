
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Ramp_Diagonal_8x2_02(FGRecipe):
    mDisplayName = NSLOCTEXT("", "1588094C4509D9596A9C4EBFD293C36B", "Ramp 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 3}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Ramp/Desc_Ramp_Diagonal_8x2_02.Desc_Ramp_Diagonal_8x2_02_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
