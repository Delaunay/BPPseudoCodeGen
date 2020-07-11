
from codegen.ue4_stub import *

from Script.AIModule import AISense_Hearing
from Script.AIModule import AIPerceptionComponent
from Script.Engine import Actor
from Script.AIModule import GetAIController
from Script.Engine import K2_GetActorLocation
from Script.Engine import Default__KismetArrayLibrary
from Game.FactoryGame.Character.Creature.AI.BP_EQSTestingPawn import BP_EQSTestingPawn
from Game.FactoryGame.Character.Creature.AI.BP_ThreatActor import BP_ThreatActor
from Script.AIModule import AISense_Sight
from Script.Engine import Default__GameplayStatics
from Script.CoreUObject import Vector
from Script.AIModule import EnvQueryContext_BlueprintBase
from Script.AIModule import Default__AIBlueprintHelperLibrary
from Script.Engine import Array_Append
from Script.Engine import GetAllActorsOfClass
from Script.AIModule import GetAIPerceptionComponent
from Script.AIModule import AIController
from Script.AIModule import GetPerceivedActors

class Context_KnownThreatLocations(EnvQueryContext_BlueprintBase):
    
    
    def ProvideLocationsSet(self):
        ExecutionFlow.Push("L1500")
        ReturnValue: Ptr[AIController] = Default__AIBlueprintHelperLibrary.GetAIController(QuerierActor)
        ReturnValue_0: Ptr[AIPerceptionComponent] = ReturnValue.GetAIPerceptionComponent()
        OutActors1: List[Ptr[Actor]] = []
        
        ReturnValue_0.GetPerceivedActors(AISense_Sight, Ref[OutActors1])
        
        Default__KismetArrayLibrary.Array_Append(Ref[hostileActors], Ref[OutActors1])
        ReturnValue = Default__AIBlueprintHelperLibrary.GetAIController(QuerierActor)
        ReturnValue_0 = ReturnValue.GetAIPerceptionComponent()
        OutActors: List[Ptr[Actor]] = []
        
        ReturnValue_0.GetPerceivedActors(AISense_Hearing, Ref[OutActors])
        
        Default__KismetArrayLibrary.Array_Append(Ref[hostileActors], Ref[OutActors])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 459
        ReturnValue_1: int32 = len(hostileActors)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
            goto('L780')
        Variable_0 = Variable
        ExecutionFlow.Push("L1320")
        
        Item = None
        Item = hostileActors[Variable_0]
        ReturnValue_3: Vector = Item.K2_GetActorLocation()
        
        ReturnValue1: int32 = locationSet.append(ReturnValue_3)
        goto(ExecutionFlow.Pop())
        # Label 780
        Pawn: Ptr[BP_EQSTestingPawn] = Cast[BP_EQSTestingPawn](QuerierActor)
        bSuccess: bool = Pawn
        if not bSuccess:
            goto('L1288')
        OutActors_0: List[Ptr[BP_ThreatActor]] = []
        
        Default__GameplayStatics.GetAllActorsOfClass(self, BP_ThreatActor, Ref[OutActors_0])
        Variable1: int32 = 0
        Variable1_0: int32 = 0
        
        # Label 967
        ReturnValue1_0: int32 = len(OutActors_0)
        ReturnValue1_1: bool = Variable1 <= ReturnValue1_0
        if not ReturnValue1_1:
            goto('L1394')
        Variable1_0 = Variable1
        ExecutionFlow.Push("L1426")
        
        Item1 = None
        Item1 = OutActors_0[Variable1_0]
        ReturnValue1_2: Vector = Item1.K2_GetActorLocation()
        
        ReturnValue_4: int32 = locationSet.append(ReturnValue1_2)
        goto(ExecutionFlow.Pop())
        # Label 1288
        ResultingLocationSet = locationSet
        # End
        # Label 1320
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L459')
        # Label 1394
        ResultingLocationSet = locationSet
        # End
        # Label 1426
        ReturnValue1_3: int32 = Variable1 + 1
        Variable1 = ReturnValue1_3
        goto('L967')
    
