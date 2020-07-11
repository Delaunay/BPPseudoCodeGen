
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import FinishExecute
from Script.AIModule import SetBlackboardValueAsBool
from Script.AIModule import BlackboardKeySelector
from Game.FactoryGame.Character.Creature.AI.Task.BTT_StopPanic import ExecuteUbergraph_BTT_StopPanic
from Game.FactoryGame.Character.Creature.AI.Task.BTT_StopPanic import ExecuteUbergraph_BTT_StopPanic.K2Node_Event_OwnerActor
from Script.FactoryGame import FGCreatureController
from Script.Engine import PrintString
from Script.CoreUObject import LinearColor

class BTT_StopPanic(BTTask_BlueprintBase):
    DidPanicBBKey: BlackboardKeySelector
    
    def ReceiveExecute(self):
        ExecuteUbergraph_BTT_StopPanic.K2Node_Event_OwnerActor = OwnerActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_StopPanic(130)
    

    def ExecuteUbergraph_BTT_StopPanic(self):
        # Label 10
        Default__KismetSystemLibrary.PrintString(self, "cast failed in BTT_StopPanic", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        self.FinishExecute(False)
        # End
        Controller: Ptr[FGCreatureController] = Cast[FGCreatureController](OwnerActor)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L10')
        Controller.StopPanic()
        
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, False, Ref[self.DidPanicBBKey])
        self.FinishExecute(True)
    
