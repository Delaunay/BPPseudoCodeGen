
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class Desc_DowsingStick(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_DowsingStick]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "A0D960E94B9C50A10BF6F2889DD55736", "Dowsing stick")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Assets/Shared/0_White.0_White')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Interface/UI/Assets/Shared/0_White.0_White')
    mItemCategory = NewObject[Cat_Equipment]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
