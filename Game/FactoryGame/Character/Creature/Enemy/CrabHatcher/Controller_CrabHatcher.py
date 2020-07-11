
from codegen.ue4_stub import *

from Script.Engine import Array_Find
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import FGCrabHatcher
from Script.Engine import K2_GetPawn
from Script.FactoryGame import SetThreatNearby
from Game.FactoryGame.Character.Creature.Enemy.CrabHatcher.Controller_CrabHatcher import ExecuteUbergraph_Controller_CrabHatcher.K2Node_ComponentBoundEvent_Stimulus
from Script.FactoryGame import FGCharacterPlayer
from Game.FactoryGame.Character.Creature.Enemy.CrabHatcher.Controller_CrabHatcher import ExecuteUbergraph_Controller_CrabHatcher.K2Node_ComponentBoundEvent_Actor
from Game.FactoryGame.Character.Creature.Enemy.CrabHatcher.Controller_CrabHatcher import ExecuteUbergraph_Controller_CrabHatcher
from Script.Engine import Pawn
from Game.FactoryGame.Character.Creature.Enemy.CrabHatcher.Controller_CrabHatcher import ExecuteUbergraph_Controller_CrabHatcher.K2Node_CustomEvent_inPlayer
from Script.Engine import GreaterEqual_IntInt
from Game.FactoryGame.Character.Creature.Enemy.CrabHatcher.Controller_CrabHatcher import ExecuteUbergraph_Controller_CrabHatcher.K2Node_CustomEvent_inPlayer1
from Game.FactoryGame.Character.Creature.Enemy.BP_EnemyController import BP_EnemyController

class Controller_CrabHatcher(BP_EnemyController):
    mPlayersNearby: List[Ptr[FGCharacterPlayer]]
    mBehaviorTree = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/CrabHatcher/AI/BT_CrabHatcher.BT_CrabHatcher')
    mUpdateAggroInterval = 1
    mTimeToLoseAllAggro = 10
    mAggroBaseWeight = 1
    mAggroDistanceWeight = 1
    mTargetSwitchFactor = 0.30000001192092896
    mGainAggroThreshold = 0.009999999776482582
    mLoseAggroThreshold = -1
    mIgnoredAggroTargetClasses = ['/Game/FactoryGame/Buildable/Vehicle/Train/Wagon/BP_FreightWagon.BP_FreightWagon_C', '/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/BP_Locomotive.BP_Locomotive_C', '/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/BP_Locomotive.BP_Locomotive_C', '/Game/FactoryGame/Buildable/Vehicle/-Shared/PassengerSeat/BP_PassengerSeat.BP_PassengerSeat_C', '/Script/FactoryGame.FGFreightWagon', '/Script/FactoryGame.FGLocomotive', '/Script/FactoryGame.FGPassengerSeat', '/Script/FactoryGame.FGRailroadVehicle', '/Script/FactoryGame.FGVehicle']
    mPanicIgnoreTime = 3
    PathFollowingComponent = Namespace(ObjectClass='/Script/AIModule.PathFollowingComponent', ObjectFlags=2883617, ObjectName='PathFollowingComponent')
    PerceptionComponent = Namespace(DominantSense='/Script/AIModule.AISense_Sight', ObjectClass='/Script/AIModule.AIPerceptionComponent', ObjectFlags=2883617, ObjectName='PerceptionComponent', OnTargetPerceptionUpdated=0, SensesConfig=[{'$ObjectClass': '/Script/AIModule.AISenseConfig_Sight', '$ObjectFlags': 2621473, '$ObjectName': 'AISenseConfig_Sight_0', 'SightRadius': 2000, 'LoseSightRadius': 2500, 'PeripheralVisionAngleDegrees': 179, 'bStartsEnabled': False}])
    ActionsComp = Namespace(ObjectClass='/Script/AIModule.PawnActionsComponent', ObjectFlags=2883617, ObjectName='ActionsComp')
    TransformComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    
    def UpdateThreatNearby(self):
        ReturnValue: Ptr[Pawn] = self.K2_GetPawn()
        Hatcher: Ptr[FGCrabHatcher] = Cast[FGCrabHatcher](ReturnValue)
        bSuccess: bool = Hatcher
        if not bSuccess:
            goto('L233')
        
        ReturnValue_0: int32 = len(self.mPlayersNearby)
        ReturnValue_1: bool = ReturnValue_0 > 0
        Hatcher.SetThreatNearby(ReturnValue_1)
    

    def BndEvt__PerceptionComponent_K2Node_ComponentBoundEvent_1_ActorPerceptionUpdatedDelegate__DelegateSignature(self, Actor: Ptr[Actor], Stimulus: AIStimulus):
        ExecuteUbergraph_Controller_CrabHatcher.K2Node_ComponentBoundEvent_Actor = Actor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Controller_CrabHatcher.K2Node_ComponentBoundEvent_Stimulus = Stimulus #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Controller_CrabHatcher(457)
    

    def TryRemovePlayer(self, inPlayer: Ptr[FGCharacterPlayer]):
        ExecuteUbergraph_Controller_CrabHatcher.K2Node_CustomEvent_inPlayer1 = inPlayer #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Controller_CrabHatcher(29)
    

    def TryAddPlayer(self, inPlayer: Ptr[FGCharacterPlayer]):
        ExecuteUbergraph_Controller_CrabHatcher.K2Node_CustomEvent_inPlayer = inPlayer #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Controller_CrabHatcher(268)
    

    def ExecuteUbergraph_Controller_CrabHatcher(self):
        # Label 10
        self.UpdateThreatNearby()
        # End
        
        inPlayer1 = None
        ReturnValue: int32 = Default__KismetArrayLibrary.Array_Find(Ref[self.mPlayersNearby], Ref[inPlayer1])
        ReturnValue_0: bool = GreaterEqual_IntInt(ReturnValue, 0)
        if not ReturnValue_0:
            goto('L615')
        
        inPlayer1 = None
        ReturnValue = Default__KismetArrayLibrary.Array_Find(Ref[self.mPlayersNearby], Ref[inPlayer1])
        
        self.mPlayersNearby.remove(ReturnValue)
        # End
        
        inPlayer = None
        ReturnValue1: int32 = Default__KismetArrayLibrary.Array_Find(Ref[self.mPlayersNearby], Ref[inPlayer])
        ReturnValue_1: bool = ReturnValue1 <= 0
        if not ReturnValue_1:
            goto('L615')
        
        inPlayer = None
        ReturnValue_2: int32 = self.mPlayersNearby.append(inPlayer)
        # End
        Player: Ptr[FGCharacterPlayer] = Cast[FGCharacterPlayer](Actor)
        bSuccess: bool = Player
        if not bSuccess:
            goto('L615')
        if not Stimulus.bSuccessfullySensed:
            goto('L587')
        self.TryAddPlayer(Player)
        goto('L10')
        # Label 587
        self.TryRemovePlayer(Player)
        goto('L10')
    
