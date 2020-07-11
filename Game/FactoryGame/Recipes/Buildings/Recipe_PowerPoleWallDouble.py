
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PowerPoleWallDouble(FGRecipe):
    mDisplayName = NSLOCTEXT("", "78B755064972A015003C099B90C59A2D", "Power Pole")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 8}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/PowerPoleWallDouble/Desc_PowerPoleWallDouble.Desc_PowerPoleWallDouble_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
