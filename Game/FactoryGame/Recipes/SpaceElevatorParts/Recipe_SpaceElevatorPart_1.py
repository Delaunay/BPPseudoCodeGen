
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_SpaceElevatorPart_1(FGRecipe):
    mDisplayName = NSLOCTEXT("", "34723FF04485F7A5B719D992BD617B5E", "Alternate: Iron Wire")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rotor/Desc_Rotor.Desc_Rotor_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SpaceElevatorParts/Desc_SpaceElevatorPart_1.Desc_SpaceElevatorPart_1_C', 'amount': 1}]
    mManufactoringDuration = 30
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C']
    
