
from codegen.ue4_stub import *

from Script.AIModule import GetBlackboardValueAsActor
from Script.NavigationSystem import GetPathLength
from Script.Engine import Pawn
from Script.NavigationSystem import Default__NavigationSystemV1
from Script.AIModule import AIController
from Game.FactoryGame.Character.Creature.AI.Task.BTT_CheckValidPath import ExecuteUbergraph_BTT_CheckValidPath.K2Node_Event_OwnerActor
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import K2_GetPawn
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import FinishExecute
from Script.NavigationSystem import NavigationSystemV1
from Script.AIModule import BlackboardKeySelector
from Script.Engine import IsValid
from Script.AIModule import GetBlackboardValueAsVector
from Script.NavigationSystem import GetNavigationSystem
from Script.NavigationSystem import IsPartial
from Script.Engine import BooleanOR
from Script.AIModule import BTTask_BlueprintBase
from Script.AIModule import SetBlackboardValueAsBool
from Script.CoreUObject import Vector
from Script.NavigationSystem import NavigationQueryFilter
from Script.NavigationSystem import FindPathToLocationSynchronously
from Script.NavigationSystem import NavigationPath
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.Character.Creature.AI.Task.BTT_CheckValidPath import ExecuteUbergraph_BTT_CheckValidPath
from Script.Engine import NotEqual_VectorVector

class BTT_CheckValidPath(BTTask_BlueprintBase):
    mTargetObjectBBKey: BlackboardKeySelector
    mTargetLocationBBKey: BlackboardKeySelector
    mHasValidPath: BlackboardKeySelector
    mPathEnd: Vector
    NavFilter: TSubclassOf[NavigationQueryFilter]
    
    def ReceiveExecute(self):
        ExecuteUbergraph_BTT_CheckValidPath.K2Node_Event_OwnerActor = OwnerActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_CheckValidPath(1156)
    

    def ExecuteUbergraph_BTT_CheckValidPath(self):
        # Label 10
        self.FinishExecute(True)
        # End
        # Label 26
        self.FinishExecute(True)
        # End
        
        # Label 42
        ReturnValue: Ptr[Actor] = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.mTargetObjectBBKey])
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L836')
        
        ReturnValue = Default__BTFunctionLibrary.GetBlackboardValueAsActor(self, Ref[self.mTargetObjectBBKey])
        ReturnValue_1: Vector = ReturnValue.K2_GetActorLocation()
        self.mPathEnd = ReturnValue_1
        # Label 288
        AsAIController: Ptr[AIController] = Cast[AIController](OwnerActor)
        bSuccess: bool = AsAIController
        if not bSuccess:
            goto('L1161')
        ReturnValue_2: Ptr[NavigationSystemV1] = Default__NavigationSystemV1.GetNavigationSystem(self)
        ReturnValue_3: Ptr[Pawn] = AsAIController.K2_GetPawn()
        ReturnValue1: Vector = ReturnValue_3.K2_GetActorLocation()
        
        ReturnValue_4: Ptr[NavigationPath] = ReturnValue_2.FindPathToLocationSynchronously(self, ReturnValue_3, self.NavFilter, Ref[ReturnValue1], Ref[self.mPathEnd])
        ReturnValue_5: float = ReturnValue_4.GetPathLength()
        ReturnValue_6: bool = ReturnValue_5 <= 0
        ReturnValue_7: bool = ReturnValue_4.IsPartial()
        ReturnValue_8: bool = BooleanOR(ReturnValue_7, ReturnValue_6)
        ReturnValue_9: bool = Not_PreBool(ReturnValue_8)
        if not ReturnValue_9:
            goto('L1108')
        
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, True, Ref[self.mHasValidPath])
        goto('L10')
        
        # Label 836
        ReturnValue_10: Vector = Default__BTFunctionLibrary.GetBlackboardValueAsVector(self, Ref[self.mTargetLocationBBKey])
        ReturnValue_11: bool = NotEqual_VectorVector(ReturnValue_10, Vector(0, 0, 0), 9.999999747378752e-05)
        if not ReturnValue_11:
            goto('L1049')
        
        ReturnValue_10 = Default__BTFunctionLibrary.GetBlackboardValueAsVector(self, Ref[self.mTargetLocationBBKey])
        self.mPathEnd = ReturnValue_10
        goto('L288')
        
        # Label 1049
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, False, Ref[self.mHasValidPath])
        self.FinishExecute(True)
        # End
        
        # Label 1108
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, False, Ref[self.mHasValidPath])
        goto('L26')
        goto('L42')
    
