
from codegen.ue4_stub import *

from Game.FactoryGame.Character.Creature.Enemy.BP_EnemyController import BP_EnemyController
from Script.AIModule import SetValueAsVector
from Script.AIModule import BlackboardComponent
from Script.FactoryGame import AddToAggroByTarget
from Script.AIModule import GetBlackboard
from Script.FactoryGame import StartPanic
from Script.AIModule import Default__AIBlueprintHelperLibrary
from Game.FactoryGame.Character.Creature.Enemy.Hog.Controller_HogCharge import ExecuteUbergraph_Controller_HogCharge
from Script.AIModule import SetValueAsBool
from Game.FactoryGame.Character.Creature.Enemy.Hog.Controller_HogCharge import ExecuteUbergraph_Controller_HogCharge.K2Node_ComponentBoundEvent_Actor
from Script.Engine import EqualEqual_NameName
from Game.FactoryGame.Character.Creature.Enemy.Hog.Controller_HogCharge import ExecuteUbergraph_Controller_HogCharge.K2Node_ComponentBoundEvent_Stimulus
from Script.FactoryGame import FGAggroTargetInterface

class Controller_HogCharge(BP_EnemyController):
    mIsChargingAtEnemy: bool
    mFinalGoalKeyName: FName = FinalGoal
    mHearNoiseKeyName: FName = DidHearNoise
    mNoiseLocationKeyName: FName = NoiseLocation
    mDoPanicName: FName = DoPanic
    mBlackboardAsset = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Hog/AI/BB_Hog.BB_Hog')
    mBehaviorTree = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Hog/AI/BT_Hog.BT_Hog')
    mUpdateAggroInterval = 1
    mTimeToLoseAllAggro = 6
    mAggroBaseWeight = 1
    mAggroAggroWeight = 1
    mAggroDistanceWeight = 1
    mTargetSwitchFactor = 1.100000023841858
    mDefaultIgnoreCooldown = 1
    mStaticIgnoreCooldown = 30
    mAggroDistanceCurve = Namespace(AssetPath='/Game/FactoryGame/Character/Creature/Enemy/Hog/Curve_DistanceAggroHog.Curve_DistanceAggroHog')
    mGainAggroThreshold = 0.800000011920929
    mLoseAggroThreshold = 0.6899999976158142
    mIgnoredAggroTargetClasses = ['/Game/FactoryGame/Buildable/Vehicle/Train/Wagon/BP_FreightWagon.BP_FreightWagon_C', '/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/BP_Locomotive.BP_Locomotive_C', '/Game/FactoryGame/Buildable/Vehicle/Train/Locomotive/BP_Locomotive.BP_Locomotive_C', '/Game/FactoryGame/Buildable/Vehicle/-Shared/PassengerSeat/BP_PassengerSeat.BP_PassengerSeat_C', '/Script/FactoryGame.FGFreightWagon', '/Script/FactoryGame.FGLocomotive', '/Script/FactoryGame.FGPassengerSeat', '/Script/FactoryGame.FGRailroadVehicle', '/Game/FactoryGame/Buildable/Vehicle/Tractor/BP_Tractor.BP_Tractor_C', '/Game/FactoryGame/Buildable/Vehicle/Truck/BP_Truck.BP_Truck_C', '/Game/FactoryGame/Buildable/Vehicle/Explorer/BP_Explorer.BP_Explorer_C']
    mPanicIgnoreTime = 3
    PathFollowingComponent = Namespace(ObjectClass='/Script/AIModule.PathFollowingComponent', ObjectFlags=2883617, ObjectName='PathFollowingComponent')
    PerceptionComponent = Namespace(DominantSense='/Script/AIModule.AISense_Sight', ObjectClass='/Script/AIModule.AIPerceptionComponent', ObjectFlags=2883617, ObjectName='PerceptionComponent', OnTargetPerceptionUpdated=0, SensesConfig=[{'$ObjectClass': '/Script/AIModule.AISenseConfig_Sight', '$ObjectFlags': 2621473, '$ObjectName': 'AISenseConfig_Sight_0', 'SightRadius': 4500, 'LoseSightRadius': 5000, 'PeripheralVisionAngleDegrees': 179, 'bStartsEnabled': False}, {'$ObjectClass': '/Script/AIModule.AISenseConfig_Hearing', '$ObjectFlags': 2621481, '$ObjectName': 'AISenseConfig_Hearing_0', 'HearingRange': 5000}])
    ActionsComp = Namespace(ObjectClass='/Script/AIModule.PawnActionsComponent', ObjectFlags=2883617, ObjectName='ActionsComp')
    TransformComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='TransformComponent0', bAbsoluteRotation=True)
    
    def BndEvt__PerceptionComponent_K2Node_ComponentBoundEvent_2_ActorPerceptionUpdatedDelegate__DelegateSignature(self, Actor: Ptr[Actor], Stimulus: AIStimulus):
        ExecuteUbergraph_Controller_HogCharge.K2Node_ComponentBoundEvent_Actor = Actor #  PERSISTENT_FRAME(
        ExecuteUbergraph_Controller_HogCharge.K2Node_ComponentBoundEvent_Stimulus = Stimulus #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Controller_HogCharge(10)
    

    def StartPanic(self):
        self.ExecuteUbergraph_Controller_HogCharge(417)
    

    def ExecuteUbergraph_Controller_HogCharge(self):
        ReturnValue: bool = EqualEqual_NameName(Stimulus.Tag, "WeaponFire")
        ReturnValue_0: bool = ReturnValue and Stimulus.bSuccessfullySensed
        if not ReturnValue_0:
            goto('L512')
        Interface: TScriptInterface[FGAggroTargetInterface] = QueryInterface[FGAggroTargetInterface](Actor)
        bSuccess: bool = Interface
        if not bSuccess:
            goto('L512')
        self.AddToAggroByTarget(Interface, 1)
        ReturnValue_1: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue_1.SetValueAsBool(True, Ref[self.mHearNoiseKeyName])
        ReturnValue_1 = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue_1.SetValueAsVector(Stimulus.StimulusLocation, Ref[self.mNoiseLocationKeyName])
        # End
        self.StartPanic()
        ReturnValue1: Ptr[BlackboardComponent] = Default__AIBlueprintHelperLibrary.GetBlackboard(self)
        
        ReturnValue1.SetValueAsBool(True, Ref[self.mDoPanicName])
    
