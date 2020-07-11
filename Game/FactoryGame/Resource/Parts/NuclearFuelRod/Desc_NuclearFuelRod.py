
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptorNuclearFuel

class Desc_NuclearFuelRod(FGItemDescriptorNuclearFuel):
    mSpentFuelClass = NewObject[Desc_NuclearWaste]()
    mAmountOfWaste = 25
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "E6B0D2E345B649C9DBEC4DAA8A5B7064", "Nuclear Fuel Rod")
    mDescription = NSLOCTEXT("", "BFF44C874B53122AD9D2E2840B1384B4", "Nuclear Fuel Rods are used as fuel in nuclear reactors.\r\nVERY RADIOACTIVE")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mEnergyValue = 750000
    mRadioactiveDecay = 60
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/NuclearFuelRod/UI/IconDesc_NuclearFuelRod_64.IconDesc_NuclearFuelRod_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/NuclearFuelRod/UI/IconDesc_NuclearFuelRod_256.IconDesc_NuclearFuelRod_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/NuclearFuelRod/SM_NuclearFuelRod_01.SM_NuclearFuelRod_01')
    mItemCategory = NewObject[Cat_Nuclear]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
