
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_StoragePlayer(FGRecipe):
    mDisplayName = NSLOCTEXT("", "5DE27A9C4A35F615C3413BB2AE0D00C6", "Expanded Storage Container")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 6}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 6}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/StoragePlayer/Desc_StoragePlayer.Desc_StoragePlayer_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
