
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_MoveToTargetPoint import ExecuteUbergraph_BTT_MoveToTargetPoint.K2Node_Event_OwnerController
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_MoveToTargetPoint import ExecuteUbergraph_BTT_MoveToTargetPoint.K2Node_Event_ControlledPawn1
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_MoveToTargetPoint import ExecuteUbergraph_BTT_MoveToTargetPoint.K2Node_Event_OwnerController1
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_MoveToTargetPoint import ExecuteUbergraph_BTT_MoveToTargetPoint
from Script.AIModule import FinishAbort
from Script.AIModule import ReceiveAbortAI
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import FinishExecute
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import BP_WheeledVehicle
from Script.Engine import K2_ClearAndInvalidateTimerHandle
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_MoveToTargetPoint import ExecuteUbergraph_BTT_MoveToTargetPoint.K2Node_Event_ControlledPawn

class BTT_MoveToTargetPoint(BTTask_BlueprintBase):
    
    
    def OnLocationReached(self):
        self.ExecuteUbergraph_BTT_MoveToTargetPoint(469)
    

    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_MoveToTargetPoint.K2Node_Event_OwnerController1 = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_MoveToTargetPoint.K2Node_Event_ControlledPawn1 = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_MoveToTargetPoint(41)
    

    def ReceiveAbortAI(self):
        ExecuteUbergraph_BTT_MoveToTargetPoint.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_MoveToTargetPoint.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_MoveToTargetPoint(225)
    

    def ExecuteUbergraph_BTT_MoveToTargetPoint(self):
        # Label 10
        self.FinishAbort()
        # End
        # Label 25
        self.FinishExecute(True)
        # End
        Vehicle: Ptr[BP_WheeledVehicle] = Cast[BP_WheeledVehicle](ControlledPawn1)
        bSuccess: bool = Vehicle
        if not bSuccess:
            goto('L474')
        Vehicle.MoveToLocation()
        OutputDelegate.BindUFunction(self, OnLocationReached)
        Vehicle.LocationReached.AddUnique(OutputDelegate)
        # End
        self.ReceiveAbortAI(OwnerController, ControlledPawn)
        Vehicle1: Ptr[BP_WheeledVehicle] = Cast[BP_WheeledVehicle](ControlledPawn)
        bSuccess1: bool = Vehicle1
        if not bSuccess1:
            goto('L474')
        Vehicle1.LocationReached.Clear()
        Vehicle1.StopVehicle()
        
        Vehicle1.mUpdateMovementHandle = None
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[Vehicle1.mUpdateMovementHandle])
        goto('L10')
        goto('L25')
    
