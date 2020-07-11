
from codegen.ue4_stub import *

from Script.FactoryGame import FGSchematic

class Research_AOrganisms_1(FGSchematic):
    mType = ESchematicType::EST_MAM
    mDisplayName = NSLOCTEXT("", "3A58EF5B4FD427122239A9BA0ACD6105", "Object Scanner Improvements")
    mSchematicCategory = NewObject[SC_Organisation]()
    mTechTier = 3
    mCost = [{'ItemClass': '/Game/FactoryGame/Resource/Parts/CrystalOscillator/Desc_CrystalOscillator.Desc_CrystalOscillator_C', 'amount': 5}, {'ItemClass': '/Game/FactoryGame/Resource/Parts/Stator/Desc_Stator.Desc_Stator_C', 'amount': 10}, {'ItemClass': '/Game/FactoryGame/Resource/Equipment/GemstoneScanner/BP_EquipmentDescriptorObjectScanner.BP_EquipmentDescriptorObjectScanner_C', 'amount': 1}]
    mTimeToComplete = 3
    mSchematicIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Interface/UI/InGame/-Shared/Mam_Key_64.Mam_Key_64'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    
