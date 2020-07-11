
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class BP_EquipmentDescriptorRifleMk2(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_Rifle_Mk2]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "845B8CD9424DA274FC943EAD47C4CAF0", "Rifle Mk.2")
    mDescription = NSLOCTEXT("", "7F6511BA478C0B8C22EC1ABBC55DEE35", "A better rifle!")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/Rifle/UI/RifleMk1_64.RifleMk1_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/Rifle/UI/RifleMk1_256.RifleMk1_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/DefaultItemMesh.DefaultItemMesh')
    mItemCategory = NewObject[Cat_Hands]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
