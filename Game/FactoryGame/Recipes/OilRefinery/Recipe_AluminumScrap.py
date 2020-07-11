
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_AluminumScrap(FGRecipe):
    mDisplayName = NSLOCTEXT("", "8CADC224429A0060BF416783C132484D", "Fuel")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Alumina/Desc_AluminaSolution.Desc_AluminaSolution_C', 'amount': 4000}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/PetroleumCoke/Desc_PetroleumCoke.Desc_PetroleumCoke_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumScrap/Desc_AluminumScrap.Desc_AluminumScrap_C', 'amount': 6}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Water/Desc_Water.Desc_Water_C', 'amount': 1000}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
