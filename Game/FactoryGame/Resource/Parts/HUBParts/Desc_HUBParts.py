
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_HUBParts(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "1D76276E44F1F518169048B5B378EBE8", "HUB Parts")
    mDescription = NSLOCTEXT("", "B50BF0674966D1FBA93B61BAB7F2E0C7", "The parts required to build the basic structure of the HUB.")
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HUBParts/UI/IconDesc_HubParts_64.IconDesc_HubParts_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HUBParts/UI/IconDesc_HubParts_256.IconDesc_HubParts_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HUBParts/SM_HUBparts_01.SM_HUBparts_01')
    mPreviewView = Namespace(CameraPitch=-35, Distance=50, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
