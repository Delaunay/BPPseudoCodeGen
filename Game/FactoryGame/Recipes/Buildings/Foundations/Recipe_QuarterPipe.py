
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_QuarterPipe(FGRecipe):
    mDisplayName = NSLOCTEXT("", "C99752A64D34E072F4BD2E917B015731", "Foundation 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 6}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Foundation/Desc_QuarterPipe.Desc_QuarterPipe_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
