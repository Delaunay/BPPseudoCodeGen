
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildingDescriptor

class Desc_TradingPost(FGBuildingDescriptor):
    mBuildableClass = NewObject[Build_TradingPost]()
    mBuildCategory = NewObject[BC_TradingPost]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Special/SC_Special.SC_Special_C']
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mCanBeDiscarded = True
    mInventoryIcon = Namespace(DrawAs=3, ImageSize={'X': 256, 'Y': 256}, ImageType=0, Margin={'Left': 0, 'Top': 0, 'Right': 0, 'Bottom': 0}, Mirroring=0, ResourceName='None', ResourceObject={'$Empty': True}, Tiling=0, TintColor={'SpecifiedColor': {'R': 1, 'G': 1, 'B': 1, 'A': 1}, 'ColorUseRule': 0}, UVRegion={'Min': {'X': 0, 'Y': 0}, 'Max': {'X': 0, 'Y': 0}, 'bIsValid': 0}, bHasUObject=False, bIsDynamicallyLoaded=False)
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/TradingPost/UI/Hub_256.Hub_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/TradingPost/UI/Hub_512.Hub_512')
    mConveyorMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/TradingPost/Mesh/Tradingpost.Tradingpost')
    mPreviewView = Namespace(CameraPitch=-25, Distance=2200, FocalOffset={'X': 0, 'Y': 0, 'Z': 1362.327392578125})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
