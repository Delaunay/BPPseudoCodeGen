
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_CrystalOscillator(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "A2860DFE43D063B913C64294919F78FF", "Crystal Oscillator")
    mDescription = NSLOCTEXT("", "A88AEC554A3C72C9310930A24D611936", "A crystal oscillator is an electronic oscillator circuit that uses the mechanical resonance of a vibrating crystal to create an electrical signal with a precise frequency.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CrystalOscillator/UI/IconDesc_CrystalOscillator_64.IconDesc_CrystalOscillator_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CrystalOscillator/UI/IconDesc_CrystalOscillator_256.IconDesc_CrystalOscillator_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CrystalOscillator/SM_Crystal_Oscillator_01.SM_Crystal_Oscillator_01')
    mItemCategory = NewObject[Cat_Communications]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
