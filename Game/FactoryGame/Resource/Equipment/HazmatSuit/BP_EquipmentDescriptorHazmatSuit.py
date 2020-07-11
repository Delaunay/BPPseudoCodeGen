
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class BP_EquipmentDescriptorHazmatSuit(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_HazmatSuit]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "80D1FDC140FBBA01D5BB0DA62D42FE1E", "Hazmat Suit")
    mDescription = NSLOCTEXT("", "2102C03F4A1379DD7F4D6EA98D289BFD", "Slot: Body\r\n\r\nShields you from the adverse effects of radiation. \r\nConsumes Iodine Infused Filters from your inventory when you are in radioactive areas.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HazmatSuit/UI/IconDesc_HazmatSuit_64.IconDesc_HazmatSuit_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HazmatSuit/UI/IconDesc_HazmatSuit_256.IconDesc_HazmatSuit_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HazmatSuit/SM_HazmatSuit_01.SM_HazmatSuit_01')
    mItemCategory = NewObject[Cat_Body]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
