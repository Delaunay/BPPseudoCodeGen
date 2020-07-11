
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_IngotCopper(FGRecipe):
    mDisplayName = NSLOCTEXT("", "948EFA39469E48661B891B924E5AF36B", "Copper Ingot")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/OreCopper/Desc_OreCopper.Desc_OreCopper_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperIngot/Desc_CopperIngot.Desc_CopperIngot_C', 'amount': 1}]
    mManufactoringDuration = 2
    mManualManufacturingMultiplier = 3
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/SmelterMk1/Build_SmelterMk1.Build_SmelterMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
