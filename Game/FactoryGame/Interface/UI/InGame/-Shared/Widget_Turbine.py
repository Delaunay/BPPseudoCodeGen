
from codegen.ue4_stub import *

from Script.Engine import Lerp
from Script.UMG import CanvasPanelSlot
from Script.Engine import K2_SetTimerDelegate
from Script.UMG import GetChildrenCount
from Script.UMG import Default__WidgetLayoutLibrary
from Script.UMG import SlotAsCanvasSlot
from Script.Engine import Conv_IntToFloat
from Script.SlateCore import Margin
from Script.Engine import Not_PreBool
from Script.Engine import Ease
from Script.Engine import Default__KismetSystemLibrary
from Script.UMG import GetChildAt
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Turbine import ExecuteUbergraph_Widget_Turbine.K2Node_Event_IsDesignTime
from Script.Engine import TimerHandle
from Script.Engine import IsValid
from Script.UMG import SetBrushSize
from Script.UMG import SetColorAndOpacity
from Script.UMG import SetHeightOverride
from Script.Engine import EqualEqual_IntInt
from Script.UMG import SetOpacity
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Turbine import ExecuteUbergraph_Widget_Turbine
from Script.UMG import CanvasPanel
from Script.UMG import Widget
from Script.UMG import SizeBox
from Script.Engine import EqualEqual_ObjectObject
from Script.UMG import Overlay
from Script.UMG import UserWidget
from Script.UMG import Image
from Script.UMG import SetOffsets
from Script.UMG import SetBrushTintColor
from Script.CoreUObject import Vector2D
from Script.UMG import ScaleBox
from Script.Engine import K2_ClearAndInvalidateTimerHandle

