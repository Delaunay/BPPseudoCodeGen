
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_RampDouble_8x1(FGRecipe):
    mDisplayName = NSLOCTEXT("", "6455ADB6498550484F1CF288F2639AE7", "Ramp 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Ramp/Desc_RampDouble_8x1.Desc_RampDouble_8x1_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
