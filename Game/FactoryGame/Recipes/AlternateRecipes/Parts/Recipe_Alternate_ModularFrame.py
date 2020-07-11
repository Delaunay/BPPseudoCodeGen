
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_ModularFrame(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "3B42E2664237EC04AA2853B62D622A70", "Alternate: Steeled Frame")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 10}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrame/Desc_ModularFrame.Desc_ModularFrame_C', 'amount': 3}]
    mManufactoringDuration = 60
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C']
    
