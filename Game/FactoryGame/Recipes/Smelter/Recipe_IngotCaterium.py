
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_IngotCaterium(FGRecipe):
    mDisplayName = NSLOCTEXT("", "091257F3449A9E650C460AB7E3A96B19", "Gold Ingot")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/OreGold/Desc_OreGold.Desc_OreGold_C', 'amount': 3}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GoldIngot/Desc_GoldIngot.Desc_GoldIngot_C', 'amount': 1}]
    mManufactoringDuration = 4
    mManualManufacturingMultiplier = 2
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/SmelterMk1/Build_SmelterMk1.Build_SmelterMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C']
    
