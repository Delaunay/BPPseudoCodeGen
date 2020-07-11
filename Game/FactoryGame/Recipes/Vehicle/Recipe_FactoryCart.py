
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_FactoryCart(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "87CD844F4D7D1638408E8BBAF40D4EE2", "Factory Cart™")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 4}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 4}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rotor/Desc_Rotor.Desc_Rotor_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/GolfCart/Desc_GolfCart.Desc_GolfCart_C', 'amount': 1}]
    mManufactoringDuration = 20
    mManualManufacturingMultiplier = 2
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
