
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PowerPoleWallDoubleMk3(FGRecipe):
    mDisplayName = NSLOCTEXT("", "78B755064972A015003C099B90C59A2D", "Power Pole")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedConnector/Desc_HighSpeedConnector.Desc_HighSpeedConnector_C', 'amount': 6}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 6}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/PowerPoleWallDouble/Desc_PowerPoleWallDoubleMk3.Desc_PowerPoleWallDoubleMk3_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
