
from codegen.ue4_stub import *

from Script.Engine import Texture
from Script.Engine import EqualEqual_ByteByte
from Script.UMG import GetVisibility
from Script.FactoryGame import FGManufacturingButton
from Script.FactoryGame import SetButton
from Script.Engine import Not_PreBool
from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.InGame.Widget_GlowingFactoryButton import ExecuteUbergraph_Widget_GlowingFactoryButton
from Script.UMG import IsPressed
from Script.UMG import SetRenderTranslation
from Script.UMG import ESlateVisibility
from Script.UMG import PlayAnimation
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.InGame.Widget_GlowingFactoryButton import ExecuteUbergraph_Widget_GlowingFactoryButton.K2Node_Event_IsDesignTime
from Script.Engine import BooleanOR
from Script.UMG import Construct
from Script.UMG import WidgetAnimation
from Script.UMG import UMGSequencePlayer
from Script.CoreUObject import Vector2D

class Widget_GlowingFactoryButton(FGManufacturingButton):
    HoverAnim: Ptr[WidgetAnimation]
    mIcon: Ptr[Texture]
    IsEnabled: bool = True
    OnClicked: FMulticastScriptDelegate
    IsPressed: bool
    
    def SetEnabled(self, Enabled: bool):
        self.IsEnabled = Enabled
        if not self.IsEnabled:
            goto('L188')
        self.mButton.SetVisibility(0)
        ReturnValue: bool = self.mButton.IsPressed()
        if not ReturnValue:
            goto('L287')
        self.ButtonIcon.SetRenderTranslation(Vector2D(X = 0, Y = -3))
        # End
        # Label 188
        self.mButton.SetVisibility(3)
        self.ButtonIcon.SetRenderTranslation(Vector2D(X = 0, Y = -3))
        # End
        # Label 287
        self.ButtonIcon.SetRenderTranslation(Vector2D(X = 0, Y = -10))
    

    def GetHoveredVisibility(self):
        ReturnValue: uint8 = self.mButton.GetVisibility()
        ReturnValue_0: bool = self.IsHovered()
        ReturnValue_1: bool = EqualEqual_ByteByte(ReturnValue, 4)
        ReturnValue1: bool = EqualEqual_ByteByte(ReturnValue, 3)
        ReturnValue_2: bool = BooleanOR(ReturnValue1, ReturnValue_1)
        ReturnValue_3: bool = Not_PreBool(ReturnValue_2)
        ReturnValue_4: bool = ReturnValue_3 and ReturnValue_0
        if not ReturnValue_4:
            goto('L280')
        ReturnValue_5: uint8 = 0
        goto('L300')
        # Label 280
        ReturnValue_5 = 2
    

    def GetIdleVisibility(self):
        ReturnValue: uint8 = self.mButton.GetVisibility()
        ReturnValue_0: bool = EqualEqual_ByteByte(ReturnValue, 4)
        ReturnValue1: bool = EqualEqual_ByteByte(ReturnValue, 3)
        ReturnValue_1: bool = BooleanOR(ReturnValue1, ReturnValue_0)
        ReturnValue_2: bool = Not_PreBool(ReturnValue_1)
        if not ReturnValue_2:
            goto('L218')
        ReturnValue_3: uint8 = 0
        goto('L238')
        # Label 218
        ReturnValue_3 = 2
    

    def GetDisabledVisibility(self):
        ReturnValue: uint8 = self.mButton.GetVisibility()
        ReturnValue_0: bool = EqualEqual_ByteByte(ReturnValue, 4)
        ReturnValue1: bool = EqualEqual_ByteByte(ReturnValue, 3)
        ReturnValue_1: bool = BooleanOR(ReturnValue1, ReturnValue_0)
        if not ReturnValue_1:
            goto('L189')
        ReturnValue_2: uint8 = 0
        goto('L209')
        # Label 189
        ReturnValue_2 = 2
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_1_OnButtonReleasedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_GlowingFactoryButton(222)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_2_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_GlowingFactoryButton(364)
    

    def BndEvt__Button_0_K2Node_ComponentBoundEvent_3_OnButtonHoverEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_GlowingFactoryButton(415)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_GlowingFactoryButton(466)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_5_OnButtonPressedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_GlowingFactoryButton(1045)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_GlowingFactoryButton.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_GlowingFactoryButton(1050)
    

    def BndEvt__mButton_K2Node_ComponentBoundEvent_4_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_GlowingFactoryButton(1055)
    

    def SimulateRelease(self):
        self.ExecuteUbergraph_Widget_GlowingFactoryButton(10)
    

    def ExecuteUbergraph_Widget_GlowingFactoryButton(self):
        # Label 10
        self.NonClickedContainer.SetVisibility(0)
        self.ClickedContainer.SetVisibility(2)
        if not self.IsEnabled:
            goto('L161')
        self.ButtonIcon.SetRenderTranslation(Vector2D(X = 0, Y = -10))
        # End
        # Label 161
        self.ButtonIcon.SetRenderTranslation(Vector2D(X = 0, Y = -3))
        # End
        goto('L10')
        # Label 227
        self.NonClickedContainer.SetVisibility(2)
        self.ClickedContainer.SetVisibility(0)
        self.ButtonIcon.SetRenderTranslation(Vector2D(X = 0, Y = -3))
        # End
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.HoverAnim, 0, 1, 0, 1)
        # End
        ReturnValue1: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.HoverAnim, 0, 1, 1, 1)
        # End
        self.Construct()
        self.SetButton(self.mButton)
        # End
        # Label 500
        ReturnValue_0: bool = Default__KismetSystemLibrary.IsValid(self.mIcon)
        if not ReturnValue_0:
            goto('L1074')
        SlateBrush.ImageSize = self.ButtonIcon.Brush.ImageSize
        SlateBrush.Margin = self.ButtonIcon.Brush.Margin
        SlateBrush.TintColor = self.ButtonIcon.Brush.TintColor
        SlateBrush.ResourceObject = self.mIcon
        SlateBrush.DrawAs = self.ButtonIcon.Brush.DrawAs
        SlateBrush.Tiling = self.ButtonIcon.Brush.Tiling
        SlateBrush.Mirroring = self.ButtonIcon.Brush.Mirroring
        
        SlateBrush = None
        self.ButtonIcon.SetBrush(Ref[SlateBrush])
        # End
        goto('L227')
        goto('L500')
        self.OnClicked.ProcessMulticastDelegate()
    

    def OnClicked__DelegateSignature(self):
        pass
    
