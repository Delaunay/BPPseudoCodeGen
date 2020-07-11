
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Biomass_Wood(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "708D6EDE49F6EC13D549608A67B09CB0", "Biomass (Wood)")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_Wood.Desc_Wood_C', 'amount': 4}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_GenericBiomass.Desc_GenericBiomass_C', 'amount': 20}]
    mManufactoringDuration = 4
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
