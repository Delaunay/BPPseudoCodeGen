
from codegen.ue4_stub import *

from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import BTDecorator_BlueprintBase
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.AIModule import BlackboardKeySelector
from Script.CoreUObject import Object
from Script.Engine import VSize
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import Char_Hog
from Script.AIModule import GetBlackboardValueAsObject
from Script.AIModule import PerformConditionCheckAI

class BTD_CloseEnoughToCharge(BTDecorator_BlueprintBase):
    mFinalGoalBBKey: BlackboardKeySelector
    bIsObservingBB = True
    
    def PerformConditionCheckAI(self):
        ReturnValue: bool = self.PerformConditionCheckAI(OwnerController, ControlledPawn)
        Hog: Ptr[Char_Hog] = Cast[Char_Hog](ControlledPawn)
        bSuccess: bool = Hog
        if not bSuccess:
            goto('L515')
        
        ReturnValue_0: Ptr[Object] = Default__BTFunctionLibrary.GetBlackboardValueAsObject(self, Ref[self.mFinalGoalBBKey])
        AsActor: Ptr[Actor] = Cast[Actor](ReturnValue_0)
        bSuccess1: bool = AsActor
        if not bSuccess1:
            goto('L515')
        ReturnValue_1: Vector = ControlledPawn.K2_GetActorLocation()
        ReturnValue1: Vector = AsActor.K2_GetActorLocation()
        ReturnValue_2: Vector = Subtract_VectorVector(ReturnValue1, ReturnValue_1)
        ReturnValue_3: float = VSize(ReturnValue_2)
        ReturnValue_4: bool = ReturnValue_3 <= Hog.mChargeDistance
        ReturnValue_5: bool = ReturnValue_4
        goto('L526')
        # Label 515
        ReturnValue_5 = False
    
