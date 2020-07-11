
from codegen.ue4_stub import *

from Script.Engine import Pawn
from Script.Engine import SpawnEmitterAtLocation
from Script.FactoryGame import FGAttack
from Game.FactoryGame.Character.Creature.AI.Task.BTT_NoRangeAttack import ExecuteUbergraph_BTT_NoRangeAttack.K2Node_Event_ControlledPawn
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import FGEnemyController
from Script.Engine import K2_GetPawn
from Game.FactoryGame.Character.Creature.Enemy.Hog.Particle.HogShockWave import HogShockWave
from Script.AIModule import FinishExecute
from Script.Engine import IsValid
from Game.FactoryGame.Character.Creature.Enemy.Hog.AlphaHog.Char_AlphaHog import Char_AlphaHog
from Script.FactoryGame import FGGameplayTask_AttackMelee
from Script.FactoryGame import Attack
from Game.FactoryGame.Character.Creature.Enemy.Stinger.BigStinger.Char_EliteCaveStinger import Char_EliteCaveStinger
from Script.Engine import Default__GameplayStatics
from Script.GameplayTasks import ReadyForActivation
from Script.FactoryGame import Default__FGGameplayTask_AttackMelee
from Script.AIModule import BTTask_BlueprintBase
from Script.CoreUObject import Vector
from Game.FactoryGame.Character.Creature.AI.Task.BTT_NoRangeAttack import ExecuteUbergraph_BTT_NoRangeAttack.K2Node_Event_OwnerController
from Script.FactoryGame import FGEnemy
from Game.FactoryGame.Character.Creature.Enemy.Stinger.BigStinger.Char_EliteStinger import Char_EliteStinger
from Script.GameplayTasks import GameplayTask
from Script.Engine import ParticleSystemComponent
from Script.AIModule import ReceiveExecuteAI
from Game.FactoryGame.Character.Creature.AI.Task.BTT_NoRangeAttack import ExecuteUbergraph_BTT_NoRangeAttack

class BTT_NoRangeAttack(BTTask_BlueprintBase):
    mAttackClass: TSubclassOf[FGAttack]
    mGameplayTask: Ptr[GameplayTask]
    
    def mOnAttackFailed_116612B142195CF8862D28AC809559CE(self):
        self.ExecuteUbergraph_BTT_NoRangeAttack(1425)
    

    def mOnAttackFinished_116612B142195CF8862D28AC809559CE(self):
        self.ExecuteUbergraph_BTT_NoRangeAttack(27)
    

    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_NoRangeAttack.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_NoRangeAttack.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_NoRangeAttack(39)
    

    def ExecuteUbergraph_BTT_NoRangeAttack(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.FinishExecute(True)
        goto(ExecutionFlow.Pop())
        self.FinishExecute(True)
        goto(ExecutionFlow.Pop())
        self.ReceiveExecuteAI(OwnerController, ControlledPawn)
        Controller: Ptr[FGEnemyController] = Cast[FGEnemyController](OwnerController)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L590")
        ReturnValue: Ptr[Pawn] = Controller.K2_GetPawn()
        AsFGEnemy: Ptr[FGEnemy] = Cast[FGEnemy](ReturnValue)
        bSuccess1: bool = AsFGEnemy
        ReturnValue_0: Ptr[FGGameplayTask_AttackMelee] = Default__FGGameplayTask_AttackMelee.Attack(AsFGEnemy, Controller.mCurrentAggroTarget, self.mAttackClass)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L570')
        OutputDelegate.BindUFunction(self, mOnAttackFinished_116612B142195CF8862D28AC809559CE)
        ReturnValue_0.mOnAttackFinished.AddUnique(OutputDelegate)
        OutputDelegate1.BindUFunction(self, mOnAttackFailed_116612B142195CF8862D28AC809559CE)
        ReturnValue_0.mOnAttackFailed.AddUnique(OutputDelegate1)
        ReturnValue_0.ReadyForActivation()
        # Label 570
        self.mGameplayTask = ReturnValue_0
        goto(ExecutionFlow.Pop())
        # Label 590
        ReturnValue = Controller.K2_GetPawn()
        AsFGEnemy = Cast[FGEnemy](ReturnValue)
        bSuccess1 = AsFGEnemy
        Hog: Ptr[Char_AlphaHog] = Cast[Char_AlphaHog](AsFGEnemy)
        bSuccess4: bool = Hog
        if not bSuccess4:
            goto('L956')
        ReturnValue_2: Vector = Hog.Mesh.GetSocketLocation("vfxjawSocket")
        ReturnValue_3: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, HogShockWave, ReturnValue_2, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        goto(ExecutionFlow.Pop())
        # Label 956
        ReturnValue = Controller.K2_GetPawn()
        AsFGEnemy = Cast[FGEnemy](ReturnValue)
        bSuccess1 = AsFGEnemy
        Stinger: Ptr[Char_EliteCaveStinger] = Cast[Char_EliteCaveStinger](AsFGEnemy)
        bSuccess2: bool = Stinger
        if not bSuccess2:
            goto('L1190')
        Stinger.SpawnGas()
        self.FinishExecute(True)
        goto(ExecutionFlow.Pop())
        # Label 1190
        ReturnValue = Controller.K2_GetPawn()
        AsFGEnemy = Cast[FGEnemy](ReturnValue)
        bSuccess1 = AsFGEnemy
        Stinger_0: Ptr[Char_EliteStinger] = Cast[Char_EliteStinger](AsFGEnemy)
        bSuccess3: bool = Stinger_0
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        Stinger_0.SpawnGas()
        goto('L15')
        # Label 1413
        self.FinishExecute(False)
        goto(ExecutionFlow.Pop())
        goto('L1413')
    
