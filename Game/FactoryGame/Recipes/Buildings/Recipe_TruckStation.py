
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_TruckStation(FGRecipe):
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrame/Desc_ModularFrame.Desc_ModularFrame_C', 'amount': 15}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rotor/Desc_Rotor.Desc_Rotor_C', 'amount': 20}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 50}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/TruckStation/Desc_TruckStation.Desc_TruckStation_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
