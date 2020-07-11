
from codegen.ue4_stub import *

from Script.FactoryGame import FGTargetPointLinkedList
from Script.AIModule import BlackboardComponent
from Script.AIModule import AIController
from Script.AIModule import SetValueAsBool
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.AIModule import Default__AIBlueprintHelperLibrary
from Script.Engine import IsValid
from Script.FactoryGame import FGTargetPoint
from Game.FactoryGame.Buildable.Vehicle.BP_SelfDrivingController import ExecuteUbergraph_BP_SelfDrivingController.K2Node_Event_UnpossessedPawn
from Script.Engine import FlushNetDormancy
from Script.AIModule import GetBlackboard
from Script.FactoryGame import GetFirstTarget
from Game.FactoryGame.Buildable.Vehicle.BP_SelfDrivingController import ExecuteUbergraph_BP_SelfDrivingController.K2Node_Event_PossessedPawn
from Script.FactoryGame import SetCurrentTarget
from Game.FactoryGame.Buildable.Vehicle.BP_SelfDrivingController import ExecuteUbergraph_BP_SelfDrivingController
from Game.FactoryGame.Buildable.Vehicle.BP_WheeledVehicle import BP_WheeledVehicle
from Game.FactoryGame.Buildable.Vehicle.-Shared.AI.BT_SelfDrivingVehicle import BT_SelfDrivingVehicle
from Script.FactoryGame import GetTargetNodeLinkedList
from Script.Engine import K2_ClearAndInvalidateTimerHandle

class BP_SelfDrivingController(AIController):
    mWantsTargetBBKeyName: FName = WantsNewTarget
    PathFollowingComponent = Namespace(ObjectClass='/Script/AIModule.PathFollowingComponent', ObjectFlags=2883617, ObjectName='PathFollowingComponent')
    ActionsComp = Namespace(ObjectClass='/Script/AIModule.PawnActionsComponent', ObjectFlags=2883617, ObjectName='ActionsComp')
    TransformComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    
    def ReceivePossess(self):
        ExecuteUbergraph_BP_SelfDrivingController.K2Node_Event_PossessedPawn = PossessedPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SelfDrivingController(668)
    

    def ReceiveUnPossess(self):
        ExecuteUbergraph_BP_SelfDrivingController.K2Node_Event_UnpossessedPawn = UnpossessedPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_SelfDrivingController(10)
    

    def ExecuteUbergraph_BP_SelfDrivingController(self):
        Vehicle: Ptr[BP_WheeledVehicle] = Cast[BP_WheeledVehicle](UnpossessedPawn)
        bSuccess: bool = Vehicle
        if not bSuccess:
            goto('L1050')
        if not Vehicle.mIsFollowingPath:
            goto('L226')
        Vehicle.FlushNetDormancy()
        Vehicle.mIsFollowingPath = False
        Vehicle.OnRep_mIsFollowingPath()
        
        Vehicle.mUpdateMovementHandle = None
        # Label 226
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[Vehicle.mUpdateMovementHandle])
        ReturnValue: Ptr[FGTargetPointLinkedList] = Vehicle.GetTargetNodeLinkedList()
        ReturnValue.SetCurrentTarget(None)
        Vehicle.ClientClearAIMovment()
        self.BrainComponent.StopLogic("")
        # End
        # Label 444
        ReturnValue_0: bool = self.RunBehaviorTree(BT_SelfDrivingVehicle)
        Vehicle1.FlushNetDormancy()
        Vehicle1.mIsFollowingPath = True
        Vehicle1.OnRep_mIsFollowingPath()
        ReturnValue_1: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue_1.SetValueAsBool(True, Ref[self.mWantsTargetBBKeyName])
        # End
        Vehicle1: Ptr[BP_WheeledVehicle] = Cast[BP_WheeledVehicle](PossessedPawn)
        bSuccess1: bool = Vehicle1
        if not bSuccess1:
            goto('L1050')
        ReturnValue1: Ptr[FGTargetPointLinkedList] = Vehicle1.GetTargetNodeLinkedList()
        ReturnValue_2: Ptr[FGTargetPoint] = ReturnValue1.GetFirstTarget()
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_2)
        ReturnValue_4: bool = Not_PreBool(Vehicle1.mIsRecordSessionActive)
        ReturnValue_5: bool = ReturnValue_4 and ReturnValue_3
        ReturnValue1_0: bool = ReturnValue_5 and Vehicle1.mIsAutoPilotEnabled
        if not ReturnValue1_0:
            goto('L1050')
        goto('L444')
    
