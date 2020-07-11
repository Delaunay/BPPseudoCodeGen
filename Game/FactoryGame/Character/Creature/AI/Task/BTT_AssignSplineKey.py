
from codegen.ue4_stub import *

from Script.FactoryGame import FGSplinePath
from Game.FactoryGame.Character.Creature.AI.Task.BTT_AssignSplineKey import ExecuteUbergraph_BTT_AssignSplineKey.K2Node_Event_OwnerController
from Script.FactoryGame import GetSplinePath
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import FinishExecute
from Script.AIModule import BlackboardKeySelector
from Game.FactoryGame.Character.Creature.AI.Task.BTT_AssignSplineKey import ExecuteUbergraph_BTT_AssignSplineKey
from Script.AIModule import SetBlackboardValueAsObject
from Game.FactoryGame.Character.Creature.AI.Task.BTT_AssignSplineKey import ExecuteUbergraph_BTT_AssignSplineKey.K2Node_Event_ControlledPawn
from Script.FactoryGame import FGCreature

class BTT_AssignSplineKey(BTTask_BlueprintBase):
    SplineKey: BlackboardKeySelector
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_AssignSplineKey.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_AssignSplineKey.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_AssignSplineKey(10)
    

    def ExecuteUbergraph_BTT_AssignSplineKey(self):
        AsFGCreature: Ptr[FGCreature] = Cast[FGCreature](ControlledPawn)
        bSuccess: bool = AsFGCreature
        if not bSuccess:
            goto('L193')
        ReturnValue: Ptr[FGSplinePath] = AsFGCreature.GetSplinePath()
        
        Default__BTFunctionLibrary.SetBlackboardValueAsObject(self, ReturnValue, Ref[self.SplineKey])
        self.FinishExecute(True)
    
