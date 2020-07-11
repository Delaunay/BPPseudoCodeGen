
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.AI.Task.BTT_SetBoolKey import ExecuteUbergraph_BTT_SetBoolKey
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import FinishExecute
from Script.AIModule import SetBlackboardValueAsBool
from Script.AIModule import BlackboardKeySelector
from Game.FactoryGame.Character.Creature.AI.Task.BTT_SetBoolKey import ExecuteUbergraph_BTT_SetBoolKey.K2Node_Event_OwnerActor

class BTT_SetBoolKey(BTTask_BlueprintBase):
    mBoolBBKey: BlackboardKeySelector
    mValue: bool
    mSucceed: bool
    
    def ReceiveExecute(self):
        ExecuteUbergraph_BTT_SetBoolKey.K2Node_Event_OwnerActor = OwnerActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_SetBoolKey(34)
    

    def ExecuteUbergraph_BTT_SetBoolKey(self):
        # Label 10
        self.FinishExecute(self.mSucceed)
        # End
        
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, self.mValue, Ref[self.mBoolBBKey])
        goto('L10')
    
