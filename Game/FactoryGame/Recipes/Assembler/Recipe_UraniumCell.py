﻿
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_UraniumCell(FGRecipe):
    mDisplayName = NSLOCTEXT("", "A468E4774A053E75767EC9907622E05C", "Tire")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/UraniumPellet/Desc_UraniumPellet.Desc_UraniumPellet_C', 'amount': 40}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 9}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/UraniumCell/Desc_UraniumCell.Desc_UraniumCell_C', 'amount': 10}]
    mManufactoringDuration = 60
    mManualManufacturingMultiplier = 0.5
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
