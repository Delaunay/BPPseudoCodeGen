
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.Enemy.Hog.AI.BTS_CheckNearbyThreats import ExecuteUbergraph_BTS_CheckNearbyThreats
from Script.Engine import NotEqual_BoolBool
from Game.FactoryGame.Character.Creature.Enemy.Hog.AI.BTS_CheckNearbyThreats import ExecuteUbergraph_BTS_CheckNearbyThreats.K2Node_Event_DeltaSeconds
from Game.FactoryGame.Character.Creature.Enemy.Hog.Controller_HogCharge import Controller_HogCharge
from Script.FactoryGame import GetTargetingDesire
from Script.AIModule import BTService_BlueprintBase
from Script.FactoryGame import FGAggroTargetInterface
from Script.Engine import Default__KismetSystemLibrary
from Script.AIModule import Default__BTFunctionLibrary
from Script.AIModule import BlackboardKeySelector
from Script.CoreUObject import Object
from Game.FactoryGame.Character.Creature.Enemy.Hog.Char_Hog import Char_Hog
from Script.Engine import FlushNetDormancy
from Script.AIModule import SetBlackboardValueAsBool
from Script.Engine import Conv_InterfaceToObject
from Script.FactoryGame import GetMostDesirableAggroTarget
from Game.FactoryGame.Character.Creature.Enemy.Hog.AI.BTS_CheckNearbyThreats import ExecuteUbergraph_BTS_CheckNearbyThreats.K2Node_Event_ControlledPawn
from Script.AIModule import SetBlackboardValueAsObject
from Game.FactoryGame.Character.Creature.Enemy.Hog.AI.BTS_CheckNearbyThreats import ExecuteUbergraph_BTS_CheckNearbyThreats.K2Node_Event_OwnerController

class BTS_CheckNearbyThreats(BTService_BlueprintBase):
    ThreatNearbyBBkey: BlackboardKeySelector
    NearbyActorBBKey: BlackboardKeySelector
    localHogPawn: Ptr[Char_Hog]
    
    def ReceiveTickAI(self):
        ExecuteUbergraph_BTS_CheckNearbyThreats.K2Node_Event_OwnerController = OwnerController #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_CheckNearbyThreats.K2Node_Event_ControlledPawn = ControlledPawn #  PERSISTENT_FRAME(
        ExecuteUbergraph_BTS_CheckNearbyThreats.K2Node_Event_DeltaSeconds = DeltaSeconds #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BTS_CheckNearbyThreats(10)
    

    def ExecuteUbergraph_BTS_CheckNearbyThreats(self):
        Hog: Ptr[Char_Hog] = Cast[Char_Hog](ControlledPawn)
        bSuccess: bool = Hog
        if not bSuccess:
            goto('L784')
        self.localHogPawn = Hog
        Charge: Ptr[Controller_HogCharge] = Cast[Controller_HogCharge](OwnerController)
        bSuccess1: bool = Charge
        if not bSuccess1:
            goto('L784')
        ReturnValue: TScriptInterface[FGAggroTargetInterface] = Charge.GetMostDesirableAggroTarget()
        ReturnValue_0: float = Charge.GetTargetingDesire(ReturnValue)
        ReturnValue_1: bool = ReturnValue_0 > 0.699999988079071
        
        Default__BTFunctionLibrary.SetBlackboardValueAsBool(self, ReturnValue_1, Ref[self.ThreatNearbyBBkey])
        ReturnValue = Charge.GetMostDesirableAggroTarget()
        
        ReturnValue_2: Ptr[Object] = Default__KismetSystemLibrary.Conv_InterfaceToObject(Ref[ReturnValue])
        
        Default__BTFunctionLibrary.SetBlackboardValueAsObject(self, ReturnValue_2, Ref[self.NearbyActorBBKey])
        ReturnValue_1 = ReturnValue_0 > 0.699999988079071
        ReturnValue_3: bool = NotEqual_BoolBool(ReturnValue_1, self.localHogPawn.mIsThreatened)
        if not ReturnValue_3:
            goto('L784')
        self.localHogPawn.FlushNetDormancy()
        ReturnValue_1 = ReturnValue_0 > 0.699999988079071
        self.localHogPawn.mIsThreatened = ReturnValue_1
        self.localHogPawn.OnRep_mIsThreatened()
    
