
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_MedicinalInhaler(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "06605B79438E7E9F9613B7A58B1EE21F", "Nutritional Inhaler")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Environment/DesertShroom/Desc_Shroom.Desc_Shroom_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Environment/Berry/Desc_Berry.Desc_Berry_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/Environment/Nut/Desc_Nut.Desc_Nut_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_Mycelia.Desc_Mycelia_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/Medkit/Desc_Medkit.Desc_Medkit_C', 'amount': 1}]
    mManufactoringDuration = 20
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
