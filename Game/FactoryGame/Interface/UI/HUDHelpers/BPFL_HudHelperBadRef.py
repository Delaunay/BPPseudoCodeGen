
from codegen.ue4_stub import *

from Script.Engine import PlayerController
from Game.FactoryGame.-Shared.Blueprint.BP_HUD import BP_HUD
from Script.Engine import GetHUD
from Script.Engine import BlueprintFunctionLibrary
from Script.Engine import HUD

class BPFL_HudHelperBadRef(BlueprintFunctionLibrary):
    
    
    def GetBPHUD(self, Controller: Ptr[Controller], __WorldContext: Ptr[Object]):
        Controller: Ptr[PlayerController] = Cast[PlayerController](Controller_0)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L235')
        ReturnValue: Ptr[HUD] = Controller.GetHUD()
        HUD: Ptr[BP_HUD] = Cast[BP_HUD](ReturnValue)
        bSuccess1: bool = HUD
        if not bSuccess1:
            goto('L224')
        outHUD = HUD
        # End
        # Label 224
        outHUD = None
    
