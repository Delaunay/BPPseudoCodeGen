
from codegen.ue4_stub import *

from Script.Engine import BreakVector2D
from Script.UMG import Default__SlateBlueprintLibrary
from Script.Engine import Subtract_Vector2DVector2D
from Script.UMG import UserWidget
from Script.Engine import Default__KismetArrayLibrary
from Script.UMG import Tick
from Script.UMG import GetLocalSize
from Script.CoreUObject import Vector2D
from Game.FactoryGame.Buildable.-Shared.Widgets.GraphCurve import GraphCurve
from Script.Engine import Multiply_Vector2DVector2D
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Graph import ExecuteUbergraph_Widget_Graph.K2Node_Event_MyGeometry
from Script.UMG import DrawLine
from Script.Engine import Conv_IntToFloat
from Script.Engine import Add_Vector2DVector2D
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Graph import ExecuteUbergraph_Widget_Graph.K2Node_Event_InDeltaTime
from Script.UMG import Default__WidgetBlueprintLibrary
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_Graph import ExecuteUbergraph_Widget_Graph

class Widget_Graph(UserWidget):
    mCurves: List[GraphCurve]
    mAxisMax: Vector2D = Namespace(X=1, Y=1)
    mCanvasSize: Vector2D = Namespace(X=50, Y=50)
    mScaler: Vector2D
    mLineThickness: int32 = 2
    
    def OnPaint(self):
        ExecutionFlow.Push("L2651")
        
        X1 = None
        Y1 = None
        BreakVector2D(self.mCanvasSize, Ref[X1], Ref[Y1])
        ReturnValue: Vector2D = Vector2D(1, Y1)
        Origin = ReturnValue
        ReturnValue1: Vector2D = Vector2D(1, -1)
        invert = ReturnValue1
        Variable: int32 = 0
        Variable_0: int32 = 0
        
        # Label 222
        ReturnValue_0: int32 = len(self.mCurves)
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
            goto('L2350')
        Variable_0 = Variable
        ExecutionFlow.Push("L2355")
        
        Item = None
        Item = self.mCurves[Variable_0]
        
        Item.Points_11_7F825CE44C5C364A4E1F71B0D820C91E = None
        ReturnValue_2: int32 = len(Item.Points_11_7F825CE44C5C364A4E1F71B0D820C91E) - 1
        ReturnValue_3: bool = ReturnValue_2 > 0
        if not ReturnValue_3:
           goto(ExecutionFlow.Pop())
        Variable_1: int32 = 1
        
        Item = None
        # Label 559
        Item = self.mCurves[Variable_0]
        
        Item.Points_11_7F825CE44C5C364A4E1F71B0D820C91E = None
        ReturnValue_2 = len(Item.Points_11_7F825CE44C5C364A4E1F71B0D820C91E) - 1
        ReturnValue2: bool = Variable_1 <= ReturnValue_2
        if not ReturnValue2:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L2429")
        Variable1: int32 = 0
        # Label 762
        ReturnValue1_0: int32 = self.mLineThickness - 1
        ReturnValue_4: bool = Variable1 <= ReturnValue1_0
        if not ReturnValue_4:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L2503")
        xLinePixel = Variable1
        Variable2: int32 = 0
        # Label 907
        ReturnValue1_0 = self.mLineThickness - 1
        ReturnValue1_1: bool = Variable2 <= ReturnValue1_0
        if not ReturnValue1_1:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L2577")
        yLinePixel = Variable2
        ReturnValue_5: int32 = Variable_1 - 1
        ReturnValue_6: float = Conv_IntToFloat(yLinePixel)
        ReturnValue1_2: float = Conv_IntToFloat(xLinePixel)
        ReturnValue2_0: float = Conv_IntToFloat(yLinePixel)
        ReturnValue3: float = Conv_IntToFloat(xLinePixel)
        
        X = None
        Y = None
        BreakVector2D(invert, Ref[X], Ref[Y])
        
        Item = None
        Item = self.mCurves[Variable_0]
        ReturnValue_7: float = Item.OffsetY_14_0BB8215B4F827D9DCB6242B85AC85100 * Y
        ReturnValue2_1: Vector2D = Vector2D(0, ReturnValue_7)
        
        Item.Points_11_7F825CE44C5C364A4E1F71B0D820C91E = None
        Item1 = None
        Item1 = Item.Points_11_7F825CE44C5C364A4E1F71B0D820C91E[ReturnValue_5]
        
        Item.Points_11_7F825CE44C5C364A4E1F71B0D820C91E = None
        Item2 = None
        Item2 = Item.Points_11_7F825CE44C5C364A4E1F71B0D820C91E[Variable_1]
        ReturnValue_8: Vector2D = Multiply_Vector2DVector2D(Item1, self.mScaler)
        ReturnValue1_3: Vector2D = Multiply_Vector2DVector2D(Item2, self.mScaler)
        ReturnValue2_2: Vector2D = Multiply_Vector2DVector2D(ReturnValue_8, invert)
        ReturnValue3_0: Vector2D = Multiply_Vector2DVector2D(ReturnValue1_3, invert)
        ReturnValue_9: Vector2D = Add_Vector2DVector2D(ReturnValue2_2, Origin)
        ReturnValue1_4: Vector2D = Add_Vector2DVector2D(ReturnValue3_0, Origin)
        ReturnValue2_3: Vector2D = Add_Vector2DVector2D(ReturnValue_9, ReturnValue2_1)
        ReturnValue3_1: Vector2D = Add_Vector2DVector2D(ReturnValue1_4, ReturnValue2_1)
        
        X2 = None
        Y2 = None
        BreakVector2D(ReturnValue2_3, Ref[X2], Ref[Y2])
        
        X3 = None
        Y3 = None
        BreakVector2D(ReturnValue3_1, Ref[X3], Ref[Y3])
        ReturnValue_10: float = ReturnValue2_0 + Y2
        ReturnValue1_5: float = ReturnValue_6 + Y3
        ReturnValue2_4: float = ReturnValue1_2 + X3
        ReturnValue3_2: float = ReturnValue3 + X2
        ReturnValue3_3: Vector2D = Vector2D(ReturnValue2_4, ReturnValue1_5)
        ReturnValue4: Vector2D = Vector2D(ReturnValue3_2, ReturnValue_10)
        
        Default__WidgetBlueprintLibrary.DrawLine(ReturnValue4, ReturnValue3_3, Item.Color_10_60E36C364D08C282508165B980658169, True, 1, Ref[Context])
        goto(ExecutionFlow.Pop())
        # Label 2350
        # End
        # Label 2355
        ReturnValue2_5: int32 = Variable + 1
        Variable = ReturnValue2_5
        goto('L222')
        # Label 2429
        ReturnValue_11: int32 = Variable_1 + 1
        Variable_1 = ReturnValue_11
        goto('L559')
        # Label 2503
        ReturnValue1_6: int32 = Variable1 + 1
        Variable1 = ReturnValue1_6
        goto('L762')
        # Label 2577
        ReturnValue3_4: int32 = Variable2 + 1
        Variable2 = ReturnValue3_4
        goto('L907')
    

    def Tick(self):
        ExecuteUbergraph_Widget_Graph.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_Graph.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Graph(10)
    

    def ExecuteUbergraph_Widget_Graph(self):
        self.Tick(MyGeometry, InDeltaTime)
        ReturnValue: int32 = self.mLineThickness - 1
        ReturnValue_0: int32 = ReturnValue + 4
        ReturnValue_1: float = Conv_IntToFloat(ReturnValue_0)
        
        MyGeometry = None
        ReturnValue_2: Vector2D = Default__SlateBlueprintLibrary.GetLocalSize(Ref[MyGeometry])
        ReturnValue_3: Vector2D = Vector2D(-6, ReturnValue_1)
        ReturnValue_4: Vector2D = Subtract_Vector2DVector2D(ReturnValue_2, ReturnValue_3)
        self.mCanvasSize = ReturnValue_4
        
        X = None
        Y = None
        BreakVector2D(self.mCanvasSize, Ref[X], Ref[Y])
        
        X1 = None
        Y1 = None
        BreakVector2D(self.mAxisMax, Ref[X1], Ref[Y1])
        ReturnValue_5: float = X / X1
        ReturnValue1: float = Y / Y1
        ReturnValue1_0: Vector2D = Vector2D(ReturnValue_5, ReturnValue1)
        self.mScaler = ReturnValue1_0
    
