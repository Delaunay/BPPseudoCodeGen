
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_AssemblerMk1(FGRecipe):
    mDisplayName = NSLOCTEXT("", "6A36577341ECB5FACADA9F913D0CDD0D", "Advanced Constructor")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 8}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rotor/Desc_Rotor.Desc_Rotor_C', 'amount': 4}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 10}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Desc_AssemblerMk1.Desc_AssemblerMk1_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
