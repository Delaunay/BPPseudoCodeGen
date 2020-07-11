
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_CrystalShard(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "305E3F9A4A52BAC3CE4AE1BD19273834", "Power Shard")
    mDescription = NSLOCTEXT("", "D8AB702D414C74DE397E29BADD9DB3AA", "Mucus from the power slugs compressed into a solid crystal-like shard. \r\nIt radiates a strange power.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Environment/Crystal/UI/PowerShard_64.PowerShard_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Environment/Crystal/UI/PowerShard_256.PowerShard_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/PowerShard/SM_PowerShard_01.SM_PowerShard_01')
    mItemCategory = NewObject[Cat_PowerShards]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
