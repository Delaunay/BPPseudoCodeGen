
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_CokeSteelIngot(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "3FA6E6204EF22BB3ACD3C293912B8402", "Alternate: Coke Steel Ingot")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/OreIron/Desc_OreIron.Desc_OreIron_C', 'amount': 15}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/PetroleumCoke/Desc_PetroleumCoke.Desc_PetroleumCoke_C', 'amount': 15}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelIngot/Desc_SteelIngot.Desc_SteelIngot_C', 'amount': 20}]
    mManufactoringDuration = 12
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/FoundryMk1/Build_FoundryMk1.Build_FoundryMk1_C']
    
