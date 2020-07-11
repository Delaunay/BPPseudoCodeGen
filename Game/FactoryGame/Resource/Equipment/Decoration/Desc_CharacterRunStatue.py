
from codegen.ue4_stub import *

from Script.FactoryGame import FGDecorationDescriptor

class Desc_CharacterRunStatue(FGDecorationDescriptor):
    mGroundMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_CharacterRun_Statue.SM_CharacterRun_Statue')
    mGroundMeshScale = Namespace(X=4, Y=4, Z=4)
    mMesh1p = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_CharacterRun_Statue.SM_CharacterRun_Statue')
    mMesh3P = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_CharacterRun_Statue.SM_CharacterRun_Statue')
    mDecorationActorClass = NewObject[BP_Decoration]()
    mEquipmentClass = NewObject[Equip_Decoration]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "4EB157E149EB32BE61EC5E9134664A55", "Adequate Pioneering Statue")
    mDescription = NSLOCTEXT("", "BF46864744B1587487B90D98248BA1B9", "The statue of the Running Character")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/UI/Award_Statue_Character_Bronze_64.Award_Statue_Character_Bronze_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/UI/Award_Statue_Character_Bronze_256.Award_Statue_Character_Bronze_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Decor/Statues/SM_CharacterRun_Statue.SM_CharacterRun_Statue')
    mItemCategory = NewObject[Cat_Equipment]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
