
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_QuarterPipeCorner_01(FGRecipe):
    mDisplayName = NSLOCTEXT("", "683A148440C20108DA372791D704CB96", "Foundation 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 6}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Foundation/Desc_QuarterPipeCorner_01.Desc_QuarterPipeCorner_01_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
