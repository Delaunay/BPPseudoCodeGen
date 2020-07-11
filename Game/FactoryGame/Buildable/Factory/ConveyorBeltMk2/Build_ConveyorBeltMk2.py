
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Factory.ConveyorBeltMk1.Build_ConveyorBeltMk1 import Build_ConveyorBeltMk1

class Build_ConveyorBeltMk2(Build_ConveyorBeltMk1):
    mMesh = Namespace(AssetPath='/Game/FactoryGame/Buildable/Factory/ConveyorBeltMk2/Mesh/SM_ConveyorBelt_Mk2.SM_ConveyorBelt_Mk2')
    mSplineComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/Engine.SplineComponent', ObjectFlags=2883617, ObjectName='SplineComponent')
    mInstancedSplineComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, ObjectClass='/Script/InstancedSplines.FGInstancedSplineMeshComponent', ObjectFlags=2883617, ObjectName='InstancedSplineComponent')
    mSpeed = 240
    mConnection0 = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGFactoryConnectionComponent', ObjectFlags=2883617, ObjectName='ConveyorAny0', bNetAddressable=True, mConnectorClearance=0, mDirection='EFactoryConnectionDirection::FCD_ANY', mForwardPeekAndGrabToBuildable=True)
    mConnection1 = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent', 'Mobility': 0}, Mobility=0, ObjectClass='/Script/FactoryGame.FGFactoryConnectionComponent', ObjectFlags=2883617, ObjectName='ConveyorAny1', RelativeLocation={'X': 100, 'Y': 0, 'Z': 0}, bNetAddressable=True, mConnectorClearance=0, mDirection='EFactoryConnectionDirection::FCD_ANY', mForwardPeekAndGrabToBuildable=True)
    mDisplayName = NSLOCTEXT("", "31D67F204C58D568339204A7FFE10BC9", "Conveyor Belt Mk.2")
    mDescription = NSLOCTEXT("", "6CAB260A4CEA9658350E36A523208EDA", "Transports up to 120 resources per minute. Used to move resources between buildings.")
    MaxRenderDistance = -1
    mFactoryTickFunction = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    mPrimaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mSecondaryColor = Namespace(A=1, B=-1, G=-1, R=-1)
    mDismantleEffectClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/Factory/-Shared/BP_MaterialEffect_Dismantle.BP_MaterialEffect_Dismantle_C', SubPathString='')
    mHighlightParticleClassName = Namespace(AssetPathName='/Game/FactoryGame/Buildable/-Shared/Particle/NewBuildingPing.NewBuildingPing_C', SubPathString='')
    mCameraDistanceSq = 100000000376832
    mBuildingID = -1
    bReplicates = True
    RemoteRole = 1
    NetCullDistanceSquared = 5624999936
    RootComponent = Namespace(Mobility=0, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
