
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_RadarTower(FGRecipe):
    mDisplayName = NSLOCTEXT("", "4606ADA9430421B2F4213D95D5512D35", "Smelter")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 30}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CrystalOscillator/Desc_CrystalOscillator.Desc_CrystalOscillator_C', 'amount': 30}, {'ItemClass': '/Game/FactoryGame/Resource/Equipment/Beacon/BP_EquipmentDescriptorBeacon.BP_EquipmentDescriptorBeacon_C', 'amount': 20}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 100}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/RadarTower/Desc_RadarTower.Desc_RadarTower_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
