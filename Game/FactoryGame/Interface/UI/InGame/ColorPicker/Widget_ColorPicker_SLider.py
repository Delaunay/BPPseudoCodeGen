
from codegen.ue4_stub import *

from Script.Engine import SetScalarParameterValue
from Script.Engine import Conv_TextToString
from Script.Engine import EqualEqual_ByteByte
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker_SLider import ExecuteUbergraph_Widget_ColorPicker_Slider.K2Node_ComponentBoundEvent_Value
from Script.Engine import MaterialInstanceDynamic
from Script.Engine import Conv_IntToFloat
from Script.UMG import SetText
from Script.Engine import Conv_FloatToText
from Script.Engine import SetVectorParameterValue
from Script.Engine import HSVToRGB
from Script.UMG import SetValue
from Game.FactoryGame.Interface.UI.Material.Material_UI_ColorPicker_Hue import Material_UI_ColorPicker_Hue
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Enum_ColorPickerSliderType import Enum_ColorPickerSliderType
from Script.Engine import Default__KismetTextLibrary
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker_SLider import ExecuteUbergraph_Widget_ColorPicker_Slider
from Script.Engine import Conv_StringToInt
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker_SLider import ExecuteUbergraph_Widget_ColorPicker_Slider.K2Node_ComponentBoundEvent_Text
from Game.FactoryGame.Interface.UI.Material.Material_UI_ColorPicker_Saturation import Material_UI_ColorPicker_Saturation
from Script.Engine import MaterialInterface
from Script.Engine import Default__KismetStringLibrary
from Script.Engine import NotEqual_ByteByte
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker_SLider import ExecuteUbergraph_Widget_ColorPicker_Slider.K2Node_Event_IsDesignTime
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.Material.Material_UI_ColorPicker_Brightness import Material_UI_ColorPicker_Brightness
from Script.Engine import Round
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker_SLider import ExecuteUbergraph_Widget_ColorPicker_Slider.K2Node_ComponentBoundEvent_CommitMethod
from Script.UMG import GetDynamicMaterial
from Script.CoreUObject import LinearColor

class Widget_ColorPicker_Slider(UserWidget):
    OnValueChanged: FMulticastScriptDelegate
    mSliderType: uint8
    
    def UpdateSliderValue(self, Value: float):
        ReturnValue: float = Value / 360
        Variable: uint8 = self.mSliderType
        
        switch = {
            0: ReturnValue,
            1: Value,
            2: Value
        }
        self.mSlider.SetValue(switch.get(Variable, None))
        ReturnValue_0: int32 = Round(Value)
        ReturnValue_1: float = Conv_IntToFloat(ReturnValue_0)
        Variable1: uint8 = self.mSliderType
        
        switch_0 = {
            0: ReturnValue_1,
            1: Value,
            2: Value
        }
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_FloatToText(switch_0.get(Variable1, None), 0, False, True, 1, 3, 0, 2)
        self.mInputText.SetText(ReturnValue_2)
    

    def UpdateSliderMaterial(self, Hue: float, SecondaryValue: float):
        LocalHue = Hue
        LocalSecondaryValue = SecondaryValue
        CmpSuccess: bool = NotEqual_ByteByte(self.mSliderType, 1)
        if not CmpSuccess:
            goto('L149')
        CmpSuccess = NotEqual_ByteByte(self.mSliderType, 2)
        if not CmpSuccess:
            goto('L149')
        # End
        # Label 149
        ReturnValue: Ptr[MaterialInstanceDynamic] = self.SliderBackground.GetDynamicMaterial()
        ReturnValue_0: LinearColor = HSVToRGB(LocalHue, 1, 1, 1)
        ReturnValue.SetVectorParameterValue("Color", ReturnValue_0)
        ReturnValue.SetScalarParameterValue("SecondaryValue", LocalSecondaryValue)
    

    def BndEvt__Slider_0_K2Node_ComponentBoundEvent_109_OnFloatValueChangedEvent__DelegateSignature(self, Value: float):
        ExecuteUbergraph_Widget_ColorPicker_Slider.K2Node_ComponentBoundEvent_Value = Value #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorPicker_Slider(10)
    

    def BndEvt__mInputText_K2Node_ComponentBoundEvent_270_OnEditableTextBoxCommittedEvent__DelegateSignature(self, text: Const[Ref[FText]], CommitMethod: uint8):
        ExecuteUbergraph_Widget_ColorPicker_Slider.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_ColorPicker_Slider.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorPicker_Slider(575)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_ColorPicker_Slider.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorPicker_Slider(808)
    

    def ExecuteUbergraph_Widget_ColorPicker_Slider(self):
        ReturnValue: float = Value * 360
        ReturnValue_0: int32 = Round(ReturnValue)
        ReturnValue_1: float = Conv_IntToFloat(ReturnValue_0)
        Variable: uint8 = self.mSliderType
        
        switch = {
            0: ReturnValue_1,
            1: Value,
            2: Value
        }
        ReturnValue_2: FText = Default__KismetTextLibrary.Conv_FloatToText(switch.get(Variable, None), 0, False, True, 1, 3, 0, 2)
        self.mInputText.SetText(ReturnValue_2)
        ReturnValue = Value * 360
        ReturnValue_0 = Round(ReturnValue)
        ReturnValue_1 = Conv_IntToFloat(ReturnValue_0)
        Variable = self.mSliderType
        
        switch_0 = {
            0: ReturnValue_1,
            1: Value,
            2: Value
        }
        self.OnValueChanged.ProcessMulticastDelegate(switch_0.get(Variable, None))
        # End
        ReturnValue_3: bool = EqualEqual_ByteByte(CommitMethod, 1)
        if not ReturnValue_3:
            goto('L998')
        
        Text = None
        ReturnValue_4: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Text])
        ReturnValue_5: int32 = Default__KismetStringLibrary.Conv_StringToInt(ReturnValue_4)
        ReturnValue1: float = Conv_IntToFloat(ReturnValue_5)
        self.OnValueChanged.ProcessMulticastDelegate(ReturnValue1)
        # End
        Variable_0: Ptr[MaterialInterface] = Material_UI_ColorPicker_Brightness
        Variable1: Ptr[MaterialInterface] = Material_UI_ColorPicker_Saturation
        Variable2: Ptr[MaterialInterface] = Material_UI_ColorPicker_Hue
        Variable1_0: uint8 = self.mSliderType
        
        switch_1 = {
            0: Variable2,
            1: Variable1,
            2: Variable_0
        }
        self.SliderBackground.SetBrushFromMaterial(switch_1.get(Variable1_0, None))
    

    def OnValueChanged__DelegateSignature(self, Value: float):
        pass
    
