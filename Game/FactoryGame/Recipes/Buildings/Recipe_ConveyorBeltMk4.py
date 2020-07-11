
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_ConveyorBeltMk4(FGRecipe):
    mDisplayName = NSLOCTEXT("", "85F8ABF944F5064C0C1D40B9BBD0574B", "Conveyor Belt")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlateReinforced/Desc_SteelPlateReinforced.Desc_SteelPlateReinforced_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk4/Desc_ConveyorBeltMk4.Desc_ConveyorBeltMk4_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
