
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_IngotSteel_1(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "D26F7A60474850677854E597891A382F", "Alternate: Solid Steel Ingot")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronIngot/Desc_IronIngot.Desc_IronIngot_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Coal/Desc_Coal.Desc_Coal_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelIngot/Desc_SteelIngot.Desc_SteelIngot_C', 'amount': 3}]
    mManufactoringDuration = 3
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/FoundryMk1/Build_FoundryMk1.Build_FoundryMk1_C']
    
