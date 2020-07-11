
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_HeavyOilResidue(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "D8AD88004853C966477FCFB5CE60D73C", "Alternate: Heavy Oil Residue")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/CrudeOil/Desc_LiquidOil.Desc_LiquidOil_C', 'amount': 3000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HeavyOilResidue/Desc_HeavyOilResidue.Desc_HeavyOilResidue_C', 'amount': 4000}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/PolymerResin/Desc_PolymerResin.Desc_PolymerResin_C', 'amount': 2}]
    mManufactoringDuration = 6
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
