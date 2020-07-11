
from codegen.ue4_stub import *

from Script.FactoryGame import FGPoleDescriptor

class Desc_HyperPoleStackable(FGPoleDescriptor):
    mHeightMeshes = [{'Mesh': {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/PipeHyperSupport/Mesh/SM_HyperTubePoleMulti_01.SM_HyperTubePoleMulti_01'}, 'Height': 0}]
    mBuildableClass = NewObject[Build_HyperPoleStackable]()
    mBuildCategory = NewObject[BC_Vehicles]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Transport/SC_HyperTubes.SC_HyperTubes_C']
    mBuildMenuPriority = 10
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/HyperTubeWallSupport/UI/IconDesc_HyperTubeStackable_256.IconDesc_HyperTubeStackable_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/HyperTubeWallSupport/UI/IconDesc_HyperTubeStackable_512.IconDesc_HyperTubeStackable_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Misc/Mesh/Cube.Cube')
    mPreviewView = Namespace(CameraPitch=-25, Distance=500, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
