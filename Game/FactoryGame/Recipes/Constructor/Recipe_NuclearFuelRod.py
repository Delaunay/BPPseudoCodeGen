
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_NuclearFuelRod(FGRecipe):
    mDisplayName = NSLOCTEXT("", "95338B074903DF7035D7059E4AFA8B6E", "Nuclear Fuel Rod")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/UraniumCell/Desc_UraniumCell.Desc_UraniumCell_C', 'amount': 25}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlateReinforced/Desc_SteelPlateReinforced.Desc_SteelPlateReinforced_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ElectromagneticControlRod/Desc_ElectromagneticControlRod.Desc_ElectromagneticControlRod_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/NuclearFuelRod/Desc_NuclearFuelRod.Desc_NuclearFuelRod_C', 'amount': 1}]
    mManufactoringDuration = 150
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C']
    
