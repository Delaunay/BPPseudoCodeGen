
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PureAluminumIngot(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "F9682D2C4F8B10E6C1ED01AE76799F4B", "Alternate: Pure Aluminum Ingot")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumScrap/Desc_AluminumScrap.Desc_AluminumScrap_C', 'amount': 12}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumIngot/Desc_AluminumIngot.Desc_AluminumIngot_C', 'amount': 3}]
    mManufactoringDuration = 5
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/SmelterMk1/Build_SmelterMk1.Build_SmelterMk1_C']
    
