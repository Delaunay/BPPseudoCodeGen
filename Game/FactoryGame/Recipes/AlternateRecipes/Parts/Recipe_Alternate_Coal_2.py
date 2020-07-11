
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_Coal_2(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "B01B8FB3463513BCB8CC07867FAC0C0C", "Alternate: Biocoal")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_GenericBiomass.Desc_GenericBiomass_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/Coal/Desc_Coal.Desc_Coal_C', 'amount': 6}]
    mManufactoringDuration = 8
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C']
    
