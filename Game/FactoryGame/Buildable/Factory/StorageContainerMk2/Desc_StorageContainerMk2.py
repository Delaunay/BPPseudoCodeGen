
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildingDescriptor

class Desc_StorageContainerMk2(FGBuildingDescriptor):
    mBuildableClass = NewObject[Build_StorageContainerMk2]()
    mBuildCategory = NewObject[BC_Organization]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Organisation/SC_Storage.SC_Storage_C']
    mBuildMenuPriority = 63
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/StorageContainerMk2/UI/StorageContainerMk2_256.StorageContainerMk2_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/StorageContainerMk2/UI/StorageContainerMk2_512.StorageContainerMk2_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/StorageContainerMk2/Mesh/StorageContainerMk2_static.StorageContainerMk2_static')
    mPreviewView = Namespace(CameraPitch=-25, Distance=1200, FocalOffset={'X': 0, 'Y': 0, 'Z': 341.06158447265625})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
