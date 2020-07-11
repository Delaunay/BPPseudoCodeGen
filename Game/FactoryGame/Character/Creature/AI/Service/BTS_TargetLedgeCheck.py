
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.AI.Service.BTS_TargetLedgeCheck import ExecuteUbergraph_BTS_TargetLedgeCheck.K2Node_Event_DeltaSeconds
from Script.AIModule import GetBlackboardValueAsActor
from Script.Engine import VSize
from Script.AIModule import BTService_BlueprintBase
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Creature.AI.Service.BTS_TargetLedgeCheck import ExecuteUbergraph_BTS_TargetLedgeCheck.K2Node_Event_ControlledPawn
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import BlackboardKeySelector
from Script.Engine import IsValid
from Script.AIModule import GetBlackboardValueAsVector
from Script.Engine import BooleanOR
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.FactoryGame import FGEnemy
from Script.AIModule import ReceiveTickAI
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.Character.Creature.AI.Service.BTS_TargetLedgeCheck import ExecuteUbergraph_BTS_TargetLedgeCheck.K2Node_Event_OwnerController
from Game.FactoryGame.Character.Creature.AI.Service.BTS_TargetLedgeCheck import ExecuteUbergraph_BTS_TargetLedgeCheck

class BTS_TargetLedgeCheck(BTService_BlueprintBase):
    mBBKeyA: BlackboardKeySelector
    mBBKeyB: BlackboardKeySelector
    mBBKeyC: BlackboardKeySelector
    mCanFallDistance: float
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
        ExecuteUbergraph_BTS_TargetLedgeCheck.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_TargetLedgeCheck.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_TargetLedgeCheck.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTS_TargetLedgeCheck(10)
    

    def ExecuteUbergraph_BTS_TargetLedgeCheck(self):
        self.ReceiveTickAI(OwnerController, ControlledPawn, DeltaSeconds)
        AsFGEnemy: Ptr[FGEnemy] = Cast[FGEnemy](ControlledPawn)
        bSuccess: bool = AsFGEnemy
        if not bSuccess:
            goto('L597')
        
        location = None
        self.GetKeyLocation(self.mBBKeyA, Ref[location])
        
        location1 = None
        self.GetKeyLocation(self.mBBKeyB, Ref[location1])
        ReturnValue: Vector = Subtract_VectorVector(location, location1)
        
        location2 = None
        self.GetKeyLocation(self.mBBKeyA, Ref[location2])
        ReturnValue_0: float = VSize(ReturnValue)
        ReturnValue_1: bool = ReturnValue_0 <= self.mCanFallDistance
        
        location3 = None
        self.GetKeyLocation(self.mBBKeyC, Ref[location3])
        ReturnValue1: Vector = Subtract_VectorVector(location2, location3)
        ReturnValue1_0: float = VSize(ReturnValue1)
        ReturnValue1_1: bool = ReturnValue1_0 <= self.mCanFallDistance
        ReturnValue_2: bool = BooleanOR(ReturnValue_1, ReturnValue1_1)
        AsFGEnemy.CharacterMovement.bCanWalkOffLedges = ReturnValue_2
    
