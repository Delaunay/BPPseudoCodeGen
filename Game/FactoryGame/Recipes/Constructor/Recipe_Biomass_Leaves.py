
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Biomass_Leaves(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "E14289D0445F1ADF5C8B0D9DC6F4FBD2", "Biomass (Leaves)")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_Leaves.Desc_Leaves_C', 'amount': 10}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_GenericBiomass.Desc_GenericBiomass_C', 'amount': 5}]
    mManufactoringDuration = 5
    mManualManufacturingMultiplier = 0.4000000059604645
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
