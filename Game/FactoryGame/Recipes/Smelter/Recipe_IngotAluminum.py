
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_IngotAluminum(FGRecipe):
    mDisplayName = NSLOCTEXT("", "5375C8454153987A73C4CD9E97A6B38E", "Aluminum Ingot")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumScrap/Desc_AluminumScrap.Desc_AluminumScrap_C', 'amount': 12}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Silica/Desc_Silica.Desc_Silica_C', 'amount': 7}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumIngot/Desc_AluminumIngot.Desc_AluminumIngot_C', 'amount': 4}]
    mManufactoringDuration = 3
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/FoundryMk1/Build_FoundryMk1.Build_FoundryMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C']
    
