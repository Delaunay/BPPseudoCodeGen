
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_LookoutTower(FGRecipe):
    mDisplayName = NSLOCTEXT("", "4606ADA9430421B2F4213D95D5512D35", "Smelter")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/LookoutTower/Desc_LookoutTower.Desc_LookoutTower_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
