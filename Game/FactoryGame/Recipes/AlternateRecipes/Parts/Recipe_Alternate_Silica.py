
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_Silica(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "7D5002CC4ED54A2B7A99F18468B3A028", "Alternate: Cheap Silica")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/RawQuartz/Desc_RawQuartz.Desc_RawQuartz_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Stone/Desc_Stone.Desc_Stone_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Silica/Desc_Silica.Desc_Silica_C', 'amount': 7}]
    mManufactoringDuration = 16
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C']
    
