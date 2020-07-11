
from codegen.ue4_stub import *

from Script.Engine import SelectFloat
from Script.Engine import Actor
from Script.Engine import GetDistanceTo
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import BTDecorator_BlueprintBase
from Script.AIModule import GetBlackboardValueAsFloat
from Script.AIModule import BlackboardKeySelector
from Script.CoreUObject import Object
from Script.AIModule import GetBlackboardValueAsObject
from Script.AIModule import PerformConditionCheckAI

class BTD_TooCloseToActor(BTDecorator_BlueprintBase):
    mOtherActorBBKey: BlackboardKeySelector
    mMinDistanceBBKey: BlackboardKeySelector
    mDistanceMultiplier: float = 1
    mDistance: float = -1
    bIsObservingBB = True
    
    def PerformConditionCheckAI(self):
        ReturnValue: bool = self.PerformConditionCheckAI(OwnerController, ControlledPawn)
        
        ReturnValue_0: Ptr[Object] = Default__BTFunctionLibrary.GetBlackboardValueAsObject(self, Ref[self.mOtherActorBBKey])
        AsActor: Ptr[Actor] = Cast[Actor](ReturnValue_0)
        bSuccess: bool = AsActor
        if not bSuccess:
            goto('L485')
        ReturnValue_1: bool = self.mDistance > -1
        
        ReturnValue_2: float = Default__BTFunctionLibrary.GetBlackboardValueAsFloat(self, Ref[self.mMinDistanceBBKey])
        ReturnValue_3: float = SelectFloat(self.mDistance, ReturnValue_2, ReturnValue_1)
        ReturnValue_4: float = ReturnValue_3 * self.mDistanceMultiplier
        ReturnValue_5: float = AsActor.GetDistanceTo(ControlledPawn)
        ReturnValue_6: bool = ReturnValue_5 <= ReturnValue_4
        ReturnValue_7: bool = ReturnValue_6
        goto('L496')
        # Label 485
        ReturnValue_7 = False
    
