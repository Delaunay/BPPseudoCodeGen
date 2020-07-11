
from codegen.ue4_stub import *

from Script.Engine import GetNumberOfSplinePoints
from Script.Engine import GreaterEqual_IntInt
from Script.FactoryGame import FGSplinePath

class BP_Spline(FGSplinePath):
    mIndex: int32
    mIsYoyoing: bool
    mIncrementSign: int32 = 1
    mSpline = Namespace(BodyInstance={'ObjectType': 0, 'CollisionEnabled': 0, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'Custom', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'VehicleWheelQuery', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 100, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, ObjectClass='/Script/Engine.SplineComponent', ObjectFlags=2883617, ObjectName='Spline')
    
    def GetNextSplineIndex(self, currentIndex: int32):
        ReturnValue: int32 = currentIndex + self.mIncrementSign
        LocalIndex = ReturnValue
        ReturnValue_0: bool = LocalIndex <= 0
        if not ReturnValue_0:
            goto('L176')
        self.mIncrementSign = 1
        # Label 144
        nextIndex = LocalIndex
        # End
        # Label 176
        ReturnValue1: int32 = self.mSpline.GetNumberOfSplinePoints()
        ReturnValue_1: bool = GreaterEqual_IntInt(LocalIndex, ReturnValue1)
        if not ReturnValue_1:
            goto('L144')
        if not self.mIsYoyoing:
            goto('L439')
        self.mIncrementSign = -1
        ReturnValue_2: int32 = self.mSpline.GetNumberOfSplinePoints()
        ReturnValue_3: int32 = ReturnValue_2 - 1
        LocalIndex = ReturnValue_3
        goto('L144')
        # Label 439
        LocalIndex = 0
        goto('L144')
    
