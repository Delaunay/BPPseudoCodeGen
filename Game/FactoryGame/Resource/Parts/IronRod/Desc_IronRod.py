
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_IronRod(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "F636CC1047E4C1E1C65B6B92763EBB27", "Iron Rod")
    mDescription = NSLOCTEXT("", "DA83EF8541AF89BD0B45F9BFCF111944", "Used for crafting.\r\nOne of the most basic parts.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/IronRod/UI/IconDesc_IronRods_64.IconDesc_IronRods_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/IronRod/UI/IconDesc_IronRods_256.IconDesc_IronRods_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/IronRod/Mesh/SM_IronRod_01.SM_IronRod_01')
    mItemCategory = NewObject[Cat_StandardParts]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
