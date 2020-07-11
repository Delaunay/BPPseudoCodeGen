
from codegen.ue4_stub import *

from Script.FactoryGame import FGPoleDescriptor

class Desc_PipelineSupport(FGPoleDescriptor):
    mHeightMeshes = [{'Mesh': {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/PipeHyperSupport/Mesh/SM_HyperTubePole_01.SM_HyperTubePole_01'}, 'Height': 175}, {'Mesh': {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/PipeHyperSupport/Mesh/SM_HyperTubePole_02.SM_HyperTubePole_02'}, 'Height': 275}, {'Mesh': {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/PipeHyperSupport/Mesh/SM_HyperTubePole_03.SM_HyperTubePole_03'}, 'Height': 375}, {'Mesh': {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/PipeHyperSupport/Mesh/SM_HyperTubePole_04.SM_HyperTubePole_04'}, 'Height': 475}]
    mBuildableClass = NewObject[Build_PipelineSupport]()
    mBuildCategory = NewObject[BC_Logistics]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Transport/SC_PipeSupport.SC_PipeSupport_C']
    mBuildMenuPriority = 1
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/PipePole/UI/PipePole_256.PipePole_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/PipePole/UI/PipePole_512.PipePole_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/PipelineSupport/Mesh/PipelineSupport_static.PipelineSupport_static')
    mPreviewView = Namespace(CameraPitch=-25, Distance=500, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
