
from codegen.ue4_stub import *

from Script.FactoryGame import FGDecorationDescriptor

class Desc_CharacterSpin_Statue(FGDecorationDescriptor):
    mGroundMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_CharacterSpin_Statue.SM_CharacterSpin_Statue')
    mGroundMeshScale = Namespace(X=4, Y=4, Z=4)
    mMesh1p = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_CharacterSpin_Statue.SM_CharacterSpin_Statue')
    mMesh3P = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_CharacterClap_Statue.SM_CharacterClap_Statue')
    mDecorationActorClass = NewObject[BP_Decoration]()
    mEquipmentClass = NewObject[Equip_Decoration]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "FA6182964FCB071B5A40BB9BB35D95CD", "Satisfactory Pioneering Statue")
    mDescription = NSLOCTEXT("", "325714CF4848BFB7F1FE2BBD780EB4E8", "The statue of the Character Spinning the Build Gun")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/UI/Award_Statue_Character_Gold_64.Award_Statue_Character_Gold_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/UI/Award_Statue_Character_Gold_256.Award_Statue_Character_Gold_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_CharacterSpin_Statue.SM_CharacterSpin_Statue')
    mItemCategory = NewObject[Cat_Equipment]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
