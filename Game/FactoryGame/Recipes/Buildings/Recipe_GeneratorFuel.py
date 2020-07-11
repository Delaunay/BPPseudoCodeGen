
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_GeneratorFuel(FGRecipe):
    mDisplayName = NSLOCTEXT("", "9189D69E4824333BFD484DABAC4CDE62", "Fuel Generator")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Computer/Desc_Computer.Desc_Computer_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameHeavy/Desc_ModularFrameHeavy.Desc_ModularFrameHeavy_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Motor/Desc_Motor.Desc_Motor_C', 'amount': 15}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedWire/Desc_HighSpeedWire.Desc_HighSpeedWire_C', 'amount': 50}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Buildable/Factory/GeneratorFuel/Desc_GeneratorFuel.Desc_GeneratorFuel_C', 'amount': 1}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Equipment/BuildGun/BP_BuildGun.BP_BuildGun_C']
    
