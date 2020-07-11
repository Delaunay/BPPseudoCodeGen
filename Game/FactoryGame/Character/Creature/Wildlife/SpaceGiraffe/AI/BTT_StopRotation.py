
from codegen.ue4_stub import *

from Script.AIModule import K2_ClearFocus
from Script.AIModule import BTTask_BlueprintBase
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.AI.BTT_StopRotation import ExecuteUbergraph_BTT_StopRotation.K2Node_Event_ControlledPawn
from Script.AIModule import FinishExecute
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.AI.BTT_StopRotation import ExecuteUbergraph_BTT_StopRotation
from Script.FactoryGame import FGCreature
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.AI.BTT_StopRotation import ExecuteUbergraph_BTT_StopRotation.K2Node_Event_OwnerController

class BTT_StopRotation(BTTask_BlueprintBase):
    
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_StopRotation.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_StopRotation.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_StopRotation(10)
    

    def ExecuteUbergraph_BTT_StopRotation(self):
        OwnerController.StopMovement()
        OwnerController.K2_ClearFocus()
        AsFGCreature: Ptr[FGCreature] = Cast[FGCreature](ControlledPawn)
        bSuccess: bool = AsFGCreature
        if not bSuccess:
            goto('L204')
        AsFGCreature.CancelRotationMovement()
        self.FinishExecute(True)
    
