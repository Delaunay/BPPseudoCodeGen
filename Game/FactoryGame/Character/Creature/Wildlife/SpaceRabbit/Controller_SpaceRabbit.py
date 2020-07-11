
from codegen.ue4_stub import *

from Script.AIModule import SetValueAsVector
from Script.AIModule import BlackboardComponent
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Controller_SpaceRabbit import ExecuteUbergraph_Controller_SpaceRabbit.K2Node_Event_PossessedPawn
from Script.FactoryGame import FGCharacterPlayer
from Script.Engine import Pawn
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Char_SpaceRabbit import Char_SpaceRabbit
from Script.AIModule import SetValueAsBool
from Script.AIModule import SetValueAsFloat
from Script.Engine import Default__KismetSystemLibrary
from Script.AIModule import GetCurrentlyPerceivedActors
from Script.AIModule import AIPerceptionComponent
from Script.Engine import Array_Find
from Script.AIModule import UseBlackboard
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import K2_GetPawn
from Script.AIModule import Default__AIBlueprintHelperLibrary
from Script.Engine import IsValid
from Script.Engine import EqualEqual_NameName
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.AI.BB_SpaceRabbit import BB_SpaceRabbit
from Script.Engine import FlushNetDormancy
from Script.AIModule import AISense_Sight
from Script.AIModule import GetBlackboard
from Script.CoreUObject import Vector
from Script.Engine import EqualEqual_ObjectObject
from Script.AIModule import GetAIPerceptionComponent
from Script.FactoryGame import FGCreatureController
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Controller_SpaceRabbit import ExecuteUbergraph_Controller_SpaceRabbit.K2Node_ComponentBoundEvent_Stimulus
from Script.Engine import Actor
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Controller_SpaceRabbit import ExecuteUbergraph_Controller_SpaceRabbit.K2Node_ComponentBoundEvent_Actor
from Script.Engine import K2_GetActorLocation
from Script.Engine import ReceivePossess
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.AI.BT_SpaceRabbit import BT_SpaceRabbit
from Script.AIModule import SetValueAsObject
from Game.FactoryGame.Character.Creature.Wildlife.SpaceRabbit.Controller_SpaceRabbit import ExecuteUbergraph_Controller_SpaceRabbit

