
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_SpaceElevatorPart_1(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "A375458D4EE37500B65CE892F68F29F3", "Smart Plating")
    mDescription = NSLOCTEXT("", "5A9486C34D645755851825803E06B936", "Project Part #1. Send up the Space Elevator to complete phases of Project Assembly.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SmartPlate/UI/IconDesc_SpelevatorPart_1_64.IconDesc_SpelevatorPart_1_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SmartPlate/UI/IconDesc_SpelevatorPart_1_256.IconDesc_SpelevatorPart_1_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/SmartPlate/SM_SmartPlate_01.SM_SmartPlate_01')
    mPreviewView = Namespace(CameraPitch=-35, Distance=200, FocalOffset={'X': 0, 'Y': 0, 'Z': 40.605743408203125})
    mItemCategory = NewObject[Cat_SpaceElevator]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
