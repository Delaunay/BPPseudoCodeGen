
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_NuclearFuelRod_1(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "DC7D840445395ED8DF7CC791BB1E0A75", "Alternate: Nuclear Fuel Unit")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/UraniumCell/Desc_UraniumCell.Desc_UraniumCell_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ElectromagneticControlRod/Desc_ElectromagneticControlRod.Desc_ElectromagneticControlRod_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CrystalOscillator/Desc_CrystalOscillator.Desc_CrystalOscillator_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Equipment/Beacon/BP_EquipmentDescriptorBeacon.BP_EquipmentDescriptorBeacon_C', 'amount': 6}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/NuclearFuelRod/Desc_NuclearFuelRod.Desc_NuclearFuelRod_C', 'amount': 3}]
    mManufactoringDuration = 300
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C']
    
