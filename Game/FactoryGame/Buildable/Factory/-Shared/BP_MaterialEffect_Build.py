
from codegen.ue4_stub import *

from Game.FactoryGame.Buildable.-Shared.Audio.BuildEffect_2018-08.Play_F_BuildEffect_Switch import Play_F_BuildEffect_Switch
from Script.Engine import FinishSpawningActor
from Game.FactoryGame.Buildable.Factory.-Shared.BP_MaterialEffect_Build import ExecuteUbergraph_BP_MaterialEffect_Build
from Script.Engine import GetScaledBoxExtent
from Script.FactoryGame import GetCost
from Script.Engine import SpawnEmitterAtLocation
from Script.Engine import GetTransform
from Game.FactoryGame.Resource.Parts.AluminumPlate.Desc_AluminumPlate import Desc_AluminumPlate
from Game.FactoryGame.-Shared.Audio.DebugTools.Debug_ComponentCreator import Debug_ComponentCreator
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Buildable.Factory.-Shared.BP_CostEffectActor import BP_CostEffectActor
from Game.FactoryGame.Resource.Parts.IronPlate.Desc_IronPlate import Desc_IronPlate
from Script.Engine import Array_Append
from Script.Engine import IsValid
from Script.Engine import EqualEqual_IntInt
from Script.Engine import FMax
from Game.FactoryGame.VFX.Misc.BuildEffect.P_BuildImpactFoot_01 import P_BuildImpactFoot_01
from Script.Engine import GetGameState
from Game.FactoryGame.Resource.Parts.IronIngot.Desc_IronIngot import Desc_IronIngot
from Script.FactoryGame import FGFactoryLegsComponent
from Script.Engine import GetComponentsByClass
from Script.Engine import SetClassPropertyByName
from Script.AkAudio import SetActorRTPCValue
from Script.Engine import GetComponentByClass
from Script.Engine import GreaterEqual_IntInt
from Script.FactoryGame import FGBuildable
from Script.Engine import FMin
from Script.Engine import Max
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import GameStateBase
from Script.Engine import StaticMeshComponent
from Game.FactoryGame.Buildable.-Shared.Audio.BuildEffect_2018-08.Play_F_BuildEffect_Switch_Thump import Play_F_BuildEffect_Switch_Thump
from Script.FactoryGame import FGGameState
from Script.Engine import K2_GetComponentLocation
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import MakeTransform
from Script.FactoryGame import OnUpdate
from Script.FactoryGame import OnStarted
from Script.Engine import GetOwner
from Script.FactoryGame import ItemAmount
from Script.AkAudio import AkComponent
from Script.FactoryGame import FGBuildableSpaceElevator
from Script.FactoryGame import GetCheatNoCost
from Script.FactoryGame import GetClearanceComponent
from Game.FactoryGame.Buildable.Factory.-Shared.BP_MaterialEffect_Build import ExecuteUbergraph_BP_MaterialEffect_Build.K2Node_Event_deltaTime
from Script.AkAudio import PostAkEvent
from Script.FactoryGame import GetFloatCurveValue
from Script.Engine import Delay
from Script.FactoryGame import FGMaterialEffect_Build
from Script.Engine import Conv_IntToFloat
from Script.Engine import BreakTransform
from Script.Engine import Array_Shuffle
from Script.Engine import LatentActionInfo
from Game.FactoryGame.Resource.Parts.Cement.Desc_Cement import Desc_Cement
from Script.FactoryGame import SetMeshes
from Script.Engine import SetFloatPropertyByName
from Game.FactoryGame.Buildable.-Shared.Audio.BuildEffect_2018-05.Play_BuildEffect_SwishComponents import Play_BuildEffect_SwishComponents
from Script.Engine import Default__GameplayStatics
from Script.Engine import ShapeComponent
from Game.FactoryGame.VFX.Misc.BuildEffect.P_BuildingComplete_01 import P_BuildingComplete_01
from Script.Engine import ComponentHasTag
from Game.FactoryGame.Resource.Parts.Motor.Desc_Motor import Desc_Motor
from Script.FactoryGame import GetMeshesBounds
from Script.Engine import Multiply_VectorVector
from Script.FactoryGame import FGItemDescriptor
from Script.FactoryGame import OnEnded
from Script.FactoryGame import PreStarted
from Script.Engine import SetVectorPropertyByName
from Game.FactoryGame.Buildable.-Shared.Audio.Play_BuildEffect_MegaThump import Play_BuildEffect_MegaThump
from Script.CoreUObject import Color
from Script.Engine import GreaterEqual_FloatFloat
from Script.Engine import BeginDeferredActorSpawnFromClass
from Script.Engine import FInterpTo
from Script.Engine import FCeil
from Script.CoreUObject import Vector
from Game.FactoryGame.Resource.Parts.IronScrew.Desc_IronScrew import Desc_IronScrew
from Script.Engine import RuntimeFloatCurve
from Script.FactoryGame import Default__FGSkySphere
from Script.FactoryGame import GetFootMeshComponents
from Script.FactoryGame import SetMaterialScalarParameterValue
from Script.Engine import Actor
from Script.Engine import ParticleSystemComponent
from Script.Engine import K2_GetActorLocation
from Script.Engine import SetFloatParameter
from Script.Engine import RandomUnitVector
from Script.FactoryGame import GetInstigator
from Script.Engine import BoxComponent
from Script.CoreUObject import Transform
from Script.Engine import MeshComponent

