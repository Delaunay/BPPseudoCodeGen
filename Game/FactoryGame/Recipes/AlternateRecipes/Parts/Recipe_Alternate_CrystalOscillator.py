
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_CrystalOscillator(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "5912CC7C4FB4A0278A9CC3A42651BBFB", "Alternate: Insulated Crystal Oscillator")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/QuartzCrystal/Desc_QuartzCrystal.Desc_QuartzCrystal_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 7}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CircuitBoardHighSpeed/Desc_CircuitBoardHighSpeed.Desc_CircuitBoardHighSpeed_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CrystalOscillator/Desc_CrystalOscillator.Desc_CrystalOscillator_C', 'amount': 1}]
    mManufactoringDuration = 32
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C']
    
