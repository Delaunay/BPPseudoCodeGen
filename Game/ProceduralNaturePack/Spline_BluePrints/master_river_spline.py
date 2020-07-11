
from codegen.ue4_stub import *

from Script.Engine import SetScalarParameterValue
from Script.Engine import AddComponent
from Script.CoreUObject import Rotator
from Script.Engine import K2_SetText
from Script.Engine import MaterialInstanceDynamic
from Script.Engine import GetNumberOfSplinePoints
from Script.Engine import SetTranslucentSortPriority
from Script.Engine import ReceiveBeginPlay
from Script.Engine import SplineMeshComponent
from Script.FactoryGame import FGSoundSplineComponent
from Script.Engine import GetLocationAndTangentAtSplinePoint
from Script.Engine import SetHiddenInGame
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import K2_AttachTo
from Game.ProceduralNaturePack.Spline_BluePrints.data.River_Scale_Data import River_Scale_Data
from Game.FactoryGame.World.Environment.Landscape.Layer.LayerInfo.WetSand_LayerInfo import WetSand_LayerInfo
from Script.Engine import IsValid
from Script.Engine import TextRenderComponent
from Game.ProceduralNaturePack.Spline_BluePrints.master_river_spline import ExecuteUbergraph_master_river_spline
from Script.Engine import EObjectTypeQuery
from Script.Engine import K2_AddActorWorldOffset
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.Engine import SetStartAndEnd
from Script.Engine import Default__GameplayStatics
from Script.AkAudio import PostAssociatedAkEvent
from Script.Landscape import LandscapeProxy
from Script.Engine import Subtract_VectorVector
from Script.CoreUObject import Vector
from Script.Engine import BreakHitResult
from Script.Engine import MaterialInterface
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import GetSplineLength
from Script.AkAudio import Default__AkGameplayStatics
from Script.Engine import DrawDebugSphere
from Script.Engine import Conv_IntToString
from Script.Engine import LineTraceSingleForObjects
from Script.Engine import MakeTransform
from Script.Engine import SetStartScale
from Script.Engine import SetEndScale
from Script.Engine import GetDistanceAlongSplineAtSplinePoint
from Script.Engine import SelectColor
from Script.Engine import GetLocationAtSplinePoint
from Script.AkAudio import IsEditor
from Script.CoreUObject import Vector2D
from Script.Engine import K2_AttachToComponent
from Script.Landscape import EditorApplySpline
from Script.Engine import MakeRotFromX
from Script.Landscape import LandscapeLayerInfoObject
from Script.FactoryGame import FGRiverSpline
from Script.Engine import SetLocationAtSplinePoint
from Script.CoreUObject import Transform
from Script.Engine import MeshComponent
from Script.Engine import StaticMesh
from Script.CoreUObject import LinearColor
from Script.FactoryGame import SetEmitterInterval

