
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PowerCrystalShard_1(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "F570839544A1BBB6BC090CAAD0FF9DF9", "Power Shard (1)")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Environment/Crystal/Desc_Crystal.Desc_Crystal_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Environment/Crystal/Desc_CrystalShard.Desc_CrystalShard_C', 'amount': 1}]
    mManufactoringDuration = 10
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
