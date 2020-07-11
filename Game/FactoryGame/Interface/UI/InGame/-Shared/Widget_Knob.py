
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Knob import ExecuteUbergraph_Widget_Knob.K2Node_CustomEvent_Value
from Script.UMG import SetRenderTranslation
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Knob import ExecuteUbergraph_Widget_Knob
from Script.Engine import FClamp
from Script.UMG import SetRenderAngle
from Script.CoreUObject import Vector2D
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_Knob import ExecuteUbergraph_Widget_Knob.K2Node_ComponentBoundEvent_Value
from Script.UMG import SetValue
from Script.UMG import UserWidget

class Widget_Knob(UserWidget):
    mValue: float
    OrgValue: float
    ValueChanged: bool
    
    def BndEvt__ValueSlider_K2Node_ComponentBoundEvent_1_OnFloatValueChangedEvent__DelegateSignature(self, Value: float):
        ExecuteUbergraph_Widget_Knob.K2Node_ComponentBoundEvent_Value = Value #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Knob(10)
    

    def SetupValue(self, Value: float):
        ExecuteUbergraph_Widget_Knob.K2Node_CustomEvent_Value = Value #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Knob(734)
    

    def BndEvt__Slider_75_K2Node_ComponentBoundEvent_0_OnMouseCaptureEndEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Knob(1428)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Knob(1470)
    

    def ExecuteUbergraph_Widget_Knob(self):
        if not self.ValueChanged:
            goto('L691')
        # Label 24
        ReturnValue6: float = Value * 2
        ReturnValue: float = ReturnValue6 - 1
        ReturnValue_0: float = self.OrgValue + ReturnValue
        ReturnValue1: float = FClamp(ReturnValue_0, 0, 1)
        self.mValue = ReturnValue1
        ReturnValue_1: float = self.mValue * 360
        self.Top.SetRenderAngle(ReturnValue_1)
        ReturnValue_1 = self.mValue * 360
        self.PointerContainer.SetRenderAngle(ReturnValue_1)
        ReturnValue_1 = self.mValue * 360
        ReturnValue2: float = ReturnValue_1 * -1
        self.Pointer.SetRenderAngle(ReturnValue2)
        ReturnValue_1 = self.mValue * 360
        ReturnValue5: float = ReturnValue_1 * -0.925000011920929
        ReturnValue1_0: Vector2D = Vector2D(ReturnValue5, 0)
        self.Side.SetRenderTranslation(ReturnValue1_0)
        # End
        # Label 691
        self.OrgValue = self.mValue
        self.ValueChanged = True
        goto('L24')
        self.mValue = Value
        ReturnValue_2: float = FClamp(self.mValue, 0, 1)
        ReturnValue1_1: float = ReturnValue_2 * 360
        self.Top.SetRenderAngle(ReturnValue1_1)
        ReturnValue_2 = FClamp(self.mValue, 0, 1)
        ReturnValue1_1 = ReturnValue_2 * 360
        self.PointerContainer.SetRenderAngle(ReturnValue1_1)
        ReturnValue_2 = FClamp(self.mValue, 0, 1)
        ReturnValue1_1 = ReturnValue_2 * 360
        ReturnValue3: float = ReturnValue1_1 * -1
        self.Pointer.SetRenderAngle(ReturnValue3)
        ReturnValue_2 = FClamp(self.mValue, 0, 1)
        ReturnValue1_1 = ReturnValue_2 * 360
        ReturnValue4: float = ReturnValue1_1 * -0.925000011920929
        ReturnValue_3: Vector2D = Vector2D(ReturnValue4, 0)
        self.Side.SetRenderTranslation(ReturnValue_3)
        # End
        # Label 1412
        self.ValueChanged = False
        # End
        self.mValueSlider.SetValue(0.5)
        goto('L1412')
    
