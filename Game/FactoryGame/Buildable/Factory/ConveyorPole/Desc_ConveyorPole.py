
from codegen.ue4_stub import *

from Script.FactoryGame import FGPoleDescriptor

class Desc_ConveyorPole(FGPoleDescriptor):
    mHeightMeshes = [{'Mesh': {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/ConveyorPole/Mesh/SM_ConveyorPole_01.SM_ConveyorPole_01'}, 'Height': 100}, {'Mesh': {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/ConveyorPole/Mesh/SM_ConveyorPole_02.SM_ConveyorPole_02'}, 'Height': 300}, {'Mesh': {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/ConveyorPole/Mesh/SM_ConveyorPole_03.SM_ConveyorPole_03'}, 'Height': 500}, {'Mesh': {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/ConveyorPole/Mesh/SM_ConveyorPole_04.SM_ConveyorPole_04'}, 'Height': 700}]
    mBuildableClass = NewObject[Build_ConveyorPole]()
    mBuildCategory = NewObject[BC_Logistics]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Transport/SC_ConverPole.SC_ConverPole_C']
    mBuildMenuPriority = 30
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ConveyorPole/UI/ConveyorPole_256.ConveyorPole_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ConveyorPole/UI/ConveyorPole_256.ConveyorPole_256')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ConveyorPole/Mesh/SM_ConveyorPole_01.SM_ConveyorPole_01')
    mPreviewView = Namespace(CameraPitch=-25, Distance=150, FocalOffset={'X': 0, 'Y': 0, 'Z': 40})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
