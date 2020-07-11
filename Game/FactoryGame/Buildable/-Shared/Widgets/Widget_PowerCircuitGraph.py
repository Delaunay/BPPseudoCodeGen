
from codegen.ue4_stub import *

from Script.FactoryGame import Default__FGPowerCircuit
from Script.FactoryGame import GetPowerCircuit
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_PowerCircuitGraph import ExecuteUbergraph_Widget_PowerCircuitGraph
from Script.UMG import CanvasPanelSlot
from Script.FactoryGame import GetNumGraphPoint
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import SlotAsCanvasSlot
from Script.FactoryGame import FGPowerCircuit
from Script.FactoryGame import FGPowerInfoComponent
from Script.Engine import Conv_IntToFloat
from Script.Engine import Array_Set
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Script.FactoryGame import GetGraphPointAtIndex
from Script.Engine import SelectFloat
from Script.Engine import Default__KismetArrayLibrary
from Script.Engine import FormatArgumentData
from Script.UMG import Unhandled
from Script.UMG import ESlateVisibility
from Script.UMG import GetLocalSize
from Script.Engine import Conv_FloatToText
from Script.Engine import IsValid
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_PowerCircuitGraph import ExecuteUbergraph_Widget_PowerCircuitGraph.K2Node_Event_MyGeometry
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.UMG import SetColorAndOpacity
from Script.Engine import Conv_IntToText
from Script.Engine import Default__KismetTextLibrary
from Script.UMG import Default__SlateBlueprintLibrary
from Script.Engine import BreakVector2D
from Script.FactoryGame import IsFuseTriggered
from Script.Engine import BooleanOR
from Script.Engine import FCeil
from Game.FactoryGame.Buildable.-Shared.Widgets.Widget_PowerCircuitGraph import ExecuteUbergraph_Widget_PowerCircuitGraph.K2Node_Event_InDeltaTime
from Script.UMG import Tick
from Script.Engine import Format
from Script.FactoryGame import GetStats
from Script.SlateCore import Geometry
from Script.FactoryGame import FGPowerCircuitWidget
from Script.Engine import Divide_Vector2DVector2D
from Script.Engine import Subtract_Vector2DVector2D
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.UMG import GetMousePositionOnViewport
from Script.CoreUObject import Vector2D
from Script.Engine import Round
from Script.UMG import SetPosition
from Script.SlateCore import SlateColor
from Script.UMG import LocalToViewport
from Script.UMG import GetCachedGeometry
from Script.UMG import EventReply
from Script.CoreUObject import LinearColor

