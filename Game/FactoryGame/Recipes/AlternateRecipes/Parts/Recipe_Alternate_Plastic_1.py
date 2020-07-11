
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_Plastic_1(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "D7D7F22D4BA14900308334BD8E9312BB", "Alternate: Recycled Plastic")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Rubber/Desc_Rubber.Desc_Rubber_C', 'amount': 6}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Fuel/Desc_LiquidFuel.Desc_LiquidFuel_C', 'amount': 6000}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Plastic/Desc_Plastic.Desc_Plastic_C', 'amount': 12}]
    mManufactoringDuration = 12
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
