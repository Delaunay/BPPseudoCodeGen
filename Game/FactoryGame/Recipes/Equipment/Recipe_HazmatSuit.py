
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_HazmatSuit(FGRecipe):
    mDisplayName = NSLOCTEXT("", "004D0A114A7CE66D8AD4AFB96CD12F42", "Gas Mask")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Plastic/Desc_Plastic.Desc_Plastic_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumPlate/Desc_AluminumPlate.Desc_AluminumPlate_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_Fabric.Desc_Fabric_C', 'amount': 50}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/HazmatSuit/BP_EquipmentDescriptorHazmatSuit.BP_EquipmentDescriptorHazmatSuit_C', 'amount': 1}]
    mManufactoringDuration = 120
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
