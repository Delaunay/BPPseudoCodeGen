
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_HighSpeedWiring(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "C1F120734939E64681AE32864FE9A08F", "Alternate: Automated Speed Wiring")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Stator/Desc_Stator.Desc_Stator_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 40}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedConnector/Desc_HighSpeedConnector.Desc_HighSpeedConnector_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SpaceElevatorParts/Desc_SpaceElevatorPart_3.Desc_SpaceElevatorPart_3_C', 'amount': 4}]
    mManufactoringDuration = 32
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C']
    
