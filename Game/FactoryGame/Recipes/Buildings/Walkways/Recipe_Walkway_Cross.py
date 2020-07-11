
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Walkway_Cross(FGRecipe):
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Walkway/Desc_WalkwayCross.Desc_WalkwayCross_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
