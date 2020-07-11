
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_QuarterPipe_02(FGRecipe):
    mDisplayName = NSLOCTEXT("", "709030C74C0BE32D64E013BD37CD1FDC", "Foundation 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 6}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Foundation/Desc_QuarterPipe_02.Desc_QuarterPipe_02_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
