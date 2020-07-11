
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Actor
from Script.AIModule import GetBlackboardValueAsActor
from Script.Engine import K2_GetActorLocation
from Script.AIModule import Default__BTFunctionLibrary
from Game.FactoryGame.Character.Creature.AI.Task.BTT_RandomLocation import ExecuteUbergraph_BTT_RandomLocation.K2Node_Event_ControlledPawn
from Script.AIModule import FinishExecute
from Script.AIModule import SetBlackboardValueAsVector
from Script.NavigationSystem import K2_GetRandomPointInNavigableRadius
from Script.CoreUObject import Vector
from Game.FactoryGame.Character.Creature.AI.Task.BTT_RandomLocation import ExecuteUbergraph_BTT_RandomLocation.K2Node_Event_OwnerController
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import BlackboardKeySelector
from Script.Engine import IsValid
from Script.NavigationSystem import Default__NavigationSystemV1
from Game.FactoryGame.Character.Creature.AI.Task.BTT_RandomLocation import ExecuteUbergraph_BTT_RandomLocation

class BTT_RandomLocation(BTTask_BlueprintBase):
    MoveToKey: BlackboardKeySelector
    ForceSuccess: bool
    FoundNewRandomPoint: bool = True
    mRadius: float = 1000
    CenterActorKey: BlackboardKeySelector
    mCenterLocation: Vector
    mTestLocation: Vector
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_RandomLocation.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_RandomLocation.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_RandomLocation(522)
    

    def ExecuteUbergraph_BTT_RandomLocation(self):
        # Label 10
        self.FinishExecute(self.ForceSuccess)
        # End
        
        # Label 34
        Default__BTFunctionLibrary.SetBlackboardValueAsVector(self, self.mTestLocation, Ref[self.MoveToKey])
        goto('L10')
        
        # Label 90
        ReturnValue: Ptr[Actor] = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.CenterActorKey])
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L440')
        
        ReturnValue = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.CenterActorKey])
        ReturnValue_1: Vector = ReturnValue.K2_GetActorLocation()
        self.mCenterLocation = ReturnValue_1
        
        RandomLocation = None
        # Label 336
        ReturnValue_2: bool = Default__NavigationSystemV1.K2_GetRandomPointInNavigableRadius(self, self.mRadius, None, None, Ref[self.mCenterLocation], Ref[RandomLocation])
        self.mTestLocation = RandomLocation
        goto('L34')
        # Label 440
        ReturnValue1: Vector = ControlledPawn.K2_GetActorLocation()
        self.mCenterLocation = ReturnValue1
        goto('L336')
        goto('L90')
    
