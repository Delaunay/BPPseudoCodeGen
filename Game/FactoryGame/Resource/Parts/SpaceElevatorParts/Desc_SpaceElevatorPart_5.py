
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_SpaceElevatorPart_5(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "A64AB7EE4AC8A45BEAFD799401ED4FD7", "Adaptive Control Unit")
    mDescription = NSLOCTEXT("", "99E2A44D40AC37F56687DB8B1C7DDDD9", "Project Part #5. Send up the Space Elevator to complete phases of Project Assembly.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ControlSystem/UI/IconDesc_SpelevatorPart_5_64.IconDesc_SpelevatorPart_5_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ControlSystem/UI/IconDesc_SpelevatorPart_5_256.IconDesc_SpelevatorPart_5_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ControlSystem/SM_ControlSystem_01.SM_ControlSystem_01')
    mPreviewView = Namespace(CameraPitch=-35, Distance=200, FocalOffset={'X': 0, 'Y': 0, 'Z': 40.605743408203125})
    mItemCategory = NewObject[Cat_SpaceElevator]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
