
from codegen.ue4_stub import *

from Script.AIModule import GetBlackboardValueAsActor
from Script.AIModule import K2_SetFocus
from Script.Engine import Pawn
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.AI.BTT_RotateToTarget import ExecuteUbergraph_BTT_RotateToTarget.K2Node_CustomEvent_PawnRotated
from Script.CoreUObject import Rotator
from Script.FactoryGame import FGCreature
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.AI.BTT_RotateToTarget import ExecuteUbergraph_BTT_RotateToTarget.K2Node_Event_ControlledPawn
from Script.Engine import K2_GetPawn
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import FinishExecute
from Script.AIModule import BlackboardKeySelector
from Script.Engine import IsValid
from Script.AIModule import GetBlackboardValueAsVector
from Script.Engine import BreakRotator
from Script.Engine import Conv_VectorToRotator
from Script.AIModule import BTTask_BlueprintBase
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.AI.BTT_RotateToTarget import ExecuteUbergraph_BTT_RotateToTarget.K2Node_Event_ControlledPawn1
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.AI.BTT_RotateToTarget import ExecuteUbergraph_BTT_RotateToTarget.K2Node_Event_OwnerController
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.AI.BTT_RotateToTarget import ExecuteUbergraph_BTT_RotateToTarget.K2Node_Event_OwnerController1
from Script.Engine import K2_GetActorRotation
from Script.Engine import MakeRotator
from Script.Engine import NearlyEqual_FloatFloat
from Script.Engine import Actor
from Script.AIModule import K2_SetFocalPoint
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.AI.BTT_RotateToTarget import ExecuteUbergraph_BTT_RotateToTarget

class BTT_RotateToTarget(BTTask_BlueprintBase):
    mTargetLocationBBKey: BlackboardKeySelector
    mTargetRotation: float
    mTargetLocation: Vector
    mIsFacingRotation: bool
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_RotateToTarget.K2Node_Event_OwnerController1 = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_RotateToTarget.K2Node_Event_ControlledPawn1 = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_RotateToTarget(26)
    

    def RotationComplete(self, PawnRotated: Ptr[Pawn]):
        ExecuteUbergraph_BTT_RotateToTarget.K2Node_CustomEvent_PawnRotated = PawnRotated #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_RotateToTarget(1425)
    

    def ReceiveAbortAI(self):
        ExecuteUbergraph_BTT_RotateToTarget.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_RotateToTarget.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_RotateToTarget(2097)
    

    def ExecuteUbergraph_BTT_RotateToTarget(self):
        # Label 10
        self.FinishExecute(True)
        # End
        
        ReturnValue1: Ptr[Actor] = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.mTargetLocationBBKey])
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        if not ReturnValue:
            goto('L834')
        
        ReturnValue2: Ptr[Actor] = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.mTargetLocationBBKey])
        OwnerController1.K2_SetFocus(ReturnValue2)
        
        ReturnValue2 = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.mTargetLocationBBKey])
        ReturnValue3: Vector = ReturnValue2.K2_GetActorLocation()
        self.mTargetLocation = ReturnValue3
        # Label 365
        AsFGCreature: Ptr[FGCreature] = Cast[FGCreature](ControlledPawn1)
        bSuccess: bool = AsFGCreature
        if not bSuccess:
            goto('L1027')
        ReturnValue_0: Ptr[Pawn] = OwnerController1.K2_GetPawn()
        ReturnValue_1: Rotator = ReturnValue_0.K2_GetActorRotation()
        ReturnValue1_0: Vector = ReturnValue_0.K2_GetActorLocation()
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_1, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_2: Vector = Subtract_VectorVector(self.mTargetLocation, ReturnValue1_0)
        ReturnValue_3: Rotator = Conv_VectorToRotator(ReturnValue_2)
        
        Roll2 = None
        Pitch2 = None
        Yaw2 = None
        BreakRotator(ReturnValue_3, Ref[Roll2], Ref[Pitch2], Ref[Yaw2])
        ReturnValue_4: bool = NearlyEqual_FloatFloat(Yaw, Yaw2, 10)
        if not ReturnValue_4:
            goto('L1043')
        self.FinishExecute(True)
        # End
        
        # Label 834
        ReturnValue_5: Vector = Default__BTFunctionLibrary.GetBlackboardValueAsVector(self, Ref[self.mTargetLocationBBKey])
        OwnerController1.K2_SetFocalPoint(ReturnValue_5)
        
        ReturnValue_5 = Default__BTFunctionLibrary.GetBlackboardValueAsVector(self, Ref[self.mTargetLocationBBKey])
        self.mTargetLocation = ReturnValue_5
        goto('L365')
        # Label 1027
        self.FinishExecute(False)
        # End
        # Label 1043
        ReturnValue_0 = OwnerController1.K2_GetPawn()
        ReturnValue1_0 = ReturnValue_0.K2_GetActorLocation()
        ReturnValue_2 = Subtract_VectorVector(self.mTargetLocation, ReturnValue1_0)
        ReturnValue_3 = Conv_VectorToRotator(ReturnValue_2)
        
        Roll2 = None
        Pitch2 = None
        Yaw2 = None
        BreakRotator(ReturnValue_3, Ref[Roll2], Ref[Pitch2], Ref[Yaw2])
        ReturnValue_6: Rotator = MakeRotator(0, 0, Yaw2)
        AsFGCreature.StartRotationMovement(ReturnValue_6)
        OutputDelegate.BindUFunction(self, RotationComplete)
        AsFGCreature.mRotationDoneDelegate.AddUnique(OutputDelegate)
        # End
        AsFGCreature1: Ptr[FGCreature] = Cast[FGCreature](PawnRotated)
        bSuccess1: bool = AsFGCreature1
        if not bSuccess1:
            goto('L2223')
        AsFGCreature1.mRotationDoneDelegate.Clear()
        
        ReturnValue3_0: Ptr[Actor] = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.mTargetLocationBBKey])
        ReturnValue1_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue3_0)
        if not ReturnValue1_1:
            goto('L10')
        
        ReturnValue_7: Ptr[Actor] = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.mTargetLocationBBKey])
        ReturnValue_8: Vector = ReturnValue_7.K2_GetActorLocation()
        ReturnValue1_2: Rotator = AsFGCreature1.K2_GetActorRotation()
        
        Roll1 = None
        Pitch1 = None
        Yaw1 = None
        BreakRotator(ReturnValue1_2, Ref[Roll1], Ref[Pitch1], Ref[Yaw1])
        ReturnValue2_0: Vector = AsFGCreature1.K2_GetActorLocation()
        ReturnValue1_3: Vector = Subtract_VectorVector(ReturnValue_8, ReturnValue2_0)
        ReturnValue1_4: Rotator = Conv_VectorToRotator(ReturnValue1_3)
        
        Roll3 = None
        Pitch3 = None
        Yaw3 = None
        BreakRotator(ReturnValue1_4, Ref[Roll3], Ref[Pitch3], Ref[Yaw3])
        ReturnValue1_5: bool = NearlyEqual_FloatFloat(Yaw1, Yaw3, 10)
        self.FinishExecute(ReturnValue1_5)
        # End
        AsFGCreature2: Ptr[FGCreature] = Cast[FGCreature](ControlledPawn)
        bSuccess2: bool = AsFGCreature2
        if not bSuccess2:
            goto('L2223')
        AsFGCreature2.CancelRotationMovement()
        self.FinishExecute(True)
    
