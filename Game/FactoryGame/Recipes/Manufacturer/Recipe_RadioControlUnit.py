
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_RadioControlUnit(FGRecipe):
    mDisplayName = NSLOCTEXT("", "121E45A7479D5337189586A4EFCB5D8F", "Explorer Jeep Chassis")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumPlateReinforced/Desc_AluminumPlateReinforced.Desc_AluminumPlateReinforced_C', 'amount': 4}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 16}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CrystalOscillator/Desc_CrystalOscillator.Desc_CrystalOscillator_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Computer/Desc_Computer.Desc_Computer_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameLightweight/Desc_ModularFrameLightweight.Desc_ModularFrameLightweight_C', 'amount': 1}]
    mManufactoringDuration = 24
    mManualManufacturingMultiplier = 1.5
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
