
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildingDescriptor

class Desc_QuarterPipeCorner_01(FGBuildingDescriptor):
    mBuildableClass = NewObject[Build_QuarterPipeCorner_01]()
    mBuildCategory = NewObject[BC_Foundations]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Organisation/SC_QuatPipes.SC_QuatPipes_C']
    mBuildMenuPriority = 72
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Building/Foundation/UI/M_Foundation_1a_Icon.M_Foundation_1a_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Ramp/UI/QuarterPipe_Corner_01_256.QuarterPipe_Corner_01_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Ramp/UI/QuarterPipe_Corner_01_512.QuarterPipe_Corner_01_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Ramp/Mesh/SM_QuarterPipeCorner_01.SM_QuarterPipeCorner_01')
    mPreviewView = Namespace(CameraPitch=-20, Distance=1000, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
