
from codegen.ue4_stub import *

from Script.Engine import Conv_TextToString
from Script.FactoryGame import GetFGGameUserSettings
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.Widget_OptionsSlider import ExecuteUbergraph_Widget_OptionsSlider
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.Widget_OptionsSlider import ExecuteUbergraph_Widget_OptionsSlider.K2Node_ComponentBoundEvent_Value
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.Widget_OptionsSlider import ExecuteUbergraph_Widget_OptionsSlider.K2Node_ComponentBoundEvent_Text
from Script.FactoryGame import SetFloatOptionValue
from Script.Engine import EqualEqual_FloatFloat
from Game.FactoryGame.Interface.UI.Menu.Widget_OptionValueController import Widget_OptionValueController
from Script.UMG import SetText
from Script.Engine import Conv_FloatToText
from Script.UMG import SetValue
from Script.FactoryGame import FGGameUserSettings
from Script.UMG import SetColorAndOpacity
from Script.Engine import Replace
from Script.Engine import Default__KismetTextLibrary
from Script.FactoryGame import Default__FGGameUserSettings
from Script.UMG import SetFillColorAndOpacity
from Game.FactoryGame.Interface.UI.Menu.PauseMenu.Widget_OptionsSlider import ExecuteUbergraph_Widget_OptionsSlider.K2Node_ComponentBoundEvent_CommitMethod
from Script.Engine import Default__KismetStringLibrary
from Script.FactoryGame import Default__FGBlueprintFunctionLibrary
from Script.Engine import NotEqual_ByteByte
from Script.Engine import NormalizeToRange
from Script.Engine import Conv_StringToFloat
from Script.Engine import MapRangeClamped
from Script.FactoryGame import RoundFloatWithPrecision
from Script.FactoryGame import GetFloatOptionValue
from Script.UMG import GetValue

