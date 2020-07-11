
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_SulfuricAcid(FGRecipe):
    mDisplayName = NSLOCTEXT("", "8CADC224429A0060BF416783C132484D", "Fuel")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/Sulfur/Desc_Sulfur.Desc_Sulfur_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Water/Desc_Water.Desc_Water_C', 'amount': 5000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SulfuricAcid/Desc_SulfuricAcid.Desc_SulfuricAcid_C', 'amount': 10000}]
    mManufactoringDuration = 6
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
