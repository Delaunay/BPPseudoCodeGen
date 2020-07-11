
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_Alternate_DilutedPackagedFuel(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "6984AA104FDFEE048E3745872EB52E20", "Alternate: Diluted Packaged Fuel")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HeavyOilResidue/Desc_HeavyOilResidue.Desc_HeavyOilResidue_C', 'amount': 1000}, {'ItemClass': '/Game/FactoryGame/Resource/RawResources/Water/Desc_PackagedWater.Desc_PackagedWater_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Fuel/Desc_Fuel.Desc_Fuel_C', 'amount': 2}]
    mManufactoringDuration = 2
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
