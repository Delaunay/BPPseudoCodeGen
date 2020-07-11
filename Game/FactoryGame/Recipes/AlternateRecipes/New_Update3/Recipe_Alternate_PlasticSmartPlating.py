
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_PlasticSmartPlating(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "505EA2C14859757A81898483EAA75ABE", "Alternate: Plastic Smart Plating")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rotor/Desc_Rotor.Desc_Rotor_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Plastic/Desc_Plastic.Desc_Plastic_C', 'amount': 3}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SpaceElevatorParts/Desc_SpaceElevatorPart_1.Desc_SpaceElevatorPart_1_C', 'amount': 2}]
    mManufactoringDuration = 24
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C']
    
