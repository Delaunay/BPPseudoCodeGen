﻿
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_RampDouble(FGRecipe):
    mDisplayName = NSLOCTEXT("", "86497419485E968C396937902AE6DAA5", "Ramp 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Ramp/Desc_RampDouble.Desc_RampDouble_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
