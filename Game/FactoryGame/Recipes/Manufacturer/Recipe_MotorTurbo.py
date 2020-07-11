
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_MotorTurbo(FGRecipe):
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AluminumPlateReinforced/Desc_AluminumPlateReinforced.Desc_AluminumPlateReinforced_C', 'amount': 4}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameLightweight/Desc_ModularFrameLightweight.Desc_ModularFrameLightweight_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Motor/Desc_Motor.Desc_Motor_C', 'amount': 4}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 24}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/MotorLightweight/Desc_MotorLightweight.Desc_MotorLightweight_C', 'amount': 1}]
    mManufactoringDuration = 32
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
