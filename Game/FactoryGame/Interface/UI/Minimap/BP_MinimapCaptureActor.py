
from codegen.ue4_stub import *

from Script.FactoryGame import FGMinimapCaptureActor

class BP_MinimapCaptureActor(FGMinimapCaptureActor):
    CaptureComponent2D = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'SceneComponent'}, CaptureSource=3, ObjectClass='/Script/Engine.SceneCaptureComponent2D', ObjectFlags=2883617, ObjectName='NewSceneCaptureComponent2D', ProjectionType=1, bCaptureEveryFrame=False)
    SceneComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='SceneComponent')
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='SceneComponent')
    
