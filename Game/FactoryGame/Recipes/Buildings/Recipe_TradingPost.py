
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_TradingPost(FGRecipe):
    mDisplayName = NSLOCTEXT("", "447F2B8C46BB3ACAB2A847A41C34470E", "Trading Post")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HUBParts/Desc_HUBParts.Desc_HUBParts_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/TradingPost/Desc_TradingPost.Desc_TradingPost_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
