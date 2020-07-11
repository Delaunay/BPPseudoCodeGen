
from codegen.ue4_stub import *

from Script.AIModule import AISense_Hearing
from Script.AIModule import AIPerceptionComponent
from Script.Engine import Actor
from Script.Engine import Default__KismetArrayLibrary
from Script.AIModule import BTService_BlueprintBase
from Script.AIModule import Default__BTFunctionLibrary
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTS_TickStuff import ExecuteUbergraph_BTS_TickStuff.K2Node_Event_OwnerController
from Script.AIModule import SetBlackboardValueAsBool
from Script.AIModule import BlackboardKeySelector
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTS_TickStuff import ExecuteUbergraph_BTS_TickStuff.K2Node_Event_ControlledPawn
from Script.AIModule import GetAIPerceptionComponent
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Controller_NonFlyingBird import Controller_NonFlyingBird
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTS_TickStuff import ExecuteUbergraph_BTS_TickStuff.K2Node_Event_DeltaSeconds
from Script.Engine import RandomBool
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTS_TickStuff import ExecuteUbergraph_BTS_TickStuff
from Script.AIModule import GetPerceivedActors
from Script.AIModule import GetBlackboardValueAsBool

class BTS_TickStuff(BTService_BlueprintBase):
    mWantToFlyBBkey: BlackboardKeySelector
    Actors: List[Ptr[Actor]]
    
    def ReceiveTickAI(self):
        ExecuteUbergraph_BTS_TickStuff.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_TickStuff.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_TickStuff.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTS_TickStuff(10)
    

    def ExecuteUbergraph_BTS_TickStuff(self):
        
        ReturnValue: bool = Default__BTFunctionLibrary.GetBlackboardValueAsBool(self, Ref[self.mWantToFlyBBkey])
        if not ReturnValue:
            goto('L81')
        # End
        # Label 81
        Bird: Ptr[Controller_NonFlyingBird] = Cast[Controller_NonFlyingBird](OwnerController)
        bSuccess: bool = Bird
        if not bSuccess:
            goto('L441')
        ReturnValue_0: Ptr[AIPerceptionComponent] = Bird.GetAIPerceptionComponent()
        OutActors: List[Ptr[Actor]] = []
        
        ReturnValue_0.GetPerceivedActors(AISense_Hearing, Ref[OutActors])
        
        ReturnValue_1: int32 = len(OutActors)
        ReturnValue_2: bool = ReturnValue_1 > 0
        if not ReturnValue_2:
            goto('L441')
        ReturnValue_3: bool = RandomBool()
        
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, ReturnValue_3, Ref[self.mWantToFlyBBkey])
    
