
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.Enemy.Spitter.Controller_Spitter import ExecuteUbergraph_Controller_Spitter
from Game.FactoryGame.Character.Creature.Enemy.BP_EnemyController import BP_EnemyController
from Script.Engine import Not_PreBool
from Script.AIModule import BlackboardComponent
from Script.FactoryGame import AddToAggroByTarget
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Controller_Spitter import ExecuteUbergraph_Controller_Spitter.K2Node_ComponentBoundEvent_Actor
from Script.AIModule import GetBlackboard
from Script.FactoryGame import CanSeeActor
from Script.AIModule import Default__AIBlueprintHelperLibrary
from Script.AIModule import SetValueAsBool
from Script.Engine import EqualEqual_NameName
from Script.FactoryGame import FGAggroTargetInterface
from Game.FactoryGame.Character.Creature.Enemy.Spitter.Controller_Spitter import ExecuteUbergraph_Controller_Spitter.K2Node_ComponentBoundEvent_Stimulus

class Controller_Spitter(BP_EnemyController):
    mDoPanicName: FName = DoPanic
    mBlackboardAsset = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Spitter/BB_Spitter.BB_Spitter')
    mBehaviorTree = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Spitter/BT_Spitter.BT_Spitter')
    mUpdateAggroInterval = 1
    mTimeToLoseAllAggro = 10
    mAggroBaseWeight = 1
    mAggroAggroWeight = 1
    mAggroDistanceWeight = 1
    mTargetSwitchFactor = 0.30000001192092896
    mDefaultIgnoreCooldown = 1
    mStaticIgnoreCooldown = 5
    mAggroDistanceCurve = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Spitter/Curve_SpitterDistanceAggro.Curve_SpitterDistanceAggro')
    mGainAggroThreshold = 0.6499999761581421
    mLoseAggroThreshold = 0.5
    mPanicIgnoreTime = 3
    PathFollowingComponent = Namespace(ObjectClass='/Script/AIModule.PathFollowingComponent', ObjectFlags=2883617, ObjectName='PathFollowingComponent')
    PerceptionComponent = Namespace(DominantSense='/Script/AIModule.AISense_Sight', ObjectClass='/Script/AIModule.AIPerceptionComponent', ObjectFlags=2883617, ObjectName='PerceptionComponent', OnTargetPerceptionUpdated=0, SensesConfig=[{'$ObjectClass': '/Script/AIModule.AISenseConfig_Sight', '$ObjectFlags': 2621473, '$ObjectName': 'AISenseConfig_Sight_0', 'SightRadius': 9000, 'LoseSightRadius': 11000, 'PeripheralVisionAngleDegrees': 179, 'bStartsEnabled': False}, {'$ObjectClass': '/Script/AIModule.AISenseConfig_Hearing', '$ObjectFlags': 2621481, '$ObjectName': 'AISenseConfig_Hearing_0', 'HearingRange': 7500}])
    ActionsComp = Namespace(ObjectClass='/Script/AIModule.PawnActionsComponent', ObjectFlags=2883617, ObjectName='ActionsComp')
    TransformComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    
    def BndEvt__PerceptionComponent_K2Node_ComponentBoundEvent_0_ActorPerceptionUpdatedDelegate__DelegateSignature(self, Actor: Ptr[Actor], Stimulus: AIStimulus):
        ExecuteUbergraph_Controller_Spitter.K2Node_ComponentBoundEvent_Actor = Actor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Controller_Spitter.K2Node_ComponentBoundEvent_Stimulus = Stimulus #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Controller_Spitter(10)
    

    def ExecuteUbergraph_Controller_Spitter(self):
        ReturnValue: bool = EqualEqual_NameName(Stimulus.Tag, "WeaponFire")
        ReturnValue_0: bool = ReturnValue and Stimulus.bSuccessfullySensed
        if not ReturnValue_0:
            goto('L376')
        Interface: TScriptInterface[FGAggroTargetInterface] = QueryInterface[FGAggroTargetInterface](Actor)
        bSuccess: bool = Interface
        if not bSuccess:
            goto('L376')
        self.AddToAggroByTarget(Interface, 0.699999988079071)
        ReturnValue_1: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        ReturnValue_2: bool = self.CanSeeActor(Actor)
        ReturnValue_3: bool = Not_PreBool(ReturnValue_2)
        
        ReturnValue_1.SetValueAsBool(ReturnValue_3, Ref[self.mDoPanicName])
    
