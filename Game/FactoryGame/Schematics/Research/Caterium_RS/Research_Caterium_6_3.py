
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Research_Caterium_6_3(FGSchematic):
    mType = ESchematicType::EST_MAM
    mDisplayName = NSLOCTEXT("", "EB49ABFE4C7C17AA6BA31DB8CE1B2986", "Inflated Pocket Dimension")
    mSchematicCategory = NewObject[SC_Production]()
    mTechTier = 3
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/HighSpeedConnector/Desc_HighSpeedConnector.Desc_HighSpeedConnector_C', 'amount': 50}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Motor/Desc_Motor.Desc_Motor_C', 'amount': 50}]
    mTimeToComplete = 180
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockInventorySlot.BP_UnlockInventorySlot_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockInventorySlot_C_0', 'mNumInventorySlotsToUnlock': 5}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Interface/UI/Assets/Shared/ThumbsUp_64.ThumbsUp_64'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
