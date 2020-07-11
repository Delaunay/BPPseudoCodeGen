
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Wall_Conveyor_8x4_02(FGRecipe):
    mDisplayName = NSLOCTEXT("", "D9AFB99140BA0B39AC48B1A4309C886D", "Wall 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 3}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Wall/Desc_Wall_Conveyor_8x4_02.Desc_Wall_Conveyor_8x4_02_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
