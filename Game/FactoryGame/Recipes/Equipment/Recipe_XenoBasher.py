
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_XenoBasher(FGRecipe):
    mDisplayName = NSLOCTEXT("", "346A2B29487AA085EF7DFAB192D6B8A8", "JetPack")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrame/Desc_ModularFrame.Desc_ModularFrame_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Equipment/ShockShank/BP_EquipmentDescriptorShockShank.BP_EquipmentDescriptorShockShank_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 25}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 500}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/StunSpear/BP_EquipmentDescriptorStunSpear.BP_EquipmentDescriptorStunSpear_C', 'amount': 1}]
    mManufactoringDuration = 80
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
