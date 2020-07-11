
from codegen.ue4_stub import *

from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import FinishExecute
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_ReverseToFreedom import ExecuteUbergraph_BTT_ReverseToFreedom
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_ReverseToFreedom import ExecuteUbergraph_BTT_ReverseToFreedom.K2Node_Event_OwnerController
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import BP_WheeledVehicle
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_ReverseToFreedom import ExecuteUbergraph_BTT_ReverseToFreedom.K2Node_Event_ControlledPawn

class BTT_ReverseToFreedom(BTTask_BlueprintBase):
    mIsStuckBBKey: bool
    
    def ReverseComplete(self):
        self.ExecuteUbergraph_BTT_ReverseToFreedom(194)
    

    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_ReverseToFreedom.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_ReverseToFreedom.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_ReverseToFreedom(10)
    

    def ExecuteUbergraph_BTT_ReverseToFreedom(self):
        Vehicle: Ptr[BP_WheeledVehicle] = Cast[BP_WheeledVehicle](ControlledPawn)
        bSuccess: bool = Vehicle
        if not bSuccess:
            goto('L205')
        Vehicle.ReverseToFreedom()
        OutputDelegate.BindUFunction(self, ReverseComplete)
        Vehicle.LocationReached.AddUnique(OutputDelegate)
        # End
        self.FinishExecute(True)
    
