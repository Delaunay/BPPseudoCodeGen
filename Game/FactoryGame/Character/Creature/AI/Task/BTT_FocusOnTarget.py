
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.AI.Task.BTT_FocusOnTarget import ExecuteUbergraph_BTT_FocusOnTarget.K2Node_Event_ControlledPawn
from Game.FactoryGame.Character.Creature.AI.Task.BTT_FocusOnTarget import ExecuteUbergraph_BTT_FocusOnTarget
from Game.FactoryGame.Character.Creature.AI.Task.BTT_FocusOnTarget import ExecuteUbergraph_BTT_FocusOnTarget.K2Node_Event_OwnerController
from Script.Engine import Actor
from Script.AIModule import K2_SetFocus
from Script.AIModule import K2_SetFocalPoint
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import FinishExecute
from Script.CoreUObject import Vector
from Script.AIModule import BlackboardKeySelector
from Script.CoreUObject import Object
from Script.AIModule import GetBlackboardValueAsObject
from Script.AIModule import GetBlackboardValueAsVector

class BTT_FocusOnTarget(BTTask_BlueprintBase):
    FinalGoalBBKey: BlackboardKeySelector
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_FocusOnTarget.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_FocusOnTarget.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_FocusOnTarget(26)
    

    def ExecuteUbergraph_BTT_FocusOnTarget(self):
        # Label 10
        self.FinishExecute(True)
        # End
        
        ReturnValue: Ptr[Object] = Default__BTFunctionLibrary.GetBlackboardValueAsObject(self, Ref[self.FinalGoalBBKey])
        AsActor: Ptr[Actor] = Cast[Actor](ReturnValue)
        bSuccess: bool = AsActor
        if not bSuccess:
            goto('L203')
        OwnerController.K2_SetFocus(AsActor)
        goto('L10')
        
        # Label 203
        ReturnValue_0: Vector = Default__BTFunctionLibrary.GetBlackboardValueAsVector(self, Ref[self.FinalGoalBBKey])
        OwnerController.K2_SetFocalPoint(ReturnValue_0)
        goto('L10')
    
