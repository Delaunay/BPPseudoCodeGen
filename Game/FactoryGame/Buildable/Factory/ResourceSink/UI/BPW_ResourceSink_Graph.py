
from codegen.ue4_stub import *

from Script.Engine import SetTextPropertyByName
from Script.Engine import Delay
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.BPW_Graph_DataPreview import BPW_Graph_DataPreview
from Script.Engine import Map_Contains
from Script.Engine import FFloor
from Script.Engine import GreaterEqual_IntInt
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import PanelSlot
from Script.UMG import AddChild
from Script.Engine import Conv_IntToFloat
from Script.Engine import EqualExactly_Vector2DVector2D
from Script.Engine import Not_PreBool
from Script.Engine import LatentActionInfo
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.Engine import SetStringPropertyByName
from Script.Engine import SetStructurePropertyByName
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import DrawLines
from Script.Engine import FormatArgumentData
from Script.UMG import Unhandled
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.BPW_ResourceSink_Graph import ExecuteUbergraph_BPW_ResourceSink_Graph.K2Node_Event_MouseEvent
from Script.UMG import GetLocalSize
from Script.Engine import Conv_FloatToText
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import Map_Values
from Script.UMG import Default__SlateBlueprintLibrary
from Script.Engine import BreakVector2D
from Script.Engine import NotEqual_FloatFloat
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.FloatArrayStruct import FloatArrayStruct
from Script.Engine import NotEqual_StrStr
from Script.Engine import Format
from Game.FactoryGame.Buildable.-Shared.Widgets.GraphCurve import GraphCurve
from Script.Engine import Default__KismetStringLibrary
from Game.FactoryGame.Buildable.Factory.ResourceSink.UI.BPW_ResourceSink_Graph import ExecuteUbergraph_BPW_ResourceSink_Graph
from Script.SlateCore import Geometry
from Script.UMG import UserWidget
from Script.Engine import Map_Find
from Script.Engine import Map_Add
from Script.Engine import Subtract_Vector2DVector2D
from Script.UMG import Create
from Script.UMG import GetMousePositionOnViewport
from Script.CoreUObject import Vector2D
from Script.Engine import Map_Keys
from Script.Engine import Default__BlueprintMapLibrary
from Script.UMG import LocalToViewport
from Script.Engine import Array_Clear
from Script.UMG import GetCachedGeometry
from Script.UMG import EventReply
from Script.CoreUObject import LinearColor

