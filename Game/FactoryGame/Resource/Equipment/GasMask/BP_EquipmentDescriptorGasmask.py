
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class BP_EquipmentDescriptorGasmask(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_GasMask]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "2266AAFA4E435830CF304988EF3B0097", "Gas mask")
    mDescription = NSLOCTEXT("", "173A6E2C46E95CD950A8CA98F7CE98DE", "Slot: Body\r\n\r\nAllows you to breathe normally in poison gas. Consumes Gas Filters from your inventory when you are in poison gas.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/GasMask/UI/GasMask_64.GasMask_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/GasMask/UI/GasMask_256.GasMask_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/GasMask/Mesh/Gasmask.GasMask')
    mItemCategory = NewObject[Cat_Body]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
