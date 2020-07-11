
from codegen.ue4_stub import *

from Game.FactoryGame.Resource.BP_HealthGainDescriptor import BP_HealthGainDescriptor

class Desc_Nut(BP_HealthGainDescriptor):
    mHealthGain = 5
    mConsumeEvent = Namespace(AssetPath='/Game/FactoryGame/Character/Player/Audio/SB_CharacterEssentials/Consume/Play_P_Consume_Nuts.Play_P_Consume_Nuts')
    mCustomHandsMeshScale = 1
    mCustomRotation = Namespace(Pitch=0, Roll=0, Yaw=-90)
    mFPOverrideMesh = Namespace(AssetPath='/Game/FactoryGame/World/Benefit/NutBush/Mesh/Nut_FPS_01.Nut_FPS_01')
    mTPOverrideMesh = Namespace(AssetPath='/Game/FactoryGame/World/Benefit/NutBush/Mesh/Nut_TPS_01.Nut_TPS_01')
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "A8FE1F3B422A792EA58603B683DD775D", "Beryl Nut")
    mDescription = NSLOCTEXT("", "30361C10426AB8B92CBC1FB0B2596D5B", "Slot: Hands\r\nConsumable\r\n\r\nCan be eaten to restore half a health segment.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mRememberPickUp = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Environment/Nut/UI/Nut_64_new.Nut_64_new')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Environment/Nut/UI/Nut_256_New.Nut_256_New')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/World/Benefit/NutBush/Mesh/Nut_02.Nut_02')
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
