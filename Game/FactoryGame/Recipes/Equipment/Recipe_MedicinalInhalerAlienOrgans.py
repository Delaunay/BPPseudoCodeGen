
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_MedicinalInhalerAlienOrgans(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "69D0F583482AF9E7CA7E2C95B31FE3DA", "Medicinal Inhaler: Alien Organs")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AnimalParts/Desc_SpitterParts.Desc_SpitterParts_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_Mycelia.Desc_Mycelia_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/Medkit/Desc_Medkit.Desc_Medkit_C', 'amount': 1}]
    mManufactoringDuration = 20
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
