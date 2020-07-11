
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_ConveyorLiftMk3(FGRecipe):
    mDisplayName = NSLOCTEXT("", "85F8ABF944F5064C0C1D40B9BBD0574B", "Conveyor Belt")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlate/Desc_SteelPlate.Desc_SteelPlate_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/ConveyorLiftMk3/Desc_ConveyorLiftMk3.Desc_ConveyorLiftMk3_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
