
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_PureIronIngot(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "5619207F4301CCC5BD0DFA83FCA9034F", "Alternate: Pure Iron Ingot")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/OreIron/Desc_OreIron.Desc_OreIron_C', 'amount': 7}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Water/Desc_Water.Desc_Water_C', 'amount': 4000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronIngot/Desc_IronIngot.Desc_IronIngot_C', 'amount': 13}]
    mManufactoringDuration = 12
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
