
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_AluminumSheet(FGRecipe):
    mDisplayName = NSLOCTEXT("", "FBC9F1384334B3157356329D60212511", "Aluminum Plate")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumIngot/Desc_AluminumIngot.Desc_AluminumIngot_C', 'amount': 8}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperIngot/Desc_CopperIngot.Desc_CopperIngot_C', 'amount': 3}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumPlate/Desc_AluminumPlate.Desc_AluminumPlate_C', 'amount': 4}]
    mManufactoringDuration = 8
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
