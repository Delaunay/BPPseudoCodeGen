
from codegen.ue4_stub import *

from Script.FactoryGame import FGEnemyController
from Game.FactoryGame.Character.Creature.AI.Task.BTT_UpdateAttackPattern import ExecuteUbergraph_BTT_UpdateAttackPattern.K2Node_Event_ControlledPawn
from Game.FactoryGame.Character.Creature.AI.Task.BTT_UpdateAttackPattern import ExecuteUbergraph_BTT_UpdateAttackPattern.K2Node_Event_OwnerController
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import FinishExecute
from Script.FactoryGame import UpdateAttackPattern
from Game.FactoryGame.Character.Creature.AI.Task.BTT_UpdateAttackPattern import ExecuteUbergraph_BTT_UpdateAttackPattern

class BTT_UpdateAttackPattern(BTTask_BlueprintBase):
    
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_UpdateAttackPattern.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_UpdateAttackPattern.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_UpdateAttackPattern(26)
    

    def ExecuteUbergraph_BTT_UpdateAttackPattern(self):
        # Label 10
        self.FinishExecute(False)
        # End
        Controller: Ptr[FGEnemyController] = Cast[FGEnemyController](OwnerController)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L10')
        Controller.UpdateAttackPattern()
        self.FinishExecute(True)
    
