
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildingDescriptor

class Desc_PillarMiddle(FGBuildingDescriptor):
    mBuildableClass = NewObject[Build_PillarMiddle]()
    mBuildCategory = NewObject[BC_Foundations]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Organisation/SC_Floors.SC_Floors_C']
    mBuildMenuPriority = 7
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Building/Foundation/UI/M_Foundation_1a_Icon.M_Foundation_1a_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Pillars/UI/Pillar_Middle_256.Pillar_Middle_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Pillars/UI/Pillar_Middle_512.Pillar_Middle_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Pillars/Mesh/SM_Pillar_Middle.SM_Pillar_Middle')
    mPreviewView = Namespace(CameraPitch=-20, Distance=1000, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
