
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_ElectromagneticControlRod(FGRecipe):
    mDisplayName = NSLOCTEXT("", "A468E4774A053E75767EC9907622E05C", "Tire")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Stator/Desc_Stator.Desc_Stator_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CircuitBoardHighSpeed/Desc_CircuitBoardHighSpeed.Desc_CircuitBoardHighSpeed_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ElectromagneticControlRod/Desc_ElectromagneticControlRod.Desc_ElectromagneticControlRod_C', 'amount': 2}]
    mManufactoringDuration = 30
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
