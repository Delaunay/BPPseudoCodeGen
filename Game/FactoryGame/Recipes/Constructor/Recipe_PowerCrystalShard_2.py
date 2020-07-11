
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PowerCrystalShard_2(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "5DBB8D0D42AD88D57569A9A3D9EFB551", "Power Shard (2)")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Environment/Crystal/Desc_Crystal_mk2.Desc_Crystal_mk2_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Environment/Crystal/Desc_CrystalShard.Desc_CrystalShard_C', 'amount': 2}]
    mManufactoringDuration = 15
    mManualManufacturingMultiplier = 1.2000000476837158
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
