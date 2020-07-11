
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_GeneratorGeoThermal(FGRecipe):
    mDisplayName = NSLOCTEXT("", "9189D69E4824333BFD484DABAC4CDE62", "Fuel Generator")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ComputerSuper/Desc_ComputerSuper.Desc_ComputerSuper_C', 'amount': 8}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 16}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedConnector/Desc_HighSpeedConnector.Desc_HighSpeedConnector_C', 'amount': 16}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperSheet/Desc_CopperSheet.Desc_CopperSheet_C', 'amount': 40}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 80}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/GeneratorGeoThermal/Desc_GeneratorGeoThermal.Desc_GeneratorGeoThermal_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
