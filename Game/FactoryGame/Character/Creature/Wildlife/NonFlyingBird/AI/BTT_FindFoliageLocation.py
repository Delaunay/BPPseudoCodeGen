
from codegen.ue4_stub import *

from Script.FactoryGame import Default__FGFoliageRemovalSubsystem
from Script.FactoryGame import GetClosestFoliage
from Script.NavigationSystem import Default__NavigationSystemV1
from Script.NavigationSystem import K2_GetRandomPointInNavigableRadius
from Script.FactoryGame import GetFoliageRemovalSubsystem
from Script.AIModule import GetBlackboardValueAsBool
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTT_FindFoliageLocation import ExecuteUbergraph_BTT_FindFoliageLocation.K2Node_Event_ControlledPawn
from Script.FactoryGame import FGFoliageRemovalSubsystem
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.BP_NFBHideableFoliage import BP_NFBHideableFoliage
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import FinishExecute
from Script.AIModule import BlackboardKeySelector
from Script.Engine import SelectVector
from Script.AIModule import BTTask_BlueprintBase
from Script.CoreUObject import Vector
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTT_FindFoliageLocation import ExecuteUbergraph_BTT_FindFoliageLocation
from Script.Engine import K2_GetActorLocation
from Script.AIModule import SetBlackboardValueAsVector
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTT_FindFoliageLocation import ExecuteUbergraph_BTT_FindFoliageLocation.K2Node_Event_OwnerController

class BTT_FindFoliageLocation(BTTask_BlueprintBase):
    mTargetLocationBBKey: BlackboardKeySelector
    mUseOwnLocation: bool
    mRadius: float = 6000
    mWasUncoveredBBKey: BlackboardKeySelector
    
    def ReceiveExecuteAI(self):
        ExecuteUbergraph_BTT_FindFoliageLocation.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTT_FindFoliageLocation.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTT_FindFoliageLocation(10)
    

    def ExecuteUbergraph_BTT_FindFoliageLocation(self):
        
        ReturnValue: bool = Default__BTFunctionLibrary.GetBlackboardValueAsBool(self, Ref[self.mWasUncoveredBBKey])
        self.mUseOwnLocation = ReturnValue
        ReturnValue_0: Vector = ControlledPawn.K2_GetActorLocation()
        ReturnValue_1: Ptr[FGFoliageRemovalSubsystem] = Default__FGFoliageRemovalSubsystem.GetFoliageRemovalSubsystem(ControlledPawn)
        
        RandomLocation = None
        ReturnValue_2: bool = Default__NavigationSystemV1.K2_GetRandomPointInNavigableRadius(self, self.mRadius, None, None, Ref[ReturnValue_0], Ref[RandomLocation])
        ReturnValue_3: Vector = SelectVector(ReturnValue_0, RandomLocation, self.mUseOwnLocation)
        
        component = None
        instanceId = None
        instanceLocation = None
        ReturnValue_4: bool = ReturnValue_1.GetClosestFoliage(5000, BP_NFBHideableFoliage, False, Ref[ReturnValue_3], Ref[component], Ref[instanceId], Ref[instanceLocation])
        if not ReturnValue_4:
            goto('L483')
        
        Default__BTFunctionLibrary.SetBlackboardValueAsVector(self, instanceLocation, Ref[self.mTargetLocationBBKey])
        self.FinishExecute(True)
        # End
        # Label 483
        self.FinishExecute(False)
    
