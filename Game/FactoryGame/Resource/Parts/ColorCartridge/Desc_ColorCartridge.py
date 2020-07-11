
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_ColorCartridge(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "84DF71F24C00941583C20194D065D165", "Color Cartridge")
    mDescription = NSLOCTEXT("", "56DED1564CA310F85AC48081CCEE32A6", "Ammo for the Color Gun.\r\nNecessary to change the color of factory buildings and vehicles.")
    mStackSize = EStackSize::SS_BIG
    mCanBeDiscarded = True
    mEnergyValue = 900
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ColorCartridge/UI/IconDesc_ColorCartridge_64.IconDesc_ColorCartridge_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ColorCartridge/UI/IconDesc_ColorCartridge_256.IconDesc_ColorCartridge_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ColorGunCartridge/SM_ColorGun_Cartridge_01.SM_ColorGun_Cartridge_01')
    mItemCategory = NewObject[Cat_Equipment]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
