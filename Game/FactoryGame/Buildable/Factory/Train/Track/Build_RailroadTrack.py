
from codegen.ue4_stub import *

from Script.AkAudio import PostAkEvent
from Script.FactoryGame import FGBuildableRailroadTrack
from Game.FactoryGame.Buildable.Factory.Train.Track.Build_RailroadTrack import ExecuteUbergraph_Build_RailroadTrack
from Script.AkAudio import AkComponent
from Script.AkAudio import Default__AkGameplayStatics
from Game.FactoryGame.Buildable.Vehicle.Train.-Shared.Audio.Play_F_TrainTrack_Construct import Play_F_TrainTrack_Construct

class Build_RailroadTrack(FGBuildableRailroadTrack):
    mMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/Train/Track/Mesh/SM_TrainTrack_02.SM_TrainTrack_02')
    mMeshLength = 1200
    mSplineComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, BodyInstance={'ObjectType': 0, 'CollisionEnabled': 3, 'SleepFamily': 'ESleepFamily::Normal', 'DOFMode': 0, 'bUseCCD': False, 'bNotifyRigidBodyCollision': False, 'bSimulatePhysics': False, 'bOverrideMass': False, 'bEnableGravity': True, 'bAutoWeld': False, 'bStartAwake': True, 'bGenerateWakeEvents': False, 'bUpdateMassWhenScaleChanges': False, 'bLockTranslation': True, 'bLockRotation': True, 'bLockXTranslation': False, 'bLockYTranslation': False, 'bLockZTranslation': False, 'bLockXRotation': False, 'bLockYRotation': False, 'bLockZRotation': False, 'bOverrideMaxAngularVelocity': False, 'bOverrideMaxDepenetrationVelocity': False, 'bOverrideWalkableSlopeOnInstance': False, 'bInterpolateWhenSubStepping': True, 'CollisionProfileName': 'BlockAll', 'CollisionResponses': {'ResponseArray': [{'Channel': 'BuildGun', 'Response': 2}, {'Channel': 'WeaponInstantHit', 'Response': 2}, {'Channel': 'VehicleWheelQuery', 'Response': 2}]}, 'MaxDepenetrationVelocity': 0, 'MassInKgOverride': 0, 'LinearDamping': 0.009999999776482582, 'AngularDamping': 0, 'CustomDOFPlaneNormal': {'X': 0, 'Y': 0, 'Z': 0}, 'COMNudge': {'X': 0, 'Y': 0, 'Z': 0}, 'MassScale': 1, 'InertiaTensorScale': {'X': 1, 'Y': 1, 'Z': 1}, 'WalkableSlopeOverride': {'WalkableSlopeBehavior': 0, 'WalkableSlopeAngle': 0}, 'PhysMaterialOverride': {'$Empty': True}, 'MaxAngularVelocity': 3600, 'CustomSleepThresholdMultiplier': 1, 'StabilizationThresholdMultiplier': 1, 'PhysicsBlendWeight': 0, 'PositionSolverIterationCount': 8, 'VelocitySolverIterationCount': 1}, Mobility=0, ObjectClass='/Script/Engine.SplineComponent', ObjectFlags=2883617, ObjectName='SplineComponent', SplineCurves={'Position': {'Points': [{'InVal': 0, 'OutVal': {'X': 0, 'Y': 0, 'Z': 0}, 'ArriveTangent': {'X': 200, 'Y': 0, 'Z': 0}, 'LeaveTangent': {'X': 200, 'Y': 0, 'Z': 0}, 'InterpMode': 1}, {'InVal': 1, 'OutVal': {'X': 200, 'Y': 0, 'Z': 0}, 'ArriveTangent': {'X': 200, 'Y': 0, 'Z': 0}, 'LeaveTangent': {'X': 200, 'Y': 0, 'Z': 0}, 'InterpMode': 1}], 'bIsLooped': False, 'LoopKeyOffset': 0}, 'Rotation': {'Points': [{'InVal': 0, 'OutVal': {'X': 0, 'Y': 0, 'Z': 0, 'W': 1}, 'ArriveTangent': {'X': 0, 'Y': 0, 'Z': 0, 'W': 1}, 'LeaveTangent': {'X': 0, 'Y': 0, 'Z': 0, 'W': 1}, 'InterpMode': 1}, {'InVal': 1, 'OutVal': {'X': 0, 'Y': 0, 'Z': 0, 'W': 1}, 'ArriveTangent': {'X': 0, 'Y': 0, 'Z': 0, 'W': 1}, 'LeaveTangent': {'X': 0, 'Y': 0, 'Z': 0, 'W': 1}, 'InterpMode': 1}], 'bIsLooped': False, 'LoopKeyOffset': 0}, 'Scale': {'Points': [{'InVal': 0, 'OutVal': {'X': 1, 'Y': 1, 'Z': 1}, 'ArriveTangent': {'X': 0, 'Y': 0, 'Z': 0}, 'LeaveTangent': {'X': 0, 'Y': 0, 'Z': 0}, 'InterpMode': 1}, {'InVal': 1, 'OutVal': {'X': 1, 'Y': 1, 'Z': 1}, 'ArriveTangent': {'X': 0, 'Y': 0, 'Z': 0}, 'LeaveTangent': {'X': 0, 'Y': 0, 'Z': 0}, 'InterpMode': 1}], 'bIsLooped': False, 'LoopKeyOffset': 0}, 'ReparamTable': {'Points': [{'InVal': 0, 'OutVal': 0, 'ArriveTangent': 0, 'LeaveTangent': 0, 'InterpMode': 0}, {'InVal': 20, 'OutVal': 0.10000000149011612, 'ArriveTangent': 0, 'LeaveTangent': 0, 'InterpMode': 0}, {'InVal': 40, 'OutVal': 0.20000000298023224, 'ArriveTangent': 0, 'LeaveTangent': 0, 'InterpMode': 0}, {'InVal': 60.000003814697266, 'OutVal': 0.30000001192092896, 'ArriveTangent': 0, 'LeaveTangent': 0, 'InterpMode': 0}, {'InVal': 80, 'OutVal': 0.4000000059604645, 'ArriveTangent': 0, 'LeaveTangent': 0, 'InterpMode': 0}, {'InVal': 100, 'OutVal': 0.5, 'ArriveTangent': 0, 'LeaveTangent': 0, 'InterpMode': 0}, {'InVal': 120.00000762939453, 'OutVal': 0.6000000238418579, 'ArriveTangent': 0, 'LeaveTangent': 0, 'InterpMode': 0}, {'InVal': 140, 'OutVal': 0.699999988079071, 'ArriveTangent': 0, 'LeaveTangent': 0, 'InterpMode': 0}, {'InVal': 160, 'OutVal': 0.800000011920929, 'ArriveTangent': 0, 'LeaveTangent': 0, 'InterpMode': 0}, {'InVal': 180, 'OutVal': 0.9000000357627869, 'ArriveTangent': 0, 'LeaveTangent': 0, 'InterpMode': 0}, {'InVal': 200, 'OutVal': 1, 'ArriveTangent': 0, 'LeaveTangent': 0, 'InterpMode': 0}], 'bIsLooped': False, 'LoopKeyOffset': 0}}, bGenerateOverlapEvents=False)
    mInstancedSplineComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, ObjectClass='/Script/InstancedSplines.FGInstancedSplineMeshComponent', ObjectFlags=2883617, ObjectName='InstancedSplineComponent')
    mConnections = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGRailroadTrackConnectionComponent', ObjectFlags=2883617, ObjectName='TrackConnection0')
    mHologramClass = NewObject[Holo_RailroadTrack]()
    mDisplayName = NSLOCTEXT("", "A99FD448401EE8273142B19004C59912", "Railway")
    mDescription = NSLOCTEXT("", "C8D98C1649559E700DCDC49B0EF3CE3C", "Used to transport trains in a reliable and fast manner.\r\nHas a wide turn angle so make sure to plan it out properly.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=False, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mBuildEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_TrainTrack.BP_MaterialEffect_TrainTrack_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def PlayConstructSound(self):
        self.ExecuteUbergraph_Build_RailroadTrack(10)
    

    def ExecuteUbergraph_Build_RailroadTrack(self):
        ReturnValue: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_F_TrainTrack_Construct, self, True)
    
