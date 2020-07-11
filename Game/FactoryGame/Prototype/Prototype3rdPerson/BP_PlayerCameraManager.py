
from codegen.ue4_stub import *

from Script.Engine import PlayerCameraManager

class BP_PlayerCameraManager(PlayerCameraManager):
    TransformComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0')
    FreeCamOffset = Namespace(X=0, Y=100, Z=64)
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0')
    
