
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_BladeRunners(FGRecipe):
    mDisplayName = NSLOCTEXT("", "346A2B29487AA085EF7DFAB192D6B8A8", "JetPack")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedWire/Desc_HighSpeedWire.Desc_HighSpeedWire_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrame/Desc_ModularFrame.Desc_ModularFrame_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rotor/Desc_Rotor.Desc_Rotor_C', 'amount': 3}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/JumpingStilts/BP_EquipmentDescriptorJumpingStilts.BP_EquipmentDescriptorJumpingStilts_C', 'amount': 1}]
    mManufactoringDuration = 80
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
