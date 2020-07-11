
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_TrainPlatformEmpty(FGRecipe):
    mDisplayName = NSLOCTEXT("", "0EBA08E841868C93252A988A8AD45499", "TSL")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 6}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 50}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/Train/Station/Desc_TrainPlatformEmpty.Desc_TrainPlatformEmpty_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
