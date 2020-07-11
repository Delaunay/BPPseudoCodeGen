
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_CopperSheet(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "80A45546416416AF5BB55EA854A67E65", "Copper Sheet")
    mDescription = NSLOCTEXT("", "C827FE8B4673B545E3443B8245AB9675", "Used for crafting.\r\nPrimarily used for pipelines due to its high corrosion resistance.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CopperSheet/UI/IconDesc_CopperSheet_64.IconDesc_CopperSheet_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CopperSheet/UI/IconDesc_CopperSheet_256.IconDesc_CopperSheet_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CopperSheet/SM_CopperSheet_01.SM_CopperSheet_01')
    mItemCategory = NewObject[Cat_StandardParts]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