class Widget_PowerCircuitGraph(FGPowerCircuitWidget):
    mPowerInfo: Ptr[FGPowerInfoComponent]
    
    def ZeroGraphStats(self):
        DefaultValue = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': '0'}"
        FormatArgumentData2.ArgumentName = "Value"
        FormatArgumentData2.ArgumentValueType = 4
        FormatArgumentData2.ArgumentValue = DefaultValue
        FormatArgumentData2.ArgumentValueInt = 0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array2: List[FormatArgumentData] = [FormatArgumentData2]
        ReturnValue2: FText = Default__KismetTextLibrary.Format(STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/ST_Units.ST_Units", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 380, 'Value': 'Value_MW'}", Array2)
        self.mConsumptionHover.SetText(ReturnValue2)
        FormatArgumentData1.ArgumentName = "Value"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = DefaultValue
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        # Label 637
        Array1: List[FormatArgumentData] = [FormatArgumentData1]
        ReturnValue1: FText = Default__KismetTextLibrary.Format(STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/ST_Units.ST_Units", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 766, 'Value': 'Value_MW'}", Array1)
        self.mProductionHover.SetText(ReturnValue1)
        FormatArgumentData.ArgumentName = "Value"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = DefaultValue
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue: FText = Default__KismetTextLibrary.Format(STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/ST_Units.ST_Units", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1152, 'Value': 'Value_MW'}", Array)
        self.mCapacityHover.SetText(ReturnValue)
    

    def UpdateStats(self):
        ReturnValue: bool = self.mGraph.IsHovered()
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        if not ReturnValue_0:
            goto('L1810')
        ReturnValue_1: Ptr[FGPowerCircuit] = self.GetPowerCircuit()
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_1)
        if not ReturnValue_2:
            goto('L1796')
        ReturnValue_1 = self.GetPowerCircuit()
        
        stats = None
        ReturnValue_1.GetStats(Ref[stats])
        ReturnValue1: FText = Default__KismetTextLibrary.Conv_FloatToText(stats.PowerConsumed, 0, False, True, 1, 324, 0, 1)
        FormatArgumentData1.ArgumentName = "Value"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue1
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData1]
        ReturnValue1_0: FText = Default__KismetTextLibrary.Format(STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/ST_Units.ST_Units", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 648, 'Value': 'Value_MW'}", Array1)
        self.mConsumptionHover.SetText(ReturnValue1_0)
        ReturnValue_1 = self.GetPowerCircuit()
        
        stats = None
        ReturnValue_1.GetStats(Ref[stats])
        ReturnValue2: FText = Default__KismetTextLibrary.Conv_FloatToText(stats.PowerProduced, 0, False, True, 1, 324, 0, 1)
        FormatArgumentData2.ArgumentName = "Value"
        FormatArgumentData2.ArgumentValueType = 4
        FormatArgumentData2.ArgumentValue = ReturnValue2
        FormatArgumentData2.ArgumentValueInt = 0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array2: List[FormatArgumentData] = [FormatArgumentData2]
        ReturnValue2_0: FText = Default__KismetTextLibrary.Format(STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/ST_Units.ST_Units", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1187, 'Value': 'Value_MW'}", Array2)
        self.mProductionHover.SetText(ReturnValue2_0)
        ReturnValue_1 = self.GetPowerCircuit()
        
        stats = None
        ReturnValue_1.GetStats(Ref[stats])
        ReturnValue_3: FText = Default__KismetTextLibrary.Conv_FloatToText(stats.PowerProductionCapacity, 0, False, True, 1, 324, 0, 1)
        FormatArgumentData.ArgumentName = "Value"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_3
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_4: FText = Default__KismetTextLibrary.Format(STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/ST_Units.ST_Units", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 1726, 'Value': 'Value_MW'}", Array)
        self.mCapacityHover.SetText(ReturnValue_4)
        # End
        # Label 1796
        self.ZeroGraphStats()
    

    def OnMouseMove(self):
        ReturnValue: bool = self.mGraph.IsHovered()
        if not ReturnValue:
            goto('L4446')
        ReturnValue_0: Const[Geometry] = self.GetCachedGeometry()
        
        ReturnValue_1: Vector2D = Default__SlateBlueprintLibrary.GetLocalSize(Ref[ReturnValue_0])
        mGraphSize = ReturnValue_1
        ReturnValue1: Ptr[FGPowerCircuit] = self.GetPowerCircuit()
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        if not ReturnValue_2:
            goto('L4369')
        ReturnValue_3: Vector2D = Default__WidgetLayoutLibrary.GetMousePositionOnViewport(self)
        
        PixelPosition = None
        ViewportPosition = None
        Default__SlateBlueprintLibrary.LocalToViewport(self, Vector2D(X = 0, Y = 0), Ref[MyGeometry], Ref[PixelPosition], Ref[ViewportPosition])
        ReturnValue_4: Vector2D = Subtract_Vector2DVector2D(ReturnValue_3, ViewportPosition)
        ReturnValue_5: Ptr[FGPowerCircuit] = self.GetPowerCircuit()
        ReturnValue_6: Vector2D = Divide_Vector2DVector2D(ReturnValue_4, mGraphSize)
        
        stats = None
        ReturnValue_5.GetStats(Ref[stats])
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_6, Ref[X], Ref[Y])
        
        stats = None
        ReturnValue_7: int32 = Default__FGPowerCircuit.GetNumGraphPoint(Ref[stats])
        ReturnValue_8: int32 = ReturnValue_7 - 1
        ReturnValue_9: float = Conv_IntToFloat(ReturnValue_8)
        ReturnValue_10: float = X * ReturnValue_9
        ReturnValue_11: int32 = Round(ReturnValue_10)
        ReturnValue_12: bool = ReturnValue_11 <= ReturnValue_7
        if not ReturnValue_12:
            goto('L4446')
        
        PixelPosition = None
        ViewportPosition = None
        Default__SlateBlueprintLibrary.LocalToViewport(self, Vector2D(X = 0, Y = 0), Ref[MyGeometry], Ref[PixelPosition], Ref[ViewportPosition])
        ReturnValue_13: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(self.mPointer)
        ReturnValue_4 = Subtract_Vector2DVector2D(ReturnValue_3, ViewportPosition)
        
        X1 = None
        Y1 = None
        BreakVector2D(ReturnValue_4, Ref[X1], Ref[Y1])
        ReturnValue_14: Vector2D = Vector2D(X1, 0)
        ReturnValue_13.SetPosition(ReturnValue_14)
        
        PixelPosition = None
        ViewportPosition = None
        Default__SlateBlueprintLibrary.LocalToViewport(self, Vector2D(X = 0, Y = 0), Ref[MyGeometry], Ref[PixelPosition], Ref[ViewportPosition])
        ReturnValue_4 = Subtract_Vector2DVector2D(ReturnValue_3, ViewportPosition)
        ReturnValue_5 = self.GetPowerCircuit()
        ReturnValue_6 = Divide_Vector2DVector2D(ReturnValue_4, mGraphSize)
        
        stats = None
        ReturnValue_5.GetStats(Ref[stats])
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_6, Ref[X], Ref[Y])
        
        stats = None
        ReturnValue_7 = Default__FGPowerCircuit.GetNumGraphPoint(Ref[stats])
        ReturnValue_8 = ReturnValue_7 - 1
        ReturnValue_9 = Conv_IntToFloat(ReturnValue_8)
        ReturnValue_10 = X * ReturnValue_9
        ReturnValue_11 = Round(ReturnValue_10)
        
        stats = None
        item = None
        ReturnValue_15: bool = Default__FGPowerCircuit.GetGraphPointAtIndex(ReturnValue_11, Ref[stats], Ref[item])
        ReturnValue2: FText = Default__KismetTextLibrary.Conv_FloatToText(item.Consumed, 0, False, True, 1, 324, 0, 1)
        FormatArgumentData2.ArgumentName = "Value"
        FormatArgumentData2.ArgumentValueType = 4
        FormatArgumentData2.ArgumentValue = ReturnValue2
        FormatArgumentData2.ArgumentValueInt = 0
        FormatArgumentData2.ArgumentValueFloat = 0
        FormatArgumentData2.ArgumentValueGender = 0
        Array2: List[FormatArgumentData] = [FormatArgumentData2]
        ReturnValue2_0: FText = Default__KismetTextLibrary.Format(STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/ST_Units.ST_Units", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 2135, 'Value': 'Value_MWh'}", Array2)
        self.mConsumptionHover.SetText(ReturnValue2_0)
        
        PixelPosition = None
        ViewportPosition = None
        Default__SlateBlueprintLibrary.LocalToViewport(self, Vector2D(X = 0, Y = 0), Ref[MyGeometry], Ref[PixelPosition], Ref[ViewportPosition])
        ReturnValue_4 = Subtract_Vector2DVector2D(ReturnValue_3, ViewportPosition)
        ReturnValue_5 = self.GetPowerCircuit()
        ReturnValue_6 = Divide_Vector2DVector2D(ReturnValue_4, mGraphSize)
        
        stats = None
        ReturnValue_5.GetStats(Ref[stats])
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_6, Ref[X], Ref[Y])
        
        stats = None
        ReturnValue_7 = Default__FGPowerCircuit.GetNumGraphPoint(Ref[stats])
        ReturnValue_8 = ReturnValue_7 - 1
        ReturnValue_9 = Conv_IntToFloat(ReturnValue_8)
        ReturnValue_10 = X * ReturnValue_9
        ReturnValue_11 = Round(ReturnValue_10)
        
        stats = None
        item = None
        ReturnValue_15 = Default__FGPowerCircuit.GetGraphPointAtIndex(ReturnValue_11, Ref[stats], Ref[item])
        ReturnValue1_0: FText = Default__KismetTextLibrary.Conv_FloatToText(item.Produced, 0, False, True, 1, 324, 0, 1)
        FormatArgumentData1.ArgumentName = "Value"
        FormatArgumentData1.ArgumentValueType = 4
        FormatArgumentData1.ArgumentValue = ReturnValue1_0
        FormatArgumentData1.ArgumentValueInt = 0
        FormatArgumentData1.ArgumentValueFloat = 0
        FormatArgumentData1.ArgumentValueGender = 0
        Array1: List[FormatArgumentData] = [FormatArgumentData1]
        ReturnValue1_1: FText = Default__KismetTextLibrary.Format(STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/ST_Units.ST_Units", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 3178, 'Value': 'Value_MWh'}", Array1)
        self.mProductionHover.SetText(ReturnValue1_1)
        
        PixelPosition = None
        ViewportPosition = None
        Default__SlateBlueprintLibrary.LocalToViewport(self, Vector2D(X = 0, Y = 0), Ref[MyGeometry], Ref[PixelPosition], Ref[ViewportPosition])
        ReturnValue_4 = Subtract_Vector2DVector2D(ReturnValue_3, ViewportPosition)
        ReturnValue_5 = self.GetPowerCircuit()
        ReturnValue_6 = Divide_Vector2DVector2D(ReturnValue_4, mGraphSize)
        
        stats = None
        ReturnValue_5.GetStats(Ref[stats])
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_6, Ref[X], Ref[Y])
        
        stats = None
        ReturnValue_7 = Default__FGPowerCircuit.GetNumGraphPoint(Ref[stats])
        ReturnValue_8 = ReturnValue_7 - 1
        ReturnValue_9 = Conv_IntToFloat(ReturnValue_8)
        ReturnValue_10 = X * ReturnValue_9
        ReturnValue_11 = Round(ReturnValue_10)
        
        stats = None
        item = None
        ReturnValue_15 = Default__FGPowerCircuit.GetGraphPointAtIndex(ReturnValue_11, Ref[stats], Ref[item])
        ReturnValue_16: FText = Default__KismetTextLibrary.Conv_FloatToText(item.ProductionCapacity, 0, False, True, 1, 324, 0, 1)
        FormatArgumentData.ArgumentName = "Value"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_16
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_17: FText = Default__KismetTextLibrary.Format(STRING_TABLE_ENTRY("StringTable /Game/FactoryGame/Interface/UI/ST_Units.ST_Units", "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 4221, 'Value': 'Value_MWh'}", Array)
        self.mCapacityHover.SetText(ReturnValue_17)
        ReturnValue_18: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_19: EventReply = ReturnValue_18
        goto('L4446')
        # Label 4369
        ReturnValue1_2: EventReply = Default__WidgetBlueprintLibrary.Unhandled()
        ReturnValue_19 = ReturnValue1_2
    

    def SetHoverStyle(self, TextObject: Ptr[TextBlock], BackgroundObject: Ptr[Image], IsHovered: bool):
        SlateColor.SpecifiedColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        SlateColor.ColorUseRule = 0
        Variable1: bool = IsHovered
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        
        switch = {
            False: Text,
            True: SlateColor
        }
        TextObject.SetColorAndOpacity(switch.get(Variable1, None))
        Variable: LinearColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.05951099842786789, A = 1)
        Variable1_0: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 0)
        Variable_0: bool = IsHovered
        
        switch_0 = {
            False: Variable1_0,
            True: Variable
        }
        BackgroundObject.SetColorAndOpacity(switch_0.get(Variable_0, None))
    

    def GetCurrentlyUsingText(self):
        ReturnValue1: Ptr[FGPowerCircuit] = self.GetPowerCircuit()
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(ReturnValue1)
        if not ReturnValue:
            goto('L618')
        ReturnValue_0: Ptr[FGPowerCircuit] = self.GetPowerCircuit()
        
        stats = None
        ReturnValue_0.GetStats(Ref[stats])
        ReturnValue_1: int32 = Round(stats.PowerConsumed)
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_1, False, True, 1, 324)
        FormatArgumentData.ArgumentName = "0"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_2
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 522, 'Value': 'Consuming: {0}MW'}", Array)
        ReturnValue_4: FText = ReturnValue_3
        goto('L638')
        # Label 618
        ReturnValue_4 = 
    

    def GetResetFuseButtonEnabled(self):
        ReturnValue: Ptr[FGPowerCircuit] = self.GetPowerCircuit()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L171')
        ReturnValue = self.GetPowerCircuit()
        ReturnValue_1: bool = ReturnValue.IsFuseTriggered()
        ReturnValue_2: bool = ReturnValue_1
        goto('L182')
        # Label 171
        ReturnValue_2 = False
    

    def GetCapacityText(self):
        ReturnValue: Ptr[FGPowerCircuit] = self.GetPowerCircuit()
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(ReturnValue)
        if not ReturnValue_0:
            goto('L617')
        ReturnValue1: Ptr[FGPowerCircuit] = self.GetPowerCircuit()
        
        stats = None
        ReturnValue1.GetStats(Ref[stats])
        ReturnValue_1: int32 = Round(stats.PowerProductionCapacity)
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_1, False, True, 1, 324)
        FormatArgumentData.ArgumentName = "0"
        FormatArgumentData.ArgumentValueType = 4
        FormatArgumentData.ArgumentValue = ReturnValue_2
        FormatArgumentData.ArgumentValueInt = 0
        FormatArgumentData.ArgumentValueFloat = 0
        FormatArgumentData.ArgumentValueGender = 0
        Array: List[FormatArgumentData] = [FormatArgumentData]
        ReturnValue_3: FText = Default__KismetTextLibrary.Format("{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 522, 'Value': 'Capacity: {0}MW'}", Array)
        ReturnValue_4: FText = ReturnValue_3
        goto('L637')
        # Label 617
        ReturnValue_4 = 
    

    def UpdatePoints(self):
        ExecutionFlow.Push("L4396")
        ReturnValue2: Ptr[FGPowerCircuit] = self.GetPowerCircuit()
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(ReturnValue2)
        if not ReturnValue:
            goto('L1610')
        Variable4: int32 = 0
        # Label 113
        ReturnValue_0: Ptr[FGPowerCircuit] = self.GetPowerCircuit()
        
        stats = None
        ReturnValue_0.GetStats(Ref[stats])
        
        stats = None
        ReturnValue_1: int32 = Default__FGPowerCircuit.GetNumGraphPoint(Ref[stats])
        ReturnValue_2: int32 = ReturnValue_1 - 1
        ReturnValue_3: bool = Variable4 <= ReturnValue_2
        if not ReturnValue_3:
            goto('L1615')
        ExecutionFlow.Push("L4322")
        ReturnValue_0 = self.GetPowerCircuit()
        
        stats = None
        ReturnValue_0.GetStats(Ref[stats])
        ReturnValue1: float = Variable4 * stats.StatIntervalTime
        
        stats = None
        item = None
        ReturnValue_4: bool = Default__FGPowerCircuit.GetGraphPointAtIndex(Variable4, Ref[stats], Ref[item])
        ReturnValue3: Vector2D = Vector2D(ReturnValue1, item.Consumed)
        
        ReturnValue2_0: int32 = consumptionPoints.append(ReturnValue3)
        ReturnValue_0 = self.GetPowerCircuit()
        
        stats = None
        ReturnValue_0.GetStats(Ref[stats])
        ReturnValue1 = Variable4 * stats.StatIntervalTime
        
        stats = None
        item = None
        ReturnValue_4 = Default__FGPowerCircuit.GetGraphPointAtIndex(Variable4, Ref[stats], Ref[item])
        ReturnValue2_1: Vector2D = Vector2D(ReturnValue1, item.Produced)
        
        ReturnValue1_0: int32 = productionPoints.append(ReturnValue2_1)
        ReturnValue_0 = self.GetPowerCircuit()
        
        stats = None
        ReturnValue_0.GetStats(Ref[stats])
        ReturnValue1 = Variable4 * stats.StatIntervalTime
        
        stats = None
        item = None
        ReturnValue_4 = Default__FGPowerCircuit.GetGraphPointAtIndex(Variable4, Ref[stats], Ref[item])
        ReturnValue1_1: Vector2D = Vector2D(ReturnValue1, item.ProductionCapacity)
        
        ReturnValue_5: int32 = capacityPoints.append(ReturnValue1_1)
        ReturnValue_0 = self.GetPowerCircuit()
        
        stats = None
        ReturnValue_0.GetStats(Ref[stats])
        
        stats = None
        item = None
        ReturnValue_4 = Default__FGPowerCircuit.GetGraphPointAtIndex(Variable4, Ref[stats], Ref[item])
        ReturnValue1_2: bool = item.ProductionCapacity > capacityMax
        if not ReturnValue1_2:
           goto(ExecutionFlow.Pop())
        ReturnValue_0 = self.GetPowerCircuit()
        
        stats = None
        ReturnValue_0.GetStats(Ref[stats])
        
        stats = None
        item = None
        ReturnValue_4 = Default__FGPowerCircuit.GetGraphPointAtIndex(Variable4, Ref[stats], Ref[item])
        capacityMax = item.ProductionCapacity
        goto(ExecutionFlow.Pop())
        # Label 1610
        # End
        # Label 1615
        Variable3: int32 = 0
        # Label 1638
        ReturnValue1_3: bool = Variable3 <= 2
        if not ReturnValue1_3:
            goto('L3854')
        ExecutionFlow.Push("L3780")
        ReturnValue_6: SlateColor = self.GetCapacityColorAndOpacity()
        GraphCurve.Color_10_60E36C364D08C282508165B980658169 = ReturnValue_6.SpecifiedColor
        GraphCurve.Points_11_7F825CE44C5C364A4E1F71B0D820C91E = capacityPoints
        GraphCurve.OffsetY_14_0BB8215B4F827D9DCB6242B85AC85100 = 0
        ReturnValue_7: SlateColor = self.GetProductionColorAndOpacity()
        ReturnValue_8: SlateColor = self.GetConsumptionColorAndOpacity()
        GraphCurve1.Color_10_60E36C364D08C282508165B980658169 = ReturnValue_7.SpecifiedColor
        GraphCurve1.Points_11_7F825CE44C5C364A4E1F71B0D820C91E = productionPoints
        GraphCurve1.OffsetY_14_0BB8215B4F827D9DCB6242B85AC85100 = -2
        GraphCurve2.Color_10_60E36C364D08C282508165B980658169 = ReturnValue_8.SpecifiedColor
        GraphCurve2.Points_11_7F825CE44C5C364A4E1F71B0D820C91E = consumptionPoints
        GraphCurve2.OffsetY_14_0BB8215B4F827D9DCB6242B85AC85100 = -4
        ReturnValue_9: bool = self.mCapacityButton.IsHovered()
        ReturnValue1_4: bool = self.mConsumptionButton.IsHovered()
        ReturnValue2_2: bool = self.mProductionButton.IsHovered()
        ReturnValue_10: bool = BooleanOR(ReturnValue_9, ReturnValue2_2)
        ReturnValue1_5: bool = BooleanOR(ReturnValue_10, ReturnValue1_4)
        Variable2: int32 = 2
        Variable1: int32 = Variable3
        
        switch = {
            0: GraphCurve,
            1: GraphCurve1,
            2: GraphCurve2
        }
        LinearColor.R = switch.get(Variable1, None).Color_10_60E36C364D08C282508165B980658169.R
        
        switch_0 = {
            0: GraphCurve,
            1: GraphCurve1,
            2: GraphCurve2
        }
        LinearColor.G = switch_0.get(Variable1, None).Color_10_60E36C364D08C282508165B980658169.G
        
        switch_1 = {
            0: GraphCurve,
            1: GraphCurve1,
            2: GraphCurve2
        }
        LinearColor.B = switch_1.get(Variable1, None).Color_10_60E36C364D08C282508165B980658169.B
        LinearColor.A = 0.10000000149011612
        Variable: int32 = Variable3
        ReturnValue1_6: int32 = Variable3 + HoverIndexOffset
        
        switch_2 = {
            0: self.mCapacityButton,
            1: self.mProductionButton,
            2: self.mConsumptionButton
        }
        ReturnValue3_0: bool = switch_2.get(Variable, None).IsHovered()
        ReturnValue_11: bool = Not_PreBool(ReturnValue3_0)
        ReturnValue_12: bool = ReturnValue_11 and ReturnValue1_5
        Variable_0: bool = ReturnValue_12
        
        switch_3 = {
            0: GraphCurve,
            1: GraphCurve1,
            2: GraphCurve2
        }
        
        switch_4 = {
            False: switch_3.get(Variable1, None).Color_10_60E36C364D08C282508165B980658169,
            True: LinearColor
        }
        GraphCurve3.Color_10_60E36C364D08C282508165B980658169 = switch_4.get(Variable_0, None)
        
        switch_5 = {
            0: GraphCurve,
            1: GraphCurve1,
            2: GraphCurve2
        }
        GraphCurve3.Points_11_7F825CE44C5C364A4E1F71B0D820C91E = switch_5.get(Variable1, None).Points_11_7F825CE44C5C364A4E1F71B0D820C91E
        
        switch_6 = {
            0: GraphCurve,
            1: GraphCurve1,
            2: GraphCurve2
        }
        GraphCurve3.OffsetY_14_0BB8215B4F827D9DCB6242B85AC85100 = switch_6.get(Variable1, None).OffsetY_14_0BB8215B4F827D9DCB6242B85AC85100
        Variable1_0: bool = ReturnValue3_0
        
        switch_7 = {
            False: ReturnValue1_6,
            True: Variable2
        }
        
        self.mGraph.mCurves = None
        GraphCurve3 = None
        Default__KismetArrayLibrary.Array_Set(switch_7.get(Variable1_0, None), True, Ref[self.mGraph.mCurves], Ref[GraphCurve3])
        Variable = Variable3
        
        switch_8 = {
            0: self.mCapacityButton,
            1: self.mProductionButton,
            2: self.mConsumptionButton
        }
        ReturnValue3_0 = switch_8.get(Variable, None).IsHovered()
        if not ReturnValue3_0:
           goto(ExecutionFlow.Pop())
        HoverIndexOffset = -1
        goto(ExecutionFlow.Pop())
        # Label 3780
        ReturnValue2_3: int32 = Variable3 + 1
        Variable3 = ReturnValue2_3
        goto('L1638')
        # Label 3854
        ReturnValue1_7: Ptr[FGPowerCircuit] = self.GetPowerCircuit()
        
        stats1 = None
        ReturnValue1_7.GetStats(Ref[stats1])
        ReturnValue_13: float = capacityMax / 100
        ReturnValue_14: int32 = FCeil(ReturnValue_13)
        ReturnValue_15: float = ReturnValue_14 * 100
        ReturnValue_16: float = ReturnValue_15 + 25
        ReturnValue_17: float = ReturnValue_15 - capacityMax
        ReturnValue_18: bool = ReturnValue_17 > 25
        ReturnValue_19: float = SelectFloat(ReturnValue_15, ReturnValue_16, ReturnValue_18)
        ReturnValue_20: Vector2D = Vector2D(stats1.StatHistoryTime, ReturnValue_19)
        self.mGraph.mAxisMax = ReturnValue_20
        # End
        # Label 4322
        ReturnValue_21: int32 = Variable4 + 1
        Variable4 = ReturnValue_21
        goto('L113')
    

    def GetCapacityColorAndOpacity(self):
        SlateColor.SpecifiedColor = LinearColor(R = 0.421875, G = 0.417246013879776, B = 0.417246013879776, A = 1)
        SlateColor.ColorUseRule = 0
        ReturnValue = SlateColor
    

    def GetProductionColorAndOpacity(self):
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        ReturnValue = Text
    

    def GetConsumptionColorAndOpacity(self):
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        ReturnValue = OrangeText
    

    def Tick(self):
        ExecuteUbergraph_Widget_PowerCircuitGraph.K2Node_Event_MyGeometry = MyGeometry #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_PowerCircuitGraph.K2Node_Event_InDeltaTime = InDeltaTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_PowerCircuitGraph(29)
    

    def BndEvt__mConsumptionButton_K2Node_ComponentBoundEvent_0_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PowerCircuitGraph(270)
    

    def BndEvt__mProductionButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PowerCircuitGraph(308)
    

    def BndEvt__mCapacityButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PowerCircuitGraph(346)
    

    def BndEvt__mCapacityButton_K2Node_ComponentBoundEvent_3_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PowerCircuitGraph(384)
    

    def BndEvt__mProductionButton_K2Node_ComponentBoundEvent_4_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PowerCircuitGraph(422)
    

    def BndEvt__mConsumptionButton_K2Node_ComponentBoundEvent_5_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_PowerCircuitGraph(460)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_PowerCircuitGraph(498)
    

    def ExecuteUbergraph_Widget_PowerCircuitGraph(self):
        # Label 10
        self.UpdateStats()
        # End
        self.Tick(MyGeometry, InDeltaTime)
        self.UpdatePoints()
        Variable: uint8 = 3
        Variable1: uint8 = 2
        ReturnValue: bool = self.mGraph.IsHovered()
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mPointer.SetVisibility(switch.get(Variable_0, None))
        goto('L10')
        self.SetHoverStyle(self.mConsumptionText, self.mConsumptionTextBG, True)
        # End
        self.SetHoverStyle(self.mProductionText, self.mProductionTextBG, True)
        # End
        self.SetHoverStyle(self.mCapacityText, self.mCapacityTextBG, True)
        # End
        self.SetHoverStyle(self.mCapacityText, self.mCapacityTextBG, False)
        # End
        self.SetHoverStyle(self.mProductionText, self.mProductionTextBG, False)
        # End
        self.SetHoverStyle(self.mConsumptionText, self.mConsumptionTextBG, False)
        # End
        ReturnValue_0: SlateColor = self.GetConsumptionColorAndOpacity()
        self.mConsumptionHover.SetColorAndOpacity(ReturnValue_0)
        ReturnValue_1: SlateColor = self.GetProductionColorAndOpacity()
        self.mProductionHover.SetColorAndOpacity(ReturnValue_1)
        ReturnValue_2: SlateColor = self.GetCapacityColorAndOpacity()
        self.mCapacityHover.SetColorAndOpacity(ReturnValue_2)
    
