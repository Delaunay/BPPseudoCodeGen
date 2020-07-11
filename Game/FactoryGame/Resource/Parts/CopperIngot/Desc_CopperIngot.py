
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_CopperIngot(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "699130B545EF577CB534D89256F587D2", "Copper Ingot")
    mDescription = NSLOCTEXT("", "B239C223423284ED45ECF6B507A70118", "Used for crafting.\r\nCrafted into the most basic parts.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CopperIngot/UI/IconDesc_CopperIngot_64.IconDesc_CopperIngot_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CopperIngot/UI/IconDesc_CopperIngot_256.IconDesc_CopperIngot_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CopperIngot/SM_CopperIngot_01.SM_CopperIngot_01')
    mItemCategory = NewObject[Cat_Ingots]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
