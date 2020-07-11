
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_ConveyorBeltMk1(FGRecipe):
    mDisplayName = NSLOCTEXT("", "85F8ABF944F5064C0C1D40B9BBD0574B", "Conveyor Belt")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk1/Desc_ConveyorBeltMk1.Desc_ConveyorBeltMk1_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
