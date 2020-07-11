
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_GeneratorBiomass(FGRecipe):
    mDisplayName = NSLOCTEXT("", "02FF1221439A0AC2D791B0ADCC6158F4", "Biomass Burner")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 15}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 15}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 25}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/GeneratorBiomass/Desc_GeneratorBiomass.Desc_GeneratorBiomass_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
