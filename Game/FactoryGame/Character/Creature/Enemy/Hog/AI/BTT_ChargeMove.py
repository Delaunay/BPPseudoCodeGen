
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import K2_GetPawn
from Game.FactoryGame.Character.Creature.Enemy.Hog.AI.BTT_ChargeMove import ExecuteUbergraph_BTT_ChargeMove.K2Node_Event_OwnerActor
from Script.Engine import Delay
from Script.AIModule import FinishExecute
from Script.AIModule import BTTask_BlueprintBase
from Game.FactoryGame.Character.Creature.Enemy.Hog.AI.BTT_ChargeMove import ExecuteUbergraph_BTT_ChargeMove.K2Node_Event_OwnerController
from Game.FactoryGame.Character.Creature.Enemy.Hog.AI.BTT_ChargeMove import ExecuteUbergraph_BTT_ChargeMove.K2Node_Event_ControlledPawn
from Script.Engine import Pawn
from Game.FactoryGame.Character.Creature.Enemy.Hog.AI.BTT_ChargeMove import ExecuteUbergraph_BTT_ChargeMove
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import Char_Hog
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Character.Creature.Enemy.BP_EnemyController import BP_EnemyController

class BTT_ChargeMove(BTTask_BlueprintBase):
    CircleCharge: bool
    MaxChargeTime: float = 5
    
    def ReceiveExecute(self):
        ExecuteUbergraph_BTT_ChargeMove.K2Node_Event_OwnerActor = OwnerActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_ChargeMove(181)
    

    def ChargeComplete(self):
        self.ExecuteUbergraph_BTT_ChargeMove(478)
    

    def ReceiveAbortAI(self):
        ExecuteUbergraph_BTT_ChargeMove.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_ChargeMove.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_ChargeMove(490)
    

    def ExecuteUbergraph_BTT_ChargeMove(self):
        goto(ComputedJump("EntryPoint"))
        Hog.StopChargeMovement()
        goto(ExecutionFlow.Pop())
        # Label 52
        if not self.CircleCharge:
            goto('L147')
        Default__KismetSystemLibrary.Delay(self, self.MaxChargeTime, LatentActionInfo(Linkage = 15, UUID = 2126283025, ExecutionFunction = "ExecuteUbergraph_BTT_ChargeMove", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 147
        Hog.mCircling = False
        goto(ExecutionFlow.Pop())
        Controller: Ptr[BP_EnemyController] = Cast[BP_EnemyController](OwnerActor)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue: Ptr[Pawn] = Controller.K2_GetPawn()
        Hog: Ptr[Char_Hog] = Cast[Char_Hog](ReturnValue)
        bSuccess1: bool = Hog
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Hog.StartChargeMovement()
        OutputDelegate.BindUFunction(self, ChargeComplete)
        Hog.OnChargeMovementStopped.AddUnique(OutputDelegate)
        goto('L52')
        self.FinishExecute(True)
        goto(ExecutionFlow.Pop())
        Controller1: Ptr[BP_EnemyController] = Cast[BP_EnemyController](OwnerController)
        bSuccess2: bool = Controller1
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        ReturnValue1: Ptr[Pawn] = Controller1.K2_GetPawn()
        Hog1: Ptr[Char_Hog] = Cast[Char_Hog](ReturnValue1)
        bSuccess3: bool = Hog1
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        Hog1.StopChargeMovement()
        goto(ExecutionFlow.Pop())
    
