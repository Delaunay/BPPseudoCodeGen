
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_QuarterPipeCorner_04(FGRecipe):
    mDisplayName = NSLOCTEXT("", "E6AEC1274AD152F80933B9A2C34BF1FB", "Foundation 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 6}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Foundation/Desc_QuarterPipeCorner_04.Desc_QuarterPipeCorner_04_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
