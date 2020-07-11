
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PipeHyper(FGRecipe):
    mDisplayName = NSLOCTEXT("", "63830CA14FBF7E868B9A95BBAEFA8DB5", "Hyper")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperSheet/Desc_CopperSheet.Desc_CopperSheet_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/PipeHyper/Desc_PipeHyper.Desc_PipeHyper_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
