
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildingDescriptor

class Desc_HyperTubeWallSupport(FGBuildingDescriptor):
    mBuildableClass = NewObject[Build_HyperTubeWallSupport]()
    mBuildCategory = NewObject[BC_Vehicles]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Transport/SC_HyperTubes.SC_HyperTubes_C']
    mBuildMenuPriority = 5
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/HyperTubeWallSupport/UI/IconDesc_HyperTube_WallSupport_256.IconDesc_HyperTube_WallSupport_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/HyperTubeWallSupport/UI/IconDesc_HyperTube_WallSupport_512.IconDesc_HyperTube_WallSupport_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/PipelineSupportWall/Mesh/PipelineSupport_static.PipelineSupport_static')
    mPreviewView = Namespace(CameraPitch=-35, Distance=1200, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
