
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_UraniumCell_1(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "445FDDF9454B15DD980DC49E6F1D9D82", "Alternate: Infused Uranium Cell")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/UraniumPellet/Desc_UraniumPellet.Desc_UraniumPellet_C', 'amount': 40}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Sulfur/Desc_Sulfur.Desc_Sulfur_C', 'amount': 45}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Silica/Desc_Silica.Desc_Silica_C', 'amount': 45}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedWire/Desc_HighSpeedWire.Desc_HighSpeedWire_C', 'amount': 75}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/UraniumCell/Desc_UraniumCell.Desc_UraniumCell_C', 'amount': 35}]
    mManufactoringDuration = 120
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C']
    
