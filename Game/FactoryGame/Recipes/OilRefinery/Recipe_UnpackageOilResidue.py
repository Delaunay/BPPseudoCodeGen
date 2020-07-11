
from codegen.ue4_stub import *

from Script.FactoryGame import FGRecipe

class Recipe_UnpackageOilResidue(FGRecipe):
    mDisplayNameOverride = True
    mDisplayName = NSLOCTEXT("", "F643E69D455CF931FE0924B5038679B7", "Unpackage Heavy Oil Residue")
    mIngredients = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HeavyOilResidue/Desc_PackagedOilResidue.Desc_PackagedOilResidue_C', 'amount': 2}]
    mProduct = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HeavyOilResidue/Desc_HeavyOilResidue.Desc_HeavyOilResidue_C', 'amount': 2000}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/FluidCanister/Desc_FluidCanister.Desc_FluidCanister_C', 'amount': 2}]
    mManufactoringDuration = 6
    mManualManufacturingMultiplier = 1
    mProducedIn = ['/Game/FactoryGame/Buildable/Factory/OilRefinery/Build_OilRefinery.Build_OilRefinery_C']
    
