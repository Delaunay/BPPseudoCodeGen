
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_Rotor(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "0515762A4B35ADCC1897EA955C2B6083", "Rotor")
    mDescription = NSLOCTEXT("", "5F40202F43285A9754D5FA9313D1E6AA", "Used for crafting.\r\nThe moving parts of a motor.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Rotor/UI/IconDesc_Rotor_64.IconDesc_Rotor_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Rotor/UI/IconDesc_Rotor_256.IconDesc_Rotor_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Rotor/SM_Rotor_01.SM_Rotor_01')
    mItemCategory = NewObject[Cat_IndustrialParts]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
