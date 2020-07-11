
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Fence_01(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "9A918A5B4AB649D83C0FE08D662545A7", "Fence 1")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Fence/Desc_Fence_01.Desc_Fence_01_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
