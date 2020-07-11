
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_WaterPump(FGRecipe):
    mDisplayName = NSLOCTEXT("", "661AD73044EA2B723E4B13BB52823E50", "Oil Pump")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperSheet/Desc_CopperSheet.Desc_CopperSheet_C', 'amount': 20}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rotor/Desc_Rotor.Desc_Rotor_C', 'amount': 10}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/WaterPump/Desc_WaterPump.Desc_WaterPump_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
