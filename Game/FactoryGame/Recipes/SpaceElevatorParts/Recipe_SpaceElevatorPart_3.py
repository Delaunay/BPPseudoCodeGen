
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_SpaceElevatorPart_3(FGRecipe):
    mDisplayName = NSLOCTEXT("", "34723FF04485F7A5B719D992BD617B5E", "Alternate: Iron Wire")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Stator/Desc_Stator.Desc_Stator_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 20}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SpaceElevatorParts/Desc_SpaceElevatorPart_3.Desc_SpaceElevatorPart_3_C', 'amount': 1}]
    mManufactoringDuration = 24
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C']
    
