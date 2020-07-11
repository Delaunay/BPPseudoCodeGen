
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_JetPack(FGRecipe):
    mDisplayName = NSLOCTEXT("", "346A2B29487AA085EF7DFAB192D6B8A8", "JetPack")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Plastic/Desc_Plastic.Desc_Plastic_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CircuitBoard/Desc_CircuitBoard.Desc_CircuitBoard_C', 'amount': 15}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 25}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/JetPack/BP_EquipmentDescriptorJetPack.BP_EquipmentDescriptorJetPack_C', 'amount': 1}]
    mManufactoringDuration = 120
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
