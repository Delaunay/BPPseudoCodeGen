
from codegen.ue4_stub import *

from Script.FactoryGame import FGItemDescriptor

class Desc_SpaceElevatorPart_4(FGItemDescriptor):
    mUseDisplayNameAndDescription = True
    mDisplayName = NSLOCTEXT("", "4EFFC7DA4DBCA7A2DC627E8C47DFB297", "Modular Engine")
    mDescription = NSLOCTEXT("", "DD2E9DCA4BDC7DC9AEA4F1B8E25CAC7C", "Project Part #4. Send up the Space Elevator to complete phases of Project Assembly.")
    mStackSize = EStackSize::SS_SMALL
    mCanBeDiscarded = True
    mForm = EResourceForm::RF_SOLID
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 64, 'Y': 64}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ModularEngine/UI/IconDesc_SpelevatorPart_4_64.IconDesc_SpelevatorPart_4_64')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ModularEngine/UI/IconDesc_SpelevatorPart_4_256.IconDesc_SpelevatorPart_4_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Resource/Parts/ModularEngine/SM_ModularEngine_01.SM_ModularEngine_01')
    mPreviewView = Namespace(CameraPitch=-35, Distance=200, FocalOffset={'X': 0, 'Y': 0, 'Z': 40.605743408203125})
    mItemCategory = NewObject[Cat_SpaceElevator]()
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
