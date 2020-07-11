
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_OilRefinery(FGRecipe):
    mDisplayName = NSLOCTEXT("", "86CE40D04D69202D435D6CA4114AC4E9", "Oil Refinery")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Motor/Desc_Motor.Desc_Motor_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlateReinforced/Desc_SteelPlateReinforced.Desc_SteelPlateReinforced_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 30}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperSheet/Desc_CopperSheet.Desc_CopperSheet_C', 'amount': 20}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/OilRefinery/Desc_OilRefinery.Desc_OilRefinery_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
