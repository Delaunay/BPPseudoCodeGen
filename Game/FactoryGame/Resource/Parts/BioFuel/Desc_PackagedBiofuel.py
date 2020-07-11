
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptorBiomass

class Desc_PackagedBiofuel(FGItemDescriptorBiomass):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "79AF58C6440F9536D4F095997526097B", "Packaged Liquid Biofuel")
    mDescription = NSLOCTEXT("", "5999ACB048DE04E5865EE19CFA313958", "Fuel.\r\nPackaged Liquid Biofuel, either converted into electricity or as fuel for vehicles.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mEnergyValue = 750
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Turbofuel/UI/IconDesc_LiquidBiofuel_64.IconDesc_LiquidBiofuel_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Turbofuel/UI/IconDesc_LiquidBiofuel_256.IconDesc_LiquidBiofuel_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Fuel/SM_FuelBio_01.SM_FuelBio_01')
    mPreviewView = Namespace(CameraPitch=-35, Distance=100, FocalOffset={'X': 0, 'Y': 0, 'Z': 100})
    mItemCategory = NewObject[Cat_Packaging]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
