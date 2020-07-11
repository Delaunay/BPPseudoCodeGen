
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_ComputerSuper(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "A6A453EB4F469273A9D3BD9AAE4BDA77", "Supercomputer")
    mDescription = NSLOCTEXT("", "085B560E4A268D57DD382FB613C81CD7", "The supercomputer is the next-gen version of the computer.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ComputerSuper/UI/IconDesc_SuperComputer_64.IconDesc_SuperComputer_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ComputerSuper/UI/IconDesc_SuperComputer_256.IconDesc_SuperComputer_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ComputerSuper/SM_SuperCom_01.SM_SuperCom_01')
    mItemCategory = NewObject[Cat_Communications]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
