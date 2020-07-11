
from codegen.ue4_stub import *

from Script.Engine import RandomBoolWithWeight
from Script.Engine import PlayerCameraManager
from Script.FactoryGame import GetParticleSystemFromMapArea
from Game.FactoryGame.Character.Player.BP_ProximitySubsystem import ExecuteUbergraph_BP_ProximitySubsystem.K2Node_Event_newArea
from Script.Engine import K2_SetTimerDelegate
from Script.Engine import SceneComponent
from Game.FactoryGame.World.Environment.DayNight.BP_Sky_Sphere import BP_Sky_Sphere
from Script.Engine import GetDisplayName
from Script.Engine import Pawn
from Script.Engine import SpawnEmitterAtLocation
from Script.Engine import SpawnEmitterAttached
from Script.Engine import VSize
from Script.Engine import SetComponentTickInterval
from Script.CoreUObject import Rotator
from Script.Engine import Conv_IntToFloat
from Script.Engine import GreaterEqual_IntInt
from Script.Engine import GetPlayerPawn
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import EqualEqual_FloatFloat
from Script.Engine import ETimelineDirection
from Script.Engine import Array_Find
from Script.Engine import Default__KismetArrayLibrary
from Script.FactoryGame import FGProximitySubsystem
from Game.FactoryGame.Character.Player.BP_ProximitySubsystem import ExecuteUbergraph_BP_ProximitySubsystem
from Game.FactoryGame.-Shared.Collections.WeatherSystem.MPC_Weather import MPC_Weather
from Script.Engine import MaterialInstance
from Script.FactoryGame import OnEnteredMapArea
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.Engine import GetAllActorsOfClass
from Script.Engine import EqualEqual_StrStr
from Script.Engine import EObjectTypeQuery
from Script.Engine import LineTraceSingle
from Script.Engine import K2_GetRootComponent
from Script.Engine import Divide_IntInt
from Script.FactoryGame import FGMapArea
from Script.Engine import Default__GameplayStatics
from Script.Engine import BreakRotator
from Script.Engine import WeightedBlendable
from Script.Engine import Default__KismetMaterialLibrary
from Script.Engine import ParticleSystem
from Game.FactoryGame.VFX.Character.Player.Ambient.P_StarFishAmbient_01 import P_StarFishAmbient_01
from Script.Engine import BooleanOR
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.Engine import Normal
from Script.Engine import GetPlayerCameraManager
from Script.Engine import BreakHitResult
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import K2_GetActorRotation
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import MakeRotator
from Game.FactoryGame.Character.Player.BP_ProximitySubsystem import ExecuteUbergraph_BP_ProximitySubsystem.K2Node_Event_newPawn
from Script.Engine import GetVectorParameterValue
from Script.Engine import LineTraceSingleForObjects
from Script.Engine import ParticleSystemComponent
from Script.AkAudio import SetGlobalRTPCValue
from Script.Engine import K2_GetActorLocation
from Script.FactoryGame import OnPawnChanged
from Script.Engine import MapRangeClamped
from Script.Engine import PostProcessVolume
from Script.Engine import PrintString
from Script.Engine import GetActorForwardVector
from Script.CoreUObject import LinearColor
from Script.Engine import RandomFloatInRange

