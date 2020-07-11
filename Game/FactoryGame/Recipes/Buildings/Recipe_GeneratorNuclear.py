
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_GeneratorNuclear(FGRecipe):
    mDisplayName = NSLOCTEXT("", "3583E71C454A0FA918860BACE62F537C", "Nuclear Power Plant")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 150}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ComputerSuper/Desc_ComputerSuper.Desc_ComputerSuper_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedConnector/Desc_HighSpeedConnector.Desc_HighSpeedConnector_C', 'amount': 15}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/GeneratorNuclear/Desc_GeneratorNuclear.Desc_GeneratorNuclear_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
