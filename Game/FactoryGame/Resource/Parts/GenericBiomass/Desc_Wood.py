
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptorBiomass

class Desc_Wood(FGItemDescriptorBiomass):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "9379C1414220E91A18B78E802C6D192C", "Wood")
    mDescription = NSLOCTEXT("", "4311F0E440244DEF88883EA7D34A1457", "Primarily used as fuel.\r\nBiomass Burners and vehicles can use it for power.")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mRememberPickUp = True
    mEnergyValue = 100
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/GenericBiomass/UI/IconDesc_Wood_64.IconDesc_Wood_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/GenericBiomass/UI/IconDesc_Wood_256.IconDesc_Wood_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Wood/SM_Biomass_Wood_01.SM_Biomass_Wood_01')
    mPreviewView = Namespace(CameraPitch=-45, Distance=200, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mItemCategory = NewObject[Cat_Biomass]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
