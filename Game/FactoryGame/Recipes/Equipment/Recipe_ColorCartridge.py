
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_ColorCartridge(FGRecipe):
    mDisplayName = NSLOCTEXT("", "70B80F6A4F45A39B55B9E68290FD1B70", "Wire")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_FlowerPetals.Desc_FlowerPetals_C', 'amount': 25}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ColorCartridge/Desc_ColorCartridge.Desc_ColorCartridge_C', 'amount': 50}]
    mManufactoringDuration = 40
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
