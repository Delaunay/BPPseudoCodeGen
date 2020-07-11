
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_ElectromagneticControlRod(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "64E8B00B435D087F5A35078942F520E4", "Electromagnetic Control Rod")
    mDescription = NSLOCTEXT("", "ED35424246AAE76B6898EA8A40FFA651", "Control Rods regulate power expenditure via electromagnetism.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ElectromagneticControlRod/UI/IconDesc_ElectromagneticControlRod_64.IconDesc_ElectromagneticControlRod_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ElectromagneticControlRod/UI/IconDesc_ElectromagneticControlRod_256.IconDesc_ElectromagneticControlRod_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ElectromagneticControlRod/SM_ElectromagneticControlRod_01.SM_ElectromagneticControlRod_01')
    mItemCategory = NewObject[Cat_Nuclear]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
