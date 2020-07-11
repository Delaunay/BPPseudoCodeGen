
from codegen.ue4_stub import *

from Script.FactoryGame import FGVehicleWheel

class BP_RearWheelExplorer(FGVehicleWheel):
    mCamberAtMaxCompression = -5
    mCamberAtMaxDroop = 8
    mCamberStiffness = 100
    ShapeRadius = 70
    ShapeWidth = 65
    Mass = 500
    TireConfig = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Explorer/BP_TireConfigExplorer.BP_TireConfigExplorer')
    LatStiffMaxLoad = 1.7000000476837158
    LatStiffValue = 12
    LongStiffValue = 85000
    SuspensionMaxRaise = 100
    SuspensionMaxDrop = 120
    SuspensionNaturalFrequency = 6
    SuspensionDampingRatio = 0.25
    SweepType = 1
    MaxBrakeTorque = 20000
    MaxHandBrakeTorque = 20000
    
