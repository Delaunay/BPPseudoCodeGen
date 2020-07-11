
from codegen.ue4_stub import *

from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker import Widget_ColorPicker
from Script.Engine import RGBToHSV
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorSquare import ExecuteUbergraph_Widget_ColorSquare
from Script.Engine import EqualEqual_ObjectObject
from Script.SlateCore import SlateColor
from Script.UMG import UserWidget
from Script.CoreUObject import LinearColor

class Widget_ColorSquare(UserWidget):
    mDefaultColor: SlateColor
    mColor: SlateColor
    mIndex: int32
    mColorPicker: Ptr[Widget_ColorPicker]
    
    def GetBorderColor(self):
        Variable: LinearColor = LinearColor(R = 1, G = 0, B = 0, A = 1)
        Variable1: LinearColor = LinearColor(R = 1, G = 1, B = 1, A = 1)
        ReturnValue: bool = EqualEqual_ObjectObject(self.mColorPicker.mLastClickedColorSquare, self)
        Variable_0: bool = ReturnValue
        
        switch = {
            False: Variable1,
            True: Variable
        }
        ReturnValue_0: LinearColor = switch.get(Variable_0, None)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_5_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorSquare(10)
    

    def ExecuteUbergraph_Widget_ColorSquare(self):
        self.mColorPicker.mLastClickedColorSquare = self
        
        H = None
        S = None
        V = None
        A = None
        RGBToHSV(self.mColor.SpecifiedColor, Ref[H], Ref[S], Ref[V], Ref[A])
        self.mColorPicker.mHueValue = H
        
        H = None
        S = None
        V = None
        A = None
        RGBToHSV(self.mColor.SpecifiedColor, Ref[H], Ref[S], Ref[V], Ref[A])
        self.mColorPicker.mSaturationValue = S
        
        H = None
        S = None
        V = None
        A = None
        RGBToHSV(self.mColor.SpecifiedColor, Ref[H], Ref[S], Ref[V], Ref[A])
        self.mColorPicker.mValueValue = V
    
