
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_PipeHyperStart(FGRecipe):
    mDisplayName = NSLOCTEXT("", "BDB37E474499EB24DD74B7A4F6D4E5DF", "Conveyor Pole")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPlateReinforced/Desc_SteelPlateReinforced.Desc_SteelPlateReinforced_C', 'amount': 4}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rotor/Desc_Rotor.Desc_Rotor_C', 'amount': 4}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 10}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/PipeHyperStart/Desc_PipeHyperStart.Desc_PipeHyperStart_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
