
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_CopperRotor(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "EA3ED26D421FD0632F9D52B1330DB341", "Alternate: Copper Rotor")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperSheet/Desc_CopperSheet.Desc_CopperSheet_C', 'amount': 6}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronScrew/Desc_IronScrew.Desc_IronScrew_C', 'amount': 52}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Rotor/Desc_Rotor.Desc_Rotor_C', 'amount': 3}]
    mManufactoringDuration = 16
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C']
    
