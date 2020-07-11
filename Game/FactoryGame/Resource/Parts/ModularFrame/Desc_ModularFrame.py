
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_ModularFrame(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "AD30C73549A860138BAAEDA09E9F1075", "Modular Frame")
    mDescription = NSLOCTEXT("", "10DD3515427A537D446D09A1AD91EF5F", "Used for crafting.\r\nMulti-purpose building block.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ModularFrame/UI/IconDesc_ModularFrame_64.IconDesc_ModularFrame_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ModularFrame/UI/IconDesc_ModularFrame_256.IconDesc_ModularFrame_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ModularFrame/SM_ModularFrame_01.SM_ModularFrame_01')
    mPreviewView = Namespace(CameraPitch=-35, Distance=200, FocalOffset={'X': 0, 'Y': 0, 'Z': 40.605743408203125})
    mItemCategory = NewObject[Cat_StandardParts]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