class BP_MaterialEffect_Build(FGMaterialEffect_Build):
    mCurrentStep: int32
    mElapsedTime: float
    mThrowDuration: float
    mDisplacementDuration: float = 1
    mMaterializeAmountCurrent: float
    mMaterializeAmount: float
    mDisplacementAmount: float
    mThrowCurve: RuntimeFloatCurve = Namespace(EditorCurveData={'Keys': [{'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 0, 'Value': 0, 'ArriveTangent': 0.4687862694263458, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 1, 'Value': 1, 'ArriveTangent': 2.4143052101135254, 'ArriveTangentWeight': 0, 'LeaveTangent': 21.799013137817383, 'LeaveTangentWeight': 0}], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$Empty': True})
    mThrowQueue: List[TSubclassOf[FGItemDescriptor]]
    mCostAmountPerThrow: int32 = 1
    mMaterializeAmountPerThrow: float
    mGlowPower: float
    mVolume: float
    mElapsedTimeCorrectionBuildup: float
    mOffsetCurve_Buildup: RuntimeFloatCurve = Namespace(EditorCurveData={'Keys': [{'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 0, 'Value': 0, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 1, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 1, 'Value': -1.5, 'ArriveTangent': 0.056543998420238495, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$Empty': True})
    mOffsetCurve_Drop: RuntimeFloatCurve = Namespace(EditorCurveData={'Keys': [{'InterpMode': 2, 'TangentMode': 1, 'TangentWeightMode': 0, 'Time': 0, 'Value': -1.5, 'ArriveTangent': 0.023319000378251076, 'ArriveTangentWeight': 0, 'LeaveTangent': 0.16357900202274323, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 2, 'TangentWeightMode': 0, 'Time': 0.10000000149011612, 'Value': 0, 'ArriveTangent': 40.77663040161133, 'ArriveTangentWeight': 0, 'LeaveTangent': -23.87531280517578, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 1, 'TangentWeightMode': 0, 'Time': 0.15000000596046448, 'Value': -0.5, 'ArriveTangent': 0, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 1, 'TangentWeightMode': 0, 'Time': 0.20000000298023224, 'Value': 0, 'ArriveTangent': 30.911006927490234, 'ArriveTangentWeight': 0, 'LeaveTangent': 0.08202599734067917, 'LeaveTangentWeight': 0}, {'InterpMode': 0, 'TangentMode': 0, 'TangentWeightMode': 0, 'Time': 1, 'Value': 0, 'ArriveTangent': 0.056543998420238495, 'ArriveTangentWeight': 0, 'LeaveTangent': 0, 'LeaveTangentWeight': 0}], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$Empty': True})
    mGlowPowerCurve: RuntimeFloatCurve = Namespace(EditorCurveData={'Keys': [{'InterpMode': 2, 'TangentMode': 2, 'TangentWeightMode': 0, 'Time': 0, 'Value': 20, 'ArriveTangent': 100.69493865966797, 'ArriveTangentWeight': 0, 'LeaveTangent': -40.7244987487793, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 1, 'TangentWeightMode': 0, 'Time': 1, 'Value': 0, 'ArriveTangent': -3.586557626724243, 'ArriveTangentWeight': 0, 'LeaveTangent': -3.586395740509033, 'LeaveTangentWeight': 0}], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$AssetPath': '/Game/FactoryGame/Buildable/Factory/-Shared/Curve_GlowPowerEnd.Curve_GlowPowerEnd'})
    mVolumeCurve: RuntimeFloatCurve = Namespace(EditorCurveData={'Keys': [{'InterpMode': 2, 'TangentMode': 2, 'TangentWeightMode': 0, 'Time': 0, 'Value': 0.5, 'ArriveTangent': 0.26993897557258606, 'ArriveTangentWeight': 0, 'LeaveTangent': 0.6435052752494812, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 2, 'TangentWeightMode': 0, 'Time': 5, 'Value': 1.5, 'ArriveTangent': 0.02571178786456585, 'ArriveTangentWeight': 0, 'LeaveTangent': 0.017290964722633362, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 1, 'TangentWeightMode': 0, 'Time': 100, 'Value': 3, 'ArriveTangent': -0.0019930896814912558, 'ArriveTangentWeight': 0, 'LeaveTangent': -0.001993088982999325, 'LeaveTangentWeight': 0}], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$Empty': True})
    mItemsThrown: int32
    mBoxBounds: Vector
    mOrigin: Vector
    mParticleCurve: RuntimeFloatCurve = Namespace(EditorCurveData={'Keys': [{'InterpMode': 2, 'TangentMode': 1, 'TangentWeightMode': 0, 'Time': 0, 'Value': 0.6000000238418579, 'ArriveTangent': 0.04267847537994385, 'ArriveTangentWeight': 0, 'LeaveTangent': 0.042677976191043854, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 1, 'TangentWeightMode': 0, 'Time': 100, 'Value': 2, 'ArriveTangent': 0.007463009562343359, 'ArriveTangentWeight': 0, 'LeaveTangent': 0.007462674751877785, 'LeaveTangentWeight': 0}], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$Empty': True})
    mParticleVeloCurve: RuntimeFloatCurve = Namespace(EditorCurveData={'Keys': [{'InterpMode': 2, 'TangentMode': 1, 'TangentWeightMode': 0, 'Time': 0, 'Value': 0.30000001192092896, 'ArriveTangent': 0.04143799841403961, 'ArriveTangentWeight': 0, 'LeaveTangent': 0.04143799841403961, 'LeaveTangentWeight': 0}, {'InterpMode': 2, 'TangentMode': 1, 'TangentWeightMode': 0, 'Time': 100, 'Value': 5, 'ArriveTangent': 0.019591720774769783, 'ArriveTangentWeight': 0, 'LeaveTangent': 0.0195916835218668, 'LeaveTangentWeight': 0}], 'PreInfinityExtrap': 4, 'PostInfinityExtrap': 4, 'DefaultValue': 3.4028234663852886e+38}, ExternalCurve={'$Empty': True})
    mMaterial = Namespace(AssetPath='/Game/FactoryGame/Buildable/-Shared/Material/Factory_Materialize_Inst.Factory_Materialize_Inst')
    mAutoDestroy = True
    PrimaryComponentTick = Namespace(EndTickGroup=0, TickGroup=2, TickInterval=0, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=False, bTickEvenWhenPaused=False)
    bAutoActivate = True
    
    def PlayThumpSound(self):
        ReturnValue: Ptr[Actor] = self.GetOwner()
        ReturnValue_0: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_F_BuildEffect_Switch_Thump, ReturnValue, True)
    

    def InitMaterialParameters(self):
        self.SetMaterialScalarParameterValue("Width_Lower", 0.10000000149011612)
        self.SetMaterialScalarParameterValue("Glow Power", 2)
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(self.mOrigin)
        self.SetMaterialScalarParameterValue("OriginZ", Z1)
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(self.mBoxBounds)
        self.SetMaterialScalarParameterValue("HeightZ", Z)
    

    def SetupBounds(self):
        
        origin = None
        boxExtent = None
        self.GetMeshesBounds(False, False, Ref[origin], Ref[boxExtent])
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(boxExtent)
        
        X2 = None
        Y2 = None
        Z2 = None
        X2, Y2, Z2 = BreakVector(origin)
        ReturnValue: float = Z2 - Z1
        ReturnValue1: Vector = Vector(X2, Y2, ReturnValue)
        self.mOrigin = ReturnValue1
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(boxExtent)
        ReturnValue_0: Vector = Vector(X1, Y1, Z1)
        ReturnValue_1: Vector = ReturnValue_0 * 2
        self.mBoxBounds = ReturnValue_1
        ReturnValue_2: Ptr[Actor] = self.GetOwner()
        Elevator: Ptr[FGBuildableSpaceElevator] = Cast[FGBuildableSpaceElevator](ReturnValue_2)
        bSuccess: bool = Elevator
        if not bSuccess:
            goto('L876')
        self.mBoxBounds = Vector(5000, 5000, 6000)
        ReturnValue_3: Vector = Elevator.K2_GetActorLocation()
        self.mOrigin = ReturnValue_3
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(self.mBoxBounds)
        ReturnValue_4: float = X * Y
        ReturnValue1_0: float = ReturnValue_4 * Z
        ReturnValue2: float = ReturnValue1_0 * 9.999999747378752e-06
        ReturnValue_5: float = ReturnValue2 / 2000
        self.mVolume = ReturnValue_5
    

    def GotoNextStep(self):
        ReturnValue: int32 = self.mCurrentStep + 1
        Variable: int32 = ReturnValue
        self.mCurrentStep = Variable
        self.mElapsedTime = 0
    

    def CalcCostQueueNewLength(self):
        ReturnValue: float = FMin(self.mElapsedTime / self.mThrowDuration, 1)
        
        ReturnValue_0: float = Default__FGSkySphere.GetFloatCurveValue(ReturnValue, Ref[self.mThrowCurve])
        ReturnValue_1: float = 1 - ReturnValue_0
        ReturnValue1: float = ReturnValue_1 / self.mMaterializeAmountPerThrow
        ReturnValue_2: int32 = FCeil(ReturnValue1)
        ReturnValue_3: int32 = ReturnValue_2 - 1
        ReturnValue_4: int32 = Max(ReturnValue_3, 0)
        NewLength = ReturnValue_4
    

    def DebugFillCostQueue(self):
        ReturnValue: Ptr[GameStateBase] = Default__GameplayStatics.GetGameState(self)
        
        ReturnValue_0: int32 = len(self.mThrowQueue)
        State: Ptr[FGGameState] = Cast[FGGameState](ReturnValue)
        bSuccess: bool = State
        ReturnValue_1: bool = EqualEqual_IntInt(ReturnValue_0, 0)
        ReturnValue_2: bool = State.GetCheatNoCost()
        ReturnValue_3: bool = ReturnValue_2 and ReturnValue_1
        if not ReturnValue_3:
            goto('L590')
        Array: Const[List[TSubclassOf[FGItemDescriptor]]] = [Desc_IronIngot, Desc_IronPlate, Desc_IronScrew, Desc_AluminumPlate, Desc_Motor, Desc_Cement, Desc_Cement, Desc_IronPlate, Desc_IronPlate, Desc_IronPlate, Desc_IronPlate, Desc_IronPlate, Desc_IronPlate, Desc_IronPlate, Desc_IronPlate, Desc_IronPlate, Desc_IronPlate, Desc_IronPlate, Desc_IronPlate, Desc_IronPlate, Desc_IronPlate, Desc_IronPlate, Desc_Cement, Desc_IronPlate, Desc_IronPlate, Desc_IronPlate]
        
        Default__KismetArrayLibrary.Array_Append(Ref[self.mThrowQueue], Ref[Array])
    

    def CalcDisplacementAmount(self):
        ReturnValue: float = FMax(self.mElapsedTime - self.mThrowDuration / self.mDisplacementDuration, 0)
        
        ReturnValue_0: float = Default__FGSkySphere.GetFloatCurveValue(ReturnValue, Ref[self.mOffsetCurve_Drop])
        amount = ReturnValue_0
    

    def UpdateCostQueue(self):
        
        NewLength = None
        self.CalcCostQueueNewLength(Ref[NewLength])
        
        ReturnValue: int32 = len(self.mThrowQueue)
        ReturnValue_0: bool = ReturnValue > NewLength
        ReturnValue1: bool = ReturnValue > 0
        ReturnValue_1: bool = ReturnValue_0 and ReturnValue1
        if not ReturnValue_1:
            goto('L1904')
        
        Item = None
        Item = self.mThrowQueue[0]
        LocalItemDescriptor = Item
        
        self.mThrowQueue.remove(0)
        ReturnValue1_0: Ptr[Actor] = self.GetInstigator()
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1_0)
        if not ReturnValue_2:
            goto('L1890')
        ReturnValue2: Ptr[Actor] = self.GetInstigator()
        ReturnValue_3: Transform = ReturnValue2.GetTransform()
        
        Location = None
        Rotation = None
        Scale = None
        # Label 481
        BreakTransform(Ref[ReturnValue_3], Ref[Location], Ref[Rotation], Ref[Scale])
        ReturnValue_4: Transform = MakeTransform(Location, Rotation, Scale)
        
        ReturnValue_5: Ptr[Actor] = Default__GameplayStatics.BeginDeferredActorSpawnFromClass(self, BP_CostEffectActor, 1, None, Ref[ReturnValue_4])
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(self.mBoxBounds)
        ReturnValue_6: float = Y * 0.4000000059604645
        ReturnValue1_1: float = X * 0.4000000059604645
        ReturnValue_7: Vector = Vector(ReturnValue1_1, ReturnValue_6, 0)
        ReturnValue_8: float = self.mItemsThrown * self.mMaterializeAmountPerThrow
        ReturnValue2_0: float = Z * ReturnValue_8
        ReturnValue1_2: Vector = Vector(0, 0, ReturnValue2_0)
        ReturnValue_9: Vector = RandomUnitVector()
        ReturnValue_10: Vector = Multiply_VectorVector(ReturnValue_9, ReturnValue_7)
        ReturnValue_11: Vector = ReturnValue_10 + ReturnValue1_2
        ReturnValue1_3: Vector = self.mOrigin + ReturnValue_11
        
        Default__KismetSystemLibrary.SetVectorPropertyByName(ReturnValue_5, "mTargetLocation", Ref[ReturnValue1_3])
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(self.mBoxBounds)
        ReturnValue_12: float = FMin(X, Y)
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue_5, "mTargetExtent", ReturnValue_12)
        Default__KismetSystemLibrary.SetClassPropertyByName(ReturnValue_5, "mItemDescriptor", LocalItemDescriptor)
        ReturnValue2 = self.GetInstigator()
        ReturnValue_3 = ReturnValue2.GetTransform()
        
        Location = None
        Rotation = None
        Scale = None
        BreakTransform(Ref[ReturnValue_3], Ref[Location], Ref[Rotation], Ref[Scale])
        ReturnValue_4 = MakeTransform(Location, Rotation, Scale)
        
        ReturnValue_13: Ptr[BP_CostEffectActor] = Default__GameplayStatics.FinishSpawningActor(ReturnValue_5, Ref[ReturnValue_4])
        OutputDelegate.BindUFunction(self, OnCostActorReachedTarget)
        ReturnValue_13.OnReachedTarget.AddUnique(OutputDelegate)
        ReturnValue_14: int32 = self.mItemsThrown + 1
        Variable: int32 = ReturnValue_14
        self.mItemsThrown = Variable
        ReturnValue_15: Ptr[Actor] = self.GetInstigator()
        ReturnValue_16: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_BuildEffect_SwishComponents, ReturnValue_15, True)
        # End
        # Label 1890
        self.OnCostActorReachedTarget()
    

    def SetupCostQueue(self):
        ExecutionFlow.Push("L2152")
        LocalPartThreshold = 40
        ReturnValue: Ptr[Actor] = self.GetInstigator()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L472')
        ReturnValue_1: List[ItemAmount] = self.GetCost()
        Variable1: int32 = 0
        Variable: int32 = 0
        
        # Label 187
        ReturnValue2: int32 = len(ReturnValue_1)
        ReturnValue1: bool = Variable1 <= ReturnValue2
        if not ReturnValue1:
            goto('L693')
        Variable = Variable1
        ExecutionFlow.Push("L2004")
        
        Item = None
        Item = ReturnValue_1[Variable]
        ReturnValue3: int32 = Item.amount + LocalCounter
        LocalCounter = ReturnValue3
        goto(ExecutionFlow.Pop())
        # Label 472
        self.DebugFillCostQueue()
        
        ReturnValue_2: int32 = len(self.mThrowQueue)
        ReturnValue3_0: float = Conv_IntToFloat(ReturnValue_2)
        ReturnValue2_0: float = 1 / ReturnValue3_0
        self.mMaterializeAmountPerThrow = ReturnValue2_0
        
        Default__KismetArrayLibrary.Array_Shuffle(Ref[self.mThrowQueue])
        goto(ExecutionFlow.Pop())
        # Label 693
        ReturnValue_3: bool = GreaterEqual_IntInt(LocalCounter, LocalPartThreshold)
        if not ReturnValue_3:
            goto('L1192')
        ReturnValue1_0: float = Conv_IntToFloat(LocalPartThreshold)
        # Label 782
        ReturnValue2_1: float = Conv_IntToFloat(LocalCounter)
        ReturnValue1_1: float = ReturnValue2_1 / ReturnValue1_0
        ReturnValue1_2: int32 = FCeil(ReturnValue1_1)
        self.mCostAmountPerThrow = ReturnValue1_2
        ReturnValue_4: bool = self.mCostAmountPerThrow > 1
        if not ReturnValue_4:
            goto('L1192')
        ReturnValue_5: float = Conv_IntToFloat(self.mCostAmountPerThrow)
        
        ReturnValue_6: float = Default__FGSkySphere.GetFloatCurveValue(self.mVolume, Ref[self.mVolumeCurve])
        ReturnValue_7: float = ReturnValue_5 / ReturnValue_6
        ReturnValue_8: int32 = FCeil(ReturnValue_7)
        self.mCostAmountPerThrow = ReturnValue_8
        # Label 1192
        Variable_0: int32 = 0
        Variable1_0: int32 = 0
        
        # Label 1238
        ReturnValue1_3: int32 = len(ReturnValue_1)
        ReturnValue_9: bool = Variable_0 <= ReturnValue1_3
        if not ReturnValue_9:
            goto('L472')
        Variable1_0 = Variable_0
        ExecutionFlow.Push("L1930")
        ReturnValue4: float = Conv_IntToFloat(self.mCostAmountPerThrow)
        
        Item1 = None
        Item1 = ReturnValue_1[Variable1_0]
        ReturnValue5: float = Conv_IntToFloat(Item1.amount)
        ReturnValue3_1: float = ReturnValue5 / ReturnValue4
        ReturnValue2_2: int32 = FCeil(ReturnValue3_1)
        ReturnValue_10: int32 = Max(ReturnValue2_2, 1)
        LocalNumActors = ReturnValue_10
        Variable_1: int32 = 0
        # Label 1698
        ReturnValue_11: int32 = LocalNumActors - 1
        ReturnValue_12: bool = Variable_1 <= ReturnValue_11
        if not ReturnValue_12:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L2078")
        
        Item1 = None
        Item1 = ReturnValue_1[Variable1_0]
        
        Item1.ItemClass = None
        ReturnValue_13: int32 = self.mThrowQueue.append(Item1.ItemClass)
        goto(ExecutionFlow.Pop())
        # Label 1930
        ReturnValue_14: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_14
        goto('L1238')
        # Label 2004
        ReturnValue2_3: int32 = Variable1 + 1
        # Label 2046
        Variable1 = ReturnValue2_3
        goto('L187')
        # Label 2078
        ReturnValue1_4: int32 = Variable_1 + 1
        Variable_1 = ReturnValue1_4
        goto('L1698')
    

    def SetupDuration(self):
        
        ReturnValue: int32 = len(self.mThrowQueue)
        ReturnValue_0: float = ReturnValue * 0.10000000149011612
        self.mThrowDuration = ReturnValue_0
    

    def SetupMeshes(self):
        ExecutionFlow.Push("L782")
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 51
        ReturnValue: Ptr[Actor] = self.GetOwner()
        ReturnValue_0: List[Ptr[MeshComponent]] = ReturnValue.GetComponentsByClass(MeshComponent)
        
        ReturnValue_1: int32 = len(ReturnValue_0)
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
            goto('L481')
        Variable_0 = Variable
        ExecutionFlow.Push("L501")
        ReturnValue = self.GetOwner()
        ReturnValue_0 = ReturnValue.GetComponentsByClass(MeshComponent)
        
        Item = None
        Item = ReturnValue_0[Variable_0]
        ReturnValue_3: bool = Item.ComponentHasTag("CustomMaterial")
        if not ReturnValue_3:
            goto('L575')
        goto(ExecutionFlow.Pop())
        # Label 481
        self.SetMeshes(localMeshes)
        goto(ExecutionFlow.Pop())
        # Label 501
        ReturnValue_4: int32 = Variable + 1
        Variable = ReturnValue_4
        goto('L51')
        # Label 575
        ReturnValue = self.GetOwner()
        ReturnValue_0 = ReturnValue.GetComponentsByClass(MeshComponent)
        
        Item = None
        Item = ReturnValue_0[Variable_0]
        
        Item = None
        ReturnValue_5: int32 = localMeshes.append(Item)
        goto(ExecutionFlow.Pop())
    

    def SpawnFootEmitters(self):
        ExecutionFlow.Push("L1326")
        ReturnValue: Ptr[Actor] = self.GetOwner()
        ReturnValue_0: Ptr[FGFactoryLegsComponent] = ReturnValue.GetComponentByClass(FGFactoryLegsComponent)
        ReturnValue_1: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_0)
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        Variable_0: int32 = 0
        # Label 183
        ReturnValue = self.GetOwner()
        ReturnValue_0 = ReturnValue.GetComponentByClass(FGFactoryLegsComponent)
        ReturnValue_2: List[Ptr[StaticMeshComponent]] = ReturnValue_0.GetFootMeshComponents()
        
        ReturnValue_3: int32 = len(ReturnValue_2)
        ReturnValue_4: bool = Variable <= ReturnValue_3
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L1252")
        ReturnValue = self.GetOwner()
        ReturnValue_0 = ReturnValue.GetComponentByClass(FGFactoryLegsComponent)
        ReturnValue_2 = ReturnValue_0.GetFootMeshComponents()
        
        Item = None
        Item = ReturnValue_2[Variable_0]
        ReturnValue_5: Vector = Item.K2_GetComponentLocation()
        ReturnValue_6: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_BuildImpactFoot_01, ReturnValue_5, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        
        ReturnValue1: float = Default__FGSkySphere.GetFloatCurveValue(self.mVolume, Ref[self.mParticleCurve])
        ReturnValue_6.SetFloatParameter("smoke_01_size", ReturnValue1)
        
        ReturnValue1 = Default__FGSkySphere.GetFloatCurveValue(self.mVolume, Ref[self.mParticleCurve])
        ReturnValue_6.SetFloatParameter("smoke_02_size", ReturnValue1)
        
        ReturnValue_7: float = Default__FGSkySphere.GetFloatCurveValue(self.mVolume, Ref[self.mParticleVeloCurve])
        ReturnValue_6.SetFloatParameter("smoke_01_acc", ReturnValue_7)
        
        ReturnValue_7 = Default__FGSkySphere.GetFloatCurveValue(self.mVolume, Ref[self.mParticleVeloCurve])
        ReturnValue_6.SetFloatParameter("smoke_02_acc", ReturnValue_7)
        goto(ExecutionFlow.Pop())
        # Label 1252
        ReturnValue_8: int32 = Variable + 1
        Variable = ReturnValue_8
        goto('L183')
    

    def OnUpdate(self):
        ExecuteUbergraph_BP_MaterialEffect_Build.K2Node_Event_deltaTime = DeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_MaterialEffect_Build(2651)
    

    def OnEnded(self):
        self.ExecuteUbergraph_BP_MaterialEffect_Build(4067)
    

    def PreStarted(self):
        self.ExecuteUbergraph_BP_MaterialEffect_Build(4082)
    

    def OnStarted(self):
        self.ExecuteUbergraph_BP_MaterialEffect_Build(4149)
    

    def OnCostActorReachedTarget(self):
        self.ExecuteUbergraph_BP_MaterialEffect_Build(4446)
    

    def ExecuteUbergraph_BP_MaterialEffect_Build(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.PlayThumpSound()
        # Label 29
        Default__KismetSystemLibrary.Delay(self, 0.4000000059604645, LatentActionInfo(Linkage = 106, UUID = -2095869779, ExecutionFunction = "ExecuteUbergraph_BP_MaterialEffect_Build", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        ReturnValue: Ptr[Actor] = self.GetOwner()
        ReturnValue_0: Vector = ReturnValue.K2_GetActorLocation()
        ReturnValue_1: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_BuildingComplete_01, ReturnValue_0, Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), True, 0)
        
        ReturnValue5: float = Default__FGSkySphere.GetFloatCurveValue(self.mVolume, Ref[self.mParticleVeloCurve])
        ReturnValue_1.SetFloatParameter("BurstScale", ReturnValue5)
        
        ReturnValue6: float = Default__FGSkySphere.GetFloatCurveValue(self.mVolume, Ref[self.mParticleVeloCurve])
        ReturnValue2: float = ReturnValue6 * 20
        ReturnValue_1.SetFloatParameter("BurstScaleLight", ReturnValue2)
        ReturnValue1: Ptr[Actor] = self.GetOwner()
        AsFGBuildable: Ptr[FGBuildable] = Cast[FGBuildable](ReturnValue1)
        bSuccess: bool = AsFGBuildable
        ReturnValue_2: Ptr[ShapeComponent] = AsFGBuildable.GetClearanceComponent()
        Collision: Ptr[BoxComponent] = Cast[BoxComponent](ReturnValue_2)
        bSuccess1: bool = Collision
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue_3: Vector = Collision.GetScaledBoxExtent()
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_3)
        ReturnValue3: float = Z * 2
        ReturnValue4: float = Y * -1.100000023841858
        ReturnValue5_0: float = Y * 1.100000023841858
        ReturnValue6_0: float = X * -1.100000023841858
        ReturnValue7: float = X * 1.100000023841858
        ReturnValue_4: Vector = Vector(ReturnValue6_0, ReturnValue4, 0)
        ReturnValue1_0: Vector = Vector(ReturnValue7, ReturnValue5_0, ReturnValue3)
        ParticleSysParam.Name = "Location"
        ParticleSysParam.ParamType = 4
        ParticleSysParam.Scalar = 0
        ParticleSysParam.Scalar_Low = 0
        ParticleSysParam.Vector = ReturnValue1_0
        ParticleSysParam.Vector_Low = ReturnValue_4
        ParticleSysParam.Color = Color(B = 0, G = 0, R = 0, A = 0)
        ParticleSysParam.Actor = None
        ParticleSysParam.Material = None
        
        ReturnValue_1.InstanceParameters = None
        ParticleSysParam = None
        ReturnValue_5: int32 = ReturnValue_1.InstanceParameters.append(ParticleSysParam)
        goto(ExecutionFlow.Pop())
        # Label 1551
        ExecutionFlow.Push("L1571")
        if not Variable1:
            goto('L1930')
        goto(ExecutionFlow.Pop())
        # Label 1571
        if not Variable2:
            goto('L1586')
        goto(ExecutionFlow.Pop())
        # Label 1586
        Variable2: bool = True
        self.SpawnFootEmitters()
        
        X2 = None
        Y2 = None
        Z2 = None
        X2, Y2, Z2 = BreakVector(self.mBoxBounds)
        ReturnValue4_0: float = X2 + Y2
        ReturnValue5_1: float = ReturnValue4_0 + Z2
        ReturnValue4_1: float = ReturnValue5_1 / 10
        ReturnValue1_1: bool = ReturnValue4_1 <= 1400
        if not ReturnValue1_1:
            goto('L1844')
        goto('L15')
        # Label 1844
        ReturnValue3_0: Ptr[Actor] = self.GetOwner()
        ReturnValue1_2: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_BuildEffect_MegaThump, ReturnValue3_0, True)
        goto('L29')
        # Label 1930
        Variable1: bool = True
        if not False:
           goto(ExecutionFlow.Pop())
        Variable2 = True
        goto(ExecutionFlow.Pop())
        # Label 1955
        if not Variable:
            goto('L1970')
        goto(ExecutionFlow.Pop())
        # Label 1970
        Variable: bool = True
        self.InitMaterialParameters()
        goto(ExecutionFlow.Pop())
        # Label 1996
        Variable = True
        goto(ExecutionFlow.Pop())
        # Label 2008
        ExecutionFlow.Push("L1955")
        if not Variable_0:
            goto('L2028')
        goto(ExecutionFlow.Pop())
        # Label 2028
        Variable_0: bool = True
        if not False:
           goto(ExecutionFlow.Pop())
        goto('L1996')
        # Label 2046
        self.SetMaterialScalarParameterValue("MaterializeAmount", self.mMaterializeAmount)
        # Label 2078
        goto(ExecutionFlow.Pop())
        # Label 2079
        self.SetMaterialScalarParameterValue("BuildOffset", self.mDisplacementAmount)
        goto(ExecutionFlow.Pop())
        # Label 2112
        if not Variable1_0:
            goto('L2127')
        goto(ExecutionFlow.Pop())
        # Label 2127
        Variable1_0: bool = True
        self.mElapsedTimeCorrectionBuildup = self.mElapsedTime
        ReturnValue2_0: Ptr[Actor] = self.GetOwner()
        ReturnValue2_1: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Debug_ComponentCreator, ReturnValue2_0, True)
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(self.mBoxBounds)
        ReturnValue2_2: float = X1 + Y1
        ReturnValue3_1: float = ReturnValue2_2 + Z1
        ReturnValue3_2: float = ReturnValue3_1 / 10
        ReturnValue2_0 = self.GetOwner()
        Default__AkGameplayStatics.SetActorRTPCValue("RTPC_BoxVector", ReturnValue3_2, 0, ReturnValue2_0)
        ReturnValue2_0 = self.GetOwner()
        ReturnValue_6: Ptr[AkComponent] = Default__AkGameplayStatics.PostAkEvent(Play_F_BuildEffect_Switch, ReturnValue2_0, True)
        goto(ExecutionFlow.Pop())
        # Label 2596
        Variable1_0 = True
        goto(ExecutionFlow.Pop())
        # Label 2608
        Variable2_0: bool = True
        if not False:
           goto(ExecutionFlow.Pop())
        goto('L2596')
        # Label 2626
        if not Variable2_0:
            goto('L2608')
        goto(ExecutionFlow.Pop())
        # Label 2641
        ExecutionFlow.Push("L2112")
        goto('L2626')
        self.OnUpdate(deltaTime)
        ReturnValue_7: float = self.mElapsedTime + deltaTime
        self.mElapsedTime = ReturnValue_7
        ExecutionFlow.Push("L2753")
        goto('L2008')
        # Label 2753
        CmpSuccess: bool = self.mCurrentStep != 0
        if not CmpSuccess:
            goto('L3452')
        CmpSuccess = self.mCurrentStep != 1
        if not CmpSuccess:
            goto('L2898')
        CmpSuccess = self.mCurrentStep != 2
        if not CmpSuccess:
            goto('L4052')
        goto(ExecutionFlow.Pop())
        # Label 2898
        ReturnValue1_3: float = FMin(self.mElapsedTime / self.mDisplacementDuration, 1)
        
        ReturnValue_8: float = Default__FGSkySphere.GetFloatCurveValue(ReturnValue1_3, Ref[self.mGlowPowerCurve])
        self.mGlowPower = ReturnValue_8
        self.SetMaterialScalarParameterValue("Glow Power", self.mGlowPower)
        ExecutionFlow.Push("L1551")
        ReturnValue_9: float = FMin(self.mElapsedTime / self.mDisplacementDuration, 1)
        
        ReturnValue1_4: float = Default__FGSkySphere.GetFloatCurveValue(ReturnValue_9, Ref[self.mOffsetCurve_Drop])
        
        ReturnValue3_3: float = Default__FGSkySphere.GetFloatCurveValue(self.mVolume, Ref[self.mVolumeCurve])
        ReturnValue_10: float = ReturnValue1_4 * ReturnValue3_3
        self.mDisplacementAmount = ReturnValue_10
        self.SetMaterialScalarParameterValue("BuildOffset", self.mDisplacementAmount)
        ReturnValue_11: bool = self.mGlowPower <= 0.009999999776482582
        if not ReturnValue_11:
           goto(ExecutionFlow.Pop())
        self.GotoNextStep()
        goto(ExecutionFlow.Pop())
        # Label 3452
        self.UpdateCostQueue()
        ExecutionFlow.Push("L3874")
        ReturnValue_12: bool = self.mMaterializeAmount > 0
        if not ReturnValue_12:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L3525")
        goto('L2641')
        # Label 3525
        ReturnValue_13: float = self.mElapsedTime - self.mElapsedTimeCorrectionBuildup
        ReturnValue2_3: float = FMin(ReturnValue_13 / self.mThrowDuration, 1)
        
        ReturnValue2_4: float = Default__FGSkySphere.GetFloatCurveValue(ReturnValue2_3, Ref[self.mOffsetCurve_Buildup])
        
        ReturnValue4_2: float = Default__FGSkySphere.GetFloatCurveValue(self.mVolume, Ref[self.mVolumeCurve])
        ReturnValue1_5: float = ReturnValue2_4 * ReturnValue4_2
        self.mDisplacementAmount = ReturnValue1_5
        self.SetMaterialScalarParameterValue("BuildOffset", self.mDisplacementAmount)
        goto(ExecutionFlow.Pop())
        # Label 3874
        ReturnValue_14: float = FInterpTo(self.mMaterializeAmountCurrent, self.mMaterializeAmount, deltaTime, 20)
        self.mMaterializeAmountCurrent = ReturnValue_14
        self.SetMaterialScalarParameterValue("MaterializeAmount", self.mMaterializeAmountCurrent)
        ReturnValue_15: bool = GreaterEqual_FloatFloat(self.mMaterializeAmountCurrent, 0.9900000095367432)
        if not ReturnValue_15:
           goto(ExecutionFlow.Pop())
        self.GotoNextStep()
        goto(ExecutionFlow.Pop())
        # Label 4052
        self.Deactivate()
        goto(ExecutionFlow.Pop())
        self.OnEnded()
        goto('L1551')
        self.PreStarted()
        self.SetupMeshes()
        self.SetupBounds()
        self.SetupCostQueue()
        self.SetupDuration()
        goto(ExecutionFlow.Pop())
        self.OnStarted()
        
        ReturnValue_16: int32 = len(self.mThrowQueue)
        ReturnValue_17: bool = ReturnValue_16 > 0
        if not ReturnValue_17:
            goto('L4395')
        self.mCurrentStep = 0
        self.mElapsedTime = 0
        self.mMaterializeAmount = 0
        self.SetMaterialScalarParameterValue("MaterializeAmount", self.mMaterializeAmount)
        self.mDisplacementAmount = 0
        goto('L2079')
        # Label 4395
        self.mCurrentStep = 1
        self.mMaterializeAmount = 1
        goto('L2046')
        ReturnValue1_6: float = self.mMaterializeAmount + self.mMaterializeAmountPerThrow
        self.mMaterializeAmount = ReturnValue1_6
        goto(ExecutionFlow.Pop())
    
