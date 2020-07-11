
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_TurboHeavyFuel(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "4603298348EFC73D75CF14B359B63FCA", "Alternate: Turbo Heavy Fuel")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HeavyOilResidue/Desc_HeavyOilResidue.Desc_HeavyOilResidue_C', 'amount': 5000}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CompactedCoal/Desc_CompactedCoal.Desc_CompactedCoal_C', 'amount': 4}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Turbofuel/Desc_LiquidTurboFuel.Desc_LiquidTurboFuel_C', 'amount': 4000}]
    mManufactoringDuration = 8
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
