
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_WetConcrete(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "773DC4634D5F48893A8860B32264B05B", "Alternate: Wet Concrete")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/Stone/Desc_Stone.Desc_Stone_C', 'amount': 6}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Water/Desc_Water.Desc_Water_C', 'amount': 5000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 4}]
    mManufactoringDuration = 3
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
