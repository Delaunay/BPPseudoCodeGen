
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Script.Engine import EqualEqual_ByteByte
from Script.Engine import Conv_IntToFloat
from Script.Engine import FTrunc
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import Conv_FloatToText
from Script.Engine import IsValid
from Script.Engine import HSVToRGB
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Default__KismetTextLibrary
from Script.Engine import FMax
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_SaturationSlider import ExecuteUbergraph_Widget_SaturationSlider
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker import Widget_ColorPicker
from Script.Engine import Conv_StringToInt
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_SaturationSlider import ExecuteUbergraph_Widget_SaturationSlider.K2Node_ComponentBoundEvent_Text
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import DrawLine
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_SaturationSlider import ExecuteUbergraph_Widget_SaturationSlider.K2Node_ComponentBoundEvent_Value
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_SaturationSlider import ExecuteUbergraph_Widget_SaturationSlider.K2Node_ComponentBoundEvent_CommitMethod
from Script.CoreUObject import Vector2D
from Script.CoreUObject import LinearColor

class Widget_SaturationSlider(UserWidget):
    mColorPicker: Ptr[Widget_ColorPicker]
    
    def GetSliderValue(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mColorPicker)
        if not ReturnValue:
            goto('L119')
        ReturnValue_0: float = self.mColorPicker.mSaturationValue
        goto('L142')
        # Label 119
        ReturnValue_0 = 0
    

    def GetInputText(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mColorPicker)
        if not ReturnValue:
            goto('L202')
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_FloatToText(self.mColorPicker.mSaturationValue, 0, False, True, 1, 1, 3, 3)
        ReturnValue_1: FText = ReturnValue_0
        goto('L222')
        # Label 202
        ReturnValue_1 = 
    

    def OnPaint(self):
        ExecutionFlow.Push("L832")
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mColorPicker)
        if not ReturnValue:
           goto(ExecutionFlow.Pop())
        Variable: int32 = 0
        # Label 89
        ReturnValue_0: int32 = FTrunc(self.mSliderSizeBox.WidthOverride)
        ReturnValue_1: int32 = ReturnValue_0 - 1
        ReturnValue_2: bool = Variable <= ReturnValue_1
        if not ReturnValue_2:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L758")
        ReturnValue_3: float = self.mSliderSizeBox.WidthOverride - 1
        ReturnValue_4: float = self.mSliderSizeBox.HeightOverride / 2
        ReturnValue_5: float = Conv_IntToFloat(Variable)
        ReturnValue1: float = ReturnValue_5 / ReturnValue_3
        ReturnValue1_0: float = Conv_IntToFloat(Variable)
        ReturnValue_6: LinearColor = HSVToRGB(self.mColorPicker.mHueValue, ReturnValue1, self.mColorPicker.mValueValue, 1)
        ReturnValue_7: Vector2D = Vector2D(ReturnValue1_0, 0)
        ReturnValue1_1: Vector2D = Vector2D(ReturnValue1_0, ReturnValue_4)
        
        Default__WidgetBlueprintLibrary.DrawLine(ReturnValue_7, ReturnValue1_1, ReturnValue_6, True, 1, Ref[Context])
        goto(ExecutionFlow.Pop())
        # Label 758
        ReturnValue_8: int32 = Variable + 1
        Variable = ReturnValue_8
        goto('L89')
    

    def BndEvt__Slider_0_K2Node_ComponentBoundEvent_109_OnFloatValueChangedEvent__DelegateSignature(self, Value: float):
        ExecuteUbergraph_Widget_SaturationSlider.K2Node_ComponentBoundEvent_Value = Value #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SaturationSlider(10)
    

    def BndEvt__mInputText_K2Node_ComponentBoundEvent_270_OnEditableTextBoxCommittedEvent__DelegateSignature(self, text: Const[Ref[FText]], CommitMethod: uint8):
        ExecuteUbergraph_Widget_SaturationSlider.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_SaturationSlider.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SaturationSlider(132)
    

    def ExecuteUbergraph_Widget_SaturationSlider(self):
        ReturnValue1: float = FMax(Value, self.mColorPicker.mShadeExtremeCutoff)
        self.mColorPicker.mSaturationValue = ReturnValue1
        # End
        ReturnValue: bool = EqualEqual_ByteByte(CommitMethod, 1)
        if not ReturnValue:
            goto('L449')
        
        Text = None
        ReturnValue_0: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Text])
        ReturnValue_1: int32 = Default__KismetStringLibrary.Conv_StringToInt(ReturnValue_0)
        ReturnValue_2: float = Conv_IntToFloat(ReturnValue_1)
        ReturnValue_3: float = FMax(ReturnValue_2, self.mColorPicker.mShadeExtremeCutoff)
        self.mColorPicker.mSaturationValue = ReturnValue_3
    
