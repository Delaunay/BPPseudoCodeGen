
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_StorageContainerMk1(FGRecipe):
    mDisplayName = NSLOCTEXT("", "49B16827419423BB339D77AD2CA2D9DE", "Storage Container")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 10}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/StorageContainerMk1/Desc_StorageContainerMk1.Desc_StorageContainerMk1_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
