﻿
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_QuartzCrystal(FGRecipe):
    mDisplayName = NSLOCTEXT("", "D18E0A7D41DD230FCC731893FD54F0A0", "Quartz Crystal")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/RawQuartz/Desc_RawQuartz.Desc_RawQuartz_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/QuartzCrystal/Desc_QuartzCrystal.Desc_QuartzCrystal_C', 'amount': 3}]
    mManufactoringDuration = 8
    mManualManufacturingMultiplier = 2
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Script/FactoryGame.FGBuildableAutomatedWorkBench']
    
