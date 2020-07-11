
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.AI.Task.BTT_EnemyAttack import ExecuteUbergraph_BTT_EnemyAttack.K2Node_Event_OwnerActor
from Game.FactoryGame.Character.Creature.AI.Task.BTT_EnemyAttack import ExecuteUbergraph_BTT_EnemyAttack
from Script.Engine import Pawn
from Script.FactoryGame import FGAttack
from Script.FactoryGame import GetAttackActivationDistance
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import FGEnemyController
from Script.Engine import K2_GetPawn
from Script.AIModule import FinishExecute
from Script.Engine import IsValid
from Script.FactoryGame import FGGameplayTask_AttackMelee
from Script.FactoryGame import Attack
from Script.FactoryGame import IsWithinRange
from Script.AIModule import FinishAbort
from Game.FactoryGame.Character.Creature.AI.Task.BTT_EnemyAttack import ExecuteUbergraph_BTT_EnemyAttack.K2Node_Event_OwnerController
from Script.GameplayTasks import ReadyForActivation
from Script.FactoryGame import Default__FGGameplayTask_AttackMelee
from Script.AIModule import BTTask_BlueprintBase
from Script.FactoryGame import Default__FGAttack
from Script.GameplayTasks import EndTask
from Script.FactoryGame import FGEnemy
from Script.FactoryGame import Default__FGCombatFunctionLibrary
from Script.AIModule import ReceiveAbort
from Game.FactoryGame.Character.Creature.AI.Task.BTT_EnemyAttack import ExecuteUbergraph_BTT_EnemyAttack.K2Node_Event_ControlledPawn
from Script.GameplayTasks import GameplayTask
from Script.AIModule import ReceiveAbortAI
from Script.AIModule import ReceiveExecuteAI
from Game.FactoryGame.Character.Creature.AI.Task.BTT_EnemyAttack import ExecuteUbergraph_BTT_EnemyAttack.K2Node_Event_OwnerController1
from Game.FactoryGame.Character.Creature.AI.Task.BTT_EnemyAttack import ExecuteUbergraph_BTT_EnemyAttack.K2Node_Event_ControlledPawn1

class BTT_EnemyAttack(BTTask_BlueprintBase):
    mAttackClass: TSubclassOf[FGAttack]
    mGameplayTask: Ptr[GameplayTask]
    
    def mOnAttackFailed_8426540B4FC18260A20A279426BD39C8(self):
        self.ExecuteUbergraph_BTT_EnemyAttack(97)
    

    def mOnAttackFinished_8426540B4FC18260A20A279426BD39C8(self):
        self.ExecuteUbergraph_BTT_EnemyAttack(58)
    

    def ReceiveAbort(self):
        ExecuteUbergraph_BTT_EnemyAttack.K2Node_Event_OwnerActor = OwnerActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_EnemyAttack(63)
    

    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_EnemyAttack.K2Node_Event_OwnerController1 = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_EnemyAttack.K2Node_Event_ControlledPawn1 = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_EnemyAttack(102)
    

    def ReceiveAbortAI(self):
        ExecuteUbergraph_BTT_EnemyAttack.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_EnemyAttack.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_EnemyAttack(862)
    

    def ExecuteUbergraph_BTT_EnemyAttack(self):
        # Label 10
        self.FinishExecute(True)
        # End
        # Label 26
        self.FinishExecute(True)
        # End
        # Label 42
        self.FinishExecute(False)
        # End
        goto('L26')
        self.ReceiveAbort(OwnerActor)
        self.FinishAbort()
        # End
        goto('L42')
        self.ReceiveExecuteAI(OwnerController1, ControlledPawn1)
        Controller: Ptr[FGEnemyController] = Cast[FGEnemyController](OwnerController1)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L927')
        ReturnValue: float = Default__FGAttack.GetAttackActivationDistance(self.mAttackClass)
        ReturnValue1: Ptr[Pawn] = Controller.K2_GetPawn()
        ReturnValue_0: bool = Default__FGCombatFunctionLibrary.IsWithinRange(ReturnValue1, Controller.mCurrentAggroTarget, ReturnValue)
        if not ReturnValue_0:
            goto('L42')
        ReturnValue_1: Ptr[Pawn] = Controller.K2_GetPawn()
        AsFGEnemy: Ptr[FGEnemy] = Cast[FGEnemy](ReturnValue_1)
        bSuccess1: bool = AsFGEnemy
        ReturnValue_2: Ptr[FGGameplayTask_AttackMelee] = Default__FGGameplayTask_AttackMelee.Attack(AsFGEnemy, Controller.mCurrentAggroTarget, self.mAttackClass)
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_2)
        if not ReturnValue_3:
            goto('L838')
        OutputDelegate.BindUFunction(self, mOnAttackFinished_8426540B4FC18260A20A279426BD39C8)
        ReturnValue_2.mOnAttackFinished.AddUnique(OutputDelegate)
        OutputDelegate1.BindUFunction(self, mOnAttackFailed_8426540B4FC18260A20A279426BD39C8)
        ReturnValue_2.mOnAttackFailed.AddUnique(OutputDelegate1)
        ReturnValue_2.ReadyForActivation()
        # Label 838
        self.mGameplayTask = ReturnValue_2
        # End
        self.ReceiveAbortAI(OwnerController, ControlledPawn)
        self.mGameplayTask.EndTask()
        goto('L10')
    
