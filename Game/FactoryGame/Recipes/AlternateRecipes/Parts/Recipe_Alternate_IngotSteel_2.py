
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_IngotSteel_2(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "CDB4FF9D43032E0075B3CA90F29E2526", "Alternate: Compacted Steel Ingot")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/OreIron/Desc_OreIron.Desc_OreIron_C', 'amount': 6}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CompactedCoal/Desc_CompactedCoal.Desc_CompactedCoal_C', 'amount': 3}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelIngot/Desc_SteelIngot.Desc_SteelIngot_C', 'amount': 10}]
    mManufactoringDuration = 16
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/FoundryMk1/Build_FoundryMk1.Build_FoundryMk1_C']
    
