
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class ResourceSink_StatueGoldenNut(FGSchematic):
    mType = ESchematicType::EST_ResourceSink
    mDisplayName = NSLOCTEXT("", "4CE2CDA547F95D2DE41C8D822A83F7A5", "Golden Nut")
    mSchematicCategory = NewObject[SC_RSS_Statues]()
    mSubCategories = ['/Game/FactoryGame/Schematics/ResourceSinkShopCategories/SC_RSS_Massage-2ABb.SC_RSS_Massage-2ABb_C']
    mTechTier = 1
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ResourceSinkCoupon/Desc_ResourceSinkCoupon.Desc_ResourceSinkCoupon_C', 'amount': 1000}]
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockGiveItem.BP_UnlockGiveItem_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockGiveItem_C_0', 'mItemsToGive': [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/Decoration/Desc_GoldenNut_Statue.Desc_GoldenNut_Statue_C', 'amount': 1}]}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Building/Decor/Statues/UI/Award_Statue_Nut_256.Award_Statue_Nut_256'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
