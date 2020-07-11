
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class ResourceSink_DoorWalls_Normal(FGSchematic):
    mType = ESchematicType::EST_ResourceSink
    mDisplayName = NSLOCTEXT("", "1605954D4D9DC5FA5435BB9CFEA7AF21", "Door Walls")
    mSchematicCategory = NewObject[SC_RSS_Walls]()
    mSubCategories = ['/Game/FactoryGame/Schematics/ResourceSinkShopCategories/SC_RSS_Walls.SC_RSS_Walls_C']
    mTechTier = 1
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ResourceSinkCoupon/Desc_ResourceSinkCoupon.Desc_ResourceSinkCoupon_C', 'amount': 2}]
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockRecipe.BP_UnlockRecipe_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockRecipe_C_0', 'mRecipes': ['/Game/FactoryGame/Recipes/Buildings/Walls/Recipe_Wall_Door_8x4_01.Recipe_Wall_Door_8x4_01_C', '/Game/FactoryGame/Recipes/Buildings/Walls/Recipe_Wall_Door_8x4_02.Recipe_Wall_Door_8x4_02_C', '/Game/FactoryGame/Recipes/Buildings/Walls/Recipe_Wall_Door_8x4_03.Recipe_Wall_Door_8x4_03_C', '/Game/FactoryGame/Recipes/Buildings/Walls/Recipe_Wall_Gate_8x4_01.Recipe_Wall_Gate_8x4_01_C']}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Building/Wall/UI/Wall_Door_Center_Orange_256.Wall_Door_Center_Orange_256'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
