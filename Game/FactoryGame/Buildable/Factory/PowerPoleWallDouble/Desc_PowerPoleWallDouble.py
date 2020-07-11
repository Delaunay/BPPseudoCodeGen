
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildingDescriptor

class Desc_PowerPoleWallDouble(FGBuildingDescriptor):
    mBuildableClass = NewObject[Build_PowerPoleWallDouble]()
    mBuildCategory = NewObject[BC_Power]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Power/SC_WallPoles.SC_WallPoles_C']
    mBuildMenuPriority = 4
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/PowerPoleWallDouble/UI/PowerPoleWallDouble_MK1_256.PowerPoleWallDouble_MK1_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/PowerPoleWallDouble/UI/PowerPoleWallDouble_MK1_512.PowerPoleWallDouble_MK1_512')
    mPreviewView = Namespace(CameraPitch=-35, Distance=1200, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
