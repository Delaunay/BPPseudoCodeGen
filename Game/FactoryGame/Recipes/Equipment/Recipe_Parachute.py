
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Parachute(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "EFE1FE074ABC2E0EC6F8328E0FBAFAFA", "Parachute")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_Fabric.Desc_Fabric_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Cable/Desc_Cable.Desc_Cable_C', 'amount': 5}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/Beacon/Desc_Parachute.Desc_Parachute_C', 'amount': 5}]
    mManufactoringDuration = 40
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/-Shared/WorkBench/BP_WorkshopComponent.BP_WorkshopComponent_C']
    
