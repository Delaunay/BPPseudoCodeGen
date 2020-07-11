
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_FluidCanister(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "C14635E64053EB52D2EC9E88261A16BE", "Empty Canister")
    mDescription = NSLOCTEXT("", "D4E1AD924877C6A6EF5162BD989DA19B", "Used to package fluids for transportation. Can be recycled.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/FluidCanister/UI/IconDesc_EmptyCannister_64.IconDesc_EmptyCannister_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/FluidCanister/UI/IconDesc_EmptyCannister_256.IconDesc_EmptyCannister_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/FluidCanister/SM_FluidCanister_01.SM_FluidCanister_01')
    mItemCategory = NewObject[Cat_Other]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
