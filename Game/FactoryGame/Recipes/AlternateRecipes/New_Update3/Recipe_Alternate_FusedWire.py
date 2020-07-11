
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_FusedWire(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "2E70905C4A517BABD5672A83DB582277", "Alternate: Fused Wire")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperIngot/Desc_CopperIngot.Desc_CopperIngot_C', 'amount': 4}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/GoldIngot/Desc_GoldIngot.Desc_GoldIngot_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 30}]
    mManufactoringDuration = 20
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C']
    
