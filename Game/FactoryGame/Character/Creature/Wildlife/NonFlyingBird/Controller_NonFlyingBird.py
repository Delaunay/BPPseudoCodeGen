
from codegen.ue4_stub import *

from Script.AIModule import GetValueAsBool
from Script.AIModule import BlackboardComponent
from Script.Engine import Delay
from Script.FactoryGame import StartPanic
from Script.Engine import Pawn
from Script.AIModule import SetValueAsBool
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BT_NonFlyingBird import BT_NonFlyingBird
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.AIModule import UseBlackboard
from Script.Engine import K2_GetPawn
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Controller_NonFlyingBird import ExecuteUbergraph_Controller_NonFlyingBird
from Script.AIModule import Default__AIBlueprintHelperLibrary
from Script.Engine import IsValid
from Script.Engine import EqualEqual_NameName
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Char_NonFlyingBird import Char_NonFlyingBird
from Script.Engine import BooleanOR
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Controller_NonFlyingBird import ExecuteUbergraph_Controller_NonFlyingBird.K2Node_Event_PossessedPawn
from Script.AIModule import GetBlackboard
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Controller_NonFlyingBird import ExecuteUbergraph_Controller_NonFlyingBird.K2Node_ComponentBoundEvent_Stimulus
from Script.FactoryGame import FGCreatureController
from Script.Engine import ReceivePossess
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.AI.BB_NonFlyingBird import BB_NonFlyingBird
from Game.FactoryGame.Character.Creature.Wildlife.NonFlyingBird.Controller_NonFlyingBird import ExecuteUbergraph_Controller_NonFlyingBird.K2Node_ComponentBoundEvent_Actor

class Controller_NonFlyingBird(FGCreatureController):
    mPanicBBKeyName: FName = DoPanic
    mIsLuringBBKey: FName = isLuring
    PathFollowingComponent = Namespace(ObjectClass='/Script/AIModule.PathFollowingComponent', ObjectFlags=2883617, ObjectName='PathFollowingComponent')
    PerceptionComponent = Namespace(ObjectClass='/Script/AIModule.AIPerceptionComponent', ObjectFlags=2883617, ObjectName='PerceptionComponent', OnTargetPerceptionUpdated=0, SensesConfig=[{'$ObjectClass': '/Script/AIModule.AISenseConfig_Sight', '$ObjectFlags': 2621481, '$ObjectName': 'AISenseConfig_Sight_0', 'PeripheralVisionAngleDegrees': 180}, {'$ObjectClass': '/Script/AIModule.AISenseConfig_Hearing', '$ObjectFlags': 2621481, '$ObjectName': 'AISenseConfig_Hearing_0', 'MaxAge': 2}])
    ActionsComp = Namespace(ObjectClass='/Script/AIModule.PawnActionsComponent', ObjectFlags=2883617, ObjectName='ActionsComp')
    TransformComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    
    def ReceivePossess(self):
        ExecuteUbergraph_Controller_NonFlyingBird.K2Node_Event_PossessedPawn = PossessedPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Controller_NonFlyingBird(87)
    

    def TryToJump(self):
        self.ExecuteUbergraph_Controller_NonFlyingBird(183)
    

    def BndEvt__PerceptionComponent_K2Node_ComponentBoundEvent_0_ActorPerceptionUpdatedDelegate__DelegateSignature(self, Actor: Ptr[Actor], Stimulus: AIStimulus):
        ExecuteUbergraph_Controller_NonFlyingBird.K2Node_ComponentBoundEvent_Actor = Actor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Controller_NonFlyingBird.K2Node_ComponentBoundEvent_Stimulus = Stimulus #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Controller_NonFlyingBird(315)
    

    def StartPanic(self):
        self.ExecuteUbergraph_Controller_NonFlyingBird(768)
    

    def ExecuteUbergraph_Controller_NonFlyingBird(self):
        goto(ComputedJump("EntryPoint"))
        
        BlackboardComponent = None
        ReturnValue: bool = self.UseBlackboard(BB_NonFlyingBird, Ref[BlackboardComponent])
        ReturnValue_0: bool = self.RunBehaviorTree(BT_NonFlyingBird)
        goto(ExecutionFlow.Pop())
        self.ReceivePossess(PossessedPawn)
        Default__KismetSystemLibrary.Delay(self, 3, LatentActionInfo(Linkage = 15, UUID = -439682924, ExecutionFunction = "ExecuteUbergraph_Controller_NonFlyingBird", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue_1: Ptr[Pawn] = self.K2_GetPawn()
        Bird: Ptr[Char_NonFlyingBird] = Cast[Char_NonFlyingBird](ReturnValue_1)
        bSuccess: bool = Bird
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Bird.TryToJump()
        goto(ExecutionFlow.Pop())
        ReturnValue_2: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        ReturnValue_3: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_2)
        ReturnValue_4: bool = EqualEqual_NameName(Stimulus.Tag, "WeaponFire")
        ReturnValue1: bool = EqualEqual_NameName(Stimulus.Tag, "PlayerSprinting")
        ReturnValue_5: bool = BooleanOR(ReturnValue1, ReturnValue_4)
        ReturnValue_6: bool = Stimulus.bSuccessfullySensed and ReturnValue_5
        ReturnValue1_0: bool = ReturnValue_6 and ReturnValue_3
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        ReturnValue2: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue_7: bool = ReturnValue2.GetValueAsBool(Ref[self.mIsLuringBBKey])
        if not ReturnValue_7:
            goto('L753')
        goto(ExecutionFlow.Pop())
        # Label 753
        self.StartPanic()
        goto(ExecutionFlow.Pop())
        self.StartPanic()
        ReturnValue1_1: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue1_1.SetValueAsBool(True, Ref[self.mPanicBBKeyName])
        goto(ExecutionFlow.Pop())
    
