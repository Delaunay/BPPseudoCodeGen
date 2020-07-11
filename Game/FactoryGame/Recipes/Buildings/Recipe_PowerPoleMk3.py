
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PowerPoleMk3(FGRecipe):
    mDisplayName = NSLOCTEXT("", "F635A62E494D800B04E7D5B9C14AA019", "Huge Power Pole")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedConnector/Desc_HighSpeedConnector.Desc_HighSpeedConnector_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 3}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/PowerPoleMk3/Desc_PowerPoleMk3.Desc_PowerPoleMk3_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
