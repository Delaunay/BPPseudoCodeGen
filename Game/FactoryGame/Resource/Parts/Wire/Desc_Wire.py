
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_Wire(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "B26AF15A4B6C6A2B86A5BCB05C1C0150", "Wire")
    mDescription = NSLOCTEXT("", "5417E1CA48C8698434FC869B9B09884B", "Used for crafting.\r\nOne of the most basic parts.")
    mStackSize = EStackSize::SS_HUGE
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Wire/UI/IconDesc_Wire_64.IconDesc_Wire_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Wire/UI/IconDesc_Wire_256.IconDesc_Wire_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Wire/SM_Wire_01.SM_Wire_01')
    mItemCategory = NewObject[Cat_Electronics]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
