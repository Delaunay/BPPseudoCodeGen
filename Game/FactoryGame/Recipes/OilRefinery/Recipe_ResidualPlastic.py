
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_ResidualPlastic(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "001749B0473C86E14F557CB319B8F27C", "Residual Plastic")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/PolymerResin/Desc_PolymerResin.Desc_PolymerResin_C', 'amount': 6}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Water/Desc_Water.Desc_Water_C', 'amount': 2000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Plastic/Desc_Plastic.Desc_Plastic_C', 'amount': 2}]
    mManufactoringDuration = 6
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
