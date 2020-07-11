
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_AdheredIronPlate(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "0662C5D0454D2CB8B2A701881A4CF107", "Alternate: Adhered Iron Plate")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 3}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 1}]
    mManufactoringDuration = 16
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C']
    
