
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Ramp_Diagonal_8x4_02(FGRecipe):
    mDisplayName = NSLOCTEXT("", "F1E0894B4D0620566F24CAA5C61B4798", "Ramp 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 4}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Ramp/Desc_Ramp_Diagonal_8x4_02.Desc_Ramp_Diagonal_8x4_02_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
