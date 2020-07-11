
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_FluidCanister(FGRecipe):
    mDisplayName = NSLOCTEXT("", "70B80F6A4F45A39B55B9E68290FD1B70", "Wire")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Plastic/Desc_Plastic.Desc_Plastic_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/FluidCanister/Desc_FluidCanister.Desc_FluidCanister_C', 'amount': 4}]
    mManufactoringDuration = 4
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
