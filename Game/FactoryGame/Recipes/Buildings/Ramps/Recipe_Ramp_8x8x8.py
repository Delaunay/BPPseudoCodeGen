
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Ramp_8x8x8(FGRecipe):
    mDisplayName = NSLOCTEXT("", "416465414787DD64C46753AEC936706C", "Ramp 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Ramp/Desc_Ramp_8x8x8.Desc_Ramp_8x8x8_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
