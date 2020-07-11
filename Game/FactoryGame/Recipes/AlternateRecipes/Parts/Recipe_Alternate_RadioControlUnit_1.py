
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_RadioControlUnit_1(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "8BAB377E44A0BBAB3F036D97950C8727", "Alternate: Radio Control System")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumPlateReinforced/Desc_AluminumPlateReinforced.Desc_AluminumPlateReinforced_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ComputerSuper/Desc_ComputerSuper.Desc_ComputerSuper_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/QuartzCrystal/Desc_QuartzCrystal.Desc_QuartzCrystal_C', 'amount': 30}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameLightweight/Desc_ModularFrameLightweight.Desc_ModularFrameLightweight_C', 'amount': 3}]
    mManufactoringDuration = 48
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C']
    
