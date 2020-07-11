
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_QuarterPipeCorner_02(FGRecipe):
    mDisplayName = NSLOCTEXT("", "E2BCDE264F23A5779A337090CABCE5D4", "Foundation 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 6}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Foundation/Desc_QuarterPipeCorner_02.Desc_QuarterPipeCorner_02_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