class master_river_spline(FGRiverSpline):
    MeshComponent: Ptr[MeshComponent]
    Draw_Spline_Point_Numbers: bool
    Dynamic_Material: Ptr[MaterialInstanceDynamic]
    Lastscale_Value: Vector2D = Namespace(X=1, Y=1)
    Firstscale_Value: Vector2D = Namespace(X=1, Y=1)
    Index_Number: int32
    SplineMesh1: Ptr[SplineMeshComponent]
    Spline_Start: float
    SplineEnd: float
    SplineLength: float
    River_Speed_Minimum: float = 1
    Water_Tiling: float = 2.25
    Water_Tiling_Horizontal: float = 1
    Tesselation_Scale: float = 1
    Tesselation_Fade_Distance: float = 2
    SplineMesh: Ptr[StaticMesh] = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Water/Mesh/River_Plane.River_Plane')
    Choose_Material: Ptr[MaterialInterface] = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Water/Material/River_Inst_01.River_Inst_01')
    GetNumSplinePoints: int32
    River_Scale_Spline_Points: List[River_Scale_Data] = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
    SplineMesh2: Ptr[SplineMeshComponent]
    Spline_Start2: float
    SplineEnd2: float
    Firstscale_Value2: Vector2D
    Last_Index: int32
    Start_Foam: float
    End_Foam: float
    Spline_Point_Number: FString
    mAudioSpline: Ptr[FGSoundSplineComponent]
    SnapOffset: float = 50
    LandscapeProxy: Ptr[LandscapeProxy]
    WidthStart: float = 200
    Width_End: float = 200
    TerrainOffset: float
    Falloff: float = 200
    bShouldPaintWetSand: bool = True
    mEmitterInterval = 600
    mShouldHaveAudio = True
    
    def ModifyTerrain(self):
        ExecutionFlow.Push("L493")
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.LandscapeProxy)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L401")
        ReturnValue_0: Vector = Vector(0, 0, self.TerrainOffset)
        ReturnValue_1: Vector = ReturnValue_0 * -1
        
        SweepHitResult1 = None
        self.K2_AddActorWorldOffset(ReturnValue_1, False, False, Ref[SweepHitResult1])
        Variable: Ptr[LandscapeLayerInfoObject] = None
        Variable1: Ptr[LandscapeLayerInfoObject] = WetSand_LayerInfo
        Variable_0: bool = self.bShouldPaintWetSand
        
        switch = {
            False: Variable,
            True: Variable1
        }
        self.LandscapeProxy.EditorApplySpline(self.Spline1, self.WidthStart, self.Width_End, self.Falloff, self.Falloff, 0, 0, 20, True, True, switch.get(Variable_0, None))
        goto(ExecutionFlow.Pop())
        # Label 401
        ReturnValue_0 = Vector(0, 0, self.TerrainOffset)
        
        SweepHitResult = None
        self.K2_AddActorWorldOffset(ReturnValue_0, False, False, Ref[SweepHitResult])
        goto(ExecutionFlow.Pop())
    

    def CheckPointsHeight(self):
        ExecutionFlow.Push("L778")
        ReturnValue: bool = Default__AkGameplayStatics.IsEditor()
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        LastHeight = 300000000
        # Label 80
        Variable: int32 = 0
        # Label 103
        ReturnValue_0: int32 = self.Spline1.GetNumberOfSplinePoints()
        ReturnValue_1: int32 = ReturnValue_0 - 1
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L704")
        ReturnValue_3: Vector = self.Spline1.GetLocationAtSplinePoint(Variable, 1)
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_3)
        ReturnValue_4: bool = Z <= LastHeight
        ReturnValue_5: LinearColor = SelectColor(LinearColor(R = 0, G = 1, B = 0, A = 1), LinearColor(R = 1, G = 0, B = 0, A = 1), ReturnValue_4)
        Default__KismetSystemLibrary.DrawDebugSphere(self, ReturnValue_3, 50, 12, ReturnValue_5, 10, 5)
        ReturnValue_3 = self.Spline1.GetLocationAtSplinePoint(Variable, 1)
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(ReturnValue_3)
        LastHeight = Z
        goto(ExecutionFlow.Pop())
        # Label 704
        ReturnValue_6: int32 = Variable + 1
        Variable = ReturnValue_6
        goto('L103')
    

    def SnapToTerrain(self):
        ExecutionFlow.Push("L1115")
        ReturnValue: bool = Default__AkGameplayStatics.IsEditor()
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        # Label 80
        ReturnValue_0: int32 = self.Spline1.GetNumberOfSplinePoints()
        ReturnValue_1: int32 = ReturnValue_0 - 1
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1041")
        Array: Const[List[uint8]] = [0]
        ReturnValue_3: Vector = self.Spline1.GetLocationAtSplinePoint(Variable, 1)
        ReturnValue_4: Vector = Subtract_VectorVector(ReturnValue_3, Vector(0, 0, 50000))
        
        Variable_0 = None
        OutHit = None
        ReturnValue_5: bool = Default__KismetSystemLibrary.LineTraceSingleForObjects(self, ReturnValue_3, ReturnValue_4, False, 2, True, LinearColor(R = 1, G = 0, B = 0, A = 1), LinearColor(R = 0, G = 1, B = 0, A = 1), 2, Ref[Array], Ref[Variable_0], Ref[OutHit])
        
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
        if not bBlockingHit:
           goto(ExecutionFlow.Pop())
        ReturnValue_6: Vector = Vector(0, 0, self.SnapOffset)
        
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
        ReturnValue_7: Vector = Location + ReturnValue_6
        
        self.Spline1.SetLocationAtSplinePoint(Variable, 1, True, Ref[ReturnValue_7])
        goto(ExecutionFlow.Pop())
        # Label 1041
        ReturnValue_8: int32 = Variable + 1
        Variable = ReturnValue_8
        goto('L80')
    

    def UserConstructionScript(self):
        ExecutionFlow.Push("L4776")
        scale: float = 1
        scale_0: float = 1
        ExecutionFlow.Push("L544")
        ReturnValue: int32 = self.Spline1.GetNumberOfSplinePoints()
        self.GetNumSplinePoints = ReturnValue
        ReturnValue = self.Spline1.GetNumberOfSplinePoints()
        ReturnValue1: int32 = ReturnValue - 2
        self.Last_Index = ReturnValue1
        Variable: int32 = 0
        # Label 275
        ReturnValue_0: bool = Variable <= self.Last_Index
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L956")
        ExecutionFlow.Push("L1030")
        self.Index_Number = Variable
        
        # Label 360
        ReturnValue_1: int32 = len(self.River_Scale_Spline_Points)
        ReturnValue_2: bool = ReturnValue_1 <= self.GetNumSplinePoints
        if not ReturnValue_2:
            goto('L1797')
        
        Variable2 = None
        ReturnValue_3: int32 = self.River_Scale_Spline_Points.append(Variable2)
        goto('L360')
        # Label 544
        ReturnValue_4: bool = Default__KismetSystemLibrary.IsValid(self.mAudioEvent)
        ReturnValue_5: bool = self.mShouldHaveAudio and ReturnValue_4
        if not ReturnValue_5:
           goto(ExecutionFlow.Pop())
        Variable_0: Const[Transform] = Transform(Rotator(0, 0, 0, 1), Vector(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_6: Ptr[FGSoundSplineComponent] = self.AddComponent("NODE_AddFGSoundSplineComponent-1", True, self, Ref[Variable_0])
        ReturnValue_7: bool = ReturnValue_6.K2_AttachToComponent(self.Spline1, "None", 0, 0, 0, True)
        ReturnValue_6.SetAutoActivate(False)
        ReturnValue_6.SetEmitterInterval(self.mEmitterInterval)
        ReturnValue_6.AkAudioEvent = self.mAudioEvent
        self.mAudioSpline = ReturnValue_6
        goto(ExecutionFlow.Pop())
        # Label 956
        ReturnValue3: int32 = Variable + 1
        Variable = ReturnValue3
        goto('L275')
        # Label 1030
        if not self.Draw_Spline_Point_Numbers:
           goto(ExecutionFlow.Pop())
        ReturnValue_8: FString = Default__KismetStringLibrary.Conv_IntToString(self.Index_Number)
        self.Spline_Point_Number = ReturnValue_8
        Variable1: int32 = 0
        # Label 1149
        ReturnValue_9: int32 = self.GetNumSplinePoints - 1
        ReturnValue1_0: bool = Variable1 <= ReturnValue_9
        if not ReturnValue1_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1723")
        
        Location2 = None
        Tangent2 = None
        self.Spline1.GetLocationAndTangentAtSplinePoint(self.Index_Number, 0, Ref[Location2], Ref[Tangent2])
        
        Tangent2 = None
        ReturnValue_10: Rotator = MakeRotFromX(Ref[Tangent2])
        
        X2 = None
        Y2 = None
        Z2 = None
        X2, Y2, Z2 = BreakVector(Location2)
        ReturnValue2: float = Z2 + 20
        ReturnValue_11: Vector = Vector(X2, Y2, ReturnValue2)
        ReturnValue_12: Transform = MakeTransform(ReturnValue_11, ReturnValue_10, Vector(1, 1, 1))
        
        ReturnValue2_0: Ptr[TextRenderComponent] = self.AddComponent("NODE_AddTextRenderComponent-0", False, self, Ref[ReturnValue_12])
        ReturnValue_13: FText = Default__KismetTextLibrary.Conv_StringToText(self.Spline_Point_Number)
        
        ReturnValue2_0.K2_SetText(Ref[ReturnValue_13])
        ReturnValue2_0.SetHiddenInGame(True, False)
        goto(ExecutionFlow.Pop())
        # Label 1723
        ReturnValue4: int32 = Variable1 + 1
        Variable1 = ReturnValue4
        goto('L1149')
        
        # Label 1797
        ReturnValue_1 = len(self.River_Scale_Spline_Points)
        ReturnValue_14: bool = ReturnValue_1 > self.GetNumSplinePoints
        if not ReturnValue_14:
            goto('L2022')
        
        ReturnValue_15: int32 = len(self.River_Scale_Spline_Points) - 1
        
        self.River_Scale_Spline_Points.remove(ReturnValue_15)
        goto('L360')
        # Label 2022
        Variable1_0: Const[Transform] = Transform(Rotator(0, 0, 0, 1), Vector(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue1_1: Ptr[SplineMeshComponent] = self.AddComponent("NODE_AddSplineMeshComponent-0", False, self, Ref[Variable1_0])
        ReturnValue1_1.SetCollisionResponseToChannel(6, 1)
        Index: int32 = self.Index_Number
        ReturnValue1_2: int32 = self.Index_Number + 1
        Index_0: int32 = ReturnValue1_2
        self.SplineMesh1 = ReturnValue1_1
        self.SplineMesh1.SetTranslucentSortPriority(1)
        
        Item = None
        Item = self.River_Scale_Spline_Points[Index]
        scale = Item.River_Scale_12_AE0379524F575EEEF2B664BD68F148B6
        
        Item1 = None
        Item1 = self.River_Scale_Spline_Points[Index_0]
        scale_0 = Item1.River_Scale_12_AE0379524F575EEEF2B664BD68F148B6
        
        Item = None
        Item = self.River_Scale_Spline_Points[Index]
        ReturnValue_16: bool = Item.River_Scale_12_AE0379524F575EEEF2B664BD68F148B6 <= 0
        if not ReturnValue_16:
            goto('L4520')
        # Label 2623
        ReturnValue_17: Vector2D = Vector2D(scale, scale)
        self.SplineMesh1.SetStartScale(ReturnValue_17, True)
        
        Item1 = None
        # Label 2711
        Item1 = self.River_Scale_Spline_Points[Index_0]
        ReturnValue1_3: bool = Item1.River_Scale_12_AE0379524F575EEEF2B664BD68F148B6 <= 0
        if not ReturnValue1_3:
            goto('L4264')
        # Label 2827
        ReturnValue1_4: Vector2D = Vector2D(scale_0, scale_0)
        self.SplineMesh1.SetEndScale(ReturnValue1_4, True)
        # Label 2915
        ReturnValue_18: bool = self.SplineMesh1.SetStaticMesh(self.SplineMesh)
        ReturnValue_19: float = self.Spline1.GetSplineLength()
        ReturnValue1_5: float = self.Spline1.GetDistanceAlongSplineAtSplinePoint(self.Index_Number)
        ReturnValue1_6: float = ReturnValue_19 - ReturnValue1_5
        self.Spline_Start = ReturnValue1_6
        ReturnValue_20: int32 = self.Index_Number + 1
        ReturnValue_19 = self.Spline1.GetSplineLength()
        ReturnValue_21: float = self.Spline1.GetDistanceAlongSplineAtSplinePoint(ReturnValue_20)
        ReturnValue_22: float = ReturnValue_19 - ReturnValue_21
        self.SplineEnd = ReturnValue_22
        ReturnValue_19 = self.Spline1.GetSplineLength()
        self.SplineLength = ReturnValue_19
        
        Location = None
        Tangent = None
        self.Spline1.GetLocationAndTangentAtSplinePoint(self.Index_Number, 0, Ref[Location], Ref[Tangent])
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(Tangent)
        self.Start_Foam = Z
        ReturnValue2_1: int32 = self.Index_Number + 1
        
        Location1 = None
        Tangent1 = None
        self.Spline1.GetLocationAndTangentAtSplinePoint(ReturnValue2_1, 0, Ref[Location1], Ref[Tangent1])
        
        X1 = None
        Y1 = None
        Z1 = None
        X1, Y1, Z1 = BreakVector(Tangent1)
        self.End_Foam = Z1
        ReturnValue_23: bool = self.SplineMesh1.K2_AttachTo(self.spline_mesh, "None", 0, True)
        
        Location = None
        Tangent = None
        self.Spline1.GetLocationAndTangentAtSplinePoint(self.Index_Number, 0, Ref[Location], Ref[Tangent])
        ReturnValue2_1 = self.Index_Number + 1
        
        Location1 = None
        Tangent1 = None
        self.Spline1.GetLocationAndTangentAtSplinePoint(ReturnValue2_1, 0, Ref[Location1], Ref[Tangent1])
        self.SplineMesh1.SetStartAndEnd(Location, Tangent, Location1, Tangent1, True)
        ReturnValue_24: Ptr[MaterialInstanceDynamic] = self.SplineMesh1.CreateDynamicMaterialInstance(0, self.Choose_Material, "None")
        self.Dynamic_Material = ReturnValue_24
        ReturnValue_24.SetScalarParameterValue("Start", self.Spline_Start)
        ReturnValue_24.SetScalarParameterValue("End", self.SplineEnd)
        goto(ExecutionFlow.Pop())
        
        Item1 = None
        # Label 4264
        Item1 = self.River_Scale_Spline_Points[Index_0]
        ReturnValue1_7: bool = Item1.River_Scale_12_AE0379524F575EEEF2B664BD68F148B6 > 0
        if not ReturnValue1_7:
            goto('L4385')
        goto('L2827')
        # Label 4385
        ReturnValue_25: float = scale_0 + 1
        ReturnValue2_2: Vector2D = Vector2D(ReturnValue_25, ReturnValue_25)
        self.SplineMesh1.SetEndScale(ReturnValue2_2, True)
        goto('L2915')
        
        Item = None
        # Label 4520
        Item = self.River_Scale_Spline_Points[Index]
        ReturnValue_26: bool = Item.River_Scale_12_AE0379524F575EEEF2B664BD68F148B6 > 0
        if not ReturnValue_26:
            goto('L4641')
        goto('L2623')
        # Label 4641
        ReturnValue1_8: float = scale + 1
        ReturnValue3_0: Vector2D = Vector2D(ReturnValue1_8, ReturnValue1_8)
        self.SplineMesh1.SetStartScale(ReturnValue3_0, True)
        goto('L2711')
    

    def ReceiveBeginPlay(self):
        self.ExecuteUbergraph_master_river_spline(107)
    

    def ExecuteUbergraph_master_river_spline(self):
        # Label 10
        ReturnValue: int32 = self.mAudioSpline.PostAssociatedAkEvent()
        # End
        # Label 65
        self.mAudioSpline.Activate(False)
        goto('L10')
        self.ReceiveBeginPlay()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mAudioEvent)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(self.mAudioSpline)
        ReturnValue_1: bool = self.mShouldHaveAudio and ReturnValue_0
        ReturnValue1_0: bool = ReturnValue_1 and ReturnValue1
        if not ReturnValue1_0:
            goto('L314')
        goto('L65')
    
