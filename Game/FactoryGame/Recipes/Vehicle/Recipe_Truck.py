
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Truck(FGRecipe):
    mDisplayName = NSLOCTEXT("", "BC298AD34D8C45E83BD449A5A0A7B0EA", "Truck")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Motor/Desc_Motor.Desc_Motor_C', 'amount': 8}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Computer/Desc_Computer.Desc_Computer_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 4}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Equipment/Beacon/BP_EquipmentDescriptorBeacon.BP_EquipmentDescriptorBeacon_C', 'amount': 10}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Vehicle/Truck/Desc_Truck.Desc_Truck_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
