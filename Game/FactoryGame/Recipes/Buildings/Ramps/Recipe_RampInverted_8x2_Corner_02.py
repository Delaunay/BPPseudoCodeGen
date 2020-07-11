
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_RampInverted_8x2_Corner_02(FGRecipe):
    mDisplayName = NSLOCTEXT("", "1EF16A4142E7824391D82BAC2496FD36", "Ramp 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Ramp/Desc_RampInverted_8x2_Corner_02.Desc_RampInverted_8x2_Corner_02_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
