
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_PureQuartzCrystal(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "0963770245ADC5A9997B5BA6EFFD22C4", "Alternate: Pure Quartz Crystal")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/RawQuartz/Desc_RawQuartz.Desc_RawQuartz_C', 'amount': 9}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Water/Desc_Water.Desc_Water_C', 'amount': 5000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/QuartzCrystal/Desc_QuartzCrystal.Desc_QuartzCrystal_C', 'amount': 7}]
    mManufactoringDuration = 8
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
