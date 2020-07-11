
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_SpaceElevatorPart_2(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "E13014B6406289846DC528BF508AEE6D", "Versatile Framework")
    mDescription = NSLOCTEXT("", "DAE82DF7411FFE1134DE0B91DD5CF268", "Project Part #2. Send up the Space Elevator to complete phases of Project Assembly.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Skeletalframework/UI/IconDesc_SpelevatorPart_2_64.IconDesc_SpelevatorPart_2_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Skeletalframework/UI/IconDesc_SpelevatorPart_2_256.IconDesc_SpelevatorPart_2_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/Skeletalframework/SM_Skeletalframework_01.SM_Skeletalframework_01')
    mPreviewView = Namespace(CameraPitch=-35, Distance=200, FocalOffset={'X': 0, 'Y': 0, 'Z': 40.605743408203125})
    mItemCategory = NewObject[Cat_SpaceElevator]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
