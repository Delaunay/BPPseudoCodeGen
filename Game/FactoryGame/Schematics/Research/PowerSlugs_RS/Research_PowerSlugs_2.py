
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Research_PowerSlugs_2(FGSchematic):
    mType = ESchematicType::EST_MAM
    mDisplayName = NSLOCTEXT("", "27BE64B44225044FE7727B93E852A76D", "Overclock Production")
    mSchematicCategory = NewObject[SC_Organisation]()
    mTechTier = 3
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 50}]
    mTimeToComplete = 300
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockBuildOverclock.BP_UnlockBuildOverclock_C', '$ObjectFlags': 2621473, '$ObjectName': 'BP_UnlockBuildOverclock_C_0'}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Interface/UI/Assets/Shared/Overclock_Icon.Overclock_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
