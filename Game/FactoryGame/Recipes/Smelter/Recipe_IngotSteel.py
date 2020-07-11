
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_IngotSteel(FGRecipe):
    mDisplayName = NSLOCTEXT("", "6325BFD14A3E8E65F6F92DB703012B41", "Steel Ingot")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/OreIron/Desc_OreIron.Desc_OreIron_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Coal/Desc_Coal.Desc_Coal_C', 'amount': 3}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelIngot/Desc_SteelIngot.Desc_SteelIngot_C', 'amount': 3}]
    mManufactoringDuration = 4
    mManualManufacturingMultiplier = 6
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/FoundryMk1/Build_FoundryMk1.Build_FoundryMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C']
    
