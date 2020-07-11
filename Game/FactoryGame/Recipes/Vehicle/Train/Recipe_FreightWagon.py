
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_FreightWagon(FGRecipe):
    mDisplayName = NSLOCTEXT("", "E25AB2C04721EDD0F96C3385AD7A86DF", "Freight Car")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 4}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 10}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Vehicle/Train/Wagon/Desc_FreightWagon.Desc_FreightWagon_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
