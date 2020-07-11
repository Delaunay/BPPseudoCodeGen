
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PillarMiddle(FGRecipe):
    mDisplayName = NSLOCTEXT("", "ECF210E044D65F7A63FE1EA5C640535D", "Foundation 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 6}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Foundation/Desc_PillarMiddle.Desc_PillarMiddle_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
