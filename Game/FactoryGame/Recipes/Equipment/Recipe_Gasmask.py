
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Gasmask(FGRecipe):
    mDisplayName = NSLOCTEXT("", "004D0A114A7CE66D8AD4AFB96CD12F42", "Gas Mask")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 100}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Plastic/Desc_Plastic.Desc_Plastic_C', 'amount': 100}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_Fabric.Desc_Fabric_C', 'amount': 100}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/GasMask/BP_EquipmentDescriptorGasmask.BP_EquipmentDescriptorGasmask_C', 'amount': 1}]
    mManufactoringDuration = 80
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
