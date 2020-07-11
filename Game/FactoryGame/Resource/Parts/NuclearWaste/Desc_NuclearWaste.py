
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_NuclearWaste(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "13F40FB74ABBA1FEF24C408FAE0EAA48", "Nuclear Waste")
    mDescription = NSLOCTEXT("", "66DD601F4D284E598DAAF591563D7A10", "Nuclear Waste is the byproduct of nuclear power plants. You gotta find a way to handle all of this.\r\nEXTREMELY RADIOACTIVE")
    mStackSize = EStackSize::SS_HUGE
    mRadioactiveDecay = 20
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/NuclearWaste/UI/IconDesc_NuclearWaste_64.IconDesc_NuclearWaste_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/NuclearWaste/UI/IconDesc_NuclearWaste_256.IconDesc_NuclearWaste_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/NuclearWaste/SM_NuclearWaste_01.SM_NuclearWaste_01')
    mItemCategory = NewObject[Cat_Nuclear]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
