
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptorBiomass

class Desc_Biofuel(FGItemDescriptorBiomass):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "07AE2C1C4B564CA4BB2CD3A41105CFF4", "Solid Biofuel")
    mDescription = NSLOCTEXT("", "1F5914D84AF9BB1E57BB05BF9B7F0F08", "Fuel.\r\nThe most energy efficient form of solid biomass.")
    mStackSize = EStackSize::SS_BIG
    mCanBeDiscarded = True
    mEnergyValue = 450
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SolidBiofuel/UI/IconDesc_SolidBiofuel_64.IconDesc_SolidBiofuel_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SolidBiofuel/UI/IconDesc_SolidBiofuel_256.IconDesc_SolidBiofuel_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SolidBiofuel/SM_SolidBiofuel_01.SM_SolidBiofuel_01')
    mPreviewView = Namespace(CameraPitch=-35, Distance=100, FocalOffset={'X': 0, 'Y': 0, 'Z': 100})
    mItemCategory = NewObject[Cat_Biomass]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