class Controller_SpaceRabbit(FGCreatureController):
    mPotentialThreat: Ptr[FGCharacterPlayer]
    mSneakLimit: float = -0.800000011920929
    mSneakLimitBBKeyName: FName = SneakLimit
    mThreatTags: List[FName] = ['WeaponFire', 'PlayerSprinting']
    mIsCuriousBBKeyName: FName = IsCurious
    mPersonalDistance: float = 1500
    mPersonalDistanceBBKeyName: FName = PersonalDistance
    mPanicBBKeyName: FName = DoPanic
    mFriendBBKeyName: FName = friend
    PathFollowingComponent = Namespace(ObjectClass='/Script/AIModule.PathFollowingComponent', ObjectFlags=2883617, ObjectName='PathFollowingComponent')
    PerceptionComponent = Namespace(ObjectClass='/Script/AIModule.AIPerceptionComponent', ObjectFlags=2883617, ObjectName='PerceptionComponent', OnTargetPerceptionUpdated=0, SensesConfig=[{'$ObjectClass': '/Script/AIModule.AISenseConfig_Sight', '$ObjectFlags': 2621481, '$ObjectName': 'AISenseConfig_Sight_0', 'LoseSightRadius': 3000, 'PeripheralVisionAngleDegrees': 120}, {'$ObjectClass': '/Script/AIModule.AISenseConfig_Hearing', '$ObjectFlags': 2621481, '$ObjectName': 'AISenseConfig_Hearing_0', 'MaxAge': 2}])
    ActionsComp = Namespace(ObjectClass='/Script/AIModule.PawnActionsComponent', ObjectFlags=2883617, ObjectName='ActionsComp')
    TransformComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    
    def isThreat(self, inTag: FName):
        
        ReturnValue: int32 = Default__KismetArrayLibrary.Array_Find(Ref[self.mThreatTags], Ref[inTag])
        ReturnValue_0: bool = ReturnValue > -1
        isThreat = ReturnValue_0
    

    def ReactToSound(self, InActor: Ptr[Actor], soundLocation: Vector, Tag: FName):
        PanicBBKeyName = "DoPanic"
        mItemBBKeyName = "FetchItem"
        
        isThreat = None
        self.isThreat(Tag, Ref[isThreat])
        if not isThreat:
            goto('L138')
        self.StartPanic()
        didReact = True
        # End
        # Label 138
        ReturnValue: bool = EqualEqual_NameName(Tag, "Bone")
        if not ReturnValue:
            goto('L303')
        ReturnValue_0: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue_0.SetValueAsObject(InActor, Ref[mItemBBKeyName])
        didReact = True
        # End
        # Label 303
        didReact = False
    

    def SetNewThreat(self, newThreat: Ptr[FGCharacterPlayer]):
        threatBBKeyName = "Threat"
        threatLocationBBKeyName = "ThreatLocation"
        self.mPotentialThreat = newThreat
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mPotentialThreat)
        if not ReturnValue:
            goto('L223')
        ReturnValue_0: Vector = self.mPotentialThreat.K2_GetActorLocation()
        ThreatLocation = ReturnValue_0
        # Label 223
        ReturnValue1: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue1.SetValueAsObject(self.mPotentialThreat, Ref[threatBBKeyName])
        ReturnValue_1: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue_1.SetValueAsVector(ThreatLocation, Ref[threatLocationBBKeyName])
        ReturnValue_2: Ptr[Pawn] = self.K2_GetPawn()
        Rabbit: Ptr[Char_SpaceRabbit] = Cast[Char_SpaceRabbit](ReturnValue_2)
        bSuccess: bool = Rabbit
        if not bSuccess:
            goto('L581')
        Rabbit.FlushNetDormancy()
        Rabbit.mPotentialThreat = self.mPotentialThreat
    

    def GetCurrentThreat(self):
        outThreat = self.mPotentialThreat
    

    def ReceivePossess(self):
        ExecuteUbergraph_Controller_SpaceRabbit.K2Node_Event_PossessedPawn = PossessedPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Controller_SpaceRabbit(1602)
    

    def BndEvt__PerceptionComponent_K2Node_ComponentBoundEvent_0_ActorPerceptionUpdatedDelegate__DelegateSignature(self, Actor: Ptr[Actor], Stimulus: AIStimulus):
        ExecuteUbergraph_Controller_SpaceRabbit.K2Node_ComponentBoundEvent_Actor = Actor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Controller_SpaceRabbit.K2Node_ComponentBoundEvent_Stimulus = Stimulus #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Controller_SpaceRabbit(559)
    

    def StartPanic(self):
        self.ExecuteUbergraph_Controller_SpaceRabbit(1626)
    

    def ExecuteUbergraph_Controller_SpaceRabbit(self):
        # Label 10
        ReturnValue: bool = self.RunBehaviorTree(BT_SpaceRabbit)
        
        outThreat2 = None
        self.GetCurrentThreat(Ref[outThreat2])
        self.SetNewThreat(outThreat2)
        ReturnValue_0: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue_0.SetValueAsFloat(self.mSneakLimit, Ref[self.mSneakLimitBBKeyName])
        ReturnValue_0 = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue_0.SetValueAsBool(True, Ref[self.mIsCuriousBBKeyName])
        ReturnValue1: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue1.SetValueAsFloat(self.mPersonalDistance, Ref[self.mPersonalDistanceBBKeyName])
        Rabbit: Ptr[Char_SpaceRabbit] = Cast[Char_SpaceRabbit](PossessedPawn)
        bSuccess2: bool = Rabbit
        if not bSuccess2:
            goto('L1711')
        ReturnValue3: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue3.SetValueAsObject(Rabbit.mFriendActor, Ref[self.mFriendBBKeyName])
        # End
        if not Stimulus.bSuccessfullySensed:
            goto('L669')
        
        didReact = None
        self.ReactToSound(Actor, Stimulus.StimulusLocation, Stimulus.Tag, Ref[didReact])
        if not didReact:
            goto('L669')
        # End
        # Label 669
        if not Stimulus.bSuccessfullySensed:
            goto('L785')
        
        outThreat1 = None
        self.GetCurrentThreat(Ref[outThreat1])
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(outThreat1)
        if not ReturnValue_1:
            goto('L968')
        # End
        
        outThreat = None
        # Label 785
        self.GetCurrentThreat(Ref[outThreat])
        ReturnValue1_0: bool = Default__KismetSystemLibrary.IsValid(outThreat)
        if not ReturnValue1_0:
            goto('L1711')
        
        outThreat = None
        self.GetCurrentThreat(Ref[outThreat])
        ReturnValue_2: bool = EqualEqual_ObjectObject(Actor, outThreat)
        if not ReturnValue_2:
            goto('L1711')
        self.SetNewThreat(None)
        # End
        # Label 968
        Player1: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](Actor)
        bSuccess1: bool = Player1
        if not bSuccess1:
            goto('L1711')
        ReturnValue_3: Ptr[AIPerceptionComponent] = self.GetAIPerceptionComponent()
        OutActors: List[Ptr[Actor]] = []
        
        ReturnValue_3.GetCurrentlyPerceivedActors(AISense_Sight, Ref[OutActors])
        
        Actor = None
        ReturnValue_4: int32 = Default__KismetArrayLibrary.Array_Find(Ref[OutActors], Ref[Actor])
        ReturnValue_5: bool = ReturnValue_4 != -1
        if not ReturnValue_5:
            goto('L1711')
        ReturnValue_3 = self.GetAIPerceptionComponent()
        OutActors = []
        
        ReturnValue_3.GetCurrentlyPerceivedActors(AISense_Sight, Ref[OutActors])
        
        Actor = None
        ReturnValue_4 = Default__KismetArrayLibrary.Array_Find(Ref[OutActors], Ref[Actor])
        
        Item = None
        Item = OutActors[ReturnValue_4]
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](Item)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L1711')
        self.SetNewThreat(Player)
        # End
        
        BlackboardComponent = None
        # Label 1559
        ReturnValue_6: bool = self.UseBlackboard(BB_SpaceRabbit, Ref[BlackboardComponent])
        goto('L10')
        self.ReceivePossess(PossessedPawn)
        goto('L1559')
        ReturnValue2: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue2.SetValueAsBool(True, Ref[self.mPanicBBKeyName])
    
