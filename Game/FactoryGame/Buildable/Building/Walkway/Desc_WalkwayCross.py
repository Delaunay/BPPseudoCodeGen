
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildingDescriptor

class Desc_WalkwayCross(FGBuildingDescriptor):
    mBuildableClass = NewObject[Build_WalkwayCross]()
    mBuildCategory = NewObject[BC_Organization]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Organisation/SC_Walkways.SC_Walkways_C']
    mBuildMenuPriority = 102
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Building/Walkway/UI/M_WalkwayCross_Icon.M_WalkwayCross_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Walkway/UI/WalkwayCross_256.WalkwayCross_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Walkway/UI/WalkwayCross_256.WalkwayCross_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Walkway/Mesh/Walkway_Cross.Walkway_Cross')
    mPreviewView = Namespace(CameraPitch=-35, Distance=1200, FocalOffset={'X': 0, 'Y': 0, 'Z': -22.75384521484375})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
