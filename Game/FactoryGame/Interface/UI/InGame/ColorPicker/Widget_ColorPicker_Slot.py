
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Script.Engine import BreakVector2D
from Script.Engine import Not_PreBool
from Script.UMG import SetBrushTintColor
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker_Slot import ExecuteUbergraph_Widget_ColorPicker_Slot
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker_Slot import ExecuteUbergraph_Widget_ColorPicker_Slot.K2Node_Event_IsDesignTime
from Script.CoreUObject import Vector2D
from Script.UMG import SetColorAndOpacity
from Script.UMG import SetHeightOverride
from Script.UMG import SetWidthOverride
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class Widget_ColorPicker_Slot(UserWidget):
    mSize: Vector2D = Namespace(X=90, Y=90)
    mPrimaryColor: LinearColor = Namespace(A=1, B=0.09530699998140335, G=0.09530699998140335, R=0.09530699998140335)
    mSecondaryColor: LinearColor = Namespace(A=1, B=0.13541699945926666, G=0.13541699945926666, R=0.13541699945926666)
    OnClicked: FMulticastScriptDelegate
    OnHovered: FMulticastScriptDelegate
    OnUnhovered: FMulticastScriptDelegate
    mIndex: int32
    isSelected: bool
    OnEditClicked: FMulticastScriptDelegate
    
    def UpdateColors(self, PrimaryColor: LinearColor, SecondaryColor: LinearColor):
        LocalPrimaryColor = PrimaryColor
        LocalSecondaryColor = SecondaryColor
        LinearColor1.R = LocalPrimaryColor.R
        LinearColor1.G = LocalPrimaryColor.G
        LinearColor1.B = LocalPrimaryColor.B
        LinearColor1.A = 1
        self.mPrimaryColor = LinearColor1
        LinearColor.R = LocalSecondaryColor.R
        LinearColor.G = LocalSecondaryColor.G
        LinearColor.B = LocalSecondaryColor.B
        LinearColor.A = 1
        self.mSecondaryColor = LinearColor
        SlateColor1.SpecifiedColor = self.mPrimaryColor
        SlateColor1.ColorUseRule = 0
        self.mPrimary.SetBrushTintColor(SlateColor1)
        SlateColor.SpecifiedColor = self.mSecondaryColor
        SlateColor.ColorUseRule = 0
        self.mSecondary.SetBrushTintColor(SlateColor)
    

    def SetIsSelected(self, isSelected: bool):
        self.isSelected = isSelected
        if not self.isSelected:
            goto('L210')
        
        Orange = None
        OrangeText = None
        Default__HUDHelpers.GetFactoryGameOrange(self, Ref[Orange], Ref[OrangeText])
        self.mBorder.SetColorAndOpacity(Orange)
        self.mBorder.SetVisibility(0)
        self.mEditButton.SetVisibility(0)
        # End
        
        Text = None
        Graphics = None
        # Label 210
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        self.mBorder.SetColorAndOpacity(Graphics)
        self.mBorder.SetVisibility(1)
        self.mEditButton.SetVisibility(1)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_ColorPicker_Slot.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorPicker_Slot(10)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorPicker_Slot(203)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorPicker_Slot(228)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_3_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorPicker_Slot(291)
    

    def BndEvt__mEditButton_K2Node_ComponentBoundEvent_1_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorPicker_Slot(397)
    

    def ExecuteUbergraph_Widget_ColorPicker_Slot(self):
        self.UpdateColors(self.mPrimaryColor, self.mSecondaryColor)
        
        X = None
        Y = None
        BreakVector2D(self.mSize, Ref[X], Ref[Y])
        self.mSizeBox.SetWidthOverride(X)
        
        X1 = None
        Y1 = None
        BreakVector2D(self.mSize, Ref[X1], Ref[Y1])
        self.mSizeBox.SetHeightOverride(Y1)
        # End
        self.OnClicked.ProcessMulticastDelegate(self)
        # End
        self.OnHovered.ProcessMulticastDelegate(self)
        self.mBorder.SetVisibility(0)
        # End
        self.OnUnhovered.ProcessMulticastDelegate(self)
        ReturnValue: bool = Not_PreBool(self.isSelected)
        if not ReturnValue:
            goto('L417')
        self.mBorder.SetVisibility(1)
        # End
        self.OnEditClicked.ProcessMulticastDelegate(self)
    

    def OnEditClicked__DelegateSignature(self, Slot: Ptr[Widget_ColorPicker_Slot]):
        pass
    

    def OnUnhovered__DelegateSignature(self, Slot: Ptr[Widget_ColorPicker_Slot]):
        pass
    

    def OnHovered__DelegateSignature(self, Slot: Ptr[Widget_ColorPicker_Slot]):
        pass
    

    def OnClicked__DelegateSignature(self, Slot: Ptr[Widget_ColorPicker_Slot]):
        pass
    
