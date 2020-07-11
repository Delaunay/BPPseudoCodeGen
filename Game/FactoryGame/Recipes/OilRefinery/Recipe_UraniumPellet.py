
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_UraniumPellet(FGRecipe):
    mDisplayName = NSLOCTEXT("", "8CADC224429A0060BF416783C132484D", "Fuel")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/OreUranium/Desc_OreUranium.Desc_OreUranium_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SulfuricAcid/Desc_SulfuricAcid.Desc_SulfuricAcid_C', 'amount': 8000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/UraniumPellet/Desc_UraniumPellet.Desc_UraniumPellet_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/SulfuricAcid/Desc_SulfuricAcid.Desc_SulfuricAcid_C', 'amount': 2000}]
    mManufactoringDuration = 6
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
