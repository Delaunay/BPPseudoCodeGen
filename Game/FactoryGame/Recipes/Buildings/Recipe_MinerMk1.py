
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_MinerMk1(FGRecipe):
    mDisplayName = NSLOCTEXT("", "03FE8F834989E7E016DC7DBE4B7431CE", "Miner")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/PortableMiner/BP_ItemDescriptorPortableMiner.BP_ItemDescriptorPortableMiner_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 10}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/MinerMK1/Desc_MinerMk1.Desc_MinerMk1_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
