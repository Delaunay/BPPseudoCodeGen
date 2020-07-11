
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_ResidualRubber(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "867CC5AA487AF45910B20DBF284B06B1", "Residual Rubber")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/PolymerResin/Desc_PolymerResin.Desc_PolymerResin_C', 'amount': 4}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Water/Desc_Water.Desc_Water_C', 'amount': 4000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 2}]
    mManufactoringDuration = 6
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
