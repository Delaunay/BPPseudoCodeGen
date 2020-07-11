
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildingDescriptor

class Desc_MinerMk1(FGBuildingDescriptor):
    mBuildableClass = NewObject[Build_MinerMk1]()
    mBuildCategory = NewObject[BC_Production]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Production/SC_Miners.SC_Miners_C']
    mBuildMenuPriority = 3
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/MinerMK1/UI/MinerMk1_256.MinerMk1_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/MinerMK1/UI/MinerMk1_512.MinerMk1_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/MinerMK1/Mesh/MinerMk1_static.MinerMk1_static')
    mPreviewView = Namespace(CameraPitch=-25, Distance=1200, FocalOffset={'X': 0, 'Y': 0, 'Z': 150})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
