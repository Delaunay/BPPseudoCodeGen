
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PowerLine(FGRecipe):
    mDisplayName = NSLOCTEXT("", "2D95E89B4956225320B0CBB6CC35E0C8", "Power Line")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/PowerLine/Desc_PowerLine.Desc_PowerLine_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