class BP_ProximitySubsystem(FGProximitySubsystem):
    OcclusionInterpAlpha_OcclusionAlpha_393DB8FF4199240D3BAF62908831E857: float
    OcclusionInterpAlpha__Direction_393DB8FF4199240D3BAF62908831E857: uint8
    mCurrentAreaParticle: Ptr[ParticleSystemComponent]
    mCurrentWindSpeed: float
    mIsOccluded: bool
    mWindAreas: List[TSubclassOf[FGMapArea]] = ['/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_DuneDesert_1.Area_DuneDesert_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_DuneDesert_2.Area_DuneDesert_2_C']
    mWindOcclusionTimer: TimerHandle
    IsInDesertDune: bool
    mGlobalPostProcess: Ptr[PostProcessVolume]
    mHeatHaze_Mat: Ptr[MaterialInstance] = Namespace(AssetPath='/Game/FactoryGame/VFX/World/DuneDesert/MI/MI_HeatHaze.MI_HeatHaze')
    mPPI_OutlineColored: Ptr[MaterialInstance] = Namespace(AssetPath='/Game/FactoryGame/PostProcess/Materials/PPI_OutlineColored.PPI_OutlineColored')
    mNumberOfWindOcclusionTraces: int32 = 2
    mWindOcclusionTraceDistance: float = 1500
    mWindOcclusionTraceSpread: float = 0.20000000298023224
    WindSideDir: Vector
    WindDir: Vector
    mOcclusionValuePerTrace: float
    SetOcclusionValue: float = 50
    mRootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    mMapAreaParticleCollection = [{'Areas': ['/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_DuneDesert_1.Area_DuneDesert_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_DuneDesert_2.Area_DuneDesert_2_C'], 'Particle': {'$AssetPath': '/Game/FactoryGame/VFX/Character/Player/Ambient/P_Player_Ambient_SandDunes_01.P_Player_Ambient_SandDunes_01'}}, {'Areas': ['/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_GrassFields_1.Area_GrassFields_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_GrassFields_1.Area_GrassFields_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_GrassFields_2.Area_GrassFields_2_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_GrassFields_3.Area_GrassFields_3_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_LakeForest_1.Area_LakeForest_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_LakeForest_2.Area_LakeForest_2_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_NorthernForest_1.Area_NorthernForest_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_NorthernForest_2.Area_NorthernForest_2_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_TitanForest_1.Area_TitanForest_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_TitanForest_2.Area_TitanForest_2_C'], 'Particle': {'$AssetPath': '/Game/FactoryGame/VFX/Character/Player/Ambient/P_Player_Grassfields_Ambient.P_Player_Grassfields_Ambient'}}, {'Areas': ['/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_AbyssCliffs_1.Area_AbyssCliffs_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_crater_1.Area_crater_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_crater_2.Area_crater_2_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_DesertCanyons_1.Area_DesertCanyons_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_DesertCanyons_2.Area_DesertCanyons_2_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_MazeCanyons_1.Area_MazeCanyons_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_MazeCanyons_2.Area_MazeCanyons_2_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_NoMansLand_1.Area_NoMansLand_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_RedBambooFields_1.Area_RedBambooFields_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_RedBambooFields_2.Area_RedBambooFields_2_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_RedJungle_1.Area_RedJungle_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_RedJungle_2.Area_RedJungle_2_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_RockyDesert_1.Area_RockyDesert_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_RockyDesert_2.Area_RockyDesert_2_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_Savanna_1.Area_Savanna_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_Savanna_2.Area_Savanna_2_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_SouthernForest_1.Area_SouthernForest_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_SouthernForest_2.Area_SouthernForest_2_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_Swamp_1.Area_Swamp_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_Swamp_2.Area_Swamp_2_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_WesternDuneForest_1.Area_WesternDuneForest_1_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_WesternDuneForest_2.Area_WesternDuneForest_2_C', '/Game/FactoryGame/Interface/UI/Minimap/MapAreaPersistenLevel/Area_EasternDuneForest_1.Area_EasternDuneForest_1_C'], 'Particle': {'$AssetPath': '/Game/FactoryGame/World/Environment/Particle/WindDustGreen_01.WindDustGreen_01'}}]
    mMaxNumDecals = 20
    PrimaryActorTick = Namespace(EndTickGroup=0, TickGroup=0, TickInterval=0.30000001192092896, bAllowTickOnDedicatedServer=True, bCanEverTick=True, bStartWithTickEnabled=True, bTickEvenWhenPaused=False)
    RootComponent = Namespace(ObjectClass='/Script/Engine.SceneComponent', ObjectFlags=2883617, ObjectName='RootComponent')
    
    def SetupMapAreaEffect(self, newArea: TSubclassOf[FGMapArea]):
        ExecutionFlow.Push("L385")
        ReturnValue: Ptr[ParticleSystem] = self.GetParticleSystemFromMapArea(newArea)
        localTemplate = ReturnValue
        ExecutionFlow.Push("L167")
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mCurrentAreaParticle)
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        self.mCurrentAreaParticle.Deactivate()
        self.mCurrentAreaParticle = None
        goto(ExecutionFlow.Pop())
        # Label 167
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(localTemplate)
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ReturnValue_1: Ptr[SceneComponent] = self.K2_GetRootComponent()
        ReturnValue_2: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAttached(localTemplate, ReturnValue_1, "None", Vector(0, 0, 0), Rotator::FromPitchYawRoll(0, 0, 0), Vector(1, 1, 1), 3, True, 0)
        self.mCurrentAreaParticle = ReturnValue_2
        goto(ExecutionFlow.Pop())
    

    def OcclusionInterpAlpha__FinishedFunc(self):
        self.ExecuteUbergraph_BP_ProximitySubsystem(7886)
    

    def OcclusionInterpAlpha__UpdateFunc(self):
        self.ExecuteUbergraph_BP_ProximitySubsystem(7669)
    

    def SetWindSpeedEvent(self):
        self.ExecuteUbergraph_BP_ProximitySubsystem(75)
    

    def VirtualWindSystemEvent(self):
        self.ExecuteUbergraph_BP_ProximitySubsystem(370)
    

    def UpdateWindTimer(self):
        self.ExecuteUbergraph_BP_ProximitySubsystem(722)
    

    def WindOcclusionEvent(self):
        self.ExecuteUbergraph_BP_ProximitySubsystem(935)
    

    def WindOcclusionTimer(self):
        self.ExecuteUbergraph_BP_ProximitySubsystem(1051)
    

    def Ambient(self):
        self.ExecuteUbergraph_BP_ProximitySubsystem(6531)
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_BP_ProximitySubsystem(7481)
    

    def OnEnteredMapArea(self):
        ExecuteUbergraph_BP_ProximitySubsystem.K2Node_Event_newArea = newArea #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_ProximitySubsystem(7486)
    

    def OnPawnChanged(self):
        ExecuteUbergraph_BP_ProximitySubsystem.K2Node_Event_newPawn = newPawn #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BP_ProximitySubsystem(7649)
    

    def CalculateWindOcclusionEvent(self):
        self.ExecuteUbergraph_BP_ProximitySubsystem(7674)
    

    def ExecuteUbergraph_BP_ProximitySubsystem(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        Default__AkGameplayStatics.SetGlobalRTPCValue("RTPC_Occlusion", self.OcclusionInterpAlpha_OcclusionAlpha_393DB8FF4199240D3BAF62908831E857, 0)
        goto(ExecutionFlow.Pop())
        ReturnValue: bool = RandomBoolWithWeight(0.6000000238418579)
        ReturnValue_0: float = RandomFloatInRange(10, 20)
        ReturnValue1: float = RandomFloatInRange(15, 30)
        Variable: bool = ReturnValue
        
        switch = {
            False: ReturnValue_0,
            True: ReturnValue1
        }
        ReturnValue_1: float = MapRangeClamped(switch.get(Variable, None), 0, 30, 0, 100)
        Default__AkGameplayStatics.SetGlobalRTPCValue("RTPC_WindSpeedAmplitude", ReturnValue_1, 0)
        self.UpdateWindTimer()
        goto(ExecutionFlow.Pop())
        self.SetWindSpeedEvent()
        goto(ExecutionFlow.Pop())
        # Label 385
        Variable_0: int32 = 0
        
        OutActors = None
        # Label 408
        ReturnValue_2: int32 = len(OutActors)
        ReturnValue_3: bool = Variable_1 <= ReturnValue_2
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable_1
        ExecutionFlow.Push("L648")
        
        OutActors = None
        Item = None
        Item = OutActors[Variable_0]
        self.mGlobalPostProcess = Item.mGlobalPostProcess
        goto(ExecutionFlow.Pop())
        # Label 648
        ReturnValue_4: int32 = Variable_1 + 1
        Variable_1: int32 = ReturnValue_4
        goto('L408')
        ReturnValue2: float = RandomFloatInRange(15, 45)
        OutputDelegate.BindUFunction(self, SetWindSpeedEvent)
        ReturnValue_5: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, ReturnValue2, False)
        goto(ExecutionFlow.Pop())
        # Label 853
        Default__KismetSystemLibrary.PrintString(self, "Hello", True, True, LinearColor(R = 0, G = 0.6600000262260437, B = 1, A = 1), 2)
        goto(ExecutionFlow.Pop())
        OutputDelegate1.BindUFunction(self, WindOcclusionTimer)
        ReturnValue1_0: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate1, 0.10000000149011612, True)
        self.mWindOcclusionTimer = ReturnValue1_0
        goto(ExecutionFlow.Pop())
        ReturnValue_6: LinearColor = Default__KismetMaterialLibrary.GetVectorParameterValue(self, MPC_Weather, "WindDirection")
        self.mOcclusionValuePerTrace = 0
        ReturnValue1_1: Vector = Vector(ReturnValue_6.R, ReturnValue_6.G, 0)
        ReturnValue_7: Vector = Normal(ReturnValue1_1, 9.999999747378752e-05)
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(ReturnValue_7)
        ReturnValue3: float = RandomFloatInRange(-0.05000000074505806, 0.05000000074505806)
        ReturnValue3_0: Vector = Vector(X1, Y1, ReturnValue3)
        self.WindDir = ReturnValue3_0
        ReturnValue1_1 = Vector(ReturnValue_6.R, ReturnValue_6.G, 0)
        ReturnValue_7 = Normal(ReturnValue1_1, 9.999999747378752e-05)
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(ReturnValue_7)
        ReturnValue3 = RandomFloatInRange(-0.05000000074505806, 0.05000000074505806)
        ReturnValue3_0 = Vector(X1, Y1, ReturnValue3)
        
        X2 = None
        Y2 = None
        Z2 = None
        X2, Y2, Z2 = BreakVector(ReturnValue3_0)
        ReturnValue_8: float = Y2 * -1
        ReturnValue4: Vector = Vector(ReturnValue_8, X2, 0)
        self.WindSideDir = ReturnValue4
        Variable_2: int32 = 0
        # Label 1863
        ReturnValue_9: int32 = Divide_IntInt(self.mNumberOfWindOcclusionTraces, 2)
        ReturnValue_10: int32 = ReturnValue_9 - 1
        ReturnValue_11: bool = Variable_2 <= ReturnValue_10
        if not ReturnValue_11:
            goto('L5079')
        ExecutionFlow.Push("L5094")
        ReturnValue1_2: int32 = Variable_2 + 1
        Array2: Const[List[uint8]] = [0]
        ReturnValue_12: Ptr[PlayerCameraManager] = Default__GameplayStatics.GetPlayerCameraManager(self, 0)
        ReturnValue1_3: Vector = ReturnValue_12.K2_GetActorLocation()
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue1_3)
        ReturnValue_13: float = Z + 0.07999999821186066
        ReturnValue2_0: Vector = Vector(X, Y, ReturnValue_13)
        ReturnValue_14: float = ReturnValue1_2 * self.mWindOcclusionTraceSpread
        ReturnValue1_4: Vector = self.WindSideDir * ReturnValue_14
        ReturnValue2_1: Vector = self.WindDir + ReturnValue1_4
        ReturnValue2_2: Vector = Normal(ReturnValue2_1, 9.999999747378752e-05)
        ReturnValue3_1: Vector = ReturnValue2_2 * self.mWindOcclusionTraceDistance
        ReturnValue4_0: Vector = ReturnValue2_0 + ReturnValue3_1
        
        Variable1 = None
        OutHit1 = None
        ReturnValue1_5: bool = Default__KismetSystemLibrary.LineTraceSingleForObjects(self, ReturnValue2_0, ReturnValue4_0, False, 0, True, LinearColor(R = 0, G = 1, B = 0.6550760269165039, A = 1), LinearColor(R = 1, G = 0.3459010124206543, B = 0, A = 1), 1, Ref[Array2], Ref[Variable1], Ref[OutHit1])
        
        OutHit1 = None
        bBlockingHit1 = None
        bInitialOverlap1 = None
        Time1 = None
        Distance1 = None
        Location1 = None
        ImpactPoint1 = None
        Normal1 = None
        ImpactNormal1 = None
        PhysMat1 = None
        HitActor1 = None
        HitComponent1 = None
        HitBoneName1 = None
        HitItem1 = None
        FaceIndex1 = None
        TraceStart1 = None
        TraceEnd1 = None
        Default__GameplayStatics.BreakHitResult(Ref[OutHit1], Ref[bBlockingHit1], Ref[bInitialOverlap1], Ref[Time1], Ref[Distance1], Ref[Location1], Ref[ImpactPoint1], Ref[Normal1], Ref[ImpactNormal1], Ref[PhysMat1], Ref[HitActor1], Ref[HitComponent1], Ref[HitBoneName1], Ref[HitItem1], Ref[FaceIndex1], Ref[TraceStart1], Ref[TraceEnd1])
        ReturnValue1_6: FString = Default__KismetSystemLibrary.GetDisplayName(PhysMat1)
        ReturnValue1_7: bool = Default__KismetStringLibrary.EqualEqual_StrStr(ReturnValue1_6, "PhysMat_Rock")
        if not ReturnValue1_7:
            goto('L5168')
        
        OutHit1 = None
        bBlockingHit1 = None
        bInitialOverlap1 = None
        Time1 = None
        Distance1 = None
        Location1 = None
        ImpactPoint1 = None
        Normal1 = None
        ImpactNormal1 = None
        PhysMat1 = None
        HitActor1 = None
        HitComponent1 = None
        HitBoneName1 = None
        HitItem1 = None
        FaceIndex1 = None
        TraceStart1 = None
        TraceEnd1 = None
        Default__GameplayStatics.BreakHitResult(Ref[OutHit1], Ref[bBlockingHit1], Ref[bInitialOverlap1], Ref[Time1], Ref[Distance1], Ref[Location1], Ref[ImpactPoint1], Ref[Normal1], Ref[ImpactNormal1], Ref[PhysMat1], Ref[HitActor1], Ref[HitComponent1], Ref[HitBoneName1], Ref[HitItem1], Ref[FaceIndex1], Ref[TraceStart1], Ref[TraceEnd1])
        ReturnValue2_3: Vector = Subtract_VectorVector(ImpactPoint1, TraceStart1)
        ReturnValue1_8: float = VSize(ReturnValue2_3)
        ReturnValue1_9: int32 = Divide_IntInt(100, self.mNumberOfWindOcclusionTraces)
        ReturnValue_15: float = Conv_IntToFloat(ReturnValue1_9)
        ReturnValue1_10: float = MapRangeClamped(ReturnValue1_8, 100, 1500, 0, ReturnValue_15)
        ReturnValue3_2: float = self.mOcclusionValuePerTrace + ReturnValue1_10
        self.mOcclusionValuePerTrace = ReturnValue3_2
        # Label 3541
        ReturnValue1_2 = Variable_2 + 1
        ReturnValue_12 = Default__GameplayStatics.GetPlayerCameraManager(self, 0)
        ReturnValue1_3 = ReturnValue_12.K2_GetActorLocation()
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue1_3)
        ReturnValue_13 = Z + 0.07999999821186066
        ReturnValue2_0 = Vector(X, Y, ReturnValue_13)
        ReturnValue_14 = ReturnValue1_2 * self.mWindOcclusionTraceSpread
        Array3: Const[List[uint8]] = [0]
        ReturnValue1_4 = self.WindSideDir * ReturnValue_14
        ReturnValue_16: Vector = Subtract_VectorVector(self.WindDir, ReturnValue1_4)
        ReturnValue1_11: Vector = Normal(ReturnValue_16, 9.999999747378752e-05)
        ReturnValue2_4: Vector = ReturnValue1_11 * self.mWindOcclusionTraceDistance
        ReturnValue3_3: Vector = ReturnValue2_0 + ReturnValue2_4
        
        Variable_3 = None
        OutHit = None
        ReturnValue_17: bool = Default__KismetSystemLibrary.LineTraceSingleForObjects(self, ReturnValue2_0, ReturnValue3_3, False, 0, True, LinearColor(R = 0.40088599920272827, G = 0, B = 1, A = 1), LinearColor(R = 1, G = 0, B = 0.05176699906587601, A = 1), 1, Ref[Array3], Ref[Variable_3], Ref[OutHit])
        
        OutHit = None
        bBlockingHit = None
        bInitialOverlap = None
        Time = None
        Distance = None
        Location = None
        ImpactPoint = None
        Normal = None
        ImpactNormal = None
        PhysMat = None
        HitActor = None
        HitComponent = None
        HitBoneName = None
        HitItem = None
        FaceIndex = None
        TraceStart = None
        TraceEnd = None
        Default__GameplayStatics.BreakHitResult(Ref[OutHit], Ref[bBlockingHit], Ref[bInitialOverlap], Ref[Time], Ref[Distance], Ref[Location], Ref[ImpactPoint], Ref[Normal], Ref[ImpactNormal], Ref[PhysMat], Ref[HitActor], Ref[HitComponent], Ref[HitBoneName], Ref[HitItem], Ref[FaceIndex], Ref[TraceStart], Ref[TraceEnd])
        ReturnValue_18: FString = Default__KismetSystemLibrary.GetDisplayName(PhysMat)
        ReturnValue_19: bool = Default__KismetStringLibrary.EqualEqual_StrStr(ReturnValue_18, "PhysMat_Rock")
        if not ReturnValue_19:
            goto('L5386')
        
        OutHit = None
        bBlockingHit = None
        bInitialOverlap = None
        Time = None
        Distance = None
        Location = None
        ImpactPoint = None
        Normal = None
        ImpactNormal = None
        PhysMat = None
        HitActor = None
        HitComponent = None
        HitBoneName = None
        HitItem = None
        FaceIndex = None
        TraceStart = None
        TraceEnd = None
        Default__GameplayStatics.BreakHitResult(Ref[OutHit], Ref[bBlockingHit], Ref[bInitialOverlap], Ref[Time], Ref[Distance], Ref[Location], Ref[ImpactPoint], Ref[Normal], Ref[ImpactNormal], Ref[PhysMat], Ref[HitActor], Ref[HitComponent], Ref[HitBoneName], Ref[HitItem], Ref[FaceIndex], Ref[TraceStart], Ref[TraceEnd])
        ReturnValue1_12: Vector = Subtract_VectorVector(ImpactPoint, TraceStart)
        ReturnValue_20: float = VSize(ReturnValue1_12)
        ReturnValue3_4: int32 = Divide_IntInt(100, self.mNumberOfWindOcclusionTraces)
        ReturnValue2_5: float = Conv_IntToFloat(ReturnValue3_4)
        ReturnValue3_5: float = MapRangeClamped(ReturnValue_20, 100, 1500, 0, ReturnValue2_5)
        ReturnValue1_13: float = self.mOcclusionValuePerTrace + ReturnValue3_5
        self.mOcclusionValuePerTrace = ReturnValue1_13
        goto(ExecutionFlow.Pop())
        # Label 5079
        self.CalculateWindOcclusionEvent()
        goto(ExecutionFlow.Pop())
        # Label 5094
        ReturnValue2_6: int32 = Variable_2 + 1
        Variable_2 = ReturnValue2_6
        goto('L1863')
        # Label 5168
        ReturnValue2_7: int32 = Divide_IntInt(100, self.mNumberOfWindOcclusionTraces)
        ReturnValue1_14: float = Conv_IntToFloat(ReturnValue2_7)
        ReturnValue2_8: float = MapRangeClamped(self.mWindOcclusionTraceDistance, 100, 1500, 0, ReturnValue1_14)
        ReturnValue4_1: float = self.mOcclusionValuePerTrace + ReturnValue2_8
        self.mOcclusionValuePerTrace = ReturnValue4_1
        goto('L3541')
        # Label 5386
        ReturnValue4_2: int32 = Divide_IntInt(100, self.mNumberOfWindOcclusionTraces)
        ReturnValue3_6: float = Conv_IntToFloat(ReturnValue4_2)
        ReturnValue4_3: float = MapRangeClamped(self.mWindOcclusionTraceDistance, 100, 1500, 0, ReturnValue3_6)
        ReturnValue2_9: float = self.mOcclusionValuePerTrace + ReturnValue4_3
        self.mOcclusionValuePerTrace = ReturnValue2_9
        goto(ExecutionFlow.Pop())
        # Label 5600
        self.OcclusionInterpAlpha.SetComponentTickInterval(0.10000000149011612)
        OutActors: List[Ptr[BP_Sky_Sphere]] = []
        
        Default__GameplayStatics.GetAllActorsOfClass(self, BP_Sky_Sphere, Ref[OutActors])
        Variable_1 = 0
        goto('L385')
        # Label 5727
        self.IsInDesertDune = True
        ReturnValue_21: bool = Default__KismetSystemLibrary.IsValid(self.mGlobalPostProcess)
        if not ReturnValue_21:
           goto(ExecutionFlow.Pop())
        WeightedBlendable.Weight = 1
        WeightedBlendable.Object = self.mHeatHaze_Mat
        WeightedBlendable2.Weight = 1
        WeightedBlendable2.Object = self.mPPI_OutlineColored
        Array1: List[WeightedBlendable] = [WeightedBlendable2, WeightedBlendable]
        WeightedBlendables1.Array = Array1
        self.mGlobalPostProcess.Settings.WeightedBlendables = WeightedBlendables1
        self.mGlobalPostProcess.Settings = self.mGlobalPostProcess.Settings
        goto(ExecutionFlow.Pop())
        # Label 6114
        self.IsInDesertDune = False
        ReturnValue1_15: bool = Default__KismetSystemLibrary.IsValid(self.mGlobalPostProcess)
        if not ReturnValue1_15:
           goto(ExecutionFlow.Pop())
        WeightedBlendable1.Weight = 0
        WeightedBlendable1.Object = self.mHeatHaze_Mat
        WeightedBlendable2.Weight = 1
        WeightedBlendable2.Object = self.mPPI_OutlineColored
        Array: List[WeightedBlendable] = [WeightedBlendable2, WeightedBlendable1]
        WeightedBlendables.Array = Array
        self.mGlobalPostProcess.Settings.WeightedBlendables = WeightedBlendables
        self.mGlobalPostProcess.Settings = self.mGlobalPostProcess.Settings
        goto(ExecutionFlow.Pop())
        # Label 6501
        if not self.IsInDesertDune:
            goto('L5727')
        goto(ExecutionFlow.Pop())
        # Label 6516
        if not self.IsInDesertDune:
           goto(ExecutionFlow.Pop())
        goto('L6114')
        ReturnValue_22: Vector = Vector(0, 0, -2155)
        ReturnValue_23: Ptr[Pawn] = Default__GameplayStatics.GetPlayerPawn(self, 0)
        ReturnValue_24: Vector = ReturnValue_23.K2_GetActorLocation()
        ReturnValue_25: Vector = ReturnValue_23.GetActorForwardVector()
        ReturnValue_26: Vector = ReturnValue_25 * 25
        ReturnValue_27: Vector = ReturnValue_24 + ReturnValue_26
        ReturnValue1_16: Vector = ReturnValue_27 + ReturnValue_22
        
        Variable2 = None
        OutHit = None
        ReturnValue_28: bool = Default__KismetSystemLibrary.LineTraceSingle(self, ReturnValue_27, ReturnValue1_16, 0, False, 0, True, LinearColor(R = 1, G = 0, B = 0, A = 1), LinearColor(R = 0, G = 1, B = 0, A = 1), 5, Ref[Variable2], Ref[OutHit])
        ReturnValue_23 = Default__GameplayStatics.GetPlayerPawn(self, 0)
        ReturnValue_29: Rotator = ReturnValue_23.K2_GetActorRotation()
        
        Roll = None
        Pitch = None
        Yaw = None
        BreakRotator(ReturnValue_29, Ref[Roll], Ref[Pitch], Ref[Yaw])
        ReturnValue_30: Rotator = MakeRotator(0, 0, Yaw)
        
        OutHit = None
        bBlockingHit2 = None
        bInitialOverlap2 = None
        Time2 = None
        Distance2 = None
        Location2 = None
        ImpactPoint2 = None
        Normal2 = None
        ImpactNormal2 = None
        PhysMat2 = None
        HitActor2 = None
        HitComponent2 = None
        HitBoneName2 = None
        HitItem2 = None
        FaceIndex2 = None
        TraceStart2 = None
        TraceEnd2 = None
        Default__GameplayStatics.BreakHitResult(Ref[OutHit], Ref[bBlockingHit2], Ref[bInitialOverlap2], Ref[Time2], Ref[Distance2], Ref[Location2], Ref[ImpactPoint2], Ref[Normal2], Ref[ImpactNormal2], Ref[PhysMat2], Ref[HitActor2], Ref[HitComponent2], Ref[HitBoneName2], Ref[HitItem2], Ref[FaceIndex2], Ref[TraceStart2], Ref[TraceEnd2])
        ReturnValue_31: Ptr[ParticleSystemComponent] = Default__GameplayStatics.SpawnEmitterAtLocation(self, P_StarFishAmbient_01, Location2, ReturnValue_30, Vector(1, 1, 1), True, 0)
        goto('L853')
        goto('L5600')
        self.OnEnteredMapArea(newArea)
        self.SetupMapAreaEffect(newArea)
        
        newArea = None
        ReturnValue_32: int32 = Default__KismetArrayLibrary.Array_Find(Ref[self.mWindAreas], Ref[newArea])
        ReturnValue_33: bool = GreaterEqual_IntInt(ReturnValue_32, 0)
        if not ReturnValue_33:
            goto('L6516')
        goto('L6501')
        self.OnPawnChanged(newPawn)
        goto(ExecutionFlow.Pop())
        goto('L15')
        ReturnValue_34: bool = EqualEqual_FloatFloat(self.SetOcclusionValue, 0)
        ReturnValue1_17: bool = EqualEqual_FloatFloat(self.SetOcclusionValue, 100)
        ReturnValue_35: bool = BooleanOR(ReturnValue_34, ReturnValue1_17)
        if not ReturnValue_35:
            goto('L7822')
        # Label 7794
        self.SetOcclusionValue = self.mOcclusionValuePerTrace
        goto(ExecutionFlow.Pop())
        # Label 7822
        Default__AkGameplayStatics.SetGlobalRTPCValue("RTPC_Occlusion", self.mOcclusionValuePerTrace, 0)
        goto('L7794')
        goto(ExecutionFlow.Pop())
    
