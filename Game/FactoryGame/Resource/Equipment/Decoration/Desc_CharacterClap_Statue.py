
from codegen.ue4_stub import *

from Script.FactoryGame import FGDecorationDescriptor

class Desc_CharacterClap_Statue(FGDecorationDescriptor):
    mGroundMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_CharacterClap_Statue.SM_CharacterClap_Statue')
    mGroundMeshScale = Namespace(X=4, Y=4, Z=4)
    mMesh1p = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_CharacterClap_Statue.SM_CharacterClap_Statue')
    mMesh3P = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_CharacterClap_Statue.SM_CharacterClap_Statue')
    mDecorationActorClass = NewObject[BP_Decoration]()
    mEquipmentClass = NewObject[Equip_Decoration]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "A262C2FE4B0DF5FF82D9839E6821B39E", "Pretty Good Pioneering Statue")
    mDescription = NSLOCTEXT("", "4E09AFDF4F6123DFBEDEE69187F320F9", "The statue of the Clapping Character")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/UI/Award_Statue_Character_Silver_64.Award_Statue_Character_Silver_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/UI/Award_Statue_Character_Silver_256.Award_Statue_Character_Silver_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_CharacterClap_Statue.SM_CharacterClap_Statue')
    mItemCategory = NewObject[Cat_Equipment]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
