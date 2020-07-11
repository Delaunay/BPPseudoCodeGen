
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class ResourceSink_Biofuel(FGSchematic):
    mType = ESchematicType::EST_ResourceSink
    mDisplayName = NSLOCTEXT("", "2F52615E4E6132E94CE429B06EB38A33", "Biofuel")
    mSchematicCategory = NewObject[SC_RSS_Parts]()
    mSubCategories = ['/Game/FactoryGame/Schematics/ResourceSinkShopCategories/SC_RSS_Biomass.SC_RSS_Biomass_C']
    mTechTier = 1
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ResourceSinkCoupon/Desc_ResourceSinkCoupon.Desc_ResourceSinkCoupon_C', 'amount': 2}]
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockGiveItem.BP_UnlockGiveItem_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockGiveItem_C_0', 'mItemsToGive': [{'ItemClass': '/Game/FactoryGame/Resource/Parts/BioFuel/Desc_Biofuel.Desc_Biofuel_C', 'amount': 200}]}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Resource/Parts/SolidBiofuel/UI/IconDesc_SolidBiofuel_256.IconDesc_SolidBiofuel_256'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSchematicDependencies = [{'$ObjectClass': '/Game/FactoryGame/AvailabilityDependencies/BP_SchematicPurchasedDependency.BP_SchematicPurchasedDependency_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_SchematicPurchasedDependency_C_0', 'mSchematics': ['/Game/FactoryGame/Schematics/Progression/Schematic_2-2.Schematic_2-2_C'], 'mRequireAllSchematicsToBePurchased': True}]
    mDependsOnSchematic = NewObject[Schematic_2-2]()
    
