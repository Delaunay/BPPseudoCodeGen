
from codegen.ue4_stub import *

from Script.AIModule import GetValueAsBool
from Script.AIModule import BlackboardComponent
from Script.Engine import Delay
from Script.Engine import Pawn
from Script.AIModule import AIController
from Script.AIModule import SetValueAsBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import K2_GetPawn
from Script.AIModule import FinishExecute
from Game.FactoryGame.Character.Creature.AI.Task.BTT_GroupPanic import ExecuteUbergraph_BTT_GroupPanic
from Script.AIModule import Default__AIBlueprintHelperLibrary
from Script.Engine import IsValid
from Script.Engine import GetAllActorsOfClass
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import Char_Hog
from Game.FactoryGame.Character.Creature.AI.Task.BTT_GroupPanic import ExecuteUbergraph_BTT_GroupPanic.K2Node_Event_OwnerActor
from Script.Engine import Default__GameplayStatics
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import GetBlackboard
from Script.AIModule import GetAIController
from Script.Engine import GetDistanceTo
from Script.Engine import RandomFloatInRange

class BTT_GroupPanic(BTTask_BlueprintBase):
    MaxDistance: float = 1000
    GroupPanicBBKey: FName = GroupPanic
    DoPanicBBKey: FName = DoPanic
    MaxGroupDelay: float = 1.5
    
    def ReceiveExecute(self):
        ExecuteUbergraph_BTT_GroupPanic.K2Node_Event_OwnerActor = OwnerActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_GroupPanic(150)
    

    def ExecuteUbergraph_BTT_GroupPanic(self):
        goto(ComputedJump("EntryPoint"))
        self.FinishExecute(True)
        goto(ExecutionFlow.Pop())
        # Label 27
        ReturnValue: float = RandomFloatInRange(0.5, self.MaxGroupDelay)
        Default__KismetSystemLibrary.Delay(self, ReturnValue, LatentActionInfo(Linkage = 15, UUID = 2129601663, ExecutionFunction = "ExecuteUbergraph_BTT_GroupPanic", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue_0: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(OwnerActor)
        
        ReturnValue_1: bool = ReturnValue_0.GetValueAsBool(Ref[self.GroupPanicBBKey])
        if not ReturnValue_1:
            goto('L271')
        goto('L27')
        # Label 271
        OutActors: List[Ptr[Char_Hog]] = []
        
        Default__GameplayStatics.GetAllActorsOfClass(self, Char_Hog, Ref[OutActors])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 379
        ReturnValue_2: int32 = len(OutActors)
        ReturnValue_3: bool = Variable <= ReturnValue_2
        if not ReturnValue_3:
            goto('L1359')
        Variable_0 = Variable
        ExecutionFlow.Push("L1371")
        ReturnValue_4: Ptr[AIController] = Default__AIBlueprintHelperLibrary.GetAIController(OwnerActor)
        ReturnValue_5: Ptr[Pawn] = ReturnValue_4.K2_GetPawn()
        
        Item = None
        Item = OutActors[Variable_0]
        ReturnValue_6: float = Item.GetDistanceTo(ReturnValue_5)
        ReturnValue_7: bool = ReturnValue_6 <= self.MaxDistance
        if not ReturnValue_7:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = OutActors[Variable_0]
        ReturnValue1: Ptr[AIController] = Default__AIBlueprintHelperLibrary.GetAIController(Item)
        ReturnValue_8: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        if not ReturnValue_8:
           goto(ExecutionFlow.Pop())
        
        Item = None
        Item = OutActors[Variable_0]
        ReturnValue1 = Default__AIBlueprintHelperLibrary.GetAIController(Item)
        ReturnValue1_0: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(ReturnValue1)
        
        ReturnValue1_0.SetValueAsBool(True, Ref[self.GroupPanicBBKey])
        
        Item = None
        Item = OutActors[Variable_0]
        ReturnValue1 = Default__AIBlueprintHelperLibrary.GetAIController(Item)
        ReturnValue1_0 = Default__AIBlueprintHelperLibrary.GetBlackboard(ReturnValue1)
        
        ReturnValue1_0.SetValueAsBool(True, Ref[self.DoPanicBBKey])
        goto(ExecutionFlow.Pop())
        # Label 1359
        self.FinishExecute(True)
        goto(ExecutionFlow.Pop())
        # Label 1371
        ReturnValue_9: int32 = Variable + 1
        Variable = ReturnValue_9
        goto('L379')
    
