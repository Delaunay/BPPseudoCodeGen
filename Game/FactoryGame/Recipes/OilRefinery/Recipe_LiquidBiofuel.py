
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_LiquidBiofuel(FGRecipe):
    mDisplayName = NSLOCTEXT("", "8CADC224429A0060BF416783C132484D", "Fuel")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/BioFuel/Desc_Biofuel.Desc_Biofuel_C', 'amount': 6}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Water/Desc_Water.Desc_Water_C', 'amount': 3000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/BioFuel/Desc_LiquidBiofuel.Desc_LiquidBiofuel_C', 'amount': 4000}]
    mManufactoringDuration = 4
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
