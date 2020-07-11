
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildingDescriptor

class Desc_ConveyorPoleWall(FGBuildingDescriptor):
    mBuildableClass = NewObject[Build_ConveyorPoleWall]()
    mBuildCategory = NewObject[BC_Logistics]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Transport/SC_ConverPole.SC_ConverPole_C']
    mBuildMenuPriority = 31
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ConveyorPoleWall/UI/ConveyorPole_Wall_256.ConveyorPole_Wall_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ConveyorPoleWall/UI/ConveyorPole_Wall_512.ConveyorPole_Wall_512')
    mPreviewView = Namespace(CameraPitch=-35, Distance=1200, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
