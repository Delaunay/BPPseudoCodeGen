
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PetroleumCoke(FGRecipe):
    mDisplayName = NSLOCTEXT("", "025E1A4D4BE6F0149396D1BFBA4C9895", "Petroleum Coke")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HeavyOilResidue/Desc_HeavyOilResidue.Desc_HeavyOilResidue_C', 'amount': 4000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/PetroleumCoke/Desc_PetroleumCoke.Desc_PetroleumCoke_C', 'amount': 12}]
    mManufactoringDuration = 6
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
