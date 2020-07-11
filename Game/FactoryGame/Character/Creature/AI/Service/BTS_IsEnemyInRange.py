
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.AI.Service.BTS_IsEnemyInRange import ExecuteUbergraph_BTS_IsEnemyInRange.K2Node_Event_DeltaSeconds
from Script.Engine import Pawn
from Script.FactoryGame import FGAttack
from Script.FactoryGame import GetAttackActivationDistance
from Script.AIModule import GetBlackboardValueAsObject
from Script.AIModule import BTService_BlueprintBase
from Script.FactoryGame import FGAggroTargetInterface
from Script.FactoryGame import FGEnemyController
from Script.Engine import K2_GetPawn
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import BlackboardKeySelector
from Script.CoreUObject import Object
from Script.FactoryGame import IsWithinRange
from Script.AIModule import SetBlackboardValueAsBool
from Script.FactoryGame import Default__FGAttack
from Script.FactoryGame import Default__FGCombatFunctionLibrary
from Game.FactoryGame.Character.Creature.AI.Service.BTS_IsEnemyInRange import ExecuteUbergraph_BTS_IsEnemyInRange.K2Node_Event_OwnerActor
from Game.FactoryGame.Character.Creature.AI.Service.BTS_IsEnemyInRange import ExecuteUbergraph_BTS_IsEnemyInRange
from Game.FactoryGame.Character.Creature.AI.Service.BTS_IsEnemyInRange import ExecuteUbergraph_BTS_IsEnemyInRange.K2Node_Event_ControlledPawn
from Game.FactoryGame.Character.Creature.AI.Service.BTS_IsEnemyInRange import ExecuteUbergraph_BTS_IsEnemyInRange.K2Node_Event_OwnerController

class BTS_IsEnemyInRange(BTService_BlueprintBase):
    mEnemyBBKey: BlackboardKeySelector
    mIsInRangeBBKey: BlackboardKeySelector
    mAIController: Ptr[FGEnemyController]
    mAttackClass: TSubclassOf[FGAttack]
    
    def ReceiveTick(self):
        ExecuteUbergraph_BTS_IsEnemyInRange.K2Node_Event_OwnerActor = OwnerActor #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_IsEnemyInRange.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTS_IsEnemyInRange(10)
    

    def ReceiveActivationAI(self):
        ExecuteUbergraph_BTS_IsEnemyInRange.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_IsEnemyInRange.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTS_IsEnemyInRange(625)
    

    def ExecuteUbergraph_BTS_IsEnemyInRange(self):
        Controller: Ptr[FGEnemyController] = Cast[FGEnemyController](OwnerActor)
        bSuccess: bool = Controller
        if not bSuccess:
            goto('L728')
        self.mAIController = Controller
        
        # Label 108
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, False, Ref[self.mIsInRangeBBKey])
        
        ReturnValue: Ptr[Object] = Default__BTFunctionLibrary.GetBlackboardValueAsObject(self, Ref[self.mEnemyBBKey])
        Interface: TScriptInterface[FGAggroTargetInterface] = QueryInterface[FGAggroTargetInterface](ReturnValue)
        bSuccess2: bool = Interface
        if not bSuccess2:
            goto('L728')
        ReturnValue_0: float = Default__FGAttack.GetAttackActivationDistance(self.mAttackClass)
        ReturnValue_1: Ptr[Pawn] = self.mAIController.K2_GetPawn()
        
        ReturnValue = Default__BTFunctionLibrary.GetBlackboardValueAsObject(self, Ref[self.mEnemyBBKey])
        Interface = QueryInterface[FGAggroTargetInterface](ReturnValue)
        bSuccess2 = Interface
        ReturnValue_2: bool = Default__FGCombatFunctionLibrary.IsWithinRange(ReturnValue_1, Interface, ReturnValue_0)
        
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, ReturnValue_2, Ref[self.mIsInRangeBBKey])
        # End
        Controller1: Ptr[FGEnemyController] = Cast[FGEnemyController](OwnerController)
        bSuccess1: bool = Controller1
        if not bSuccess1:
            goto('L728')
        self.mAIController = Controller1
        goto('L108')
    
