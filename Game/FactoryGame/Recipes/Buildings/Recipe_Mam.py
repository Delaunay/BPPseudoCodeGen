
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Mam(FGRecipe):
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 15}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 45}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/Mam/Desc_Mam.Desc_Mam_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
