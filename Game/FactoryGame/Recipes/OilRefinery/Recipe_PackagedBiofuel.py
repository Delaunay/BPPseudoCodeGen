
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PackagedBiofuel(FGRecipe):
    mDisplayName = NSLOCTEXT("", "8CADC224429A0060BF416783C132484D", "Fuel")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/BioFuel/Desc_LiquidBiofuel.Desc_LiquidBiofuel_C', 'amount': 2000}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/FluidCanister/Desc_FluidCanister.Desc_FluidCanister_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/BioFuel/Desc_PackagedBiofuel.Desc_PackagedBiofuel_C', 'amount': 2}]
    mManufactoringDuration = 3
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
