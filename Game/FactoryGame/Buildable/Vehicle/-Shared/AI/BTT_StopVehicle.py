
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_StopVehicle import ExecuteUbergraph_BTT_StopVehicle.K2Node_Event_OwnerController
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_StopVehicle import ExecuteUbergraph_BTT_StopVehicle.K2Node_Event_ControlledPawn1
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_StopVehicle import ExecuteUbergraph_BTT_StopVehicle.K2Node_Event_ControlledPawn
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import FinishExecute
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_StopVehicle import ExecuteUbergraph_BTT_StopVehicle.K2Node_Event_OwnerController1
from Script.PhysXVehicles import SetHandbrakeInput
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import BP_WheeledVehicle
from Script.PhysXVehicles import WheeledVehicleMovementComponent
from Script.AIModule import ReceiveTickAI
from Script.PhysXVehicles import SetBrakeInput
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_StopVehicle import ExecuteUbergraph_BTT_StopVehicle.K2Node_Event_DeltaSeconds
from Script.PhysXVehicles import SetThrottleInput
from Script.FactoryGame import GetVehicleMovementComponent
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_StopVehicle import ExecuteUbergraph_BTT_StopVehicle

class BTT_StopVehicle(BTTask_BlueprintBase):
    mVehicle: Ptr[BP_WheeledVehicle]
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_StopVehicle.K2Node_Event_OwnerController1 = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_StopVehicle.K2Node_Event_ControlledPawn1 = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_StopVehicle(418)
    

    def ReceiveTickAI(self):
        ExecuteUbergraph_BTT_StopVehicle.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_StopVehicle.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_StopVehicle.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_StopVehicle(557)
    

    def ExecuteUbergraph_BTT_StopVehicle(self):
        # Label 10
        ReturnValue: Ptr[WheeledVehicleMovementComponent] = self.mVehicle.GetVehicleMovementComponent()
        ReturnValue.SetThrottleInput(0)
        self.FinishExecute(True)
        # End
        # Label 105
        ReturnValue = self.mVehicle.GetVehicleMovementComponent()
        ReturnValue.SetHandbrakeInput(True)
        # End
        # Label 185
        ReturnValue_0: bool = self.mVehicle.mSpeedInKMH > 0
        if not ReturnValue_0:
            goto('L10')
        ReturnValue = self.mVehicle.GetVehicleMovementComponent()
        ReturnValue.SetThrottleInput(-1)
        ReturnValue = self.mVehicle.GetVehicleMovementComponent()
        ReturnValue.SetBrakeInput(1)
        goto('L105')
        Vehicle: Ptr[BP_WheeledVehicle] = Cast[BP_WheeledVehicle](ControlledPawn1)
        bSuccess: bool = Vehicle
        if not bSuccess:
            goto('L599')
        self.mVehicle = Vehicle
        Vehicle.StopVehicle()
        # End
        self.ReceiveTickAI(OwnerController, ControlledPawn, DeltaSeconds)
        goto('L185')
    
