
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_OreBauxite(FGRecipe):
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/OreBauxite/Desc_OreBauxite.Desc_OreBauxite_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/OreBauxite/Desc_OreBauxite.Desc_OreBauxite_C', 'amount': 1}]
    mManufactoringDuration = 2
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/Converter/Build_Converter.Build_Converter_C']
    
