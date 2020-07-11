
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_Wire_1(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "34723FF04485F7A5B719D992BD617B5E", "Alternate: Iron Wire")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronIngot/Desc_IronIngot.Desc_IronIngot_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 9}]
    mManufactoringDuration = 24
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C']
    
