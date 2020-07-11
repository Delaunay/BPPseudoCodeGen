
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_ModularFrameHeavy(FGRecipe):
    mDisplayName = NSLOCTEXT("", "34272A29446E4804EA516192520E5AE1", "Truck Chassis")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrame/Desc_ModularFrame.Desc_ModularFrame_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 15}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlateReinforced/Desc_SteelPlateReinforced.Desc_SteelPlateReinforced_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronScrew/Desc_IronScrew.Desc_IronScrew_C', 'amount': 100}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 1}]
    mManufactoringDuration = 30
    mManualManufacturingMultiplier = 0.6000000238418579
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
