
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class BP_EquipmentDescriptorRifle(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_Rifle]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "9FDA375E441EBEF47E4FDF8810E136FF", "Rifle")
    mDescription = NSLOCTEXT("", "F050C23E4FA8D248CE98DA9DC1248506", "Slot: Hands\r\nAmmo: Rifle Cartridges\r\n\r\nRapid fire weapon for self-defense. Has a mag size of 10.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/Rifle/UI/RifleMk1_64.RifleMk1_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/Rifle/UI/RifleMk1_256.RifleMk1_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/Rifle/Mesh/SpaceRifle_PickupMesh.SpaceRifle_PickupMesh')
    mItemCategory = NewObject[Cat_Hands]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
