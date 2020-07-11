
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.AI.Task.BTT_SetVectorKey import ExecuteUbergraph_BTT_SetVectorKey.K2Node_Event_OwnerActor
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import SetBlackboardValueAsVector
from Script.AIModule import FinishExecute
from Script.AIModule import BTTask_BlueprintBase
from Script.CoreUObject import Vector
from Script.Engine import EqualEqual_VectorVector
from Script.AIModule import BlackboardKeySelector
from Script.AIModule import ClearBlackboardValue
from Game.FactoryGame.Character.Creature.AI.Task.BTT_SetVectorKey import ExecuteUbergraph_BTT_SetVectorKey

class BTT_SetVectorKey(BTTask_BlueprintBase):
    mVectorKey: BlackboardKeySelector
    mValue: Vector
    mSucceed: bool
    
    def ReceiveExecute(self):
        ExecuteUbergraph_BTT_SetVectorKey.K2Node_Event_OwnerActor = OwnerActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_SetVectorKey(10)
    

    def ExecuteUbergraph_BTT_SetVectorKey(self):
        ReturnValue: Vector = Vector(0, 0, 0)
        ReturnValue_0: bool = EqualEqual_VectorVector(self.mValue, ReturnValue, 9.999999747378752e-05)
        if not ReturnValue_0:
            goto('L176')
        
        Default__BTFunctionLibrary.ClearBlackboardValue(self, Ref[self.mVectorKey])
        # Label 152
        self.FinishExecute(self.mSucceed)
        # End
        
        # Label 176
        Default__BTFunctionLibrary.SetBlackboardValueAsVector(self, self.mValue, Ref[self.mVectorKey])
        goto('L152')
    
