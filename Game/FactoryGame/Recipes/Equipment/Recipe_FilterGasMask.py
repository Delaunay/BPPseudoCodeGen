
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_FilterGasMask(FGRecipe):
    mDisplayName = NSLOCTEXT("", "AB5FD96646ABBA7980D0569A8DECAD01", "Filter")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/Coal/Desc_Coal.Desc_Coal_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_Fabric.Desc_Fabric_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Filter/Desc_Filter.Desc_Filter_C', 'amount': 1}]
    mManufactoringDuration = 8
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/ManufacturerMk1/Build_ManufacturerMk1.Build_ManufacturerMk1_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkBenchComponent.BP_WorkBenchComponent_C', '/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
