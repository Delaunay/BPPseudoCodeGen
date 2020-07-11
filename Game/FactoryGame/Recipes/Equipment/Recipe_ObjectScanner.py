
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_ObjectScanner(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "A25068FC4F6EF76883C63A8BD537335D", "Object Scanner")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 4}, {'ItemClass': '/Game/FactoryGame/Resource/Equipment/Beacon/BP_EquipmentDescriptorBeacon.BP_EquipmentDescriptorBeacon_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronScrew/Desc_IronScrew.Desc_IronScrew_C', 'amount': 50}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/GemstoneScanner/BP_EquipmentDescriptorObjectScanner.BP_EquipmentDescriptorObjectScanner_C', 'amount': 1}]
    mManufactoringDuration = 40
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
