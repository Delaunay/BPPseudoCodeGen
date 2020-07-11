
from codegen.ue4_stub import *

from Game.FactoryGame.Resource.BP_HealthGainDescriptor import BP_HealthGainDescriptor

class Desc_Berry(BP_HealthGainDescriptor):
    mHealthGain = 10
    mConsumeEvent = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/Consume/Play_P_Consume_Fruit.Play_P_Consume_Fruit')
    mCustomHandsMeshScale = 1
    mCustomRotation = Namespace(Pitch=0, Roll=0, Yaw=-90)
    mFPOverrideMesh = Namespace(AssetPath='/Game/FactoryGame/World/Benefit/BerryBush/Mesh/Berry_FPS_01.Berry_FPS_01')
    mTPOverrideMesh = Namespace(AssetPath='/Game/FactoryGame/World/Benefit/BerryBush/Mesh/Berry_TPS_01.Berry_TPS_01')
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "1162DC4E4C780A1E6E3A9E96B750769F", "Paleberry")
    mDescription = NSLOCTEXT("", "F4CB225B423A803DBA7CE88CB292CE34", "Slot: Hands\r\nConsumable\r\n\r\nCan be eaten to restore one health segment.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mRememberPickUp = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Environment/Berry/UI/Berry_64.Berry_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Environment/Berry/UI/Berry_256.Berry_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/World/Benefit/BerryBush/Mesh/Berry_02.Berry_02')
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
