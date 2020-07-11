
from codegen.ue4_stub import *

from Script.Engine import Texture
from Script.UMG import UMGSequencePlayer
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SwitchingImage import ExecuteUbergraph_Widget_SwitchingImage
from Script.UMG import PlayAnimation
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SwitchingImage import ExecuteUbergraph_Widget_SwitchingImage.K2Node_Event_IsDesignTime
from Script.UMG import WidgetAnimation
from Script.UMG import UserWidget
from Game.FactoryGame.Interface.UI.InGame.-Shared.Widget_SwitchingImage import ExecuteUbergraph_Widget_SwitchingImage.K2Node_CustomEvent_NewTexture

class Widget_SwitchingImage(UserWidget):
    mSwitchImageAnim: Ptr[WidgetAnimation]
    mImage: Ptr[Texture] = Namespace(AssetPath='/Game/FactoryGame/Equipment/Beacon/UI/Beacon_PickupIcon.Beacon_PickupIcon')
    OnSwitchAnimationFinished: FMulticastScriptDelegate
    
    def PreConstruct(self):
        ExecuteUbergraph_Widget_SwitchingImage.K2Node_Event_IsDesignTime = IsDesignTime #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SwitchingImage(34)
    

    def EventImageSwitch(self):
        self.ExecuteUbergraph_Widget_SwitchingImage(514)
    

    def SwitchImage(self, newTexture: Ptr[Texture]):
        ExecuteUbergraph_Widget_SwitchingImage.K2Node_CustomEvent_NewTexture = newTexture #  PERSISTENT_FRAME(
        self.ExecuteUbergraph_Widget_SwitchingImage(994)
    

    def WidgetAnimationEvt_mSwitchImageAnim_K2Node_WidgetAnimationEvent_0(self):
        self.ExecuteUbergraph_Widget_SwitchingImage(10)
    

    def ExecuteUbergraph_Widget_SwitchingImage(self):
        self.OnSwitchAnimationFinished.ProcessMulticastDelegate()
        # End
        SlateBrush.ImageSize = self.mImageObject.Brush.ImageSize
        SlateBrush.Margin = self.mImageObject.Brush.Margin
        SlateBrush.TintColor = self.mImageObject.Brush.TintColor
        SlateBrush.ResourceObject = self.mImage
        SlateBrush.DrawAs = self.mImageObject.Brush.DrawAs
        SlateBrush.Tiling = self.mImageObject.Brush.Tiling
        SlateBrush.Mirroring = self.mImageObject.Brush.Mirroring
        
        SlateBrush = None
        self.mImageObject.SetBrush(Ref[SlateBrush])
        # End
        SlateBrush1.ImageSize = self.mImageObject.Brush.ImageSize
        SlateBrush1.Margin = self.mImageObject.Brush.Margin
        SlateBrush1.TintColor = self.mImageObject.Brush.TintColor
        SlateBrush1.ResourceObject = self.mImage
        SlateBrush1.DrawAs = self.mImageObject.Brush.DrawAs
        SlateBrush1.Tiling = self.mImageObject.Brush.Tiling
        SlateBrush1.Mirroring = self.mImageObject.Brush.Mirroring
        
        SlateBrush1 = None
        self.mImageObject.SetBrush(Ref[SlateBrush1])
        # End
        self.mImage = NewTexture
        ReturnValue: Ptr[UMGSequencePlayer] = self.PlayAnimation(self.mSwitchImageAnim, 0, 1, 0, 1)
    

    def OnSwitchAnimationFinished__DelegateSignature(self):
        pass
    
