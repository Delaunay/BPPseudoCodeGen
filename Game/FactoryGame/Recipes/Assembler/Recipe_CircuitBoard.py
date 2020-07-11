
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_CircuitBoard(FGRecipe):
    mDisplayName = NSLOCTEXT("", "658E3115403CFB9B7C08FCA109F2AC20", "Circuit Board")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperSheet/Desc_CopperSheet.Desc_CopperSheet_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Plastic/Desc_Plastic.Desc_Plastic_C', 'amount': 4}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CircuitBoard/Desc_CircuitBoard.Desc_CircuitBoard_C', 'amount': 1}]
    mManufactoringDuration = 8
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
