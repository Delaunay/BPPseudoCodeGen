
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_NobeliskExplosive(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "80A48EB743C00652ABDE80B9D83B48FB", "Nobelisk")
    mDescription = NSLOCTEXT("", "E3B104F3408348E3584B93BB1CD4FF18", "Can be used with the Nobelisk Detonator to blow up cracked boulders, vegetation or other vulnerable targets.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/NobeliskExplosive/UI/IconDesc_Explosive_64.IconDesc_Explosive_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/NobeliskExplosive/UI/IconDesc_Explosive_256.IconDesc_Explosive_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/NobeliskDetonator/Mesh/NobeliskExplosive.NobeliskExplosive')
    mItemCategory = NewObject[Cat_Equipment]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
