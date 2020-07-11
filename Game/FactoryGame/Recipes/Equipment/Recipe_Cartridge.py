
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Cartridge(FGRecipe):
    mDisplayName = NSLOCTEXT("", "330DCA9B4A8F47278A1B5A92F6A8FA13", "Standard Cartridge")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/Beacon/BP_EquipmentDescriptorBeacon.BP_EquipmentDescriptorBeacon_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/GunPowder/Desc_Gunpowder.Desc_Gunpowder_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 10}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CartridgeStandard/Desc_CartridgeStandard.Desc_CartridgeStandard_C', 'amount': 5}]
    mManufactoringDuration = 20
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
