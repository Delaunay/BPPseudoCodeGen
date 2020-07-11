
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class ResourceSink_CurvedFoundationPack(FGSchematic):
    mType = ESchematicType::EST_ResourceSink
    mDisplayName = NSLOCTEXT("", "E24A332D451CEE02F02C1D81FDF9BC90", "Quarter Pipes Pack")
    mSchematicCategory = NewObject[SC_RSS_Foundations]()
    mSubCategories = ['/Game/FactoryGame/Schematics/ResourceSinkShopCategories/SC_RSS_Walls.SC_RSS_Walls_C']
    mTechTier = 1
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ResourceSinkCoupon/Desc_ResourceSinkCoupon.Desc_ResourceSinkCoupon_C', 'amount': 8}]
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Foundations/Recipe_QuarterPipe.Recipe_QuarterPipe_C', '/Game/FactoryGame/Recipes/Buildings/Foundations/Recipe_QuarterPipe_02.Recipe_QuarterPipe_02_C', '/Game/FactoryGame/Recipes/Buildings/Foundations/Recipe_QuarterPipeCorner_01.Recipe_QuarterPipeCorner_01_C', '/Game/FactoryGame/Recipes/Buildings/Foundations/Recipe_QuarterPipeCorner_02.Recipe_QuarterPipeCorner_02_C', '/Game/FactoryGame/Recipes/Buildings/Foundations/Recipe_QuarterPipeCorner_03.Recipe_QuarterPipeCorner_03_C', '/Game/FactoryGame/Recipes/Buildings/Foundations/Recipe_QuarterPipeCorner_04.Recipe_QuarterPipeCorner_04_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 512, 'Y': 512}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Building/Ramp/UI/QuarterPipe_01_512.QuarterPipe_01_512'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
