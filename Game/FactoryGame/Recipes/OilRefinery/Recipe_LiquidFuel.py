
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_LiquidFuel(FGRecipe):
    mDisplayName = NSLOCTEXT("", "8CADC224429A0060BF416783C132484D", "Fuel")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/CrudeOil/Desc_LiquidOil.Desc_LiquidOil_C', 'amount': 6000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Fuel/Desc_LiquidFuel.Desc_LiquidFuel_C', 'amount': 4000}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/PolymerResin/Desc_PolymerResin.Desc_PolymerResin_C', 'amount': 3}]
    mManufactoringDuration = 6
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
