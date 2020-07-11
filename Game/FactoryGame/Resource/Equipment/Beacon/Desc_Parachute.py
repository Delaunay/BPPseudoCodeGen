
from codegen.ue4_stub import *

from Script.FactoryGame import FGConsumableDescriptor

class Desc_Parachute(FGConsumableDescriptor):
    mCustomHandsMeshScale = 1
    mEquipmentClass = NewObject[Equip_Parachute]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "32ED93BF48CF581538C93CB2C789EDE6", "Parachute")
    mDescription = NSLOCTEXT("", "33C30C7C4C930A689478B79E7C2D0A01", "Slot: Body\r\nConsumable\r\n\r\nSlows down your fall when activated in mid-air.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/Beacon/UI/Parachute_64.Parachute_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/Beacon/UI/Parachute_256.Parachute_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/Parachute/Mesh/Parachute_static.Parachute_static')
    mItemCategory = NewObject[Cat_Body]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
