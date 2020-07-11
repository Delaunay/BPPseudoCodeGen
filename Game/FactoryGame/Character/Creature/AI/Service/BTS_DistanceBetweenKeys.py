
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Creature.AI.Service.BTS_DistanceBetweenKeys import ExecuteUbergraph_BTS_DistanceBetweenKeys.K2Node_Event_ControlledPawn
from Script.Engine import Actor
from Script.AIModule import GetBlackboardValueAsActor
from Script.Engine import K2_GetActorLocation
from Script.AIModule import SetBlackboardValueAsFloat
from Script.AIModule import Default__BTFunctionLibrary
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.AIModule import BlackboardKeySelector
from Script.Engine import IsValid
from Game.FactoryGame.Character.Creature.AI.Service.BTS_DistanceBetweenKeys import ExecuteUbergraph_BTS_DistanceBetweenKeys
from Script.Engine import VSize
from Game.FactoryGame.Character.Creature.AI.Service.BTS_DistanceBetweenKeys import ExecuteUbergraph_BTS_DistanceBetweenKeys.K2Node_Event_OwnerController
from Game.FactoryGame.Character.Creature.AI.Service.BTS_DistanceBetweenKeys import ExecuteUbergraph_BTS_DistanceBetweenKeys.K2Node_Event_DeltaSeconds
from Script.AIModule import ReceiveTickAI
from Script.AIModule import BTService_BlueprintBase
from Script.AIModule import GetBlackboardValueAsVector

class BTS_DistanceBetweenKeys(BTService_BlueprintBase):
    mBBKeyA: BlackboardKeySelector
    mBBKeyB: BlackboardKeySelector
    mDistanceBBKey: BlackboardKeySelector
    NodeName = BTS_DistanceBetweenKeys
    
    def GetKeyLocation(self, Key: BlackboardKeySelector):
        
        ReturnValue: Ptr[Actor] = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[Key])
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L278')
        
        ReturnValue = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[Key])
        ReturnValue_1: Vector = ReturnValue.K2_GetActorLocation()
        Location: Vector = ReturnValue_1
        # Label 246
        Location_0: Vector = Location
        # End
        
        # Label 278
        ReturnValue_2: Vector = Default__BTFunctionLibrary.GetBlackboardValueAsVector(self, Ref[Key])
        Location = ReturnValue_2
        goto('L246')
    

    def ReceiveTickAI(self):
        ExecuteUbergraph_BTS_DistanceBetweenKeys.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_DistanceBetweenKeys.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_DistanceBetweenKeys.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTS_DistanceBetweenKeys(10)
    

    def ExecuteUbergraph_BTS_DistanceBetweenKeys(self):
        self.ReceiveTickAI(OwnerController, ControlledPawn, DeltaSeconds)
        
        location = None
        self.GetKeyLocation(self.mBBKeyA, Ref[location])
        
        location1 = None
        self.GetKeyLocation(self.mBBKeyB, Ref[location1])
        ReturnValue: Vector = Subtract_VectorVector(location, location1)
        ReturnValue_0: float = VSize(ReturnValue)
        
        Default__BTFunctionLibrary.SetBlackboardValueAsFloat(self, ReturnValue_0, Ref[self.mDistanceBBKey])
    
