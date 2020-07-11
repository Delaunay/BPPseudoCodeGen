
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_PolymerResin(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "A57542EA4A191D2F892D92A511685DB8", "Alternate: Polymer Resin")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/CrudeOil/Desc_LiquidOil.Desc_LiquidOil_C', 'amount': 6000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/PolymerResin/Desc_PolymerResin.Desc_PolymerResin_C', 'amount': 13}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/HeavyOilResidue/Desc_HeavyOilResidue.Desc_HeavyOilResidue_C', 'amount': 2000}]
    mManufactoringDuration = 6
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
