
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_HueSlider import ExecuteUbergraph_Widget_HueSlider.K2Node_ComponentBoundEvent_CommitMethod
from Script.Engine import EqualEqual_ByteByte
from Script.Engine import Conv_IntToFloat
from Script.Engine import FTrunc
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_HueSlider import ExecuteUbergraph_Widget_HueSlider.K2Node_ComponentBoundEvent_Text
from Script.Engine import IsValid
from Script.Engine import HSVToRGB
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import Conv_IntToText
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker import Widget_ColorPicker
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_HueSlider import ExecuteUbergraph_Widget_HueSlider
from Script.Engine import Conv_StringToInt
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_HueSlider import ExecuteUbergraph_Widget_HueSlider.K2Node_ComponentBoundEvent_Value
from Script.Engine import Default__KismetStringLibrary
from Script.UMG import DrawLine
from Script.UMG import UserWidget
from Script.CoreUObject import Vector2D
from Script.Engine import Round
from Script.CoreUObject import LinearColor

class Widget_HueSlider(UserWidget):
    mColorPicker: Ptr[Widget_ColorPicker]
    
    def GetSliderValue(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mColorPicker)
        if not ReturnValue:
            goto('L161')
        ReturnValue_0: float = self.mColorPicker.mHueValue / 360
        ReturnValue_1: float = ReturnValue_0
        goto('L184')
        # Label 161
        ReturnValue_1 = 0
    

    def GetInputText(self):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(self.mColorPicker)
        if not ReturnValue:
            goto('L227')
        ReturnValue_0: int32 = Round(self.mColorPicker.mHueValue)
        ReturnValue_1: FText = Default__KismetTextLibrary.Conv_IntToText(ReturnValue_0, False, True, 1, 324)
        ReturnValue_2: FText = ReturnValue_1
        goto('L247')
        # Label 227
        ReturnValue_2 = 
    

    def OnPaint(self):
        ExecutionFlow.Push("L682")
        Variable: int32 = 0
        # Label 28
        ReturnValue: int32 = FTrunc(self.mSliderSizeBox.WidthOverride)
        ReturnValue_0: int32 = ReturnValue - 1
        ReturnValue_1: bool = Variable <= ReturnValue_0
        if not ReturnValue_1:
           goto(ExecutionFlow.Pop())
        ExecutionFlow.Push("L608")
        ReturnValue_2: float = 360 / self.mSliderSizeBox.WidthOverride
        ReturnValue1: float = self.mSliderSizeBox.HeightOverride / 2
        ReturnValue_3: float = Variable * ReturnValue_2
        ReturnValue_4: LinearColor = HSVToRGB(ReturnValue_3, 1, 1, 1)
        ReturnValue_5: float = Conv_IntToFloat(Variable)
        ReturnValue_6: Vector2D = Vector2D(ReturnValue_5, 0)
        ReturnValue1_0: Vector2D = Vector2D(ReturnValue_5, ReturnValue1)
        
        Default__WidgetBlueprintLibrary.DrawLine(ReturnValue_6, ReturnValue1_0, ReturnValue_4, True, 1, Ref[Context])
        goto(ExecutionFlow.Pop())
        # Label 608
        ReturnValue_7: int32 = Variable + 1
        Variable = ReturnValue_7
        goto('L28')
    

    def BndEvt__Slider_0_K2Node_ComponentBoundEvent_109_OnFloatValueChangedEvent__DelegateSignature(self, Value: float):
        ExecuteUbergraph_Widget_HueSlider.K2Node_ComponentBoundEvent_Value = Value #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_HueSlider(10)
    

    def BndEvt__mInputText_K2Node_ComponentBoundEvent_270_OnEditableTextBoxCommittedEvent__DelegateSignature(self, text: Const[Ref[FText]], CommitMethod: uint8):
        ExecuteUbergraph_Widget_HueSlider.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_HueSlider.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_HueSlider(106)
    

    def ExecuteUbergraph_Widget_HueSlider(self):
        ReturnValue: float = Value * 360
        self.mColorPicker.mHueValue = ReturnValue
        # End
        ReturnValue_0: bool = EqualEqual_ByteByte(CommitMethod, 1)
        if not ReturnValue_0:
            goto('L355')
        
        Text = None
        ReturnValue_1: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Text])
        ReturnValue_2: int32 = Default__KismetStringLibrary.Conv_StringToInt(ReturnValue_1)
        ReturnValue_3: float = Conv_IntToFloat(ReturnValue_2)
        self.mColorPicker.mHueValue = ReturnValue_3
    
