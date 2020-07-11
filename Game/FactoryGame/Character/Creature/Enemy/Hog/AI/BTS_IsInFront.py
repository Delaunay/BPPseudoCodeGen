
from codegen.ue4_stub import *

from Script.Engine import NormalizedDeltaRotator
from Game.FactoryGame.Character.Creature.Enemy.Hog.AI.BTS_IsInFront import ExecuteUbergraph_BTS_IsInFront.K2Node_Event_ControlledPawn
from Script.CoreUObject import Rotator
from Script.AIModule import BTService_BlueprintBase
from Script.FactoryGame import GetCurrentAggroTarget
from Script.Engine import FindLookAtRotation
from Game.FactoryGame.Character.Creature.Enemy.Hog.AI.BTS_IsInFront import ExecuteUbergraph_BTS_IsInFront.K2Node_Event_OwnerController
from Script.Engine import Default__KismetSystemLibrary
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import BlackboardKeySelector
from Script.Engine import IsValid
from Script.Engine import InRange_FloatFloat
from Game.FactoryGame.Character.Creature.Enemy.Hog.AI.BTS_IsInFront import ExecuteUbergraph_BTS_IsInFront
from Script.Engine import BreakRotator
from Script.AIModule import SetBlackboardValueAsBool
from Script.CoreUObject import Vector
from Script.FactoryGame import FGEnemy
from Script.Engine import K2_GetActorRotation
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.Character.Creature.Enemy.Hog.AI.BTS_IsInFront import ExecuteUbergraph_BTS_IsInFront.K2Node_Event_DeltaSeconds

class BTS_IsInFront(BTService_BlueprintBase):
    mIsInFrontBBKey: BlackboardKeySelector
    
    def ReceiveTickAI(self):
        ExecuteUbergraph_BTS_IsInFront.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_IsInFront.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_IsInFront.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTS_IsInFront(10)
    

    def ExecuteUbergraph_BTS_IsInFront(self):
        AsFGEnemy: Ptr[FGEnemy] = Cast[FGEnemy](ControlledPawn)
        bSuccess: bool = AsFGEnemy
        if not bSuccess:
            goto('L618')
        ReturnValue: Ptr[Actor] = AsFGEnemy.GetCurrentAggroTarget()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L618')
        ReturnValue = AsFGEnemy.GetCurrentAggroTarget()
        ReturnValue_1: Rotator = AsFGEnemy.K2_GetActorRotation()
        ReturnValue_2: Vector = ReturnValue.K2_GetActorLocation()
        ReturnValue1: Vector = AsFGEnemy.K2_GetActorLocation()
        
        ReturnValue_3: Rotator = FindLookAtRotation(Ref[ReturnValue1], Ref[ReturnValue_2])
        ReturnValue_4: Rotator = NormalizedDeltaRotator(ReturnValue_3, ReturnValue_1)
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_4, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_5: bool = InRange_FloatFloat(Yaw, -100, 100, True, True)
        
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, ReturnValue_5, Ref[self.mIsInFrontBBKey])
    
