
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Stator(FGRecipe):
    mDisplayName = NSLOCTEXT("", "A468E4774A053E75767EC9907622E05C", "Tire")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 8}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Stator/Desc_Stator.Desc_Stator_C', 'amount': 1}]
    mManufactoringDuration = 12
    mManualManufacturingMultiplier = 1.5
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
