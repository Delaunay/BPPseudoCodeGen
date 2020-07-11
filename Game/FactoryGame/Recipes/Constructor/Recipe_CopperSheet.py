
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_CopperSheet(FGRecipe):
    mDisplayName = NSLOCTEXT("", "70B80F6A4F45A39B55B9E68290FD1B70", "Wire")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperIngot/Desc_CopperIngot.Desc_CopperIngot_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperSheet/Desc_CopperSheet.Desc_CopperSheet_C', 'amount': 1}]
    mManufactoringDuration = 6
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
