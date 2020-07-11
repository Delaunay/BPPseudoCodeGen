
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Fuel(FGRecipe):
    mDisplayName = NSLOCTEXT("", "8CADC224429A0060BF416783C132484D", "Fuel")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Fuel/Desc_LiquidFuel.Desc_LiquidFuel_C', 'amount': 2000}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/FluidCanister/Desc_FluidCanister.Desc_FluidCanister_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Fuel/Desc_Fuel.Desc_Fuel_C', 'amount': 2}]
    mManufactoringDuration = 3
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
