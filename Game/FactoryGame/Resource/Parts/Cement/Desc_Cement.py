
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_Cement(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "EED5C92544637062F7201E9CDA5B8DA0", "Concrete")
    mDescription = NSLOCTEXT("", "BA22177F4AD5BB522B0BEF9BD33FA342", "Used for building.\r\nGood for stable foundations.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Cement/UI/IconDesc_Concrete_64.IconDesc_Concrete_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Cement/UI/IconDesc_Concrete_256.IconDesc_Concrete_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Cement/Mesh/SM_Cement_01.SM_Cement_01')
    mPreviewView = Namespace(CameraPitch=-35, Distance=175, FocalOffset={'X': 0, 'Y': 0, 'Z': 50})
    mItemCategory = NewObject[Cat_Minerals]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
