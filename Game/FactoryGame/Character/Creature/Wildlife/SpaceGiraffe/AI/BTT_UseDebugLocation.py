
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.AI.BTT_UseDebugLocation import ExecuteUbergraph_BTT_UseDebugLocation.K2Node_Event_ControlledPawn
from Script.Engine import K2_GetActorLocation
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import SetBlackboardValueAsVector
from Script.AIModule import FinishExecute
from Script.AIModule import BTTask_BlueprintBase
from Script.CoreUObject import Vector
from Script.AIModule import GetBlackboardValueAsFloat
from Script.Engine import GetForwardVector
from Script.AIModule import BlackboardKeySelector
from Script.Engine import ComposeRotators
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.AI.BTT_UseDebugLocation import ExecuteUbergraph_BTT_UseDebugLocation.K2Node_Event_OwnerController
from Script.CoreUObject import Rotator
from Script.Engine import K2_GetActorRotation
from Script.Engine import MakeRotator
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.AI.BTT_UseDebugLocation import ExecuteUbergraph_BTT_UseDebugLocation

class BTT_UseDebugLocation(BTTask_BlueprintBase):
    mRotationBBkey: BlackboardKeySelector
    mTargetLocation: BlackboardKeySelector
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_UseDebugLocation.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_UseDebugLocation.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_UseDebugLocation(26)
    

    def ExecuteUbergraph_BTT_UseDebugLocation(self):
        # Label 10
        self.FinishExecute(True)
        # End
        ReturnValue: Vector = ControlledPawn.K2_GetActorLocation()
        
        ReturnValue_0: float = Default__BTFunctionLibrary.GetBlackboardValueAsFloat(self, Ref[self.mRotationBBkey])
        ReturnValue_1: Rotator = ControlledPawn.K2_GetActorRotation()
        ReturnValue_2: Rotator = MakeRotator(0, 0, ReturnValue_0)
        ReturnValue_3: Rotator = ComposeRotators(ReturnValue_1, ReturnValue_2)
        ReturnValue_4: Vector = GetForwardVector(ReturnValue_3)
        ReturnValue_5: Vector = ReturnValue_4 * 1000
        ReturnValue_6: Vector = ReturnValue + ReturnValue_5
        
        Default__BTFunctionLibrary.SetBlackboardValueAsVector(self, ReturnValue_6, Ref[self.mTargetLocation])
        goto('L10')
    
