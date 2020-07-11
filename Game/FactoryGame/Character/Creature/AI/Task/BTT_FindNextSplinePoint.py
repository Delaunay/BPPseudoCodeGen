
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.AI.Task.BTT_FindNextSplinePoint import ExecuteUbergraph_BTT_FindNextSplinePoint.K2Node_Event_ControlledPawn
from Script.Engine import GetLocationAtSplinePoint
from Script.AIModule import GetBlackboardValueAsInt
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import ReceiveExecuteAI
from Game.FactoryGame.Character.Creature.AI.Task.BTT_FindNextSplinePoint import ExecuteUbergraph_BTT_FindNextSplinePoint.K2Node_Event_OwnerController
from Script.AIModule import SetBlackboardValueAsVector
from Script.AIModule import FinishExecute
from Game.FactoryGame.Character.Creature.Enemy.BP_Spline import BP_Spline
from Script.CoreUObject import Vector
from Script.AIModule import SetBlackboardValueAsInt
from Script.AIModule import BlackboardKeySelector
from Game.FactoryGame.Character.Creature.AI.Task.BTT_FindNextSplinePoint import ExecuteUbergraph_BTT_FindNextSplinePoint
from Script.CoreUObject import Object
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import GetBlackboardValueAsObject

class BTT_FindNextSplinePoint(BTTask_BlueprintBase):
    SplineKey: BlackboardKeySelector
    MoveToKey: BlackboardKeySelector
    ForceSucess: bool
    SplineIndexKey: BlackboardKeySelector
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_FindNextSplinePoint.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_FindNextSplinePoint.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_FindNextSplinePoint(10)
    

    def ExecuteUbergraph_BTT_FindNextSplinePoint(self):
        self.ReceiveExecuteAI(OwnerController, ControlledPawn)
        
        ReturnValue: Ptr[Object] = Default__BTFunctionLibrary.GetBlackboardValueAsObject(self, Ref[self.SplineKey])
        Spline: Ptr[BP_Spline] = Cast[BP_Spline](ReturnValue)
        bSuccess: bool = Spline
        if not bSuccess:
            goto('L552')
        
        ReturnValue_0: int32 = Default__BTFunctionLibrary.GetBlackboardValueAsInt(self, Ref[self.SplineIndexKey])
        ReturnValue_1: Vector = Spline.mSpline.GetLocationAtSplinePoint(ReturnValue_0, 1)
        
        Default__BTFunctionLibrary.SetBlackboardValueAsVector(self, ReturnValue_1, Ref[self.MoveToKey])
        
        ReturnValue_0 = Default__BTFunctionLibrary.GetBlackboardValueAsInt(self, Ref[self.SplineIndexKey])
        
        nextIndex = None
        Spline.GetNextSplineIndex(ReturnValue_0, Ref[nextIndex])
        
        Default__BTFunctionLibrary.SetBlackboardValueAsInt(self, nextIndex, Ref[self.SplineIndexKey])
        self.FinishExecute(self.ForceSucess)
        # End
        # Label 552
        self.FinishExecute(self.ForceSucess)
    
