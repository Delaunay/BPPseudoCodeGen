
from codegen.ue4_stub import *

from Game.FactoryGame.Equipment.ColorGun.Widget_ColorGunUI import ExecuteUbergraph_Widget_ColorGunUI
from Script.UMG import GetViewportSize
from Script.UMG import Default__WidgetLayoutLibrary
from Script.Engine import FTrunc
from Script.Engine import Default__KismetSystemLibrary
from Script.Engine import PlayerController
from Script.FactoryGame import GetSecondaryColor
from Game.FactoryGame.Equipment.ColorGun.Equip_ColorGun import Equip_ColorGun
from Script.UMG import Default__WidgetBlueprintLibrary
from Script.Engine import SetFloatPropertyByName
from Game.FactoryGame.Equipment.ColorGun.Widget_ColorGunUI import ExecuteUbergraph_Widget_ColorGunUI.K2Node_CustomEvent_Color
from Game.FactoryGame.Equipment.ColorGun.Widget_ColorGunUI import ExecuteUbergraph_Widget_ColorGunUI.K2Node_CustomEvent_Color1
from Script.Engine import BreakVector2D
from Script.FactoryGame import FGInteractWidget
from Game.FactoryGame.Interface.UI.InGame.ColorPicker.Widget_ColorPicker import Widget_ColorPicker
from Script.Engine import RGBToHSV
from Script.Engine import SetMouseLocation
from Game.FactoryGame.Interface.UI.HUDHelpers.BPHUDHelpers import Default__BPHUDHelpers
from Script.UMG import Create
from Script.FactoryGame import GetPrimaryColor
from Script.CoreUObject import Vector2D
from Script.CoreUObject import LinearColor

class Widget_ColorGunUI(FGInteractWidget):
    mColorGun: Ptr[Equip_ColorGun]
    mUseMouse = True
    mRestoreFocusWhenLost = True
    mCallCustomTickOnConstruct = True
    
    def OnPrimaryColorPicked(self, Color: LinearColor):
        ExecuteUbergraph_Widget_ColorGunUI.K2Node_CustomEvent_Color1 = Color #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorGunUI(65)
    

    def OnSecondaryColorPicked(self, Color: LinearColor):
        ExecuteUbergraph_Widget_ColorGunUI.K2Node_CustomEvent_Color = Color #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_ColorGunUI(807)
    

    def BndEvt__mSecondaryButton_K2Node_ComponentBoundEvent_26_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorGunUI(812)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_ColorGunUI(2069)
    

    def BndEvt__mAcceptButton_K2Node_ComponentBoundEvent_1_OnClicked__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorGunUI(2329)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_21_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_ColorGunUI(2334)
    

    def OnClose(self):
        self.ExecuteUbergraph_Widget_ColorGunUI(10)
    

    def ExecuteUbergraph_Widget_ColorGunUI(self):
        self.OnEscapePressed()
        self.mColorGun.Event Clear Color Picker UI()
        # End
        # End
        # Label 70
        ReturnValue1: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue: Ptr[Widget_ColorPicker] = Default__WidgetBlueprintLibrary.Create(self, Widget_ColorPicker, ReturnValue1)
        ReturnValue_0: LinearColor = self.mColorGun.GetSecondaryColor()
        
        H = None
        S = None
        V = None
        A = None
        RGBToHSV(ReturnValue_0, Ref[H], Ref[S], Ref[V], Ref[A])
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue, "mHueValue", H)
        ReturnValue_0 = self.mColorGun.GetSecondaryColor()
        
        H = None
        S = None
        V = None
        A = None
        RGBToHSV(ReturnValue_0, Ref[H], Ref[S], Ref[V], Ref[A])
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue, "mSaturationValue", S)
        ReturnValue_0 = self.mColorGun.GetSecondaryColor()
        
        H = None
        S = None
        V = None
        A = None
        RGBToHSV(ReturnValue_0, Ref[H], Ref[S], Ref[V], Ref[A])
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue, "mValueValue", V)
        ReturnValue_1: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__BPHUDHelpers.PushStackWidget(ReturnValue_1, ReturnValue, self)
        OutputDelegate.BindUFunction(self, OnSecondaryColorPicked)
        ReturnValue.mOnColorPicked.AddUnique(OutputDelegate)
        # End
        # End
        self.mCanvasPanel.SetVisibility(1)
        goto('L70')
        # Label 855
        ReturnValue2: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue1_0: Ptr[Widget_ColorPicker] = Default__WidgetBlueprintLibrary.Create(self, Widget_ColorPicker, ReturnValue2)
        ReturnValue_2: LinearColor = self.mColorGun.GetPrimaryColor()
        
        H1 = None
        S1 = None
        V1 = None
        A1 = None
        RGBToHSV(ReturnValue_2, Ref[H1], Ref[S1], Ref[V1], Ref[A1])
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue1_0, "mHueValue", H1)
        ReturnValue_2 = self.mColorGun.GetPrimaryColor()
        
        H1 = None
        S1 = None
        V1 = None
        A1 = None
        RGBToHSV(ReturnValue_2, Ref[H1], Ref[S1], Ref[V1], Ref[A1])
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue1_0, "mSaturationValue", S1)
        ReturnValue_2 = self.mColorGun.GetPrimaryColor()
        
        H1 = None
        S1 = None
        V1 = None
        A1 = None
        RGBToHSV(ReturnValue_2, Ref[H1], Ref[S1], Ref[V1], Ref[A1])
        Default__KismetSystemLibrary.SetFloatPropertyByName(ReturnValue1_0, "mValueValue", V1)
        ReturnValue4: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__BPHUDHelpers.PushStackWidget(ReturnValue4, ReturnValue1_0, self)
        OutputDelegate1.BindUFunction(self, OnPrimaryColorPicked)
        ReturnValue1_0.mOnColorPicked.AddUnique(OutputDelegate1)
        # End
        # Label 1592
        ReturnValue3: Ptr[PlayerController] = self.GetOwningPlayer()
        Default__BPHUDHelpers.PopStackWidget(ReturnValue3, self, self)
        self.mColorGun.mColorWidget = None
        # End
        # Label 1701
        self.mCanvasPanel.SetVisibility(1)
        goto('L855')
        # Label 1744
        ReturnValue_3: Vector2D = Default__WidgetLayoutLibrary.GetViewportSize(self)
        
        X = None
        Y = None
        BreakVector2D(ReturnValue_3, Ref[X], Ref[Y])
        ReturnValue_4: float = Y / 2
        ReturnValue1_1: float = X / 2
        ReturnValue_5: int32 = FTrunc(ReturnValue_4)
        ReturnValue1_2: int32 = FTrunc(ReturnValue1_1)
        ReturnValue5: Ptr[PlayerController] = self.GetOwningPlayer()
        ReturnValue5.SetMouseLocation(ReturnValue1_2, ReturnValue_5)
        # End
        self.Widget_ColorGun_ColorPicker.mColorGun = self.mColorGun
        OutputDelegate2.BindUFunction(self, OnClose)
        self.Widget_ColorGun_ColorPicker.Widget_Window_DarkMode.OnClose.AddUnique(OutputDelegate2)
        OutputDelegate2.BindUFunction(self, OnClose)
        self.Widget_ColorGun_ColorPicker.OnAccept.AddUnique(OutputDelegate2)
        OutputDelegate2.BindUFunction(self, OnClose)
        self.Widget_ColorGun_ColorPicker.OnCancel.AddUnique(OutputDelegate2)
        goto('L1744')
        goto('L1592')
        goto('L1701')
    
