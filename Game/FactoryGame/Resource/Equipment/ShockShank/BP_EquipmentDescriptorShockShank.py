
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class BP_EquipmentDescriptorShockShank(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_ShockShank]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "5C86A6904E473207711F00973B0E9AB1", "Xeno-Zapper")
    mDescription = NSLOCTEXT("", "BF189BD34E37E4602AEA739D997ECE34", "Slot: Hands\r\n\r\nStandard issue electroshock self defense weapon for melee range.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/ShockShank/UI/XenoZapper_64.XenoZapper_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/ShockShank/UI/XenoZapper_256.XenoZapper_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/ShockShank/Mesh/ShockShank.ShockShank')
    mItemCategory = NewObject[Cat_Hands]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
