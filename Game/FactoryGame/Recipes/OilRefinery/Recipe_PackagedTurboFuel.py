
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PackagedTurboFuel(FGRecipe):
    mDisplayName = NSLOCTEXT("", "C024DE534E580F0C4506D8A5A0778593", "Packaged Turbofuel")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Turbofuel/Desc_LiquidTurboFuel.Desc_LiquidTurboFuel_C', 'amount': 2000}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/FluidCanister/Desc_FluidCanister.Desc_FluidCanister_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Turbofuel/Desc_TurboFuel.Desc_TurboFuel_C', 'amount': 2}]
    mManufactoringDuration = 6
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
