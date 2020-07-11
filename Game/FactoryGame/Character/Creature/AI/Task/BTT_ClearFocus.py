
from codegen.ue4_stub import *

from Script.AIModule import K2_SetFocus
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import FinishExecute
from Game.FactoryGame.Character.Creature.AI.Task.BTT_ClearFocus import ExecuteUbergraph_BTT_ClearFocus.K2Node_Event_OwnerActor
from Game.FactoryGame.Character.Creature.AI.Task.BTT_ClearFocus import ExecuteUbergraph_BTT_ClearFocus
from Script.AIModule import AIController

class BTT_ClearFocus(BTTask_BlueprintBase):
    
    
    def ReceiveExecute(self):
        ExecuteUbergraph_BTT_ClearFocus.K2Node_Event_OwnerActor = OwnerActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_ClearFocus(26)
    

    def ExecuteUbergraph_BTT_ClearFocus(self):
        # Label 10
        self.FinishExecute(True)
        # End
        AsAIController: Ptr[AIController] = Cast[AIController](OwnerActor)
        bSuccess: bool = AsAIController
        if not bSuccess:
            goto('L143')
        AsAIController.K2_SetFocus(None)
        goto('L10')
        # Label 143
        AsAIController.K2_SetFocus(None)
        goto('L10')
    
