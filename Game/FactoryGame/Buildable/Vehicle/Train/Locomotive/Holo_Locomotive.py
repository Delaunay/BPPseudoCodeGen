
from codegen.ue4_stub import *

from Script.FactoryGame import FGRailroadVehicleHologram

class Holo_Locomotive(FGRailroadVehicleHologram):
    mValidHitClasses = ['/Script/FactoryGame.FGBuildableFoundation', '/Script/FactoryGame.FGBuildableRailroadTrack', '/Script/FactoryGame.FGBuildableRoad']
    mLoopSound = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent'}, ObjectClass='/Script/AkAudio.AkComponent', ObjectFlags=2883617, ObjectName='LoopSound')
    bHidden = True
    bReplicates = True
    RemoteRole = 1
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
