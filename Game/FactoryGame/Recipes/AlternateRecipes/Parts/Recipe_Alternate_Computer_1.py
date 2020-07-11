
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_Computer_1(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "9B31B2484D165F780D975DB07A6063E8", "Alternate: Caterium Computer")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CircuitBoard/Desc_CircuitBoard.Desc_CircuitBoard_C', 'amount': 7}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedWire/Desc_HighSpeedWire.Desc_HighSpeedWire_C', 'amount': 28}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 12}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Computer/Desc_Computer.Desc_Computer_C', 'amount': 1}]
    mManufactoringDuration = 16
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C']
    
