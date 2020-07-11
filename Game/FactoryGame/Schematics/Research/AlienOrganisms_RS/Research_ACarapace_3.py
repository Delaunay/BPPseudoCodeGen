
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Research_ACarapace_3(FGSchematic):
    mType = ESchematicType::EST_MAM
    mDisplayName = NSLOCTEXT("", "D7D87CB04093C5FB0F0C959D74E12F95", "Expanded Toolbelt")
    mSchematicCategory = NewObject[SC_Organisation]()
    mTechTier = 3
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/AnimalParts/Desc_HogParts.Desc_HogParts_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Wire/Desc_Wire.Desc_Wire_C', 'amount': 1000}]
    mTimeToComplete = 300
    mUnlocks = [{'$ObjectClass': '/Game/FactoryGame/Unlocks/BP_UnlockArmEquipmentSlot.BP_UnlockArmEquipmentSlot_C', '$ObjectFlags': 2621481, '$ObjectName': 'BP_UnlockArmEquipmentSlot_C_0', 'mNumArmEquipmentSlotsToUnlock': 1}]
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Interface/UI/Assets/Shared/ThumbsUp_64.ThumbsUp_64'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
