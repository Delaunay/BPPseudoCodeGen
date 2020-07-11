
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildingDescriptor

class Desc_ResourceSinkShop(FGBuildingDescriptor):
    mBuildableClass = NewObject[Build_ResourceSinkShop]()
    mBuildCategory = NewObject[BC_TradingPost]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Special/SC_Special.SC_Special_C']
    mBuildMenuPriority = 40
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ResourceSinkShop/UI/ResourceSinkShop_256.ResourceSinkShop_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ResourceSinkShop/UI/ResourceSinkShop_512.ResourceSinkShop_512')
    mPreviewView = Namespace(CameraPitch=-35, Distance=1200, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
