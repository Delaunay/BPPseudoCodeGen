
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_SmelterBasicMk1(FGRecipe):
    mDisplayName = NSLOCTEXT("", "4606ADA9430421B2F4213D95D5512D35", "Smelter")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 8}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/SmelterMk1/Desc_SmelterMk1.Desc_SmelterMk1_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
