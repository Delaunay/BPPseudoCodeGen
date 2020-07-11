
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_PureCateriumIngot(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "B52A98DD492E1DEF630E8BA372B501AA", "Alternate: Pure Caterium Ingot")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/OreGold/Desc_OreGold.Desc_OreGold_C', 'amount': 2}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Water/Desc_Water.Desc_Water_C', 'amount': 2000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/GoldIngot/Desc_GoldIngot.Desc_GoldIngot_C', 'amount': 1}]
    mManufactoringDuration = 5
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
