
from codegen.ue4_stub import *

from Script.FactoryGame import FGVehicleDescriptor

class Desc_CyberWagon(FGVehicleDescriptor):
    mVehicleClass = NewObject[Testa_BP_WB]()
    mBuildCategory = NewObject[BC_Vehicles]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Transport/SC_Vehicles.SC_Vehicles_C']
    mBuildMenuPriority = 42
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mCanBeDiscarded = True
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Cyberwagon/UI/Cyberwagon_256.Cyberwagon_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Cyberwagon/UI/Cyberwagon_512.Cyberwagon_512')
    mPreviewView = Namespace(CameraPitch=-35, Distance=1200, FocalOffset={'X': 0, 'Y': 0, 'Z': 0})
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
