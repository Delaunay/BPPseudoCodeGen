
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_IronScrew(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "F86C5F2A426AE1A985229B8CAC9854E1", "Screw")
    mDescription = NSLOCTEXT("", "C926DDB24C3B8F9E2EBD5094668292A3", "Used for crafting.\r\nOne of the most basic parts.")
    mStackSize = EStackSize::SS_HUGE
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/IronScrew/UI/IconDesc_IronScrews_64.IconDesc_IronScrews_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/IronScrew/UI/IconDesc_IronScrews_256.IconDesc_IronScrews_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/IronScrew/SM_IronScrew_01.SM_IronScrew_01')
    mItemCategory = NewObject[Cat_StandardParts]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
