
from codegen.ue4_stub import *

from Script.Engine import K2_GetPawn
from Script.AIModule import BTDecorator_BlueprintBase
from Script.Engine import Pawn
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import BP_WheeledVehicle
from Script.AIModule import AIController

class BTD_AtStation(BTDecorator_BlueprintBase):
    
    
    def PerformConditionCheck(self):
        AsAIController: Ptr[AIController] = Cast[AIController](OwnerActor)
        bSuccess: bool = AsAIController
        if not bSuccess:
            goto('L246')
        ReturnValue: Ptr[Pawn] = AsAIController.K2_GetPawn()
        Vehicle: Ptr[BP_WheeledVehicle] = Cast[BP_WheeledVehicle](ReturnValue)
        bSuccess1: bool = Vehicle
        if not bSuccess1:
            goto('L246')
        ReturnValue_0: bool = Vehicle.mIsAtStation
        goto('L257')
        # Label 246
        ReturnValue_0 = False
    
