
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Chainsaw(FGRecipe):
    mDisplayName = NSLOCTEXT("", "E0DFCEAF495FE4479570BFB1BB603C7C", "Space Rifle")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 25}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronScrew/Desc_IronScrew.Desc_IronScrew_C', 'amount': 160}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 15}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Equipment/Chainsaw/Desc_Chainsaw.Desc_Chainsaw_C', 'amount': 1}]
    mManufactoringDuration = 60
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
