
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_QuantumCrystal(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "732F055945CF85E235754197AC5BB4F4", "Quantum Crystal")
    mDescription = NSLOCTEXT("", "FA786B6C467654448D835EB781F5AEC3", "Quantum Crystals are crystals manipulated to store data in quantum bits. Can store an incredible amount of data.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/QuantumCrystal/UI/IconDesc_QuantumCrystal_64.IconDesc_QuantumCrystal_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/QuantumCrystal/UI/IconDesc_QuantumCrystal_256.IconDesc_QuantumCrystal_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/QuantumCrystal/SM_QuantumCrystal_01.SM_QuantumCrystal_01')
    mItemCategory = NewObject[Cat_Quantum]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
