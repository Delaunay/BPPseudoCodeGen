
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_SpaceElevatorPart_2(FGRecipe):
    mDisplayName = NSLOCTEXT("", "34723FF04485F7A5B719D992BD617B5E", "Alternate: Iron Wire")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrame/Desc_ModularFrame.Desc_ModularFrame_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlate/Desc_SteelPlate.Desc_SteelPlate_C', 'amount': 12}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SpaceElevatorParts/Desc_SpaceElevatorPart_2.Desc_SpaceElevatorPart_2_C', 'amount': 2}]
    mManufactoringDuration = 24
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C']
    
