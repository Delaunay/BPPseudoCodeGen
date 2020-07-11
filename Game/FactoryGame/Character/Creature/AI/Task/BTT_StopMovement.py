
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.AI.Task.BTT_StopMovement import ExecuteUbergraph_BTT_StopMovement.K2Node_Event_ControlledPawn
from Game.FactoryGame.Character.Creature.AI.Task.BTT_StopMovement import ExecuteUbergraph_BTT_StopMovement.K2Node_Event_OwnerController
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import FinishExecute
from Script.Engine import PawnMovementComponent
from Game.FactoryGame.Character.Creature.AI.Task.BTT_StopMovement import ExecuteUbergraph_BTT_StopMovement

class BTT_StopMovement(BTTask_BlueprintBase):
    
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_StopMovement.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_StopMovement.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_StopMovement(10)
    

    def ExecuteUbergraph_BTT_StopMovement(self):
        ReturnValue: Ptr[PawnMovementComponent] = ControlledPawn.GetMovementComponent()
        ReturnValue.StopMovementImmediately()
        OwnerController.StopMovement()
        self.FinishExecute(True)
    
