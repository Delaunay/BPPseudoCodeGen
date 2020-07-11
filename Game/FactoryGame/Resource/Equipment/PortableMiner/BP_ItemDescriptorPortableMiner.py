
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class BP_ItemDescriptorPortableMiner(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_PortableMinerDispenser]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "B0C5FAF440E928D3E216818A3C8C70D3", "Portable Miner")
    mDescription = NSLOCTEXT("", "BECE828A453B4CF97714448737553C36", "Slot: Hands\r\n\r\nCan be set up on a resource node to automatically extract the resource. Very limited storage space.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Equipment/PortableMiner/UI/PortableMiner_64.PortableMiner_64'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Equipment/PortableMiner/UI/PortableMiner_64.PortableMiner_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/PortableMiner_256.PortableMiner_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/PortableMiner/Mesh/PortableMiner_Folded_static.PortableMiner_Folded_static')
    mItemCategory = NewObject[Cat_Hands]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
