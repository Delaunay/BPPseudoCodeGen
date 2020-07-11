
from codegen.ue4_stub import *

from Script.Engine import Actor
from Script.AIModule import GetAIController
from Script.AIModule import GetValueAsObject
from Script.AIModule import BlackboardComponent
from Script.AIModule import GetBlackboard
from Script.AIModule import EnvQueryContext_BlueprintBase
from Script.AIModule import Default__AIBlueprintHelperLibrary
from Script.CoreUObject import Object
from Script.AIModule import AIController

class Context_FinalTarget(EnvQueryContext_BlueprintBase):
    
    
    def ProvideSingleActor(self):
        localFinalGoal = "FinalGoal"
        ReturnValue: Ptr[AIController] = Default__AIBlueprintHelperLibrary.GetAIController(QuerierActor)
        ReturnValue_0: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(ReturnValue)
        
        ReturnValue_1: Ptr[Object] = ReturnValue_0.GetValueAsObject(Ref[localFinalGoal])
        AsActor: Ptr[Actor] = Cast[Actor](ReturnValue_1)
        bSuccess: bool = AsActor
        if not bSuccess:
            goto('L282')
        ResultingActor = AsActor
    
