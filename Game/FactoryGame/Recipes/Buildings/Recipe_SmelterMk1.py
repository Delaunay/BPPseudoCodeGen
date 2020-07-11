
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_SmelterMk1(FGRecipe):
    mDisplayName = NSLOCTEXT("", "4606ADA9430421B2F4213D95D5512D35", "Smelter")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrame/Desc_ModularFrame.Desc_ModularFrame_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rotor/Desc_Rotor.Desc_Rotor_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 20}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/FoundryMk1/Desc_FoundryMk1.Desc_FoundryMk1_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
