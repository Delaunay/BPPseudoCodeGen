
from codegen.ue4_stub import *

from Script.FactoryGame import FGDecorationDescriptor

class Desc_GoldenNut_Statue(FGDecorationDescriptor):
    mGroundMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_Nut_Statue.SM_Nut_Statue')
    mGroundMeshScale = Namespace(X=4, Y=4, Z=4)
    mMesh1p = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_Nut_Statue.SM_Nut_Statue')
    mMesh3P = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_Nut_Statue.SM_Nut_Statue')
    mDecorationActorClass = NewObject[BP_Decoration]()
    mEquipmentClass = NewObject[Equip_Decoration]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "3002DD89481F4ADE4BEA78BC8937EC52", "Golden Nut Statue")
    mDescription = NSLOCTEXT("", "E206FFA54617374D10DFE5AD5903DCAF", "The statue of the golden nut")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/UI/Award_Statue_Nut_64.Award_Statue_Nut_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/UI/Award_Statue_Nut_256.Award_Statue_Nut_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_Nut_Statue.SM_Nut_Statue')
    mItemCategory = NewObject[Cat_Equipment]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
