
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.Enemy.BP_EnemyController import BP_EnemyController

class Controller_Stinger(BP_EnemyController):
    mBlackboardAsset = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Stinger/AI/BB_Stinger.BB_Stinger')
    mBehaviorTree = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Stinger/AI/BT_Stinger.BT_Stinger')
    mUpdateAggroInterval = 1
    mTimeToLoseAllAggro = 10
    mAggroBaseWeight = 1
    mAggroAggroWeight = 1
    mAggroDistanceWeight = 1
    mTargetSwitchFactor = 0.30000001192092896
    mDefaultIgnoreCooldown = 0.10000000149011612
    mStaticIgnoreCooldown = 5
    mAggroDistanceCurve = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Stinger/AI/StingerDistanceAggro.StingerDistanceAggro')
    mGainAggroThreshold = 0.20000000298023224
    mLoseAggroThreshold = 0.15000000596046448
    mAttackPattern = ['/Game/FactoryGame/Character/Creature/Enemy/Stinger/Attack_StingerSwipe.Attack_StingerSwipe_C', '/Game/FactoryGame/Character/Creature/Enemy/Stinger/Attack_StingerSwipe.Attack_StingerSwipe_C', '/Game/FactoryGame/Character/Creature/Enemy/Stinger/Attack_StingerJump.Attack_StingerJump_C']
    mPanicIgnoreTime = 3
    PathFollowingComponent = Namespace(ObjectClass='/Script/AIModule.PathFollowingComponent', ObjectFlags=2883617, ObjectName='PathFollowingComponent')
    PerceptionComponent = Namespace(DominantSense='/Script/AIModule.AISense_Sight', ObjectClass='/Script/AIModule.AIPerceptionComponent', ObjectFlags=2883617, ObjectName='PerceptionComponent', OnTargetPerceptionUpdated=0, SensesConfig=[{'$ObjectClass': '/Script/AIModule.AISenseConfig_Sight', '$ObjectFlags': 2621473, '$ObjectName': 'AISenseConfig_Sight_0', 'SightRadius': 9000, 'LoseSightRadius': 10500, 'PeripheralVisionAngleDegrees': 179, 'bStartsEnabled': False}, {'$ObjectClass': '/Script/AIModule.AISenseConfig_Hearing', '$ObjectFlags': 2621481, '$ObjectName': 'AISenseConfig_Hearing_0', 'HearingRange': 10000}])
    ActionsComp = Namespace(ObjectClass='/Script/AIModule.PawnActionsComponent', ObjectFlags=2883617, ObjectName='ActionsComp')
    TransformComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    
