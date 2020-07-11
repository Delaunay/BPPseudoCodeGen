
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Ramp_Diagonal_8x4_01(FGRecipe):
    mDisplayName = NSLOCTEXT("", "8B2C8B4E4D83A873DA3AF39C720181E2", "Ramp 1a")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 4}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Building/Ramp/Desc_Ramp_Diagonal_8x4_01.Desc_Ramp_Diagonal_8x4_01_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
