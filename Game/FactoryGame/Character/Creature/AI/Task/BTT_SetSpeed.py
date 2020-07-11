
from codegen.ue4_stub import *

from Script.Engine import CharacterMovementComponent
from Game.FactoryGame.Character.Creature.AI.Task.BTT_SetSpeed import ExecuteUbergraph_BTT_SetSpeed.K2Node_Event_ControlledPawn
from Game.FactoryGame.Character.Creature.AI.Task.BTT_SetSpeed import ExecuteUbergraph_BTT_SetSpeed
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import FinishExecute
from Script.FactoryGame import SetMoveSpeed
from Script.Engine import PawnMovementComponent
from Script.FactoryGame import FGCreature
from Script.Engine import NotEqual_ByteByte
from Game.FactoryGame.Character.Creature.AI.Task.BTT_SetSpeed import ExecuteUbergraph_BTT_SetSpeed.K2Node_Event_OwnerController
from Script.FactoryGame import EMoveSpeed

class BTT_SetSpeed(BTTask_BlueprintBase):
    Speed: float
    ForceSuccess: bool
    MoveSpeed: uint8
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_SetSpeed.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_SetSpeed.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_SetSpeed(10)
    

    def ExecuteUbergraph_BTT_SetSpeed(self):
        AsFGCreature: Ptr[FGCreature] = Cast[FGCreature](ControlledPawn)
        bSuccess: bool = AsFGCreature
        if not bSuccess:
            goto('L464')
        ReturnValue: bool = NotEqual_ByteByte(self.MoveSpeed, 0)
        ReturnValue_0: bool = self.Speed <= 0
        ReturnValue_1: bool = ReturnValue and ReturnValue_0
        if not ReturnValue_1:
            goto('L285')
        AsFGCreature.SetMoveSpeed(self.MoveSpeed)
        # Label 247
        self.FinishExecute(self.ForceSuccess)
        # End
        # Label 285
        ReturnValue_2: Ptr[PawnMovementComponent] = AsFGCreature.GetMovementComponent()
        Component: Ptr[CharacterMovementComponent] = Cast[CharacterMovementComponent](ReturnValue_2)
        bSuccess1: bool = Component
        if not bSuccess1:
            goto('L464')
        Component.MaxWalkSpeed = self.Speed
        goto('L247')
    
