
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_HyperTubeWallHole(FGRecipe):
    mDisplayName = NSLOCTEXT("", "BDB37E474499EB24DD74B7A4F6D4E5DF", "Conveyor Pole")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/HyperTubeWallSupport/Desc_HyperTubeWallHole.Desc_HyperTubeWallHole_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
