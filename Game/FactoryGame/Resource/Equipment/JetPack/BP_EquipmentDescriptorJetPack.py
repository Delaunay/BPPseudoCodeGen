
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class BP_EquipmentDescriptorJetPack(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_JetPack]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "8EB0B1AD4CE903AA8BDE8C88EAA0C671", "Jetpack")
    mDescription = NSLOCTEXT("", "5BEFEF6E417457392C28EAB2694C60A9", "Slot: Body\r\n\r\nAllows you to move more freely in the air. Consumes Fuel when used and refills with Fuel from your inventory when you\'re on the ground.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/JetPack/UI/Jetpack_64.Jetpack_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/JetPack/UI/Jetpack_256.Jetpack_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/JetPack/Mesh/Jetpack_Groundmesh.Jetpack_Groundmesh')
    mItemCategory = NewObject[Cat_Body]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
