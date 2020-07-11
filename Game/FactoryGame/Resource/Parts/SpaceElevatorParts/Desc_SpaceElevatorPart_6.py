
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_SpaceElevatorPart_6(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "BBDFE6A544599133DDD0E0854BD7A52A", "Spelevator Part 6")
    mDescription = NSLOCTEXT("", "D5476077435C8137AB32A898D17B38F8", "Used for completing space elevator stages.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HUBParts/UI/IconDesc_HubParts_64.IconDesc_HubParts_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HUBParts/UI/IconDesc_HubParts_256.IconDesc_HubParts_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/HUBParts/SM_HUBparts_01.SM_HUBparts_01')
    mPreviewView = Namespace(CameraPitch=-35, Distance=200, FocalOffset={'X': 0, 'Y': 0, 'Z': 40.605743408203125})
    mItemCategory = NewObject[Cat_SpaceElevator]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
