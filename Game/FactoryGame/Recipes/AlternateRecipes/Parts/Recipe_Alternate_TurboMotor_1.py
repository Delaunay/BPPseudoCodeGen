
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_TurboMotor_1(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "A7016AF349DD1DD2B09BAFAB5FA746C8", "Alternate: Turbo Rigour Motor")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Motor/Desc_Motor.Desc_Motor_C', 'amount': 7}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameLightweight/Desc_ModularFrameLightweight.Desc_ModularFrameLightweight_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/CircuitBoardHighSpeed/Desc_CircuitBoardHighSpeed.Desc_CircuitBoardHighSpeed_C', 'amount': 9}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Stator/Desc_Stator.Desc_Stator_C', 'amount': 7}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/MotorLightweight/Desc_MotorLightweight.Desc_MotorLightweight_C', 'amount': 3}]
    mManufactoringDuration = 64
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C']
    
