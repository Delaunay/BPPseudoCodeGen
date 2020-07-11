
from codegen.ue4_stub import *

from Script.AIModule import GetBlackboardValueAsActor
from Script.Engine import Pawn
from Script.AIModule import AIController
from Script.AIModule import BTService_BlueprintBase
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import K2_GetPawn
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import BlackboardKeySelector
from Script.AIModule import Default__AIBlueprintHelperLibrary
from Script.Engine import IsValid
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.AI.BTS_LookAngleDiff import ExecuteUbergraph_BTS_LookAngleDiff.K2Node_Event_OwnerActor
from Script.Engine import Dot_VectorVector
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.AI.BTS_LookAngleDiff import ExecuteUbergraph_BTS_LookAngleDiff
from Script.AIModule import SetBlackboardValueAsBool
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.Engine import Normal
from Script.Engine import Actor
from Script.AIModule import GetAIController
from Script.Engine import K2_GetActorLocation
from Script.AIModule import GetBlackboardValueAsFloat
from Script.Engine import GetActorForwardVector
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.AI.BTS_LookAngleDiff import ExecuteUbergraph_BTS_LookAngleDiff.K2Node_Event_DeltaSeconds

class BTS_LookAngleDiff(BTService_BlueprintBase):
    mThreatBBKey: BlackboardKeySelector
    mSneakLimitBBKey: BlackboardKeySelector
    mIsInViewBBKey: BlackboardKeySelector
    
    def ReceiveTick(self):
        ExecuteUbergraph_BTS_LookAngleDiff.K2Node_Event_OwnerActor = OwnerActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_LookAngleDiff.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTS_LookAngleDiff(10)
    

    def ExecuteUbergraph_BTS_LookAngleDiff(self):
        
        ReturnValue: Ptr[Actor] = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.mThreatBBKey])
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L705')
        ReturnValue_1: Ptr[AIController] = Default__AIBlueprintHelperLibrary.GetAIController(OwnerActor)
        
        ReturnValue = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.mThreatBBKey])
        ReturnValue_2: Ptr[Pawn] = ReturnValue_1.K2_GetPawn()
        ReturnValue_3: Vector = ReturnValue_2.K2_GetActorLocation()
        ReturnValue1: Vector = ReturnValue.K2_GetActorLocation()
        ReturnValue_4: Vector = ReturnValue.GetActorForwardVector()
        ReturnValue_5: Vector = Subtract_VectorVector(ReturnValue1, ReturnValue_3)
        ReturnValue_6: Vector = Normal(ReturnValue_5, 9.999999747378752e-05)
        
        ReturnValue_7: float = Default__BTFunctionLibrary.GetBlackboardValueAsFloat(self, Ref[self.mSneakLimitBBKey])
        ReturnValue_8: float = Dot_VectorVector(ReturnValue_4, ReturnValue_6)
        ReturnValue_9: bool = ReturnValue_8 <= ReturnValue_7
        
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, ReturnValue_9, Ref[self.mIsInViewBBKey])
    
