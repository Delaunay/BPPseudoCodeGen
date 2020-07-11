
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_ComputerQuantum(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "9D4E48074DF49C6C95C424A647EF37FB", "Quantum Computer")
    mDescription = NSLOCTEXT("", "A04BA0724F5D545C50C99586B1A3F3A1", "Uses quantum bits instead of normal bits which makes it much faster than a traditional computer.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ComputerQuantum/UI/IconDesc_QuantumComputer_64.IconDesc_QuantumComputer_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ComputerQuantum/UI/IconDesc_QuantumComputer_256.IconDesc_QuantumComputer_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ComputerQuantum/SM_QuantumComputer_01.SM_QuantumComputer_01')
    mItemCategory = NewObject[Cat_Quantum]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
