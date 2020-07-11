
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Biofuel(FGRecipe):
    mDisplayName = NSLOCTEXT("", "70B80F6A4F45A39B55B9E68290FD1B70", "Wire")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_GenericBiomass.Desc_GenericBiomass_C', 'amount': 8}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/BioFuel/Desc_Biofuel.Desc_Biofuel_C', 'amount': 4}]
    mManufactoringDuration = 4
    mManualManufacturingMultiplier = 5
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Game/FactoryGame/Buildable/Factory/AutomatedWorkBench/Build_AutomatedWorkBench.Build_AutomatedWorkBench_C']
    
