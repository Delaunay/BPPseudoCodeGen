
from codegen.ue4_stub import *

from Script.AIModule import GetBlackboardValueAsActor
from Game.FactoryGame.Character.Creature.AI.Task.BTT_MoveToActor import ExecuteUbergraph_BTT_MoveToActor.K2Node_Event_OwnerController
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Creature.AI.Task.BTT_MoveToActor import ExecuteUbergraph_BTT_MoveToActor.K2Node_CustomEvent_MovementResult
from Script.Engine import SelectFloat
from Game.FactoryGame.Character.Creature.AI.Task.BTT_MoveToActor import ExecuteUbergraph_BTT_MoveToActor.K2Node_CustomEvent_MovementResult1
from Game.FactoryGame.Character.Creature.AI.Task.BTT_MoveToActor import ExecuteUbergraph_BTT_MoveToActor
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import FinishExecute
from Script.AIModule import BlackboardKeySelector
from Script.AIModule import Default__AIBlueprintHelperLibrary
from Script.Engine import IsValid
from Script.AIModule import EPathFollowingResult
from Game.FactoryGame.Character.Creature.AI.Task.BTT_MoveToActor import ExecuteUbergraph_BTT_MoveToActor.K2Node_Event_ControlledPawn
from Script.AIModule import BTTask_BlueprintBase
from Script.Engine import Actor
from Script.AIModule import AIAsyncTaskBlueprintProxy
from Script.AIModule import GetBlackboardValueAsFloat
from Script.AIModule import CreateMoveToProxyObject

class BTT_MoveToActor(BTTask_BlueprintBase):
    mTargetActorBBKey: BlackboardKeySelector
    mAcceptanceRadius: float = -1
    mAcceptanceRadiusBBkey: BlackboardKeySelector
    
    def OnFail_A86C15A64D326131272CCA93E74F5421(self, MovementResult: uint8):
        ExecuteUbergraph_BTT_MoveToActor.K2Node_CustomEvent_MovementResult1 = MovementResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_MoveToActor(501)
    

    def OnSuccess_A86C15A64D326131272CCA93E74F5421(self, MovementResult: uint8):
        ExecuteUbergraph_BTT_MoveToActor.K2Node_CustomEvent_MovementResult = MovementResult #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_MoveToActor(544)
    

    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_MoveToActor.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_MoveToActor.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_MoveToActor(10)
    

    def ExecuteUbergraph_BTT_MoveToActor(self):
        
        ReturnValue: Ptr[Actor] = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.mTargetActorBBKey])
        ReturnValue_0: bool = self.mAcceptanceRadius > -1
        
        ReturnValue_1: float = Default__BTFunctionLibrary.GetBlackboardValueAsFloat(self, Ref[self.mAcceptanceRadiusBBkey])
        ReturnValue_2: float = SelectFloat(self.mAcceptanceRadius, ReturnValue_1, ReturnValue_0)
        ReturnValue_3: Ptr[AIAsyncTaskBlueprintProxy] = Default__AIBlueprintHelperLibrary.CreateMoveToProxyObject(ControlledPawn, ControlledPawn, Vector(0, 0, 0), ReturnValue, ReturnValue_2, True)
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_3)
        if not ReturnValue_4:
            goto('L582')
        OutputDelegate1.BindUFunction(self, OnSuccess_A86C15A64D326131272CCA93E74F5421)
        ReturnValue_3.OnSuccess.AddUnique(OutputDelegate1)
        OutputDelegate.BindUFunction(self, OnFail_A86C15A64D326131272CCA93E74F5421)
        ReturnValue_3.OnFail.AddUnique(OutputDelegate)
        # End
        Variable: uint8 = MovementResult1
        self.FinishExecute(False)
        # End
        Variable = MovementResult
        self.FinishExecute(True)
    
