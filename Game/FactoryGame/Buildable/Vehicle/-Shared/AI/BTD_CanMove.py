
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.Vehicle.BP_SelfDrivingController import BP_SelfDrivingController
from Script.Engine import K2_GetPawn
from Script.AIModule import BTDecorator_BlueprintBase
from Script.Engine import Pawn
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import BP_WheeledVehicle

class BTD_CanMove(BTDecorator_BlueprintBase):
    
    
    def PerformConditionCheck(self):
        Controller: Ptr[BP_SelfDrivingController] = Cast[BP_SelfDrivingController](OwnerActor)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L269')
        ReturnValue: Ptr[Pawn] = Controller.K2_GetPawn()
        Vehicle: Ptr[BP_WheeledVehicle] = Cast[BP_WheeledVehicle](ReturnValue)
        bSuccess1: bool = Vehicle
        if not bSuccess1:
            goto('L269')
        
        canMove = None
        Vehicle.canMove(Ref[canMove])
        ReturnValue_0: bool = canMove
        goto('L280')
        # Label 269
        ReturnValue_0 = False
    
