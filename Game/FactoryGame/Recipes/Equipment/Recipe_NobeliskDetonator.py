
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_NobeliskDetonator(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "6F06334C4E2A300AFA0EE39FBC6DF539", "Nobelisk Detonator")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/GemstoneScanner/BP_EquipmentDescriptorObjectScanner.BP_EquipmentDescriptorObjectScanner_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlateReinforced/Desc_SteelPlateReinforced.Desc_SteelPlateReinforced_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 50}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/NobeliskDetonator/BP_EquipmentDescriptorNobeliskDetonator.BP_EquipmentDescriptorNobeliskDetonator_C', 'amount': 1}]
    mManufactoringDuration = 80
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
