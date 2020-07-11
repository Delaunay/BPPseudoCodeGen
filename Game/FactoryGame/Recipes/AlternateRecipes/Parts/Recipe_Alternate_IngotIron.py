
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_IngotIron(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "78E031DB40994133BCBEEBBE2A641F4F", "Alternate: Iron Alloy Ingot")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/OreIron/Desc_OreIron.Desc_OreIron_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/OreCopper/Desc_OreCopper.Desc_OreCopper_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronIngot/Desc_IronIngot.Desc_IronIngot_C', 'amount': 5}]
    mManufactoringDuration = 6
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/FoundryMk1/Build_FoundryMk1.Build_FoundryMk1_C']
    
