
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_ResidualFuel(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "E248112349744FD51F8ADBA297846679", "Residual Fuel")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HeavyOilResidue/Desc_HeavyOilResidue.Desc_HeavyOilResidue_C', 'amount': 6000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Fuel/Desc_LiquidFuel.Desc_LiquidFuel_C', 'amount': 4000}]
    mManufactoringDuration = 6
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
