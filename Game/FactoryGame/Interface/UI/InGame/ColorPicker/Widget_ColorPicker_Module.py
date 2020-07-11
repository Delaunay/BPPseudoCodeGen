
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker_Module import ExecuteUbergraph_Widget_ColorPicker_Module.K2Node_ComponentBoundEvent_Value
from Script.Engine import RGBToHSV
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker_Module import ExecuteUbergraph_Widget_ColorPicker_Module.K2Node_CustomEvent_Color
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker_Module import ExecuteUbergraph_Widget_ColorPicker_Module.K2Node_ComponentBoundEvent_Value2
from Script.Engine import HSVToRGB
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker_Module import ExecuteUbergraph_Widget_ColorPicker_Module
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker_Module import ExecuteUbergraph_Widget_ColorPicker_Module.K2Node_ComponentBoundEvent_Value1
from Script.UMG import SetColorAndOpacity
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class Widget_ColorPicker_Module(UserWidget):
    mHue: float
    mSaturation: float
    mBrightness: float
    CurrentColor: LinearColor = Namespace(A=1, B=0, G=1, R=0)
    StartColor: LinearColor
    OnValueChanged: FMulticastScriptDelegate
    
    def SetAndUpdateColor(self):
        ReturnValue: LinearColor = HSVToRGB(self.mHue, self.mSaturation, self.mBrightness, 1)
        self.CurrentColor = ReturnValue
        self.mPreview.SetColorAndOpacity(self.CurrentColor)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ColorPicker_Module(569)
    

    def BndEvt__Widget_ColorPicker_Slider_K2Node_ComponentBoundEvent_0_OnValueChanged__DelegateSignature(self, Value: float):
        ExecuteUbergraph_Widget_ColorPicker_Module.K2Node_ComponentBoundEvent_Value2 = Value #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorPicker_Module(597)
    

    def BndEvt__mBrightnessSlider_K2Node_ComponentBoundEvent_1_OnValueChanged__DelegateSignature(self, Value: float):
        ExecuteUbergraph_Widget_ColorPicker_Module.K2Node_ComponentBoundEvent_Value1 = Value #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorPicker_Module(770)
    

    def BndEvt__mSaturationSlider_K2Node_ComponentBoundEvent_2_OnValueChanged__DelegateSignature(self, Value: float):
        ExecuteUbergraph_Widget_ColorPicker_Module.K2Node_ComponentBoundEvent_Value = Value #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorPicker_Module(870)
    

    def SetupColorAndSliders(self, Color: LinearColor):
        ExecuteUbergraph_Widget_ColorPicker_Module.K2Node_CustomEvent_Color = Color #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorPicker_Module(989)
    

    def ExecuteUbergraph_Widget_ColorPicker_Module(self):
        # Label 10
        self.OnValueChanged.ProcessMulticastDelegate()
        # End
        # Label 34
        self.CurrentColor = self.StartColor
        
        H = None
        S = None
        V = None
        A = None
        RGBToHSV(self.CurrentColor, Ref[H], Ref[S], Ref[V], Ref[A])
        self.mHue = H
        
        H = None
        S = None
        V = None
        A = None
        RGBToHSV(self.CurrentColor, Ref[H], Ref[S], Ref[V], Ref[A])
        self.mSaturation = S
        
        H = None
        S = None
        V = None
        A = None
        RGBToHSV(self.CurrentColor, Ref[H], Ref[S], Ref[V], Ref[A])
        self.mBrightness = V
        self.mSaturationSlider.UpdateSliderMaterial(self.mHue, self.mBrightness)
        self.mBrightnessSlider.UpdateSliderMaterial(self.mHue, self.mSaturation)
        self.mHueSlider.UpdateSliderValue(self.mHue)
        self.mSaturationSlider.UpdateSliderValue(self.mSaturation)
        self.mBrightnessSlider.UpdateSliderValue(self.mBrightness)
        self.SetAndUpdateColor()
        # End
        self.SetupColorAndSliders(self.StartColor)
        # End
        self.mHue = Value2
        self.mSaturationSlider.UpdateSliderMaterial(self.mHue, self.mBrightness)
        self.mBrightnessSlider.UpdateSliderMaterial(self.mHue, self.mSaturation)
        self.SetAndUpdateColor()
        self.OnValueChanged.ProcessMulticastDelegate()
        # End
        self.mBrightness = Value1
        self.mSaturationSlider.UpdateSliderMaterial(self.mHue, self.mBrightness)
        self.SetAndUpdateColor()
        goto('L10')
        self.mSaturation = Value
        self.mBrightnessSlider.UpdateSliderMaterial(self.mHue, self.mSaturation)
        self.SetAndUpdateColor()
        self.OnValueChanged.ProcessMulticastDelegate()
        # End
        self.StartColor = Color
        goto('L34')
    

    def OnValueChanged__DelegateSignature(self):
        pass
    
