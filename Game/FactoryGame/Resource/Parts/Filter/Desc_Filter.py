
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_Filter(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "34E5B76146806792CCBAC1B7DDF354DB", "Gas Filter")
    mDescription = NSLOCTEXT("", "F30C79C640A2708895E0F7A7A4368A86", "Used in gas masks to filter out pollutants in the air.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Filter/UI/IconDesc_GasMaskFilter_64.IconDesc_GasMaskFilter_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Filter/UI/IconDesc_GasMaskFilter_256.IconDesc_GasMaskFilter_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/GasMask/Mesh/GasMask_Filter.GasMask_Filter')
    mItemCategory = NewObject[Cat_Equipment]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
