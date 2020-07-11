
from codegen.ue4_stub import *

from Script.FactoryGame import FGPoleDescriptor

class Desc_ConveyorPoleStackable(FGPoleDescriptor):
    mHeightMeshes = [{'Mesh': {'$AssetPath': '/Game/FactoryGame/Buildable/Factory/ConveyorPoleStackable/Mesh/ConveyorPoleMulti_01_static.ConveyorPoleMulti_01_static'}, 'Height': 100}]
    mBuildableClass = NewObject[Build_ConveyorPoleStackable]()
    mBuildCategory = NewObject[BC_Logistics]()
    mSubCategories = ['/Game/FactoryGame/Interface/UI/InGame/BuildMenu/BuildCategories/Sub_Transport/SC_ConverPole.SC_ConverPole_C']
    mBuildMenuPriority = 30
    mUseDisplayNameAndDescription = True
    mDisplayName = INVTEXT("")
    mDescription = INVTEXT("")
    mStackSize = EStackSize::SS_MEDIUM
    mCanBeDiscarded = True
    mSmallIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ConveyorPoleMulti/UI/ConveyorPoleMulti_256.ConveyorPoleMulti_256')
    mPersistentBigIcon = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ConveyorPoleMulti/UI/ConveyorPoleMulti_512.ConveyorPoleMulti_512')
    mFluidDensity = 1
    mFluidViscosity = 1
    mFluidFriction = 0.10000000149011612
    
