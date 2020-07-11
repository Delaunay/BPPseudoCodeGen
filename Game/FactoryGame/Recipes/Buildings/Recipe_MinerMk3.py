
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_MinerMk3(FGRecipe):
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/PortableMiner/BP_ItemDescriptorPortableMiner.BP_ItemDescriptorPortableMiner_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 4}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 20}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/MotorLightweight/Desc_MotorLightweight.Desc_MotorLightweight_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Computer/Desc_Computer.Desc_Computer_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/MinerMk3/Desc_MinerMk3.Desc_MinerMk3_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
