
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_CrystalOscillator(FGRecipe):
    mDisplayName = NSLOCTEXT("", "D924108141E7E1B5E6023288A2FA28F5", "Crystal Oscillator")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/QuartzCrystal/Desc_QuartzCrystal.Desc_QuartzCrystal_C', 'amount': 36}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 28}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CrystalOscillator/Desc_CrystalOscillator.Desc_CrystalOscillator_C', 'amount': 2}]
    mManufactoringDuration = 120
    mManualManufacturingMultiplier = 0.30000001192092896
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
