
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_ColorGun(FGRecipe):
    mDisplayName = NSLOCTEXT("", "3164F2DD446D965E35941D929DF5E5D1", "Nail Gun")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronScrew/Desc_IronScrew.Desc_IronScrew_C', 'amount': 80}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 40}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/ColorGun/BP_EquipmentDescriptorColorGun.BP_EquipmentDescriptorColorGun_C', 'amount': 1}]
    mManufactoringDuration = 80
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
