
from codegen.ue4_stub import *

from Game.FactoryGame.Resource.BP_HealthGainDescriptor import BP_HealthGainDescriptor

class Desc_Medkit(BP_HealthGainDescriptor):
    mHealthGain = 100
    mCustomHandsMeshScale = 0.20000000298023224
    mEquipmentClass = NewObject[Equip_MedKit]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "FC4C697749695074BDDACEB3427E4EF2", "Medicinal Inhaler")
    mDescription = NSLOCTEXT("", "7D0EB4B04625553AAE652FABE17F5BA9", "Slot: Hands\r\nConsumable\r\n\r\nCan be inhaled to fully restore health.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/Medkit/UI/Inhaler_64.Inhaler_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/Medkit/UI/Inhaler_256.Inhaler_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/Medkit/Mesh/Medkit_01.Medkit_01')
    mItemCategory = NewObject[Cat_Hands]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
