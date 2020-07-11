
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_HazmatFilter(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "053156674B0420ECD07B8CBBD5A81A7C", "Iodine Infused Filter")
    mDescription = NSLOCTEXT("", "E28147CC42251AF3C38D3298E93366BD", "Used in hazmat suits to filter out radioactive particles in the air.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/IodineInfusedFilter/UI/IconDesc_HazmatFilter_64.IconDesc_HazmatFilter_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/IodineInfusedFilter/UI/IconDesc_HazmatFilter_256.IconDesc_HazmatFilter_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/IodineInfusedFilter/SM_IodineInfusedFilter_01.SM_IodineInfusedFilter_01')
    mItemCategory = NewObject[Cat_Equipment]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
