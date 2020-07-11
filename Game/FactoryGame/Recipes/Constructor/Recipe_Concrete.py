
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Concrete(FGRecipe):
    mDisplayName = NSLOCTEXT("", "2729A23349CFE8D6C52F8B9B0E7959D6", "Stone Brick")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/Stone/Desc_Stone.Desc_Stone_C', 'amount': 3}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 1}]
    mManufactoringDuration = 4
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
