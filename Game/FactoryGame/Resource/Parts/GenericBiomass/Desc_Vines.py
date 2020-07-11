
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptorBiomass

class Desc_Vines(FGItemDescriptorBiomass):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "1F49F1904901568F3AC3C7A1042BEA23", "Vines")
    mDescription = NSLOCTEXT("", "CA4A8DB84FB8F8C25320378B09AAAB3A", "Primarily used as fuel.\r\nBiomass Burners and vehicles can use it for power.")
    mStackSize = EStackSize::SS_BIG
    mCanBeDiscarded = True
    mEnergyValue = 35
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Resource/Parts/GenericBiomass/UI/M_GenericBiomass_Icon.M_GenericBiomass_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/GenericBiomass/UI/IconDesc_Vines_64.IconDesc_Vines_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/GenericBiomass/UI/IconDesc_Vines_256.IconDesc_Vines_256')
    mPreviewView = Namespace(CameraPitch=-45, Distance=200, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mItemCategory = NewObject[Cat_Biomass]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
