
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_QuartzCrystal(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "E8CD33CC4193B199528F72BEC3F15850", "Quartz Crystal")
    mDescription = NSLOCTEXT("", "44939EC4450A547E87384780E0730965", "Used for radar and quantum technology.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/QuartzCrystal/UI/IconDesc_QuartzResource_64.IconDesc_QuartzResource_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/QuartzCrystal/UI/IconDesc_QuartzResource_256.IconDesc_QuartzResource_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/QuartzCrystal/SM_QuartzCrystal_01.SM_QuartzCrystal_01')
    mItemCategory = NewObject[Cat_Minerals]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
