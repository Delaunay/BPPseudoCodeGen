
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_UJellyLandingPad(FGRecipe):
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Rotor/Desc_Rotor.Desc_Rotor_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 20}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_GenericBiomass.Desc_GenericBiomass_C', 'amount': 200}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/LandingPad/Desc_LandingPad.Desc_LandingPad_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
