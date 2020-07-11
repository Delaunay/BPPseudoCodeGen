
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_IronRod(FGRecipe):
    mDisplayName = NSLOCTEXT("", "CEFDA0B145E8A5857A7861A5F9F88E2E", "Iron Rod")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronIngot/Desc_IronIngot.Desc_IronIngot_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 1}]
    mManufactoringDuration = 4
    mManualManufacturingMultiplier = 0.5
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
