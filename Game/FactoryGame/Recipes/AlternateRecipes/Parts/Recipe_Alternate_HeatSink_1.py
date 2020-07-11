
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_HeatSink_1(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "98508EEE46C64BAE0025118FD55B6EE7", "Alternate: Heat Exchanger")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumPlate/Desc_AluminumPlate.Desc_AluminumPlate_C', 'amount': 20}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperSheet/Desc_CopperSheet.Desc_CopperSheet_C', 'amount': 30}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumPlateReinforced/Desc_AluminumPlateReinforced.Desc_AluminumPlateReinforced_C', 'amount': 7}]
    mManufactoringDuration = 32
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C']
    
