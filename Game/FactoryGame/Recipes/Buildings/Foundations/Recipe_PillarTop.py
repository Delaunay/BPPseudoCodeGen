
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PillarTop(FGRecipe):
    mDisplayName = NSLOCTEXT("", "FBE33A4E497BB836069D68BB480266E6", "Foundation 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 6}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Foundation/Desc_PillarTop.Desc_PillarTop_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
