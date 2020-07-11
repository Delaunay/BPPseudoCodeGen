
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.Enemy.BP_EnemyController import BP_EnemyController

class Controller_BabyCrab(BP_EnemyController):
    mBehaviorTree = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Crab/BabyCrab/BT_BabyCrab.BT_BabyCrab')
    mUpdateAggroInterval = 0.5
    mTimeToLoseAllAggro = 6
    mAggroBaseWeight = 1
    mAggroAggroWeight = 1
    mAggroDistanceWeight = 1
    mTargetSwitchFactor = 1.100000023841858
    mStaticIgnoreCooldown = 30
    mAggroDistanceCurve = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Hog/Curve_DistanceAggroHog.Curve_DistanceAggroHog')
    mGainAggroThreshold = 0.20000000298023224
    mIgnoredAggroTargetClasses = ['/Game/FactoryGame/Buildable/Vehicle/Train/Wagon/BP_FreightWagon.BP_FreightWagon_C', '/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/BP_Locomotive.BP_Locomotive_C', '/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/BP_Locomotive.BP_Locomotive_C', '/Game/FactoryGame/Buildable/Vehicle/-Shared/PassengerSeat/BP_PassengerSeat.BP_PassengerSeat_C', '/Script/FactoryGame.FGFreightWagon', '/Script/FactoryGame.FGLocomotive', '/Script/FactoryGame.FGPassengerSeat', '/Script/FactoryGame.FGRailroadVehicle', '/Game/FactoryGame/Buildable/Vehicle/Tractor/BP_Tractor.BP_Tractor_C', '/Game/FactoryGame/Buildable/Vehicle/Truck/BP_Truck.BP_Truck_C', '/Game/FactoryGame/Buildable/Vehicle/Explorer/BP_Explorer.BP_Explorer_C']
    mPanicIgnoreTime = 3
    PathFollowingComponent = Namespace(ObjectClass='/Script/AIModule.PathFollowingComponent', ObjectFlags=2883617, ObjectName='PathFollowingComponent')
    PerceptionComponent = Namespace(DominantSense='/Script/AIModule.AISense_Sight', ObjectClass='/Script/AIModule.AIPerceptionComponent', ObjectFlags=2883617, ObjectName='PerceptionComponent', OnTargetPerceptionUpdated=0, SensesConfig=[{'$ObjectClass': '/Script/AIModule.AISenseConfig_Sight', '$ObjectFlags': 2621473, '$ObjectName': 'AISenseConfig_Sight_0', 'PeripheralVisionAngleDegrees': 179, 'bStartsEnabled': False}])
    ActionsComp = Namespace(ObjectClass='/Script/AIModule.PawnActionsComponent', ObjectFlags=2883617, ObjectName='ActionsComp')
    TransformComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    
