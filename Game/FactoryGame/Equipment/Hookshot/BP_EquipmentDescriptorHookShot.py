
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class BP_EquipmentDescriptorHookShot(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_Hookshot]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "C27C874941A863416AACAFB7CC8576CD", "Hook Shot")
    mDescription = NSLOCTEXT("", "DA39E51F410CDEE431D41FA7520412C1", "Slot: Hands\r\n\r\nGrappling hook.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/ShockShank/UI/XenoZapper_64.XenoZapper_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/ShockShank/UI/XenoZapper_256.XenoZapper_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/Hookshot/Mesh/Hookshot.Hookshot')
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
