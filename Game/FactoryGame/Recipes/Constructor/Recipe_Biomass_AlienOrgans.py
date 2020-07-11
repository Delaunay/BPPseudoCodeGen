
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Biomass_AlienOrgans(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "2D27904143B8BF36BF98BF8CBECD40AF", "Biomass (Alien Organs)")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AnimalParts/Desc_SpitterParts.Desc_SpitterParts_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_GenericBiomass.Desc_GenericBiomass_C', 'amount': 200}]
    mManufactoringDuration = 8
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
