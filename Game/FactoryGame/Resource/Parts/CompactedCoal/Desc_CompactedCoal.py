
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_CompactedCoal(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "00AC56E64A5E12D026084A96A3A38C1E", "Compacted Coal")
    mDescription = NSLOCTEXT("", "295BC0B94A5F7C2DE756C5B37B0B4706", "A much more efficient alternative for Coal. Used as fuel for vehicles & coal generators.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mEnergyValue = 630
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CompactedCoal/UI/CompactedCoal_64.CompactedCoal_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CompactedCoal/UI/CompactedCoal_256.CompactedCoal_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CompactedCoal/SM_CompactedCoal_01.SM_CompactedCoal_01')
    mItemCategory = NewObject[Cat_Minerals]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
