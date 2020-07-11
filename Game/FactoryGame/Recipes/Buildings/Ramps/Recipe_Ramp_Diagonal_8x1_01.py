
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Ramp_Diagonal_8x1_01(FGRecipe):
    mDisplayName = NSLOCTEXT("", "AC4BE28D46F563DCD4A0E693447A71AA", "Ramp 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Ramp/Desc_Ramp_Diagonal_8x1_01.Desc_Ramp_Diagonal_8x1_01_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
