
from codegen.ue4_stub import *

from Script.FactoryGame import FGEquipmentDescriptor

class BP_EquipmentDescriptorColorGun(FGEquipmentDescriptor):
    mEquipmentClass = NewObject[Equip_ColorGun]()
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "26A215D04D6096885A09A2BCAABDCC21", "Color Gun")
    mDescription = NSLOCTEXT("", "6FB443664F2AA92AF2D3C3AA5D745BE4", "Slot: Hands\r\nAmmo: Color Cartridge\r\n\r\nPaints factory buildings and vehicles. The color can be adjusted prior to painting.")
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/ColorGun/UI/ColorGun_64.colorgun_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Equipment/ColorGun/UI/ColorGun_256.colorgun_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Equipment/ColorGun/Mesh/colorgun.colorgun')
    mItemCategory = NewObject[Cat_Hands]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
