
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_RampInverted_8x1_Corner_01(FGRecipe):
    mDisplayName = NSLOCTEXT("", "41184C6747A9C74969A37B8354BC96E6", "Ramp 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Ramp/Desc_RampInverted_8x1_Corner_01.Desc_RampInverted_8x1_Corner_01_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
