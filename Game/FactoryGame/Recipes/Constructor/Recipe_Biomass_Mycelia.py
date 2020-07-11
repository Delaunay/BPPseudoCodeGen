
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Biomass_Mycelia(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "00791E3A4EA70DF52479969B7431D5B3", "Biomass (Mycelia)")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_Mycelia.Desc_Mycelia_C', 'amount': 10}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_GenericBiomass.Desc_GenericBiomass_C', 'amount': 10}]
    mManufactoringDuration = 4
    mManualManufacturingMultiplier = 0.5
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
