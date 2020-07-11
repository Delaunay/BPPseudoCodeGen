
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class BP_EquipmentDescriptorHazardSuit(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_HazardSuit]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "CE9EB37C4E99794498E68FBEA788A757", "Hazard Suit")
    mDescription = NSLOCTEXT("", "F144E7E2460611BB9F4FD5AD487A3C88", "By your powers combines I take no damage from environmental effects")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/GasMask/Mesh/Gasmask.GasMask')
    mItemCategory = NewObject[Cat_Body]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
