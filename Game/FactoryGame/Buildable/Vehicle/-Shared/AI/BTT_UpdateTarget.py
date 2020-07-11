
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Vehicle.BP_SelfDrivingController import BP_SelfDrivingController
from Script.Engine import K2_GetPawn
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import FinishExecute
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_UpdateTarget import ExecuteUbergraph_BTT_UpdateTarget
from Script.AIModule import BlackboardKeySelector
from Script.Engine import Pawn
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import BP_WheeledVehicle
from Script.AIModule import SetBlackboardValueAsObject
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_UpdateTarget import ExecuteUbergraph_BTT_UpdateTarget.K2Node_Event_OwnerActor
from Script.AIModule import GetBlackboardValueAsBool

class BTT_UpdateTarget(BTTask_BlueprintBase):
    TargetPoint: BlackboardKeySelector
    WantsNewTargetBBKey: BlackboardKeySelector
    
    def ReceiveExecute(self):
        ExecuteUbergraph_BTT_UpdateTarget.K2Node_Event_OwnerActor = OwnerActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_UpdateTarget(26)
    

    def ExecuteUbergraph_BTT_UpdateTarget(self):
        # Label 10
        self.FinishExecute(True)
        # End
        
        ReturnValue: bool = Default__BTFunctionLibrary.GetBlackboardValueAsBool(self, Ref[self.WantsNewTargetBBKey])
        if not ReturnValue:
            goto('L10')
        Controller: Ptr[BP_SelfDrivingController] = Cast[BP_SelfDrivingController](OwnerActor)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L463')
        ReturnValue_0: Ptr[Pawn] = Controller.K2_GetPawn()
        Vehicle: Ptr[BP_WheeledVehicle] = Cast[BP_WheeledVehicle](ReturnValue_0)
        bSuccess1: bool = Vehicle
        if not bSuccess1:
            goto('L463')
        
        newTarget = None
        Vehicle.SetNewPath(Ref[newTarget])
        
        Default__BTFunctionLibrary.SetBlackboardValueAsObject(self, newTarget, Ref[self.TargetPoint])
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(newTarget)
        self.FinishExecute(ReturnValue_1)
        # End
        # Label 463
        self.FinishExecute(False)
    
