
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_SteelPipe(FGRecipe):
    mDisplayName = NSLOCTEXT("", "BA6B414444A54B33004CF099598191D9", "Steel Pipe")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelIngot/Desc_SteelIngot.Desc_SteelIngot_C', 'amount': 3}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 2}]
    mManufactoringDuration = 6
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
