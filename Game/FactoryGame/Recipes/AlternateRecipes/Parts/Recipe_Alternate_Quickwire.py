
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_Quickwire(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "69BE1B84453DB4C5B9CC139E75C9B256", "Alternate: Fused Quckwire")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GoldIngot/Desc_GoldIngot.Desc_GoldIngot_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperIngot/Desc_CopperIngot.Desc_CopperIngot_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedWire/Desc_HighSpeedWire.Desc_HighSpeedWire_C', 'amount': 12}]
    mManufactoringDuration = 8
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C']
    
