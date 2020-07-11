
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Beacon(FGRecipe):
    mDisplayName = NSLOCTEXT("", "96C938AE40F2323C3641D7A346D90A02", "Beacon")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 15}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/Beacon/BP_EquipmentDescriptorBeacon.BP_EquipmentDescriptorBeacon_C', 'amount': 1}]
    mManufactoringDuration = 8
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C', '/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C']
    
