
from codegen.ue4_stub import *

from Script.Engine import ReceiveTick
from Script.Engine import BreakRotator
from Script.Engine import SceneComponent
from Script.FactoryGame import FGRenderTargetStage
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.BP_BuildingPreview import ExecuteUbergraph_BP_BuildingPreview.K2Node_Event_DeltaSeconds
from Game.FactoryGame.Interface.UI.InGame.BuildMenu.BP_BuildingPreview import ExecuteUbergraph_BP_BuildingPreview
from Script.CoreUObject import Rotator
from Script.Engine import K2_SetRelativeRotation
from Script.FactoryGame import GetStage
from Script.Engine import MakeRotator

class BP_BuildingPreview(FGRenderTargetStage):
    mRotationSpeed: float = 50
    mDynamicRenderTargetSizeX = 512
    mDynamicRenderTargetSizeY = 512
    mDynamicPixelFormat = 2
    mSceneCaptureComponent = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent'}, ObjectClass='/Script/Engine.SceneCaptureComponent2D', ObjectFlags=2883617, ObjectName='SceneCapture', RelativeLocation={'X': 900, 'Y': 0, 'Z': 800}, RelativeRotation={'Pitch': -45, 'Yaw': 180, 'Roll': 0}, TextureTarget={'$AssetPath': '/Game/FactoryGame/Interface/UI/InGame/BuildMenu/T_BuildingPreview.T_BuildingPreview'}, bCaptureEveryFrame=False, bCaptureOnMovement=False)
    mStage = Namespace(AttachParent={'$ObjectClass': '/Script/Engine.SceneComponent', '$ObjectFlags': 2883617, '$ObjectName': 'RootComponent'}, ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='Stage')
    mDynamicRenderTarget = True
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def ReceiveTick(self):
        ExecuteUbergraph_BP_BuildingPreview.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_BuildingPreview(10)
    

    def ExecuteUbergraph_BP_BuildingPreview(self):
        self.ReceiveTick(DeltaSeconds)
        ReturnValue: Ptr[SceneComponent] = self.GetStage()
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue.RelativeRotation, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_0: float = DeltaSeconds * self.mRotationSpeed
        ReturnValue_1: float = Yaw + ReturnValue_0
        ReturnValue_2: Rotator = MakeRotator(Roll, Pitch, ReturnValue_1)
        
        SweepHitResult = None
        ReturnValue.K2_SetRelativeRotation(ReturnValue_2, False, True, Ref[SweepHitResult])
    
