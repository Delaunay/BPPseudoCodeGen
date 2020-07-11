
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_Screw(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "957302C146A322C1E479BD8A06F2B6A0", "Alternate: Casted Screw")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronIngot/Desc_IronIngot.Desc_IronIngot_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronScrew/Desc_IronScrew.Desc_IronScrew_C', 'amount': 20}]
    mManufactoringDuration = 24
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C']
    
