
from codegen.ue4_stub import *

from Script.UMG import UMGSequencePlayer
from Script.UMG import PlayAnimation
from Script.FactoryGame import GetStationName
from Script.UMG import ESlateVisibility
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Train_TimeTable_Rule import ExecuteUbergraph_Widget_Train_TimeTable_Rule.K2Node_Event_IsDesignTime
from Game.FactoryGame.Buildable.Vehicle.Train.Locomotive.UI.Widget_Train_TimeTable_Rule import ExecuteUbergraph_Widget_Train_TimeTable_Rule
from Script.UMG import SetStyle
from Script.UMG import WidgetAnimation
from Script.UMG import SetColorAndOpacity
from Script.Engine import Not_PreBool
from Script.FactoryGame import FGTrainStationIdentifier
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class Widget_Train_TimeTable_Rule(UserWidget):
    NameChange: Ptr[WidgetAnimation]
    mTitle: FText = NSLOCTEXT("", "53DFB0AC4C6FDF199AC184993D8F11DE", "Falköping C")
    OnClicked: FMulticastScriptDelegate
    mIsSelected: bool
    OnDeleted: FMulticastScriptDelegate
    mStation: Ptr[FGTrainStationIdentifier]
    OnMoveUpClicked: FMulticastScriptDelegate
    OnMoveDownClicked: FMulticastScriptDelegate
    mOrderUpVisible: bool
    mOrderDownVisible: bool
    mIsNextStop: bool
    OnSetCurrentStopClicked: FMulticastScriptDelegate
    
    def SetIsNextStop(self, mIsNextStop: bool):
        self.mIsNextStop = mIsNextStop
        Variable: uint8 = 3
        Variable1: uint8 = 2
        Variable1_0: bool = self.mIsNextStop
        
        switch = {
            False: Variable1,
            True: Variable
        }
        self.mNextStop.SetVisibility(switch.get(Variable1_0, None))
        Variable_0: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        Variable1_1: LinearColor = LinearColor(R = 0.6038280129432678, G = 0.5972020030021667, B = 0.5972020030021667, A = 0.20000000298023224)
        ReturnValue: bool = Not_PreBool(self.mIsNextStop)
        Variable_1: bool = ReturnValue
        
        switch_0 = {
            False: Variable1_1,
            True: Variable_0
        }
        self.mSetCurrentStopButton.SetColorAndOpacity(switch_0.get(Variable_1, None))
    

    def OnUnhovered(self):
        ReturnValue: bool = Not_PreBool(self.mIsSelected)
        if not ReturnValue:
            goto('L81')
        self.mBackground.SetVisibility(2)
    

    def OnHovered(self):
        self.mBackground.SetVisibility(3)
    

    def PlayNewNameAnim(self):
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.NameChange, 0, 1, 0, 1)
    

    def SetOrderButtonsVisibility(self, UpVisible: bool, DownVisible: bool):
        self.mOrderUpVisible = UpVisible
        self.mOrderDownVisible = DownVisible
        Variable2: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        Variable3: LinearColor = LinearColor(R = 0.6038280129432678, G = 0.5972020030021667, B = 0.5972020030021667, A = 0.20000000298023224)
        Variable1: bool = self.mOrderUpVisible
        
        switch = {
            False: Variable3,
            True: Variable2
        }
        self.mMoveUp.SetColorAndOpacity(switch.get(Variable1, None))
        Variable: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        Variable1_0: LinearColor = LinearColor(R = 0.6038280129432678, G = 0.5972020030021667, B = 0.5972020030021667, A = 0.20000000298023224)
        Variable_0: bool = self.mOrderDownVisible
        
        switch_0 = {
            False: Variable1_0,
            True: Variable
        }
        self.mMoveDown.SetColorAndOpacity(switch_0.get(Variable_0, None))
    

    def UpdateRule(self, mStation: Ptr[FGTrainStationIdentifier]):
        self.mStation = mStation
        ReturnValue: FText = self.mStation.GetStationName()
        self.SetTitle(ReturnValue)
    

    def SetIsSelected(self, mIsSelected: bool):
        self.mIsSelected = mIsSelected
        Variable1: bool = self.mIsSelected
        Variable: LinearColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.05951099842786789, A = 1)
        Variable1_0: LinearColor = LinearColor(R = 0.7835379838943481, G = 0.2917709946632385, B = 0.05951099842786789, A = 0)
        
        switch = {
            False: Variable1_0,
            True: Variable
        }
        SlateColor.SpecifiedColor = switch.get(Variable1, None)
        SlateColor.ColorUseRule = 0
        SlateBrush.ImageSize = self.mButton.WidgetStyle.Normal.ImageSize
        SlateBrush.Margin = self.mButton.WidgetStyle.Normal.Margin
        SlateBrush.TintColor = SlateColor
        SlateBrush.ResourceObject = self.mButton.WidgetStyle.Normal.ResourceObject
        SlateBrush.DrawAs = 3
        SlateBrush.Tiling = self.mButton.WidgetStyle.Normal.Tiling
        SlateBrush.Mirroring = self.mButton.WidgetStyle.Normal.Mirroring
        ButtonStyle.Normal = SlateBrush
        ButtonStyle.Hovered = self.mButton.WidgetStyle.Hovered
        ButtonStyle.Pressed = self.mButton.WidgetStyle.Pressed
        ButtonStyle.Disabled = self.mButton.WidgetStyle.Disabled
        ButtonStyle.NormalPadding = self.mButton.WidgetStyle.NormalPadding
        ButtonStyle.PressedPadding = self.mButton.WidgetStyle.PressedPadding
        ButtonStyle.PressedSlateSound = self.mButton.WidgetStyle.PressedSlateSound
        ButtonStyle.HoveredSlateSound = self.mButton.WidgetStyle.HoveredSlateSound
        
        ButtonStyle = None
        self.mButton.SetStyle(Ref[ButtonStyle])
        Variable_0: uint8 = 0
        Variable1_1: uint8 = 2
        Variable_1: bool = self.mIsSelected
        
        switch_0 = {
            False: Variable1_1,
            True: Variable_0
        }
        self.mBackground.SetVisibility(switch_0.get(Variable_1, None))
    

    def SetTitle(self, mTitle: FText):
        self.mTitle = mTitle
        self.mTitleObject.SetText(self.mTitle)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_Train_TimeTable_Rule.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_Train_TimeTable_Rule(35)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable_Rule(86)
    

    def BndEvt__mDeleteButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable_Rule(189)
    

    def BndEvt__mMoveUp_K2Node_ComponentBoundEvent_2_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable_Rule(214)
    

    def BndEvt__mMoveDown_K2Node_ComponentBoundEvent_3_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable_Rule(253)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_4_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable_Rule(292)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_5_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable_Rule(297)
    

    def BndEvt__mDeleteButton_K2Node_ComponentBoundEvent_6_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable_Rule(316)
    

    def BndEvt__mMoveUp_K2Node_ComponentBoundEvent_7_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable_Rule(321)
    

    def BndEvt__mMoveDown_K2Node_ComponentBoundEvent_8_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable_Rule(326)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_9_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable_Rule(331)
    

    def BndEvt__mDeleteButton_K2Node_ComponentBoundEvent_10_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable_Rule(350)
    

    def BndEvt__mMoveUp_K2Node_ComponentBoundEvent_11_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable_Rule(355)
    

    def BndEvt__mMoveDown_K2Node_ComponentBoundEvent_12_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable_Rule(360)
    

    def BndEvt__mSetCurrentStopButton_K2Node_ComponentBoundEvent_1_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable_Rule(365)
    

    def BndEvt__mSetCurrentStopButton_K2Node_ComponentBoundEvent_13_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable_Rule(370)
    

    def BndEvt__mSetCurrentStopButton_K2Node_ComponentBoundEvent_14_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_Train_TimeTable_Rule(375)
    

    def ExecuteUbergraph_Widget_Train_TimeTable_Rule(self):
        # Label 10
        self.OnSetCurrentStopClicked.ProcessMulticastDelegate(self)
        # End
        self.SetTitle(self.mTitle)
        self.SetIsSelected(self.mIsSelected)
        # Label 81
        # End
        ReturnValue: FText = self.mStation.GetStationName()
        self.SetTitle(ReturnValue)
        # End
        # Label 164
        self.OnClicked.ProcessMulticastDelegate(self)
        # End
        self.OnDeleted.ProcessMulticastDelegate(self)
        # End
        if not self.mOrderUpVisible:
            goto('L423')
        self.OnMoveUpClicked.ProcessMulticastDelegate(self)
        # End
        if not self.mOrderDownVisible:
            goto('L423')
        self.OnMoveDownClicked.ProcessMulticastDelegate(self)
        # End
        goto('L164')
        # Label 297
        self.OnHovered()
        # End
        goto('L297')
        goto('L297')
        goto('L297')
        # Label 331
        self.OnUnhovered()
        # End
        goto('L331')
        goto('L331')
        goto('L331')
        goto('L297')
        goto('L331')
        ReturnValue_0: bool = Not_PreBool(self.mIsNextStop)
        if not ReturnValue_0:
            goto('L423')
        goto('L10')
    

    def OnSetCurrentStopClicked__DelegateSignature(self, RuleWidget: Ptr[Widget_Train_TimeTable_Rule]):
        pass
    

    def OnMoveDownClicked__DelegateSignature(self, RuleWidget: Ptr[Widget_Train_TimeTable_Rule]):
        pass
    

    def OnMoveUpClicked__DelegateSignature(self, RuleWidget: Ptr[Widget_Train_TimeTable_Rule]):
        pass
    

    def OnDeleted__DelegateSignature(self, RuleWidget: Ptr[Widget_Train_TimeTable_Rule]):
        pass
    

    def OnClicked__DelegateSignature(self, RuleWidget: Ptr[Widget_Train_TimeTable_Rule]):
        pass
    
