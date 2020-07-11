
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_HeatSink(FGRecipe):
    mDisplayName = NSLOCTEXT("", "43FF2B1645884F41403B0FA1EA902842", "Reinforced Aluminum Plate")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumPlate/Desc_AluminumPlate.Desc_AluminumPlate_C', 'amount': 8}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 14}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumPlateReinforced/Desc_AluminumPlateReinforced.Desc_AluminumPlateReinforced_C', 'amount': 2}]
    mManufactoringDuration = 12
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
