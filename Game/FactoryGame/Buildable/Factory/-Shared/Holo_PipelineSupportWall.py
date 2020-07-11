
from codegen.ue4_stub import *

from Script.FactoryGame import FGWallAttachmentHologram

class Holo_PipelineSupportWall(FGWallAttachmentHologram):
    mIsRotationAllowed = True
    mRotationStep = 45
    mSnapOffset = Namespace(X=0, Y=75)
    mMaxPlacementFloorAngle = 35
    mValidHitClasses = ['/Script/FactoryGame.FGBuildableFoundation', '/Script/FactoryGame.FGBuildableRailroadTrack', '/Script/FactoryGame.FGBuildableRoad', '/Script/FactoryGame.FGBuildableWall']
    mLoopSound = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent'}, ObjectClass='/Script/AkAudio.AkComponent', ObjectFlags=2883617, ObjectName='LoopSound')
    mUseBuildClearanceOverlapSnapp = True
    bHidden = True
    bReplicates = True
    RemoteRole = 1
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
