
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class BP_EquipmentDescriptorJetPackMk2(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_JetPackMk2]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "DEDA675C46AAD742BE6DD58FA8526C24", "Jetpack Mk.2")
    mDescription = NSLOCTEXT("", "2B0875B2419626B9C84A09A36F0DB939", "A better jetpack! :D")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/JetPack/Mesh/Jetpack.Jetpack')
    mItemCategory = NewObject[Cat_Body]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
