
from codegen.ue4_stub import *

from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import FinishExecute
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.AI.BTT_ClearObject import ExecuteUbergraph_BTT_ClearObject.K2Node_Event_OwnerActor
from Script.AIModule import BlackboardKeySelector
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.AI.BTT_ClearObject import ExecuteUbergraph_BTT_ClearObject
from Script.AIModule import SetBlackboardValueAsObject

class BTT_ClearObject(BTTask_BlueprintBase):
    mObjectBBKey: BlackboardKeySelector
    
    def ReceiveExecute(self):
        ExecuteUbergraph_BTT_ClearObject.K2Node_Event_OwnerActor = OwnerActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_ClearObject(26)
    

    def ExecuteUbergraph_BTT_ClearObject(self):
        # Label 10
        self.FinishExecute(True)
        # End
        
        Default__BTFunctionLibrary.SetBlackboardValueAsObject(self, None, Ref[self.mObjectBBKey])
        goto('L10')
    
