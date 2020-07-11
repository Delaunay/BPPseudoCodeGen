
from codegen.ue4_stub import *

from Script.Engine import K2_GetPawn
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import FinishExecute
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import Char_SpaceRabbit
from Script.Engine import Pawn
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.AI.BTT_WalkBackSlowly import ExecuteUbergraph_BTT_WalkBackSlowly
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.AI.BTT_WalkBackSlowly import ExecuteUbergraph_BTT_WalkBackSlowly.K2Node_Event_OwnerActor1
from Script.FactoryGame import FGCreatureController
from Script.AIModule import ReceiveAbort
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.AI.BTT_WalkBackSlowly import ExecuteUbergraph_BTT_WalkBackSlowly.K2Node_Event_OwnerActor

class BTT_WalkBackSlowly(BTTask_BlueprintBase):
    
    
    def ReceiveExecute(self):
        ExecuteUbergraph_BTT_WalkBackSlowly.K2Node_Event_OwnerActor1 = OwnerActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_WalkBackSlowly(270)
    

    def WalkBackComplete(self):
        self.ExecuteUbergraph_BTT_WalkBackSlowly(575)
    

    def ReceiveAbort(self):
        ExecuteUbergraph_BTT_WalkBackSlowly.K2Node_Event_OwnerActor = OwnerActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_WalkBackSlowly(10)
    

    def ExecuteUbergraph_BTT_WalkBackSlowly(self):
        self.ReceiveAbort(OwnerActor)
        Controller: Ptr[FGCreatureController] = Cast[FGCreatureController](OwnerActor)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L586')
        ReturnValue: Ptr[Pawn] = Controller.K2_GetPawn()
        Rabbit: Ptr[Char_SpaceRabbit] = Cast[Char_SpaceRabbit](ReturnValue)
        bSuccess2: bool = Rabbit
        if not bSuccess2:
            goto('L586')
        Rabbit.StopBackwardWalk()
        # End
        Controller1: Ptr[FGCreatureController] = Cast[FGCreatureController](OwnerActor1)
        bSuccess1: bool = Controller1
        if not bSuccess1:
            goto('L586')
        ReturnValue1: Ptr[Pawn] = Controller1.K2_GetPawn()
        Rabbit1: Ptr[Char_SpaceRabbit] = Cast[Char_SpaceRabbit](ReturnValue1)
        bSuccess3: bool = Rabbit1
        if not bSuccess3:
            goto('L586')
        Rabbit1.StartWalkBack()
        OutputDelegate.BindUFunction(self, WalkBackComplete)
        Rabbit1.OnWalkBackStopped.AddUnique(OutputDelegate)
        # End
        self.FinishExecute(True)
    
