
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PortableMiner(FGRecipe):
    mDisplayName = NSLOCTEXT("", "5E4A9B47487DE784BDE440B6A32A318E", "Portable Miner")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 3}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/PortableMiner/BP_ItemDescriptorPortableMiner.BP_ItemDescriptorPortableMiner_C', 'amount': 1}]
    mManufactoringDuration = 40
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
