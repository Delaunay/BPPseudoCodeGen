
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildingDescriptor

class Desc_TrainDockingStationLiquid(FGBuildingDescriptor):
    mBuildableClass = NewObject[Build_TrainDockingStationLiquid]()
    mBuildCategory = NewObject[BC_Vehicles]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Transport/SC_Trains.SC_Trains_C']
    mBuildMenuPriority = 52
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/Train/Station/UI/TrainDockingFluid_256.TrainDockingFluid_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/Train/Station/UI/TrainDockingFluid_512.TrainDockingFluid_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/Train/Station/Mesh/SM_Trainstation_01.SM_Trainstation_01')
    mPreviewView = Namespace(CameraPitch=-25, Distance=3000, FocalOffset={'X': 0, 'Y': 0, 'Z': 575.1693115234375})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
