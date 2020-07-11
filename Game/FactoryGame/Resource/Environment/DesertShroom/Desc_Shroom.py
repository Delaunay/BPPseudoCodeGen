
from codegen.ue4_stub import *

from Game.FactoryGame.Resource.BP_HealthGainDescriptor import BP_HealthGainDescriptor

class Desc_Shroom(BP_HealthGainDescriptor):
    mHealthGain = 20
    mConsumeEvent = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/Consume/Play_P_Consume_Shrooms.Play_P_Consume_Shrooms')
    mCustomHandsMeshScale = 1
    mCustomRotation = Namespace(Pitch=0, Roll=0, Yaw=-90)
    mFPOverrideMesh = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Swamp/EdibleMushroom/Mesh/EdibleMushroom_FPS_01.EdibleMushroom_FPS_01')
    mTPOverrideMesh = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Swamp/EdibleMushroom/Mesh/EdibleMushroom_TPS_01.EdibleMushroom_TPS_01')
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "49CBA7BD49BC595CC0790F8E78CE64F7", "Bacon Agaric")
    mDescription = NSLOCTEXT("", "B7FA0FC34919FD4D796FBAAB2951B78C", "Slot: Hands\r\nConsumable\r\n\r\nCan be eaten to restore two health segments.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mRememberPickUp = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Environment/DesertShroom/UI/Mushroom_64.Mushroom_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Environment/DesertShroom/UI/Mushroom_256.Mushroom_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Swamp/EdibleMushroom/Mesh/EdibleMushroom_02.EdibleMushroom_02')
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
