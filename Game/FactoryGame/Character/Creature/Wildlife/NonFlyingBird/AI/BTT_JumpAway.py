
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Char_NonFlyingBird import Char_NonFlyingBird
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTT_JumpAway import ExecuteUbergraph_BTT_JumpAway.K2Node_Event_ControlledPawn
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import FinishExecute
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Controller_NonFlyingBird import Controller_NonFlyingBird
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTT_JumpAway import ExecuteUbergraph_BTT_JumpAway.K2Node_CustomEvent_birdLanded
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTT_JumpAway import ExecuteUbergraph_BTT_JumpAway.K2Node_Event_OwnerController
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTT_JumpAway import ExecuteUbergraph_BTT_JumpAway
from Script.Engine import NotEqual_ByteByte

class BTT_JumpAway(BTTask_BlueprintBase):
    
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_JumpAway.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_JumpAway.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_JumpAway(26)
    

    def BirdHasLanded(self, birdLanded: Ptr[Char_NonFlyingBird]):
        ExecuteUbergraph_BTT_JumpAway.K2Node_CustomEvent_birdLanded = birdLanded #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_JumpAway(933)
    

    def ExecuteUbergraph_BTT_JumpAway(self):
        # Label 10
        self.FinishExecute(True)
        # End
        Bird: Ptr[Controller_NonFlyingBird] = Cast[Controller_NonFlyingBird](OwnerController)
        bSuccess1: bool = Bird
        if not bSuccess1:
            goto('L970')
        Bird.TryToJump()
        Bird_0: Ptr[Char_NonFlyingBird] = Cast[Char_NonFlyingBird](ControlledPawn)
        bSuccess: bool = Bird_0
        if not bSuccess:
            goto('L970')
        CmpSuccess: bool = NotEqual_ByteByte(Bird_0.CharacterMovement.MovementMode, 0)
        if not CmpSuccess:
            goto('L848')
        CmpSuccess = NotEqual_ByteByte(Bird_0.CharacterMovement.MovementMode, 1)
        if not CmpSuccess:
            goto('L848')
        CmpSuccess = NotEqual_ByteByte(Bird_0.CharacterMovement.MovementMode, 2)
        if not CmpSuccess:
            goto('L848')
        CmpSuccess = NotEqual_ByteByte(Bird_0.CharacterMovement.MovementMode, 3)
        if not CmpSuccess:
            goto('L864')
        CmpSuccess = NotEqual_ByteByte(Bird_0.CharacterMovement.MovementMode, 4)
        if not CmpSuccess:
            goto('L848')
        CmpSuccess = NotEqual_ByteByte(Bird_0.CharacterMovement.MovementMode, 5)
        if not CmpSuccess:
            goto('L848')
        CmpSuccess = NotEqual_ByteByte(Bird_0.CharacterMovement.MovementMode, 6)
        if not CmpSuccess:
            goto('L848')
        # End
        # Label 848
        self.FinishExecute(False)
        # End
        # Label 864
        OutputDelegate.BindUFunction(self, BirdHasLanded)
        Bird_0.OnLandedDelegate.AddUnique(OutputDelegate)
        # End
        birdLanded.OnLandedDelegate.Clear()
        goto('L10')
    
