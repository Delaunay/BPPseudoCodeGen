
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_HeavyFlexibleFrame(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "E76FC8554F36DF592175908FE696B47F", "Alternate: Heavy Flexible Frame")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrame/Desc_ModularFrame.Desc_ModularFrame_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlateReinforced/Desc_SteelPlateReinforced.Desc_SteelPlateReinforced_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 20}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronScrew/Desc_IronScrew.Desc_IronScrew_C', 'amount': 104}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 1}]
    mManufactoringDuration = 16
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C']
    
