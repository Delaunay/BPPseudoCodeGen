
from codegen.ue4_stub import *

from Script.Engine import Default__KismetSystemLibrary
from Game.FactoryGame.Interface.UI.HUDHelpers.HUDHelpers import Default__HUDHelpers
from Game.FactoryGame.Interface.UI.Assets.Shared.Widget_SwitchButton import ExecuteUbergraph_Widget_SwitchButton.K2Node_Event_IsDesignTime
from Script.UMG import Construct
from Script.Engine import Texture
from Script.UMG import SetRenderTranslation
from Script.CoreUObject import Vector2D
from Script.Engine import IsValid
from Game.FactoryGame.Interface.UI.Assets.Shared.ButtonLeftEnabled import ButtonLeftEnabled
from Script.UMG import SetColorAndOpacity
from Game.FactoryGame.Interface.UI.Assets.Shared.Button_RightEnabled import Button_RightEnabled
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.Assets.Shared.Widget_SwitchButton import ExecuteUbergraph_Widget_SwitchButton

class Widget_SwitchButton(UserWidget):
    OnClicked: FMulticastScriptDelegate
    mIsSending: bool
    mTextureSending: Ptr[Texture]
    mTextureReceiving: Ptr[Texture]
    
    def SetIcon(self, TextureSending: Ptr[Texture], TextureReceiving: Ptr[Texture]):
        ReturnValue: bool = Default__KismetSystemLibrary.IsValid(TextureReceiving)
        ReturnValue1: bool = Default__KismetSystemLibrary.IsValid(TextureSending)
        ReturnValue_0: bool = ReturnValue1 and ReturnValue
        if not ReturnValue_0:
            goto('L1147')
        self.mTextureSending = TextureSending
        self.mTextureReceiving = TextureReceiving
        SlateBrush1.ImageSize = self.mIconReceiving.Brush.ImageSize
        SlateBrush1.Margin = self.mIconReceiving.Brush.Margin
        SlateBrush1.TintColor = self.mIconReceiving.Brush.TintColor
        SlateBrush1.ResourceObject = self.mTextureReceiving
        SlateBrush1.DrawAs = self.mIconReceiving.Brush.DrawAs
        SlateBrush1.Tiling = self.mIconReceiving.Brush.Tiling
        SlateBrush1.Mirroring = self.mIconReceiving.Brush.Mirroring
        
        SlateBrush1 = None
        self.mIconReceiving.SetBrush(Ref[SlateBrush1])
        SlateBrush.ImageSize = self.mIconSending.Brush.ImageSize
        SlateBrush.Margin = self.mIconSending.Brush.Margin
        SlateBrush.TintColor = self.mIconSending.Brush.TintColor
        SlateBrush.ResourceObject = self.mTextureSending
        SlateBrush.DrawAs = self.mIconSending.Brush.DrawAs
        SlateBrush.Tiling = self.mIconSending.Brush.Tiling
        SlateBrush.Mirroring = self.mIconSending.Brush.Mirroring
        
        SlateBrush = None
        self.mIconSending.SetBrush(Ref[SlateBrush])
        # End
        # Label 1147
        self.mIconReceiving.SetVisibility(1)
        self.mIconSending.SetVisibility(1)
    

    def SetButtonBrush(self, mButtonState: bool):
        if not mButtonState:
            goto('L606')
        SlateBrush1.ImageSize = self.mButtonBrush.Brush.ImageSize
        SlateBrush1.Margin = self.mButtonBrush.Brush.Margin
        SlateBrush1.TintColor = self.mButtonBrush.Brush.TintColor
        SlateBrush1.ResourceObject = Button_RightEnabled
        SlateBrush1.DrawAs = self.mButtonBrush.Brush.DrawAs
        SlateBrush1.Tiling = self.mButtonBrush.Brush.Tiling
        SlateBrush1.Mirroring = self.mButtonBrush.Brush.Mirroring
        
        SlateBrush1 = None
        self.mButtonBrush.SetBrush(Ref[SlateBrush1])
        self.mIconSending.SetRenderTranslation(Vector2D(X = -6, Y = -6))
        self.mIconReceiving.SetRenderTranslation(Vector2D(X = 6, Y = 2))
        # End
        # Label 606
        SlateBrush.ImageSize = self.mButtonBrush.Brush.ImageSize
        SlateBrush.Margin = self.mButtonBrush.Brush.Margin
        SlateBrush.TintColor = self.mButtonBrush.Brush.TintColor
        SlateBrush.ResourceObject = ButtonLeftEnabled
        SlateBrush.DrawAs = self.mButtonBrush.Brush.DrawAs
        SlateBrush.Tiling = self.mButtonBrush.Brush.Tiling
        SlateBrush.Mirroring = self.mButtonBrush.Brush.Mirroring
        
        SlateBrush = None
        self.mButtonBrush.SetBrush(Ref[SlateBrush])
        self.mIconSending.SetRenderTranslation(Vector2D(X = -6, Y = 2))
        self.mIconReceiving.SetRenderTranslation(Vector2D(X = 6, Y = -6))
    

    def BndEvt__Button_2_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature(self):
        self.ExecuteUbergraph_Widget_SwitchButton(10)
    

    def Construct(self):
        self.ExecuteUbergraph_Widget_SwitchButton(57)
    

    def PreConstruct(self):
        ExecuteUbergraph_Widget_SwitchButton.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SwitchButton(209)
    

    def ExecuteUbergraph_Widget_SwitchButton(self):
        self.OnClicked.ProcessMulticastDelegate()
        self.SetButtonBrush(self.mIsSending)
        # End
        self.Construct()
        
        Text = None
        Graphics = None
        Default__HUDHelpers.GetFactoryGameDarkGray(self, Ref[Text], Ref[Graphics])
        self.mIconSending.SetColorAndOpacity(Graphics)
        self.mIconReceiving.SetColorAndOpacity(Graphics)
        # End
        self.SetIcon(self.mTextureSending, self.mTextureReceiving)
    

    def OnClicked__DelegateSignature(self):
        pass
    
