
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class BP_EquipmentDescriptorNobeliskDetonator(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_NobeliskDetonator]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "6AA29C5E4799A9B82F421E918E9D3CFD", "Nobelisk Detonator")
    mDescription = NSLOCTEXT("", "55B185F8428C691F91086589168D5938", "Slot: Hands\r\nAmmo: Nobelisk\r\n\r\nUsed to blow up cracked boulders, rocks and invasive vegetation.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/NobeliskDetonator/UI/Detonator_64.Detonator_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/NobeliskDetonator/UI/Detonator_256.Detonator_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/NobeliskDetonator/Mesh/NobeliskDetonator.NobeliskDetonator')
    mItemCategory = NewObject[Cat_Hands]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
