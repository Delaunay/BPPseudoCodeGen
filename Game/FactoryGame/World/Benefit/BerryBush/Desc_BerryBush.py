
from codegen.ue4_stub import *

from Script.FactoryGame import FGDecorationDescriptor

class Desc_BerryBush(FGDecorationDescriptor):
    mGroundMesh = Namespace(AssetPath='/Game/FactoryGame/World/Benefit/NutBush/Mesh/Nut_01.Nut_01')
    mGroundMeshScale = Namespace(X=1, Y=1, Z=1)
    mMesh1p = Namespace(AssetPath='/Game/FactoryGame/World/Benefit/NutBush/Mesh/Nut_01.Nut_01')
    mMesh3P = Namespace(AssetPath='/Game/FactoryGame/World/Benefit/NutBush/Mesh/Nut_01.Nut_01')
    mDecorationActorClass = NewObject[BP_BerryBush]()
    mEquipmentClass = NewObject[Equip_BushPlanter]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "E0A91AE248373FBAF2A2D1A02113DA06", "Berry Bush Plant")
    mDescription = NSLOCTEXT("", "F387042242541AFEDD7A468705EA53E7", "Plant it")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mItemCategory = NewObject[Cat_Equipment]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
