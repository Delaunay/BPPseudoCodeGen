
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_IngotIron(FGRecipe):
    mDisplayName = NSLOCTEXT("", "C56E67B84E03CD359D9659A3EF870CED", "Iron Ingot")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/OreIron/Desc_OreIron.Desc_OreIron_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronIngot/Desc_IronIngot.Desc_IronIngot_C', 'amount': 1}]
    mManufactoringDuration = 2
    mManualManufacturingMultiplier = 3
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/SmelterMk1/Build_SmelterMk1.Build_SmelterMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
