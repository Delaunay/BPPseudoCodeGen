
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import ReceiveOnDeactivate
from Game.FactoryGame.Character.Player.BP_DebugCameraController import ExecuteUbergraph_BP_DebugCameraController.K2Node_Event_RestoredPC
from Script.Engine import ReceiveOnActivate
from Game.FactoryGame.Character.Player.BP_DebugCameraController import ExecuteUbergraph_BP_DebugCameraController
from Script.Engine import DebugCameraController
from Game.FactoryGame.Character.Player.BP_DebugCameraController import ExecuteUbergraph_BP_DebugCameraController.K2Node_InputKeyEvent_Key
from Script.Engine import GetHUD
from Script.FactoryGame import FGHUD
from Game.FactoryGame.Character.Player.BP_DebugCameraController import ExecuteUbergraph_BP_DebugCameraController.K2Node_Event_OriginalPC
from Script.Engine import ExecuteConsoleCommand
from Script.Engine import HUD

class BP_DebugCameraController(DebugCameraController):
    mOriginalHUD: Ptr[FGHUD]
    TransformComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    
    def InpActEvt_Shift_P_K2Node_InputKeyEvent_0(self, Key: Key):
        ExecuteUbergraph_BP_DebugCameraController.K2Node_InputKeyEvent_Key = Key #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_DebugCameraController(26)
    

    def ReceiveOnActivate(self):
        ExecuteUbergraph_BP_DebugCameraController.K2Node_Event_OriginalPC = OriginalPC #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_DebugCameraController(84)
    

    def ReceiveOnDeactivate(self):
        ExecuteUbergraph_BP_DebugCameraController.K2Node_Event_RestoredPC = RestoredPC #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_DebugCameraController(248)
    

    def ExecuteUbergraph_BP_DebugCameraController(self):
        # Label 10
        self.mOriginalHUD = None
        # End
        Default__KismetSystemLibrary.ExecuteConsoleCommand(self, "toggledebugcamera", self)
        # End
        self.ReceiveOnActivate(OriginalPC)
        ReturnValue: Ptr[HUD] = OriginalPC.GetHUD()
        AsFGHUD: Ptr[FGHUD] = Cast[FGHUD](ReturnValue)
        bSuccess: bool = AsFGHUD
        if not bSuccess:
            goto('L272')
        self.mOriginalHUD = AsFGHUD
        # End
        self.ReceiveOnDeactivate(RestoredPC)
        goto('L10')
    
