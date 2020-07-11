
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Char_NonFlyingBird import Char_NonFlyingBird
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTT_SetLuring import ExecuteUbergraph_BTT_SetLuring.K2Node_Event_ControlledPawn
from Script.AIModule import Default__BTFunctionLibrary
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTT_SetLuring import ExecuteUbergraph_BTT_SetLuring
from Script.AIModule import FinishExecute
from Script.AIModule import SetBlackboardValueAsBool
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import BlackboardKeySelector
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTT_SetLuring import ExecuteUbergraph_BTT_SetLuring.K2Node_Event_OwnerController

class BTT_SetLuring(BTTask_BlueprintBase):
    isLuring: bool
    mIsLuringBBKey: BlackboardKeySelector
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_SetLuring.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_SetLuring.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_SetLuring(10)
    

    def ExecuteUbergraph_BTT_SetLuring(self):
        Bird: Ptr[Char_NonFlyingBird] = Cast[Char_NonFlyingBird](ControlledPawn)
        bSuccess: bool = Bird
        if not bSuccess:
            goto('L201')
        Bird.SetLuring(self.isLuring)
        
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, self.isLuring, Ref[self.mIsLuringBBKey])
        self.FinishExecute(True)
        # End
        # Label 201
        self.FinishExecute(False)
    
