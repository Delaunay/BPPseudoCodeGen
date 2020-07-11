
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_SteelRod(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "983F68D5469149079D1444AC28A36E20", "Alternate: Steel Rod")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelIngot/Desc_SteelIngot.Desc_SteelIngot_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 4}]
    mManufactoringDuration = 5
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C']
    
