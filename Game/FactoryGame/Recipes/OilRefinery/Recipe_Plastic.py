
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Plastic(FGRecipe):
    mDisplayName = NSLOCTEXT("", "108B10684CCFEEF3B568199A7235858B", "Plastic")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/CrudeOil/Desc_LiquidOil.Desc_LiquidOil_C', 'amount': 3000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Plastic/Desc_Plastic.Desc_Plastic_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/HeavyOilResidue/Desc_HeavyOilResidue.Desc_HeavyOilResidue_C', 'amount': 1000}]
    mManufactoringDuration = 6
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
