
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_ConstructorMk1(FGRecipe):
    mDisplayName = NSLOCTEXT("", "C55B457D44ED9C4440647CB57CED5AE4", "Simple Constructor")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 8}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Desc_ConstructorMk1.Desc_ConstructorMk1_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
