
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_Screw_2(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "071E204D4FF6DF6B18F9439ED0A26DD7", "Alternate: Steel Screw")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlate/Desc_SteelPlate.Desc_SteelPlate_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronScrew/Desc_IronScrew.Desc_IronScrew_C', 'amount': 52}]
    mManufactoringDuration = 12
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C']
    
