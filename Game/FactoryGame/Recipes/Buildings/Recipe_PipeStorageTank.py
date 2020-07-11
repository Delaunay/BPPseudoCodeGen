
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PipeStorageTank(FGRecipe):
    mDisplayName = NSLOCTEXT("", "C55B457D44ED9C4440647CB57CED5AE4", "Simple Constructor")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperSheet/Desc_CopperSheet.Desc_CopperSheet_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrame/Desc_ModularFrame.Desc_ModularFrame_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/StorageTank/Desc_PipeStorageTank.Desc_PipeStorageTank_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
