
from codegen.ue4_stub import *

from Script.FactoryGame import FGVehicleWheel

class BP_FrontWheelTractor(FGVehicleWheel):
    mCamberStiffness = 100
    ShapeRadius = 65
    ShapeWidth = 70
    Mass = 250
    DampingRate = 100
    SteerAngle = 42
    TireConfig = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Tractor/BP_TireConfigTractor.BP_TireConfigTractor')
    LatStiffValue = 25
    LongStiffValue = 7500
    SuspensionForceOffset = 100
    SuspensionMaxRaise = 25
    SuspensionMaxDrop = 30
    SuspensionNaturalFrequency = 8.5
    SuspensionDampingRatio = 0.6000000238418579
    SweepType = 1
    MaxBrakeTorque = 100000
    
