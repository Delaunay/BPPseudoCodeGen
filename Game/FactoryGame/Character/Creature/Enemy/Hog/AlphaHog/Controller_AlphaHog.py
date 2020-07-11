
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.Enemy.Hog.Controller_HogCharge import Controller_HogCharge

class Controller_AlphaHog(Controller_HogCharge):
    mBehaviorTree = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Hog/AlphaHog/BT_AlphaHog.BT_AlphaHog')
    mUpdateAggroInterval = 1
    mAggroBaseWeight = 1
    mAggroAggroWeight = 1
    mAggroDistanceWeight = 1
    mPanicIgnoreTime = 3
    PathFollowingComponent = Namespace(ObjectClass='/Script/AIModule.PathFollowingComponent', ObjectFlags=2883617, ObjectName='PathFollowingComponent')
    PerceptionComponent = Namespace(DominantSense='/Script/AIModule.AISense_Sight', ObjectClass='/Script/AIModule.AIPerceptionComponent', ObjectFlags=2883617, ObjectName='PerceptionComponent', OnTargetPerceptionUpdated=0, SensesConfig=[{'$ObjectClass': '/Script/AIModule.AISenseConfig_Sight', '$ObjectFlags': 2621473, '$ObjectName': 'AISenseConfig_Sight_0', 'SightRadius': 4500, 'LoseSightRadius': 5000, 'PeripheralVisionAngleDegrees': 179, 'bStartsEnabled': False}, {'$ObjectClass': '/Script/AIModule.AISenseConfig_Hearing', '$ObjectFlags': 2621473, '$ObjectName': 'AISenseConfig_Hearing_0', 'HearingRange': 5000}])
    ActionsComp = Namespace(ObjectClass='/Script/AIModule.PawnActionsComponent', ObjectFlags=2883617, ObjectName='ActionsComp')
    TransformComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    
