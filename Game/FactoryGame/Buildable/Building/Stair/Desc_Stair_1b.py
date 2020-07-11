
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildingDescriptor

class Desc_Stair_1b(FGBuildingDescriptor):
    mBuildableClass = NewObject[Build_Stair_1b]()
    mBuildCategory = NewObject[BC_Organization]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Organisation/SC_Stair.SC_Stair_C']
    mBuildMenuPriority = 97
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Building/Stair/UI/M_Stair_1b_Icon.M_Stair_1b_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Stair/UI/T_Stair_1b.T_Stair_1b')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Stair/UI/T_Stair_1b.T_Stair_1b')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Stair/Mesh/Stair_01b.Stair_01b')
    mPreviewView = Namespace(CameraPitch=-25, Distance=800, FocalOffset={'X': 0, 'Y': 0, 'Z': 242.78976440429688})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
