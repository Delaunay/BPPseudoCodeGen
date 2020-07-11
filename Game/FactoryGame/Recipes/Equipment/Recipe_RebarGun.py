
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_RebarGun(FGRecipe):
    mDisplayName = NSLOCTEXT("", "59EB979D4F9E4384BAA81290C9893AFD", "Nail Gun")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 6}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 16}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronScrew/Desc_IronScrew.Desc_IronScrew_C', 'amount': 100}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/NailGun/Desc_RebarGunProjectile.Desc_RebarGunProjectile_C', 'amount': 1}]
    mManufactoringDuration = 100
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
