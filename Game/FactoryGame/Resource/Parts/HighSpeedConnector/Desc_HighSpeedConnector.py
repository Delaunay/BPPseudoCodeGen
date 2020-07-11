
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_HighSpeedConnector(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "75A1FAFF41A1E47365411E883E6BA88B", "High-Speed Connector")
    mDescription = NSLOCTEXT("", "FE0E8F914C6A8A86EBEB39875CEE3C7E", "The high-speed connector connects several cables and wires in a very efficient way. Uses a standard pattern so its applications are many and varied.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HighSpeedConnector/UI/IconDesc_HighSpeedConnector_64.IconDesc_HighSpeedConnector_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HighSpeedConnector/UI/IconDesc_HighSpeedConnector_256.IconDesc_HighSpeedConnector_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HighSpeedConnector/SM_HighSpeedConnector_01.SM_HighSpeedConnector_01')
    mItemCategory = NewObject[Cat_Electronics]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
