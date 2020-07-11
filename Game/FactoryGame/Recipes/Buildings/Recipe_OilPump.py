
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_OilPump(FGRecipe):
    mDisplayName = NSLOCTEXT("", "661AD73044EA2B723E4B13BB52823E50", "Oil Pump")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Motor/Desc_Motor.Desc_Motor_C', 'amount': 15}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlateReinforced/Desc_SteelPlateReinforced.Desc_SteelPlateReinforced_C', 'amount': 20}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 60}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/OilPump/Desc_OilPump.Desc_OilPump_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