class Widget_Turbine(UserWidget):
    mT: float
    mUpdateTime: float = 0.009999999776482582
    mTurnTimer: TimerHandle
    mSpeed: float = 0.5
    mSizes: float
    mTurnsUp: bool
    
    def TurnTurbine(self, Container: Ptr[PanelWidget]):
        ExecutionFlow.Push("L7614")
        Variable2: int32 = 0
        # Label 28
        ReturnValue: int32 = Container.GetChildrenCount()
        ReturnValue_0: bool = Variable2 <= ReturnValue
        if not ReturnValue_0:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L7418")
        ReturnValue_1: Ptr[Widget] = Container.GetChildAt(Variable2)
        ReturnValue_2: bool = Default__KismetSystemLibrary.IsValid(ReturnValue_1)
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        ReturnValue_1 = Container.GetChildAt(Variable2)
        Panel: Ptr[CanvasPanel] = Cast[CanvasPanel](ReturnValue_1)
        bSuccess: bool = Panel
        if not bSuccess:
           goto(ExecutionFlow.Pop())
        LocalCanvas = Panel
        ReturnValue2: Ptr[Widget] = LocalCanvas.GetChildAt(0)
        AsImage: Ptr[Image] = Cast[Image](ReturnValue2)
        bSuccess2: bool = AsImage
        if not bSuccess2:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        Variable1: int32 = 1
        ReturnValue1: bool = EqualEqual_ObjectObject(Container, self.mTopContainer)
        ReturnValue_3: float = Lerp(0, 1, self.mT)
        Variable1_0: bool = ReturnValue1
        ReturnValue2_0: bool = EqualEqual_ObjectObject(Container, self.mTopContainer)
        ReturnValue2_1: int32 = self.mTopContainer.GetChildrenCount()
        Variable2_0: bool = ReturnValue2_0
        ReturnValue_4: float = Conv_IntToFloat(ReturnValue2_1)
        ReturnValue1_0: float = Lerp(0, -1, self.mT)
        ReturnValue3: int32 = self.mTopContainer.GetChildrenCount()
        ReturnValue1_1: int32 = ReturnValue3 - Variable2
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue2_2: int32 = ReturnValue1_1 - switch.get(Variable1_0, None)
        ReturnValue1_2: float = Conv_IntToFloat(ReturnValue2_2)
        ReturnValue_5: float = self.mTurbineSizeBox.HeightOverride / 2
        
        switch_0 = {
            False: ReturnValue_3,
            True: ReturnValue1_0
        }
        ReturnValue_6: float = ReturnValue1_2 + switch_0.get(Variable2_0, None)
        ReturnValue1_3: float = ReturnValue_6 / ReturnValue_4
        ReturnValue3_0: float = Ease(0, ReturnValue_5, ReturnValue1_3, 3, 2, 2)
        ReturnValue_7: Vector2D = Vector2D(0, ReturnValue3_0)
        AsImage.SetBrushSize(ReturnValue_7)
        Variable = 0
        Variable1 = 1
        ReturnValue1 = EqualEqual_ObjectObject(Container, self.mTopContainer)
        ReturnValue_3 = Lerp(0, 1, self.mT)
        Variable1_0 = ReturnValue1
        ReturnValue2_0 = EqualEqual_ObjectObject(Container, self.mTopContainer)
        ReturnValue2_1 = self.mTopContainer.GetChildrenCount()
        Variable2_0 = ReturnValue2_0
        ReturnValue_4 = Conv_IntToFloat(ReturnValue2_1)
        ReturnValue1_0 = Lerp(0, -1, self.mT)
        ReturnValue3 = self.mTopContainer.GetChildrenCount()
        ReturnValue1_1 = ReturnValue3 - Variable2
        
        switch_1 = {
            False: Variable1,
            True: Variable
        }
        ReturnValue2_2 = ReturnValue1_1 - switch_1.get(Variable1_0, None)
        ReturnValue1_2 = Conv_IntToFloat(ReturnValue2_2)
        
        switch_2 = {
            False: ReturnValue_3,
            True: ReturnValue1_0
        }
        ReturnValue_6 = ReturnValue1_2 + switch_2.get(Variable2_0, None)
        ReturnValue1_3 = ReturnValue_6 / ReturnValue_4
        ReturnValue_8: float = 1 - ReturnValue1_3
        LinearColor1.R = AsImage.Brush.TintColor.SpecifiedColor.R
        LinearColor1.G = AsImage.Brush.TintColor.SpecifiedColor.G
        LinearColor1.B = AsImage.Brush.TintColor.SpecifiedColor.B
        LinearColor1.A = ReturnValue_8
        SlateColor.SpecifiedColor = LinearColor1
        SlateColor.ColorUseRule = AsImage.Brush.TintColor.ColorUseRule
        AsImage.SetBrushTintColor(SlateColor)
        ReturnValue1_4: int32 = self.mTopContainer.GetChildrenCount()
        ReturnValue_9: int32 = ReturnValue1_4 - 1
        ReturnValue_10: bool = EqualEqual_IntInt(Variable2, ReturnValue_9)
        ReturnValue_11: bool = Not_PreBool(ReturnValue_10)
        if not ReturnValue_11:
            goto('L7492')
        Variable = 0
        Variable1 = 1
        ReturnValue_12: bool = EqualEqual_ObjectObject(Container, self.mTopContainer)
        Variable_0: bool = ReturnValue_12
        ReturnValue_13: Ptr[CanvasPanelSlot] = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(AsImage)
        ReturnValue1 = EqualEqual_ObjectObject(Container, self.mTopContainer)
        ReturnValue_3 = Lerp(0, 1, self.mT)
        Variable1_0 = ReturnValue1
        ReturnValue2_0 = EqualEqual_ObjectObject(Container, self.mTopContainer)
        ReturnValue2_1 = self.mTopContainer.GetChildrenCount()
        Variable2_0 = ReturnValue2_0
        ReturnValue_4 = Conv_IntToFloat(ReturnValue2_1)
        ReturnValue1_0 = Lerp(0, -1, self.mT)
        ReturnValue3 = self.mTopContainer.GetChildrenCount()
        ReturnValue1_1 = ReturnValue3 - Variable2
        
        switch_3 = {
            False: Variable1,
            True: Variable
        }
        ReturnValue2_2 = ReturnValue1_1 - switch_3.get(Variable1_0, None)
        ReturnValue1_2 = Conv_IntToFloat(ReturnValue2_2)
        ReturnValue_5 = self.mTurbineSizeBox.HeightOverride / 2
        
        switch_4 = {
            False: ReturnValue_3,
            True: ReturnValue1_0
        }
        ReturnValue_6 = ReturnValue1_2 + switch_4.get(Variable2_0, None)
        ReturnValue1_5: float = ReturnValue_6 + -1
        ReturnValue2_3: float = ReturnValue1_5 / ReturnValue_4
        ReturnValue1_6: float = Ease(0, ReturnValue_5, ReturnValue2_3, 3, 2, 2)
        Margin.Left = 0
        Margin.Top = 0
        Margin.Right = 0
        Margin.Bottom = ReturnValue1_6
        Margin1.Left = 0
        Margin1.Top = ReturnValue1_6
        Margin1.Right = 0
        Margin1.Bottom = 0
        
        switch_5 = {
            False: Margin1,
            True: Margin
        }
        ReturnValue_13.SetOffsets(switch_5.get(Variable_0, None))
        # Label 4105
        ReturnValue1_7: Ptr[Widget] = LocalCanvas.GetChildAt(1)
        Box: Ptr[SizeBox] = Cast[SizeBox](ReturnValue1_7)
        bSuccess1: bool = Box
        if not bSuccess1:
           goto(ExecutionFlow.Pop())
        ReturnValue3_1: Ptr[Widget] = Box.GetChildAt(0)
        Box_0: Ptr[ScaleBox] = Cast[ScaleBox](ReturnValue3_1)
        bSuccess3: bool = Box_0
        if not bSuccess3:
           goto(ExecutionFlow.Pop())
        ReturnValue4: Ptr[Widget] = Box_0.GetChildAt(0)
        AsOverlay: Ptr[Overlay] = Cast[Overlay](ReturnValue4)
        bSuccess4: bool = AsOverlay
        if not bSuccess4:
           goto(ExecutionFlow.Pop())
        ReturnValue6: Ptr[Widget] = AsOverlay.GetChildAt(0)
        AsImage2: Ptr[Image] = Cast[Image](ReturnValue6)
        bSuccess6: bool = AsImage2
        if not bSuccess6:
           goto(ExecutionFlow.Pop())
        Variable = 0
        Variable1 = 1
        ReturnValue1 = EqualEqual_ObjectObject(Container, self.mTopContainer)
        ReturnValue_3 = Lerp(0, 1, self.mT)
        Variable1_0 = ReturnValue1
        ReturnValue2_0 = EqualEqual_ObjectObject(Container, self.mTopContainer)
        ReturnValue2_1 = self.mTopContainer.GetChildrenCount()
        Variable2_0 = ReturnValue2_0
        ReturnValue_4 = Conv_IntToFloat(ReturnValue2_1)
        ReturnValue1_0 = Lerp(0, -1, self.mT)
        ReturnValue3 = self.mTopContainer.GetChildrenCount()
        ReturnValue1_1 = ReturnValue3 - Variable2
        
        switch_6 = {
            False: Variable1,
            True: Variable
        }
        ReturnValue2_2 = ReturnValue1_1 - switch_6.get(Variable1_0, None)
        ReturnValue1_2 = Conv_IntToFloat(ReturnValue2_2)
        
        switch_7 = {
            False: ReturnValue_3,
            True: ReturnValue1_0
        }
        ReturnValue_6 = ReturnValue1_2 + switch_7.get(Variable2_0, None)
        ReturnValue1_3 = ReturnValue_6 / ReturnValue_4
        ReturnValue2_4: float = Ease(0.5, 0, ReturnValue1_3, 3, 2, 2)
        LinearColor.R = ReturnValue2_4
        LinearColor.G = ReturnValue2_4
        LinearColor.B = ReturnValue2_4
        LinearColor.A = 1
        AsImage2.SetColorAndOpacity(LinearColor)
        ReturnValue5: Ptr[Widget] = AsOverlay.GetChildAt(1)
        AsImage1: Ptr[Image] = Cast[Image](ReturnValue5)
        bSuccess5: bool = AsImage1
        if not bSuccess5:
           goto(ExecutionFlow.Pop())
        Variable = 0
        Variable1 = 1
        ReturnValue1 = EqualEqual_ObjectObject(Container, self.mTopContainer)
        ReturnValue_3 = Lerp(0, 1, self.mT)
        Variable1_0 = ReturnValue1
        ReturnValue2_0 = EqualEqual_ObjectObject(Container, self.mTopContainer)
        ReturnValue2_1 = self.mTopContainer.GetChildrenCount()
        Variable2_0 = ReturnValue2_0
        ReturnValue_4 = Conv_IntToFloat(ReturnValue2_1)
        ReturnValue1_0 = Lerp(0, -1, self.mT)
        ReturnValue3 = self.mTopContainer.GetChildrenCount()
        ReturnValue1_1 = ReturnValue3 - Variable2
        
        switch_8 = {
            False: Variable1,
            True: Variable
        }
        ReturnValue2_2 = ReturnValue1_1 - switch_8.get(Variable1_0, None)
        ReturnValue1_2 = Conv_IntToFloat(ReturnValue2_2)
        
        switch_9 = {
            False: ReturnValue_3,
            True: ReturnValue1_0
        }
        ReturnValue_6 = ReturnValue1_2 + switch_9.get(Variable2_0, None)
        ReturnValue1_3 = ReturnValue_6 / ReturnValue_4
        ReturnValue_14: float = Ease(0.699999988079071, 0, ReturnValue1_3, 3, 2, 2)
        AsImage1.SetOpacity(ReturnValue_14)
        Variable = 0
        Variable1 = 1
        Variable_1: float = 0
        ReturnValue1 = EqualEqual_ObjectObject(Container, self.mTopContainer)
        ReturnValue_3 = Lerp(0, 1, self.mT)
        Variable1_0 = ReturnValue1
        ReturnValue2_0 = EqualEqual_ObjectObject(Container, self.mTopContainer)
        ReturnValue2_1 = self.mTopContainer.GetChildrenCount()
        Variable2_0 = ReturnValue2_0
        ReturnValue_4 = Conv_IntToFloat(ReturnValue2_1)
        ReturnValue1_0 = Lerp(0, -1, self.mT)
        ReturnValue3 = self.mTopContainer.GetChildrenCount()
        ReturnValue1_1 = ReturnValue3 - Variable2
        
        switch_10 = {
            False: Variable1,
            True: Variable
        }
        ReturnValue2_2 = ReturnValue1_1 - switch_10.get(Variable1_0, None)
        ReturnValue1_2 = Conv_IntToFloat(ReturnValue2_2)
        
        switch_11 = {
            False: ReturnValue_3,
            True: ReturnValue1_0
        }
        ReturnValue_6 = ReturnValue1_2 + switch_11.get(Variable2_0, None)
        ReturnValue1_3 = ReturnValue_6 / ReturnValue_4
        ReturnValue4_0: float = Ease(10, 0, ReturnValue1_3, 3, 2, 2)
        ReturnValue_15: bool = ReturnValue4_0 > 1
        Variable3: bool = ReturnValue_15
        
        switch_12 = {
            False: Variable_1,
            True: ReturnValue4_0
        }
        ReturnValue1_8: Vector2D = Vector2D(0, switch_12.get(Variable3, None))
        AsImage1.SetBrushSize(ReturnValue1_8)
        goto(ExecutionFlow.Pop())
        # Label 7418
        ReturnValue_16: int32 = Variable2 + 1
        Variable2 = ReturnValue_16
        goto('L28')
        # Label 7492
        ReturnValue_13 = Default__WidgetLayoutLibrary.SlotAsCanvasSlot(AsImage)
        ReturnValue_13.SetOffsets(Margin(Left = 0, Top = 0, Right = 0, Bottom = 0))
        goto('L4105')
    

    def TurnEvent(self):
        self.ExecuteUbergraph_Widget_Turbine(698)
    

    def Destruct(self):
        self.ExecuteUbergraph_Widget_Turbine(827)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Turbine(874)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_Turbine.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Turbine(879)
    

    def ExecuteUbergraph_Widget_Turbine(self):
        # Label 10
        ReturnValue: bool = self.mSpeed <= 0
        ReturnValue_0: bool = Not_PreBool(ReturnValue)
        if not ReturnValue_0:
            goto('L1071')
        self.TurnTurbine(self.mTopContainer)
        self.TurnTurbine(self.mBottomContainer)
        ReturnValue_1: bool = self.mT > 1
        Variable2: bool = self.mTurnsUp
        ReturnValue_2: bool = self.mT <= 0
        
        switch = {
            False: ReturnValue_1,
            True: ReturnValue_2
        }
        if not switch.get(Variable2, None):
            goto('L419')
        Variable: float = 1
        Variable1: float = 0
        Variable_0: bool = self.mTurnsUp
        
        switch_0 = {
            False: Variable1,
            True: Variable
        }
        self.mT = switch_0.get(Variable_0, None)
        # End
        # Label 419
        ReturnValue_3: float = self.mUpdateTime / self.mSpeed
        ReturnValue_4: float = self.mT + ReturnValue_3
        Variable1_0: bool = self.mTurnsUp
        ReturnValue2: float = self.mUpdateTime / self.mSpeed
        ReturnValue_5: float = self.mT - ReturnValue2
        
        switch_1 = {
            False: ReturnValue_4,
            True: ReturnValue_5
        }
        self.mT = switch_1.get(Variable1_0, None)
        # End
        goto('L10')
        # Label 703
        OutputDelegate.BindUFunction(self, TurnEvent)
        ReturnValue_6: TimerHandle = Default__KismetSystemLibrary.K2_SetTimerDelegate(OutputDelegate, self.mUpdateTime, True)
        self.mTurnTimer = ReturnValue_6
        # End
        
        Default__KismetSystemLibrary.K2_ClearAndInvalidateTimerHandle(self, Ref[self.mTurnTimer])
        # End
        goto('L703')
        self.TurnTurbine(self.mTopContainer)
        self.TurnTurbine(self.mBottomContainer)
        ReturnValue1: float = self.mTurbineSizeBox.HeightOverride / 2
        self.mBottomSizeBox.SetHeightOverride(ReturnValue1)
        self.mTopSizeBox.SetHeightOverride(ReturnValue1)
    
