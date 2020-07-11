
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildingDescriptor

class Desc_WalkwayRamp(FGBuildingDescriptor):
    mBuildableClass = NewObject[Build_WalkwayRamp]()
    mBuildCategory = NewObject[BC_Organization]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Organisation/SC_Walkways.SC_Walkways_C']
    mBuildMenuPriority = 102
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Building/Walkway/UI/M_WalkwayRamp_Icon.M_WalkwayRamp_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Walkway/UI/WalkwayRamp_256.WalkwayRamp_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Walkway/UI/WalkwayRamp_256.WalkwayRamp_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Walkway/Mesh/Walkway_Ramp.Walkway_Ramp')
    mPreviewView = Namespace(CameraPitch=3.615162346292896e-33, Distance=0, FocalOffset={'X': 201.21656799316406, 'Y': 0, 'Z': 124.82713317871094})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
