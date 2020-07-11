
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_IronIngot(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "2041017647939FF8898D7386DEDE62C0", "Iron Ingot")
    mDescription = NSLOCTEXT("", "3F3E69E64F155FBFB826798BDD8A891B", "Used for crafting.\r\nCrafted into the most basic parts.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/IronIngot/UI/IconDesc_IronIngot_64.IconDesc_IronIngot_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/IronIngot/UI/IconDesc_IronIngot_256.IconDesc_IronIngot_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/IronIngot/SM_IronIngot_01.SM_IronIngot_01')
    mItemCategory = NewObject[Cat_Ingots]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
