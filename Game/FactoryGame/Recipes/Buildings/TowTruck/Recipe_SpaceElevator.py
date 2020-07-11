
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_SpaceElevator(FGRecipe):
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 500}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 250}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 400}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 1500}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/SpaceElevator/Desc_SpaceElevator.Desc_SpaceElevator_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Script/FactoryGame.FGBuildGun']
    