class BPW_ResourceSink_Graph(UserWidget):
    mPoints: Dict[FString, GraphCurve]
    mMosePosition: List[Vector2D]
    mDataPoints: Dict[FString, FloatArrayStruct]
    mHighestPoint: float
    mNumOfPoints: int32 = 10
    mPreviewWidgets: Dict[FString, BPW_Graph_DataPreview*]
    mGraphPadding: float = 5
    mSuffixes: Dict[FString, FText]
    
    def ResetPreviewValues(self):
        ExecutionFlow.Push("L1454")
        Keys: List[FString] = []
        
        Default__BlueprintMapLibrary.Map_Keys(Ref[self.mDataPoints], Ref[Keys])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 112
        ReturnValue: int32 = len(Keys)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L1380")
        
        Item = None
        Item = Keys[Variable_0]
        LocalGraphID = Item
        
        Value = None
        ReturnValue_1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mSuffixes], Ref[LocalGraphID], Ref[Value])
        FormatArgumentData.ArgumentName = "Suffix"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = Value
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        
        Value1 = None
        ReturnValue1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mPreviewWidgets], Ref[LocalGraphID], Ref[Value1])
        
        Value2 = None
        ReturnValue2: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mDataPoints], Ref[LocalGraphID], Ref[Value2])
        
        Value2.Array_3_27D674CB46ADE972708FE7BE723F42BF = None
        ReturnValue1_0: int32 = len(Value2.Array_3_27D674CB46ADE972708FE7BE723F42BF)
        ReturnValue_2: int32 = ReturnValue1_0 - 1
        
        Value2.Array_3_27D674CB46ADE972708FE7BE723F42BF = None
        Item1 = None
        Item1 = Value2.Array_3_27D674CB46ADE972708FE7BE723F42BF[ReturnValue_2]
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_FloatToText(Item1, 0, False, True, 1, 324, 0, 3)
        FormatArgumentData1.ArgumentName = "Value"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue_3
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_4: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1270, 'Value': '{Value} {Suffix}'}", Array)
        Value1.SetValue(ReturnValue_4)
        goto(ExecutionFlow.Pop())
        # Label 1380
        ReturnValue_5: int32 = Variable + 1
        Variable = ReturnValue_5
        goto('L112')
    

    def AddDataPreview(self, GraphID: FString):
        
        ReturnValue: bool = Default__BlueprintMapLibrary.Map_Contains(Ref[self.mPreviewWidgets], Ref[GraphID])
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        if not ReturnValue_0:
            goto('L1608')
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue_2: Ptr[BPW_Graph_DataPreview] = Default__WidgetBlueprintLibrary.Create(self, BPW_Graph_DataPreview, ReturnValue_1)
        Default__KismetSystemLibrary.SetStringPropertyByName(ReturnValue_2, "mTitle", GraphID)
        
        Value = None
        ReturnValue_3: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mSuffixes], Ref[GraphID], Ref[Value])
        FormatArgumentData.ArgumentName = "Suffix"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = Value
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        
        Value1 = None
        ReturnValue1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mDataPoints], Ref[GraphID], Ref[Value1])
        
        Value1.Array_3_27D674CB46ADE972708FE7BE723F42BF = None
        ReturnValue_4: int32 = len(Value1.Array_3_27D674CB46ADE972708FE7BE723F42BF)
        ReturnValue_5: int32 = ReturnValue_4 - 1
        
        Value1.Array_3_27D674CB46ADE972708FE7BE723F42BF = None
        Item = None
        Item = Value1.Array_3_27D674CB46ADE972708FE7BE723F42BF[ReturnValue_5]
        ReturnValue_6: FText = Default__KismetTextLibrary.Conv_FloatToText(Item, 0, False, True, 1, 324, 0, 3)
        FormatArgumentData1.ArgumentName = "Value"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue_6
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_7: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1115, 'Value': '{Value} {Suffix}'}", Array)
        
        Default__KismetSystemLibrary.SetTextPropertyByName(ReturnValue_2, "mStartingValue", Ref[ReturnValue_7])
        
        Value2 = None
        ReturnValue2: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mPoints], Ref[GraphID], Ref[Value2])
        
        Value2.Color_10_60E36C364D08C282508165B980658169 = None
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_2, "mPrimaryColor", Ref[Value2.Color_10_60E36C364D08C282508165B980658169])
        Variable: Const[LinearColor] = LinearColor(R = 0.05999999865889549, G = 0.05999999865889549, B = 0.05999999865889549, A = 1)
        
        Default__KismetSystemLibrary.SetStructurePropertyByName(ReturnValue_2, "mSecondaryColor", Ref[Variable])
        ReturnValue_8: Ptr[PanelSlot] = self.mDataPreviewContainer.AddChild(ReturnValue_2)
        
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mPreviewWidgets], Ref[GraphID], Ref[ReturnValue_2])
    

    def RedrawGraph(self):
        ExecutionFlow.Push("L584")
        Keys: List[FString] = []
        
        Default__BlueprintMapLibrary.Map_Keys(Ref[self.mDataPoints], Ref[Keys])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 112
        ReturnValue: int32 = len(Keys)
        ReturnValue_0: bool = Variable <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        Variable_0 = Variable
        ExecutionFlow.Push("L510")
        
        Item = None
        Item = Keys[Variable_0]
        
        Item = None
        Value = None
        ReturnValue_1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mPoints], Ref[Item], Ref[Value])
        
        Item = None
        Value1 = None
        ReturnValue1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mDataPoints], Ref[Item], Ref[Value1])
        
        Value1.Array_3_27D674CB46ADE972708FE7BE723F42BF = None
        self.UpdateOrAddGraphLine(Item, , Value.Color_10_60E36C364D08C282508165B980658169, Ref[Value1.Array_3_27D674CB46ADE972708FE7BE723F42BF])
        goto(ExecutionFlow.Pop())
        # Label 510
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L112')
    

    def OnMouseMove(self):
        ExecutionFlow.Push("L2796")
        LocalTimeIndex = 0
        MousePosX = 0
        ReturnValue: Const[Geometry] = self.GetCachedGeometry()
        
        ReturnValue_0: Vector2D = Default__SlateBlueprintLibrary.GetLocalSize(Ref[ReturnValue])
        mGraphSize = ReturnValue_0
        ReturnValue_1: Vector2D = Default__WidgetLayoutLibrary.GetMousePositionOnViewport(self)
        
        PixelPosition = None
        ViewportPosition = None
        Default__SlateBlueprintLibrary.LocalToViewport(self, Vector2D(X = 0, Y = 0), Ref[MyGeometry], Ref[PixelPosition], Ref[ViewportPosition])
        ReturnValue_2: Vector2D = Subtract_Vector2DVector2D(ReturnValue_1, ViewportPosition)
        
        X2 = None
        Y2 = None
        BreakVector2D(ReturnValue_2, Ref[X2], Ref[Y2])
        MousePosX = X2
        ReturnValue_3: int32 = self.mNumOfPoints - 1
        ReturnValue_4: float = Conv_IntToFloat(ReturnValue_3)
        
        X1 = None
        Y1 = None
        BreakVector2D(mGraphSize, Ref[X1], Ref[Y1])
        # Label 526
        ReturnValue_5: float = X1 / ReturnValue_4
        ReturnValue1: float = MousePosX / ReturnValue_5
        ReturnValue_6: int32 = FFloor(ReturnValue1)
        LocalTimeIndex = ReturnValue_6
        Keys: List[FString] = []
        
        Default__BlueprintMapLibrary.Map_Keys(Ref[self.mDataPoints], Ref[Keys])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 789
        ReturnValue1_0: int32 = len(Keys)
        ReturnValue_7: bool = Variable <= ReturnValue1_0
        if not ReturnValue_7:
            goto('L2270')
        Variable_0 = Variable
        ExecutionFlow.Push("L2722")
        
        Item1 = None
        Item1 = Keys[Variable_0]
        LocalGraphID = Item1
        Variable_1: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1038, 'Value': 'None'}"
        
        Value = None
        ReturnValue_8: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mSuffixes], Ref[LocalGraphID], Ref[Value])
        FormatArgumentData.ArgumentName = "Suffix"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = Value
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        
        Value1 = None
        ReturnValue1_1: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mPreviewWidgets], Ref[LocalGraphID], Ref[Value1])
        
        Value2 = None
        ReturnValue2: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mDataPoints], Ref[LocalGraphID], Ref[Value2])
        
        Value2.Array_3_27D674CB46ADE972708FE7BE723F42BF = None
        ReturnValue_9: int32 = len(Value2.Array_3_27D674CB46ADE972708FE7BE723F42BF)
        ReturnValue1_2: int32 = self.mNumOfPoints - ReturnValue_9
        ReturnValue2_0: int32 = LocalTimeIndex - ReturnValue1_2
        
        Value2.Array_3_27D674CB46ADE972708FE7BE723F42BF = None
        Item = None
        Item = Value2.Array_3_27D674CB46ADE972708FE7BE723F42BF[ReturnValue2_0]
        ReturnValue_10: FText = Default__KismetTextLibrary.Conv_FloatToText(Item, 0, False, True, 1, 324, 0, 3)
        ReturnValue_11: bool = GreaterEqual_IntInt(ReturnValue2_0, 0)
        FormatArgumentData1.ArgumentName = "Value"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue_10
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Variable_2: bool = ReturnValue_11
        Array: List[FormatArgumentData] = [FormatArgumentData1, FormatArgumentData]
        ReturnValue_12: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2116, 'Value': '{Value} {Suffix}'}", Array)
        
        switch = {
            False: Variable_1,
            True: ReturnValue_12
        }
        Value1.SetValue(switch.get(Variable_2, None))
        goto(ExecutionFlow.Pop())
        
        # Label 2270
        Default__KismetArrayLibrary.Array_Clear(Ref[self.mMosePosition])
        ReturnValue_13: Vector2D = Vector2D(MousePosX, 0)
        
        ReturnValue_14: int32 = self.mMosePosition.append(ReturnValue_13)
        
        X = None
        Y = None
        BreakVector2D(mGraphSize, Ref[X], Ref[Y])
        ReturnValue_15: float = Y - self.mDataPreviewSizeBox.HeightOverride
        ReturnValue1_3: Vector2D = Vector2D(MousePosX, ReturnValue_15)
        
        ReturnValue1_4: int32 = self.mMosePosition.append(ReturnValue1_3)
        ReturnValue_16: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_17: EventReply = ReturnValue_16
        goto('L2796')
        # Label 2722
        ReturnValue_18: int32 = Variable + 1
        Variable = ReturnValue_18
        goto('L789')
    

    def UpdateOrAddGraphLine(self, GraphID: FString, GraphPreviewDataSuffix: FText, GraphColor: LinearColor, GraphData: Ref[List[float]]):
        ExecutionFlow.Push("L3588")
        LocalHighestPoint = 0
        Keys: List[FString] = []
        
        Default__BlueprintMapLibrary.Map_Keys(Ref[self.mDataPoints], Ref[Keys])
        Variable2: int32 = 0
        # Label 112
        Variable: int32 = 0
        
        # Label 135
        ReturnValue3: int32 = len(Keys)
        ReturnValue2: bool = Variable2 <= ReturnValue3
        if not ReturnValue2:
            goto('L1197')
        Variable = Variable2
        ExecutionFlow.Push("L3292")
        
        Item2 = None
        Item2 = Keys[Variable]
        ReturnValue: bool = Default__KismetStringLibrary.NotEqual_StrStr(Item2, GraphID)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        Variable_0: int32 = 0
        Variable3: int32 = 0
        
        Item2 = None
        # Label 453
        Item2 = Keys[Variable]
        
        Item2 = None
        Value = None
        ReturnValue_0: bool = Default__BlueprintMapLibrary.Map_Find(Ref[self.mDataPoints], Ref[Item2], Ref[Value])
        
        Value.Array_3_27D674CB46ADE972708FE7BE723F42BF = None
        ReturnValue4: int32 = len(Value.Array_3_27D674CB46ADE972708FE7BE723F42BF)
        ReturnValue3_0: bool = Variable_0 <= ReturnValue4
        if not ReturnValue3_0:
           goto(ExecutionFlow.Pop())
        Variable3 = Variable_0
        ExecutionFlow.Push("L3366")
        
        Item2 = None
        Item2 = Keys[Variable]
        
        Item2 = None
        Value = None
        ReturnValue_0 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mDataPoints], Ref[Item2], Ref[Value])
        
        Value.Array_3_27D674CB46ADE972708FE7BE723F42BF = None
        Item3 = None
        Item3 = Value.Array_3_27D674CB46ADE972708FE7BE723F42BF[Variable3]
        ReturnValue1: bool = Item3 > LocalHighestPoint
        if not ReturnValue1:
           goto(ExecutionFlow.Pop())
        
        Item2 = None
        Item2 = Keys[Variable]
        
        Item2 = None
        Value = None
        ReturnValue_0 = Default__BlueprintMapLibrary.Map_Find(Ref[self.mDataPoints], Ref[Item2], Ref[Value])
        
        Value.Array_3_27D674CB46ADE972708FE7BE723F42BF = None
        Item3 = None
        Item3 = Value.Array_3_27D674CB46ADE972708FE7BE723F42BF[Variable3]
        LocalHighestPoint = Item3
        goto(ExecutionFlow.Pop())
        # Label 1197
        Variable1: int32 = 0
        Variable1_0: int32 = 0
        
        # Label 1243
        ReturnValue2_0: int32 = len(GraphData)
        ReturnValue1_0: bool = Variable1 <= ReturnValue2_0
        if not ReturnValue1_0:
            goto('L1580')
        Variable1_0 = Variable1
        ExecutionFlow.Push("L3440")
        
        Item1 = None
        Item1 = GraphData[Variable1_0]
        ReturnValue_1: bool = Item1 > LocalHighestPoint
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        
        Item1 = None
        Item1 = GraphData[Variable1_0]
        LocalHighestPoint = Item1
        goto(ExecutionFlow.Pop())
        # Label 1580
        ReturnValue1_1: bool = NotEqual_FloatFloat(LocalHighestPoint, 0)
        if not ReturnValue1_1:
            goto('L2810')
        Variable3_0: int32 = 0
        Variable2_0: int32 = 0
        
        # Label 1674
        ReturnValue1_2: int32 = len(GraphData)
        ReturnValue_2: bool = Variable3_0 <= ReturnValue1_2
        if not ReturnValue_2:
            goto('L2810')
        Variable2_0 = Variable3_0
        ExecutionFlow.Push("L3514")
        ReturnValue_3: float = self.mGraphPadding * 2
        ReturnValue_4: float = self.mDataPreviewSizeBox.HeightOverride + ReturnValue_3
        
        ReturnValue_5: int32 = len(GraphData)
        ReturnValue_6: int32 = self.mNumOfPoints - 1
        ReturnValue1_3: int32 = self.mNumOfPoints - ReturnValue_5
        ReturnValue_7: float = Conv_IntToFloat(ReturnValue_6)
        ReturnValue4_0: int32 = ReturnValue1_3 + Variable2_0
        ReturnValue1_4: float = Conv_IntToFloat(ReturnValue4_0)
        
        Item = None
        Item = GraphData[Variable2_0]
        ReturnValue_8: float = Item / LocalHighestPoint
        ReturnValue_9: float = 1 - ReturnValue_8
        ReturnValue_10: Const[Geometry] = self.GetCachedGeometry()
        
        ReturnValue_11: Vector2D = Default__SlateBlueprintLibrary.GetLocalSize(Ref[ReturnValue_10])
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_11, Ref[X], Ref[Y])
        ReturnValue1_5: float = X / ReturnValue_7
        ReturnValue1_6: float = Y - ReturnValue_4
        ReturnValue1_7: float = ReturnValue1_5 * ReturnValue1_4
        ReturnValue2_1: float = ReturnValue_9 * ReturnValue1_6
        ReturnValue1_8: float = ReturnValue2_1 + self.mGraphPadding
        ReturnValue_12: Vector2D = Vector2D(ReturnValue1_7, ReturnValue1_8)
        
        ReturnValue_13: int32 = NewPoints.append(ReturnValue_12)
        goto(ExecutionFlow.Pop())
        # Label 2810
        FloatArrayStruct.Array_3_27D674CB46ADE972708FE7BE723F42BF = GraphData
        
        FloatArrayStruct = None
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mDataPoints], Ref[GraphID], Ref[FloatArrayStruct])
        GraphCurve.Color_10_60E36C364D08C282508165B980658169 = GraphColor
        GraphCurve.Points_11_7F825CE44C5C364A4E1F71B0D820C91E = NewPoints
        GraphCurve.OffsetY_14_0BB8215B4F827D9DCB6242B85AC85100 = 0
        
        GraphCurve = None
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mPoints], Ref[GraphID], Ref[GraphCurve])
        
        Default__BlueprintMapLibrary.Map_Add(Ref[self.mSuffixes], Ref[GraphID], Ref[GraphPreviewDataSuffix])
        self.AddDataPreview(GraphID)
        ReturnValue_14: bool = self.IsHovered()
        if not ReturnValue_14:
            goto('L3202')
        self.ResetPreviewValues()
        # Label 3202
        ReturnValue_15: bool = NotEqual_FloatFloat(self.mHighestPoint, LocalHighestPoint)
        if not ReturnValue_15:
           goto(ExecutionFlow.Pop())
        self.mHighestPoint = LocalHighestPoint
        self.RedrawGraph()
        goto(ExecutionFlow.Pop())
        # Label 3292
        ReturnValue2_2: int32 = Variable2 + 1
        Variable2 = ReturnValue2_2
        goto('L135')
        # Label 3366
        ReturnValue_16: int32 = Variable_0 + 1
        Variable_0 = ReturnValue_16
        goto('L453')
        # Label 3440
        ReturnValue1_9: int32 = Variable1 + 1
        Variable1 = ReturnValue1_9
        goto('L1243')
        # Label 3514
        ReturnValue3_1: int32 = Variable3_0 + 1
        Variable3_0 = ReturnValue3_1
        goto('L1674')
    

    def OnPaint(self):
        ExecutionFlow.Push("L605")
        ReturnValue: bool = self.IsHovered()
        if not ReturnValue:
            goto('L133')
        
        Default__WidgetBlueprintLibrary.DrawLines(LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.057805001735687256, A = 1), True, 1, Ref[Context], Ref[self.mMosePosition])
        # Label 133
        Values: List[GraphCurve] = []
        
        Default__BlueprintMapLibrary.Map_Values(Ref[self.mPoints], Ref[Values])
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 240
        ReturnValue_0: int32 = len(Values)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L526')
        Variable_0 = Variable
        ExecutionFlow.Push("L531")
        
        Item = None
        Item = Values[Variable_0]
        
        Item.Points_11_7F825CE44C5C364A4E1F71B0D820C91E = None
        Default__WidgetBlueprintLibrary.DrawLines(Item.Color_10_60E36C364D08C282508165B980658169, True, 2, Ref[Context], Ref[Item.Points_11_7F825CE44C5C364A4E1F71B0D820C91E])
        goto(ExecutionFlow.Pop())
        # Label 526
        # End
        # Label 531
        ReturnValue_2: int32 = Variable + 1
        Variable = ReturnValue_2
        goto('L240')
    

    def Construct(self):
        self.ExecuteUbergraph_BPW_ResourceSink_Graph(276)
    

    def OnMouseLeave(self):
        ExecuteUbergraph_BPW_ResourceSink_Graph.K2Node_Event_MouseEvent = MouseEvent #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_BPW_ResourceSink_Graph(281)
    

    def ExecuteUbergraph_BPW_ResourceSink_Graph(self):
        goto(ComputedJump("EntryPoint"))
        # Label 15
        self.ResetPreviewValues()
        goto(ExecutionFlow.Pop())
        # Label 30
        ReturnValue: Const[Geometry] = self.GetCachedGeometry()
        
        ReturnValue_0: Vector2D = Default__SlateBlueprintLibrary.GetLocalSize(Ref[ReturnValue])
        ReturnValue_1: bool = EqualExactly_Vector2DVector2D(ReturnValue_0, Vector2D(X = 0, Y = 0))
        if not ReturnValue_1:
            goto('L261')
        Default__KismetSystemLibrary.Delay(self, 0.10000000149011612, LatentActionInfo(Linkage = 30, UUID = -1958481073, ExecutionFunction = "ExecuteUbergraph_BPW_ResourceSink_Graph", CallbackTarget = self))
        goto(ExecutionFlow.Pop())
        # Label 261
        self.RedrawGraph()
        goto(ExecutionFlow.Pop())
        goto('L30')
        goto('L15')
    
