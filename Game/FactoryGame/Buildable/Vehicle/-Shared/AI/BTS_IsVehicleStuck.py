
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTS_IsVehicleStuck import ExecuteUbergraph_BTS_IsVehicleStuck.K2Node_Event_DeltaSeconds
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTS_IsVehicleStuck import ExecuteUbergraph_BTS_IsVehicleStuck.K2Node_Event_ControlledPawn
from Script.FactoryGame import IsSimulated
from Script.Engine import BooleanOR
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import SetBlackboardValueAsBool
from Script.AIModule import BlackboardKeySelector
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTS_IsVehicleStuck import ExecuteUbergraph_BTS_IsVehicleStuck
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import BP_WheeledVehicle
from Script.Engine import Abs_Int
from Script.AIModule import BTService_BlueprintBase
from Script.Engine import Not_PreBool
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTS_IsVehicleStuck import ExecuteUbergraph_BTS_IsVehicleStuck.K2Node_Event_OwnerController
from Script.AIModule import GetBlackboardValueAsBool

class BTS_IsVehicleStuck(BTService_BlueprintBase):
    IsStuckKey: BlackboardKeySelector
    mTimeSpentStuck: float
    
    def ReceiveTickAI(self):
        ExecuteUbergraph_BTS_IsVehicleStuck.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_IsVehicleStuck.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_IsVehicleStuck.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTS_IsVehicleStuck(205)
    

    def ExecuteUbergraph_BTS_IsVehicleStuck(self):
        # Label 10
        self.mTimeSpentStuck = 0
        
        # Label 33
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, False, Ref[self.IsStuckKey])
        # End
        
        # Label 81
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, True, Ref[self.IsStuckKey])
        self.mTimeSpentStuck = 0
        # End
        # Label 152
        ReturnValue: bool = self.mTimeSpentStuck > 4
        if not ReturnValue:
            goto('L33')
        goto('L81')
        Vehicle: Ptr[BP_WheeledVehicle] = Cast[BP_WheeledVehicle](ControlledPawn)
        bSuccess: bool = Vehicle
        if not bSuccess:
            goto('L1117')
        
        ReturnValue_0: bool = Default__BTFunctionLibrary.GetBlackboardValueAsBool(self, Ref[self.IsStuckKey])
        ReturnValue_1: bool = Not_PreBool(ReturnValue_0)
        ReturnValue_2: bool = Vehicle.mSpeedLimit > 0
        ReturnValue_3: bool = Vehicle.IsSimulated()
        
        canMove = None
        Vehicle.canMove(Ref[canMove])
        ReturnValue1: bool = Not_PreBool(ReturnValue_3)
        ReturnValue_4: bool = Vehicle.mIsAtStation and ReturnValue_2
        ReturnValue1_0: bool = Vehicle.mSpeedLimit > 0
        ReturnValue2: bool = Not_PreBool(Vehicle.mIsAtStation)
        ReturnValue_5: bool = BooleanOR(ReturnValue2, ReturnValue_4)
        ReturnValue_6: int32 = Abs_Int(Vehicle.mSpeedInKMH)
        ReturnValue_7: bool = ReturnValue_6 <= 2
        ReturnValue1_1: bool = ReturnValue1 and ReturnValue_7
        ReturnValue2_0: bool = ReturnValue1_1 and ReturnValue1_0
        ReturnValue3: bool = ReturnValue2_0 and ReturnValue_1
        ReturnValue4: bool = ReturnValue3 and ReturnValue_5
        ReturnValue5: bool = ReturnValue4 and canMove
        if not ReturnValue5:
            goto('L10')
        ReturnValue_8: float = DeltaSeconds + self.mTimeSpentStuck
        self.mTimeSpentStuck = ReturnValue_8
        goto('L152')
    
