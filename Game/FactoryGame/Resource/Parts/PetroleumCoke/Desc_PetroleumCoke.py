
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_PetroleumCoke(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "931A9CAD4AB2868B168F0EB5216D8CA1", "Petroleum Coke")
    mDescription = NSLOCTEXT("", "73DA64C14806A81DBADB148D860EE2F1", "Used for crafting.\r\nA carbon-rich material distilled from Heavy Oil Residue. \r\nUsed as a less efficient coal replacement or for aluminum refinement.")
    mStackSize = EStackSize::SS_BIG
    mCanBeDiscarded = True
    mEnergyValue = 180
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/PetroleumCoke/UI/IconDesc_PetroleumCoke_64.IconDesc_PetroleumCoke_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/PetroleumCoke/UI/IconDesc_PetroleumCoke_256.IconDesc_PetroleumCoke_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/PetroleumCoke/SM_PetroleumCoke_01.SM_PetroleumCoke_01')
    mItemCategory = NewObject[Cat_SolidOilProducts]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
