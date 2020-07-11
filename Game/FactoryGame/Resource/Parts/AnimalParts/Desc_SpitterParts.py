
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptorBiomass

class Desc_SpitterParts(FGItemDescriptorBiomass):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "A1D0788448DEAF2E5DDB5782DD3D4C04", "Alien Organs")
    mDescription = NSLOCTEXT("", "E4E3EE5246A1B01B58DC27A11322ED74", "Organs from alien creatures.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mRememberPickUp = True
    mEnergyValue = 250
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Resource/Parts/GenericBiomass/UI/M_GenericBiomass_Icon.M_GenericBiomass_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/AnimalParts/UI/IconDesc_SpitterPart_64.IconDesc_SpitterPart_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/AnimalParts/UI/IconDesc_SpitterPart_256.IconDesc_SpitterPart_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Environment/AnimalParts/Mesh/SM_SpitterHide_01.SM_SpitterHide_01')
    mPreviewView = Namespace(CameraPitch=-45, Distance=200, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mItemCategory = NewObject[Cat_Biomass]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
