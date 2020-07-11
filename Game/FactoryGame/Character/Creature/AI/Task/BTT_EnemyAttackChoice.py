
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.AI.Task.BTT_EnemyAttackChoice import ExecuteUbergraph_BTT_EnemyAttackChoice.K2Node_Event_OwnerController1
from Game.FactoryGame.Character.Creature.AI.Task.BTT_EnemyAttackChoice import ExecuteUbergraph_BTT_EnemyAttackChoice.K2Node_Event_OwnerController
from Game.FactoryGame.Character.Creature.AI.Task.BTT_EnemyAttackChoice import ExecuteUbergraph_BTT_EnemyAttackChoice.K2Node_Event_ControlledPawn1
from Script.Engine import Pawn
from Script.FactoryGame import FGAttack
from Script.FactoryGame import GetAttackActivationDistance
from Script.Engine import GreaterEqual_IntInt
from Game.FactoryGame.Character.Creature.AI.Task.BTT_EnemyAttackChoice import ExecuteUbergraph_BTT_EnemyAttackChoice
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import FGEnemyController
from Script.Engine import K2_GetPawn
from Script.AIModule import Default__BTFunctionLibrary
from Game.FactoryGame.Character.Creature.AI.Task.BTT_EnemyAttackChoice import ExecuteUbergraph_BTT_EnemyAttackChoice.K2Node_Event_OwnerActor
from Script.AIModule import FinishExecute
from Script.AIModule import BlackboardKeySelector
from Script.Engine import IsValid
from Script.Engine import RandomFloat
from Game.FactoryGame.Character.Creature.AI.Task.BTT_EnemyAttackChoice import ExecuteUbergraph_BTT_EnemyAttackChoice.K2Node_Event_ControlledPawn
from Script.FactoryGame import FGGameplayTask_AttackMelee
from Script.FactoryGame import Attack
from Script.FactoryGame import IsWithinRange
from Script.Engine import BooleanOR
from Script.AIModule import FinishAbort
from Script.GameplayTasks import ReadyForActivation
from Script.FactoryGame import Default__FGGameplayTask_AttackMelee
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import SetBlackboardValueAsBool
from Script.FactoryGame import Default__FGAttack
from Script.GameplayTasks import EndTask
from Script.FactoryGame import FGEnemy
from Script.AIModule import ReceiveAbort
from Script.FactoryGame import Default__FGCombatFunctionLibrary
from Script.GameplayTasks import GameplayTask
from Script.AIModule import ReceiveAbortAI
from Script.AIModule import ReceiveExecuteAI

