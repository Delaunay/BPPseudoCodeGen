
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Creature.Enemy.Stinger.AI.BTT_JumpAttack import ExecuteUbergraph_BTT_JumpAttack.K2Node_Event_ControlledPawn
from Script.GameplayTasks import ReadyForActivation
from Script.FactoryGame import FGGameplayTask_AttackJump
from Script.AIModule import FinishExecute
from Game.FactoryGame.Character.Creature.Enemy.Stinger.AI.BTT_JumpAttack import ExecuteUbergraph_BTT_JumpAttack
from Script.FactoryGame import StartJump
from Script.AIModule import BTTask_BlueprintBase
from Script.Engine import PrintString
from Script.FactoryGame import Default__FGGameplayTask_AttackJump
from Script.FactoryGame import FGAttackMeleeJump
from Game.FactoryGame.Character.Creature.Enemy.Stinger.AI.BTT_JumpAttack import ExecuteUbergraph_BTT_JumpAttack.K2Node_Event_OwnerController
from Script.Engine import IsValid
from Script.FactoryGame import FGEnemy
from Game.FactoryGame.Character.Creature.Enemy.Stinger.AI.BTT_JumpAttack import ExecuteUbergraph_BTT_JumpAttack.K2Node_Event_OwnerController1
from Game.FactoryGame.Character.Creature.Enemy.Stinger.AI.BTT_JumpAttack import ExecuteUbergraph_BTT_JumpAttack.K2Node_Event_ControlledPawn1
from Script.CoreUObject import LinearColor

class BTT_JumpAttack(BTTask_BlueprintBase):
    mAttackClass: TSubclassOf[FGAttackMeleeJump]
    mForwardSpeed: float = 600
    
    def mOnJumpAttackFailed_2B6962824822751FCAD482A8789ABE88(self):
        self.ExecuteUbergraph_BTT_JumpAttack(10)
    

    def mOnJumpAttackFinished_2B6962824822751FCAD482A8789ABE88(self):
        self.ExecuteUbergraph_BTT_JumpAttack(120)
    

    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_JumpAttack.K2Node_Event_OwnerController1 = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_JumpAttack.K2Node_Event_ControlledPawn1 = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_JumpAttack(136)
    

    def ReceiveAbortAI(self):
        ExecuteUbergraph_BTT_JumpAttack.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_JumpAttack.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_JumpAttack(492)
    

    def ExecuteUbergraph_BTT_JumpAttack(self):
        Default__KismetSystemLibrary.PrintString(self, "jump attack failed", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        self.FinishExecute(True)
        # End
        self.FinishExecute(True)
        # End
        AsFGEnemy: Ptr[FGEnemy] = Cast[FGEnemy](ControlledPawn1)
        bSuccess: bool = AsFGEnemy
        ReturnValue: Ptr[FGGameplayTask_AttackJump] = Default__FGGameplayTask_AttackJump.StartJump(AsFGEnemy, self.mAttackClass, False)
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L602')
        OutputDelegate1.BindUFunction(self, mOnJumpAttackFinished_2B6962824822751FCAD482A8789ABE88)
        ReturnValue.mOnJumpAttackFinished.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, mOnJumpAttackFailed_2B6962824822751FCAD482A8789ABE88)
        ReturnValue.mOnJumpAttackFailed.AddUnique(OutputDelegate)
        ReturnValue.ReadyForActivation()
        # End
        Default__KismetSystemLibrary.PrintString(self, "Jump attack was aborted", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        self.FinishExecute(True)
    
