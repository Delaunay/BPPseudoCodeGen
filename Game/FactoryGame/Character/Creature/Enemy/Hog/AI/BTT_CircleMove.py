
from codegen.ue4_stub import *

from Script.Engine import Delay
from Script.Engine import Pawn
from Script.AIModule import AIController
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import K2_GetPawn
from Script.AIModule import FinishExecute
from Script.AIModule import Default__AIBlueprintHelperLibrary
from Script.Engine import GetAllActorsOfClass
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import Char_Hog
from Script.Engine import Default__GameplayStatics
from Game.FactoryGame.Character.Creature.Enemy.Hog.AI.BTT_CircleMove import ExecuteUbergraph_BTT_CircleMove.K2Node_Event_OwnerActor
from Script.AIModule import BTTask_BlueprintBase
from Game.FactoryGame.Character.Creature.Enemy.Hog.AI.BTT_CircleMove import ExecuteUbergraph_BTT_CircleMove
from Script.AIModule import GetAIController
from Script.Engine import GetDistanceTo
from Script.FactoryGame import IsAliveAndWell
from Game.FactoryGame.Character.Creature.Enemy.BP_EnemyController import BP_EnemyController
from Script.Engine import RandomFloatInRange

class BTT_CircleMove(BTTask_BlueprintBase):
    Start?: bool
    MinCircleTime: float
    MaxCircleTime: float
    MaxGroupDistance: float = 5000
    GroupSize: float
    
    def ReceiveExecute(self):
        ExecuteUbergraph_BTT_CircleMove.K2Node_Event_OwnerActor = OwnerActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_CircleMove(987)
    

    def FinishCircleMove(self):
        self.ExecuteUbergraph_BTT_CircleMove(1319)
    

    def ExecuteUbergraph_BTT_CircleMove(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.GroupSize = 0
        OutActors: List[Ptr[Char_Hog]] = []
        
        Default__GameplayStatics.GetAllActorsOfClass(self, Char_Hog, Ref[OutActors])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 146
        ReturnValue: int32 = len(OutActors)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
            goto('L725')
        Variable_0 = Variable
        ExecutionFlow.Push("L913")
        ReturnValue_1: Ptr[AIController] = Default__AIBlueprintHelperLibrary.GetAIController(OwnerActor)
        ReturnValue_2: Ptr[Pawn] = ReturnValue_1.K2_GetPawn()
        
        Item = None
        Item = OutActors[Variable_0]
        ReturnValue_3: bool = Item.IsAliveAndWell()
        ReturnValue_4: float = Item.GetDistanceTo(ReturnValue_2)
        ReturnValue_5: bool = ReturnValue_4 <= self.MaxGroupDistance
        ReturnValue_6: bool = ReturnValue_3 and ReturnValue_5
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        ReturnValue_7: float = self.GroupSize + 1
        Variable_1: float = ReturnValue_7
        self.GroupSize = Variable_1
        goto(ExecutionFlow.Pop())
        # Label 725
        ReturnValue_8: float = self.MaxCircleTime * self.GroupSize
        ReturnValue_9: float = RandomFloatInRange(self.MinCircleTime, ReturnValue_8)
        Default__KismetSystemLibrary.Delay(self, ReturnValue_9, LatentActionInfo(Linkage = 898, UUID = -1129119333, ExecutionFunction = "ExecuteUbergraph_BTT_CircleMove", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.FinishCircleMove()
        goto(ExecutionFlow.Pop())
        # Label 913
        ReturnValue_10: int32 = Variable + 1
        Variable = ReturnValue_10
        goto('L146')
        Controller: Ptr[BP_EnemyController] = Cast[BP_EnemyController](OwnerActor)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        ReturnValue1: Ptr[Pawn] = Controller.K2_GetPawn()
        Hog: Ptr[Char_Hog] = Cast[Char_Hog](ReturnValue1)
        bSuccess1: bool = Hog
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        if not self.Start?:
            goto('L1271')
        Hog.StartCircling(self)
        Hog.StartChargeMovement()
        goto('L15')
        # Label 1271
        Hog.StopCircling()
        self.FinishExecute(True)
        goto(ExecutionFlow.Pop())
        goto('L1271')
    
