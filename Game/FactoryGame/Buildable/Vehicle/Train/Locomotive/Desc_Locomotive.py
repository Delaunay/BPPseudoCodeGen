
from codegen.ue4_stub import *

from Script.FactoryGame import FGVehicleDescriptor

class Desc_Locomotive(FGVehicleDescriptor):
    mVehicleClass = NewObject[BP_Locomotive]()
    mBuildCategory = NewObject[BC_Vehicles]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Transport/SC_Trains.SC_Trains_C']
    mBuildMenuPriority = 49
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mCanBeDiscarded = True
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/UI/Locomotive_256.Locomotive_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/UI/Locomotive_512.Locomotive_512')
    mPreviewView = Namespace(CameraPitch=-25, Distance=1700, FocalOffset={'X': 0, 'Y': 0, 'Z': 300})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
