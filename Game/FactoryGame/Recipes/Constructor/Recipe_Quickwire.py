
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Quickwire(FGRecipe):
    mDisplayName = NSLOCTEXT("", "4EDF83B245B7939ABABDCD8D352552A7", "High-Speed Wire")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GoldIngot/Desc_GoldIngot.Desc_GoldIngot_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedWire/Desc_HighSpeedWire.Desc_HighSpeedWire_C', 'amount': 5}]
    mManufactoringDuration = 5
    mManualManufacturingMultiplier = 2
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
