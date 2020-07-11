
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_SpikedRebar(FGRecipe):
    mDisplayName = NSLOCTEXT("", "C28915B24FB438F30987ACA0B4A9837A", "Nailgun Spike")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 1}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/SpikedRebar/Desc_SpikedRebar.Desc_SpikedRebar_C', 'amount': 1}]
    mManufactoringDuration = 4
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ConstructorMk1/Build_ConstructorMk1.Build_ConstructorMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
