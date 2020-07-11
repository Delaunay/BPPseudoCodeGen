
from codegen.ue4_stub import *

from Script.FactoryGame import FGDecorationDescriptor

class Desc_SpaceGiraffeStatue(FGDecorationDescriptor):
    mGroundMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_SpaceGiraffe_Statue.SM_SpaceGiraffe_Statue')
    mGroundMeshScale = Namespace(X=5, Y=5, Z=5)
    mMesh1p = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_SpaceGiraffe_Statue.SM_SpaceGiraffe_Statue')
    mMesh3P = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_SpaceGiraffe_Statue.SM_SpaceGiraffe_Statue')
    mDecorationActorClass = NewObject[BP_Decoration]()
    mEquipmentClass = NewObject[Equip_Decoration]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "8021BF304F42B7669C44C98865DE67B2", "Confusing Creature Statue")
    mDescription = NSLOCTEXT("", "8CA7A6034AA9A78DB6B4CCBED5EE4EAB", "The statue of the Space Giraffe")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/UI/Award_Statue_SpaceGiraffe_64.Award_Statue_SpaceGiraffe_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/UI/Award_Statue_SpaceGiraffe_256.Award_Statue_SpaceGiraffe_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_SpaceGiraffe_Statue.SM_SpaceGiraffe_Statue')
    mItemCategory = NewObject[Cat_Equipment]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
