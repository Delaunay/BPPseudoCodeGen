
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_PolyesterFabric(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "4F8C5937400F8319BB2B8880BA3C619E", "Alternate: Polyester Fabric")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/PolymerResin/Desc_PolymerResin.Desc_PolymerResin_C', 'amount': 16}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Water/Desc_Water.Desc_Water_C', 'amount': 10000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GenericBiomass/Desc_Fabric.Desc_Fabric_C', 'amount': 1}]
    mManufactoringDuration = 12
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
