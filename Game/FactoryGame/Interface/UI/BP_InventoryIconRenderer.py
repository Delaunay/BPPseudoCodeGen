
from codegen.ue4_stub import *

from Script.FactoryGame import FGRenderTargetStage

class BP_InventoryIconRenderer(FGRenderTargetStage):
    mDynamicRenderTargetSizeX = 64
    mDynamicRenderTargetSizeY = 64
    mDynamicPixelFormat = 2
    mSceneCaptureComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent'}, ObjectClass='/Script/Engine.SceneCaptureComponent2D', ObjectFlags=2883617, ObjectName='SceneCapture', RelativeLocation={'X': 235.32054138183594, 'Y': -0.00015847213217057288, 'Z': 135.32012939453125}, RelativeRotation={'Pitch': -45, 'Yaw': 180, 'Roll': 0}, bCaptureEveryFrame=False, bCaptureOnMovement=False)
    mStage = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent'}, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='Stage')
    mDynamicRenderTarget = True
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
