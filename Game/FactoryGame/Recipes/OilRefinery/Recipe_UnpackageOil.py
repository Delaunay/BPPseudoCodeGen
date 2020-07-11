
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_UnpackageOil(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "5DC37DA94F79851924D6FCB7EF4A6D32", "Unpackage Oil")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/CrudeOil/Desc_PackagedOil.Desc_PackagedOil_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/CrudeOil/Desc_LiquidOil.Desc_LiquidOil_C', 'amount': 2000}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/FluidCanister/Desc_FluidCanister.Desc_FluidCanister_C', 'amount': 2}]
    mManufactoringDuration = 2
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
