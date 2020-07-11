
from codegen.ue4_stub import *

from Script.FactoryGame import GetTargetLastValidLocation
from Game.FactoryGame.Character.Creature.Enemy.BP_EnemyController import ExecuteUbergraph_BP_EnemyController
from Game.FactoryGame.Character.Creature.Enemy.BP_EnemyController import ExecuteUbergraph_BP_EnemyController.K2Node_Event_PossessedPawn
from Game.FactoryGame.Character.Creature.Enemy.BP_EnemyController import ExecuteUbergraph_BP_EnemyController.K2Node_Event_lostActor
from Script.Engine import ReceivePossess
from Script.AIModule import UseBlackboard
from Script.AIModule import BehaviorTree
from Script.AIModule import BlackboardComponent
from Script.AIModule import SetValueAsVector
from Script.FactoryGame import FGEnemyController
from Script.AIModule import GetBlackboard
from Script.CoreUObject import Vector
from Script.AIModule import Default__AIBlueprintHelperLibrary
from Script.AIModule import BlackboardData

class BP_EnemyController(FGEnemyController):
    mBlackboardAsset: Ptr[BlackboardData] = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/BB_EnemyBlackboard.BB_EnemyBlackboard')
    mBehaviorTree: Ptr[BehaviorTree] = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Walker/BT_Walker.BT_Walker')
    mLastKnownTargetLocationBBKeyName: FName = LastKnownTargetLocation
    mUpdateAggroInterval = 1
    mTimeToLoseAllAggro = 10
    mAggroBaseWeight = 1
    mAggroAggroWeight = 1
    mAggroDistanceWeight = 1
    mTargetSwitchFactor = 0.30000001192092896
    mDefaultIgnoreCooldown = 5
    mStaticIgnoreCooldown = 5
    mAggroDistanceCurve = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/AI/DistanceAggroCurve.DistanceAggroCurve')
    mLoseAggroThreshold = -1
    mIgnoredAggroTargetClasses = ['/Game/FactoryGame/Buildable/Vehicle/Train/Wagon/BP_FreightWagon.BP_FreightWagon_C', '/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/BP_Locomotive.BP_Locomotive_C', '/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/BP_Locomotive.BP_Locomotive_C', '/Game/FactoryGame/Buildable/Vehicle/-Shared/PassengerSeat/BP_PassengerSeat.BP_PassengerSeat_C', '/Script/FactoryGame.FGFreightWagon', '/Script/FactoryGame.FGLocomotive', '/Script/FactoryGame.FGPassengerSeat', '/Script/FactoryGame.FGRailroadVehicle']
    mPanicIgnoreTime = 3
    PathFollowingComponent = Namespace(ObjectClass='/Script/AIModule.PathFollowingComponent', ObjectFlags=2883617, ObjectName='PathFollowingComponent')
    PerceptionComponent = Namespace(DominantSense='/Script/AIModule.AISense_Sight', ObjectClass='/Script/AIModule.AIPerceptionComponent', ObjectFlags=2883617, ObjectName='PerceptionComponent', OnTargetPerceptionUpdated=0, SensesConfig=[{'$ObjectClass': '/Script/AIModule.AISenseConfig_Sight', '$ObjectFlags': 2621481, '$ObjectName': 'AISenseConfig_Sight_0', 'SightRadius': 4500, 'LoseSightRadius': 5000, 'PeripheralVisionAngleDegrees': 179, 'bStartsEnabled': False}])
    ActionsComp = Namespace(ObjectClass='/Script/AIModule.PawnActionsComponent', ObjectFlags=2883617, ObjectName='ActionsComp')
    TransformComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    
    def ReceivePossess(self):
        ExecuteUbergraph_BP_EnemyController.K2Node_Event_PossessedPawn = PossessedPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_EnemyController(10)
    

    def OnAggroTargetLost(self):
        ExecuteUbergraph_BP_EnemyController.K2Node_Event_lostActor = lostActor #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_EnemyController(105)
    

    def ExecuteUbergraph_BP_EnemyController(self):
        self.ReceivePossess(PossessedPawn)
        
        BlackboardComponent = None
        ReturnValue: bool = self.UseBlackboard(self.mBlackboardAsset, Ref[BlackboardComponent])
        ReturnValue_0: bool = self.RunBehaviorTree(self.mBehaviorTree)
        # End
        ReturnValue_1: Vector = self.GetTargetLastValidLocation()
        ReturnValue_2: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue_2.SetValueAsVector(ReturnValue_1, Ref[self.mLastKnownTargetLocationBBKeyName])
    
