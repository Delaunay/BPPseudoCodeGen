
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class ResourceSink_RadioControlUnit(FGSchematic):
    mType = ESchematicType::EST_ResourceSink
    mDisplayName = NSLOCTEXT("", "74B9DD7E4C4C36DF6BF05BBA02D3B141", "Radio Control Unit")
    mSchematicCategory = NewObject[SC_RSS_Parts]()
    mSubCategories = ['/Game/FactoryGame/Schematics/ResourceSinkShopCategories/SC_RSS_Communications.SC_RSS_Communications_C']
    mTechTier = 1
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ResourceSinkCoupon/Desc_ResourceSinkCoupon.Desc_ResourceSinkCoupon_C', 'amount': 7}]
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockGiveItem.BP_UnlockGiveItem_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockGiveItem_C_0', 'mItemsToGive': [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ModularFrameLightweight/Desc_ModularFrameLightweight.Desc_ModularFrameLightweight_C', 'amount': 50}]}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Resource/Parts/RadioControlUnit/UI/IconDesc_RadioControlUnit_256.IconDesc_RadioControlUnit_256'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSchematicDependencies = [{'$ObjectClass': '/Game/FactoryGame/AvailabilityDependencies/BP_SchematicPurchasedDependency.BP_SchematicPurchasedDependency_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_SchematicPurchasedDependency_C_0', 'mSchematics': ['/Game/FactoryGame/Schematics/Research/Quartz_RS/Research_Quartz_3_3.Research_Quartz_3_3_C'], 'mRequireAllSchematicsToBePurchased': True}]
    mDependsOnSchematic = NewObject[Research_Quartz_3_3]()
    
