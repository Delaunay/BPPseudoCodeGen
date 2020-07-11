
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class ResourceSink_HealthPack(FGSchematic):
    mType = ESchematicType::EST_ResourceSink
    mDisplayName = NSLOCTEXT("", "EC1A462D4DD05F9AC04E579766C25F1B", "Health Pack")
    mSchematicCategory = NewObject[SC_RSS_Equipment]()
    mSubCategories = ['/Game/FactoryGame/Schematics/SchematicCategories/SC_Walls.SC_Walls_C']
    mTechTier = 1
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/ResourceSinkCoupon/Desc_ResourceSinkCoupon.Desc_ResourceSinkCoupon_C', 'amount': 1}]
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockGiveItem.BP_UnlockGiveItem_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockGiveItem_C_0', 'mItemsToGive': [{'ItemClass': '/Game/FactoryGame/Resource/Equipment/Medkit/Desc_Medkit.Desc_Medkit_C', 'amount': 5}]}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Resource/Equipment/Medkit/UI/Inhaler_256.Inhaler_256'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSchematicDependencies = [{'$ObjectClass': '/Game/FactoryGame/AvailabilityDependencies/BP_SchematicPurchasedDependency.BP_SchematicPurchasedDependency_C', '$ObjectFlags': 2621440, '$ObjectName': 'BP_SchematicPurchasedDependency_C_0', 'mSchematics': ['/Game/FactoryGame/Schematics/Research/AlienOrganisms_RS/Research_AOrgans_2.Research_AOrgans_2_C', '/Game/FactoryGame/Schematics/Research/Nutrients_RS/Research_Nutrients_4.Research_Nutrients_4_C', '/Game/FactoryGame/Schematics/Research/Mycelia_RS/Research_Mycelia_5.Research_Mycelia_5_C'], 'mRequireAllSchematicsToBePurchased': True}]
    mDependsOnSchematic = NewObject[Research_AOrgans_2]()
    mAdditionalSchematicDependencies = ['/Game/FactoryGame/Schematics/Research/Nutrients_RS/Research_Nutrients_4.Research_Nutrients_4_C', '/Game/FactoryGame/Schematics/Research/Mycelia_RS/Research_Mycelia_5.Research_Mycelia_5_C']
    
