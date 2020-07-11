
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_ManufacturerMk1(FGRecipe):
    mDisplayName = NSLOCTEXT("", "46DABCF742E6FE134D8C6793B2E72FE6", "Complex Constructor")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Motor/Desc_Motor.Desc_Motor_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Plastic/Desc_Plastic.Desc_Plastic_C', 'amount': 50}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Desc_ManufacturerMk1.Desc_ManufacturerMk1_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
