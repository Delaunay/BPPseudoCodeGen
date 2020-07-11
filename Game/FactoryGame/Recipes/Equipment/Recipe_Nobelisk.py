
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Nobelisk(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "9122028C4AD22B106B05958592AD80E6", "Nobelisk")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GunPowder/Desc_Gunpowder.Desc_Gunpowder_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SteelPipe/Desc_SteelPipe.Desc_SteelPipe_C', 'amount': 10}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/NobeliskExplosive/Desc_NobeliskExplosive.Desc_NobeliskExplosive_C', 'amount': 1}]
    mManufactoringDuration = 20
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C', '/Game/FactoryGame/Buildable/Factory/AssemblerMk1/Build_AssemblerMk1.Build_AssemblerMk1_C']
    
