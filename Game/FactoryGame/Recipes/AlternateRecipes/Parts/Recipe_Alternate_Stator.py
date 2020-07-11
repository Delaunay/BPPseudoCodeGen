
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_Stator(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "0B116DAD485A2329ADCFF39E7918D227", "Alternate: Quickwire Stator")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 4}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedWire/Desc_HighSpeedWire.Desc_HighSpeedWire_C', 'amount': 15}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Stator/Desc_Stator.Desc_Stator_C', 'amount': 2}]
    mManufactoringDuration = 15
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C']
    
