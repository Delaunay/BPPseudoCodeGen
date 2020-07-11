
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class ResourceSink_InvertedRampPack(FGSchematic):
    mType = ESchematicType::EST_ResourceSink
    mDisplayName = NSLOCTEXT("", "6EEBB09C40106C5831539C865D399707", "Inverted Ramp Pack")
    mSchematicCategory = NewObject[SC_RSS_Foundations]()
    mSubCategories = ['/Game/FactoryGame/Schematics/ResourceSinkShopCategories/SC_RSS_Walls.SC_RSS_Walls_C']
    mTechTier = 1
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ResourceSinkCoupon/Desc_ResourceSinkCoupon.Desc_ResourceSinkCoupon_C', 'amount': 2}]
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Ramps/Recipe_RampInverted_8x1.Recipe_RampInverted_8x1_C', '/Game/FactoryGame/Recipes/Buildings/Ramps/Recipe_RampInverted_8x2_01.Recipe_RampInverted_8x2_01_C', '/Game/FactoryGame/Recipes/Buildings/Ramps/Recipe_Ramp_8x4_Inverted_01.Recipe_Ramp_8x4_Inverted_01_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Building/Ramp/UI/Ramp_8x4_Inverted_256.Ramp_8x4_Inverted_256'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