class Widget_OptionsSlider(Widget_OptionValueController):
    mIsHovered: bool
    GetNewValue: FMulticastScriptDelegate
    mMinVal: float
    mMaxVal: float = 100
    mMinDisplayVal: float
    mMaxDisplayVal: float = 100
    MaxFractionalDigitsToDisplay: int32
    mShowZeroAsOff: bool
    
    def UpdateSliderValue(self):
        ReturnValue: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        ReturnValue_0: float = ReturnValue.GetFloatOptionValue(self.mOptionRowData.ConsoleVariable)
        self.SetNormalizedValue(ReturnValue_0)
    

    def HandleSlider(self):
        if not self.mIsDynamicOption:
            goto('L174')
        ReturnValue: Ptr[FGGameUserSettings] = Default__FGGameUserSettings.GetFGGameUserSettings()
        
        AdjustedValue = None
        self.GetAdjustedValue(Ref[AdjustedValue])
        ReturnValue.SetFloatOptionValue(self.mOptionRowData.ConsoleVariable, AdjustedValue, self.mOptionRowData.UpdateInstantly, self.mOptionRowData.RequireRestart)
    

    def SetupSlider(self):
        ExecutionFlow.Push("L264")
        ExecutionFlow.Push("L249")
        # Label 10
        ExecutionFlow.Push("L220")
        ExecutionFlow.Push("L183")
        ExecutionFlow.Push("L146")
        ExecutionFlow.Push("L109")
        ExecutionFlow.Push("L72")
        self.mMinVal = self.mOptionRowData.MinValue
        goto(ExecutionFlow.Pop())
        # Label 72
        self.mMaxVal = self.mOptionRowData.MaxValue
        goto(ExecutionFlow.Pop())
        # Label 109
        self.mMinDisplayVal = self.mOptionRowData.MinDisplayValue
        goto(ExecutionFlow.Pop())
        # Label 146
        self.mMaxDisplayVal = self.mOptionRowData.MaxDisplayValue
        goto(ExecutionFlow.Pop())
        # Label 183
        self.MaxFractionalDigitsToDisplay = self.mOptionRowData.MaxFractionalDigits
        goto(ExecutionFlow.Pop())
        # Label 220
        self.mShowZeroAsOff = self.mOptionRowData.ShowZeroAsOff
        goto(ExecutionFlow.Pop())
        # Label 249
        self.UpdateSliderValue()
        goto(ExecutionFlow.Pop())
    

    def GetDisplayValue(self):
        ReturnValue: float = self.OptionSlider.GetValue()
        ReturnValue_0: float = MapRangeClamped(ReturnValue, 0, 1, self.mMinDisplayVal, self.mMaxDisplayVal)
        ReturnValue_1: float = Default__FGBlueprintFunctionLibrary.RoundFloatWithPrecision(ReturnValue_0, self.MaxFractionalDigitsToDisplay)
        # Label 183
        DisplayValue = ReturnValue_1
    

    def SetNormalizedValue(self, CurrentUnadjustedValue: float):
        ReturnValue: float = NormalizeToRange(CurrentUnadjustedValue, self.mMinVal, self.mMaxVal)
        self.OptionSlider.SetValue(ReturnValue)
        ReturnValue_0: FText = self.GetValueText()
        self.mValueTextInput.SetText(ReturnValue_0)
    

    def GetAdjustedValue(self):
        
        DisplayValue = None
        self.GetDisplayValue(Ref[DisplayValue])
        ReturnValue: float = MapRangeClamped(DisplayValue, self.mMinDisplayVal, self.mMaxDisplayVal, self.mMinVal, self.mMaxVal)
        AdjustedValue = ReturnValue
    

    def SetProgressBarPercentage(self, Percent: float):
        self.OptionSlider.SetValue(Percent)
        ReturnValue: FText = self.GetValueText()
        self.mValueTextInput.SetText(ReturnValue)
    

    def GetProgressBarPercentage(self):
        ReturnValue: float = self.OptionSlider.GetValue()
        ReturnValue_0: float = ReturnValue
    

    def GetValueText(self):
        Variable: FText = "{'Instruction': 'EX_StringConst', 'InstOffsetFromTop': 20, 'Value': 'Off'}"
        
        DisplayValue = None
        self.GetDisplayValue(Ref[DisplayValue])
        ReturnValue: bool = EqualEqual_FloatFloat(DisplayValue, 0)
        ReturnValue_0: FText = Default__KismetTextLibrary.Conv_FloatToText(DisplayValue, 0, False, False, 1, 324, 0, self.MaxFractionalDigitsToDisplay)
        ReturnValue_1: bool = ReturnValue and self.mShowZeroAsOff
        Variable_0: bool = ReturnValue_1
        
        switch = {
            False: ReturnValue_0,
            True: Variable
        }
        ReturnValue_2: FText = switch.get(Variable_0, None)
    

    def OnInitValueController(self):
        self.ExecuteUbergraph_Widget_OptionsSlider(208)
    

    def OnRowUnhovered(self):
        self.ExecuteUbergraph_Widget_OptionsSlider(370)
    

    def OnRowHovered(self):
        self.ExecuteUbergraph_Widget_OptionsSlider(375)
    

    def BndEvt__EditableTextBox_0_K2Node_ComponentBoundEvent_0_OnEditableTextBoxCommittedEvent__DelegateSignature(self, text: Const[Ref[FText]], CommitMethod: uint8):
        ExecuteUbergraph_Widget_OptionsSlider.K2Node_ComponentBoundEvent_Text = text #  PERSISTENT_FRAME(
        ExecuteUbergraph_Widget_OptionsSlider.K2Node_ComponentBoundEvent_CommitMethod = CommitMethod #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_OptionsSlider(503)
    

    def BndEvt__OptionSlider_K2Node_ComponentBoundEvent_104_OnFloatValueChangedEvent__DelegateSignature(self, Value: float):
        ExecuteUbergraph_Widget_OptionsSlider.K2Node_ComponentBoundEvent_Value = Value #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_OptionsSlider(999)
    

    def OnOptionValueUpdated(self):
        self.ExecuteUbergraph_Widget_OptionsSlider(1004)
    

    def ExecuteUbergraph_Widget_OptionsSlider(self):
        # Label 10
        self.HandleSlider()
        
        AdjustedValue1 = None
        self.GetAdjustedValue(Ref[AdjustedValue1])
        self.GetNewValue.ProcessMulticastDelegate(AdjustedValue1)
        # End
        # Label 80
        self.mBorder.SetColorAndOpacity(self.mUnhoveredColor)
        self.mTextBackground.SetColorAndOpacity(self.mUnhoveredColor)
        self.mProgressBar.SetFillColorAndOpacity(self.mUnhoveredColor)
        # End
        self.SetupSlider()
        # End
        
        AdjustedValue = None
        # Label 227
        self.GetAdjustedValue(Ref[AdjustedValue])
        self.GetNewValue.ProcessMulticastDelegate(AdjustedValue)
        self.HandleSlider()
        ReturnValue: FText = self.GetValueText()
        self.mValueTextInput.SetText(ReturnValue)
        # End
        goto('L80')
        self.mBorder.SetColorAndOpacity(self.mHoveredColor)
        self.mTextBackground.SetColorAndOpacity(self.mHoveredColor)
        self.mProgressBar.SetFillColorAndOpacity(self.mHoveredColor)
        # End
        CmpSuccess: bool = NotEqual_ByteByte(CommitMethod, 1)
        if not CmpSuccess:
            goto('L643')
        CmpSuccess = NotEqual_ByteByte(CommitMethod, 2)
        if not CmpSuccess:
            goto('L921')
        CmpSuccess = NotEqual_ByteByte(CommitMethod, 3)
        if not CmpSuccess:
            goto('L921')
        # End
        
        Text = None
        # Label 643
        ReturnValue_0: FString = Default__KismetTextLibrary.Conv_TextToString(Ref[Text])
        ReturnValue_1: FString = Default__KismetStringLibrary.Replace(ReturnValue_0, ",", ".", 1)
        ReturnValue_2: float = Default__KismetStringLibrary.Conv_StringToFloat(ReturnValue_1)
        ReturnValue_3: float = MapRangeClamped(ReturnValue_2, self.mMinDisplayVal, self.mMaxDisplayVal, 0, 1)
        self.SetProgressBarPercentage(ReturnValue_3)
        goto('L10')
        # Label 921
        ReturnValue1: FText = self.GetValueText()
        self.mValueTextInput.SetText(ReturnValue1)
        # End
        goto('L227')
        self.UpdateSliderValue()
    

    def GetNewValue__DelegateSignature(self, NewValue: float):
        pass
    
