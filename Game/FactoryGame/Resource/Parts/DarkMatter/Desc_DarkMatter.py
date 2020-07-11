
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_DarkMatter(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "860C151041F41816C7E9D0B5A6B908DD", "Dark Matter")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/DarkMatter/UI/IconDesc_DarkMatter_64.IconDesc_DarkMatter_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/DarkMatter/UI/IconDesc_DarkMatter_256.IconDesc_DarkMatter_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/DarkMatter/SM_DarkMatter_01.SM_DarkMatter_01')
    mItemCategory = NewObject[Cat_Quantum]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
