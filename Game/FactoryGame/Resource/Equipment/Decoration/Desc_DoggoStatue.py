
from codegen.ue4_stub import *

from Script.FactoryGame import FGDecorationDescriptor

class Desc_DoggoStatue(FGDecorationDescriptor):
    mGroundMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_SpaceRabbit_Statue.SM_SpaceRabbit_Statue')
    mGroundMeshScale = Namespace(X=4, Y=4, Z=4)
    mMesh1p = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_SpaceRabbit_Statue.SM_SpaceRabbit_Statue')
    mMesh3P = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_SpaceRabbit_Statue.SM_SpaceRabbit_Statue')
    mDecorationActorClass = NewObject[BP_Decoration]()
    mEquipmentClass = NewObject[Equip_Decoration]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "9145F1E641CE23FF32081899B8C56872", "Lizard Doggo Statue")
    mDescription = NSLOCTEXT("", "758113374372D7C9AA6D66AB4E225B14", "A statue of the Lizard Doggo")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/UI/Award_Statue_LizardDoggo_64.Award_Statue_LizardDoggo_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/UI/Award_Statue_LizardDoggo_256.Award_Statue_LizardDoggo_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_SpaceRabbit_Statue.SM_SpaceRabbit_Statue')
    mItemCategory = NewObject[Cat_Equipment]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
