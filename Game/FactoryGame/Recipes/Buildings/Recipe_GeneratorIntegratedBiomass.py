
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_GeneratorIntegratedBiomass(FGRecipe):
    mDisplayName = NSLOCTEXT("", "02FF1221439A0AC2D791B0ADCC6158F4", "Biomass Burner")
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/GeneratorBiomass/Desc_GeneratorIntegratedBiomass.Desc_GeneratorIntegratedBiomass_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
