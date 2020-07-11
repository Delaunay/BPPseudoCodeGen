
from codegen.ue4_stub import *

from Script.FactoryGame import FGFoliageRemovalSubsystem
from Script.FactoryGame import Default__FGFoliageRemovalSubsystem
from Script.Engine import K2_GetActorLocation
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.BP_NFBHideableFoliage import BP_NFBHideableFoliage
from Script.AIModule import Default__BTFunctionLibrary
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTS_CheckForFoliage import ExecuteUbergraph_BTS_CheckForFoliage.K2Node_Event_ControlledPawn
from Script.AIModule import SetBlackboardValueAsBool
from Script.CoreUObject import Vector
from Script.AIModule import BlackboardKeySelector
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTS_CheckForFoliage import ExecuteUbergraph_BTS_CheckForFoliage.K2Node_Event_OwnerController
from Script.FactoryGame import GetClosestFoliage
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTS_CheckForFoliage import ExecuteUbergraph_BTS_CheckForFoliage
from Script.AIModule import BTService_BlueprintBase
from Script.FactoryGame import GetFoliageRemovalSubsystem
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BTS_CheckForFoliage import ExecuteUbergraph_BTS_CheckForFoliage.K2Node_Event_DeltaSeconds

class BTS_CheckForFoliage(BTService_BlueprintBase):
    mHasFoliageNearbyBBKey: BlackboardKeySelector
    
    def ReceiveTickAI(self):
        ExecuteUbergraph_BTS_CheckForFoliage.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_CheckForFoliage.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_CheckForFoliage.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTS_CheckForFoliage(10)
    

    def ExecuteUbergraph_BTS_CheckForFoliage(self):
        ReturnValue: Ptr[FGFoliageRemovalSubsystem] = Default__FGFoliageRemovalSubsystem.GetFoliageRemovalSubsystem(ControlledPawn)
        ReturnValue_0: Vector = ControlledPawn.K2_GetActorLocation()
        
        component = None
        instanceId = None
        instanceLocation = None
        ReturnValue_1: bool = ReturnValue.GetClosestFoliage(120, BP_NFBHideableFoliage, False, Ref[ReturnValue_0], Ref[component], Ref[instanceId], Ref[instanceLocation])
        
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, ReturnValue_1, Ref[self.mHasFoliageNearbyBBKey])
    
