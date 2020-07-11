
from codegen.ue4_stub import *

from Script.Engine import SetEndRoll
from Script.Engine import AddComponent
from Script.CoreUObject import Rotator
from Script.Engine import K2_SetText
from Script.Engine import GetNumberOfSplinePoints
from Script.Engine import SplineMeshComponent
from Script.Engine import GetLocationAndTangentAtSplinePoint
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.World.Environment.Rock.CaveFloor.CaveData import CaveData
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import MaterialInstance
from Script.Engine import SetStartRoll
from Script.Engine import IsValid
from Script.Engine import TextRenderComponent
from Script.Engine import EqualEqual_IntInt
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Conv_StringToText
from Script.Engine import SetStartAndEnd
from Script.Engine import Conv_VectorToRotator
from Script.CoreUObject import Vector
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import Conv_IntToString
from Script.Engine import MakeTransform
from Script.Engine import SetStartScale
from Script.Engine import SetEndScale
from Script.Engine import Actor
from Script.Engine import Multiply_VectorInt
from Script.CoreUObject import Vector2D
from Script.CoreUObject import Transform
from Script.Engine import StaticMesh

class BP_CaveFloor(Actor):
    mSplineMaterial: Ptr[MaterialInstance] = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Rock/CaveFloor/Material/CaveFloor_Inst.CaveFloor_Inst')
    NumberOfSplinePoints: int32
    CaveDataArray: List[CaveData]
    mCaveMesh: Ptr[StaticMesh] = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Rock/CaveFloor/Mesh/CaveTunnel_01.CaveTunnel_01')
    CaveMeshDefaults: CaveData
    mEntranceMesh: Ptr[StaticMesh] = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Rock/CaveFloor/Mesh/CaveEntrance_01.CaveEntrance_01')
    mExitMesh: Ptr[StaticMesh] = Namespace(AssetPath='/Game/FactoryGame/World/Environment/Rock/CaveFloor/Mesh/CaveExit_01.CaveExit_01')
    DrawCavePointNumbers: bool = True
    CurrentCavePoint: FString
    mSwitchEntrenceAndExit: bool
    mEnableCollision: bool = True
    
    def GetEntrenceAndExitIndex(self):
        Variable: int32 = 0
        Variable1: int32 = 0
        
        ReturnValue: int32 = len(self.CaveDataArray) - 1
        
        ReturnValue1: int32 = len(self.CaveDataArray) - 1
        ReturnValue_0: int32 = ReturnValue - 1
        ReturnValue1_0: int32 = ReturnValue1 - 1
        Variable1_0: bool = self.mSwitchEntrenceAndExit
        Variable_0: bool = self.mSwitchEntrenceAndExit
        
        switch = {
            False: Variable1,
            True: ReturnValue1_0
        }
        entrence = switch.get(Variable1_0, None)
        
        switch_0 = {
            False: ReturnValue_0,
            True: Variable
        }
        Exit = switch_0.get(Variable_0, None)
    

    def GetStaticMeshForIndex(self, index: int32):
        ExecutionFlow.Push("L257")
        index: int32 = index_0
        ExecutionFlow.Push("L141")
        
        entrence = None
        exit = None
        self.GetEntrenceAndExitIndex(Ref[entrence], Ref[exit])
        ReturnValue: bool = EqualEqual_IntInt(entrence, index)
        if not ReturnValue:
            goto('L165')
        staticMesh: Ptr[StaticMesh] = self.mEntranceMesh
        goto(ExecutionFlow.Pop())
        # Label 141
        NewParam = staticMesh
        # End
        # Label 165
        ReturnValue1: bool = EqualEqual_IntInt(exit, index)
        if not ReturnValue1:
            goto('L237')
        staticMesh = self.mExitMesh
        goto(ExecutionFlow.Pop())
        # Label 237
        staticMesh = self.mCaveMesh
        goto(ExecutionFlow.Pop())
    

    def BuildCaveElement(self):
        ExecutionFlow.Push("L1844")
        Variable: int32 = 0
        # Label 28
        ReturnValue: int32 = self.NumberOfSplinePoints - 2
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1067")
        CurrentLoopIndex: int32 = Variable
        ReturnValue1: int32 = CurrentLoopIndex + 1
        NextLoopIndex: int32 = ReturnValue1
        ExecutionFlow.Push("L1141")
        
        Location1 = None
        Tangent1 = None
        self.Spline.GetLocationAndTangentAtSplinePoint(CurrentLoopIndex, 0, Ref[Location1], Ref[Tangent1])
        StartLocation: Vector = Location1
        
        Location1 = None
        Tangent1 = None
        self.Spline.GetLocationAndTangentAtSplinePoint(CurrentLoopIndex, 0, Ref[Location1], Ref[Tangent1])
        StartTangent: Vector = Tangent1
        
        Location = None
        Tangent = None
        self.Spline.GetLocationAndTangentAtSplinePoint(NextLoopIndex, 0, Ref[Location], Ref[Tangent])
        EndLocation: Vector = Location
        
        Location = None
        Tangent = None
        self.Spline.GetLocationAndTangentAtSplinePoint(NextLoopIndex, 0, Ref[Location], Ref[Tangent])
        EndTangent: Vector = Tangent
        
        Item1 = None
        Item1 = self.CaveDataArray[CurrentLoopIndex]
        StartRoll: float = Item1.CaveBank_9_2E244F454EFB45D21BDAB0A2F52AAF65
        
        Item1 = None
        Item1 = self.CaveDataArray[CurrentLoopIndex]
        ReturnValue1_0: Vector2D = Vector2D(Item1.CaveWidth_10_21A92FE2432BB92C0A0F739941EC76CC, Item1.CaveHeight_12_F58A294D4ED9A50923132BB6156E620B)
        StartScale: Vector2D = ReturnValue1_0
        
        Item = None
        Item = self.CaveDataArray[NextLoopIndex]
        EndRoll: float = Item.CaveBank_9_2E244F454EFB45D21BDAB0A2F52AAF65
        
        Item = None
        Item = self.CaveDataArray[NextLoopIndex]
        ReturnValue_1: Vector2D = Vector2D(Item.CaveWidth_10_21A92FE2432BB92C0A0F739941EC76CC, Item.CaveHeight_12_F58A294D4ED9A50923132BB6156E620B)
        EndScale: Vector2D = ReturnValue_1
        goto(ExecutionFlow.Pop())
        # Label 1067
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L28')
        # Label 1141
        if not self.mEnableCollision:
            goto('L1717')
        Variable_0: Const[Transform] = Transform(Rotator(0, 0, 0, 1), Vector(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue_3: Ptr[SplineMeshComponent] = self.AddComponent("NODE_AddSplineMeshComponent-3", False, self, Ref[Variable_0])
        CurrentSplineMesh: Ptr[SplineMeshComponent] = ReturnValue_3
        
        NewParam = None
        # Label 1277
        self.GetStaticMeshForIndex(CurrentLoopIndex, Ref[NewParam])
        ReturnValue_4: bool = CurrentSplineMesh.SetStaticMesh(NewParam)
        ReturnValue_5: bool = Default__KismetSystemLibrary.IsValid(self.mSplineMaterial)
        if not ReturnValue_5:
            goto('L1479')
        CurrentSplineMesh.SetMaterial(0, self.mSplineMaterial)
        # Label 1479
        CurrentSplineMesh.SetStartAndEnd(StartLocation, StartTangent, EndLocation, EndTangent, False)
        CurrentSplineMesh.SetStartRoll(StartRoll, False)
        CurrentSplineMesh.SetEndRoll(EndRoll, False)
        CurrentSplineMesh.SetStartScale(StartScale, False)
        CurrentSplineMesh.SetEndScale(EndScale, True)
        goto(ExecutionFlow.Pop())
        # Label 1717
        Variable1: Const[Transform] = Transform(Rotator(0, 0, 0, 1), Vector(0, 0, 0), Vector(1, 1, 1))
        
        ReturnValue1_1: Ptr[SplineMeshComponent] = self.AddComponent("NODE_AddSplineMeshComponent-5", False, self, Ref[Variable1])
        CurrentSplineMesh = ReturnValue1_1
        goto('L1277')
    

    def UserConstructionScript(self):
        ExecutionFlow.Push("L1293")
        ExecutionFlow.Push("L518")
        ExecutionFlow.Push("L503")
        ExecutionFlow.Push("L98")
        ReturnValue: int32 = self.Spline.GetNumberOfSplinePoints()
        self.NumberOfSplinePoints = ReturnValue
        goto(ExecutionFlow.Pop())
        
        # Label 98
        ReturnValue_0: int32 = len(self.CaveDataArray)
        ReturnValue_1: bool = ReturnValue_0 <= self.NumberOfSplinePoints
        if not ReturnValue_1:
            goto('L282')
        
        ReturnValue_2: int32 = self.CaveDataArray.append(self.CaveMeshDefaults)
        goto('L98')
        
        # Label 282
        ReturnValue_0 = len(self.CaveDataArray)
        ReturnValue_3: bool = ReturnValue_0 > self.NumberOfSplinePoints
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        
        ReturnValue_4: int32 = len(self.CaveDataArray) - 1
        
        self.CaveDataArray.remove(ReturnValue_4)
        goto('L98')
        # Label 503
        self.BuildCaveElement()
        goto(ExecutionFlow.Pop())
        # Label 518
        if not self.DrawCavePointNumbers:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        # Label 551
        ReturnValue_5: int32 = self.NumberOfSplinePoints - 1
        ReturnValue_6: bool = Variable <= ReturnValue_5
        if not ReturnValue_6:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L1219")
        ReturnValue_7: FString = Default__KismetStringLibrary.Conv_IntToString(Variable)
        self.CurrentCavePoint = ReturnValue_7
        
        Location = None
        Tangent = None
        self.Spline.GetLocationAndTangentAtSplinePoint(Variable, 0, Ref[Location], Ref[Tangent])
        ReturnValue_8: Vector = Multiply_VectorInt(Tangent, -1)
        
        X = None
        Y = None
        Z = None
        X, Y, Z = BreakVector(Location)
        ReturnValue_9: Rotator = Conv_VectorToRotator(ReturnValue_8)
        ReturnValue_10: float = Z + 50
        ReturnValue_11: Vector = Vector(X, Y, ReturnValue_10)
        ReturnValue_12: Transform = MakeTransform(ReturnValue_11, ReturnValue_9, Vector(1, 1, 1))
        
        ReturnValue_13: Ptr[TextRenderComponent] = self.AddComponent("NODE_AddTextRenderComponent-0", False, self, Ref[ReturnValue_12])
        ReturnValue_14: FText = Default__KismetTextLibrary.Conv_StringToText(self.CurrentCavePoint)
        
        ReturnValue_13.K2_SetText(Ref[ReturnValue_14])
        goto(ExecutionFlow.Pop())
        # Label 1219
        ReturnValue_15: int32 = Variable + 1
        Variable = ReturnValue_15
        goto('L551')
    
