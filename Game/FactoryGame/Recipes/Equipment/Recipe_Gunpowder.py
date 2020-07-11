
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Gunpowder(FGRecipe):
    mDisplayName = NSLOCTEXT("", "689D2B2240B8B85EA62D4199FF2126BD", "Gunpowder")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/Coal/Desc_Coal.Desc_Coal_C', 'amount': 1}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Sulfur/Desc_Sulfur.Desc_Sulfur_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GunPowder/Desc_Gunpowder.Desc_Gunpowder_C', 'amount': 1}]
    mManufactoringDuration = 8
    mManualManufacturingMultiplier = 0.5
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
