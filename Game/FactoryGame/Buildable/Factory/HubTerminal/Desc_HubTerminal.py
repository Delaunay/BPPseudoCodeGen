
from codegen.ue4_stub import *

from Script.FactoryGame import FGBuildingDescriptor

class Desc_HubTerminal(FGBuildingDescriptor):
    mBuildableClass = NewObject[Build_HubTerminal]()
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mPreviewView = Namespace(CameraPitch=-35, Distance=1200, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
