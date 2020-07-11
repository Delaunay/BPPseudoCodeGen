
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_Cable_2(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "6F1B8C5C43C85CEC55EBA7B46AA3097F", "Alternate: Quickwire Cable")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedWire/Desc_HighSpeedWire.Desc_HighSpeedWire_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 11}]
    mManufactoringDuration = 24
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C']
    
