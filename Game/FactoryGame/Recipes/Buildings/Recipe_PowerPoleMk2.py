
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PowerPoleMk2(FGRecipe):
    mDisplayName = NSLOCTEXT("", "B174E83B4D2DAA15F34A22ACB9582C5E", "Big Power Pole")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedWire/Desc_HighSpeedWire.Desc_HighSpeedWire_C', 'amount': 6}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/PowerPoleMk2/Desc_PowerPoleMk2.Desc_PowerPoleMk2_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
