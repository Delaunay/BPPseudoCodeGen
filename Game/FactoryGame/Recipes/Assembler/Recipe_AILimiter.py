
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_AILimiter(FGRecipe):
    mDisplayName = NSLOCTEXT("", "686F2E1840B8D0C6EBFB9CA14FBC784C", "Advanced Circuit Board")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CopperSheet/Desc_CopperSheet.Desc_CopperSheet_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedWire/Desc_HighSpeedWire.Desc_HighSpeedWire_C', 'amount': 20}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CircuitBoardHighSpeed/Desc_CircuitBoardHighSpeed.Desc_CircuitBoardHighSpeed_C', 'amount': 1}]
    mManufactoringDuration = 12
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
