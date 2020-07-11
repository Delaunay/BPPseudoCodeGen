
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.AI.Decorator.BTD_CheckNextAttackInPattern import ExecuteUbergraph_BTD_CheckNextAttackInPattern.K2Node_Event_OwnerController
from Script.FactoryGame import FGEnemyController
from Game.FactoryGame.Character.Creature.AI.Decorator.BTD_CheckNextAttackInPattern import ExecuteUbergraph_BTD_CheckNextAttackInPattern
from Script.Engine import EqualEqual_ClassClass
from Script.AIModule import BTDecorator_BlueprintBase
from Game.FactoryGame.Character.Creature.AI.Decorator.BTD_CheckNextAttackInPattern import ExecuteUbergraph_BTD_CheckNextAttackInPattern.K2Node_Event_ControlledPawn
from Script.FactoryGame import FGAttack
from Script.FactoryGame import GetCurrentAttackFromPattern

class BTD_CheckNextAttackInPattern(BTDecorator_BlueprintBase):
    mAttackToCheck: TSubclassOf[FGAttack]
    
    def PerformConditionCheckAI(self):
        Controller: Ptr[FGEnemyController] = Cast[FGEnemyController](OwnerController)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L178')
        ReturnValue: TSubclassOf[FGAttack] = Controller.GetCurrentAttackFromPattern()
        ReturnValue_0: bool = EqualEqual_ClassClass(ReturnValue, self.mAttackToCheck)
        ReturnValue_1: bool = ReturnValue_0
    

    def ReceiveExecutionStartAI(self):
        ExecuteUbergraph_BTD_CheckNextAttackInPattern.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTD_CheckNextAttackInPattern.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTD_CheckNextAttackInPattern(10)
    

    def ExecuteUbergraph_BTD_CheckNextAttackInPattern(self):
        pass
    
