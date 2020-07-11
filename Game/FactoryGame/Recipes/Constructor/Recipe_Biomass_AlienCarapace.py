
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Biomass_AlienCarapace(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "7D71745349911E819BB134828FA19A7E", "Biomass (Alien Carapace)")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AnimalParts/Desc_HogParts.Desc_HogParts_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_GenericBiomass.Desc_GenericBiomass_C', 'amount': 100}]
    mManufactoringDuration = 4
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
