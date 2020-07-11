
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_ConveyorBeltMk2(FGRecipe):
    mDisplayName = NSLOCTEXT("", "85F8ABF944F5064C0C1D40B9BBD0574B", "Conveyor Belt")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk2/Desc_ConveyorBeltMk2.Desc_ConveyorBeltMk2_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
