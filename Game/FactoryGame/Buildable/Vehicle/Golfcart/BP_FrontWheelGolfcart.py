
from codegen.ue4_stub import *

from Script.FactoryGame import FGVehicleWheel

class BP_FrontWheelGolfcart(FGVehicleWheel):
    mAutoGenerateCollisionCylinder = True
    mCamberStiffness = 1
    ShapeRadius = 12
    Mass = 10
    SteerAngle = 45
    TireConfig = Namespace(AssetPath='/Game/FactoryGame/Buildable/Vehicle/Golfcart/BP_TireConfigGolfcart.BP_TireConfigGolfcart')
    LatStiffMaxLoad = 1
    LatStiffValue = 20
    SuspensionForceOffset = 20
    SuspensionMaxRaise = 6
    SuspensionMaxDrop = 7
    SuspensionNaturalFrequency = 23
    SuspensionDampingRatio = 0.20000000298023224
    SweepType = 1
    MaxBrakeTorque = 100000
    
