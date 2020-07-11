
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_SpaceRifleMk1(FGRecipe):
    mDisplayName = NSLOCTEXT("", "E0DFCEAF495FE4479570BFB1BB603C7C", "Space Rifle")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 25}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CircuitBoard/Desc_CircuitBoard.Desc_CircuitBoard_C', 'amount': 20}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronScrew/Desc_IronScrew.Desc_IronScrew_C', 'amount': 250}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/Rifle/BP_EquipmentDescriptorRifle.BP_EquipmentDescriptorRifle_C', 'amount': 1}]
    mManufactoringDuration = 120
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
