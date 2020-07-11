
from codegen.ue4_stub import *

from Script.FactoryGame import FGDecorationDescriptor

class Desc_NutBush(FGDecorationDescriptor):
    mGroundMesh = Namespace(AssetPath='/Game/FactoryGame/World/Benefit/NutBush/Mesh/Nut_01.Nut_01')
    mGroundMeshScale = Namespace(X=1, Y=1, Z=1)
    mMesh1p = Namespace(AssetPath='/Game/FactoryGame/World/Benefit/NutBush/Mesh/Nut_01.Nut_01')
    mMesh3P = Namespace(AssetPath='/Game/FactoryGame/World/Benefit/NutBush/Mesh/Nut_01.Nut_01')
    mDecorationActorClass = NewObject[BP_NutBush]()
    mEquipmentClass = NewObject[Equip_BushPlanter]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "74430C8D4A774A642A0563A76B2EA7D4", "Nut Bush Plant")
    mDescription = NSLOCTEXT("", "8352BE804C18EC09A9E88CAF19354223", "Plant it")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mItemCategory = NewObject[Cat_Equipment]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
