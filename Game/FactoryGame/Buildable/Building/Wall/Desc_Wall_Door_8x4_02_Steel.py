
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildingDescriptor

class Desc_Wall_Door_8x4_02_Steel(FGBuildingDescriptor):
    mBuildableClass = NewObject[Build_Wall_Door_8x4_02_Steel]()
    mBuildCategory = NewObject[BC_Walls]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Walls/SC_Doors.SC_Doors_C']
    mBuildMenuPriority = 4
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$AssetPath': '/Game/FactoryGame/Buildable/Building/Wall/Wall_Set01/UI/M_Wall_1a_Icon.M_Wall_1a_Icon'}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Wall/UI/Wall_Door_Left_Grey_256.Wall_Door_Left_Grey_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Wall/UI/Wall_Door_Left_Grey_512.Wall_Door_Left_Grey_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Building/Wall/Mesh/SM_Wall_8x4_01.SM_Wall_8x4_01')
    mPreviewView = Namespace(CameraPitch=0, Distance=700, FocalOffset={'X': 0, 'Y': 0, 'Z': 200})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
