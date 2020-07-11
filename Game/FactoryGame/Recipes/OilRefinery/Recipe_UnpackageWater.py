
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_UnpackageWater(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "4A3D4CF64CA269F20FD0B68789EB9A53", "Unpackage Water")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/Water/Desc_PackagedWater.Desc_PackagedWater_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/RawResources/Water/Desc_Water.Desc_Water_C', 'amount': 2000}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/FluidCanister/Desc_FluidCanister.Desc_FluidCanister_C', 'amount': 2}]
    mManufactoringDuration = 1
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
