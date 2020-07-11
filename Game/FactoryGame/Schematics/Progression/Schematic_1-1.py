
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Schematic_1-1(FGSchematic):
    mType = ESchematicType::EST_Milestone
    mDisplayName = NSLOCTEXT("", "D7401BFB40D1577AD511DC9A77DA8951", "Base Building")
    mSchematicCategory = NewObject[SC_Logistics]()
    mTechTier = 1
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/Cement/Desc_Cement.Desc_Cement_C', 'amount': 200}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 100}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 100}]
    mTimeToComplete = 120
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Recipe_LookoutTower.Recipe_LookoutTower_C', '/Game/FactoryGame/Recipes/Buildings/Foundations/Recipe_Foundation_8x1_01.Recipe_Foundation_8x1_01_C', '/Game/FactoryGame/Recipes/Buildings/Foundations/Recipe_Foundation_8x2_01.Recipe_Foundation_8x2_01_C', '/Game/FactoryGame/Recipes/Buildings/Foundations/Recipe_Foundation_8x4_01.Recipe_Foundation_8x4_01_C', '/Game/FactoryGame/Recipes/Buildings/Ramps/Recipe_Ramp_8x1_01.Recipe_Ramp_8x1_01_C', '/Game/FactoryGame/Recipes/Buildings/Ramps/Recipe_Ramp_8x2_01.Recipe_Ramp_8x2_01_C', '/Game/FactoryGame/Recipes/Buildings/Ramps/Recipe_Ramp_8x4_01.Recipe_Ramp_8x4_01_C', '/Game/FactoryGame/Recipes/Buildings/Walls/Recipe_Wall_8x4_01.Recipe_Wall_8x4_01_C', '/Game/FactoryGame/Recipes/Buildings/Walls/Recipe_Wall_8x4_02.Recipe_Wall_8x4_02_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/TradingPost/UI/SchematicIcons/SchematicIcon_Structure.SchematicIcon_Structure'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
