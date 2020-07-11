
from codegen.ue4_stub import *

from Script.AIModule import GetValueAsBool
from Script.AIModule import BlackboardComponent
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Controller_SpaceGiraffe import ExecuteUbergraph_Controller_SpaceGiraffe.K2Node_ComponentBoundEvent_Actor
from Script.Engine import Delay
from Script.FactoryGame import StartPanic
from Script.Engine import Pawn
from Script.AIModule import SetValueAsBool
from Script.Engine import ReceiveBeginPlay
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Controller_SpaceGiraffe import ExecuteUbergraph_Controller_SpaceGiraffe.K2Node_ComponentBoundEvent_Stimulus
from Script.AIModule import SetValueAsFloat
from Script.Engine import Default__KismetSystemLibrary
from Script.AIModule import UseBlackboard
from Script.Engine import K2_GetPawn
from Script.AIModule import Default__AIBlueprintHelperLibrary
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.BT_SpaceGiraffe import BT_SpaceGiraffe
from Script.Engine import EqualEqual_NameName
from Script.FactoryGame import StopPanic
from Script.Engine import FlushNetDormancy
from Script.AIModule import GetBlackboard
from Script.FactoryGame import FGCreatureController
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.BB_SpaceGiraffe import BB_SpaceGiraffe
from Script.Engine import ReceivePossess
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Controller_SpaceGiraffe import ExecuteUbergraph_Controller_SpaceGiraffe.K2Node_Event_PossessedPawn
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Controller_SpaceGiraffe import ExecuteUbergraph_Controller_SpaceGiraffe
from Game.FactoryGame.Character.Creature.Wildlife.SpaceGiraffe.Char_SpaceGiraffe import Char_SpaceGiraffe

class Controller_SpaceGiraffe(FGCreatureController):
    mMaxRotationAngle: float = 240
    mMaxRotationAngleBBKeyName: FName = MaxRotation
    mPanicBBKeyName: FName = DoPanic
    mDebugDoSpecifiedRotation: bool
    mDebugRotation: float = 120
    mDoDebugRotationBBkeyName: FName = DoDebugRotation
    mDebugRotationBBkeyName: FName = DebugRotation
    PathFollowingComponent = Namespace(ObjectClass='/Script/AIModule.PathFollowingComponent', ObjectFlags=2883617, ObjectName='PathFollowingComponent')
    PerceptionComponent = Namespace(ObjectClass='/Script/AIModule.AIPerceptionComponent', ObjectFlags=2883617, ObjectName='PerceptionComponent', OnTargetPerceptionUpdated=0, SensesConfig=[{'$ObjectClass': '/Script/AIModule.AISenseConfig_Sight', '$ObjectFlags': 2621481, '$ObjectName': 'AISenseConfig_Sight_0'}, {'$ObjectClass': '/Script/AIModule.AISenseConfig_Hearing', '$ObjectFlags': 2621481, '$ObjectName': 'AISenseConfig_Hearing_0'}])
    ActionsComp = Namespace(ObjectClass='/Script/AIModule.PawnActionsComponent', ObjectFlags=2883617, ObjectName='ActionsComp')
    TransformComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    
    def ReceivePossess(self):
        ExecuteUbergraph_Controller_SpaceGiraffe.K2Node_Event_PossessedPawn = PossessedPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Controller_SpaceGiraffe(323)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_Controller_SpaceGiraffe(419)
    

    def StartPanic(self):
        self.ExecuteUbergraph_Controller_SpaceGiraffe(430)
    

    def StopPanic(self):
        self.ExecuteUbergraph_Controller_SpaceGiraffe(831)
    

    def BndEvt__PerceptionComponent_K2Node_ComponentBoundEvent_2_ActorPerceptionUpdatedDelegate__DelegateSignature(self, Actor: Ptr[Actor], Stimulus: AIStimulus):
        ExecuteUbergraph_Controller_SpaceGiraffe.K2Node_ComponentBoundEvent_Actor = Actor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Controller_SpaceGiraffe.K2Node_ComponentBoundEvent_Stimulus = Stimulus #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Controller_SpaceGiraffe(1053)
    

    def ExecuteUbergraph_Controller_SpaceGiraffe(self):
        goto(ComputedJump("EntryPoint"))
        
        BlackboardComponent = None
        ReturnValue: bool = self.UseBlackboard(BB_SpaceGiraffe, Ref[BlackboardComponent])
        
        BlackboardComponent.SetValueAsFloat(self.mMaxRotationAngle, Ref[self.mMaxRotationAngleBBKeyName])
        ReturnValue2: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue2.SetValueAsBool(self.mDebugDoSpecifiedRotation, Ref[self.mDoDebugRotationBBkeyName])
        ReturnValue3: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue3.SetValueAsFloat(self.mDebugRotation, Ref[self.mDebugRotationBBkeyName])
        ReturnValue_0: bool = self.RunBehaviorTree(BT_SpaceGiraffe)
        goto(ExecutionFlow.Pop())
        self.ReceivePossess(PossessedPawn)
        Default__KismetSystemLibrary.Delay(self, 2, LatentActionInfo(Linkage = 15, UUID = -219522627, ExecutionFunction = "ExecuteUbergraph_Controller_SpaceGiraffe", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        self.ReceiveBeginPlay()
        goto(ExecutionFlow.Pop())
        self.StartPanic()
        ReturnValue1: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue_1: bool = ReturnValue1.GetValueAsBool(Ref[self.mPanicBBKeyName])
        if not ReturnValue_1:
            goto('L549')
        goto(ExecutionFlow.Pop())
        # Label 549
        ReturnValue_2: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue_2.SetValueAsBool(True, Ref[self.mPanicBBKeyName])
        ReturnValue_3: Ptr[Pawn] = self.K2_GetPawn()
        Giraffe: Ptr[Char_SpaceGiraffe] = Cast[Char_SpaceGiraffe](ReturnValue_3)
        bSuccess: bool = Giraffe
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        Giraffe.FlushNetDormancy()
        Giraffe.mDoPanic = True
        Giraffe.OnRep_mDoPanic()
        goto(ExecutionFlow.Pop())
        self.StopPanic()
        ReturnValue1_0: Ptr[Pawn] = self.K2_GetPawn()
        Giraffe1: Ptr[Char_SpaceGiraffe] = Cast[Char_SpaceGiraffe](ReturnValue1_0)
        bSuccess1: bool = Giraffe1
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        Giraffe1.FlushNetDormancy()
        Giraffe1.mDoPanic = False
        Giraffe1.OnRep_mDoPanic()
        goto(ExecutionFlow.Pop())
        # Label 1038
        self.StartPanic()
        goto(ExecutionFlow.Pop())
        ReturnValue_4: bool = EqualEqual_NameName(Stimulus.Tag, "WeaponFire")
        ReturnValue_5: bool = Stimulus.bSuccessfullySensed and ReturnValue_4
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        goto('L1038')
    
