
from codegen.ue4_stub import *

from Script.FactoryGame import FGVehicleWheel

class BP_BackWheelTruck(FGVehicleWheel):
    mInvertSteering = True
    mCamberStiffness = 100
    ShapeRadius = 105
    ShapeWidth = 100
    Mass = 1000
    SteerAngle = 15
    TireConfig = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Truck/BP_TireConfigTruck.BP_TireConfigTruck')
    LatStiffValue = 100000
    LongStiffValue = 500000
    SuspensionForceOffset = 125
    SuspensionMaxRaise = 100
    SuspensionMaxDrop = 40
    SuspensionNaturalFrequency = 4.25
    SuspensionDampingRatio = 0.125
    SweepType = 1
    MaxBrakeTorque = 200000
    MaxHandBrakeTorque = 400000
    
