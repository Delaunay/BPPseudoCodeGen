
from codegen.ue4_stub import *

from Script.FactoryGame import FGVehicleWheel

class BP_FrontWheelTruck(FGVehicleWheel):
    mCamberStiffness = 100
    ShapeRadius = 105
    ShapeWidth = 100
    Mass = 1000
    SteerAngle = 47
    TireConfig = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Truck/BP_TireConfigTruck.BP_TireConfigTruck')
    LatStiffMaxLoad = 1.75
    LatStiffValue = 100000
    LongStiffValue = 500000
    SuspensionForceOffset = 250
    SuspensionMaxRaise = 60
    SuspensionMaxDrop = 60
    SuspensionNaturalFrequency = 4.25
    SuspensionDampingRatio = 0.125
    SweepType = 1
    MaxBrakeTorque = 200000
    
