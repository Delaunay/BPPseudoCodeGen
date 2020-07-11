
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_CartridgeStandard(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "0D4257614CB7F24CB6AF34A0DB6E13E7", "Rifle Cartridge")
    mDescription = NSLOCTEXT("", "EDF7B7AD40B50A9EB2D914AE5B8675E3", "Ammo for the Rifle.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CartridgeStandard/UI/Rifle_Magazine_64.Rifle_Magazine_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/CartridgeStandard/UI/Rifle_Magazine_256.Rifle_Magazine_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/Rifle/Mesh/SpaceRifle_Magazine_static.SpaceRifle_Magazine_static')
    mItemCategory = NewObject[Cat_Equipment]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
