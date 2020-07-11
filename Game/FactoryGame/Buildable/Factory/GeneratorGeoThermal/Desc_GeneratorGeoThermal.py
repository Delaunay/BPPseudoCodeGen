
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildingDescriptor

class Desc_GeneratorGeoThermal(FGBuildingDescriptor):
    mBuildableClass = NewObject[Build_GeneratorGeoThermal]()
    mBuildCategory = NewObject[BC_Power]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Power/SC_Generators.SC_Generators_C']
    mBuildMenuPriority = 24
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/GeneratorGeoThermal/UI/GeoThermalPowerGenerator_256.GeoThermalPowerGenerator_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/GeneratorGeoThermal/UI/GeoThermalPowerGenerator_512.GeoThermalPowerGenerator_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/GeneratorGeoThermal/Mesh/GeneratorGeoThermal_static.GeneratorGeoThermal_static')
    mPreviewView = Namespace(CameraPitch=-25, Distance=2500, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
