
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_IndustrialTank(FGRecipe):
    mDisplayName = NSLOCTEXT("", "C55B457D44ED9C4440647CB57CED5AE4", "Simple Constructor")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Plastic/Desc_Plastic.Desc_Plastic_C', 'amount': 30}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 3}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/IndustrialFluidContainer/Desc_IndustrialTank.Desc_IndustrialTank_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
