
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_Cable(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "716869C14B17B82C97DEC080C5756DEE", "Cable")
    mDescription = NSLOCTEXT("", "F5526A6648554D1B03BC47A7320B8197", "Used for crafting.\r\nPrimarily used to build power lines.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Cable/UI/IconDesc_Cables_64.IconDesc_Cables_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Cable/UI/IconDesc_Cables_256.IconDesc_Cables_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Cable/Mesh/SM_Cable_01.SM_Cable_01')
    mItemCategory = NewObject[Cat_Electronics]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
