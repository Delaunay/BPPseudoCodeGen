
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PowerCrystalShard_3(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "5FC18C3847EF07C56B82B6B60CD6CFD1", "Power Shard (5)")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Environment/Crystal/Desc_Crystal_mk3.Desc_Crystal_mk3_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Environment/Crystal/Desc_CrystalShard.Desc_CrystalShard_C', 'amount': 5}]
    mManufactoringDuration = 20
    mManualManufacturingMultiplier = 1.2000000476837158
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
