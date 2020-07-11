
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.AI.Task.BTT_Counter import ExecuteUbergraph_BTT_Counter.K2Node_Event_OwnerActor
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import FinishExecute
from Game.FactoryGame.Character.Creature.AI.Task.BTT_Counter import ExecuteUbergraph_BTT_Counter
from Script.AIModule import SetBlackboardValueAsInt
from Script.AIModule import BlackboardKeySelector

class BTT_Counter(BTTask_BlueprintBase):
    mCounterKey: BlackboardKeySelector
    mMaxValue: int32
    mCurrent: int32
    
    def ReceiveExecute(self):
        ExecuteUbergraph_BTT_Counter.K2Node_Event_OwnerActor = OwnerActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_Counter(10)
    

    def ExecuteUbergraph_BTT_Counter(self):
        ReturnValue: int32 = self.mCurrent + 1
        Variable: int32 = ReturnValue
        self.mCurrent = Variable
        
        Default__BTFunctionLibrary.SetBlackboardValueAsInt(self, Variable, Ref[self.mCounterKey])
        ReturnValue_0: bool = self.mCurrent > self.mMaxValue
        ReturnValue1: bool = self.mMaxValue > 0
        ReturnValue_1: bool = ReturnValue_0 and ReturnValue1
        if not ReturnValue_1:
            goto('L355')
        self.mCurrent = 0
        
        Default__BTFunctionLibrary.SetBlackboardValueAsInt(self, self.mCurrent, Ref[self.mCounterKey])
        # Label 355
        self.FinishExecute(True)
    
