
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.AI.Service.BTS_FindTarget import ExecuteUbergraph_BTS_FindTarget.K2Node_Event_OwnerController
from Script.Engine import Delay
from Script.FactoryGame import FGCharacterPlayer
from Script.NavigationSystem import GetPathLength
from Game.FactoryGame.Character.Creature.AI.Service.BTS_FindTarget import ExecuteUbergraph_BTS_FindTarget.K2Node_Event_ControlledPawn
from Script.NavigationSystem import Default__NavigationSystemV1
from Script.AIModule import BTService_BlueprintBase
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.AIModule import Default__BTFunctionLibrary
from Game.FactoryGame.Character.Creature.AI.Service.BTS_FindTarget import ExecuteUbergraph_BTS_FindTarget
from Script.AIModule import BlackboardKeySelector
from Script.CoreUObject import Object
from Script.Engine import IsValid
from Script.NavigationSystem import IsPartial
from Script.Engine import BooleanOR
from Script.AIModule import SetBlackboardValueAsBool
from Script.CoreUObject import Vector
from Script.NavigationSystem import NavigationQueryFilter
from Game.FactoryGame.Character.Creature.AI.Service.BTS_FindTarget import ExecuteUbergraph_BTS_FindTarget.K2Node_Event_DeltaSeconds
from Script.Engine import Conv_InterfaceToObject
from Script.NavigationSystem import FindPathToLocationSynchronously
from Script.NavigationSystem import NavigationPath
from Script.Engine import Actor
from Script.Engine import K2_GetActorLocation
from Script.AIModule import SetBlackboardValueAsVector
from Script.AIModule import SetBlackboardValueAsObject
from Game.FactoryGame.Character.Creature.Enemy.BP_EnemyController import BP_EnemyController

class BTS_FindTarget(BTService_BlueprintBase):
    mFinalGoalBBKey: BlackboardKeySelector
    mClosestDistance: float
    mTargetLocationBBKey: BlackboardKeySelector
    mNeedFullPath: bool = True
    mHasPathBBKey: BlackboardKeySelector
    mNavFilter: TSubclassOf[NavigationQueryFilter] = NewObject[NavQuery_WalkingAI]()
    mSecondaryCheck: bool
    mCurrentlyHasPath: bool
    mDoubleCheckDelay: float = 1.5
    
    def ReceiveTickAI(self):
        ExecuteUbergraph_BTS_FindTarget.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_FindTarget.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_FindTarget.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTS_FindTarget(123)
    

    def ExecuteUbergraph_BTS_FindTarget(self):
        goto(ComputedJump("EntryPoint"))
        if not self.mCurrentlyHasPath:
            goto('L30')
        goto(ExecutionFlow.Pop())
        # Label 30
        self.mSecondaryCheck = True
        goto(ExecutionFlow.Pop())
        # Label 42
        Default__KismetSystemLibrary.Delay(self, self.mDoubleCheckDelay, LatentActionInfo(Linkage = 15, UUID = -468791157, ExecutionFunction = "ExecuteUbergraph_BTS_FindTarget", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        Controller: Ptr[BP_EnemyController] = Cast[BP_EnemyController](OwnerController)
        bSuccess: bool = Controller
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        
        Controller.mCurrentAggroTarget = None
        ReturnValue: Ptr[Object] = Default__KismetSystemLibrary.Conv_InterfaceToObject(Ref[Controller.mCurrentAggroTarget])
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L1093')
        ReturnValue_1: Ptr[Actor] = GetInterfaceUObject(Controller.mCurrentAggroTarget).GetActor()
        
        Default__BTFunctionLibrary.SetBlackboardValueAsObject(self, ReturnValue_1, Ref[self.mFinalGoalBBKey])
        ReturnValue_2: Vector = ControlledPawn.K2_GetActorLocation()
        ReturnValue2: Vector = ReturnValue_1.K2_GetActorLocation()
        
        ReturnValue_3: Ptr[NavigationPath] = Default__NavigationSystemV1.FindPathToLocationSynchronously(ReturnValue_1, Controller, self.mNavFilter, Ref[ReturnValue_2], Ref[ReturnValue2])
        ReturnValue_4: float = ReturnValue_3.GetPathLength()
        ReturnValue_5: bool = ReturnValue_3.IsPartial()
        ReturnValue_6: bool = ReturnValue_4 <= 0
        ReturnValue_7: bool = ReturnValue_5 and self.mNeedFullPath
        ReturnValue_8: bool = BooleanOR(ReturnValue_7, ReturnValue_6)
        if not ReturnValue_8:
            goto('L1180')
        self.mCurrentlyHasPath = False
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](ReturnValue_1)
        bSuccess1: bool = Player
        ReturnValue_9: bool = Not_PreBool(Player.bWasJumping)
        ReturnValue1: bool = self.mSecondaryCheck and ReturnValue_9
        if not ReturnValue1:
            goto('L42')
        self.mSecondaryCheck = False
        
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, False, Ref[self.mHasPathBBKey])
        goto(ExecutionFlow.Pop())
        
        # Label 1093
        Default__BTFunctionLibrary.SetBlackboardValueAsObject(self, None, Ref[self.mFinalGoalBBKey])
        
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, False, Ref[self.mHasPathBBKey])
        goto(ExecutionFlow.Pop())
        # Label 1180
        self.mCurrentlyHasPath = True
        
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, True, Ref[self.mHasPathBBKey])
        ReturnValue1_0: Vector = ReturnValue_1.K2_GetActorLocation()
        
        Default__BTFunctionLibrary.SetBlackboardValueAsVector(self, ReturnValue1_0, Ref[self.mTargetLocationBBKey])
        goto(ExecutionFlow.Pop())
    
