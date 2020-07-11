
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PillarBase(FGRecipe):
    mDisplayName = NSLOCTEXT("", "423E3FDD42751C326AC71A9C51C5485B", "Foundation 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 6}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Foundation/Desc_PillarBase.Desc_PillarBase_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
