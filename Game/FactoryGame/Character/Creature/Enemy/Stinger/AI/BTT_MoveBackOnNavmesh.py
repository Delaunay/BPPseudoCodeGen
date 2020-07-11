
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.Enemy.Stinger.AI.BTT_MoveBackOnNavmesh import ExecuteUbergraph_BTT_MoveBackOnNavmesh
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import K2_GetActorLocation
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import SetBlackboardValueAsVector
from Script.AIModule import FinishExecute
from Script.AIModule import BTTask_BlueprintBase
from Script.CoreUObject import Vector
from Script.AIModule import BlackboardKeySelector
from Game.FactoryGame.Character.Creature.Enemy.Stinger.AI.BTT_MoveBackOnNavmesh import ExecuteUbergraph_BTT_MoveBackOnNavmesh.K2Node_Event_ControlledPawn
from Script.NavigationSystem import Default__NavigationSystemV1
from Script.NavigationSystem import K2_GetRandomPointInNavigableRadius
from Script.Engine import PrintString
from Game.FactoryGame.Character.Creature.Enemy.Stinger.AI.BTT_MoveBackOnNavmesh import ExecuteUbergraph_BTT_MoveBackOnNavmesh.K2Node_Event_OwnerController
from Script.CoreUObject import LinearColor

class BTT_MoveBackOnNavmesh(BTTask_BlueprintBase):
    mTargetLocation: BlackboardKeySelector
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_MoveBackOnNavmesh.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_MoveBackOnNavmesh.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_MoveBackOnNavmesh(26)
    

    def ExecuteUbergraph_BTT_MoveBackOnNavmesh(self):
        # Label 10
        self.FinishExecute(True)
        # End
        Default__KismetSystemLibrary.PrintString(self, "can't move to any location", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        ReturnValue: Vector = ControlledPawn.K2_GetActorLocation()
        
        RandomLocation = None
        ReturnValue_0: bool = Default__NavigationSystemV1.K2_GetRandomPointInNavigableRadius(self, 500, None, None, Ref[ReturnValue], Ref[RandomLocation])
        
        Default__BTFunctionLibrary.SetBlackboardValueAsVector(self, RandomLocation, Ref[self.mTargetLocation])
        goto('L10')
    