class BTT_EnemyAttackChoice(BTTask_BlueprintBase):
    mAttackClass: TSubclassOf[FGAttack]
    mAttackClass2: TSubclassOf[FGAttack]
    mChanceToDoFirstAttack: float = 0.5
    mGameplayTask: Ptr[GameplayTask]
    mAttackClassToDo: TSubclassOf[FGAttack]
    mAttack2Cooldown: bool
    mAttack2WaitAmount: int32 = 3
    mCooldownCounter: int32
    BoolBBKey: BlackboardKeySelector
    RandomMove: bool
    RandomMoveChance: float
    ForceAttack: bool
    
    def mOnAttackFailed_5A0EFF09427D5915F9D3B18E5D81C9BC(self):
        self.ExecuteUbergraph_BTT_EnemyAttackChoice(1456)
    

    def mOnAttackFinished_5A0EFF09427D5915F9D3B18E5D81C9BC(self):
        self.ExecuteUbergraph_BTT_EnemyAttackChoice(1451)
    

    def ReceiveAbort(self):
        ExecuteUbergraph_BTT_EnemyAttackChoice.K2Node_Event_OwnerActor = OwnerActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_EnemyAttackChoice(39)
    

    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_EnemyAttackChoice.K2Node_Event_OwnerController1 = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_EnemyAttackChoice.K2Node_Event_ControlledPawn1 = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_EnemyAttackChoice(69)
    

    def ReceiveAbortAI(self):
        ExecuteUbergraph_BTT_EnemyAttackChoice.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_EnemyAttackChoice.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_EnemyAttackChoice(1379)
    

    def ExecuteUbergraph_BTT_EnemyAttackChoice(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.FinishExecute(False)
        goto(ExecutionFlow.Pop())
        # Label 27
        self.FinishExecute(True)
        goto(ExecutionFlow.Pop())
        self.ReceiveAbort(OwnerActor)
        self.FinishAbort()
        goto(ExecutionFlow.Pop())
        self.ReceiveExecuteAI(OwnerController1, ControlledPawn1)
        Controller: Ptr[FGEnemyController] = Cast[FGEnemyController](OwnerController1)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue: float = RandomFloat()
        ReturnValue_0: bool = ReturnValue <= self.mChanceToDoFirstAttack
        if not ReturnValue_0:
            goto('L325')
        # Label 252
        self.mAttackClassToDo = self.mAttackClass
        ExecutionFlow.Push("L379")
        ExecutionFlow.Push("L1200")
        
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, False, Ref[self.BoolBBKey])
        goto(ExecutionFlow.Pop())
        # Label 325
        if not self.mAttack2Cooldown:
            goto('L344')
        goto('L252')
        # Label 344
        ExecutionFlow.Push("L1066")
        self.mAttackClassToDo = self.mAttackClass2
        self.mAttack2Cooldown = True
        # Label 379
        ReturnValue1: Ptr[Pawn] = Controller.K2_GetPawn()
        ReturnValue_1: float = Default__FGAttack.GetAttackActivationDistance(self.mAttackClassToDo)
        ReturnValue_2: bool = Default__FGCombatFunctionLibrary.IsWithinRange(ReturnValue1, Controller.mCurrentAggroTarget, ReturnValue_1)
        ReturnValue_3: bool = BooleanOR(ReturnValue_2, self.ForceAttack)
        if not ReturnValue_3:
            goto('L15')
        ReturnValue_4: Ptr[Pawn] = Controller.K2_GetPawn()
        AsFGEnemy: Ptr[FGEnemy] = Cast[FGEnemy](ReturnValue_4)
        bSuccess1: bool = AsFGEnemy
        ReturnValue_5: Ptr[FGGameplayTask_AttackMelee] = Default__FGGameplayTask_AttackMelee.Attack(AsFGEnemy, Controller.mCurrentAggroTarget, self.mAttackClassToDo)
        ReturnValue_6: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_5)
        if not ReturnValue_6:
            goto('L1046')
        OutputDelegate1.BindUFunction(self, mOnAttackFinished_5A0EFF09427D5915F9D3B18E5D81C9BC)
        ReturnValue_5.mOnAttackFinished.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, mOnAttackFailed_5A0EFF09427D5915F9D3B18E5D81C9BC)
        ReturnValue_5.mOnAttackFailed.AddUnique(OutputDelegate)
        ReturnValue_5.ReadyForActivation()
        # Label 1046
        self.mGameplayTask = ReturnValue_5
        goto(ExecutionFlow.Pop())
        # Label 1066
        if not self.RandomMove:
            goto('L1156')
        ReturnValue1_0: float = RandomFloat()
        ReturnValue1_1: bool = ReturnValue1_0 <= self.RandomMoveChance
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        
        # Label 1156
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, True, Ref[self.BoolBBKey])
        goto(ExecutionFlow.Pop())
        # Label 1200
        ReturnValue_7: int32 = self.mCooldownCounter + 1
        Variable: int32 = ReturnValue_7
        self.mCooldownCounter = Variable
        ReturnValue_8: bool = GreaterEqual_IntInt(Variable, self.mAttack2WaitAmount)
        if not ReturnValue_8:
           goto(ExecutionFlow.Pop())
        self.mCooldownCounter = 0
        self.mAttack2Cooldown = False
        goto(ExecutionFlow.Pop())
        self.ReceiveAbortAI(OwnerController, ControlledPawn)
        self.mGameplayTask.EndTask()
        self.FinishExecute(True)
        goto(ExecutionFlow.Pop())
        goto('L27')
        goto('L15')
    
