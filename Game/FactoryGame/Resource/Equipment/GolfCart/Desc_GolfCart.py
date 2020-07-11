
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class Desc_GolfCart(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_GolfCartDispenser]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "D863047C45F0535E462EDC9A66A72CC9", "Factory Cart™")
    mDescription = NSLOCTEXT("", "2EC405E64F4B8D3029A85998CBA91C3B", "The one and only FICSIT Factory Cart™\r\nNow with special - FICIST Foundation only - Grip Wheels, for an even smoother and faster factory floor experience!")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Equipment/GolfCart/UI/GolfCart_64.GolfCart_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Equipment/GolfCart/UI/GolfCart_256.GolfCart_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/GolfCart/Mesh/SM_GolfcartEquipment_01.SM_GolfcartEquipment_01')
    mItemCategory = NewObject[Cat_Hands]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
