
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_Turbofuel(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "E761FCD14330188C6E8999A166A4A1DC", "Turbofuel")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Fuel/Desc_LiquidFuel.Desc_LiquidFuel_C', 'amount': 6000}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CompactedCoal/Desc_CompactedCoal.Desc_CompactedCoal_C', 'amount': 4}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Turbofuel/Desc_LiquidTurboFuel.Desc_LiquidTurboFuel_C', 'amount': 5000}]
    mManufactoringDuration = 16
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
