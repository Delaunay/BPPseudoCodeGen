
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_SteamedCopperSheet(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "5BF0D56049240670A1C59ABA221A2850", "Alternate: Steamed Copper Sheet")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperIngot/Desc_CopperIngot.Desc_CopperIngot_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Water/Desc_Water.Desc_Water_C', 'amount': 3000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperSheet/Desc_CopperSheet.Desc_CopperSheet_C', 'amount': 3}]
    mManufactoringDuration = 8
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
