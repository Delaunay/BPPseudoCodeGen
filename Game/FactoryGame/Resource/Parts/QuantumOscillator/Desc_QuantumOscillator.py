
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_QuantumOscillator(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "A2FF45C34790BBC3E31829856B89BB95", "Superposition Oscillator")
    mDescription = NSLOCTEXT("", "2A921E9045304CDA3DDFA69AD33277B1", "A superposition oscillator is an oscillator circuit that uses the mechanical resonance of a vibrating crystal to create a string vibration with a precise frequency. Often used in teleportation technology and dimensional manipulation.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SuperpositionOscillator/UI/IconDesc_SuperPositionOscillator_64.IconDesc_SuperPositionOscillator_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SuperpositionOscillator/UI/IconDesc_SuperPositionOscillator_256.IconDesc_SuperPositionOscillator_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SuperpositionOscillator/SM_SuperpositionOscillator_01.SM_SuperpositionOscillator_01')
    mItemCategory = NewObject[Cat_Quantum]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
