
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildingDescriptor

class Desc_GeneratorNuclear(FGBuildingDescriptor):
    mBuildableClass = NewObject[Build_GeneratorNuclear]()
    mBuildCategory = NewObject[BC_Power]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Power/SC_Generators.SC_Generators_C']
    mBuildMenuPriority = 23
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/GeneratorNuclear/UI/NuclearPowerplant_256.NuclearPowerplant_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/GeneratorNuclear/UI/NuclearPowerplant_512.NuclearPowerplant_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/GeneratorNuclear/Mesh/GeneratorNuclear_static.GeneratorNuclear_static')
    mPreviewView = Namespace(CameraPitch=-10, Distance=5500, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
