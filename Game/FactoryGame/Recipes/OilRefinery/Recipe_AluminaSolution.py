
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_AluminaSolution(FGRecipe):
    mDisplayName = NSLOCTEXT("", "8CADC224429A0060BF416783C132484D", "Fuel")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/OreBauxite/Desc_OreBauxite.Desc_OreBauxite_C', 'amount': 7}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Water/Desc_Water.Desc_Water_C', 'amount': 10000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Alumina/Desc_AluminaSolution.Desc_AluminaSolution_C', 'amount': 8000}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Silica/Desc_Silica.Desc_Silica_C', 'amount': 2}]
    mManufactoringDuration = 6
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
