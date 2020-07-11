
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_ElectroAluminumScrap(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "ADF1CFBC4496EE971E401F92B2B8F79B", "Alternate: Electrode - Aluminum Scrap")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Alumina/Desc_AluminaSolution.Desc_AluminaSolution_C', 'amount': 3000}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Coal/Desc_Coal.Desc_Coal_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumScrap/Desc_AluminumScrap.Desc_AluminumScrap_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Water/Desc_Water.Desc_Water_C', 'amount': 1000}]
    mManufactoringDuration = 2
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
