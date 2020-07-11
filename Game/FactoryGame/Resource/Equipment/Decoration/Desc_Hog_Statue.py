
from codegen.ue4_stub import *

from Script.FactoryGame import FGDecorationDescriptor

class Desc_Hog_Statue(FGDecorationDescriptor):
    mGroundMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_Hog_Statue.SM_Hog_Statue')
    mGroundMeshScale = Namespace(X=4, Y=4, Z=4)
    mMesh1p = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_Hog_Statue.SM_Hog_Statue')
    mMesh3P = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_Hog_Statue.SM_Hog_Statue')
    mDecorationActorClass = NewObject[BP_Decoration]()
    mEquipmentClass = NewObject[Equip_Decoration]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "D995780F4ACF229909677598AFB9639F", "Silver Hog Statue")
    mDescription = NSLOCTEXT("", "0704E406430FD48C06BC04BD9C167CAF", "The statue of the SIlver Pouncing Hog. Perfect as a hood ornament.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/UI/Award_Statue_Hog_64.Award_Statue_Hog_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/UI/Award_Statue_Hog_256.Award_Statue_Hog_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_Hog_Statue.SM_Hog_Statue')
    mItemCategory = NewObject[Cat_Equipment]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
