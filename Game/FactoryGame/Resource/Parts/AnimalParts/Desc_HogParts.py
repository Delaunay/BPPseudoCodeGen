
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptorBiomass

class Desc_HogParts(FGItemDescriptorBiomass):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "2CB6B2E54FECED48418BB9A1B5366482", "Alien Carapace")
    mDescription = NSLOCTEXT("", "ADBC682E48FB8EA08D9480AFC58639BF", "Thick and sturdy natural armor plates from alien creatures.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mRememberPickUp = True
    mEnergyValue = 250
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Resource/Parts/GenericBiomass/UI/M_GenericBiomass_Icon.M_GenericBiomass_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/AnimalParts/UI/IconDesc_HogPart_64.IconDesc_HogPart_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/AnimalParts/UI/IconDesc_HogPart_256.IconDesc_HogPart_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Environment/AnimalParts/Mesh/SM_HogPart_01.SM_HogPart_01')
    mPreviewView = Namespace(CameraPitch=-45, Distance=200, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mItemCategory = NewObject[Cat_Biomass]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
