
from codegen.ue4_stub import *

from Script.FactoryGame import FGTargetPointLinkedList
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_Wait import ExecuteUbergraph_BTT_Wait
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_Wait import ExecuteUbergraph_BTT_Wait.K2Node_Event_DeltaSeconds
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_Wait import ExecuteUbergraph_BTT_Wait.K2Node_Event_OwnerActor
from Script.FactoryGame import GetCurrentTarget
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_Wait import ExecuteUbergraph_BTT_Wait.K2Node_Event_ControlledPawn1
from Script.AIModule import FinishExecute
from Script.AIModule import ReceiveAbort
from Script.AIModule import BTTask_BlueprintBase
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_Wait import ExecuteUbergraph_BTT_Wait.K2Node_Event_OwnerController
from Script.FactoryGame import GetTargetNodeLinkedList
from Script.FactoryGame import FGTargetPoint
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_Wait import ExecuteUbergraph_BTT_Wait.K2Node_Event_OwnerController1
from Script.FactoryGame import GetWaitTime
from Script.AIModule import ReceiveTickAI
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BTT_Wait import ExecuteUbergraph_BTT_Wait.K2Node_Event_ControlledPawn
from Script.FactoryGame import FGWheeledVehicle

class BTT_Wait(BTTask_BlueprintBase):
    mVehicle: Ptr[FGWheeledVehicle]
    mTimer: float
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_Wait.K2Node_Event_OwnerController1 = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_Wait.K2Node_Event_ControlledPawn1 = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_Wait(49)
    

    def ReceiveTickAI(self):
        ExecuteUbergraph_BTT_Wait.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_Wait.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_Wait.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_Wait(152)
    

    def ReceiveAbort(self):
        ExecuteUbergraph_BTT_Wait.K2Node_Event_OwnerActor = OwnerActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_Wait(453)
    

    def ExecuteUbergraph_BTT_Wait(self):
        # Label 10
        self.mTimer = 0
        self.FinishExecute(True)
        # End
        Vehicle: Ptr[FGWheeledVehicle] = Cast[FGWheeledVehicle](ControlledPawn1)
        bSuccess: bool = Vehicle
        if not bSuccess:
            goto('L495')
        self.mVehicle = Vehicle
        # End
        self.ReceiveTickAI(OwnerController, ControlledPawn, DeltaSeconds)
        ReturnValue: Ptr[FGTargetPointLinkedList] = self.mVehicle.GetTargetNodeLinkedList()
        ReturnValue_0: Ptr[FGTargetPoint] = ReturnValue.GetCurrentTarget()
        ReturnValue_1: float = ReturnValue_0.GetWaitTime()
        ReturnValue_2: bool = ReturnValue_1 > self.mTimer
        if not ReturnValue_2:
            goto('L10')
        ReturnValue_3: float = self.mTimer + DeltaSeconds
        self.mTimer = ReturnValue_3
        # End
        self.ReceiveAbort(OwnerActor)
        self.mTimer = 0
    
