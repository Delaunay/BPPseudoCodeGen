
from codegen.ue4_stub import *

from Script.AIModule import GetBlackboardValueAsActor
from Game.FactoryGame.Character.Creature.AI.Task.BTT_MoveWithinAttackRange import ExecuteUbergraph_BTT_MoveWithinAttackRange.K2Node_CustomEvent_MovementResult3
from Script.Engine import Pawn
from Script.FactoryGame import FGAttack
from Game.FactoryGame.Character.Creature.AI.Task.BTT_MoveWithinAttackRange import ExecuteUbergraph_BTT_MoveWithinAttackRange.K2Node_Event_OwnerController
from Script.FactoryGame import GetAttackActivationDistance
from Script.AIModule import AIController
from Script.Engine import Default__KismetSystemLibrary
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import FinishExecute
from Game.FactoryGame.Character.Creature.AI.Task.BTT_MoveWithinAttackRange import ExecuteUbergraph_BTT_MoveWithinAttackRange
from Script.AIModule import BlackboardKeySelector
from Script.AIModule import Default__AIBlueprintHelperLibrary
from Script.Engine import IsValid
from Script.AIModule import EPathFollowingResult
from Game.FactoryGame.Character.Creature.AI.Task.BTT_MoveWithinAttackRange import ExecuteUbergraph_BTT_MoveWithinAttackRange.K2Node_CustomEvent_MovementResult2
from Script.AIModule import GetBlackboardValueAsVector
from Script.AIModule import BTTask_BlueprintBase
from Game.FactoryGame.Character.Creature.AI.Task.BTT_MoveWithinAttackRange import ExecuteUbergraph_BTT_MoveWithinAttackRange.K2Node_CustomEvent_MovementResult1
from Script.FactoryGame import Default__FGAttack
from Script.CoreUObject import Vector
from Game.FactoryGame.Character.Creature.AI.Task.BTT_MoveWithinAttackRange import ExecuteUbergraph_BTT_MoveWithinAttackRange.K2Node_Event_ControlledPawn
from Game.FactoryGame.Character.Creature.AI.Task.BTT_MoveWithinAttackRange import ExecuteUbergraph_BTT_MoveWithinAttackRange.K2Node_CustomEvent_MovementResult
from Script.Engine import Actor
from Script.AIModule import AIAsyncTaskBlueprintProxy
from Script.Engine import IsValidClass
from Script.AIModule import CreateMoveToProxyObject

class BTT_MoveWithinAttackRange(BTTask_BlueprintBase):
    mTargetBBKey: BlackboardKeySelector
    mAttackClass: TSubclassOf[FGAttack]
    mPawn: Ptr[Pawn]
    mAIController: Ptr[AIController]
    
    def OnFail_FB4697D6429DCDB2C971F1AA11DB20A1(self, MovementResult: uint8):
        ExecuteUbergraph_BTT_MoveWithinAttackRange.K2Node_CustomEvent_MovementResult3 = MovementResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_MoveWithinAttackRange(1271)
    

    def OnSuccess_FB4697D6429DCDB2C971F1AA11DB20A1(self, MovementResult: uint8):
        ExecuteUbergraph_BTT_MoveWithinAttackRange.K2Node_CustomEvent_MovementResult2 = MovementResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_MoveWithinAttackRange(62)
    

    def OnFail_2F8CAD6F41C7875D308D88AD97B454B9(self, MovementResult: uint8):
        ExecuteUbergraph_BTT_MoveWithinAttackRange.K2Node_CustomEvent_MovementResult1 = MovementResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_MoveWithinAttackRange(105)
    

    def OnSuccess_2F8CAD6F41C7875D308D88AD97B454B9(self, MovementResult: uint8):
        ExecuteUbergraph_BTT_MoveWithinAttackRange.K2Node_CustomEvent_MovementResult = MovementResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_MoveWithinAttackRange(137)
    

    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_MoveWithinAttackRange.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_MoveWithinAttackRange.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_MoveWithinAttackRange(169)
    

    def ExecuteUbergraph_BTT_MoveWithinAttackRange(self):
        # Label 10
        self.mAIController.StopMovement()
        self.FinishExecute(False)
        # End
        Variable: uint8 = MovementResult2
        # Label 89
        self.FinishExecute(True)
        # End
        Variable1: uint8 = MovementResult1
        goto('L10')
        Variable1 = MovementResult
        goto('L89')
        self.mPawn = ControlledPawn
        self.mAIController = OwnerController
        ReturnValue: bool = Default__KismetSystemLibrary.IsValidClass(self.mAttackClass)
        if not ReturnValue:
            goto('L824')
        
        ReturnValue_0: Ptr[Actor] = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.mTargetBBKey])
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
            goto('L840')
        ReturnValue_2: float = Default__FGAttack.GetAttackActivationDistance(self.mAttackClass)
        ReturnValue_3: float = ReturnValue_2 * 0.8999999761581421
        
        ReturnValue1: Ptr[Actor] = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.mTargetBBKey])
        ReturnValue_4: Ptr[AIAsyncTaskBlueprintProxy] = Default__AIBlueprintHelperLibrary.CreateMoveToProxyObject(self, self.mPawn, Vector(0, 0, 0), ReturnValue1, ReturnValue_3, False)
        ReturnValue2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_4)
        if not ReturnValue2:
            goto('L1303')
        OutputDelegate.BindUFunction(self, OnSuccess_FB4697D6429DCDB2C971F1AA11DB20A1)
        ReturnValue_4.OnSuccess.AddUnique(OutputDelegate)
        OutputDelegate3.BindUFunction(self, OnFail_FB4697D6429DCDB2C971F1AA11DB20A1)
        ReturnValue_4.OnFail.AddUnique(OutputDelegate3)
        # End
        # Label 824
        self.FinishExecute(False)
        # End
        
        # Label 840
        ReturnValue_5: Vector = Default__BTFunctionLibrary.GetBlackboardValueAsVector(self, Ref[self.mTargetBBKey])
        ReturnValue1_0: float = Default__FGAttack.GetAttackActivationDistance(self.mAttackClass)
        ReturnValue1_1: float = ReturnValue1_0 * 0.8999999761581421
        ReturnValue1_2: Ptr[AIAsyncTaskBlueprintProxy] = Default__AIBlueprintHelperLibrary.CreateMoveToProxyObject(self, self.mPawn, ReturnValue_5, None, ReturnValue1_1, False)
        ReturnValue1_3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_2)
        if not ReturnValue1_3:
            goto('L1303')
        OutputDelegate2.BindUFunction(self, OnSuccess_2F8CAD6F41C7875D308D88AD97B454B9)
        ReturnValue1_2.OnSuccess.AddUnique(OutputDelegate2)
        OutputDelegate1.BindUFunction(self, OnFail_2F8CAD6F41C7875D308D88AD97B454B9)
        ReturnValue1_2.OnFail.AddUnique(OutputDelegate1)
        # End
        Variable = MovementResult3
        goto('L10')
    
